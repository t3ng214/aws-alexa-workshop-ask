# Create the Lex Bot Manually

**This section is optional**. You can either choose to create Lex bot manually in this section, or go to 
[Step 2.Use Lex Import Function to Create a Lex Bot without Manually Creating Intents](create-intent-using-lex-import.md) 
directly. 

## Create an Intent
1. Log in to [AWS Lex Console](https://console.aws.amazon.com/lex)

1. If you have never created a bot, click **Get Started**

1. Choose **Custom bot**

1. Our **bot name** will be `PersonalBanker`

1. Choose your preferred **Output Voice**

1. **Session timeout** should be 5 minute

1. Choose “No” to the Children’s Online Privacy Protection Act (COPPA) question

1. Click **Create** to continue
    ![](../img/workshop/create-lex-bot.png)

1. We will start by creating an intent, which represents an action that the user wants 
to perform. For example, we’re going to create three intents in this lab for different 
actions a user can perform: Get Account Details; Get Loan Details; Get Loan Products. 
Under the **Editor** tab, Click **Create Intent** button.

1. In the window that pops-up click the **Create new intent** link.
    ![](../img/workshop/add-intent.png)

1. Our first intent enables the user to get account details, enter name `GetAccountDetail` 
for **Intent Name**, then click **Add** to continue
    ![](../img/workshop/create-intent.png)

1. We now want to provide samples of what our user would type or say to perform this 
action (i.e. to activate this intent). Under **Sample utterances**, 
**type the below phrases and hit [enter] or click the blue “+” sign after each phrase**. 
Make sure you do not add a question mark at the end of the phrase as this will cause build 
issues later on. NOTE: {AccountType} represents a ‘slot’ which is information that we need 
to process the users request. Type it exactly as shown above with the braces, and in the
next step we will define the ‘AccountType’ slot and list the acceptable values (checking, savings). 
Once the lab is complete, the user will interact with our bot by saying something like “What is 
my checking balance”.               
    - `What is my {AccountType} balance`
    - `{AccountType} account balance`
    ![](../img/workshop/personal-banker.png)

1. Next we define a slot which is information we need to process the users request. This 
information can be included in the utterance (query) that the user types or says, and if 
not included, Lex will prompt the user for the information. While Lex includes many built-in 
slot types (such as number, color, city, food, etc), in this case we want to define a custom 
slot to get the account type that the user is referring to. Click on the **blue “+” button** 
under “Slot types” on the left navigation bar, and click **Create slot type** to continue

1. For **Slot type name** enter `AccountType` and input an optional description

1. For Value, we want to allow the user to make queries against either their `checking` 
or `saving` account, so enter those as values, clicking the blue “+” sign after each word.
    ![](../img/workshop/add-slot-type.png)

1. Click **Add slot to intent**

1. Change the **Name** to `AccountType` so that it matches the slot name that we specified when 
we created the sample utterances.

1. Specify `What type of account?` for the **Prompt**. This prompt will be used by our bot if the 
user does not specify an account type when asking a question.
    ![](../img/workshop/get-account-detail.png)

1. Scroll down and click “Save Intent”

1.	Let’s build this simple Bot: Hit the grey **Build** button at the top right corner. You will be 
asked for confirmation to build. Click **Build** to continue.  The build process takes approximately 
a minute. Once complete, you can ask your bot a question as a way to test it. For example, you 
could type `what is my checking balance?` in the chat window. At this stage since we have not added 
in the backend Lambda function, the response will be that the bot is ready for fulfillment.

> If at any point you made a mistake in the steps above, selecting the “Latest” version of the intent 
  at the top, next to the intent name, will allow you to edit your choices.

## Add More Intents

Let’s add 2 more intents and one more slot type. 

1. Click the **blue “+” button** next to “Intents” on the left hand side of the page, 
then click **Create new intent**. 

1. This intent will allow users to get information on their outstanding home or car loan 
balance, so set the name to `GetLoanDetail` then click **Add**

1. For sample utterances (the things we expect out users to type/say to our bot to trigger
a specific intent/action), add the following phrase then click the **blue “+”** at the end of 
the sample utterance box
    - `Get my {LoanType} loan balance`
    
1. Now we’ll create a new slot type which we’ll use to store a response from the user as to 
whether they are wanting the intent to access their car loan balance or their home loan balance. 
Click the **blue “+” button** under ‘Slot types’ on the left hand side of the screen

1. For **Slot type name** enter `LoanType` and optionally provide a description

1. Enter the following two options as values:
    - car
	- home
	
1. Click **Add slot to intent**

1. Change the name of the slot from “slotOne” to “LoanType” 

1. Provide a **prompt**, for example such as `Which loan account?`

1. Make sure that the **Required** column is selected
    ![](../img/workshop/get-loan-product.png)

1. Click **Save Intent**. Now we’ll add a final intent to allow users to get more information on the loan products that we have. 

1. Click the **blue “+” button** next to “Intents” on the left hand side of the page, then click **Create new intent**
 
1. Set the name of the intent to `GetLoanProducts` then click **Add**

1. For sample utterances, add the following two phrases. Make sure not to include 
punctuation (such as comma’s or question marks). The “More loan info” utterance will 
be used as a follow-up after a user has asked for information on their outstanding 
loan balance.
    - `What is the rate on the {LoanType} loan`
    - `More loan info`
    
1. Add a slot (this allows us to get the loan type that the user wants to query) with the following values
    - Name: `LoanType`
    - Slot Type: `LoanType` (select from the drop-down list)
    - Prompt: `Which loan type?`

1. Click the **blue “+” button** to the right of the Slots information to add this slot to the intent

1. Click **Save Intent**

36.	Click **Build**, and click **Build** again when prompted for confirmation

Our bot is almost ready. all it needs now is a smart backend.
