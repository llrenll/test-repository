n = int(input('数字を入力'))
s = []

while n != 0:
    s.append(n % 2)
    n = n//2
    
s.reverse()

for i in s:
    print(i,end="")