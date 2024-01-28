import json
import os
import sys

def read_ipc(ipc_file: str) -> json:
    with open(ipc_file, 'r') as f:
        return json.load(f)

def process_ipc(ipc: json, ipc_file:str) -> bool:
    print(ipc['commands'])
    # possible ipc commands are execute, info
    if "execute" in ipc['commands']:
        if run_cmd(ipc['commands']['execute'], ipc_file=ipc_file):    # do the thing and remove the ipc file
            cleanup_ipc(ipc_file=ipc_file)
            return True
    if "info" in ipc['commands']:
        print("wants some info")    # do the thing and remove the ipc file
        cleanup_ipc(ipc_file=ipc_file)
        return True
    return False
    
def run_cmd(cmd: list, ipc_file: str) -> bool:
    if len(cmd) > 1:
        return False
    if 'halt' in cmd:
        print("Shutting down")
        cleanup_ipc(ipc_file=ipc_file)
        sys.exit(0)
    print(f"wants to exec {cmd}")
    return True

def cleanup_ipc(ipc_file: str):
    try:
        os.remove(ipc_file)
    except OSError as e:
        raise(f"Unable to remove ipc: {e}")
    
def check_ipc_file(ipc_file: str):
    if os.path.isfile(ipc_file):
        ipc = read_ipc(ipc_file=ipc_file)
        print("Reading ipc")
        try:
            if not process_ipc(ipc=ipc, ipc_file=ipc_file):
                print(f"Invalid json in {ipc_file}.  Removing ...")
                cleanup_ipc(ipc_file)
        except KeyError:
            print(f"Invalid json in {ipc_file}.  Removing ...")
            cleanup_ipc(ipc_file)