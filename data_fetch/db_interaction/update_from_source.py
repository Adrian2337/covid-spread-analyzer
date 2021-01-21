import sys
from data_fetch.db_interaction.data_interaction import update_data


def main(argv):
    if len(argv) == 1:
        print(
            """Usage:
            update_data start_date end_date"""
        )
    else:
        start_date = argv[1]
        end_date = argv[2]
        update_data(start_date, end_date)


if __name__ == '__main__':
    main(sys.argv)
