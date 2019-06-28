# Python application accelarator

A blueprint for project teams to quickly start up a new project in Python

## Table of contents
* [Overview](#overview)
* [Pre-requisites](#pre-requisites)
* [Setup](#setup)

### Overview
The purpose of this repository is to create a quick-start project template for teams working in Python.

The following factors were considered:
* Setting a baseline for project structure and naming convention
* Automatic initialization of local virtual environment (using virtualenv)
* Github and Jenkins integration

### Pre-requisites
The following are required to be setup and configured on your system to initialize the project:
* Git command line installed on your system
* An empty Github repository initialized in Elilillyco org. If you don't know how to do this follow [these steps](https://lilly.service-now.com/nav_to.do?uri=%2Fkb_view.do%3Fsysparm_article%3DKB2016891)
* A local python installation (v3.5+) with pip and virtualenv pre-installed
* Add Cobertura and Junit plugins to your Jenkins instance for coverage and test reports


### Setup
- Step 1: Clone boilerplate repository to your local machine

    `git clone https://github.com/EliLillyCo/lusa-python-boilerplate my-project-directory`

- Step 2: Configure metadata
    - Update meta/metadata.py with project details
    
    *Important* - This should include specifying details of the empty git repository created for this project
    - Update requirements.txt with package dependencies (if any)

- Step 3: Run initialization script

    ```
    cd my-project-directory/meta
    init.bat
    ```

- Step 4: Validate
  - A local virtualenv (name defaults to project name) should be automatically created and activated on terminal
  - The remote Github repository should be  initialized with the boilerplate code