from AlexaBaseHandler import AlexaBaseHandler
import os
import requests
import inflect
import time
from datetime import datetime as date
import json
from uuid import uuid4
import pytemperature
import boto3
#from yahoofinancials import YahooFinancials as Share



class AlexaLogicHandler(AlexaBaseHandler):
    """
    Sample concrete implementation of the AlexaBaseHandler to test the
    deployment scripts and process.
    All on_ handlers call the same test response changing the request type
    spoken.
    """

    #def __init__(self):
     #   super(self.__class__, self).__init__()

    def _test_response(self, title, output, msg):
        session_attributes = {}
        card_title = title
        card_output = output
        speech_output = msg
        # If the user either does not reply to the welcome message or says something
        # that is not understood, they will be prompted again with this text.
        reprompt_text = "sorry, what did you say?"
        should_end_session = False

        speechlet = self._build_speechlet_response(
            card_title, card_output, speech_output, reprompt_text,
            should_end_session)

        return (self._build_response(session_attributes, speechlet))

    # utterance "..introduce yourself"
    def say_introduction(self, intent, session):
        
        requests.packages.urllib3.disable_warnings()

        location = os.environ['WEATHER_LOCATION'] # can be any capital city
        r = requests.get(
            "http://api.openweathermap.org/data/2.5/weather?q={0},AU&appid={1}".format(location,os.environ['OPENWEATHER_APIKEY']),
            verify=False)
        weather = r.json()
        
        temp_raw = weather["main"]["temp"] # in Kelvin
        temp_clean = round(pytemperature.k2c(temp_raw),1)

        session_attributes = {}
        day = date.today().strftime("%A")
        card_title = "Introducing myself"
        
        message = "Hello! Thank you for allowing me to introduce myself. My name is Alexa and it's a pleasure to meet you today in {0}, and I hope you are having a fantastic {1}. In case you were wondering, the weather outside is currently {2} degrees celcius.".format(location,day,temp_clean)
        
        card_output = "Greetings! I'm the Bank of Alexa"
        speech_output = message
        # If the user either does not reply to the welcome message or says something
        # that is not understood, they will be prompted again with this text.
        reprompt_text = "I am sorry, can you repeat your request?"
        should_end_session = True

        speechlet = self._build_speechlet_response(
            card_title, card_output, speech_output, reprompt_text,
            should_end_session)

        return (self._build_response(session_attributes, speechlet))

    def interact_bank_account(self,method,payload):
        requests.packages.urllib3.disable_warnings()
        print ("accessing API GW for bank account details")
        if method == "GET": # retrieving account balance
            url = os.environ['BANKOFALEXA_APIGW']
            r = requests.get(url)
            return (r.json())
        elif method == "POST": # when sending updated values to DDB
            """
                Using Boto3 client instance instead to use update_item method to retain transaction data
            """
            print ("the payload used for boto: {}".format(payload))
            client = boto3.client("dynamodb","us-east-1")
            myKey = {'account_type': {"S": str(payload["account_type"])}}
            myVal = {':b': {"S": str(payload["balance"])}}
            response = client.update_item(                                                                           
                TableName = "BankOfAlexa",                                                                                 
                Key = myKey,                                                                                                
                UpdateExpression = "SET balance = :b",                                                                     
                ExpressionAttributeValues=myVal                                                                            
            ) 
            return (response)
        else:
            message = "error encountered at interact_bank_account as method: {} is not supported".format(method)
            print (message)
            return (message)

    def _welcome(self):
        session_attributes = {}
        card_title = "Welcome to the Bank of Alexa"
        message = "Welcome to the Bank of Alexa. Please authenticate by saying, my passcode is, followed by your 4 digit security code"
        card_output = "Please authenticate using your 4 Digit Code"
        speech_output = message

        # the user either does not reply to the welcome message or says something
        # that is not understood, they will be prompted again with this text.
        reprompt_text = "I am sorry, can you repeat your request?"
        should_end_session = False

        speechlet = self._build_speechlet_response(
            card_title, card_output, speech_output, reprompt_text,
            should_end_session)

        return (self._build_response(session_attributes, speechlet))

    # utterance ".. how much is in my X account? (slots: debit, mortgage, credit, savings)"
    def _get_balance(self, intent, session):
        session_attributes = session["attributes"]
        card_title = "Current Account Balance"
        card_output = ""
        should_end_session = False
        balance = 0.00
        account_summary = self.interact_bank_account("GET",None)
        valid_types = [x['account_type']['S'] for x in account_summary]
        
        try:
            if 'Account' in intent['slots']:
                account_type = intent['slots']['Account']['value']

                if account_type in valid_types:
                    for acc in account_summary:
                        if account_type == acc['account_type']['S']:
                            balance = float(acc['balance']['S'])
                            balance_arr = self._format_currency(balance)
                            p = inflect.engine()
                            message = "You have %s dollars and %s cents in your %s account." % (p.number_to_words(balance_arr[0]), balance_arr[1], account_type)
                            speech_output = message
                            card_output = message
                            reprompt_text = "You can ask me a balance to retrieve by saying for example, What is my savings account balance?"
                else: # when value given foro account type does not match existing intent slot values
                    message = "I'm sorry, I was unable to detect the type of account you are after. I can support debit, mortgage, credit and savings"
                    card_output = "Unable to detect valid account type"
                    speech_output =  message
                    reprompt_text =  "I'm sorry, I was unable to detect the type of account you are after. I can support debit, mortgage, credit and savings"
        except Exception as e:
            print ("Exception caught on _get_balance as: {0}".format(e))
            message = "I'm sorry, I was unable to detect the type of account you are after. I can support debit, mortgage, credit and savings"
            speech_output =  message
            reprompt_text =  message
            card_title = "Uh-Oh"
            card_output = "Computer says no."


        speechlet = self._build_speechlet_response(
            card_title, card_output, speech_output, reprompt_text,
            should_end_session)

        return (self._build_response(session_attributes, speechlet))

    def _format_currency(self, balance):
        balance_str = "%.2f" % balance
        balance_arr = balance_str.split(".")

        if balance_arr[1] == "00":
            balance_arr[1] = "0"
        return (balance_arr)


    # utterance ".. what accounts do I have?"
    def _list_account(self, intent, session):
        session_attributes = session["attributes"]
        card_title = "Listing my accounts"
        message = "You have a debit, mortgage, credit and a savings account. " #lazy
        card_output = "Debit, Mortage, Credit and Savings"
        should_end_session = False
        # should really get list from slots, not hard coding..        
        speech_output = message
        reprompt_text = "I am sorry, I didnt catch that, can you please repeat your request"

        speechlet = self._build_speechlet_response(
            card_title, card_output, speech_output, reprompt_text,
            should_end_session)

        return (self._build_response(session_attributes, speechlet))

    
    def _end_session(self, intent, session):
        session_attributes = {}
        card_title = "Goodbye"
        message = "Thank you for using the bank of Alexa. We will miss you, please come back soon"

        card_output = "Thank you and goodbye!"
        reprompt_text = "I am sorry, can you repeat your request?"
        speech_output = message
        should_end_session = True
        speechlet = self._build_speechlet_response(
            card_title, card_output, speech_output, reprompt_text,
            should_end_session)

        return (self._build_response(session_attributes, speechlet))

    # utterance "..say hello/hi"
    def _say_hello(self, intent, session):
        session_attributes = {}
        card_title = "Hello"
        message = "Hello. I am the Bank of Alexa. I can help you with your personal banking."
        card_output = "Hi. Let's get started."
        reprompt_text = "I am sorry, can you repeat your request?"
        speech_output = message
        should_end_session = False
        speechlet = self._build_speechlet_response(
            card_title, card_output, speech_output, reprompt_text,
            should_end_session)
        return (self._build_response(session_attributes, speechlet))

    def _set_passCode(self, intent, session):
        session_attributes = {}
        card_title = "Setting PassCode"
        card_output = ""
        reprompt_text = "I am sorry, can you repeat your request?"
        speech_output = ""
        should_end_session = False
        
        try:
            if 'passCode' in intent['slots']:
                passCode = str(intent['slots']['passCode']['value'])
                print ("user passed passCode: {0}".format(passCode))
                # change | to do cloudformation set env var on lambda
                myPassCode = os.environ['AUTHENTICATION_PASSCODE']
                # change | set session data in dynamodb
                if passCode == myPassCode:
                    # this session attribute is used later to authenticate requests
                    session_attributes = {
                        "passCode": passCode
                    }
                    message = "Thank you. You have successfully authenticated and may now interact with your account."
                    card_output = "Successfully Authenticated."
                else:
                    message = "Sorry, that is not a valid passcode. Please try authenticating again by saying, my passcode is, followed by your 4 digit security code."
                    card_output = "Incorrect Passcode."
            speech_output = message
            
        except Exception as e:
            print ("Exception caught on _set_passCode as: {0}".format(e))
            speech_output = "Sorry. I was unable to detect a valid passCode. Please try again."
            card_title = "Invalid Passcode"
            card_output = "Invalid Passcode" 
        
        speechlet = self._build_speechlet_response(
        card_title, card_output, speech_output, reprompt_text,
        should_end_session)
        return (self._build_response(session_attributes, speechlet))

    def _get_passCode(self, session):
        
        print ("Checking if session is authenticated")
        try:
            data = session["attributes"]["passCode"]
            print ("Detected an authenticated session: {0}".format(data))
            return (True)
        except Exception as e:
            print ("Unable to detect authenticated session: {0}".format(e))   
            return (False)

    def on_processing_error(self, event, context, exc):
        print ("processing error")
        return (self._test_response("processing error", "processing error", "processing error as: {}".format(exc)))

    def on_launch(self, launch_request, session):
        return (self._welcome())

    def on_session_started(self, session_started_request, session):
        return (self._test_response("session started", "session started", "on session started"))

    def on_intent(self, intent_request, session):
        intent = intent_request['intent']
        intent_name = intent_request['intent']['name']
        print ("detected intent: {}".format(intent_name))

        if self._get_passCode(session) is False: # not an authenticated session, only allow some intents
            print ("UnAuth session. Selecting routing from available intents")
            if intent_name == "CopIntent":
                return (self._say_hello(intent, session))
            elif intent_name == "SayHelloIntent":
                return (self.say_introduction(intent, session))
            elif intent_name == "AuthenticateIntent":
                return (self._set_passCode(intent, session))
            elif intent_name == "EndSession":
                return (self._end_session(intent, session))
            else:
                return (self._test_response("No matching intent", "No matching intent", "Sorry, I wasn't able to detect an authenticated session. Please try authenticating first by saying, my passcode is, followed by your 4 digit security code."))
        else: # authenticated session
            print ("Authenticated session. Selecting routing from available intents")
            # Dispatch to your skill's intent handlers
            if intent_name == "BalanceIntent":
                return (self._get_balance(intent, session))
            elif intent_name == "ListAccountIntent":
                return (self._list_account(intent, session))
            elif intent_name == "EndSession":
                return (self._end_session(intent, session))
            elif intent_name == "CopIntent":
                return (self._say_hello(intent, session))
            elif intent_name == "SayHelloIntent":
                return (self.say_introduction(intent, session))
            elif intent_name == "AuthenticateIntent":
                return (self._set_passCode(intent, session))
            else:
                return (self._test_response("Unable to find matching intent", "Unable to find matching intent", "on intent"))
                
    def on_session_ended(self, session_end_request, session):
        return (self._test_response("session ended", "session ended", "on session end"))
