

pipeline {

    agent any

    stages {

        stage('Checkout and Pull') {

            steps {

 script {
                    
                    dir('C:\\Users\\VladimirDjordjevic\\Desktop\\razno\\Faljlovi sa Git hub-a\\selenium-python') {
                         

                        bat 'git clean -f -d -x'

 

                        bat 'git pull'
                    }
                }

            }

        }

 

        stage('Run Selenium Scenario') {

            steps { 
script {
                    
                    dir('C:\\Users\\VladimirDjordjevic\\Desktop\\razno\\Faljlovi sa Git hub-a\\selenium-python') {
                         


 

                        bat 'python test_login.py'
                    }
                }

                

                   

                    

                   

                

            }

        }

 

 

 

    }

}