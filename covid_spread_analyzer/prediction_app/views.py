import random

from django.shortcuts import render

# from covid_spread_analyzer.settings import predictioner

from covid_spread_analyzer.prediction_app.predictioner import Predictioner


# x = asarray([i for i in range(-100, 100)])
# predict_x = asarray([i for i in range(-100, 140)])
# y = asarray([i ** 2.0 for i in range(-100, 100)])


# predictioner.update_input(x, y)
# predictioner.fit_model()
# predicted_y = predictioner.predict(predict_x)


def prediction_view(request):
    ##
    # x = asarray([i for i in range(-100, 100)])
    # predict_x = asarray([i for i in range(-100, 140)])
    # y = asarray([i ** 2.0 for i in range(-100, 100)])
    x, y = [i for i in range(-100, 100)], [2 * i for i in range(-100, 100)]
    return render(request=request, template_name='prediction.html',
                  context={'x': x, 'total': [random.randint(0, 10) for _ in range(-100, 100)],
                           'cured': [random.randint(0, 10) for _ in range(-100, 100)],
                           'deaths': [random.randint(0, 10) for _ in range(-100, 100)]})
