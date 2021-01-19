import copy
import random
import time
from signal import alarm

from numpy.ma import arange, asarray
from tensorflow.python.keras.layers import Dense
from tensorflow.python.keras.models import Sequential, model_from_json, load_model

from covid_spread_analyzer.prediction_app.predictioner import Predictioner
import re
from sklearn.model_selection import train_test_split


def read_data(file='temp.txt'):
    with open(file) as f:
        txt = f.read()
        matches = re.findall(r': \d+', txt)
        return [float(re.sub(': ', '', x)) for x in matches]


def test_neural_network(data, model=None):
    y = asarray(data)
    x = arange(len(data))
    y_train, y_test, x_train, x_test = train_test_split(y, x, test_size=0.33)
    guesser = Predictioner(model_input=model)
    guesser.update_input(train_x=x_train, train_y=y_train)
    history = guesser.fit_model(verbose=0)
    eva = guesser.evaluate(y_test, x_test)
    guesser.predict(x)
    guesser.visualize()
    return eva[0]


def get_random_activation():
    return random.choice(
        ['sigmoid',
         'tanh',
         'selu',
         'relu',
         'elu'])


def get_time():
    return int(round(time.time() * 1000))


def get_random_model():
    model = Sequential()
    model.add(Dense(1, activation=get_random_activation()))
    for x in range(random.randint(0, 10)):
        model.add(Dense(random.randint(1, 100), activation=get_random_activation()))
        model.add(Dense(random.randint(1, 100), activation=get_random_activation()))
        model.add(Dense(random.randint(1, 100), activation=get_random_activation()))
        model.add(Dense(random.randint(1, 100), activation=get_random_activation()))
        model.add(Dense(random.randint(1, 100), activation=get_random_activation()))
    model.add(Dense(1, activation=get_random_activation()))
    return model


def local_search(secs, data):
    end_time = get_time() + secs * 1000
    model = get_random_model()
    loss = test_neural_network(data, model)
    best = loss
    best_model = model
    while get_time() < end_time:
        model = get_random_model()
        loss = test_neural_network(data, model)
        if loss < best:
            best = loss
            best_model = copy.deepcopy(model)
            print("Best moved to: {}".format(best))
            if best < 1600:
                best_model.summary()
                best_model.save(f'model_{best}.h5')


d = read_data()
# local_search(1800, d)

test_neural_network(d[28:])

# [1,2,3,4,5] = [[1, 2], [2, 3], [3, 4], [4,5]]
