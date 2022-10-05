# Weave Net 


  kubectl create -f "https://cloud.weave.works/k8s/net?k8s-version=$(kubectl version | base64 | tr -d '\n')"


무슨 이유에서인지 해당 명령어로 weave net을 설치할 수 없었다.. 짐작해보는데 cloud weave가 해당 [링크](https://www.weave.works/blog/weave-cloud-end-of-service)에서 보듯이 2022-09-30일에 서비스를 종료했다고 한다.. 그

weaveworks github에 들어가서 다운받아서 설치하면 된다. 


  https://github.com/weaveworks/weave/releases
