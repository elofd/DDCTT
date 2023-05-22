from django.core.management import BaseCommand
from openpyxl import load_workbook

from places.models import Place


class Command(BaseCommand):
    """
    Добавление данных из xlsx файла в БД
    """

    def handle(self, *args, **options):
        filename = 'places.xlsx'
        wb = load_workbook(filename, read_only=True)
        ws = wb.active

        for row in ws.iter_rows(min_row=2, values_only=True):
            name, point, raiting = row
            print(name, point, raiting, sep=' | ')

