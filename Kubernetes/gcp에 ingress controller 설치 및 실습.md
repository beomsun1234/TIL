# K8s ingress controlle 


VM에서 쿠버네티스를 구현했을 경우에 사용하는 방법입니다. 쿠버네티스 설치하는 방법은 아래 링크를 보고 따라하면됩니다.

https://confluence.curvc.com/pages/releaseview.action?pageId=98048155


우선 저는 GCP VM에서 쿠버네티스(Master-1, worker-2)를 구성했으므로 bare-metal을 사용해합니다.

https://kubernetes.github.io/ingress-nginx/deploy/#bare-metal-clusters 



## ingress에 SSL적용

Let's Encrypt SSL 인증서를 ingress에 적용완료


## 쿠버네티스 대시보드 

ingress 통해 대시보드 접속완료



## 트러블슈팅

### kubeadm init 시 발생한 에러

    [preflight] Running pre-flight checks
    error execution phase preflight: [preflight] Some fatal errors occurred:
            [ERROR CRI]: container runtime is not running: output: E0923 00:02:04.732882   18439 remote_runtime.go:948] "Status from runtime service failed" err="rpc error: code = Unimplemented desc = unknown service runtime.v1alpha2.RuntimeService"
    time="2022-09-23T00:02:04Z" level=fatal msg="getting status of runtime: rpc error: code = Unimplemented desc = unknown service runtime.v1alpha2.RuntimeService"
    , error: exit status 1
    [preflight] If you know what you are doing, you can make a check non-fatal with `--ignore-preflight-errors=...`
    To see the stack trace of this error execute with --v=5 or higher
    
#### 해결법

  sudo rm /etc/containerd/config.toml
  sudo systemctl restart containerd
  


### 대시보드 토큰 생성 안될때

   

대시보드 생성 후 로그인에 사용할 토큰이 생성되지 않는 문제 발생했다.. 

 error: error executing template "{{.data.token | base64decode}}": template: output:1:16: executing "output" at <base64decode>: invalid value; expected string

위와 같은 에러가 발생했고 구글링해보니 아래 명령어로 문제를 해결할 수 있었다. 참고 -> https://github.com/vmware-tanzu/kubeapps/issues/1550
   
    kubectl -n kubernetes-dashboard create token admin-user





