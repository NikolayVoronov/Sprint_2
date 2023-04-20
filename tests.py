from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    def test_set_book_rating_add_positive_rating_positive_result(self):
        collector_1 = BooksCollector()

        collector_1.add_new_book('Сборник пацанских цитат')
        collector_1.set_book_rating('Сборник пацанских цитат', 10)

        assert collector_1.books_rating == {'Сборник пацанских цитат': 10}

    def test_get_book_rating_positive_rating_positive_result(self):
        collector_2 = BooksCollector()

        collector_2.add_new_book('Прикольчики от беломорчика')
        collector_2.add_new_book('НеПрикольчики от беломорчика')
        collector_2.set_book_rating('Прикольчики от беломорчика', 9)
        collector_2.set_book_rating('НеПрикольчики от беломорчика', 1)

        assert collector_2.get_book_rating('Прикольчики от беломорчика') == 9

    def test_get_books_with_specific_rating_real_rating_positive_result(self):
        collector_3 = BooksCollector()

        collector_3.add_new_book('Горе от пума')
        collector_3.add_new_book('Горе от хурма')
        collector_3.add_new_book('Горе от пижама')
        collector_3.set_book_rating('Горе от пума', 5)
        collector_3.set_book_rating('Горе от хурма', 5)
        collector_3.set_book_rating('Горе от пижама', 7)

        assert collector_3.get_books_with_specific_rating(5) == ['Горе от пума', 'Горе от хурма']

    def test_get_books_rating_dictionary_is_not_empty_positive_result(self):
        collector_4 = BooksCollector()

        collector_4.add_new_book('Горе от пума')
        collector_4.add_new_book('Горе от хурма')
        collector_4.set_book_rating('Горе от пума', 5)
        collector_4.set_book_rating('Горе от хурма', 7)

        assert collector_4.get_books_rating() == {'Горе от пума': 5, 'Горе от хурма': 7}

    def test_add_book_in_favorites_add_real_book_positive_result(self):
        collector_5 = BooksCollector()

        collector_5.add_new_book('Главные хиты 16-ого века')
        collector_5.add_book_in_favorites('Главные хиты 16-ого века')

        assert 'Главные хиты 16-ого века' in collector_5.favorites

    def test_delete_book_from_favorites_delete_real_book_positive_result(self):
        collector_6 = BooksCollector()

        collector_6.add_new_book('Главные хиты 16-ого века')
        collector_6.delete_book_from_favorites('Главные хиты 16-ого века')

        assert collector_6.favorites == []

    def test_get_list_of_favorites_books_add_real_books_positive_result(self):
        collector_7 = BooksCollector()

        collector_7.add_new_book('7 деплоев и 1 похороны')
        collector_7.add_new_book('7 раз отмерь, 1 раз деплой')
        collector_7.add_book_in_favorites('7 деплоев и 1 похороны')
        collector_7.add_book_in_favorites('7 раз отмерь, 1 раз деплой')

        assert collector_7.get_list_of_favorites_books() == ['7 деплоев и 1 похороны', '7 раз отмерь, 1 раз деплой']

    def test_set_book_rating_more_10_dictionary_is_empty(self):
        collector_8 = BooksCollector()

        collector_8.add_new_book('Паша техник: 9 жизней')
        collector_8.set_book_rating('Паша техник: 9 жизней', 11)

        assert collector_8.books_rating == {}

    def test_set_book_rating_zero_dictionary_is_empty(self):
        collector_9 = BooksCollector()

        collector_9.add_new_book('Паша техник: 9 жизней')
        collector_9.set_book_rating('Паша техник: 9 жизней', 0)

        assert collector_9.books_rating == {}
