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
def summa_n2(n: str) -> int:
	result = sum(map(int, str(n)))
	print(f'Сумма цифр целого числа {n} равна: ',result)

# 3 Найти корень третьей степени числа 343
def koren(n):
	n = int(n)
	result = round(n **(1./3.))
	print(f'Корень третьей степение для числа {n} будет равен', result)






if __name__ == '__main__':
	print('######## Результаты ########')
	#summa_nn(n)
	#summa_n(n)
	#summa_n2(n)
	#koren(n)