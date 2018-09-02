# Python Outlook Attachments Parser
이 도구는 주기적으로 Outlook에 전달되는 급식 메일(엑셀 첨부파일)을 파싱하여, 원하는 메뉴 정보를 추출하는 도구이다.
본 도구는 https://github.com/awangga/outlook Gitbub 코드를 활용하였고, 필요한 함수들은 추가/수정하여 사용하였다.
이 도구는 회사의 아침/점심/저녁 식단정보를 구성원들에게 편하게 제공해주기 위해 만들어졌다.
# 본 도구는 아래 구조로 운영방식 
attachSpider.py : 엑셀파일의 주기적 다운로드 담당<br>
botModule.py : 봇 요청역할<br>
menuRecognizer.py : 엑셀파일 이름에 따른 파싱 담당<br>
해당 도구는 카카오톡 챗봇에 연동하여 서비스 중이다.
