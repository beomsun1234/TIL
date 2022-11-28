# Kubernetes  Health check

Kubernetes에서는 여러 유형의 probe를 사용하여 포드가 시작되었는지, 활성 상태이고 준비되었는지 확인합니다.

즉

쿠버네티스는 각 컨테이너의 상태를 주기적으로 체크해서, 문제가 있는 컨테이너를 자동으로 재시작하거나 또는 문제가 있는 컨테이너(Pod를) 서비스에서 제외할 수 있다.




## Liveness probe (컨테이너가 살아 있는지 아닌지를 체크하는 방법)

컨테이너가 작동 중인지 확인합니다. 작동하지 않으면 kubelet이 종료되고 컨테이너가 다시 시작됩니다.



## Readiness probe (컨테이너가 서비스가 가능한 상태인지를 체크하는 방법)

컨테이너에서 실행되는 애플리케이션이 요청을 수락할 준비가 되었는지 확인합니다. 준비가 된 경우 Kubernetes는 일치하는 서비스가 Pod로 트래픽을 보낼 수 있도록 허용합니다. 준비되지 않은 경우 엔드포인트 컨트롤러는 일치하는 모든 서비스에서 이 포드를 제거합니다.


## Startup probe 

컨테이너에서 실행되는 애플리케이션이 시작되었는지 확인합니다. 시작된 경우 Kubernetes는 다른 프로브가 작동을 시작할 수 있도록 허용합니다. 그렇지 않으면 kubelet이 종료되고 컨테이너가 다시 시작됩니다.


# 참고 
[참고-1](https://bcho.tistory.com/1264)
[참고-2](https://komodor.com/blog/kubernetes-health-checks-everything-you-need-to-know/)
