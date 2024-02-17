import boto3

from src import config


class SQSManager:
    def __init__(self, config):
        self.sqs = boto3.client('sqs',
                                endpoint_url=config["ENDPOINT_URL"],
                                aws_access_key_id=config["ACCESS_KEY"],
                                aws_secret_access_key=config["SECRET_KEY"],
                                region_name=config["REGION_NAME"])

    def create_queue(self, queue_name):
        response = self.sqs.create_queue(QueueName=queue_name)
        return response['QueueUrl']

    def send_message(self, queue_url, message_body):
        response = self.sqs.send_message(QueueUrl=queue_url, MessageBody=message_body)
        return response['MessageId']

    def receive_message(self, queue_url, max_messages=1):
        response = self.sqs.receive_message(QueueUrl=queue_url, MaxNumberOfMessages=max_messages)
        return response.get('Messages', [])

    def delete_message(self, queue_url, receipt_handle):
        self.sqs.delete_message(QueueUrl=queue_url, ReceiptHandle=receipt_handle)


sqs_manager = SQSManager(config["AWS"])
queue = sqs_manager.create_queue('queue')
