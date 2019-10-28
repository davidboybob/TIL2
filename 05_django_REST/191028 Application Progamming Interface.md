Application Progamming Interface

정해진 형식으로 요청을 보내면 요청한 정보를 받을 수 있는 소통 방법



Interface : 소통 수단 (접점)

1. 사람과 기계와의 접점 -> 디바이스 
2. 기계와 기계 -> 서버, 클라이언트 

Re S T

각 요청이 어떠한 동작 & 정보를 위한 것인지 요청 형식 자체(주소)로 파악이 가능한 것

Djangorestframework 

백엔드로서의 django !



Fixture

- 데이터베이스의 직렬화(serialized) 된 내용을 포함하는 파일 모음이다.
- 각 fixture 은 고유한 이름을 가지며, 이를 구성하는 파일은 여러 응용 프로그램에서 여러 디렉토리에 배포될 수 있다.
- django는 `loaddata` 시 설치된 모든 app 에서 `fixtures` 라고 하는 이름의 폴더를 찾는다.
- static templates 

```
musics/
  fixtures/
    musics/
      dummy.json
```





