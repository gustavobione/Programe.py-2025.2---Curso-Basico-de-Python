a = int(input())
b = int(input())
quociente = 0
while a >= b:
    a -= b
    quociente += 1

print(f"{quociente}")