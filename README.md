# missing-backend
- 실종자 신고 서비를 위한 서버 사이드(Back End) with Django
- 실행 및 자세한 설명에 관하여 메인 페이지 [이곳](https://github.com/oss-talkative)을 참고해주세요

<br>

## 🔗URL
|url|
|:--:|
|missingChild.pythonanywhere.com/|

## 🔗API
|uri|request|contents
|:--:|:--:|:--:|
|/allFoundChild|GET|발견 신고된 모든 정보 반환|
|/addMissingChild|POST|field 요청으로 실종자 발견 신고|
|/nameFoundChild|POST|'name' field 요청으로 발견 신고된 정보 반환|

<br>

## 📜Fields
|Field name|Type|contents|
|:--:|:--:|:--:|
|name|text|이름|
|gender|text|성별|
|age|text|실종 당시 나이|
|ageNow|text|현재 나이|
|alldressing|text|실종 당시 착장|
|occrAdd|text|실종 장소|
|occrDate|Date|실종 일자|
|writngTarget|text|실종 유형|
|inform|text|실종자 발견 제보 내용|
