import datetime

from numpy import asarray, arange, insert

from covid_spread_analyzer.database_operations import load_data, save_data
from covid_spread_analyzer.prediction_app.PredictionService import PredictionService
from covid_spread_analyzer.prediction_app.predictioner import convert_to_learning_set, get_prediction_set


def add_days_to_date(date, days):
    date_1 = datetime.datetime.strptime(date, "%Y-%m-%d")
    return str(date_1 + datetime.timedelta(days=days)).split()[0]


def predict_and_save_(data_voivodeships=None):
    if not data_voivodeships:
        data_voivodeships = load_data('Voivodeships')
    for case_type in ['daily infected', 'daily deceased', 'daily cured']:
        try:
            voi_names_list = list(data_voivodeships.keys())
            dates = list(data_voivodeships[voi_names_list[0]].keys())
            filtered_data = filter_data(data_voivodeships, dates, voi_names_list, case_type)
            dates.append(add_days_to_date(dates[-1], 1))
            predictions = get_predictions(filtered_data)
            save_data({"date": dates[-1], "Voivodeships": predictions}, "Predictions", case_type)
        except IndexError or KeyError:
            pass


def fill_data_with_predictions(filtered_data, predicted_values):
    for k, v in filtered_data.items():
        filtered_data[k].extend([predicted_values[k]])


def get_predictions(filtered_data):
    predicted_values = dict()
    predictioner = PredictionService.get_predictioner()
    for k, v in filtered_data.items():
        print(f'{str(len(v))} update {k} {str(v)}')
        if len(v) > 29:
            x_train, y_train = convert_to_learning_set(v)
            predictioner.update_input(x_train, y_train)
            predictioner.fit_model()
            x_prediction_list = get_prediction_set(v)
            y_predicted = predictioner.predict(x_prediction_list)
            y_predicted = y_predicted.reshape(1, y_predicted.shape[0])[0]
            predicted_values[k] = [int(p) for p in y_predicted]
    return predicted_values


def filter_data(data_voiv, dates, voivodes, cases='daily infected'):
    prediction_dict = dict()
    for voi in voivodes:
        inf_cases = []
        for dat in dates:
            try:
                inf_cases.append(data_voiv[voi][dat][cases])
            except KeyError:
                pass
        prediction_dict[voi] = inf_cases
    return prediction_dict
