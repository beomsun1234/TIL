# Weave Net 


    kubectl create -f "https://cloud.weave.works/k8s/net?k8s-version=$(kubectl version | base64 | tr -d '\n')"


무슨 이유에서인지 해당 명령어로 weave net을 설치할 수 없었다.. 짐작해보는데 cloud weave가 해당 [링크](https://www.weave.works/blog/weave-cloud-end-of-service)에서 보듯이 2022-09-30일에 서비스를 종료했다고 한다.. 그래서 저 링크가 안먹는 것 같다.

weaveworks github에 들어가서 yaml 파일을 복사해서 실행하면 된다. 


    https://github.com/weaveworks/weave/releases
