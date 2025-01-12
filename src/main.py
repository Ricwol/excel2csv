from constants import (
    CONSUMED_DIR,
    INPUT_DIR,
    OUTPUT_DIR
)
from converter import xlsx_to_csv


def main() -> None:
    for excel_file in INPUT_DIR.glob('*.xlsx'):
        csv_file = OUTPUT_DIR / excel_file.with_suffix('.csv').name
        
        xlsx_to_csv(excel_file, csv_file)
        
        excel_file.rename(CONSUMED_DIR / excel_file.name)


if __name__ == '__main__':
    main()
