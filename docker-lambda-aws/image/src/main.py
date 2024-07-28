import numpy as np


def handler(event, context):
    # generate random matrix
    arr = np.random.randint(0, 10, (3, 3))
    return {
        "statusCode": 200,
        "body": {"message": "Hello from Lambda!", "array": arr.tolist()},
    }