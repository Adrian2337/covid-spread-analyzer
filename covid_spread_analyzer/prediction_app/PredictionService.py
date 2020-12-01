from covid_spread_analyzer.prediction_app.predictioner import Predictioner


class PredictionService:

    predictioner = None

    @staticmethod
    def initialize():
        PredictionService.predictioner = Predictioner()

    @staticmethod
    def get_predictioner():
        return PredictionService.predictioner
