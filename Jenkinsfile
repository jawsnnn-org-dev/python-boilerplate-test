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
    stage('Lint and Test'){
      steps {        
        bat '"env/build-env/Scripts/activate.bat" && pytest --cov src/ --cov-report term-missing --cov-report xml --junitxml=junit.xml && pylint src --msg-template="{path}:{line}: [{msg_id}({symbol}), {obj}] {msg}" > pylint.log'
      }
    }    
  }
  post {
    always {
      cobertura coberturaReportFile: '**/coverage.xml'
      junit '**/junit.xml'
      scanForIssues tool: pyLint(pattern: '**/pylint.log')
    }
  }
}
