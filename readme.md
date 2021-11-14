# 🎥  PROJECT_WETCHAPEDIA | 윗차피디아

윗차피디아 UI/UX 메인 서비스

1. 각 영화에 대한 정보를 접근할 때, Entry Point를 Feed 형식으로 제공합니다.
2. 사용자의 편의성을 위해, Info-Extension에 대해 Carousel-Slider 기능을 제공합니다.
3. 영화 평점을 매길 때, 별점 UI를 제공함으로써 가시성(Visibility)을 증대시킵니다.

윗차피디아 API 메인 서비스 

1. WETCHAPEDIA에 게시된 평점 평균별 영화 리스트 및 상세정보를 제공합니다.
2. WETCHAPEDIA 회원이 시청한 영화의 평점, 댓글, 찜목록 등록을 제공합니다.
3. WETCHAPEDIA에 등록된 영화를 검색하여 총 별점 점수, 장르, 국가 등의 리스트를 한눈에 볼 수 있습니다.   

- 사이트 링크 : https://pedia.watcha.com/ko-KR

# 🚀 TEAM_WECHACHA | 윗챠챠 


- 영상 : https://youtu.be/vX-U9jLrjuE

## 👫 팀원 
- Front-end: 최병현(PM), 안재우, 전창민, 정지후
- Back-end: 박대현, 박민정, 장재원

## 개발 기간

- 기간: 2021년 11월 01일 ~ 2021년 11월 12일(12일간)

## 적용 기술

- Front-end: React(Class-Component)_reactr-router-dom, SCSS)_MIXIN/Nesting/VARIABLE, JavaScript(ES6)
- Back-end: Django, Python, MySQL, jwt, bcrypt, AWS(EC2, RDS)
- 협업툴: Trello, Slack, Notion, Github, dbdiagram, postman


## 구현 기능 및 개인 역할

> **박대현**
- 영화 상세페이지 정보 제공 API 
- 평점 등록, 조회, 수정, 삭제 기능 API

> **박민정**
- SignUpView: 회원가입 기능 구현, bcrypt를 활용한 패스워드 암호화
- SignInView, login_decorater: 로그인 기능, JWT 토큰 발행을 통한 인증・인가 기능 구현
- CommentView: Comment CRUD API 로직 구현


> **장재원**
- 카테고리별 평점순 영화리스트 제공 API, 평점순 영화리스트 제공 API
- 보고싶어요 등록, 조회, 삭제 기능 API

## EndPoint : [API 명세서 링크](https://documenter.getpostman.com/view/18262150/UVC5ESgu)   

[post] SignUpView : /users/signup

[post] Login : /users/signin

[post], [get] WishListView : /users/wishlist

[get]  MovieDetailView : /movies/<<int:pk>>

[get] MovieListView : /movies?source=<<str:sources>>

[post], [get], [put], [delete] RateListView : /movies/rate/<<int:movie_id>>

[post], [get], [put], [delete] CommentView : movies/<<int:movie_id>>/comments


## Modeling
![title](https://media.vlpt.us/images/jewon119/post/bb7a9245-e9fb-420e-95a2-dcf218d1f786/wechapedia_update.png)   

## Clinet-Server Diagram
![title](https://media.vlpt.us/images/jewon119/post/f27b811e-a9a8-4e97-a4b8-1a87f7764d47/Client-Server-Model-diagram.jpg)   


## 소감 및 후기
> **박대현** : 처음으로 한 프로젝트! 시작할 땐 기대반 걱정반이였지만, 과정과 결과물 두가지를 동시에 잡은 프로젝트였다.
이번 프로젝트를 통해 프로젝트를 시작하기 전에 비해 여러 부분에서 성장할 수 있었고, 초심을 잃지 않고 꾸준히 성장하는 개발자를 목표로 정진해야겠다.[(대현님 Project 회고)](https://enormous-authority-d65.notion.site/1-a585200a6d814ddda8d30cb1c7d37761)   


> **박민정** : 짧은 기간 내에 이루어진 팀 프로젝트, 처음이어서 잘 할 수 있을까 걱정도 됐지만 스스로 검색해가며 주체적으로 코드를 짜볼 수 있어서 좋았고 막히는 부분이 있으면 같이 머리를 맞대고 고민해주는 과정이 정말 뜻 깊었습니다. 비록 많은 기능을 구현해 보지는 못했지만 좋은 팀원분들을 만나 원활하게 소통하고 서로 응원하며 결과물을 만들어내는 과정을 보고 많은 것을 배울 수 있었습니다. 한 층 더 성장할 수 있는 발판이 되지 않았나 싶습니다. 같은 팀으로 프로젝트를 진행하게 돼서 정말 행복했습니다.[(민정님 Project 회고)](https://velog.io/@doniminp/PROJECT-WETCHAPEDIA-%ED%9B%84%EA%B8%B0)

> **장재원** : 개발자로서 진행된 첫 팀 프로젝트. 그 시작을 Wetchacha 팀을 만나 무척 즐겁고 의미가 깊었습니다. 2주가 짧고도 길었지만 귀중한 시간 속 얻었던 경험들을 깊게 세기겠습니다. 특히, 성장할 수 있도록 도와주신 멘토님들께 정말 감사드립니다.[(재원님 Project 회고)](https://velog.io/@jewon119/TIL83.-WetchaPedia-Project-1%EC%B0%A8-%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8-%ED%9A%8C%EA%B3%A0)   


## 레퍼런스
- 이 프로젝트는 <u>[왓챠피디아](https://pedia.watcha.com/ko-KR)</u> 사이트를 참조하여 학습목적으로 만들었습니다.
- 실무수준의 프로젝트이지만 학습용으로 만들었기 때문에 이 코드를 활용하여 이득을 취하거나 무단 배포할 경우 법적으로 문제될 수 있습니다.