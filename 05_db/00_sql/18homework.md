1. 우리가 사용하는 SQLite는 RDBMS에 속한다. RDBMS의 특징을 2가지만 작성하시오.

   - RDB : 관계형 데이터 모델에 기초를 둔 데이타베이스 => 2차원 테이블 + 독립성 높음 + 관계조작에 용이
   - RDBMS : 관계형 데이터베이스를 생성하고, 수정하고, 관리할 수 있는 소프트웨어
     1. 모든 데이터를 2차원 테이블로 표현
     2. 테이블은 row(record, tuple)과 column(field, item)으로 이루어진 기본 데이터 저장 단위
     3. 상호관련성을 가진 테이블의 집합
     4. 만들거나 이용하기도 쉽지만, 무엇보다도 확장이 용이하다는 장점을 가짐
     5. 데이터 베이스의 설계도 ER 모델
     6. ER 모델에 따라, 데이터베이스가 만드어지며, 데[이터베이스는 하나 이상의 테이블로 구성 됨. ER모델에서 엔티티를 기반으로 테이블이 만들어짐

   

2. 다음 중 맞으면 T, 틀리면 F를 작성하시오. 

   1. RDBMS를 조작하기 위해서는 SQL 문을 사용한다. [  T  ] 
   2. SQL에서 명령어는 대문자로 써야만 동작한다. [ F ] 
   3. 일반적인 SQL 문에서 명령어는 세미콜론(;) 으로 끝난다. [ T ] 
   4. SQLite에서 dot(.) 으로 시작하는 명령어는 SQL이 아니다. [  F  ] 
   5. 한 개의 DB 에는 한개의 테이블만 존재한다. [  F  ]

   

3. 다음 코드의 실행결과로 나타나는 값을 작성하세요. 

   ```bash
   sqlite> .nullvalue ‘NULL’ sqlite> CREATE TABLE ssafy ( 
   …> id INTEGER PRIMARY KEY, 
   …> location TEXT, 
   …> class INTEGER 
   …> ); 
   sqlite> INSERT INTO ssafy (id, location)
   …> VALUES (1, ‘JEJU’); 
   sqlite> SELECT class FROM ssafy WHERE id=1;
   ```

   