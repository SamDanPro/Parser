import requests
from bs4 import BeautifulSoup
import csv


def simple_parser():

    url = "http://books.toscrape.com/"

    try:

        response = requests.get(url)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')


        books = soup.find_all('article', class_='product_pod')

        print(f"Найдено книг: {len(books)}")
        print("-" * 50)


        with open('books.csv', 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Название', 'Цена', 'Рейтинг', 'Ссылка'])

            for book in books:

                title = book.h3.a['title']
                price = book.find('p', class_='price_color').text
                rating_class = book.find('p', class_='star-rating')['class'][1]
                rating = f"{rating_class} "
                book_link = url + book.h3.a['href']

                print(f"{title}")
                print(f"Цена: {price}")
                print(f"Рейтинг: {rating}")
                print(f"Ссылка: {book_link}")
                print("-" * 30)


                writer.writerow([title, price, rating, book_link])

        print(" Данные сохранены в файл books.csv")

    except requests.RequestException as e:
        print(f"Ошибка при запросе: {e}")
    except Exception as e:
        print(f"Произошла ошибка: {e}")


if __name__ == "__main__":
    simple_parser()