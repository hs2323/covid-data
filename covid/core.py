import argparse

from .api import api
from .config import config
from .parser import parser

def start():
    argp=argparse.ArgumentParser()
    argp.add_argument('--path', help='Folder to save your data', required=True)
    args=argp.parse_args()

    ini_file = './config.ini'
    params = ['Data', 'file']
    data_file = config.get_config(ini_file, params)

    list = parser.open_excel(data_file)

    api.get_remote_data(list)
