# AWS 망분리 구축

- [x] vpc 생성
- [x] 외부,내부 서브넷 생성
- [x] ig-gw, nat-instance 설정
- [x] 보안그룹 설정
- [x] 내부망, 외부망 구성
- [x] bastion서버를 통해 내, 외부망 접근





# VPC

우선 VPC를 알아보기 전에 VPN에 대해서 알아보겠습니다!


## VPN(Virtual Private Network)


![vpn](https://user-images.githubusercontent.com/68090443/188599991-2216543b-7651-49bf-94c4-7dae639b0913.PNG)


VPN뜻은 가상의 사설망입니다. 만약 사진과 같이 다른지역에 있는 본점과 지점을 사설망으로 연결하고자 한다면 직접 전용망을 구축하거나 통신 사업자에게 전용망을 임대하고 장비를 도입하는데 막대한 비용이 소모딘다. 이를 위해 가상의 망 VPN을 사용하게 됩니다. VPN은 인터넷을 통해 전용망과 같은 사설 네트워크를 구성할 수 있도록 해주는 기술이다. 본점과 지점은 사용자는 실제로 같은 네트워크상에 있지만 논리적으로 다른 네트워크인것처럼 동작한다.

## VPC(Virtual Private Cloud)

AWS내부에서 가상 private network 망을 만들어줄 수 있게 해주는 서비스이다. AWS와 같은 클라우드 서비스에선 수많은 인스턴스들이 물리적으로 동일한 네트워크나 장비에서 돌아가게 되는데, 이를 논리적으로 분리셔켜준다고 할 수 있다.


![vpc 사영x](https://user-images.githubusercontent.com/68090443/188600018-260d76bd-f11a-46d2-b1c5-45420e878613.PNG)

위 사진 처럼 VPC 없이 인스턴스를 생성한다면 각 인스턴스들이 거미줄처럼 연결되어있어 시스템의 복잡도가 증가합니다.

![vpc사용o](https://user-images.githubusercontent.com/68090443/188600038-39f63de6-96a5-4536-8466-496db88e6ee6.PNG)

위 사진 처럼 VPC를 적용하면 VPC별로 네트워크를 구성할 수 있고 각 VPC에 따라 다르게 네트워크를 설정 할 수 있으며 완전히 독립된 네트워크처럼 작동합니다.



# 서브넷(Subnet)

    VPC의 IP 주소 범위입니다. 


서브넷은 VPC의 IP 주소를 나누어 리소스가 배치되는 물리적인 주소 범위를 뜻하며  VPC보다 대역폭이 낮다.


![서브넷](https://user-images.githubusercontent.com/68090443/188601115-44f6043b-edcf-4fb7-87b2-63bf88d73583.PNG)


서브넷은 다시 Public Subnet과 Private Subnet으로 나뉠 수 있다. 인터넷과 연결되어있는 서브넷을 public subnet이라고 하고 인터넷과 연결되어있지 않은 서브넷을 private subnet이라고 한다.

## AWS 서브넷 설정(public, private, bastion)

### public 서브넷

![public서브넷](https://user-images.githubusercontent.com/68090443/190850488-e34cbc29-95c1-43d1-ba2e-31f80e7eaac1.PNG)

### private 서브넷

![private 서브넷](https://user-images.githubusercontent.com/68090443/190850485-97f8276a-f662-4fd9-8f70-f8f242a6af41.PNG)

### bastion 서브넷

![바스티온서브넷](https://user-images.githubusercontent.com/68090443/190850493-50bff01b-003e-4ed5-aa29-d81dac294c3d.PNG)


# 라우팅테이블(Routing Table)

네트워크 요청이 발생하면 데이터는 우선 라우터로 향하게됩니다. 라우터란 목적지이고 라우팅 테이블은 각 목적지에 대한 이정표입니다.

각 subnet에는 default로 subnet과 밖을 연결해주는 라우터가 생성되고, 이 라우터는 라우팅 테이블을 가지고 있습니다. 

대상 ip address에 라우팅 경로를 정의하는 것으로 subnet에서 밖으로 나가는 outbound traffic에 대한 라우팅 경로를 정의합니다. 

모든 서브넷은 1개의 라우팅 테이블을 가져야 하며, 하나의 라우팅 테이블은 여러개의 서브넷에 중복되서 적용될 수 있다.


라우팅테이블을 만들때 VPC CIDR에 local이라는 라우팅이 저장되는데 이는 vpc안의 네트워크 범위를 가지는 요청은 해당 vpc내부에서 찾도록 한다는 뜻 입니다. 즉 VPC 내의 다른 subnet으로 traffic을 routing 합니다. 



Local: VPC 내의 다른 subnet으로 traffic을 routing 한다.


## 라우팅 테이블 생성

### public

![퍼블릭라우팅테이블](https://user-images.githubusercontent.com/68090443/190850549-55f6028b-734a-4477-9e3e-eeebd82aaef7.PNG)

### private

![프라이빗라우팅테이블](https://user-images.githubusercontent.com/68090443/190850554-2d18b1ac-aa5c-4c7c-8488-6acf9d5a4776.PNG)


### bastion

![바스티온라우팅](https://user-images.githubusercontent.com/68090443/190850560-e8cb548d-8334-45dd-b20c-98875462f869.PNG)


라우팅테이블을 생성 후 각 라우팅 테이블에 각 서브넷을 연결해준다.

![각라우팅테이블 서브넷 연결](https://user-images.githubusercontent.com/68090443/190850591-7c34e81c-f925-4574-b37d-948baf23330d.PNG)

사진과 같이 화면이 뜨면 라우팅테이블에 연결할 서브넷을 선택해주고 연결저장 버튼을 클릭하면 된다.

# 인터넷게이트웨이(Internet Gateway) 

라우팅 테이블에 local만 정의 되어 있다면 외부 인터넷으로 트래픽을 처리 할 수 없게됩니다. 이때 외부 인터넷 트래픽을 처리 하기 위해서는 인터넷 게이트웨이를 사용하면 됩니다.

예) 설정한 vpc안의 네트워크 범위를 가지는 요청은 local, 그외 요청은 인터넷 게이트웨이로 설정하기


    local은 기본적으로 생성되지만 외부 인터넷 트래픽을 처리하기 위해 인터넷 게이트웨이를 만들어주고
    목적지를 0.0.0.0/0 (모든 IPv4)로 타켓을 인터넷게이트웨이로 라우팅을 설정해주면 된다.


이러면 vpc 네트워크 범위를 가지는 트래픽은 vpc 내부로 라우팅되고 이 외 모든 트래픽은 인터넷 게이트웨이로 라우팅된다.


Internet gateway : internet gateway를 통해서, 외부 인터넷으로 traffic을 routing 한다.


### 인터넷 게이트웨이 생성

![인터넷게이트웨이](https://user-images.githubusercontent.com/68090443/190850676-259d4bb4-0122-4ebc-9843-c63febcee577.PNG)


### public과 bastion 인터넷 게이트웨이 연결


![퍼블릭과바스티온 igw연결](https://user-images.githubusercontent.com/68090443/190850692-9ead78a0-edd4-4a4a-9211-dce4754c0f08.PNG)



# NAT 게이트웨이 (NAT gateway)

보통 public 서브넷은 외부와 통신이 가능하지만 private 서브넷은 외부와 통신이 가능하지 않도록 설계한다.
그러나 private에서 외부와 통신이 필요할 경우 NAT 게이트웨이를 설정하면 된다.

public 서브넷과 private 서브넷은 같은 VPC안에 있으면 서로 통신할수있다는 점을 이용하여, NAT 게이트웨이를 생성해주면 마치 대리기사 역할처럼 public 서브넷이 외부 인터넷 데이터를 private 서브넷에게 대신 전달해주게 된다.

NAT Gateway는 내부에서 외부로의 접속만 가능하며 외부에서 NAT Gateway를 이용하여 접속하는 것은 불가능하다는 특징을 가지고 있다. 


NAT Gateway는 비용으 들기 때문에 직접 NAT Gateway를 만들어보자!


## NAT Instance 구성


![nat 인스턴스1](https://user-images.githubusercontent.com/68090443/190893397-4bd5319c-e1fb-4930-a3d7-e01f79158ac9.PNG)

우선 EC2를 생성하고 AMI를 위와 같이 선택해준다.


![넷인스턴스 vpc설정](https://user-images.githubusercontent.com/68090443/190893451-c06c3a89-cc51-4fd1-9fe8-3ba3cf54e79e.PNG)

NAT Instance의 VPC를 설정한다.


![private에 nat 인스턴스 적용](https://user-images.githubusercontent.com/68090443/190893475-a62960f6-525f-4c7f-b9f2-5fbab55fbd7c.PNG)


이후 Private 라우팅 테이블에 NAT Instance 적용해준다.




