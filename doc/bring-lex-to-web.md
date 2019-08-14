# Bring Lex Bot to Web

In this lab, you will create a web interface that can be integrated with your 
Lex bot. This interface allows you to interact with a Lex bot directly from a 
browser using text or voice. You will be using AWS CloudFormation to create 
this web interface. **Please use us-east-1** as the CloudFormation is in us-east-1.

1. Go to [GitHub repo: aws-lex-web-ui](https://github.com/awslabs/aws-lex-web-ui )

1. Go to Getting Started section, click **Launch Stack** 
    ![](../img/workshop/cloudformation-get-start.png)
 
1. You will be brought to CloudFormation service page. If you are asked to login to AWS console, do so.
    ![](../img/workshop/template.png)

1. Click on Next

1. Scroll down. You need to change a few parameters here.
    - Enter `PersonalBanker` into the **BotName**. This must be the exact name of your bot.
    - Delete the text in **WebAppConfBotInitialText** field, and 
    enter `You can ask me for your account info`. Just type 
    `What is my checking account balance` or `click on the mic and say it`
    - Delete the text in **WebAppConfBotInitialSpeech** field, and 
    enter `Say "What is my checking account balance" to get started.`
    - Delete the text in **WebAppConfToolbarTitle** field, and enter `Personal Banker`
    ![](../img/workshop/cloudformation-configuration.png)

1. Click on **Next**

1. Click on **Next** again

1. Tick “I acknowledge that AWS CloudFormation might create IAM resources with custom names.” 
and "I acknowledge that AWS CloudFormation might require the following capability." And 
click on **Create stack**
    ![](../img/workshop/cloudformation-knowledge.png)

9. It may take a few minutes. Click on the refresh button on the top right corner to see the 
progress
    ![](../img/workshop/cloudformation-output.png)

1. Once the stacks are created. The status column will show green text

1. Click on **lex-web-ui**, go to the **Output** section. You need to expand this section 
if needed.
    ![](../img/workshop/output.png)

1. Click on **WebAppUrl**

1. Adjust your browser to an appropriate size and start chatting with your bot or speak to it.

Next, [Export the Bot to Alexa Skills Kit](../doc/export-bot-to-alexa-skill.md)