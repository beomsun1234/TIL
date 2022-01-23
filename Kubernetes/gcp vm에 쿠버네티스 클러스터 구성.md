## gcp 우분투에 클러스터 구성(단일 노드)

### step

패키지 업그레이드

    sudo apt update
    sudo apt upgrade

스왑 끄기

    sudo swapoff -a

sysctl을 구성

    sudo modprobe overlay
    sudo modprobe br_netfilter

    sudo tee /etc/sysctl.d/kubernetes.conf<<EOF
    net.bridge.bridge-nf-call-ip6tables = 1
    net.bridge.bridge-nf-call-iptables = 1
    net.ipv4.ip_forward = 1
    EOF

    sudo sysctl --system

방화벽끄기

    ufw disable

도커 설치

    sudo apt install -y curl gnupg2 software-properties-common apt-transport-https ca-certificates
    curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
    sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
    sudo apt update
    sudo apt install -y containerd.io docker-ce docker-ce-cli

    # Create required directories
    sudo mkdir -p /etc/systemd/system/docker.service.d

    # Create daemon json config file
    sudo tee /etc/docker/daemon.json <<EOF
    {
    "exec-opts": ["native.cgroupdriver=systemd"],
    "log-driver": "json-file",
    "log-opts": {
        "max-size": "100m"
    },
    "storage-driver": "overlay2"
    }
    EOF

    # Start and enable Services
    sudo systemctl daemon-reload 
    sudo systemctl restart docker
    sudo systemctl enable docker

쿠버네티스 설치

    sudo apt-get update && sudo apt-get install -y apt-transport-https curl

    curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add -
    cat <<EOF | sudo tee /etc/apt/sources.list.d/kubernetes.list
    deb https://apt.kubernetes.io/ kubernetes-xenial main
    EOF

    sudo apt-get update
    sudo apt-get install -y kubelet kubeadm kubectl
    sudo apt-mark hold kubelet kubeadm kubectl

    systemctl daemon-reload

     systemctl restart kubelet

마스터 클러스터 생성

    kubuadm init

설치 후 

    export KUBECONFIG=/etc/kubernetes/admin.conf

마스터 노드에서 pod가 실행 가능하도록 설정

    kubectl taint nodes --all node-role.kubernetes.io/master-


### 대시보드 설치해보자

대시보드 설치

    kubectl apply -f https://raw.githubusercontent.com/kubernetes/dashboard/v2.0.0/aio/deploy/recommended.yaml


proxy 실행

    kubectl proxy --port=8001 --address=[your gcp private Ip] --accept-h
    osts='^*$'

백그라운드에서 실행

    nohup kubectl proxy --port=8001 --address=[your gcp private Ip] --accept-h
    osts='^*$' &

접속

    http://[your gcp public Ip]:8001/api/v1/namespaces/kubernetes-dashboard/services/https:kubernetes-dashboard:/proxy

결과
