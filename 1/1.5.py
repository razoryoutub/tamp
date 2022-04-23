c = 0  # глобальная переменная-счетчик
all_records = []  # глобальная переменная-список со всеми записями


def add_user():
	global c, all_records  # объявление глобальных переменных
	print('Запись номер: ' + str(c))  # вывод номера записи
	z = {}  # создание локальной переменной-словаря для записи данных
	z['fname'] = str(input('Введите Имя: '))  # ввод имени
	z['sname'] = str(input('Введите Фамилию: '))
	z['patronymic'] = str(input('Введите Отчество: '))
	z['date'] = str(input('Введите Дату рождения: '))
	z['adres'] = str(input('Введите Адрес: '))
	z['gender'] = str(input('Введите Пол: '))
	all_records += z  # добавление к глобальному списку локальный элемент
	c += 1  # увеличение счетчика на 1


def del_user():
	print(2)


def print_user():
	print(3)


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
		r = int(input('Выберите пункт меню:'))  # ввод выбора пользователем
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
