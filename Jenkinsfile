node {
  git "https://github.com/jawsnnn-org-dev/python-boilerplate-test.git"
  dir('env'){
    deleteDir()
  }
  bat 'mkdir env && cd env && virtualenv build-env'
  bat '"env/build-env/Scripts/activate.bat" && pip install -r requirements.txt'  
}
