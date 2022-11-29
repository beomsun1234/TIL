#  kubeadm token 생성 

   kubeadm token create --ttl 0
   

기본적으로 만료기간이 24시간인데 --ttl 0으로 설정 할 경우 무제한이다. 

gcp 인스턴스로 클러스터를 구축했고 NODE auto scaling 을 위해 token tls를 무제한으로 설정했다.

## token 확인


  kubeadm token list


## token hash 값 확인


  openssl x509 -pubkey -in /etc/kubernetes/pki/ca.crt | openssl rsa -pubin -outform der 2>/dev/null | openssl dgst -sha256 -hex | sed 's/^.* //'
  
  
## cluster join

 kubeadm join [master_ip]:6443 --token [token] --discovery-token-ca-cert-hash sha256:[token hash 값]
