n = int(input())
vertex = []
for _ in range(n):
    vertex.append(list(map(int, input().split())))

ans = 10**9

for i in range(n):
    l, m, r = vertex[i-2], vertex[i-1], vertex[i]
    dis1 = ((r[0]-m[0])**2+(r[1]-m[1])**2)**0.5
    a, b = r[1] - l[1], l[0] - r[0]
    c = -a * l[0] - b * l[1]
    dis2 = abs(a * m[0] + b * m[1] + c)/(a**2 + b**2)**0.5
    ans = min(ans, dis1/2, dis2/2)
print(ans)
