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

def GetUnassociatedElasticIPs(config_dict):
    # Get all the regions of a aws service like ec2 service.
    session = boto3.session.Session(aws_access_key_id=config_dict["access_key"],
                                    aws_secret_access_key=config_dict["secret_key"])
    ec2_regions = session.get_available_regions('ec2')

    for region in ec2_regions:
        ec2_resource = session.client("ec2", region_name=region)
        unassociated_eips = ec2_resource.describe_addresses()
        for eip in unassociated_eips["Addresses"]:
            if("NetworkInterfaceId" not in eip):
                print("Region:", region, ", Elastic IP:", eip["PublicIp"])

if __name__ == "__main__":
    path = "Path\to\config\file"
    CONFIG_DICT = configReader(path)
    GetUnassociatedElasticIPs(CONFIG_DICT)
