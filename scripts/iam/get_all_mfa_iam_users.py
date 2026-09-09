import os
import boto3
from configparser import ConfigParser

def config_reader(config_path):
    data_dict = {}
    if not os.path.exists(config_path):
        print("[ERROR]: Config file doesn't exists.")
    else:
        config = ConfigParser()
        config.read(config_path)
        config_file_sections = config.sections()
        for section in config_file_sections:
            options = config.options(section)
            for option in options:
                value = config.get(section, option)
                data_dict[option] = value
        return data_dict

def get_all_iam_users_with_mfa_devices(config_dict):

    iam_client = boto3.client("iam", aws_access_key_id=config_dict["access_key"], aws_secret_access_key=config_dict["secret_key"])
    result = iam_client.list_users()
    for UserDetail in result["Users"]:    
        result = iam_client.list_mfa_devices(UserName=UserDetail["UserName"])
        print("UserName: ", UserDetail["UserName"], ", Total_MFA_Devices: ", len(result["MFADevices"]))

if __name__ == "__main__":
    CONFIG_PATH = "Path\to\config\file"
    CONFIG_DICT = config_reader(CONFIG_PATH)
    get_all_iam_users_with_mfa_devices(CONFIG_DICT)
