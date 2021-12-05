import os
import boto3

PUBLISH = {
    "Message": "https://www.myfitnesspal.com/",
    "Subject": "Don't forget to log noms today.",
}


def main(event, context):  # pylint: disable=unused-argument
    """RemindeMe."""
    topic_arn = os.environ["TOPIC_ARN"]
    topic = boto3.resource("sns").Topic(arn=topic_arn)
    topic.publish(**PUBLISH)
