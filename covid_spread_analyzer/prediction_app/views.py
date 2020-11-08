import datetime
import random

from django.shortcuts import render
from numpy import asarray, arange

from covid_spread_analyzer.settings import predictioner
from covid_spread_analyzer.database_operations import load_data


def add_days_to_date(date, days):
    date_1 = datetime.datetime.strptime(date, "%Y-%m-%d")
    return str(date_1 + datetime.timedelta(days=days)).split()[0]


def prediction_view(request):
    data_voiv = load_data('Voivodeships')
    voivodes = list(data_voiv.keys())
    dates = list(data_voiv[voivodes[0]].keys())
    filtered_data = filter_data(data_voiv, dates, voivodes)
    # must be after filtering.!
    dates.append(add_days_to_date(dates[-1], 1))
    x_train = asarray(list(arange(len(filtered_data[list(filtered_data.keys())[0]]))))
    filtered_data, predicted_values = fill_predictions(filtered_data, x_train)
    return render(request=request, template_name='prediction.html',
                  context={'graph_data': filtered_data, 'predicted_values': predicted_values, 'dates': dates})


def fill_predictions(filtered_data, x_train):
    predicted_values = dict()
    for k, v in filtered_data.items():
        predictioner.update_input(x_train, asarray(v))
        predictioner.fit_model()
        predicted_values[k] = int(list(predictioner.predict(asarray([x_train[-1] + 1]))[0])[0])
        filtered_data[k].extend([predicted_values[k]])
    return filtered_data, predicted_values


def filter_data(data_voiv, dates, voivodes):
    prediction_dict = dict()
    for voi in voivodes:
        inf_cases = []
        for dat in dates:
            inf_cases.append(data_voiv[voi][dat]['daily infected'])
        prediction_dict[voi] = inf_cases
    return prediction_dict
