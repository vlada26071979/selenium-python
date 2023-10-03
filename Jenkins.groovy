

pipeline {

    agent any

    stages {

        stage('Checkout and Pull') {

            steps {

 script {
                    
                    dir('C:\\Jenkins testovi\\Fajlovi sa Git hub-a\\selenium-python') {
                    bat 'git config --global safe.directory "C:\\Jenkins testovi\\Fajlovi sa Git hub-a\\selenium-python"'   

                        bat 'git clean -f -d -x'

 

                        bat 'git pull'
                    }
                }

            }

        }

 

        stage('Run Selenium Scenario') {

            steps { 
script {
                    
                    dir('C:\\Jenkins testovi\\Fajlovi sa Git hub-a\\selenium-python') {
                         


 

                        bat 'pytest'
                    }
                }

                

                   

                    

                   

                

            }

        }

 

 

 

    }

}