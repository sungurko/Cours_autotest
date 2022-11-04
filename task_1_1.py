text = input('Введите произвольную строку: ')


# 4 В строке удалить все буквы а и подсчитать количество удаленных символов

def delet_simvol():
	pass





# 5 Написать произвольную анкету и вывести полученные данные

# 6 Посчитать количество слов в строке

def count_symbol(text: str) -> str:
	result = len(text.split(' '))
	print(f'Количество слов в строке {text} :', result)


# 7 Дана строка, содержащая полное имя файла (например, C:\development\inside\test-project_management\inside\myfile.lxl).
#   Выделите из этой строки имя файла без расширения

def file_name(text: str) -> str:
	result = text.split('\\')[-1].rstrip(")'")
	print(result)

# 8 Проверить что номера телефонов состоят только из цифр. Они могут начинаться с "+", цифры могут быть разделены пробелами и дефисами "-"
#   Например, 8-999-777-1111, +7 999 333 2222, +7 999-555-11-11

def number_phone(text):
	result=[i for i in text if i !=' ' and i !='-']	
	result = ''.join(result).lstrip('+')
	if result.isnumeric():
		print(f'Строка {text} состоит только из цифр !!!')
	else:
		print(f'В строке {text} есть буквы !!!')
	




if __name__ == '__main__':
	print('######## Результаты ########')
	#count_symbol(text)
	#file_name(text)
	#delet_simvol()
	number_phone(text)