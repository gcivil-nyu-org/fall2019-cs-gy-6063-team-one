import boto3
from moto import mock_s3
from teamone.settings import AWS_STORAGE_BUCKET_NAME


def setUpMockedS3(testClass):
    """
        Set up `TestCase` class to use mocked AWS S3 storage 
        with the bucket name specified in `teamone.settings.AWS_STORAGE_BUCKET_NAME`
    """

    @mock_s3
    class Wrapper(testClass):
        def setUp(self):
            mockedS3 = boto3.resource("s3", region_name="us-east-1")
            mockedS3.create_bucket(Bucket=AWS_STORAGE_BUCKET_NAME)
            return testClass.setUp(self)

    return Wrapper


def setUpMockedS3Selenium():
    mock = mock_s3()
    mock.start()

    mockedS3 = boto3.resource("s3", region_name="us-east-1")
    mockedS3.create_bucket(Bucket=AWS_STORAGE_BUCKET_NAME)
    return mockedS3
