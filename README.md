# qa_python - Проект 2-ого спринта

main.py
---------
Файл содержит класс 'BooksCollector', включающий:
- Словарь books_rating, в который можно добавлять пару Название книги: Рейтинг книги.
- Список favorites, который содержит избранные книги.
Набор методов для работы со словарем books_rating и списком favorites:
- add_new_book — добавляет новую книгу в словарь и выставляет ей по умолчанию рейтинг 1. Одну и ту же книгу можно добавить только один раз.
- set_book_rating — устанавливает рейтинг книги, если книга есть в books_rating и её рейтинг от 1 до 10. Установить рейтинг меньше 1 и больше 10 нельзя.
- get_book_rating — выводит рейтинг книги по её имени.
- get_books_with_specific_rating — выводит список книг с указанным рейтингом от 1 до 10.
- get_books_rating — выводит текущий словарь books_rating.
- add_book_in_favorites — добавляет книгу в избранное. Книга должна находиться в словаре books_rating. Повторно добавить книгу в избранное нельзя.
- delete_book_from_favorites — удаляет книгу из избранного, если она там есть.
- get_list_of_favorites_books — получает список избранных книг.

tests.py
----------
Файл содержит набор юнит-тестов для тестирования методов класса 'BooksCollector'

test_add_new_book_add_two_books
проверяет метод add_new_book добавлением книг в словарь

test_set_book_rating_add_positive_rating_positive_result
проверяет метод set_book_rating путем присвоения книге рейтинга и отображения результатов присвоения в словаре

test_get_book_rating_positive_rating_positive_result
проверяет метод get_book_rating путем вывода рейтинга книги по её имени

test_get_books_with_specific_rating_real_rating_positive_result
проверяет метод get_books_with_specific_rating вывода наименований книг по их рейтингу

test_get_books_rating_dictionary_is_not_empty_positive_result
проверяет метод get_books_rating вывода наименований книг по их рейтингу

test_add_book_in_favorites_add_real_book_positive_result
проверяет метод add_book_in_favorites путем добавления книги в список избранного и вывода списка избранных книг

test_delete_book_from_favorites_delete_real_book_positive_result
проверяет метод delete_book_from_favorites путем удаления книги из списка избранных и вывода списка избранных книг

test_get_list_of_favorites_books_add_real_books_positive_result
проверяет метод get_list_of_favorites_books путем проверки содержимого списка избранных книг

test_set_book_rating_more_10_dictionary_is_empty
проверяет метод set_book_rating если книге присвоить рейтинг выше 10

test_set_book_rating_zero_dictionary_is_empty
проверяет метод set_book_rating если книге присвоить рейтинг 0