# 1 При заданном целом трехзначном числе n посчитайте n + nn + nnn
n = input('Введите число n: ')

def summa_nn(n):
	nn = int(n + n)
	nnn = int(n + n + n)
	res = int(n) + nn + nnn
	print('результатом n + nn + nnn будет число:', res)

# 2 Сложите цифры целого числа

def summa_n(n):
	summ = 0
	while n > 0:

result = sum(map(int, str(n)))
#print(result)
#summ = 0

#summ = 0
#while n > 0:
#	c = n % 10
#	summ += c
#	n = n // 10
#print('Сумма трехзначного числа будет:', summ)

# Найти корень третьей степени числа 343
#round(343 **(1/3))

# В строке удалить все буквы а и подсчитать количество удаленных символов
# Написать произвольную анкету и вывести полученные данные



if __name__ == '__main__':
	print('######## Результаты')
	summa_nn(n)
	summa_n()
