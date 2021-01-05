import requests
from bs4 import BeautifulSoup
raw= requests.get("https://tv.naver.com/r/")
# 데이터를 잘 갖고 왔는지 확인
# print(raw)
# 데이터의 text(소스코드)를 확인
# print(raw.text)
# 데이터를 갖고 오는 소요시간
# print(raw.elapsed)
html=BeautifulSoup(raw.text,"html.parser")
print(html)


# 1-3위 컨테이너: div.inner
# 제목: dt.title
# 채널명: dd.chn
# 재생수: span.hit
# 좋아요 수: span.like

#1. 컨테이너 수집
container=html.select("div.inner")
print(container)
# 여러개의 정보들 중에 첫번쨰 컨테이너의 정보듦만 수집하고 싶다면
print(container[0])

#2. 영상데이터 수집
title=container[0].select_one("dt.title").text()
print(title)
# 태그 데이터를 제외하고 수집하는 법
print(title.text)
# 또 다른 방식
# title=container[0].select("dt.title")
# print(title[0].text)
chn=container[0].select_one("dd.chn")
hit=container[0].select_one("span.hit")
like=container[0].select_one("span.like")

print(title.text.strip())
print(chn.text.strip())
print(hit.text.strip())
print(like.text.strip())

#3. 반복하기
for i in range(3):
    title = container[i].select_one("dt.title")
    chn = container[i].select_one("dd.chn")
    hit = container[i].select_one("span.hit")
    like = container[i].select_one("span.like")

    print(title.text.strip())
    print(chn.text.strip())
    print(hit.text.strip())
    print(like.text.strip())
for cont in container:
    title = cont.select_one("dt.title")
    chn = cont.select_one("dd.chn")
    hit = cont.select_one("span.hit")
    like = cont.select_one("span.like")

    print(title.text.strip())
    print(chn.text.strip())
    print(hit.text.strip())
    print(like.text.strip())
    print("="*50)
