# Chat with Lex Bot & Publish it 

## Chat with Lex Bot

1. Start by typing `What is my checking account balance?`
(or press the microphone button and ask your question using your computer mic). 
You should get an answer. 

1. Then type `What is my home loan balance?` (or ask using your mic). Notice that 
Lex is able to recognize that you are wanting to trigger the GetLoanDetail 
intent even though what you typed - What is my home loan balance?”, 
which did not exactly match the sample utterance that you configured the intent 
with which was “Get my {LoanType} loan balance”. 

1. Type `more loan info` and see how Lex returns information on the current, 
new home loan rate. In this case, because we didn’t set the ‘slot’ to be required, 
we did not need to specify whether we were looking for more information on car or 
home loans … Lex returned information on the loan type (in this case, home) that 
we had just asked about.


## Publish the Lex Bot
1. Go to **Setting** tab 
    ![](../img/workshop/setting-tab.png)

1. Enter `UAT` in **Alias Name**

1. Choose **Latest** as Bot version

1. Click the **blue "+" button**
    ![](../img/workshop/publish.png)
    
1. Click **Publish**
   
1. Choose the created alias, click **Publish** to continue

Next, [Bring Lex Bot to Web](../doc/bring-lex-to-web.md). This is an optional step,
if you only want to create Alexa Skill, you can navigate to 
[Export the Bot to Alexa Skills Kit](../doc/export-bot-to-alexa-skill.md)