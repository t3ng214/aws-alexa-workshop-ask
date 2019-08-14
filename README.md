#	Hands-on Workshop on Learning how to Create Amazon Alexa Skills and Amazon Lex bot


##	Pre-requisites
1.	Please [open an AWS account](https://aws.amazon.com ). You need a valid credit card to set up your account. 
**Please use us-east-1 (virginia) for this lab**

2.	Please create an Amazon Developer account. 
Go to the https://developer.amazon.com/ create an account for free.

3.  **[IMPORTANT]Please download Alexa APP using global Apple Store accounts or Google play** . 
*	For Apple users, you won't be able to find the APP if you are using Chinese Apple store account. Do use global accounts.
*	For google play users, you will need VPN to download the APP and change country setting to anything but China and stop GPS to enable the APP. If the country setting and GPS location is still China, you will meet timeout error whenever you open the APP. 

##	Table of Contents
1.	[Create the Lex Bot Manually](doc/create-lex-bot-manually.md)
2.	[Use Lex Import Function to Create a Lex Bot without Manually Creating Intents](doc/create-intent-using-lex-import.md)
3.	[Create Lex Lambda Function](doc/create-lex-lambda-function.md)
4.	[Link Lex bot with the Lex Lambda function](doc/create-lex-bot-with-lambda.md)
5.	[Chat with Lex Bot & Publish it](doc/chat-with-lex-bot-and-publish.md)
6.	(optional) [Bring Lex Bot to Web](doc/bring-lex-to-web.md)
7.	[Export the Bot to Alexa Skills Kit](doc/export-bot-to-alexa-skill.md)
8.	[Create a Lambda function for Alexa](doc/create-lambda-for-alexa.md)
9.	[Add Account Linking For Alexa](doc/account-linking-for-alexa.md)
10. (optional) [Add SMS Notification to Lex](doc/add-sms-to-lex.md)

##	Tips

* **[IMPORTANT] Please use us-east-1 (virginia) for this lab**, as the CloudFormation template used in 
[Export the Bot to Alexa Skills Kit](doc/export-bot-to-alexa-skill.md) is located in us-east-1. 
Choosing other regions is ok if you skip [Bring Lex Bot to Web](doc/bring-lex-to-web.md).

* Step 1 and step 2's function is the same, the only difference is whether to create the intents manually or not. Choose your preferred one is ok. But if you are interested, you could experience both steps and compare the difference.

*	You could find [all the code files related to this lab here](./workshop).

##	Overview

In general, the lab covers two parts. The first part is to about Lex, **step 1-6 is to demo the usage of Lex together with other services like lambda function, cognito etc. Step 7-10 is the hands on lab on Alexa**. The reason why we introduces these two services together is they are highly relative. Amazon Lex uses the same deep learning technologies that power Amazon Alexa and we could export Lex settings directly to enable Alexa skills.

**Amazon Lex**

Amazon Lex is a service for building conversational interfaces into any application using voice and text. Amazon Lex provides the advanced deep learning functionalities of automatic speech recognition (ASR) for converting speech to text, and natural language understanding (NLU) to recognize the intent of the text, to enable you to build applications with highly engaging user experiences and lifelike conversational interactions. With Amazon Lex, the same deep learning technologies that power Amazon Alexa are now available to any developer, enabling you to quickly and easily build sophisticated, natural language, conversational bots (“chatbots”). This lab is designed to demonstrate how to create a new bot including defining intents and slots. This lab will walk you through the following:

*	Creating a Lex bot
*	Adding intents
*	Adding slot types
*	Using Lambda as the back-end logic for Lex

**Amazon Alexa**

Alexa is Amazon’s cloud-based voice service available on tens of millions of devices from Amazon and third-party device manufacturers. With Alexa, you can build natural voice experiences that offer customers a more intuitive way to interact with the technology they use every day. Our collection of tools, APIs, reference solutions, and documentation make it easy for anyone to build with Alexa. This lab include:

*	Creating Alexa Voice Interface
*	Using Lambda as the back-end logic
*	Testing of Alexa skill
*	Alexa linking account 

###	Amazon Alexa Demo
After the lab, you will be able to build a smart banking system skill that could be used on Alexa APP or any Echo devices. Talk to any Echo device and Say, “open personal banker” to start the skill. 

##	Conclusion
In this lab you have learned the basic operations to manage a Lex bot and Alexa skill. Time to create your own bot and Alexa skill. 


##	Resources
* The files you need for this workshop are all here 
https://workshop-public-folder.s3.amazonaws.com/index.html
* [Speech Synthesis Markup Language (SSML) Reference](https://developer.amazon.com/docs/custom-skills/speech-synthesis-markup-language-ssml-reference.html)
* [Alexa Github](https://github.com/alexa/)

