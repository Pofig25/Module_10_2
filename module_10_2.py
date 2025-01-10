import threading                                                # Импортируем модуль threading для работы с потоками
import time                                                     # Импортируем модуль time для задержки выполнения

class Knight(threading.Thread):                                 # Создаем класс Knight, наследующий от Thread
    def __init__(self, name, power):                            # Конструктор класса
        super().__init__()                                      # Вызов конструктора родительского класса
        self.name = name                                        # Инициализация имени рыцаря
        self.power = power                                      # Инициализация силы рыцаря
        self.enemies = 100                                      # Инициализация количества врагов
        self.days = 0                                           # Инициализация счетчика дней сражения

    def run(self):                                              # Переопределяем метод run
        print(f"{self.name}, на нас напали!")                   # Выводим сообщение о нападении
        while self.enemies > 0:                                 # Пока враги не повержены
            self.days += 1                                      # Увеличиваем счетчик дней
            self.enemies -= self.power                          # Уменьшаем количество врагов на силу рыцаря
                                                                # Выводим сообщение о сражении
            print(f"{self.name}, сражается {self.days} день(дня)..., осталось {max(self.enemies, 0)} воинов.")
            time.sleep(1)                                       # Задержка на 1 секунду (1 день сражения)
                                                                # Сообщаем о победе после окончания битвы
        print(f"{self.name} одержал победу спустя {self.days} дней(дня)!")

first_knight = Knight('Sir Lancelot', 10)                       # Первый рыцарь с силой 10
second_knight = Knight("Sir Galahad", 20)                       # Второй рыцарь с силой 20

                                                                # Запуск потоков и остановка текущего
first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()

print("Все битвы закончились!")                                 # Вывод строки об окончании сражения
