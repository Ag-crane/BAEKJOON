# 입력 : 첫째 줄에 (1)의 위치에 들어갈 세 자리 자연수가, 둘째 줄에 (2)의 위치에 들어갈 세자리 자연수가 주어진다.

a = int(input())
b = int(input())
for i in range(3):
    print(b//10**i%10*a)
print(a*b)
