import os
import boto3
from configparser import *

def configReader(path):
    if not os.path.exists(path):
        print("[ERROR]: Config file doesn't exists.")
    else:
        config = ConfigParser()
        config.read(path)

        config_file_sections = config.sections()

        key_value_pairs_dict = {}

        for section in config_file_sections:
            options = config.options(section)
            for option in options:
                value=config.get(section, option)
                key_value_pairs_dict[option]=value

        return key_value_pairs_dict

def GetAllEC2Instances(config_dict):
    # Get all the regions of a aws service like ec2 service.
    session = boto3.session.Session(aws_access_key_id=config_dict["access_key"],
                                    aws_secret_access_key=config_dict["secret_key"])
    ec2_regions = session.get_available_regions('ec2')

    for region in ec2_regions:
        ec2_resource = session.resource("ec2", region_name=region)
        # ec2_instances = ec2_resource.instances.all() # To list all the instances.
        # Use the filter() method of the instances collection to retrieve all running/stopped EC2 instances.
        ec2_instances = ec2_resource.instances.filter( Filters=[{'Name': 'instance-state-name', 'Values': ['stopped']}] )
        for instance in ec2_instances:
            print("Region:", region, ", Instance ID:", instance.id)

if __name__ == "__main__":
    path = "Path\to\config\file"
    CONFIG_DICT = configReader(path)
    GetAllEC2Instances(CONFIG_DICT)
