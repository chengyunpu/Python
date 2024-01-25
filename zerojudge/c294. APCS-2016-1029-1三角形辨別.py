s = list(map(int, input().split()))
for j in range(3):
    for k in range(3):
        if s[j] < s[k]:
            s[j], s[k] = s[k], s[j]

for j in range(3):
    print(s[j], end=' ')
print()
if (s[0]+s[1]>s[2]):
    if s[2] ** 2 == s[0] ** 2 + s[1] ** 2:
        print("Right")
    elif s[2] ** 2 >( s[0] ** 2 + s[1] ** 2):
        print("Obtuse")
    elif s[2] ** 2 < (s[0] ** 2 + s[1] ** 2):
        print("Acute")
else:
    print("No")
