# Python Docker image on AWS Lambda

In this tutorial, I used a Python Docker image on AWS Lambda using Lambda container images. Using Docker containers for your Python app on AWS Lambda means you can create a special environment for your app with its own tools and settings, making sure it works everywhere, and also making it easy to include all the things (libraries and packages)your app needs to run correctly.

## Requirements:

<li>Docker</li>
<li>AWS CLI</li>
<li>AWS CLK</li>

## Create CDK Project

Make a folder for our CDK project:
```pwsh
mkdir docker-lambda-aws
```
```pwsh
cd docker-lambda-aws
```
Create the CDK application:
```pwsh
cdk init app --language typescript
```
Open up the new folder:
```pwsh
code .
```
## Create a Python handler app
Creeate a folder named 'image':
```pwsh
mkdir image
```
and create another folder within that called 'src' for source.

Within the src folder create your python application file 'main.py'. This code is going to be our Lambda Function handler aka the code that executes when the Lambda function is called.

Create a requirements file in your image folder and include 'numpy'

## Create Dockerfile for Lambda

Create a Dockerfile within your image folder.

See [here](https://docs.aws.amazon.com/lambda/latest/dg/python-image.html) for available Python base images.

Within your image folder build your docker image using:
```pwsh
docker build -t docker-image:test .
```
Next run the docker image using:
```pwsh
docker run -p 9000:8080 docker-image:test
```
## Test the Docker image locally
Got to another terminal ( ctrl + `) and send a http request ([Step 2](https://docs.aws.amazon.com/lambda/latest/dg/python-image.html)) to it to run the function inside your Dockerfile:
```pwsh
Invoke-WebRequest -Uri "http://localhost:9000/2015-03-31/functions/function/invocations" -Method Post -Body '{}' -ContentType "application/json"
```
## Create AWS Docker Lambda with CDK

Go to the Lib folder in your project and find the docker-lambda-aws-stack.ts file and update the code as per the tutorial.

## Deploying to AWS

Ensure AWS CLI is configured. Run:
```pwsh
aws sts get-caller identity
```
Go to the docker-lambda-aws folder and run:
```pwsh
cdk bootstrap --region {your region}
```
You only need to bootstrap once per account per region, so if nothing shows up that probably means you have already cdk bootstrapped this account.

Next run:
```pwsh
cdk deploy
```
When it asks you to deploy this changes (y/n), type 'y' and press enter.

If it deploys successfuly you should see the numpy matrix and hello world:

<img width=600 src="https://github.com/markbuckle/Python-Lambda-Docker/blob/main/deployed.png?raw=true">

You should also see your updated function in the Lambda Function console:

<img width=800 src="https://github.com/markbuckle/Python-Lambda-Docker/blob/main/lambdafunction.png?raw=true">
