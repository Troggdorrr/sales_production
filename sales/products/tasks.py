from sales.celery import app

from .parsers import BaseParser
from .parsers.magnit import MagnitParser
from .parsers.pyaterochka import PyaterochkaParser


class Parser:
    def __init__(self, parser: BaseParser) -> None:
        self._parser = parser

    def update_db(self):
        self._parser.save_data()


@app.task
def parse_magnit():
    parser = Parser(MagnitParser())
    parser.update_db()


@app.task
def parse_pyaterochka():
    parser = Parser(PyaterochkaParser())
    parser.update_db()