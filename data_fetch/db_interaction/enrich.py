from interact import main as interact
from update_from_source import main as update
import sys
from firebase_admin import credentials, initialize_app


def main(argv):
	if len(argv) == 1:
		print("""Usage:
main start_date end_date
	where dates are in YYYY-MM-DD format""")
	else:
		cred = credentials.Certificate(
			'../../firebase_files/covid-spread-analyzer-firebase-adminsdk-hxchu-8c78edc7cd.json'
		)
		initialize_app(cred, {
			'databaseURL': 'https://covid-spread-analyzer.firebaseio.com/'
		})
		print("downloading from database")
		interact([None, "-d", argv[1], argv[2]])
		print("\nenriching data from database")
		update([None, argv[1], argv[2]])
		print("\nsaving data to database")
		interact([None, "-u"])


if __name__ == "__main__":
	main(sys.argv)
