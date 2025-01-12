import constants as const
from converter import xlsx_to_csv


def main() -> None:
    for excel_file in const.INPUT_DIR.glob('*.xlsx'):
        csv_file = const.OUTPUT_DIR / excel_file.with_suffix('.csv').name
        
        xlsx_to_csv(excel_file, csv_file)
        
        excel_file.rename(const.CONSUMED_DIR / excel_file.name)


if __name__ == '__main__':
    main()
