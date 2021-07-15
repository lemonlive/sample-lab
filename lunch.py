#이것은 주석이다
#shift키 활용을 잘 하자.
#단축기 활용을 잘하자
#shift + up or down
#Ctrl + / (IDE마다 다르다.)

menu = ['한식','일식','중식','양식']

import random

lunch = random.choice(menu)
print(lunch)

number = {'한식' : '123-4567', '일식' : '333-4455', '중식' : '235-5566', '양식' : '298-5151'}

print(number[lunch])


print('오늘의 점심은 ',lunch,'입니다. 전화번호는 ',number[lunch],' 입니다.')

#f는 출력을 예쁘게 해주겠다는 뜻.
print(f'오늘의 점심은 {lunch}입니다. 전화번호는 {number[lunch]}입니다.')