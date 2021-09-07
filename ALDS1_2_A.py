def bubbleSort(array):
  sw = 0
  flag = True
  i = 0
  while (flag):
    flag = False
    for j in range(len(array) - 1, i, -1): # for (int j = array.length - 1; j > i; j--) {...}
      if (array[j] < array[j - 1]):
        array[j - 1], array[j] = array[j], array[j - 1] # 配列の置換
        flag = True
        sw += 1
    i += 1
  return sw

n = int(input("nを入力"))
r = []
for i in range(0, n):
  r.append(int(input(str(i + 1) + "番目の整数を入力")))

sw = bubbleSort(r)

print(r)
print(sw)