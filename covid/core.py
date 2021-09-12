import argparse

def start():
    argp=argparse.ArgumentParser()
    argp.add_argument('--path', help='Folder to save your data', required=True)
    args=argp.parse_args()
