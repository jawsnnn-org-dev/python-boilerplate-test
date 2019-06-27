node {
  stages {
    stage('Fetch code from SCM') {
      git 'https://github.com/jawsnnn-org-dev/python-boilerplate-test.git'
    }
    stage('Build') {
      dir('env'){
        deleteDir()
      }
      bat 'mkdir env && cd env && virtualenv build-env'
      bat '"env/build-env/Scripts/activate.bat" && pip install -r requirements.txt'  
    }
    stage('Test'){
      bat 'echo "hello"'
  }
}
