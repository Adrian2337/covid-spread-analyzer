population = {
    "Dolnośląskie": 2_898_525,
    "Kujawsko-pomorskie": 2_069_273,
    "Lubelskie": 2_103_342,
    "Lubuskie": 1_010_177,
    "Łódzkie": 2_448_713,
    "Małopolskie": 3_413_931,
    "Mazowieckie": 5_428_031,
    "Opolskie": 980_771,
    "Podkarpackie": 2_125_901,
    "Podlaskie": 1_176_576,
    "Pomorskie": 2_346_717,
    "Śląskie": 4_508_078,
    "Świętokrzyskie": 1_230_044,
    "Warmińsko-mazurskie": 1_420_514,
    "Wielkopolskie": 3_500_361,
    "Zachodniopomorskie": 1_693_219
}
population["Poland"] = sum(population.values())

v_names = {
    "dolnoslaskie": "Dolnośląskie",
    "kujawsko-pomorskie": "Kujawsko-pomorskie",
    "lubelskie": "Lubelskie",
    "lubuskie": "Lubuskie",
    "lodzkie": "Łódzkie",
    "malopolskie": "Małopolskie",
    "mazowieckie": "Mazowieckie",
    "opolskie": "Opolskie",
    "podkarpackie": "Podkarpackie",
    "podlaskie": "Podlaskie",
    "pomorskie": "Pomorskie",
    "slaskie": "Śląskie",
    "swietokrzyskie": "Świętokrzyskie",
    "warminsko-mazurskie": "Warmińsko-mazurskie",
    "wielkopolskie": "Wielkopolskie",
    "zachodniopomorskie": "Zachodniopomorskie"
}

patterns = {
    "Poland": {
        "total_data": {
            "general": "var dataSource_przyrost = [\n\t{}];",
            "date": "country: \"{}\"",
            "data entries": {
                "total infected": ",zar: {},",
                "total cured": ",wyl: {}}",
                "total deceased": ",zgo: {},",
                "infected now": ",chor: {},"
            }
        },
        "delta_data": {
            "general": "var populationData = [\n\t{}];",
            "date": "arg: \"{}\"",
            "data entries": {
                "daily infected": ",p_chorzy: {},",
                "daily cured": ",p_wyleczeni: {},",
                "daily deceased": ",p_zgony: {},"
            }
        },
        "respirators_data": {
            "general": "var respiratoryData = [\n\t{}];",
            "date": "arg: \"{}\"",
            "data entries": {
                "occupied respirators": ",respiratory: {},",
                "free respirators": ",l_respiratory: {},"
            }
        },
        "tests_total_data": {
            "general": "var dataSource_testy = [\n\t{}];",
            "date": " dzien: \"{}\"",
            "data entries": {
                "total tests": ", testy: {},"
            }
        },
        "tests_delta_data": {
            "general": "var Data_przyrost_testy = [\n\t{}];",
            "date": "arg: \"{}\"",
            "data entries": {
                "daily tests": ",p_testy: {},"
            }
        }
    },
    "Voivodeships": {
        "total_data": {
            "general": "var dataSource_koronawirus = [\n\t{}];",
            "date": "dzien: \"{}\"",
            "data entries": {
                "total infected": ",woj_zar: {},",
                # "total cured": ",woj_wyl: {},",
                "total deceased": ",woj_zgo: {},",
                "infected now": ",woj_chor: {},"
            }
        },
        "delta_data": {
            "general": "var populationData = [\n\t{}];",
            "date": "arg: \"{}\"",
            "data entries": {
                "daily infected": ",p_chorzy: {},",
                # "daily cured": ",p_wyleczeni: {},",
                "daily deceased": ",p_zgony: {},"
            }
        },
        "respirators_data": {
            "general": "var respiratoryData = [\n\t{}];",
            "date": "arg: \"{}\"",
            "data entries": {
                "occupied respirators": ",respiratory: {},",
                "free respirators": ",l_respiratory: {},"
            }
        }
    }
}

base_url = "https://koronawirusunas.pl/"
