from django.shortcuts import render
from covid_spread_analyzer.database_operations import load_data, save_data
from covid_spread_analyzer.prediction_app.predictions_handler import filter_data, add_days_to_date, \
    fill_data_with_predictions, predict_and_save_


def prediction_view(request):
    # predict_and_save_()
    data_voiv = load_data('Voivodeships')
    voivodes = list(data_voiv.keys())
    dates = list(data_voiv[voivodes[0]].keys())
    results = dict()
    for case_type in ['daily infected', 'daily deceased', 'daily cured']:
        try:
            filtered_data = filter_data(data_voiv, dates, voivodes, case_type)
            results[case_type] = filtered_data
        except KeyError:
            pass
    dates.append(add_days_to_date(dates[-1], 1))
    predicted_values = load_data('Predictions')

    # fill_data_with_predictions(filtered_data, predicted_values)

    return render(request=request, template_name='prediction.html',
                  context={'graph_data': results, 'predicted_values': predicted_values, 'dates': dates})
