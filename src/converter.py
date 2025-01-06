import csv
from pathlib import Path

from openpyxl import load_workbook


def main() -> None:
    filename = input('Enter Excel file: ')
    path = Path(filename)

    workbook = load_workbook(path, data_only=True)
    sheet = workbook.active

    outpath = Path(f'{sheet.title}.csv')

    with outpath.open('w', newline='') as fout:
        csv_writer = csv.writer(fout)
        csv_writer.writerows(sheet.iter_rows(values_only=True))


if __name__ == '__main__':
    main()
