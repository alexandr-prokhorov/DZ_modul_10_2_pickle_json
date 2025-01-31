import pickle
import json


class Book:
    def __init__(self, title=None, author=None, release_date=None):
        """
        Функция инициализирует объект книги.
        :param title: Название книги.
        :param author: Автор книги
        :param release_date: Дата выхода книги.
        """
        self.title = title
        self.author = author
        self.release_date = release_date

    def display_book(self):
        """
        Функция возвращает информацию о книге.
        """
        print(f'Книга: "{self.title}", Автор: {self.author}, Дата выпуска: {self.release_date}')

    def edit_information_book(self, title=None, author=None, release_date=None):
        """
        Функция корректирует данные о Книге.
        :param title: Название книги.
        :param author: Автор книги
        :param release_date: Дата выхода книги.
        """
        if title is not None:
            self.title = title
        if author is not None:
            self.author = author
        if release_date is not None:
            self.release_date = release_date
        print(f'Измененные данные: Название: {self.title}, автор: {self.author}, дата выхода: {self.release_date}')


class Encoder(json.JSONEncoder):
    """
    Класс для кодирования(сериализации) объектов Python в JSON-строку.
    """

    def default(self, obj):
        """
        Функция создает кастомный Encoder
        :param obj: Объект для сериализации.
        :return: Возвращает кастомный словарь который сериализован в формат Json.
        """
        if isinstance(obj, Book):
            return {'title': obj.title, 'author': obj.author, 'release_date': obj.release_date}
        return super().default(obj)


class Json:
    """
    Класс для сохранения и загрузки формата Json.
    """

    def save_data(self, data, filename):
        """
         Функция сохраняет информацию в файл при помощи Json.
        :param data: Информация о книге.
        :param filename: Название файла в который сохраняется информация.
        """
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(data, file, cls=Encoder, ensure_ascii=False, indent=4)
        print(f'Данные успешно сохранены в файл {filename}')

    def load_data(self, filename):
        """
        Функция загружает информацию из файла Json.
        :param filename: Имя файла.
        :return: Возвращает информацию из файла Json.
        """
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                data = json.load(file)
                print(f'Данные успешно загружены из {filename} при помощи JSON')
                return Book(**data)
        except FileNotFoundError:
            print(f'Файл {filename} для загрузки не найден')


class Pickle:
    def save_data(self, data, filename):
        """
        Сохраняет объект Book в файл формата Pickle.
        :param data: Экземпляр Book для сохранения.
        :param filename: Имя файла для сохранения данных.
        """
        if isinstance(data, Book):
            with open(filename, 'wb') as file:
                pickle.dump(data, file)
                print(f'Данные успешно сохранены в файл {filename} при помощи pickle.')
        else:
            print('Ошибка: Переданный объект не является экземпляром Book.')

    def load_data(self, filename):
        """
        Загружает объект Book из файла формата Pickle.
        :param filename: Имя файла для загрузки данных.
        :return: Экземпляр Book или None в случае ошибки.
        """
        try:
            with open(filename, 'rb') as file:
                data = pickle.load(file)
                if isinstance(data, Book):
                    print(f'Данные успешно загружены из файла {filename} при помощи pickle.')
                    return data
                else:
                    print('Ошибка: Загруженные данные не являются экземпляром Book.')
                    return None
        except FileNotFoundError:
            print(f'Файл {filename} для загрузки не найден.')
            return None
