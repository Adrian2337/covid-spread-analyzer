from numpy.ma import arange, asarray

from covid_spread_analyzer.prediction_app.predictioner import Predictioner
import re
from sklearn.model_selection import train_test_split


def read_data(file='temp.txt'):
    with open(file) as f:
        txt = f.read()
        matches = re.findall(r': \d+', txt)
        return [int(re.sub(': ', '', x)) for x in matches]


def test_neural_network(data):
    y = asarray(data)
    x = arange(len(data))
    y_train, y_test, x_train, x_test = train_test_split(y, x, test_size=0.33)
    guesser = Predictioner()
    guesser.update_input(train_x=x_train, train_y=y_train)
    history = guesser.fit_model(verbose=0)
    eva = guesser.evaluate(y_test, x_test)
    guesser.predict(x)
    guesser.visualize()
    print(eva, history)


d = read_data()
test_neural_network(d)
