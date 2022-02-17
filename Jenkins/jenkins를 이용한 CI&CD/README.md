## Jenkins를 이용한 CI/CD

### GCP에서 Jenkins로 msa프로젝트 CI/CD 구축

github master브랜치에 push하였을 때 jenkins 서버에서 자동으로 도커 이미지를 배포하고 쿠버네티스가 돌아가고 있는 서버에 서비스들을 rolling update 해보자!


### jenkins와 github을 연동


![jenkins설정](https://user-images.githubusercontent.com/68090443/154589810-6e345fac-50a4-4407-8732-3596b376a061.PNG)

	Jenkins 관리 > 시스템 설정 클릭


마우스를 내리다 보면 아래와 같이 GitHub Server라는 설정 칸이 있다. 이 칸을 작성해 주자.


![것허브연동](https://user-images.githubusercontent.com/68090443/154589766-1337d5c4-dec3-41e2-85d3-955e342b0220.PNG)


Name에는 원하는 이름을 지정하고

Credentials에 add를 클릭해준다. 클릭 해주면 아래와 같은 사진이 나오는데


![깃허브](https://user-images.githubusercontent.com/68090443/154589936-7107ed89-2294-4ece-8d56-5da9dbc28283.PNG)


	Domain : Global credentials (unrestricted) 선택

	Kind : Secret text 선택

	Secret : github 로그인 토큰 입력

	ID : 본인이 지정하는 식별자(ID) 입력 (ex) github)

칸을 채운 후 Test connection 클릭시 정상 연동 확인 한다.

### jenkins와 docker hub 연동

docker hub연동을 위해 'Username with password' 타입의 Credential을 추가한다


![jenkins깃허브연동](https://user-images.githubusercontent.com/68090443/154589715-c3bc183f-6075-4c59-8b75-f675e02c51cd.PNG)



	kind : Username with password

	Scope : 기본지정(Global)
	
	Username : dockerhub_id
	
	password : dockerhub_pwd
	
	id : 본인이 지정하는 식별자(ID) 입력 ( ex) docker-hub )
	
	Description : 해당 Credential에 대한 설명

칸을 다 채운 후 Credential을 생성한다.


### Jenkins 파이프라인을 정의

아래 사진과 같이 새로운 아이템을 클릭하여 파이프라인을 구성한다.

![jenkins아이템생성](https://user-images.githubusercontent.com/68090443/154590052-5fd235c5-25c3-4663-be21-624ca71d647f.png)


아이템 이름을 입력하고 아래 사진에서 Pipleline을 선택하여 OK버튼을 눌러 생성해주자.

![잰킨스](https://user-images.githubusercontent.com/68090443/154590139-01123a8b-c2e4-455a-bd7b-a75220128f63.PNG)


이제 파이프라인에 대한 설정을 해주면 된다. 아래 사진은 gcp에 올라가있는 msa프로젝트에 ci/cd를 적용한 설정이다. 


![잰킨스2](https://user-images.githubusercontent.com/68090443/154590158-3d99eb86-989b-49aa-8300-9889ecf6c83a.PNG)

![파이프라인작성](https://user-images.githubusercontent.com/68090443/154590188-054845ef-f0ec-4cba-8c6f-654d2b118a69.PNG)

### 파이프라인 스크립트

pipeline {
        agent any
        environment{
            DOCKERHUB_CREDENTIALS=credentials('docker-hub')
        }
        stages {
            stage('github clone') {
                steps {
                    git branch: 'main',
                        credentialsId: 'github',
                        url: 'https://github.com/beomsun1234/e-commerce-msa.git'
                }
            }

            stage('build') {
                steps {
                    sh """
                        cd /var/lib/jenkins/workspace/msa/order-service
                        chmod +x gradlew
                        ./gradlew clean build 
                        echo 'order-service build sucess'
                    """
                    sh """
                        cd /var/lib/jenkins/workspace/msa/product-service
                        chmod +x gradlew
                        ./gradlew clean build
                        echo 'product-service build sucess'
                    """
                }
            }
            stage('docker build') {
                steps {
                    sh """
                        cd /var/lib/jenkins/workspace/msa/order-service
                        sudo docker build -t beomsun22/order-service:${BUILD_NUMBER} .
                        echo 'docker jenkins-order build sucess'
                    """
                    sh """
                        cd /var/lib/jenkins/workspace/msa/product-service
                        sudo docker build -t beomsun22/product-service:${BUILD_NUMBER} .
                        echo 'docker jenkins-product build sucess'
                    """
                }
            }
            stage('login'){
                steps{
                    sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
                }
            }
             stage('docker push') {
                steps {
                    sh 'docker push beomsun22/order-service:${BUILD_NUMBER}'
                    echo 'docker order-service:v${BUILD_NUMBER} push sucess'
                    sh 'docker push beomsun22/product-service:${BUILD_NUMBER}'
                    echo 'docker product-service:v${BUILD_NUMBER} push sucess'
                }
            }
            stage('deploy') {
                steps {
                    sh """

                        sudo ssh root@[worker ip] 'export KUBECONFIG=/etc/kubernetes/admin.conf'
                        sudo ssh root@[worker ip] 'kubectl get pod'
                        sudo ssh root@[worker ip] '/home/beomsun159/./test.sh aaa bbb'
                        sudo ssh root@[worker ip] '/home/beomsun159/./rolling_update.sh order-service order-service beomsun22/order-service:${BUILD_NUMBER}'
                        sudo ssh root@[worker ip] '/home/beomsun159/./rolling_update.sh product-service product-service beomsun22/product-service:${BUILD_NUMBER}'
                    """
                }
            }
        }
        post {
            always{
                sh 'docker logout'
            }
        }
    }

### 트러블슈팅

빌드완료 후 도커 이미지를 생성하고 도커 허브에 push할때 도커 hub에 push가 이루어 지지 않았다.. 성공했다고는 나오지만 도커 hub를 확인해 보면 바뀐것이 없었다.. 도커 로그인에서 문제가 발생한 것 같다고 생각해서
도커 로그인 방법을 아래와 같이 바꿔서 작성하니 정상적으로 도커 hub에 push할 수 있었다.


    pipeline {
            agent any
            environment{
                DOCKERHUB_CREDENTIALS=credentials('docker-hub')
            }
            stages {
                .......
                stage('login') {
                    steps{
                    sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
                }
                .......
            }

