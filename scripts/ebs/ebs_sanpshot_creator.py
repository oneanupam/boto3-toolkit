import os
import boto3
import datetime
from configparser import *

def configReader(path):
    data_dict = {}
    if not os.path.exists(path):
        print("[ERROR]: Config file doesn't exists.")
    else:
        config = ConfigParser()
        config.read(path)
        config_file_sections = config.sections()
        
        for section in config_file_sections:
            options = config.options(section)
            for option in options:
                value=config.get(section, option)
                data_dict[option]=value

        return data_dict

def SnapshotCreator(VolumeID):
    SnapshotTag = VolumeID + "_" + datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

    # Create snapshot
    ec2_client = boto3.client("ec2")
    reservations = ec2_client.create_snapshot(VolumeId=VolumeID, Description="Snapshot for EBS " + VolumeID)
    result = reservations["SnapshotId"]

    # Create tag for snapshots       
    ec2_client.create_tags(Resources=[result], Tags=[{"Key": "Name", "Value": SnapshotTag}, ])

    print("[INFO]: Snapshot Created with following details...")
    print("Volume ID:", VolumeID, "Snapshot ID:", result, "Snapshot TAG:", SnapshotTag)

if __name__ == "__main__":
    path = "Path\to\config\file"
    data_dict = configReader(path)
    for VolumeID in data_dict.values():
        SnapshotCreator(VolumeID)
