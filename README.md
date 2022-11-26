# missing-backend

## 🔗URL
|base url|
|:--:|
|missingChild.pythonanywhere.com/|

## 🔗API
|url|request|contents
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