# from covid_spread_analyzer.prediction_app.predictioner import Predictioner
import re
from sklearn.model_selection import train_test_split


def read_data(file='temp.txt'):
    with open(file) as f:
        txt = f.read()
        matches = re.findall(r': \d+', txt)
        return [int(re.sub(': ', '', x)) for x in matches]


def test_neural_network(data):
    y = data
    x = range(len(data))
    y_train, y_test, x_train, x_test = train_test_split(y, x, test_size=0.33, shuffle=False)
    print(x_train)
    print(x_test)
    print(y_train)
    print(y_test)


test_neural_network(read_data())
