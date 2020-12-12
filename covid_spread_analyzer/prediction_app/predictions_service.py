import datetime

from numpy import asarray, arange, insert

from covid_spread_analyzer.database_operations import load_data, save_data
from covid_spread_analyzer.prediction_app.PredictionService import PredictionService


def add_days_to_date(date, days):
    date_1 = datetime.datetime.strptime(date, "%Y-%m-%d")
    return str(date_1 + datetime.timedelta(days=days)).split()[0]


def predict_and_save_(data_voivodeships=None):
    if not data_voivodeships:
        data_voivodeships = load_data('Voivodeships')
    for case_type in ['daily infected', 'daily deceased', 'daily cured']:
        voi_names_list = list(data_voivodeships.keys())
        dates = list(data_voivodeships[voi_names_list[0]].keys())
        filtered_data = filter_data(data_voivodeships, dates, voi_names_list, case_type)
        dates.append(add_days_to_date(dates[-1], 1))
        x_train = asarray(list(arange(len(filtered_data[list(filtered_data.keys())[0]]))))
        predictions = get_predictions(filtered_data, x_train, single=False)
        save_data({"date": dates[-1], "Voivodeships": predictions}, "Predictions", case_type)


def fill_data_with_predictions(filtered_data, predicted_values):
    for k, v in filtered_data.items():
        filtered_data[k].extend([predicted_values[k]])


def get_predictions(filtered_data, x_train, single=True):
    predicted_values = dict()
    predictioner = PredictionService.get_predictioner()
    if not single:
        x_new = insert(x_train, len(x_train), len(x_train))
    for k, v in filtered_data.items():
        predictioner.update_input(x_train, asarray(v))
        predictioner.fit_model()
        if single:
            predicted_values[k] = int(list(predictioner.predict(asarray([x_train[-1] + 1]))[0])[0])
        else:
            predicted_values[k] = [int(x) for x in
                                   predictioner.predict(asarray(x_new)).reshape(1, len(x_new)).tolist()[0]]
    return predicted_values


def filter_data(data_voiv, dates, voivodes, cases='daily infected'):
    prediction_dict = dict()
    for voi in voivodes:
        inf_cases = []
        for dat in dates:
            inf_cases.append(data_voiv[voi][dat][cases])
        prediction_dict[voi] = inf_cases
    return prediction_dict
