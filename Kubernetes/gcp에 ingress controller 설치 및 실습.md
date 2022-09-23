# K8s ingress controlle 


VM에서 쿠버네티스를 구현했을 경우에 사용하는 방법입니다. 쿠버네티스 설치하는 방법은 아래 링크를 보고 따라하면됩니다.

https://confluence.curvc.com/pages/releaseview.action?pageId=98048155


우선 저는 GCP VM에서 쿠버네티스(Master-1, worker-2)를 구성했으므로 bare-metal을 사용해합니다.

https://kubernetes.github.io/ingress-nginx/deploy/#bare-metal-clusters 






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
  






