from parse import search
from data_fetch.twitter.InfoBundle import InfoBundle
from data_fetch.twitter.NumberParser import NumberParser
from data_fetch.twitter.DataPack import DataPack

flag = None


class DataMiner:

    voivodeships = [
        "dolnośląskie",
        "kujawsko-pomorskie",
        "lubelskie",
        "lubuskie",
        "łódzkie",
        "małopolskie",
        "mazowieckie",
        "opolskie",
        "podkarpackie",
        "podlaskie",
        "pomorskie",
        "śląskie",
        "świętokrzyskie",
        "warmińsko-mazurskie",
        "wielkopolskie",
        "zachodniopomorskie"
    ]

    patterns = {
        "daily_cases": "Mamy {cases} now{suffix} i potwierdzon{suffix} przypad",
        "daily_deaths_direct": "Z powodu COVID-19 zmarł{suffix} {deaths} os",
        "daily_deaths_linked": "z powodu współistnienia COVID-19 z innymi schorzeniami zmarł{suffix} {deaths} os",
        "daily_tests": "W ciągu doby wykonano ponad {} testów",
        "total_cases": "Liczba zakażonych koronawirusem: {}/",
        "total_deaths": "/{} (wszystkie pozytywne przypadki/w tym osoby zmarłe)."
    }

    @staticmethod
    def prepare_data_pack(info_bundle: InfoBundle) -> DataPack:
        date = info_bundle.date
        daily_cases = NumberParser.int_with_space(search(DataMiner.patterns["daily_cases"], info_bundle.text)["cases"])
        daily_deaths = NumberParser.int_with_space(
            search(DataMiner.patterns["daily_deaths_direct"], info_bundle.text)["deaths"]) + \
            NumberParser.int_with_space(
            search(DataMiner.patterns["daily_deaths_linked"], info_bundle.text)["deaths"])
        daily_tests = NumberParser.int_with_modifier(search(DataMiner.patterns["daily_tests"], info_bundle.text)[0])
        total_cases = NumberParser.int_with_space(search(DataMiner.patterns["total_cases"], info_bundle.text)[0])
        total_deaths = NumberParser.int_with_space(search(DataMiner.patterns["total_cases"], info_bundle.text)[0])

        voivodeship_stats = {}
        for v in DataMiner.voivodeships:
            v_cases = 0
            v_match = search(v + "go ({})", info_bundle.text)
            if v_match:
                v_cases = v_match[0]
            voivodeship_stats[v.capitalize()] = {
                "date": date,

                "daily infected": NumberParser.int_with_space(v_cases),
                "daily cured": flag,
                "daily deceased": flag,

                "total infected": flag,
                "total cured": flag,
                "total deceased": flag,

                "infected now": flag,
                "occupied respirators": flag,
                "free respirators": flag,

                "infections 7d100k": flag,
                "deaths 7d100k": flag,
                "infected now 100k": flag
            }

        return DataPack(date, daily_cases, daily_deaths, daily_tests, total_cases, total_deaths, voivodeship_stats)
