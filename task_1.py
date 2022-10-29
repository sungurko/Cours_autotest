while True:
    n = input('Введите число n: ')
    if n.isdigit():
        break
    else:
        print('Необходимо ввести число')

# 1 При заданном целом трехзначном числе n посчитайте n + nn + nnn
def summa_nn(n: str) -> int:
	nn = int(n + n)
	nnn = int(n + n + n)
	result = int(n) + nn + nnn
	print(f'Результатом {n} + {nn} + {nnn} будет число:', result)

# 2 Сложите цифры целого числа
def summa_n(n: str) -> int:
	n = int(n)
	result = 0
	while n > 0:
		last = n % 10
		summ += last
		n = n // 10
	print(f'Сумма цифр целого числа {n} равна: ',result)

# 2 Сложите цифры целого числа (второй вариант)
def summa_n2(n):
	result = sum(map(int, str(n)))
	print(f'Сумма цифр целого числа {n} равна: ',result)

# 3 Найти корень третьей степени числа 343
#round(343 **(1/3))

# В строке удалить все буквы а и подсчитать количество удаленных символов
# Написать произвольную анкету и вывести полученные данные


if __name__ == '__main__':
	print('######## Результаты')
	summa_nn(n)
	#summa_n(n)
	#summa_n2(n)
