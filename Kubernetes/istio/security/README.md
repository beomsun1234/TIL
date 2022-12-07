# istio end-user authentication(jwt token)

최종사용자 인증

사용자 요청이 애플리케이션 코드에 도달하기 전에 JWT token을 통해 검사한다. 

    1. 요청 헤더 내부의 JWT 토큰 유효성 검사
    2. 유효한 JWT가 포함된 요청을 애플리케이션 코드로 전달
    3. 유효하지 않은 JWT로 트래픽 거부
    
    
## 실습


### jwk, jwt 만들기

openssl을 통해 인증서를 만들어준다.


만들어진 인증서를 바탕으로 jwk, jwt를 만든다. [자바코드](https://github.com/beomsun1234/TIL/blob/main/Java/pem%ED%8C%8C%EC%9D%BC%20%EC%9D%BD%EC%96%B4%EC%84%9C%20jwk.json%20%EB%A7%8C%EB%93%A4%EA%B8%B0.md)

### istio authentication 등록

orderservice에 authentication을 적용해 보자!

Istio RequestAuthentication Resource에 위에서 만든 jwks를 설정한다.
    
    apiVersion: "security.istio.io/v1beta1"
    kind: "RequestAuthentication"
    
    ....
    ...
    
    jwtRules:
    - issuer: "ISSUER"
      jwks: |
        [jks json]
                

orderservice-auth.yaml

    apiVersion: "security.istio.io/v1beta1"
    kind: "RequestAuthentication"
    metadata:
      name: "order-jwt-request-auth"
      namespace: default
    spec:
      selector:
        matchLabels:
          app: orderservice
      jwtRules:
      - issuer: "ISSUER"
        jwks: |
          {"keys":[{"e":"AQAB","kty":"RSA","n":"ALzzw1zcCT9Zqwqnc75Iio-D9J5_hcRm-MNjbYYHN8S0OVI4pdJ2brwED95R_FoLhI1ORDuMq1_Zfj7BgeC6oW-fAz6ypP3zHLQ6a6KdXZ5q-45pq6LWVifDrNH4yCXo2rSopdq-8I_HVH1h4xsJJPZySonRJk3Vqm0G-B2lJthvV2DZjCc5OCxxMbBr9PhqsPHQT6wGBR7X1BqVFAjVAoXp2-QLS6MbvXjazqf5fhfo6fvEbFEf4Dbu2BSN-ikMfoyR57rXJZU-9QpVaifrtO3Ts_v4PnRYZtbDPRQRdlw4azxen4VHzrXx-GaLynFbHILXLfUrAp9pgzsrZ318bq0="}]}
    ---
    apiVersion: security.istio.io/v1beta1
    kind: AuthorizationPolicy
    metadata:
      name: order-auth-policy
      namespace: default
    spec:
      selector:
        matchLabels:
          app: orderservice
      action: ALLOW
      rules:
      - from:
        - source:
            requestPrincipals: ["*"]


### 유효한 토큰 요청

![image](https://user-images.githubusercontent.com/68090443/206161751-44348b7b-4db5-4b35-bd95-f79f50bf4661.png)


### 유효하지 않은 토큰

![image](https://user-images.githubusercontent.com/68090443/206161615-dc9fa42f-63af-4959-b62f-fd76535abc4b.png)

### 토큰 없이 요청

#### authentication을 등록한 서비스

![image](https://user-images.githubusercontent.com/68090443/206160604-9aeb4303-5b2e-4641-a4f5-6920875f14ac.png)

#### authentication을 등록하지 않은 서비스

![image](https://user-images.githubusercontent.com/68090443/206160391-5a165082-66bc-4927-9514-0898c79a9dec.png)




