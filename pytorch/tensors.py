import torch


# из списка []
a = torch.tensor([1, 2, 3, 4, 5])
print(f'Из списка: {a}')

# из range
b = torch.arange(0, 10, 2)
print(f'arange: {b}')

# только нули
zeros = torch.zeros(3, 4)  # 3 строки, 4 столбца
print(f'Нули 3x4:\n{zeros}')

# только единицы
ones = torch.ones(2, 5)
print(f'Единицы 2x5:\n{ones}')

# случайные числа
random_tensor = torch.rand(3, 3)  # от 0.0 до 1.0
print(f'Случайные 3x3:\n{random_tensor}')



print('\n--- Свойства тензора ---')
x = torch.rand(2, 3, 4)  # 2 блока по 3 строки и 4 столбца
print(x)
print(f'Форма (shape): {x.shape}')
print(f'Размерность (ndim): {x.ndim}')
print(f'Тип данных (dtype): {x.dtype}')
print(f'Устройство (device): {x.device}')  # cpu



print('\n--- Операции ---')
a = torch.tensor([1.0, 2.0, 3.0])
b = torch.tensor([4.0, 5.0, 6.0])

print(f'a + b = {a + b}')
print(f'a * b = {a * b}')  # поэлементное умножение
print(f'a @ b = {a @ b}')  # скалярное произведение (1*4 + 2*5 + 3*6 = 32)
print(f'Среднее a: {a.mean():.2f}')
print(f'Сумма a: {a.sum():.2f}')



print('\n--- Изменение формы ---')
x = torch.arange(1, 13)
print(f'Исходный: {x}')

x_reshaped = x.reshape(3, 4)  # 3 строки, 4 столбца
print(f'reshape(3,4):\n{x_reshaped}')

x_view = x.view(4, 3)  # альтернатива reshape (чуть быстрее, но с ограничениями)
print(f'view(4,3):\n{x_view}')



print('\n--- Индексация ---')
matrix = torch.tensor([[1, 2, 3],
                       [4, 5, 6],
                       [7, 8, 9]])
print(f'Матрица:\n{matrix}')
print(f'matrix[0, 0]: {matrix[0, 0]}')  # первый элемент
print(f'matrix[1, :]: {matrix[1, :]}')  # вся вторая строка
print(f'matrix[:, 2]: {matrix[:, 2]}')  # весь третий столбец
print(f'matrix[1:, 1:]:\n{matrix[1:, 1:]}')  # подматрица с индекса [1, 1]



print('\n--- GPU ---')
if torch.cuda.is_available():
    cpu_tensor = torch.rand(3, 3)
    gpu_tensor = cpu_tensor.to('cuda')  # или cpu_tensor.cuda()

    print(f'На CPU: {cpu_tensor.device}')
    print(f'На GPU: {gpu_tensor.device}')

    back_to_cpu = gpu_tensor.to('cpu')
    print(f'Возвращение на: {back_to_cpu.device}')
else:
    print('GPU не доступен')
