from Task_1.car import *


if __name__ == '__main__':
    # Словарь в который будем добавлять автомобили.
    car_dict = Car()
    # Для работы с форматом Pickle
    pickle = Pickle()
    # Для работы с форматом Json
    json = Json()
    # Добавляем автомобили в словарь.
    car_dict.add_cars("Toyota", "Corolla", "Седан")
    car_dict.add_cars("BMW", "X5", "Внедорожник")
    car_dict.add_cars("Audi","R8","Спорт-кар")
    print("Ваш список")
    # Выводим полный список добавленных автомобилей.
    car_dict.display_cars()
    # Удаляем автомобиль из словаря.
    car_dict.remove_cars("BMW")
    print("Обновленный список")
    # повторно выводим список автомобилей после удаления
    car_dict.display_cars()
    print()
    # Сохраняем словарь в формате Pickle.
    pickle.save_data(car_dict.cars,  "cars.pkl")
    # Загружаем словарь в формате Pickle.
    car_dict.cars = pickle.load_data("cars.pkl")
    car_dict.display_cars()
    print()
    # Сохраняем словарь в формате Json.
    json.save_data(car_dict.cars, "cars.json")
    # Загружаем словарь в формате Json.
    car_dict.cars = json.load_data("cars.json")
    car_dict.display_cars()
