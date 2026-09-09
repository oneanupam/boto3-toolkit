import os
import boto3
from configparser import ConfigParser

def get_all_unassociated_security_groups():
    """
    Function to get the list of all the SGs and unassociated SGs of default
    region in default aws account.
    """
    
    security_groups = []
    associated_security_groups = []
    unassociated_security_groups = []

    ec2_client = boto3.client("ec2")
    result = ec2_client.describe_security_groups()
    for sg in result["SecurityGroups"]:
        security_groups.append(sg["GroupName"])

    instances = ec2_client.describe_instances()
    for instances in instances["Reservations"]:
        for instance in instances["Instances"]:
            for group in instance["SecurityGroups"]:
                group_name = group["GroupName"]
                if(group_name not in associated_security_groups):
                    associated_security_groups.append(group_name)

    for sg in security_groups:
        if(sg not in associated_security_groups):
            unassociated_security_groups.append(sg)

    print("Total SGs: ", security_groups)
    print("Associated SGs: ", associated_security_groups)
    print("Unassociated SGs: ", unassociated_security_groups)

if __name__ == "__main__":
    get_all_unassociated_security_groups()
