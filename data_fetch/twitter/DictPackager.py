class DictPackager:

    @staticmethod
    def prepare_dicts(data_packs: list):
        data = dict()
        data["Last Update Date"] = data_packs[-1].date

        data["Map Data"] = dict()
        for dp in data_packs:
            simpler_voivodeships = dict()
            for voivodeship, data_v in dp.voivodeship_stats.items():
                simpler_voivodeships[voivodeship] = {
                    "daily infected": data_v["daily infected"],
                }

            data["Map Data"][dp.date] = {
                "date": dp.date,
                "daily infected": dp.daily_cases,
                "daily deceased": dp.daily_deaths,
                "Voivodeships": simpler_voivodeships
            }

        data["Poland"] = dict()
        for dp in data_packs:
            data["Poland"][dp.date] = {
                "date": dp.date,

                "daily infected": dp.daily_cases,
                "daily deceased": dp.daily_deaths,
                "daily tests": dp.daily_tests,

                "total infected": dp.total_cases,
                "total deceased": dp.total_deaths,

                "positive tests percent": dp.daily_cases / dp.daily_tests
            }

        data["Voivodeships"] = dict()
        for voivodeship in data_packs[0].voivodeship_stats.keys():
            data["Voivodeships"][voivodeship] = dict()
            for dp in data_packs:
                data["Voivodeships"][voivodeship][dp.date] = dp.voivodeship_stats[voivodeship]

        return data
