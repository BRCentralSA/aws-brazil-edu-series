import boto3


def aws_client_factory(service):
    aws_client = boto3.client(service, region_name="<AWS REGION>")

    return aws_client


def send_email():
    aws_client = aws_client_factory("sns")
    response = aws_client.publish(
        TopicArn="<SNS TOPIC ARN>",
        Message="Olá! Informamos que não teremos aula amanhã.",
        Subject="Notificação Escola AWSUnicorn",
    )

    return response
