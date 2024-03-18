n, q, m = map(int, input().split())
a = list(map(int, input().split()))
queries = []
for i in range(q):
    queries.append(list(map(int, input().split())))
b = list(map(int, input().split()))

queries = queries[::-1]
dic = {}
for i in b:
    if i in dic:
        print(dic[i])
        continue
    new_ans = i
    for t, l, r in queries:
        if l > new_ans or r < new_ans:
            continue
        if t == 1:
            new_ans = new_ans-1 if new_ans > l else r
        else:
            new_ans = r - new_ans + l
    dic[i] = a[new_ans-1]
    print(dic[i])
