import pytest
from main import BooksCollector


class TestBooksCollector:

    def test_constructor_initializes_attributes(self):
        collector = BooksCollector()
        collector.books_genre = {}
        collector.favorites = []
        collector.genre = ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']
        collector.genre_age_rating = ['Ужасы', 'Детективы']

    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.books_genre) == 2

    def test_add_new_book_valid_name(self):
        collector = BooksCollector()
        collector.add_new_book('Война и мир')
        assert 'Война и мир' in collector.books_genre
        assert collector.books_genre['Война и мир'] == ''

    def test_add_new_book_valid_name_1_symbol_added(self):
        collector = BooksCollector()
        collector.add_new_book('a')
        assert 'a' in collector.books_genre
        assert collector.books_genre['a']==''

    def test_add_new_book_valid_name_40_symbols_added(self):
        collector = BooksCollector()
        long_name = 'a' * 40
        collector.add_new_book(long_name)
        assert long_name in collector.books_genre
        assert collector.books_genre[long_name]==''


    def test_add_new_book_not_valid_name_0_symbols_not_added(self):
        collector = BooksCollector()
        collector.add_new_book('')
        assert '' not in collector.books_genre


    def test_add_new_book_not_valid_name_41_symbols_not_added(self):
        collector = BooksCollector()
        long_name = 'a' * 41
        collector.add_new_book(long_name)
        assert long_name not in collector.books_genre


    def test_add_new_book_duplicate_not_added(self):
        collector = BooksCollector()
        collector.add_new_book('Преступление и наказание')
        collector.add_new_book('Преступление и наказание')
        assert len(collector.books_genre) == 1
        assert collector.books_genre['Преступление и наказание']==''

    @pytest.mark.parametrize(
        'book_name, genre',
        [
        ('Гарри Поттер', 'Фантастика'),
        ('Оно', 'Ужасы'),
        ('Шерлок Холмс', 'Детективы'),
        ],
        )

    def test_set_book_genre_valid_added(self, book_name, genre):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        assert collector.get_book_genre(book_name) == genre


    def test_set_book_genre_invalid_book_not_added(self):
        collector = BooksCollector()
        collector.set_book_genre('Неизвестная книга', 'Фантастика')
        assert collector.get_book_genre('Неизвестная книга') is None


    def test_set_book_genre_invalid_genre_not_added(self):
        collector = BooksCollector()
        collector.add_new_book('Книга без жанра')
        collector.set_book_genre('Книга без жанра', 'Романтика')
        assert collector.get_book_genre('Книга без жанра') == ''


    def test_get_books_with_specific_genre_success(self):
        collector = BooksCollector()
        collector.add_new_book('Дюна')
        collector.set_book_genre('Дюна', 'Фантастика')
        collector.add_new_book('Основание')
        collector.set_book_genre('Основание', 'Фантастика')
        books = collector.get_books_with_specific_genre('Фантастика')
        assert books == ['Дюна', 'Основание']

    def test_get_books_genre_success(self):
        collector = BooksCollector()
        collector.add_new_book('1984')
        collector.set_book_genre('1984', 'Фантастика')
        result = collector.get_books_genre()
        assert result == {'1984': 'Фантастика'}

    def test_get_books_for_children_success(self):
        collector = BooksCollector()
        collector.add_new_book('Винни-Пух')
        collector.set_book_genre('Винни-Пух', 'Мультфильмы')
        collector.add_new_book('Оно')
        collector.set_book_genre('Оно', 'Ужасы')
        children_books = collector.get_books_for_children()
        assert children_books == ['Винни-Пух']

    def test_add_book_in_favorites_valid_added(self):
        collector = BooksCollector()
        collector.add_new_book('Мастер и Маргарита')
        collector.add_book_in_favorites('Мастер и Маргарита')
        assert 'Мастер и Маргарита' in collector.favorites

    def test_add_book_in_favorites_duplicate_1_added(self):
        collector = BooksCollector()
        collector.add_new_book('Идиот')
        collector.add_book_in_favorites('Идиот')
        collector.add_book_in_favorites('Идиот')
        assert len(collector.favorites) == 1

    def test_add_book_in_favorites_invalid_not_added(self):
        collector = BooksCollector()
        collector.add_book_in_favorites('Неизвестная книга')
        assert 'Неизвестная книга' not in collector.favorites
        assert collector.favorites == []

    def test_delete_book_from_favorites_success(self):
        collector = BooksCollector()
        collector.add_new_book('Анна Каренина')
        collector.add_book_in_favorites('Анна Каренина')
        collector.delete_book_from_favorites('Анна Каренина')
        assert 'Анна Каренина' not in collector.favorites
        assert collector.favorites == []

    def test_delete_book_from_favorites_not_in_list_success(self):
        collector = BooksCollector()
        collector.delete_book_from_favorites('Не в избранном')
        assert collector.favorites == []

    def test_get_list_of_favorites_books_success(self):
        collector = BooksCollector()
        collector.add_new_book('Евгений Онегин')
        collector.add_new_book('Герой нашего времени')
        collector.add_book_in_favorites('Евгений Онегин')
        collector.add_book_in_favorites('Герой нашего времени')
        favorites = collector.get_list_of_favorites_books()
        assert favorites == ['Евгений Онегин', 'Герой нашего времени']
        assert len(favorites) == 2

        