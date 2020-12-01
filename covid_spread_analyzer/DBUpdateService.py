import covid_spread_analyzer.database_operations as db
from covid_spread_analyzer.prediction_app.predictions_service import predict_and_save_
from data_fetch.twitter.DataYieldService import DataYieldService


class DBUpdateService:
    @staticmethod
    def update_database():
        last_update_date = db.load_data("Last Update Date")
        data = DataYieldService.yield_data_since(last_update_date)
        DBUpdateService.__insert_data(data)
        predict_and_save_()

    @staticmethod
    def __insert_data(data):
        for date in data["Map Data"].keys():
            db.save_data(data["Map Data"][date], "Map Data", date)

        for date in data["Poland"].keys():
            db.save_data(data["Poland"][date], "Poland", date)

        for voivodeship in data["Voivodeships"].keys():
            for date in data["Voivodeships"][voivodeship].keys():
                db.save_data(data["Voivodeships"][voivodeship][date], "Voivodeships", voivodeship, date)

        db.save_data({"Last Update Date": data["Last Update Date"]})
