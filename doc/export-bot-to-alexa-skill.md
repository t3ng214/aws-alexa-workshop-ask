#	Export the Bot to Alexa Skills Kit

## Export the Bot to Alexa Skills Kit / Lex Format

1. Go to [AWS Lex Console](https://console.aws.amazon.com/lex)

1. Click on the Left Arrow on the top left corner
    ![](../img/workshop/step8-export-bot.png)

1. Select your bot and click on **Action**
    ![](../img/workshop/step8-lex-action.png)

1. Click on **Export**

1. Choose the bot version and **platform** as `Alexa Skills Kit(ASK)`. Click on **Export**, save the file
    ![](../img/workshop/step8-export-bot-ASK.png)

1. Unzip the downloaded file and you will get the .json file. This will be used for 
Alexa Skill later. You can also export it as Lex format. The exported file can be 
used to replicate the same bot in another account.

> Note: You could use [json formatter](https://jsonformatter.curiousconcept.com/) to convert the file to 
> standard indented json if the file's original indents is not perfect

## Import Lex Intents to Alexa Voice Interface 

1. Go to the [Alexa Developer Console](https://developer.amazon.com/alexa/console/ask)

1. If you don't already have an account, you will be able to create a new one for 
free. Note it's not the same account for amazon.com. Sign in with your developer account

1. From the Alexa Skills Console select the **Create Skill** button near the top-right of the 
list of your Alexa Skills.  
    ![](../img/workshop/create-skill.png)

1. Input **Skill Name**, `Personal Banker`. This is the name that will be shown in the 
Alexa Skills Store, and the name your users will refer to. Also change the locale if so 
desired. Click Next to continue
    ![](../img/workshop/create-new-skill.png)

1. Select the **Custom** button to add it to your skill, and select the **Create Skill** 
button at the top right.
    ![](../img/workshop/custom-skill.png) 

1. You can choose to build the Interaction Model for your skill by adding intents, 
slots and etc. manually which we have already done in Lex. So we are going to re-use our 
Lex intents, slots. Choose **Start from scratch**, click **Choose**

1. On the left hand navigation panel, select the **JSON Editor** tab under **Interaction Model**. 
In the textfield provided, replace code line 5 to 27 with the code in the zip 
file exported from Lex. Follow the instruction below.
    - Select code line 5 to 23, delete it.
    ![](../img/workshop/json-editor.png)

    - Open the .zip file you export from Lex in Visual Studio or any other text edit file. 
    (If you find it is hard to follow, replace the entire code in the textfield 
    provided with alexa-developer-console-personal-banker.json. Then you can 
    skip subsequent jump to step 8.)

    - Select the highlighted part below. Copy it. 
    ![](../img/workshop/9-7-c.png) 

    - Paste it back to the Alexa console after line 4.
    
    - Input a **invocation name** `personal banker` as shown below. 
    ![](../img/workshop/9-7-e.png)

1. Click on **Save Model** and then **Build Model**. You should notice that Intents and 
Slot Types will auto populate based on the JSON Interaction Model that you have now 
applied to your skill

1. If your interaction model builds successfully, proceed to the next step. 
If not, you should see an error. Try to resolve the errors. In our next step 
of this guide, we will be creating our Lambda function in the AWS developer 
console, but keep this browser tab open, because we will be returning here.

Next, [Create a Lambda function for Alexa](../doc/create-lambda-for-alexa.md)]