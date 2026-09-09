import os
import boto3
from configparser import ConfigParser

def get_all_security_groups_with_open22():
    """
    Function to get the list of all the SGs having port 22 open to public
    i.e. "0.0.0.0/0"
    """
    
    security_groups = []
    security_groups_with_open22 = []

    ec2_client = boto3.client("ec2")
    result = ec2_client.describe_security_groups()
    for sg in result["SecurityGroups"]:
        security_groups.append(sg["GroupName"])
        for rule in sg["IpPermissions"]:
            if("FromPort" in rule):
                if(rule["FromPort"] == 22 and rule["IpRanges"][0]["CidrIp"] == "0.0.0.0/0"):
                    security_groups_with_open22.append(sg["GroupName"])
            else:
                pass

    print("Total SGs: ", security_groups)
    print("SGs with Open 22: ", security_groups_with_open22)

if __name__ == "__main__":
    get_all_security_groups_with_open22()
