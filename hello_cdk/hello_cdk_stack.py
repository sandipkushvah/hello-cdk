from aws_cdk import (
    aws_s3 as s3,
    aws_lambda as _lambda,
    aws_apigateway as apigw,
    core
)


class HelloCdkStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # The code that defines your stack goes here
        # bucket = s3.Bucket(self, "MyFirstCDKBucket", versioned=True,) # Used to create bucket

         # Defines an AWS Lambda resource
        my_lambda = _lambda.Function(
            self, 'HelloHandler',
            runtime=_lambda.Runtime.PYTHON_3_7,
            code=_lambda.Code.asset('lambda'),
            handler='hello.handler',
        )


        apigw.LambdaRestApi(
            self, 'Endpoint',
            handler=my_lambda,
        )
