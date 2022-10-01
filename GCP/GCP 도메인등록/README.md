# GCP에 도메인 등록하기

gcp 인스턴스가 있다고 가정합니다.

도메인은 해당 링크에서 무료로 얻었습니다. https://xn--220b31d95hq8o.xn--3e0b707e/


## step 1
아래 사진과같이 우선 네티워크 서비스에 Cloud DNS 서비스에 들어가 줍니다.

![gcp](https://user-images.githubusercontent.com/68090443/193418417-ffc8893d-8187-4498-ae33-c1ea1c7ca9d2.PNG)


## step 2

영역을 만들어 줍니다.

![gcp2](https://user-images.githubusercontent.com/68090443/193418484-518c8f22-5c8d-4995-9afa-186a5698af25.PNG)


내용 작성

![gcp3](https://user-images.githubusercontent.com/68090443/193418608-da9dabff-9b18-4c3b-8bab-799b96480a0f.PNG)


## step 3

레코드 세트 추가

![gcp5](https://user-images.githubusercontent.com/68090443/193418851-84b54103-cd2b-4440-b7de-6705345bf456.PNG)


IPv4 주소에 인스턴스 ip 입력

![gcp6](https://user-images.githubusercontent.com/68090443/193418855-a76e0f64-2d25-4f27-908c-5cf8f9f91bd8.PNG)


## step 4

도메인을 구매한 페이지에서 연결 ip 설정


인스턴스 public ip를 기입해준다.

![gcp7](https://user-images.githubusercontent.com/68090443/193418862-ad6e71ee-2a21-4a4c-83c2-8f80a979647b.PNG)

