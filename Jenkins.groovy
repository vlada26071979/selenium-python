

pipeline {

    agent any

    stages {

        stage('Checkout and Pull') {

            steps {

 script {
                    
                    dir('C:\\Jenkins testovi\\selenium-python') {
                    bat 'git config --global --add safe.directory "C:/Jenkins testovi/selenium-python"'   

                        bat 'git clean -f -d -x'

 

                        bat 'git pull'
                    }
                }

            }

        }

 

        stage('Run Selenium Scenario') {

            steps { 
script {
                    
                    dir('C:\\Jenkins testovi\\selenium-python') {
                         


 

                        bat 'pytest'
                    }
                }

                

                   

                    

                   

                

            }

        }

 

 

 

    }

}