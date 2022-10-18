# (A+B)%C는 ((A%C) + (B%C))%C 와 같을까?
# (A×B)%C는 ((A%C) × (B%C))%C 와 같을까?
A, B, C = map(int, input().split())
print( (A+B)%C ) 
print( ( (A%C) + (B%C) ) %C )
print( (A*B) %C)
print( ( (A%C) * (B%C) ) %C )

# 결론 : 나머지 연산은 결합법칙이 성립한다