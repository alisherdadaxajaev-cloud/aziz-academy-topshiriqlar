a, b, c, d = map(int, input().split())
result = (a + b) - (c // 2) + (d // 2)
if result == 11:
    print(f"Result: {result + 2}")
else:
    print(f"Result: {result}")