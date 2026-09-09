import boto3

def publish_mail():

    TopicARN = "XXXXXXXXXXXX"
    Message = "Test Message."
    Subject = "Test Subject"

    # Initialize SNS client for default region
    sns_client = boto3.client("sns")
    result = sns_client.publish( TopicArn=TopicARN, Message=Message,
                                 Subject=Subject, MessageStructure='string'
                                 )
    print(result)
    
if __name__ == "__main__":
    publish_mail()
