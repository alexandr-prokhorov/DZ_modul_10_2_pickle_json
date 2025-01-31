from Task_3.stadium import *

if __name__ == "__main__":
    print()
    # Создаем объект Stadium с неправильными данными
    stadium = Stadium("Камп-ноу", "Мадрид", 100000)
    # Выводим информацию
    stadium.display_stadium()
    print()
    # Корректируем данные о стадионе.
    stadium.edit_information_stadium("Камп-ноу", "Барселона", 99354)
    # Выводим информацию
    stadium.display_stadium()
    print()
    # Сохраняем объект в JSON
    JsonAdapter.save_json(stadium, 'stadium.json')
    # Загружаем объект из JSON
    loaded_stadium = JsonAdapter.load_json('stadium.json')
    # Выводим информацию
    loaded_stadium.display_stadium()
    print()
    # Для работы с форматом Pickle
    pickle = Pickle()
    # Сохраняем в файл в формате Pickle
    pickle.save_data(stadium, 'stadium.pkl')
    # Загружаем из файла формата Pickle
    loaded_stadium_pickle = pickle.load_data('stadium.pkl')
    # Выводим информацию
    loaded_stadium_pickle.display_stadium()