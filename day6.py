print("Есепті таңдаңыз:")
print("1 - Watermelon")
print("2 - Team")
print("3 - Next Round")
print("4 - Bit++")
print("5 - Domino piling")

choice = int(input())

# 1. Watermelon
if choice == 1:
    w = int(input())
    if w > 2 and w % 2 == 0:
        print("YES")
    else:
        print("NO")

# 2. Team
elif choice == 2:
    n = int(input())
    count = 0
    for _ in range(n):
        a, b, c = map(int, input().split())
        if a + b + c >= 2:
            count += 1
    print(count)

# 3. Next Round
elif choice == 3:
    n, k = map(int, input().split())
    scores = list(map(int, input().split()))
    threshold = scores[k - 1]
    count = 0
    for s in scores:
        if s >= threshold and s > 0:
            count += 1
    print(count)

# 4. Bit++
elif choice == 4:
    n = int(input())
    x = 0
    for _ in range(n):
        op = input()
        if '+' in op:
            x += 1
        else:
            x -= 1
    print(x)

# 5. Domino piling
elif choice == 5:
    n, m = map(int, input().split())
    print((n * m) // 2)

else:
    print("Қате таңдау!")