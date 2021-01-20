import re

import numpy
from matplotlib import pyplot
from sklearn.preprocessing import MinMaxScaler
from tensorflow import keras
from tensorflow.python.framework.random_seed import set_seed
from tensorflow.python.keras import Sequential
from tensorflow.python.keras.layers import Dense, Dropout


def reshaper(x, val):
    return x.reshape((len(x), val))


class Predictioner:
    numpy.random.seed(1234)
    set_seed(1234)

    def __init__(self):
        self.model = Sequential()
        self.setup_default_model()
        self.compile_model()

    def save_model(self, path):
        self.model.save(path)

    def load_model(self, path):
        self.model = keras.models.load_model(path)

    def update_input(self, train_x, train_y):
        self.push_train_sets(train_x, train_y)
        self.y_scaler = MinMaxScaler()
        self.x_scaler = MinMaxScaler()
        self.reshape_train_sets()
        self.adjust_scalers()

    def push_train_sets(self, train_x, train_y):
        self.train_x = train_x
        self.train_y = train_y

    def reshape_train_sets(self):
        self.train_x = reshaper(self.train_x, self.train_x.shape[1])
        self.train_y = reshaper(self.train_y, 1)

    def adjust_scalers(self):
        self.train_x = self.x_scaler.fit_transform(self.train_x)
        self.train_y = self.y_scaler.fit_transform(self.train_y)

    def setup_default_model(self):
        self.model.add(Dense(30))
        self.model.add(Dense(90, activation='relu'))
        self.model.add(Dense(45, activation='relu'))
        self.model.add(Dense(20, activation='relu'))
        self.model.add(Dense(10, activation='relu'))
        self.model.add(Dense(1))

    def compile_model(self):
        self.model.compile(
            optimizer=keras.optimizers.Adam(),
            loss=keras.losses.mean_squared_error,
            metrics=[
                keras.metrics.mean_squared_error,
                keras.metrics.mean_squared_logarithmic_error,
                keras.metrics.mean_absolute_percentage_error,
                keras.metrics.mean_absolute_error,
            ]
        )

    def fit_model(self, verbose=0):
        self.model.fit(
            self.train_x,  # [:int(len(self.train_x) * 0.66)],
            self.train_y,  # [:int(len(self.train_y) * 0.66)],
            epochs=300,
            batch_size=10,
            verbose=verbose,
            # validation_data=(self.train_y[int(len(self.train_x) * 0.66):],
            #                 self.train_x[int(len(self.train_x) * 0.66):])
        )

    def evaluate(self, x_test, y_test):
        return self.model.evaluate(x_test, y_test, batch_size=12, verbose=1)

    def predict(self, prediction_interval_x):
        prediction_interval_x = self.x_scaler.transform(prediction_interval_x)
        predicted_y = self.model.predict(prediction_interval_x)

        self.x_plot = self.x_scaler.inverse_transform(self.train_x)
        self.y_plot = self.y_scaler.inverse_transform(self.train_y)
        self.x_pred_plot = self.x_scaler.inverse_transform(prediction_interval_x)
        self.y_pred_plot = self.y_scaler.inverse_transform(predicted_y)
        return self.y_pred_plot

    def visualize(self):
        pyplot.scatter(self.x_pred_plot, self.y_pred_plot, label='Predicted')
        pyplot.scatter(self.x_plot, self.y_plot, label='Actual')
        pyplot.title('Input (x) versus Output (y)')
        pyplot.xlabel('Input Variable (x)')
        pyplot.ylabel('Output Variable (y)')
        pyplot.legend()
        pyplot.show()


def convert_to_learning_set(array):
    x_vector = []
    y_vector = []
    for x in range(30, len(array)):
        x_vector.append(array[x - 30:x])
        y_vector.append(array[x])
    x_train = numpy.array(x_vector)
    y_train = numpy.array(y_vector)
    return x_train, y_train


def get_prediction_set(arr):
    rs = []
    for x in range(30, len(arr)+1):
        rs.append(arr[x - 30:x])
    rs = numpy.asarray(rs)
    return rs



##### Old one
#
# class OldPredictioner:
#     numpy.random.seed(1234)
#     set_seed(1234)
#
#     def __init__(self, model_input=None):
#         self.model = model_input
#         if model_input is None:
#             self.model = Sequential()
#             self.setup_default_model()
#         self.compile_model()
#
#     def save_model(self, path):
#         self.model.save(path)
#
#     def load_model(self, path):
#         self.model = keras.models.load_model(path)
#
#     def update_input(self, train_x, train_y):
#         self.push_train_sets(train_x, train_y)
#         self.y_scaler = MinMaxScaler()
#         self.x_scaler = MinMaxScaler()
#         self.reshape_train_sets()
#         self.adjust_scalers()
#
#     def push_train_sets(self, train_x, train_y):
#         self.train_x = train_x
#         self.train_y = train_y
#
#     def reshape_train_sets(self):
#         self.train_x = reshaper(self.train_x)
#         self.train_y = reshaper(self.train_y)
#
#     def adjust_scalers(self):
#         self.train_x = self.x_scaler.fit_transform(self.train_x)
#         self.train_y = self.y_scaler.fit_transform(self.train_y)
#
#     def setup_default_model(self):
#         self.model.add(Dense(1))
#         self.model.add(Dense(90, activation='relu'))
#         self.model.add(Dense(45, activation='relu'))
#         self.model.add(Dense(20, activation='relu'))
#         self.model.add(Dense(10, activation='relu'))
#         self.model.add(Dense(1))
