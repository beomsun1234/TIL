# 연관관계 매핑

- 객체는 참조를 사용하여 연관 관계를 맺고 테이블은 외래 키를 사용해서 연관 관계를 맺는다.

- 관계가 있는 다른 데이터를 참조한다는 점에서 동일하지만, 참조와 외래 키는 완전히 다른 특징을 갖는다.


## 연관관계가 왜 필요한가?

객체 테이블에 맞추어 모델링


![연관관계왜필요](https://user-images.githubusercontent.com/68090443/135614035-f9940350-1d87-441e-9626-efd707ff9f53.PNG)


- 참조 대신 외래 키를 그대로 사용한다


회원 클래스

    @Entity
    public class Member {

      @Id @GeneratedValue
      private Long id;

      @Column(name = "USERNAME") 
      private String name;

      @Column(name = "TEAM_ID")
      private Long teamId;
      ...
      }

팀클래스

  @Entity
  public class Team {

    @Id 
    @GeneratedValue
    private Long id;
    private String name;
    ...
    }

팀과 회원을 저장하는 코드

    //팀 저장
    Team team = new Team();
    team.setName("wooteco"); 
    em.persist(team);

    //회원 저장
    Member member = new Member();
    member.setName("conas");
    member.setTeamId(team.getId());
    em.persist(member);



여기서 회원의 팀을 찾기 위해선 어떤 코드를 작성해야하나?

    Member findMember = em.find(Member.class, member.getId());

    Long findTeamId = findMember.getId();
    Team findTeam = em.find(Team.class, findTeamId);
    
    
    
- ``연관관계가 없다면 위와 같이, member의 team을 가져오는데 member를 꺼내오고, 
id를 가져와서 다시 팀을 가져오기때문에 회원의 팀을 가져오기 위해 많은 비용이 듭니다.
그리고 객체 지향스럽지 않은 코드가 됩니다.``

-  ``객체를 테이블에 맞추어 데이터 중심으로 모델링하면, 협력 관계를 만들 수 없습니다.``

    - 테이블은 외래 키로 조인을 사용해서 연관된 테이블을 찾습니다.
    - 객체 참조를 사용해서 연관된 객체를 찾습니다.
    - 테이블과 객체 사이에는 이런 큰 간격이 있습니다.


---


## 연관관계 매핑을 이해하기 위한 키워드

- 방향(회원/팀이라는 관계로 생각해보자)

      	단방향 : 회원 → 팀 OR 팀 → 회원   둘 중 한 쪽만 참조하는 관계
      
      	양방향 : 회원 → 팀 AND 팀 → 회원   회원과 팀 양쪽 모두 서로를 참조하는 관계


	```방향은 객체관계에만 존재하고 테이블 관계는 항상 양방향이다.```

- 다중성

		1:1 (일대일)
		1:N (일대다 혹은 다대일)
		N:M (다대다)


- 연관관계의 주인 
 
	```양방향 연관관계를 만들 떄 연관 관계의 주인을 정해야 한다.```

---

## 단방향 연관관계


![단방향여과과계](https://user-images.githubusercontent.com/68090443/135614098-363686d9-9097-467a-8eda-c8af23ecd7ca.PNG)


### 객체 연관 관계
- 회원 객체(Member)는 Member.team 필드(멤버 변수)로 팀 객체와 연관관계를 맺는다.
- 회원 객체와 팀 객체는 단방향 관계이다. 
	- 회원은 Member.team 필드를 통해 팀을 알 수 있지만, 팀 객체로 소속된 회원들을 알 수 없기 때문입니다. member에서 team 의 조회는 member.getTeam()으로 가능하지만, team에서 member 를 접근하는 필드는 없다.
	



### 테이블 연관관계

- 회원 테이블은 TEAM_ID 외래 키로 팀 테이블과 연관관계를 맺는다.

- 회원 테이블과 팀 테이블은 양방향 관계이다.
	- 회원 테이블의 TEAM_ID 외래 키를 통해서 회원과 팀을 조인할 수 있고, 반대로 팀과 회원도 조인할 수 있습니다. 예를 들어, MEMBER 테이블의 TEAM_ID 외래 키 하나로 MEMBER JOIN TEAM 과 TEAM JOIN MEMBER 둘 다 가능


회원 중심

 	SELECT *
 	FROM MEMBER M INNER JOIN TEAM T 
    ON M.TEAM_ID = T.TEAM_ID

		
팀 중심

	SELECT * 
    FROM TEAM T INNER JOIN MEMBER M
    ON M.TEAM_ID = T.TEAM_ID



#### 객체 연관관계와 테이블 연관관계의 가장 큰 차이

- 참조를 통한 연관간계는 언제나 단방향. 객체간에 연관관계를 양방향으로 만들고 싶으면 반대쪽에도 필드를 추가해서 참조를 보관해야 한다. 결국 연관관계를 하나 더 만들어야 한다.
- 이렇게 양쪽에서 서로 참조하는 것을 양방향 연관관계라 한다. 정확히 이야기하면 이것은 양방향 관계가 아니라 서로 다른 단방향 관계 2개다.
- 반면에 테이블은 외래 키 하나로 양방향으로 조인할 수 있다.



```정리```
- 객체는 참조로 연관관계를 맺습니다.
- 테이블은 외래 키로 연관관계를 맺습니다.
- 참조를 사용하는 객체의 연관관계는 단방향입니다.
- 외래 키를 사용하는 테이블의 연관관계는 양방향입니다. 





### 연관관계 사용

객체 관계 매핑

    @Entity
    @Getter
    @Setter
    pubilc class Member {
        @Id
        @Column(name = "MEMBER_ID")
        private String id;

        private String username;

        //연관관계 매핑
        @ManyToOne
        @JoinColumn(name = "TEAM_ID")
        private Team team;
    }

    @Entity
    @Getter
    @Setter
    pubilc class Team {
        @Id
        @Column(name = "TEAM_ID")
        private String id;

        private String name;
    }


연관관계 저장

    //팀 저장
    Team team = new Team();
    team.setName("TeamA");
    em.persist(team);

    //회원 저장
    Member member = new Member(); 
    member.setName("conas");
    member.setTeam(team); //단방향 연관관계 설정, 참조 저장 
    em.persist(member);
    
    
참조로 연관관계 조회(객체 그래프 탐색)

    //조회
    Member findMember = em.find(Member.class, member.getId());
    //참조를 사용해서 연관관계 조회
    Team findTeam = findMember.getTeam();

연관관계 수정

    // 새로운 팀B
    Team teamB = new Team();
    teamB.setName("TeamB");
    em.persist(teamB);

    // 회원1에 새로운 팀B 설정
    member.setTeam(teamB);

연관관계 제거

    Member member1 = em.find(Member.class, "member1");
    member1.setTeam(null); //연관관계 제거
    
연관된 엔티티 삭제


    member1.setTeam(null); //회원1 연관관계 제거
    member2.setTeam(null); //회원2 연관관계 제거
    em.remove(team); //팀 삭제
    

### @ManyToOne

다대일 관계를 나타내는 매핑 정보


|속성|기능|기본값|
|------|---|---|
|optional|false로 설정하면 연관된 엔티티가 항상 있어야 함|true|
|fetch|글로벌 패치 전략 설정| @ManyToOne=FetchType.EAGER, @OneToMany=FetchType.LAZY|
|cascade|영속성 전이 기능 사용||
|targetEntity|연관된 엔티티의 타입 정보 설정 (targetEntity = Member.class 식으로 사용||

  
### @JoinColumn

|속성|기능|기본값|
|------|---|---|
|name|매핑할 외리 키 이름|필드명 + _ + 참조하는 테이블의 기본 키 컬럼명|
|referencedColumnName|외래 키가 참조하는 대상 테이블의 컬럼명|참조하는 테이블의 기본 키 컬럼명|
|foreignKey(DDL)|외래 키 제약조건을 직접 지정. 테이블을 생성할 때만 사용|기본값|
|unique, nullable, insertable, updatable, columnDefinition, table|@Column 속성과 같음|기본값|

---
## 양뱡향 연관관계

![양방향연관과계](https://user-images.githubusercontent.com/68090443/135614163-47c72c0d-2382-48c1-be1f-029ff8f44203.PNG)


``회원과 팀은 다대일 관계이며. 반대로 팀에서 회원은 일대다 관계이다. 일대다 관계는 여러 건과 연관관계를 맺을 수 있으므로 컬렉션을 사용해야 한다.``

- 회원 -> 팀 (Member.team)

- 팀 -> 회원 (Team.members)


![테이블여관관계](https://user-images.githubusercontent.com/68090443/135614262-58456558-6484-4ea8-9a16-399f2ee2e3e3.PNG)


Team 클래스는 List 필드를 갖지만 데이터베이스의 TEAM 테이블은 member id을 가질 필요가 없다.
왜냐면 DB에서는 MEMBER 테이블의 TEAM_ID 외래키 하나로도 양방향을 구현할 수 있기 때문이다.


#### 양방향 매핑의 장점
  - 단방향 매핑으로 이미 연관관계 매핑은 완료
  - 양방향은 반대 방향으로 객체 그래프 탐색 기능이 추가된 것
  - 단방향 매핑을 잘하고 양방향 매핑은 필요할 때 추가해도 됨

### 양방향 연관관계 매핑

Member class

    @Setter
    @Getter
    @Entity
    public class Member {

     @Id
     @Column(name = "MEMBER_ID")
     private String id;

     private String username;

     @ManyToOne
     @JoinColumn(name="TEAM_ID")
     private Team team;

     // 연관관계 설정
     public void setTeam(Team team) {
       this.team = team;
     }
    }


Team class


    @Setter
    @Getter  
    @Entity
    public class Team {

    @Id
    @Column(name = "TEAM_ID")
    private String id;

    private String name;

    @OneToMany(mappedBy = "team")
    private List<Member> members = new ArrayList<Member>();

	}

팀과 회원은 일대다 관계이기에 team 클래스에 List 타입 필드를 추가했다.
그리고 @OneToMany 어노테이션으로 매핑 정보를 표시했다. mappedBy 속성은 양방향 매핑 시 반대쪽 매핑(Member 클래스의 Team team)값을 주면 된다.



### 일대다 컬렉션 조회
일대다 방향으로 객체 그래프 탐색

    Team team = em.find(Team.class, "team1");
    List<Member> members = team.getMembers(); // (팀 -> 회원) 객체 그래프 탐색

    for (Member member : members) {
    System.out.println("member.username = " + member.getUsername());
    }

    // === 결과 ===
    // member.username = 회원1
    // member.username = 회원2

---

## 연관관계 주인

- 객체에는 양방향 연관관계는 없다.

- 서로 다른 단방향 연관관계 2개를 어플리케이션 로직으로 양방향인 것처럼 보이게 할 뿐
데이터베이스 테이블은 외래 키 하나로 양쪽이 서로 조인 가능

- 테이블은 외래 키 하나만으로 양방향 연관관계 가능

- 엔티티를 양방향 연관관계로 설정하면 객체의 참조는 둘인데 외래키는 하나

따라서 둘 사이에 차이가 발생

``두 객체 연관관계 중 하나를 정해서 테이블의 외래 키를 관리해야 하는데 이것을 연관관계의 주인(Owner)이라 한다``
어떤 연관관계를 주인으로 정할지는 mappedBy 속성을 사용하면 됩니다.

	- 주인은 mappedBy 속성을 사용하지 않는다.
	- 주인이 아니면 mappedBy 속성을 사용해서 속성의 값으로 연관관계의 주인을 지정해야 한다.
    - 연관관계의 주인을 정한다는 것은 사실 외래 키 관리자를 선택하는 것이다.
    - 인이 아닌 쪽은 읽기만 할 수 있다
    - 연관관계의 주인만이 데이터베이스 연관관계와 매핑되고 외래 키를 관리(등록, 수정, 삭제)할 수 있다


![연관과계주이](https://user-images.githubusercontent.com/68090443/135614345-af09eb04-ca5a-4fc0-b1e7-48334ac3382c.PNG)


Member와 Team 둘 중 어떤 것을 연관관계의 주인으로 정해야 할까??

- 회원 -> 팀) 방향

      class Member {

       @ManyToOne
       @JoinColumn(name = "TEAM_ID")
       private Team team;
       // ...
      }

 - 팀 -> 회원 방향

      class Team {

        @OneToMany
        private List<Member> members = new ArrayList<>();
        // ...
      }
    
 연관관계의 주인을 정한다는 것은 사실 외래 키 관리자를 선택하는 것입니다.
 
 그림의 회원 테이블에 있는 TEAM_ID 외래 키를 관리할 관리자를 선택해야 한다. 만약 회원 엔티티에 있는 Member.team을 주인으로 선택하면 자기 테이블에 있는 외래 키를 관리하면 된다. 하지만 팀 엔티티에 있는 Team.members를 주인으로 선택하면 물리적으로 전혀 다른 테이블의 외래 키를 관리해야 합니다. 왜냐하면 이 경우 Team.members가 있는 Team 엔티티는 TEAM 테이블에 매핑되어 있는데 관리해야할 외래 키는 MEMBER에 있기 때문입니다.
 
#### ``TIP : 외래 키가 있는 곳을 연관 관계의 주인으로 정하면 된다``

### 연관관계의 주인은 외래 키가 있는 곳


![연관관계주인은외래키](https://user-images.githubusercontent.com/68090443/135614411-f7b23687-f207-4058-b0b1-5424c4ca7ae4.PNG)



- 회원 테이블이 외래 키를 가지고 있으므로 Member.team이 주인
- 주인이 아닌 Team.members에는 mappedBy="team" 속성을 사용해서 주인이 아님을 설정

여기서 mappedBy 값으로 사용된 team은 연관관계의 주인인 Member 엔티티의 team 필드를 말함


    데이터베이스 테이블의 다대일, 일대다 관계에서는 항상 다 쪽이 외래키를 가짐.
    다 쪽인 @ManyToOne은 항상 연관관계의 주인이 되므로 mappedBy를 설정할 수 없다.
    
### 왜 연관 관계의 주인을 지정해야하는가?

객체에서 양방향 연관 관계(Member, Team) 관리 포인트가 두 개일 때는 테이블과 매핑을 담당하는 JPA입장에서 혼란을 주게 됩니다.

즉, Member에서Team를 수정할 때 FK(Foreign Key)를 수정할 지, Team에서  Member를 수정할 때 FK(Foreign Key)를 수정할 지를 결정하기 어려운 것입니다.

그렇기 때문에 두 객체 사이의 연관 관계의 주인을 정해서 명확하게 Member에서 Team를 수정할 때만 FK를 수정하겠다! 라고 정하는 것입니다.


## 양방향 연관관계 저장

    public void save() {

     // 팀1 저장
     Team team1 = new Team("team1", "팀1");
     em.persist(team1);

     // 회원1 저장
     Member member1 = new Member("member1", "회원1");
     member.setTeam(team1);  // 연관관계 설정 member1 -> team1
     em.persist(member1);

     // 회원2 저장
     Member member2 = new Member("member2", "회원2");
     member2.setTeam(team1); // 연관관계 설정 member2 -> team1
     em.persist(member2);
    }
    
  코드 실행 후 DB에서 회원테이블을 조회해보면 TEAM_ID 우리가 저장했던 team1이 저장되어 있다. 양방향 연관관계는 연관관계의 주인이 외래 키를 관리한다.
  
    team1.getMembers().add(member1); // 무시(연관관계의 주인이 아님)
    team1.getMembers().add(member2); // 무시(연관관계의 주인이 아님)
    
해당 코드가 추가로 있어야 할 것같지만 주인이 아닌 방향은 값을 설정하지 않아도 DB에 외래 키 값이 정상적으로 입력된다.주인이 아닌 곳에 입력된 값은 외래 키에 영향을 주지 않는다.

---

## 양방향 연관관계의 주의점


    //회원1 저장
    Member member1 = new Member("member1", "회원1");
    em.persist(member1);

    Team team = new Team("team1", "팀1");
    //주인이 아닌 곳만 연관관계 설정
    team.getMembers().add(member1);
    em.persist(team1);
    
    
    
회원1 저장하고 팀의 컬렉션에 담은 후에 팀을 저장하면 정상적으로 db에 저장되어 있을까?
DB에 회원테이블을 조회하면 외래 키 TEAM_ID에 team1이 아닌 null 값이 입력되어 있다. 왜냐하면 ``연관관계의 주인이 아닌 Team.members에만 값을 저장했고 연관관계의 주인인 Member.team에 값을 입력하지 않았기 때문에, TEAM_ID 외래 키의 값도 null이 저장됩니다.``

### 순수한 객체까지 고려한 양방향 연관관계
- 객체 관점에서 양쪽 방향에 모두 값을 입력해주는 것이 가장 안전 하다.
- 양쪽 방향 모두 값을 입력하지 않으면 JPA를 사용하지 않는 순수한 객체 상태에서 심각한 문제가 발생할 수 있습니다.

데이터베이스뿐만 아니라 객체도 함께 고려해야 한다.


    Team team1 = new Team("team1", "팀1");
    Member member1 = new Member("member1", "회원1");
 

    member1.setTeam(team1);


    List<Member> members = team1.getMembers();
    System.out.println("members.size = " + members.size());
    
코드를 실행하면 members.size = 0 이 나온다. 이유는 Member.team에만 연관관계를 설정하고 반대 방향은 연관관계를 설정하지 않았기 때문에 마지막 줄에서 팀에 소속된 회원이 몇 명인지 출력해보면 결과는 0이 나온다.

ORM은 객체와 데이터베이스 둘 다 고려(양쪽다 관계를 설정해야한다.)

양쪽 모두 관계를 설정해보자!

    Team team1 = new Team("team1", "팀1");
    em.persist(team1);
    
    Member member1 = new Member("member1", "회원1");
 	
    //양방향 연관관계 설정
    member1.setTeam(team1);
    team1.getMembers().add(member1);
	//-----
    em.persist(member1);
    
    List<Member> members = team1.getMembers();
    System.out.println("members.size = " + members.size());

결과는 기대했던 members.size = 1이 나온다.



### 연관관계 편의 메소드

- 양방향 연관관계는 결국 양쪽 다 신경을 써야 한다.
- 실수로 둘 중 하나만 호출해서 양방향이 깨질 수 있다


    public class Member{

      private Team team;

      public void setTeam(Team team) {
        this.team = team;
        team.getMembers().add(this);
      }
      // ...
    }
    
 setTeam() 메서드 하나로 양방향 관계를 모두 설정하도록 변경했다.
 
 	Team team1 = new Team("team1", "팀1");
 	em.persist(team1);
  
  	Member member1 = new Member("member1", "회원1");
  	member1.setTeam(team1);
  	em.persist(member1);
    
 ``이렇게 한 번에 양방향 관계를 설정하는 메서드를 연관관계 편의 메서드라 한다.``
 
 
### 연관관계 편의 메소드 작성 시 주의사항

    member.setTeam(team1);
    member.setTEam(team2);
    Member findMember = teamA.getMember(); // member1이 여전히 조회된다.
    
  
teamB로 변경할 때 teamA와 member1간의 관계를 제거하지 않았기 때문에 teamA.getMember() 메서드를 실행했을 때 member1이 남아있습니다. 따라서 연관관계를 변경할 때는 기존 팀이 있으면 기존 팀과 회원의 연관관계를 삭제하는 코드를 추가해야 한다.
  
  
     public void setTeam(Team team){

     if(this.team != null) {	// this.team이 null이 아니면 이 member객체는 team이 있음을 의미
       this.team.getMembers().remove(this);		// 해당 팀의 멤버에서 삭제
     }
     this.team = team;
     team.getMembers().add(this);
    }
