# SCA-Cloud-School-Application
An exercise for my application into She Code Africa Cloud Cloud School (Cohort 2)
A 3 months bootcamp to kickstart a career in SRE/Cloud Engineering
I created a cloud account with a free tier subscription (AWS).
I created an instance (either a linux or windows OS )
I downloaded and installed Jenkins on your local machine to run on the default port 8080
I created a repository on Github called SCA Cloud School Application
I wrote a simple code, in my language of choice (python) on my local machine and pushed it to github.
I integrated my github repo to your Jenkins.
I setup a build job on Jenkins.
On submission , I shared the url to access my jenkin server also adviced the username and password for login.


pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout([$class: 'GitSCM', branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: '90284ade-f2c3-437e-aa76-ac2272ae74ca', url: 'https://github.com/Olaoluwadunni/SCA-Cloud-School-Application.git']]])
            }
        }
        stage ('Build') {
            steps   {
                git branch: 'main', credentialsId: '90284ade-f2c3-437e-aa76-ac2272ae74ca', url: 'https://github.com/Olaoluwadunni/SCA-Cloud-School-Application.git'
                bat 'python SCA.py'
            }
        }
    
        stage ('Test')  {
            steps {
                echo 'This Build Job has been tested'
            }
        }
    }
    
}
