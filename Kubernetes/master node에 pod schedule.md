## master node에 pod schedule 가능하도록 하는 명령어

    kubectl taint nodes k8s-master-node node-role.kubernetes.io=master:NoSchedule
