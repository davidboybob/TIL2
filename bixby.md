## 5강 Bixby Capsule 디자인



### 5. 1Bixby Capsule 디자인

#### 5.1.1 Bixby Capsule 개요

Capsule 이란?

Bixby를 통해 사용자에게 제공하는 서비스 단위

#### 5.1. 2Capsule의 구성요소

- Modeling (Concept, Action)
- Business Logic (Javascript)
- UI (Dialog, Layout, Follow-Up)
- Natural Language(Vocabulary, Training data)





#### 5.1.3 Bixby Views

UI를 구성하는 기본 요소

Bixby Views는 Bixby Language를 사용하여 구현합니다.

Layout과 Dialog, Follow-Up를 사용하여 간편하게 사용자와 대화 할 수 있는 디자인을 구성하실 수 있습니다.

- Input View 
- Result View 
- Confirmation View

![bixby view 구조](https://user-images.githubusercontent.com/52685322/65733382-737c6c00-e109-11e9-8aef-30486d140956.jpg)

- Dialog : 사용자와 대화하는 창구
  - Dialog는 사용자와 대화하는 다양한 벙법들 중에 하나입니다. 설계에 따라서 현재 어떤 상황이 벌어졌는지 알려주거나, 사용자 발화의 결과를 알려줄 수도, 부가적인 정보를 요청할 수도 있습니다.
- Layout : 사용자에게 다양한 경험 제공
  - Bixby Views의 종류에 따라 다양한 Layout을 사용하실 수 있습니다. 미리 설계된 Layout Component를 활용해 직관적이고 다양한 사용자 경험을 제공할 수 있습니다.
- Follow-up : Bixby와 지속적인 대화
  - Follow-Up을 통해 Bixby와 지속적으로 대화를 이어나갈 수 있습니다. 결과 화면에서 다음 대화를 이어나갈 수 있는 힌트를 제공할 수도 있고, 후속 질문의 응답을 디반으로 다른 기능을 유도할 수 있습니다.

### 5.2.1 Bixby Capsule 디자인 실습