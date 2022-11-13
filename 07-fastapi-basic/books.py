from enum import Enum
from typing import Optional
from fastapi import FastAPI

app = FastAPI()

BOOKS = {
    'book_1': {'title': 'Title One', 'author': 'Author One'},
    'book_2': {'title': 'Title Two', 'author': 'Author Two'},
    'book_3': {'title': 'Title Three', 'author': 'Author Three'},
    'book_4': {'title': 'Title Four', 'author': 'Author Four'},
    'book_5': {'title': 'Title Five', 'author': 'Author Five'},
}


@app.get("/")
async def read_all_books(skip_book: Optional[str] = None):
    '''
    curl -X 'GET' 'http://localhost:8000/?skip_book=book_3'
    '''
    if skip_book:
        new_books = BOOKS.copy()
        del new_books[skip_book]
        return new_books
    return BOOKS


@app.get("/{book_name}")
async def read_book(book_name: str):
    return BOOKS[book_name]


@app.post("/")
async def create_book(book_title, book_author):
    largest_book_id = 0

    # find the largest book id
    if len(BOOKS) > 0:
        for book in BOOKS:
            x = int(book.split('_')[-1])
            if x > largest_book_id:
                largest_book_id = x

    new_book_id = f'book_{largest_book_id + 1}'

    BOOKS[new_book_id] = {'title': book_title, 'author': book_author}
    return BOOKS[new_book_id]


@app.put("/{book_name}")
async def update_book(book_name: str, book_title: str, book_author: str):
    book_information = {'title': book_title, 'author': book_author}
    BOOKS[book_name] = book_information
    return book_information


@app.delete("/{book_name}")
async def delete_book(book_name: str):
    del BOOKS[book_name]
    return f'Book_{book_name} deleted'
