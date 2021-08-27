n = int(input("nを入力"))
r = []
for i in range(0, n):
  r.append(int(input(str(i + 1) + "番目の整数を入力")))

maxv = -2000000000
minv = r[0]
for j in range(1, n - 1):
  maxv = max(maxv, r[j] - minv)
  minv = min(minv, r[j])

print(maxv)