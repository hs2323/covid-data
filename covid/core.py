import argparse

from .config import config

def start():
    argp=argparse.ArgumentParser()
    argp.add_argument('--path', help='Folder to save your data', required=True)
    args=argp.parse_args()

    ini_file = './config.ini'
    params = ['Data', 'file']
    config.get_config(ini_file, params)
