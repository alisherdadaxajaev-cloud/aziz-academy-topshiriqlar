a = float(input())
b = float(input())
c = float(input())
summa = a + b + c
o_rtacha = summa / 3 
print(f"Sum: {int(summa) if summa.is_integer() else summa}")
print(f"Avg: {o_rtacha:.2f}")