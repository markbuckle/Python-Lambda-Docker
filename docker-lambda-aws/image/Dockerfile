# image will be based on:
FROM public.ecr.aws/lambda/python:3.12

# Copy requirements.txt. Don't need an absolute path since it's in the same folder
COPY requirements.txt ${LAMBDA_TASK_ROOT}

# Install the specified packages
RUN pip install -r requirements.txt

# Copy all files in ./src
COPY src/* ${LAMBDA_TASK_ROOT}

# Set the CMD to your handler.
CMD [ "main.handler" ]