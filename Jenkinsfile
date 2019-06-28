pipeline {
  agent any
  stages {
    stage('Fetch code from SCM') {
      steps {
        git 'https://github.com/jawsnnn-org-dev/python-boilerplate-test.git'
      }
    }
    stage('Build') {
      steps {
        dir('env'){
          deleteDir()
        }
        bat 'mkdir env && cd env && virtualenv build-env'
        bat '"env/build-env/Scripts/activate.bat" && pip install -r requirements.txt'  
      }
    }
    stage('Test'){
      steps {        
        bat '"env/build-env/Scripts/activate.bat" && pytest --cov src/ --cov-report term-missing --cov-report xml --junitxml=junit.xml'
      }
    }
    post {
      always {
        cobertura coberturaReportFile: '**/coverage.xml'
        junit '**/junit.xml'
      }
    }
  }
}
