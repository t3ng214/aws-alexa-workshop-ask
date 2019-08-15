#	Create Lex Lambda Function

Here we will create a Lambda function that has some Python code to detect 
the intent name (`GetAccountDetail`, `GetLoanDetail` and `GetLoanProducts`) 
and to return static values based on the AccountType (checking, saving) or 
LoanType (car, home) included in the intent. In a real world example we 
would have already authenticated the user using account linking and 
would write Python code to do a database lookup for the account balances.  
To get a whole picture better, let’s build the function with hard code 
account balances first and leave authorization to the final step. 

1. Use the AWS Console to navigate to Lambda

1. Click on the orange **Create function** button, If you have not created any Lambda
function before, you may see the Get Started page

1. Select **Author from scratch** option
    ![](../img/workshop/create-lambda-function.png)

1. Let’s give our function the name of `bot-personal-assistant`. Feel free to choose 
a different name.

1. Choose **Python 2.7** as the Runtime

1. Under **Permission***, select **Create new role from AWS policy templates**. 

1. Enter `bot-personal-assistant-lambda-role` for role name and leave the policy 
template empty.
    ![](../img/workshop/author-from-scratch.png)

1. Click **Create Function** button

1. Scroll down to the integrated Cloud9 editor on the Lambda console.
    ![](../img/workshop/function-code.png)

1. Download the lambda function code [lex-lambda-personal-banker.py](../workshop/lex-lambda-personal-banker.py). 
Copy and paste the code into the inline editor (while making sure to overwrite/delete any 
template code that is already in the code box). Take a few minutes to review the code. 
Please note if you named your intents differently, you will have to update the 
dispatch method accordingly.

1. We are not going to configure any trigger now, so click ‘Save’ on the top right hand 
corner of the page. You should see a message like this.
    ![](../img/workshop/congratulations.png)
 

Next, [Link Lex bot with the Lex Lambda function](../doc/create-lex-bot-with-lambda.md).