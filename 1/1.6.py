c = 0  # глобальная переменная-счетчик
all_records = []  # глобальная переменная-список со всеми записями


def add_user():
	global c, all_records  # объявление глобальных переменных
	c += 1  # увеличение счетчика на 1
	print('Запись номер: ' + str(c))  # вывод номера записи
	z = {}  # создание локальной переменной-словаря для записи данных
	z['fname'] = str(input('Введите Имя: '))  # ввод имени
	z['sname'] = str(input('Введите Фамилию: '))
	z['patronymic'] = str(input('Введите Отчество: '))
	z['date'] = str(input('Введите Дату рождения: '))
	z['adres'] = str(input('Введите Адрес: '))
	z['gender'] = str(input('Введите Пол: '))
	all_records.append(z)  # добавление к глобальному списку локальный элемент


def del_user():
	global c, all_records  # объявление глобальных переменных
	print("""
1 - для удаления одной записи
2 - для удаления всех записей
			""")  # вывод выбора
	i = int(input('Выберите пункт меню: '))  # ввод пользователя
	match i:
		case 1:
			print(f'Всего записей: {c}')
			j = int(input('Введите номер записи для удаления: '))
			del all_records[j - 1]  # удаление j-1 элемента
			c -= 1  # уменьшение счетчика на 1
		case 2:
			all_records = []  # полная очиска списка
			c = 0  # обнуление счетчика


def print_user():
	global c, all_records  # объявление глобальных переменных
	print("""
1 - для вывода одной записи
2 - для вывода всех записей
			""")  # вывод выбора
	i = int(input('Выберите пункт меню: '))  # ввод пользователя
	match i:
		case 1:
			i = int(input('Выберите номер записи: '))
			user = all_records[i]
			print('Имя: {0}'.format(user['fname']))
			print("""
фамилия: {0}
Отчество: {1}
Дата рождения: {2}
Адрес: {3}
Пол: {4}
""".format(user['sname'], user['patronymic'], user['date'], user['adres'], user['gender']))
		case 2:
			c_l = 0
			for user in all_records:
				c_l += 1
				print('Запись номер: {0}'.format(c_l))
				print('Имя: {0}'.format(user['fname']))
				print("""
фамилия: {0}
Отчество: {1}
Дата рождения: {2}
Адрес: {3}
Пол: {4}
""".format(user['sname'], user['patronymic'], user['date'], user['adres'], user['gender']))


def search_user():
	print(4)


if __name__ == '__main__':
	r = 99  # предварительное "объявление" переменной
	while r != 5:  # цикл while
		print("""
1 - для ввода новой записи
2 - для удаления записи
3 - для вывода записи(ей)
4 - для поиска записи(ей)
5 - для выхода
			""")  # вывод меню
		r = int(input('Выберите пункт меню: '))  # ввод выбора пользователем
		match r:  # конструкция case для выбора нужной функции
			case 1:
				add_user()
			case 2:
				del_user()
			case 3:
				print_user()
			case 4:
				search_user()
	exit()  # завершение работы программы
