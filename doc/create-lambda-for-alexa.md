# Create a Lambda function for Alexa

1. Go to [AWS Console](https://console.aws.amazon.com/lambda/home)

1. Click the orange **Create function** button. It should be near the top of your screen.

1. Click the radio button in the box titled "Browse serverless app repository". We have created 
an application in the repository as a shortcut to getting everything set up for your skill.

1. Enter **fact** to search for the application repository named `alexa-skills-kit-nodejs-factskill`. 
Enter the full name into the search box if you need to narrow the search results.

1. Click on the application. This template will create the Lambda function, grant the Alexa Skills 
Kit permission to invoke it, and set up an IAM role for you. It will also add the 
code from this GitHub repo and include the required dependencies so that you don't 
have to upload them yourself.

1. Change the application name and then Click the **Deploy** button at the bottom of the page.
    ![](../img/workshop/10-7.png) 

1. Wait for the status of all resources to change to **CREATE_COMPLETE**

1. Click the **Test App** button to go to the Lambda console

1. Open the function that was just created by clicking on it

1. Scroll down the page until you see a section called Function code

1. Replace it with the code in alexa-lambda-personal-banker.js, be sure to click **Save**

1. You should see the Amazon Resource Name (ARN) a unique identifier for this function in 
the top right corner of the page. Copy the ARN value for this Lambda function for use in 
the next section of the guide

1. Go back to the [Alexa Developer Console](https://developer.amazon.com/alexa/console/ask). 
You may still have a browser tab open if you follow this tutorial

1. Select the Endpoint tab on the left side navigation panel.

1. Select the "AWS Lambda ARN" option for your endpoint. You have the ability to host your code anywhere that you would like, but for the purposes of simplicity and frugality, we are using AWS Lambda.
1. Paste your Lambda's ARN (Amazon Resource Name) into the textbox provided for Default Region.
    ![](../img/workshop/alexa-configure-lambda.png) 
1. Click the Save Endpoints button at the top of the main panel.
1. Click on Test.
2. Make sure test is enabled.
    ![](../img/workshop/test-alexa.png)

21.	**Type Open Personal Banker(your invocation name) to start the conversation** .
![](../img/workshop/start-alexa.png)