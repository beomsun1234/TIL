최범균님의 인프런 강의를 학습한 내용을 기록했습니다.

# 기능과 책임 분리

## 기능 분해

- 하나의 기능은 여러 하위 기능 이용해서 구현
- 분리한 하위 기능을 누가 제공할지 결정하는 것 → 객체 지향 설계의 기본 과정
- 기능은 곧 책임, 분리한 각 기능을 알맞게 분배


### 큰 클래스, 큰 메서드

클래스나 메서드가 커지면 절차 지향의 문제 발생

- 큰 클래스 : 많은 필드를 많은 메서드가 공유
 
- 큰 메서드 : 많은 변수를 많은 코드가 공유

- 여러 기능이 한 클래스/메서드에 섞여 있을 가능성

책임에 따라 알맞게 코드 분리 필요

### 클래스나 메서드가 커지지 않도록 책임을 분배/분리하는 방법]

  - 패턴 적용
  - 계산 기능 분리
  - 외부 연동 분리
  - 조건 분기는 추상화

### 패턴 적용

전형적인 역활 분리를 사용한다.

ex)

- 간단한 웹

    간단한 웹의 경우 컨트롤러, 서비스, DAO의 계층 분리 방식을 사용할 수 있다.

- 복잡한 도메인

    도메인이 복잡하다면 모델을 Entity, Value, Repository, Domain Service로 분리하여 사용할 수 있다.

- AOP

    여러 기능에 공통으로 포함된 기능은 Aspect를 사용해서 분리할 수 있다.

- GoF

    디자인 패턴을 사용해서 여러 기능을 분리할 수 있다.

### 계산 분리


![기능책임1](https://user-images.githubusercontent.com/68090443/175808835-cfdafeb1-fc52-4b09-8e5b-2931b1b2e56c.PNG)


포인트를 계산하는 부분을 별도의 클래스로 사용


### 연동 분리

![기능책임2](https://user-images.githubusercontent.com/68090443/175808853-8ef9b0c9-5f35-4e49-a9da-b17ffc9a012e.PNG)

네트워크, 메시징, 파일 등 연동 처리 코드 분리


### 조건 분기는 추상화

![기능책임3](https://user-images.githubusercontent.com/68090443/175808876-e489c038-ed58-4767-a273-aa50c189db99.PNG)


연속적인 if-else는 추상화 고민


## 역활 분리와 테스트

![기능책임4](https://user-images.githubusercontent.com/68090443/175808890-c82aca9e-aed3-4e6c-a1f4-d1f4733fcb33.PNG)

역활 분리가 잘 되면  테스트가 용이해진다.

### 분리연습 1

해당 코드는 평문 암호화하고 암호문을 담아 외부에 요청하고 응답을 다시 복호화한다.

    public class CashClient {
      private SecretKeySpec ketSpec;
      private IvParameterSpec ivSpec;

      private Res post(Req req) {
        String reqBody = toJson(req);

        //암호화 수행
        Cipher cipher = Cipher.getInstance(DEFAULT_TRANSFORM);
        cipher.init(Cipher.ENCRYPT_MODE, keySpec, ivSpec);
        String encReqBody = new String(Base64.getEncoder().encode(cipher.doFinal(reqBody)));

        //암호문 전송
        ResponseEntity<String> responseEntity = restTemplate.postForEntity(api, encReqBody, String.class);

        String encRespBody = responseEntity.getBody();

        //복호화 수행
        Cipher cipher2 = Cipher.getInstance(DEFAULT_TRANSFORM);
        cipher.init(Cipher.DECRYPT_MODE, keySpec, ivSpec);
        String encReqBody = new String(cipher.doFinal(Base64.getDecoder().decode(encRespBody)));

        return jsonToObj(respBody);
      }
    }

해당 코드의 기능과 책임을 분리하기 위해 계산 분리, 외부 연동 분리 방법을 적용할 수 있다. 이제 코드를 분리해보자!

    public class Cryptor {
      private SecretKeySpec keySpec;
      private IvParameterSpec ivSpec;
      
      
      //암호화
      public String encrypt(String plain) {
        Cipher cipher = Cipher.getInstance(DEFAULT_TRANSFORM);
        cipher.init(Cipher.ENCRYPT_MODE, keySpec, ivSpec);
        return new String(Base64.getEncoder().encode(cipher.doFinal(plain)));
      }
      
      //복호화
      public String decrypt(String encrypted) {
        Cipher cipher2 = Cipher.getInstance(DEFAULT_TRANSFORM);
        cipher2.init(Cipher.DECRYPT_MODE, keySpec, ivSpec);
        return new String(cipher.doFinal(Base64.getDecoder().decode(encrypted)));
      } 
    }

계산 기능(암호화, 복호화)은 Cryptor 클래스가 담당하며 CashClient에서 조립해서 사용하면된다.

조립해보자!

    public class CashClient {
      private Cryptor cryptor;
      
      private Res post(Req req) {
        String reqBody = toJson(req);

        //암호화 수행
        String encReqBody = cryptor.encrypt(reqBody)

        //암호문 전송
        ResponseEntity<String> responseEntity = restTemplate.postForEntity(api, encReqBody, String.class);

        String encRespBody = responseEntity.getBody();

        //복호화 수행
        String respBody = cryptor.decrypt(encRespBody)

        return jsonToObj(respBody);
      }
    }
    
### 분리연습 2

![기능책임5](https://user-images.githubusercontent.com/68090443/175808912-8e7db053-ec06-40b2-b5a3-e57cbf99b32a.PNG)

위 코드의 조건 분기를 추상화 해보자!

![기능책임6](https://user-images.githubusercontent.com/68090443/175808933-9a7241e1-0932-484d-9d39-b81f16dcf6cd.PNG)

Movie 클래스를 추상 클래스로 변경하고 각 하위 클래스가 포인트 기능을 제공하도록 변경한다.
