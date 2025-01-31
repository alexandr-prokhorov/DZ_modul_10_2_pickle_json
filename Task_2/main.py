from Task_2.book import *

if __name__ == '__main__':
    print()
    # Создаем экземпляр книги.
    book1 = Book("Мизери", "Стивен Кинг", "1987")
    # Выводим информацию.
    book1.display_book()
    # Изменяем информацию о книге.
    book1.edit_information_book("Атлант расправил плечи", "Айн Рэнд", "1957")
    print()
    # Сохраняем информацию в формате через JSON
    json = Json()
    json.save_data(book1, "book.json")
    # Загружаем информацию из файла формата JSON
    loaded_book_json = json.load_data("book.json")
    # Выводим информацию.
    loaded_book_json.display_book()
    print()
    # Сохраняем информацию в формате через Pickle.
    pickle = Pickle()
    pickle.save_data(book1, "book.pkl")
    # Загружаем информацию из файла формата Pickle.
    loaded_book_pickle = pickle.load_data("book.pkl")
    # Выводим информацию.
    loaded_book_pickle.display_book()
