n = int(input())
i = 2

while i <= n:
        if n % i == 0:
            break
        i += 1

if i == n:
      print("Sim, esse número é primo!") 
else:
    print("O número não é primo!")