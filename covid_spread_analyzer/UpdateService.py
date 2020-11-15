import covid_spread_analyzer.database_operations as db
from covid_spread_analyzer.DBUpdateService import DBUpdateService
from datetime import *
from threading import Thread
from time import sleep


class UpdateService:

    @staticmethod
    def start():
        last_update_date = db.load_data("Last Update Date")
        if last_update_date < datetime.now().strftime("%Y-%m-%d") and datetime.now().hour >= 11:
            print("UpdateService: Initial update needed.")
            print("UpdateService: Performing db update.")
            DBUpdateService.update_database()
        else:
            print("UpdateService: Initial update unnecessary.")
        t = Thread(target=UpdateService.ward_db, daemon=True)
        t.start()

    @staticmethod
    def ward_db():
        while True:
            delta = (datetime.fromisoformat(datetime.now().strftime("%Y-%m-%d") + " 11") + timedelta(
                days=1) - datetime.now()).total_seconds()
            print("UpdateService: Update starting in", delta, "seconds.")
            t = Thread(target=UpdateService.update_when_eligible, args=(delta, ), daemon=True)   # don't touch args
            t.start()
            t.join()

    @staticmethod
    def update_when_eligible(wait_time):
        sleep(wait_time)
        print("UpdateService: Performing db update.")
        DBUpdateService.update_database()
