# for문

# for x in iterable객체:
#       ...

for i in range(5):      # 0~4
    print(i, end=" ")

a = range(5)
print(a.start, a.stop, a.step)

# 1~5
for i in range(1,6):
    print(i, end=" ")
print()

# 1~10, 2칸씩
for i in range(1,10,2):
    print(i, end=" ")
print()

# 5,4,3,2,1 거꾸로
for i in range(5,0,-1):
    print(i, end=" ")
print()

# 1~10까지의 합
tot = 0
for i in range(1,11):
    tot+=i
else :
    print(f"sum = {sum}")

print(sum(range(1,11)))

s = "he吳泰縣😒🕐"

for c in s:
    print(c, end =" ")

print(len(s))

for i in range(2,9):
    for j in range(2,9):
        print(f"{i} * {j} = {1*j:<5d}",end="")
else:
    print("End")