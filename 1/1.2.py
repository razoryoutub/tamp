if __name__ == '__main__':
	r = 99  # предварительное "объявление" переменной
	while r != 5:  # цикл while
		print("""
1 - для удаления записи
2 - для ввода новой записи
3 - для вывода записи(ей)
4 - для поиска записи(ей)
5 - для выхода
			""")  # вывод меню
		r = int(input('Выберите пункт меню:'))  # ввод выбора пользователем
	exit()  # завершение работы программы