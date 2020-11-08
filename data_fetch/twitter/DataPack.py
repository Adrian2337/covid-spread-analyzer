class DataPack:

    def __init__(self, date, daily_cases, daily_deaths, daily_tests, total_cases, total_deaths, voivodeship_stats):
        self.date = date
        self.daily_cases = daily_cases
        self.daily_deaths = daily_deaths
        self.daily_tests = daily_tests
        self.total_cases = total_cases
        self.total_deaths = total_deaths
        self.voivodeship_stats = voivodeship_stats
