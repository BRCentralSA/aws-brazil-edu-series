import boto3
import time

def trigger_image_pipeline(client, arn):
    
    response = client.start_image_pipeline_execution(
        imagePipelineArn=arn,
    )
    return response

def list_image_pipeline(client, arn):
    response = client.list_image_pipeline_images(
        imagePipelineArn=arn
    )
    arn_number_old = 0
    state = False
    ami_id = False
    list_size = len(response.get("imageSummaryList")) - 1
    image = response.get("imageSummaryList")[list_size]

    state = image.get("state").get("status")
    if state == "TESTING":
        ami_id = image.get("outputResources").get("amis")[0].get("image")
    return state, ami_id
        

def main():
    IMAGE_PIPELINE_ARN = "arn:aws:imagebuilder:us-east-1:856860420093:image-pipeline/moodle-ci-pipeline"
    client = boto3.client('imagebuilder', region_name="us-east-1")
    response = trigger_image_pipeline(client, IMAGE_PIPELINE_ARN)
    
    time.sleep(5)
    image_status = list_image_pipeline(client, IMAGE_PIPELINE_ARN)

    while image_status[1] == False:
        print(image_status)
        time.sleep(5)
        image_status = list_image_pipeline(client, IMAGE_PIPELINE_ARN)
    
    print(image_status)
    # TODO: Upload artifact in S3 AMI ID

if __name__ == "__main__":
    main()