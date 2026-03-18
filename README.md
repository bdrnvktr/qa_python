# Бударин Виктор


В проекте реализованы следующие тесты:

Проверка инициализации атрибутов конструктора
test_constructor_initializes_attributes — проверяет, что при создании объекта BooksCollector атрибуты (books_genre, favorites, genre, genre_age_rating) инициализируются корректно.

Добавление двух книг
test_add_new_book_add_two_books — убеждается, что после добавления двух книг словарь books_genre содержит ровно 2 записи.

Добавление книги с корректным названием
test_add_new_book_valid_name — проверяет, что книга с валидным именем добавляется в books_genre, а её жанр по умолчанию — пустая строка.

Добавление книги с названием из 1 символа
test_add_new_book_valid_name_1_symbol_added — подтверждает, что книга с односимвольным названием корректно добавляется.

Добавление книги с названием из 40 символов
test_add_new_book_valid_name_40_symbols_added — проверяет добавление книги с максимально допустимой длиной названия (40 символов).

Попытка добавить книгу с пустым названием
test_add_new_book_not_valid_name_0_symbols_not_added — убеждается, что книга с пустым именем не добавляется в словарь.

Попытка добавить книгу с названием из 41 символа
test_add_new_book_not_valid_name_41_symbols_not_added — проверяет, что название длиннее 40 символов не принимается.

Попытка добавить дубликат книги
test_add_new_book_duplicate_not_added — гарантирует, что повторная попытка добавить уже существующую книгу не увеличивает размер словаря.

Установка валидного жанра для книги
test_set_book_genre_valid_added (с параметризацией) — проверяет корректное присвоение жанров («Фантастика», «Ужасы», «Детективы») существующим книгам.

Попытка установить жанр для несуществующей книги
test_set_book_genre_invalid_book_not_added — убеждается, что жанр не присваивается книге, отсутствующей в books_genre.

Попытка установить недопустимый жанр
test_set_book_genre_invalid_genre_not_added — проверяет, что жанры, не входящие в список допустимых (genre), не сохраняются.

Получение книг определённого жанра
test_get_books_with_specific_genre_success — тестирует метод get_books_with_specific_genre, который возвращает список книг заданного жанра.

Получение полного словаря книг с жанрами
test_get_books_genre_success — проверяет, что метод get_books_genre возвращает актуальный словарь books_genre.

Получение детских книг
test_get_books_for_children_success — убеждается, что метод get_books_for_children возвращает только книги, не входящие в возрастные ограничения (genre_age_rating).

Добавление книги в избранное
test_add_book_in_favorites_valid_added — проверяет, что существующая книга успешно добавляется в список favorites.

Попытка добавить дубликат в избранное
test_add_book_in_favorites_duplicate_1_added — гарантирует, что повторное добавление книги в избранное не приводит к дублированию.

Попытка добавить несуществующую книгу в избранное
test_add_book_in_favorites_invalid_not_added — проверяет, что книги, отсутствующие в books_genre, не могут быть добавлены в избранное.

Удаление книги из избранного
test_delete_book_from_favorites_success — тестирует корректное удаление книги из списка favorites.

Попытка удалить несуществующую книгу из избранного
test_delete_book_from_favorites_not_in_list_success — убеждается, что удаление отсутствующей книги не вызывает ошибок и не изменяет список.

Получение списка избранных книг
test_get_list_of_favorites_books_success — проверяет, что метод get_list_of_favorites_books возвращает актуальный список favorites с правильным количеством элементов.

оценка покрытия 85-90%

Ниже результаты тестов:

================================================== test session starts ===================================================
platform win32 -- Python 3.14.2, pytest-9.0.2, pluggy-1.6.0 -- C:\Users\Admin\AppData\Local\Python\pythoncore-3.14-64\python.exe
cachedir: .pytest_cache
rootdir: C:\qa_python
plugins: cov-7.0.0
collected 22 items

tests.py::TestBooksCollector::test_constructor_initializes_attributes PASSED                                        [  4%] 
tests.py::TestBooksCollector::test_add_new_book_add_two_books PASSED                                                [  9%] 
tests.py::TestBooksCollector::test_add_new_book_valid_name PASSED                                                   [ 13%] 
tests.py::TestBooksCollector::test_add_new_book_valid_name_1_symbol_added PASSED                                    [ 18%] 
tests.py::TestBooksCollector::test_add_new_book_valid_name_40_symbols_added PASSED                                  [ 22%] 
tests.py::TestBooksCollector::test_add_new_book_not_valid_name_0_symbols_not_added PASSED                           [ 27%] 
tests.py::TestBooksCollector::test_add_new_book_not_valid_name_41_symbols_not_added PASSED                          [ 31%] 
tests.py::TestBooksCollector::test_add_new_book_duplicate_not_added PASSED                                          [ 36%] 
tests.py::TestBooksCollector::test_set_book_genre_valid_added[\u0413\u0430\u0440\u0440\u0438 \u041f\u043e\u0442\u0442\u0435\u0440-\u0424\u0430\u043d\u0442\u0430\u0441\u0442\u0438\u043a\u0430] PASSED [ 40%]
tests.py::TestBooksCollector::test_set_book_genre_valid_added[\u041e\u043d\u043e-\u0423\u0436\u0430\u0441\u044b] PASSED [ 45%]
tests.py::TestBooksCollector::test_set_book_genre_valid_added[\u0428\u0435\u0440\u043b\u043e\u043a \u0425\u043e\u043b\u043c\u0441-\u0414\u0435\u0442\u0435\u043a\u0442\u0438\u0432\u044b] PASSED [ 50%]
tests.py::TestBooksCollector::test_set_book_genre_invalid_book_not_added PASSED                                     [ 54%] 
tests.py::TestBooksCollector::test_set_book_genre_invalid_genre_not_added PASSED                                    [ 59%] 
tests.py::TestBooksCollector::test_get_books_with_specific_genre_success PASSED                                     [ 63%]
tests.py::TestBooksCollector::test_get_books_genre_success PASSED                                                   [ 68%] 
tests.py::TestBooksCollector::test_get_books_for_children_success PASSED                                            [ 72%] 
tests.py::TestBooksCollector::test_add_book_in_favorites_valid_added PASSED                                         [ 77%] 
tests.py::TestBooksCollector::test_add_book_in_favorites_duplicate_1_added PASSED                                   [ 81%] 
tests.py::TestBooksCollector::test_add_book_in_favorites_invalid_not_added PASSED                                   [ 86%] 
tests.py::TestBooksCollector::test_delete_book_from_favorites_success PASSED                                        [ 90%] 
tests.py::TestBooksCollector::test_delete_book_from_favorites_not_in_list_success PASSED                            [ 95%] 
tests.py::TestBooksCollector::test_get_list_of_favorites_books_success PASSED                                       [100%] 

==================================== 22 passed in 0.15s =================================== 