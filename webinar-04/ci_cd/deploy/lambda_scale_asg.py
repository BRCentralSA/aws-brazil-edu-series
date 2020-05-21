import boto3
import time
import os
import json

def aws_connection(service="autoscaling"):
    client = boto3.client(service)
    return client


def change_desired_capacity(client, asg_name, desired_number):
    response = client.set_desired_capacity(
        AutoScalingGroupName=asg_name,
        DesiredCapacity=desired_number
    )
    print(response)


def put_job_success(job_id):
    code_pipeline = boto3.client('codepipeline')
    code_pipeline.put_job_success_result(jobId=job_id)


def lambda_handler(event, context):
    asg_name = os.getenv("ASG_NAME", "moodle-asg")
    client = aws_connection()
    job_id = event['CodePipeline.job']['id']

    # TODO: Get ASG size Dinamically, update half/half at same time.
    change_desired_capacity(client, asg_name, 2)
    time.sleep(300)
    change_desired_capacity(client, asg_name, 1)
    put_job_success(job_id)

    return {
        'statusCode': 200,
        'status': 'OK' 
    }