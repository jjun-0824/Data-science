# 셀레니움 연습하기
from selenium import webdriver
import time
# 데이터 확인 순서
# 1. 웹드라이버 켜기 ("./" 현재 폴더에 있는 "chromedriver" 요걸 열어줘)
driver=webdriver.Chrome("./chromedriver")
# 2. 네이버 지도 접속하기
driver.get("https://v4.map.naver.com/")

# 3. 검색창에 검색어 입력하기 // 검색창: input#search-input
search_box=driver.find_element_by_css_selector("input#search-input")
search_box.send_keys("치킨")
# 4. 검색버튼 누르기 // button.spm
search_button=driver.find_element_by_css_selector("button.spm")
# 지연시간 주기
search_button.send_keys("\n")


for n in range(1,6):
    time.sleep(1)
    # 5. 검색결과 확인하기
    # 컨테이너 dl.lsnx_det
    # stores=html.select("dl.lsnx_det")
    stores=driver.find_elements_by_css_selector("dl.lsnx_det")

    for s in stores:
        name=s.find_element_by_css_selector("dt > a").text
        addr = s.find_element_by_css_selector("dd.addr").text
        tel = s.find_element_by_css_selector("dd.tel").text
    # 가게 이름 dt > a
    # 가게 주소 dd.addr
    # 전화번호 dd.tel
        print(name)
        print(addr)
        print(tel)

    # 페이지 버튼 div.paginate > * -> 해당 태그를 갖고 있는 것들이 리스트로 저장됨.
    page_bar=driver.find_elements_by_css_selector("div.paginate > *")

    page_bar[n+1].click()
