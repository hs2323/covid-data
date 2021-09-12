import configparser
import sys

def get_config(path, params):
    """Reads configuration file for origin Excel data.

    Args:
        path (str): The config file location
        params (list): List of params to traverse the config

    Returns:
        str: The location of the Excel file
    """

    print("Reading configuration file \n")
    
    config = configparser.ConfigParser()

    # Verify that the configuration file is available and readable.
    try:
        if config.read(path):
            location = config.get(*params)
            return location
        else:
           raise
    except:
        print("Could not find or parse configuration file \n")
        sys.exit("Exiting application")
