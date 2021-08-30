def insertionSort(array):
  for i in range(1, len(array)):
      v = array[i]
      j = i - 1
      while (j >= 0 and array[j] > v):
        array[j + 1] = array[j]
        j -= 1
      array[j + 1] = v
      print(*array)

n = int(input("nを入力"))
array = []
for i in range(0, n):
  array.append(int(input(str(i + 1) + "番目の整数を入力")))

print(*array)
insertionSort(array)