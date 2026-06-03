q = int(input())
counter = 0 

for _ in range(q):
    cmd = input().strip()
    
    if cmd == "inc":
        counter += 1
        print(counter)
    elif cmd == "reset":
        counter = 0
        print(counter)