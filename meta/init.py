# -*- coding: utf-8 -*-
"""
Author: Arpan Malviya
Purpose: 
    Setup the project environment
    - Create fresh virtual environment for project 
    - Attach project to configured Git remote
    - create dynamic initialization script for installing pre-defined dependencies
Date: 24-JUN-2019
"""

import metadata
from subprocess import check_output, check_call, DEVNULL, call
import os, stat, errno
from shutil import rmtree

print("Checking base python installation")
git_url=metadata.project_git_url

def handleRemoveReadonly(func, path, exc):
    """
    If encountered permission error while recursively deleting folder,
        update permissions and retry
    """
    if not os.access(path, os.W_OK):
        # Is the error an access error ?
        os.chmod(path, stat.S_IWUSR)
        func(path)
    else:
        raise Exception

try:
    os.chdir("../env")
except Exception as e:
    print("There was an issue while changing active working directory to env")
    raise

try:
    str_python_version = check_output(['virtualenv','--version'])
    print("using virtualenv version: ",str_python_version,"...")

except Exception as e:
    print("Virtualenv not found on system. Please ensure it is installed and PATH env variable is properly set")
    raise

str_virtualEnv = metadata.virt_env_name
try:
    print("If virtual environment already exists, delete and recreate...")
    if os.path.exists(str_virtualEnv):
        rmtree(str_virtualEnv, ignore_errors=False, onerror=handleRemoveReadonly)
except Exception as e:
    print("There was an error while deleting and recreating virtualenv")
    raise

try:
    print("Creating virtualenv", str_virtualEnv, " within env subfolder...")
    call(['virtualenv',str_virtualEnv])
except Exception as e:
    print("There was an error while creating a virtualenv ")
    raise
print("...Done setting up virtual environment!")
os.chdir("..")

print("Git setup begins...")
# rm -rf .git && git init . && npm i
try:
    print("Removing original git config...")
    if os.path.exists(".git"):
        rmtree(".git", ignore_errors=False, onerror=handleRemoveReadonly)
except Exception as e:
    print("There was an error while removing Git config directory (.git)")
    raise

try:
    print("Intializing new git repo here...")
    call(["git","init","."])
except Exception as e:
    print("There was an error while initializing git repository")
    raise
print("Git initialization done")

try:
    print("Attaching remote git repo to local repository and pushing changes")
    call(("git remote add origin "+git_url).split(" "))
    call("git add .".split(" "))
    call(["git","commit", "-m", "'Python boilerplate accelarator init'"])
    call("git push -u origin master".split(" "))
except Exception as e:
    print("Error attaching local repo to remote")
    raise

try:
    print("Creating initialization batch script...")
    str_path=os.path.normcase(os.path.join(os.getcwd(),"env",str_virtualEnv,"Scripts"))
    os.chdir("meta")
    with open("setup.bat","w") as f:
        f.write("path = "+str_path+";%PATH%\r\n")
        f.write("activate "+str_virtualEnv+"&& pip install -r ../requirements.txt\r\n")
except Exception as e:
    print("Error writing setup batch file")
    raise