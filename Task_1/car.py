import pickle
import json


class Car:

    def __init__(self):
        """
        Функция инициализирует пустой словарь, в который будет добавляться информация о машинах.
        """
        self.cars = {}

    def add_cars(self, brand, model, car_class):
        """
        Функция добавляет информацию о машинах в словарь.
        :param brand: Автомобильный бренд.
        :param model: Модель автомобиля
        :param car_class: класс автомобиля.
        """
        self.cars[brand] = {"model": model, "class": car_class}
        print(f'Вы добавили автомобиль марки {brand} ее модель {model} класс автомобиля {car_class}')

    def remove_cars(self, brand):
        """
        Функция удаляет информацию об автомобиле из словаря по бренду.
        :param brand: Бренд автомобиля.
        """
        if brand in self.cars:
            del self.cars[brand]
            print(f'Вы удалили автомобиль марки {brand}')
        else:
            print(f'автомобиль марки {brand} не найден.')

    def display_cars(self):
        """
        Функция возвращает полный список добавленных автомобилей.
        """
        if not self.cars:
            print('Список автомобилей пуст')
        else:
            for brand, details in self.cars.items():
                print(f'{brand}: модель - {details["model"]}, класс - {details["class"]}')


class Pickle:

    def save_data(self, cars, filename):
        """
        Функция сохраняет информацию в формате Pickle.
        :param cars: Словарь с добавленными автомобилями.
        :param filename: Файл в который сохраняется информация.
        :return: Возвращает информацию о сохранении.
        """
        with open(filename, 'wb') as file:
            pickle.dump(cars, file)
            print(f'Данные сохранены в файл {filename} при помощи pickle.')

    def load_data(self, filename):
        """
        Функция загружает информацию из файла формата Pickle.
        :param filename: Файл из которого загружается информация.
        :return: Возвращает информацию из Car.
        """
        try:
            with open(filename, 'rb') as file:
                data = pickle.load(file)
                print(f'Данные успешно загружены {filename} при помощи pickle')
                return data
        except FileNotFoundError:
            print(f'Файл {filename} для загрузки не найден.')


class Json:

    def save_data(self, cars, filename):
        """
        Функция сохраняет информацию в формате Json.
        :param cars: Словарь с добавленными автомобилями.
        :param filename: Файл в который сохраняется информация.
        """
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(cars, file, ensure_ascii=False, indent=4)
            print(f'Данные сохранены в файл {filename} при помощи JSON')

    def load_data(self, filename):
        """
        Функция загружает информацию из файла формата Json.
        :param filename: Файл из которого загружается информация.
        :return: Возвращает информацию из Car
        """
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                data = json.load(file)
                print(f'Данные успешно загружены из {filename} при помощи JSON')
                return data
        except FileNotFoundError:
            print(f'Файл {filename} для загрузки не найден')
