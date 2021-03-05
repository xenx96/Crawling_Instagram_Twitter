# Crawling_Instagram_Twitter
트위터 및 인스타그램 크롤링

- 목적
```
해당 tweet 및 instagram Crawling ipynb Files는 
'2020-01 학기 학사학위 논문' 및 문화체육관광부 주관 '문화관광 빅데이터 분석 공모전'을 위해 제작되었습니다.

학위논문 
- 학위 논문 저자 : 한남대 비즈니스통계학과 유대선
- 학사 학위논문 내용 : 2020 대전시 총선 예측
- 필요 데이터 : Naver News Comments, Instagram Comments, Twitts' Comments, 지난 총선정보

문화관광 빅데이터 분석 공모전
- 팀 : 165번
- 직책 : 팀장
- 수상 : 우수상
- 인원 : 4명
- 데이터 : 신한카드 데이터 및 언택트(코로나) 관련 Naver,Twitts, Instagram Comments
```

- 수정 사항
```
1. .ipynb -> .py 로 변경 (예정)
2. Class 객체화 (예정)
3. 코드 한줄로 Crawling 갯수 지정, 날짜 지정, 검색어 지정 가능한 Code화 (예정)
```

- InstagramCrawling.py
```
- 사용 방법
Search = '한남대' #검색어
IC = InstagramCrawling()
IC.setSearch(Search)
IC.instCrawling()

```
