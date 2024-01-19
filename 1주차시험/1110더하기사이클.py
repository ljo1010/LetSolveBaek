seq = 0
n = int(input())
a = n

if n < 10: # 조건 1
    n = n*10
elif n == 1:
    print(60)# 해결못함
while True:
    n = (n%10)*10+(n//10 + n%10)%10 #한자리수만 가져오고 10을 곱해 십의자리로 만든뒤 일의 자리를 더한다고 생각했음
    seq += 1
    if a == n:
        break
print(seq)