#조건에 따른 실행문장 선택하기 : 조건문
# 미세먼지 농도(dust)의 값이 50초과이면 '50초과', 50 이하이면 '50이하'를 출력하기

dust = 55
if dust > 50 :
    print('50초과')
else :
    print('50이하')



dust = int(input("오늘의 미세먼지 농도를 입력하세요. : "))

if dust >  80 :
    print('미세먼지 농도 나쁨')
elif 30 < dust <= 80 :
    print('미세먼지 농도 보통')
else :
    print('미세먼지 농도 좋음')