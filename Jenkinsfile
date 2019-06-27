deleteDir()

node {
  bat "mkdir env &&" 
  bat "cd env"
  bat "virtualenv build-env"
  bat "build-env/Scripts/activate.bat"
  bat "pip install -r ../../../requirements.txt"
}
