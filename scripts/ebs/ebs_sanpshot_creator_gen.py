import os
import boto3
import datetime
from configparser import *

def configReader(path):
    data_sections = []
    if not os.path.exists(path):
        print("[ERROR]: Config file doesn't exists.")
    else:
        config = ConfigParser()
        config.read(path)
        config_file_sections = config.sections()

        for section in config_file_sections:
            temp_dict = {}
            options = config.options(section)
            for option in options:
                value=config.get(section, option)
                temp_dict[option]=value
            data_sections.append(temp_dict)

        return data_sections

def SnapshotCreator(Credentials, VolumesDetail):
    # Create session and client
    session = boto3.session.Session(aws_access_key_id=Credentials["access_key"],
                                    aws_secret_access_key=Credentials["secret_key"])

    for VolumeDetail in VolumesDetail.values():
        VolumeID = VolumeDetail.split(",")[0]
        VolumeRegion = VolumeDetail.split(",")[1]
        # Generate tag
        SnapshotTag = VolumeID + "_" + datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        # Create snapshot
        ec2_client = session.client("ec2", region_name=VolumeRegion)
        reservations = ec2_client.create_snapshot(VolumeId=VolumeID, Description="Snapshot for EBS " + VolumeID)
        result = reservations["SnapshotId"]
        # Create tag for snapshots
        ec2_client.create_tags(Resources=[result], Tags=[{"Key": "Name", "Value": SnapshotTag}, ])

        print("[INFO]: Snapshot Created with following details...")
        print("Volume ID:", VolumeID, "Snapshot ID:", result, "Snapshot TAG:", SnapshotTag)

if __name__ == "__main__":
    path = "Path\to\config\file"
    CONFIG_DICT = configReader(path)
    CREDENTIALS = CONFIG_DICT[0]
    VOLUMES_DATA = CONFIG_DICT[1]
    SnapshotCreator(CREDENTIALS, VOLUMES_DATA)
