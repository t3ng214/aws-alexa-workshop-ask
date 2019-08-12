# Create a Lambda function for Alexa
##	Create a Lambda function for Alexa

1.	Go to http://aws.amazon.com and sign in to the console.
2.	Navigate to Lambda.
3.	Click the orange "Create function" button. It should be near the top of your screen.
4.	There are three boxes labeled "Author from scratch", "Blueprints" and "Serverless Application Repository". Click the radio button in the box titled "Serverless Application Repository" We have created an application in the repository as a shortcut to getting everything set up for your skill.
5.	Enter fact to search for the application repository named alexa-skills-kit-nodejs-factskill. Enter the full name into the serach box if you need to narrow the search results.
6.	Click on the application. This template will create the Lambda function, grant the Alexa Skills Kit permission to invoke it, and set up an IAM role for you. It will also add the code from this GitHub repo and include the required dependencies so that you don't have to upload them yourself.
7.	Change the application name and then Click the deploy button at the bottom of the page.
![](../img/workshop/10-7.png) 
8.	Wait for the status of all resources to change to CREATE_COMPLETE
9.	Click the Test App button to go to the Lambda console.
10.	Open the function that was just created by clicking on it.
11.	Scroll down the page until you see a section called Function code.
12.	Replace it with the code in alexa-lambda-personal-banker.js, be sure to click "Save".
13.	You should see the Amazon Resource Name (ARN) a unique identifier for this function in the top right corner of the page. Copy the ARN value for this Lambda function for use in the next section of the guide.
14.	Go back to the Amazon Developer Portal https://developer.amazon.com. You may still have a browser tab open if you follow this tutorial.
15.	Select the Endpoint tab on the left side navigation panel.
16.	Select the "AWS Lambda ARN" option for your endpoint. You have the ability to host your code anywhere that you would like, but for the purposes of simplicity and frugality, we are using AWS Lambda.
17.	Paste your Lambda's ARN (Amazon Resource Name) into the textbox provided for Default Region.
![](../img/workshop/alexa-configure-lambda.png) 
18.	Click the Save Endpoints button at the top of the main panel.
19.	Click on Test.
20.	Make sure test is enabled.
![](../img/workshop/test-alexa.png)

21.	**Type Open Personal Banker(your invocation name) to start the conversation** .
![](../img/workshop/start-alexa.png)