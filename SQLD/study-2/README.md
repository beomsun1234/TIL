## ```데이터 모델과 성능```

```성능 데이터 모델링``` : DB 성능향상을 목적으로 설계
단계의 데이터 모델링 때부터 정규화, 반정규화, 테이
블통합, 테이블분할, 조인구조, PK, FK 등 여러 가지 
성능과 관련된 사항이 데이터 모델링에 반영될 수 있
도록 하는 것


```주의```

    분석/설계 단계에서 데이터 모델에 성능을 고려한 데이터 모델링을 수행할 경우 성능저하에 따른 재업무 비용을 최소화 할 수 있는 기회를 가지게 된다. 데이터의 증가가 빠를수록 성능저하에 따른 성능개선 비용은 기하급수적으로 증가하게 된다


### ```성능 데이터 모델링 고려사항 순서```

    1. 데이터 모델링을 할 때 정규화를 정확하게 수행

    2. DB 용량산정을 수행한다. 
    
    3. DB에 발생되는 트랜잭션의 유형을 파악한다. 
    
    4. 용량과 트랜잭션의 유형에 따라 반정규화를 수행

    5. 이력모델의 조정, PK/FK조정, 슈퍼/서브타입 조정

    6. 성능관점에서 데이터 모델을 검증한다.


### ```함수적종속성```
    - 함수적 종속성 : 데이터들이 어떤 기준 값에 의해 종
    속되는 현상

### ```정규화```
    - 정규화 : 반복적인 데이터를 분리하고 각 데이터가 종
    속된 테이블에 적절하게 배치되도록 하는 것
    칼럼에 의한 반복, 중복적인 속성 값을 갖는 형태는 1
    차 정규화의 대상

### ```반정규화```
    - 반정규화 : 정규화된 엔터티, 속성, 관계에 대해 시스
    템의 성능향상과 개발과 운영의 단순화를 위해 중복, 통합, 분리 등을 수행하는 데이터 모델링의 기법
    일반적으로 정규화시 입력/수정/삭제 성능이 향상되
    며 반정규화시 조인 성능이 향상된다. 

### ```반정규화 절차```
    1. 반정규화 대상조사(범위처리빈도수, 범위, 통계성)

    2. 다른 방법유도 검토(뷰, 클러스터링, 인덱스 조정)

    3. 반정규화 적용(테이블, 속성, 관계 반정규화)



### ```반정규화 대상조사```
    1. 자주 사용되는 테이블에 접근하는 프로세스의 수가 많고 항상 일정한 범위만을 조회하는 경우

    2. 테이블에 대량의 데이터가 있고 대량의 데이터 범위를 자주 처리하는 경우에 처리범위를 일정하게 줄이지 않으면 성능을 보장할 수 없는 경우

    3. 통계성 프로세스에 의해 통계 정보를 필요로 할 때 별도의 통계테이블을 생성한다. 

    4. 테이블에 지나치게 많은 조인이 걸려 데이터를 조회하는 작업이 기술적으로 어려울 경우

### ```다른 방법유도 검토```

    1. 지나치게 많은 조인이 걸려 데이터를 조회하는 작
    업이 기술적으로 어려울 경우 VIEW를 사용한다. 2. 대량의 데이터처리나 부분처리에 의해 성능이 저하
    되는 경우 클러스터링을 적용하거나 인덱스를 조정함

    3. 대량의 데이터는 PK의 성격에 따라 부분적인 테이
    블로 분리할 수 있다. (파티셔닝 기법)

    4. 응용 애플리케이션에서 로직을 구사하는 방법을 변
    경함으로써 성능을 향상시킬 수 있다.


### ```반정규화의 기법(테이블, 칼럼, 관계)```

#### ```테이블 반정규화```
- ```테이블 병합(1:1관계, 1:M관계, 슈퍼/서브타입)```

        1. 1:1관계를 통합하여 성능향상
        2. 1:M관계를 통합하여 성능향상
        3. 슈퍼/서브 관계를 통합하여 성능향상

- ```테이블분할(수직분할, 수평분할)```

        1. 칼럼단위 테이블을 디스크 I/O를 분산처리하기 위
        해 테이블을 1:1로 분리하여 성능향상

        2. 로우단위로 집중 발생되는 트랜잭션을 분석하여 디
        스크 I/O 및 데이터 접근의 효율성을 높여 성능을 향
        상하기 위해 로우단위로 테이블을 쪼갬

- ```테이블추가(중복, 통계, 이력, 부분테이블 추가)```

        1. 다른 업무이거나 서버가 다른 경우 동일한 테이블
        구조를 중복하여 원격조인을 제거하여 성능 향상

        2. SUM, AVG 등을 미리 수행하여 계산해 둠으로써 
        조회 시 성능을 향상

        3. 이력테이블 중에서 마스터 테이블에 존재하는 레코
        드를 중복하여 이력테이블에 존재시켜 성능 향상

        4. 하나의 테이블의 전체 칼럼 중 자주 이용하는 집중
        화된 칼럼들이 있을 때 디스크 I/O를 줄이기 위해 해
        당 칼럼들을 모아놓은 별도의 반정규화된 테이블을 
        생성

- ```칼럼 반정규화```

        1. 중복칼럼 추가 : 조인에 의해 처리할 때 성능저하
        를 예방하기 위해 중복된 칼럼을 위치시킴

        2. 파생칼럼 추가 : 트랜잭션이 처리되는 시점에 계산
        에 의해 발생되는 성능저하를 예방하기 위해 미리 값
        을 계산하여 칼럼에 보관

        3. 이력테이블 칼럼추가 : 대량의 이력데이터를 처리
        할 때 불특정 날 조회나 최근 값을 조회할 때 나타날 
        수 있는 성능저하를 예방하기 위해 이력테이블에 기
        능성 칼럼(최근값 여부, 시작과 종료일자 등)을 추가함

        4. 응용시스템 오작동을 위한 칼럼 추가 : 업무적으로
        는 의미가 없지만 사용자의 실수로 원래 값으로 복구
        하기 원하는 경우 이전 데이터를 임시적으로 중복하
        여 보관하는 기법

- ```관계 반정규화```

        중복관계 추가 : 데이터를 처리하기 위한 여러 경로를 
        거쳐 조인이 가능하지만 이 때 발생할 수 있는 성능
        저하를 예방하기 위해 추가적인 관계를 맺는 방법


### 알아두기

- ```로우 체이닝``` : 로우의 길이가 너무 길어서 데이터 블
록 하나에 데이터가 모두 저장되지 않고 두 개 이상
의 블록에 걸쳐 하나의 로우가 저장되어 있는 형태
- ```로우 마이그레이션``` : 데이터블록에서 수정이 발생하면 
수정된 데이터를 해당 데이터 블록에서 저장하지 못
하고 다른 블록의 빈 공간을 찾아 저장하는 방식


        로우 체이닝과 로우 마이그레이션이 발생하여 많은 
        블록에 데이터가 저장되면 DB 메모리에서 디스크 
        I/O가 발생할 때 많은 I/O가 발생하여 성능저하 발생
        트랜잭션을 분석하여 적절하게 1:1관계로 분리함으로
        성능향상이 가능하도록 해야 한다. 

### ```PK에 의해 테이블을 분할하는 방법(파티셔닝)```

    1. RANGE PARTITION : 대상 테이블이 날짜 또는 
    숫자값으로 분리가 가능하고 각 영역별로 트랜잭션이 
    분리되는 경우
    2. LIST PARTITION : 지점, 사업소 등 핵심적인 코
    드값으로 PK가 구성되어 있고 대량의 데이터가 있는 
    테이블의 경우
    3. HASH PARTITION : 지정된 HASH 조건에 따라 
    해시 알고리즘이 적용되어 테이블이 분리

### ```테이블에 대한 수평/수직분할의 절차```

    1. 데이터 모델링을 완성한다. 
    2. DB 용량산정을 한다. 
    3. 대량 데이터가 처리되는 테이블에 대해 트랜잭션 처리 패턴을 분석한다. 
    4. 칼럼 단위로 집중화된 처리가 발생하는지, 로우 단
    위로 집중화된 처리가 발생하는지 분석하여 집중화된 
    단위로 테이블을 분리하는 것을 검토한다.


### ```슈퍼/서브 타입 모델``` 
- 슈퍼/서브 타입 모델 : 업무를 구성하는 데이터의 특
징을 공통과 차이점의 특징을 고려하여 효과적 표현



### ```슈퍼/서브 타입 데이터 모델의 변환기술```

    1. 개별로 발생되는 트랜잭션에 대해서는 개별 테이블
    로 구성(OneToOne Type)

    2. 슈퍼타입+서브타입에 대해 발생되는 트랜잭션에 대
    해서는 슈퍼+서브타입 테이블로 구성(Plus Type)

    3. 전체를 하나로 묶어 트랜잭션이 발생할 때는 하나
    의 테이블로 구성(Single Type, All in One Type)


### ```인덱스 특성을 고려한 PK/FK DB 성능향상```

    인덱스의 특징은 여러 개의 속성이 하나의 인덱스로 
    구성되어 있을 때 앞쪽에 위치한 속성의 값이 비교자
    로 있어야 좋은 효율을 나타낸다. 앞쪽에 위치한 속성의 값이 가급적 ‘=’ 아니면 최소한 
    범위 ‘BETWEEN’ ‘<>’ 가 들어와야 효율적이다


### ```분산 DB를 만족하기 위한 6가지 투명성```
    1. 분할 투명성(단편화) : 하나의 논리적 Relation이 
    여러 단편으로 분할되어 각 사본이 여러 site에 저장

    2. 위치 투명성 : 사용하려는 데이터의 저장 장소 명
    시 불필요, 위치정보가 시스템 카탈로그에 유지

    3. 지역사상 투명성 : 지역 DBMS와 물리적 DB 사이
    의 Mapping 보장

    4. 중복 투명성 : DB 객체가 여러 stie에 중복 되어 
    있는지 알 필요가 없는 성질

    5. 장애 투명성 : 구성요소의 장애에 무관한 트랜잭션
    의 원자성 유지

    6. 병행 투명성 : 다수 트랜잭션 동시 수행시 결과의 
    일관성 유지, TimeStamp, 분산 2단계 Locking 이용
    
### ```분산 DB 장-단점```

    장점 : 지역 자치성, 신뢰성 가용성, 효용성 융통성, 빠른 응답속도, 비용절감, 각 지역 사용자 요구 수용

    단점 : 비용증가, 오류의 잠재성 증대, 설계 관리의 
    복잡성, 불규칙한 응답 속도, 통제의 어려움, 데이터 
    무결성 위협


### ```분산 DB 설계를 고려해야 하는 경우```

    1. 성능이 중요한 사이트

    2. 공통코드, 기준정보, 마스터 데이터의 성능향상

    3. 실시간 동기화가 요구되지 않는 경우, 거의 실시간
    의 업무적인 특징을 가지고 있는 경우(?)

    4. 특정 서버에 부하가 집중되어 부하를 분산

    5. 백업 사이트 구성하는 경우
