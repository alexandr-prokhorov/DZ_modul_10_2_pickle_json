import json
import pickle


class Stadium:
    def __init__(self, stadium, city, capacity):
        """
        Функция инициализирует объект стадион.
        :param stadium: Название стадиона.
        :param city: Город в котором стадион расположен
        :param capacity: Его вместительность.
        """
        self.stadium = stadium
        self.city = city
        self.capacity = capacity

    def display_stadium(self):
        """
        Функция выводит информацию о стадионе.
        """
        print(f'Стадион: {self.stadium}, Город: {self.city}, Вместимость: {self.capacity}')

    def edit_information_stadium(self, stadium=None, city=None, capacity=None):
        """
        Функция корректирует данные о стадионе.
        :param stadium: Название стадиона.
        :param city: Город в котором стадион расположен
        :param capacity: Его вместительность.
        """
        if stadium is not None:
            self.stadium = stadium
        if city is not None:
            self.city = city
        if capacity is not None:
            self.capacity = capacity
        print(f'Измененные данные: Стадион: {self.stadium}, Город: {self.city}, Вместимость: {self.capacity}')


class JsonAdapter:
    """
    Класс JsonAdapter реализует возможность сохранения информации в Json файл при помощи использования
    паттерна Adapter, а так же загрузку файла.
    """

    @staticmethod
    def save_json(data, filename):
        """
        Функция сохраняет информацию в файл при помощи Json
        :param data: информация о стадионе.
        :param filename: Название файла в который сохраняется информация.
        """
        if isinstance(data, Stadium):
            with open(filename, 'w', encoding='utf-8') as file:
                json.dump({
                    "stadium": data.stadium,
                    "city": data.city,
                    "capacity": data.capacity,
                }, file, ensure_ascii=False, indent=4)  # Возвращаем None, если data не является экземпляром Stadium
            print(f'Данные успешно сохранены в файл {filename}')

    @staticmethod
    def load_json(filename):
        """
        Функция загружает информацию из файла Json
        :param filename: Имя файла
        """
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                data = json.load(file)
                stadium = Stadium(data["stadium"], data["city"], data["capacity"])
                print(f'Данные успешно загружены из {filename} при помощи JSON')
                return stadium
        except (json.JSONDecodeError, KeyError) as e:
            print(f'Ошибка при загрузке данных: {e}')
            return None


class Pickle:

    def save_data(self, stadium, filename):
        """
        Сохраняет объект Stadium в файл формата Pickle.
        :param stadium: Экземпляр Stadium для сохранения.
        :param filename: Имя файла для сохранения данных.
        """
        if isinstance(stadium, Stadium):
            with open(filename, 'wb') as file:
                pickle.dump(stadium, file)
                print(f'Данные успешно сохранены в файл {filename} при помощи pickle.')
        else:
            print('Ошибка: Переданный объект не является экземпляром Stadium.')

    def load_data(self, filename):
        """
        Загружает объект Stadium из файла формата Pickle.
        :param filename: Имя файла для загрузки данных.
        :return: Экземпляр Stadium или None в случае ошибки.
        """
        try:
            with open(filename, 'rb') as file:
                stadium = pickle.load(file)
                if isinstance(stadium, Stadium):
                    print(f'Данные успешно загружены из файла {filename} при помощи pickle.')
                    return stadium
                else:
                    print('Ошибка: Загруженные данные не являются экземпляром Stadium.')
                    return None
        except FileNotFoundError:
            print(f'Файл {filename} для загрузки не найден.')
