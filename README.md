# Python application accelarator

A blueprint for project teams to quickly start up a new project in Python

## Table of contents
* [Overview](#overview)
* [Pre-requisits](#pre-requisites)
* [Setup](#setup)

### Overview
The purpose of this repository is to create a quick-start project template for teams working in Python.

The following factors were considered:
* Setting a baseline for project structure and naming convention
* Automatic initialization of local virtual environment
* Github and Jenkins integration

### Pre-requisites
The following are required to be setup and configured on your system to initialize the project:
* Git command line
* A local python installation (v3.5+) with pip and virtualenv pre-installed
* 
 

Pre-requisites:
    - TBD

Step 0: Create new Git repo for your project using Service now

Follow naming convention (all lower case letters, lusa-python-*)

Step 1: Clone boilerplate repository to your local machine

git clone https://github.com/EliLillyCo/lusa-python-boilerplate my-project-directory

Step 2: Configure:
    - Update metadata.py with project details
    - Update project package dependencies (if known) in requirements.txt

Step 3: Run initialization script
cd my-project-directory/meta
python init.py