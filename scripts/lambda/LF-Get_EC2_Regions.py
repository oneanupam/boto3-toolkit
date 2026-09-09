import os
import boto3

def GetEC2Regions():
    session = boto3.session.Session()
    ec2_regions = session.get_available_regions("ec2")
    for region in ec2_regions:
        print("Region:", region)

def PublishMail():

    Message = "Message."
    Subject = "Subject"

    # Initialize SNS client for default region
    sns_client = boto3.client("sns")
    result = sns_client.publish( TopicArn=os.environ["TopicARN"], Message=Message,
                                 Subject=Subject, MessageStructure='string'
                                 )
    print(result)

def lambda_handler(event, context):
    GetEC2Regions()
    PublishMail()

if __name__ == '__main__':
    lambda_handler(None, None)

"""
Note: If we are using the environment variable as below.
TopicARN = XXXXXXXXXXXXXXXX

"""
