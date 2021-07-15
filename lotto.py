import random

#range에서 첫번째는 생략 가능
numbers = range(1, 46)
#range(a, b) : a는 범위에 포함되고, b는 범위에 포함되지 않음
#로또는 1부터 45번까지라서 range는 1, 46
print(type(numbers))
#random.sample(seq,k) : 시퀀스에서 랜덤한 중복되지 않는 길이의 k의 리스트를 반환

lotto = random.sample(numbers,7)

print('로또번호는 ', lotto)


