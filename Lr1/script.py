#воспользуемся алгоритмом пирамидальной сортировки. Данная сортировка имеет сложность =n*log(n) в худшем случае
def heapify(arr, n, i):
    smallest = i #пусть наименьший элемент (родитель) имеет номер i
    left = 2 * i + 1 #определим левого "ребенка"
    right = 2 * i + 2 #определим правого "ребенка"
    if left < n and arr[left] < arr[smallest]:
        smallest = left #сравнение ребенка и родителя для выявления меньшего элемента
    if right < n and arr[right] < arr[smallest]:
        smallest = right #сравнение ребенка и родителя для выявления меньшего элемента
    if smallest != i: #проверка на то, требуется ли замена мест
        temp = arr[i]
        arr[i] = arr[smallest]
        arr[smallest] = temp
        heapify(arr, n, smallest)
def heap_sort_desc(arr):
    n = len(arr)
    # строим min-heap (пирамиду от меньшего к большему)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    # извлекаем элементы в список
    for i in range(n - 1, 0, -1):
        temp = arr[0]
        arr[0] = arr[i]
        arr[i] = temp
        heapify(arr, i, 0)
    return arr

#по условию задачи запишем 19 чисел в список, который будем сортировать
numbers = []
for i in range(1,19+1):
    numbers.append(i)
heap_sort_desc(numbers)
print(numbers)