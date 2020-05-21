import boto3
from datetime import datetime
import json
import os

def aws_connection(service="ec2"):
    client = boto3.client(service)
    return client


def get_latest_ami(client, ami_prefix_name):
    response = client.describe_images(
        Filters=[
            {
                'Name': 'name',
                'Values': [
                    ami_prefix_name
                ]
            },
        ]
    )
    images_dict = {}
    for image in response.get("Images"):
        images_dict[datetime.fromisoformat(image['CreationDate'][:-1])] = image.get("ImageId")
    dates = (list(images_dict.keys()))
    max_date = max(dates)

    ami_id = images_dict[max_date]
    return ami_id


def create_launch_template_revision(client, ami_id, launch_template_id):

    response = client.create_launch_template_version(
        LaunchTemplateId = launch_template_id,
        SourceVersion = "6",
        LaunchTemplateData = {
           'ImageId' : ami_id
        }
    )

    print(response)

def put_job_success(job_id):
    code_pipeline = boto3.client('codepipeline')
    code_pipeline.put_job_success_result(jobId=job_id)


def lambda_handler(event, context):
    launch_template_id = os.getenv("LT_ID", "")
    job_id = event['CodePipeline.job']['id']
    
    client = aws_connection()
    ami_id = get_latest_ami(client, "moodle-golden-image*")
    create_launch_template_revision(client, ami_id, launch_template_id)
    put_job_success(job_id)


    return {
        'statusCode': 200,
        'ami_id': json.dumps(ami_id)
    }