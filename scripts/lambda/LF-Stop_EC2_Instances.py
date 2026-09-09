import boto3

def StopEC2Instances():
    region = "us-east-1"
    instances = ["i-0292019453398253a"]
    ec2_client = boto3.client("ec2", region_name=region)
    ec2_client.stop_instances(InstanceIds=instances)
    print("Instances Stopped.")

def PublishMail():

    TopicARN = "XXXXXXXXXXXXXXXXXXXXXXXXXXX"
    Message = "Message."
    Subject = "Subject"

    # Initialize SNS client for default region
    sns_client = boto3.client("sns")
    result = sns_client.publish( TopicArn=TopicARN, Message=Message,
                                 Subject=Subject, MessageStructure='string'
                                 )
    print(result)

def lambda_handler(event, context):
    StopEC2Instances()
    PublishMail()

if __name__ == '__main__':
    lambda_handler(None, None)
