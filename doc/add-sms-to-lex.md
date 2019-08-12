#	Add SMS Notification to Lex 

##	Add SMS Notification to Lex 

In this lab, you will learn the basic to configure the Lex bot to send SMS to anybody. 

1.	Just like the previous section, go Lex, open the bot you just created, we will create a new intent: SendToMyMobile. Click the “Create Intent” button.
2.	Our next intent enables the user to send their balance info to their phone number, so name this intent “SendToMyMobile” then click “Add”.
3.	Now want to provide samples of what our user would type or say to perform this action. Make sure you do not add a question mark at the end of the phrase. 
•	balance to my mobile
4.	Next, we will define two new slots to process this request this time. 
5.	For ‘Slot type name’, enter ‘AccountType’, select ‘AccountType’ in the ‘Slot type’ dropdown. In the prompt, enter ‘for which account type?’. Once done, hit the blue “+” sign.
6.	Enter ‘PhoneNumber’ in the next ‘Slot type name’, select ‘AMAZON.PhoneNumber’ in the ‘Slot type’. In the prompt, enter ‘what is your phone number’. Once done, hit the blue “+” sign again.  
![](../img/workshop/optional-6.png)

7.	Scroll down and click “Save Intent”.
8.	Next, we will create the lambda function. Download the code lex-lambda-send-sms.py. And follow the steps in the previous section Create a Lambda function and give the function name ‘sendLexSms’.
9.	Go back to your Personal Banker in  the Lex Console.
10.	Make sure you select the correct “SendToMyMobile” Intent.
11.	Scroll down to ‘Fulfillment’, select “AWS Lambda function’, choose ‘sendLexSms’ and click ‘Ok’.
12.	Next, we will create a custom IAM policy. Remember that you create a ‘Lex’ IAM Role while creating the first Lambda function. 
13.	Go to IAM.
14.	Select Roles and find the ‘Lex’ IAM role.
15.	Click on “Add inline policy” at the bottom right of the table.
16.	And copy the IAM policy from this file lex-sms-iam-incline-policy.json and paste them in this IAM policy. 
![](../img/workshop/iam-policies.png)
17.	Once you are done in IAM, go back to Lex Console.
18.	Click “Build” and then click “Build” again on the confirmation screen.
19.	Time to test our new bot. And start by entering “Get balance to my mobile number”. When you are prompted to key in your mobile, enter your 8 digit phone number (without +65). 
![](../img/workshop/optinal-19.png)
