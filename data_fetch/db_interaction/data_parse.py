import stored_data
import parse
from datetime import datetime, timedelta


def __retrieve(pattern: str, text: str):
    return parse.search(pattern, text)[0]


def __gen_dates(start_date, end_date=None):
    if not end_date:
        end_date = datetime.now()
    else:
        end_date = datetime.fromisoformat(end_date)
    start_date = datetime.fromisoformat(start_date)
    for date in [
        (start_date + timedelta(days=x)).strftime("%Y-%m-%d") for x in range(0, (end_date - start_date).days + 1)
    ]:
        yield date


def parse_all(region_name, site_text):
    data = dict()
    for date in __gen_dates("2020-03-01"):
        data[date] = dict()

    if region_name == "Poland":
        region_type = "Poland"
    else:
        region_type = "Voivodeships"

    _parse_general(data, region_type, site_text)
    _derivate_additional(data, region_name)
    _derivate_additional2(data, region_name)

    return data


def _parse_general(data, region_type, site_text):
    for group_name in stored_data.patterns[region_type].keys():
        group_patterns = stored_data.patterns[region_type][group_name]
        _parse_group(data, group_patterns, site_text)


def _parse_group(data, group_patterns, site_text):
    group_text = __retrieve(group_patterns["general"], site_text)
    for doc in group_text.split(",{"):
        date = __retrieve(group_patterns["date"], doc).replace(".", "-")
        date = date[6:] + "-" + date[3:5] + "-" + date[:2]
        for entry, pattern in group_patterns["data entries"].items():
            val = __retrieve(pattern, doc)
            data[date][entry] = int(val) if val != "null" else None


def _derivate_additional(data, region_name):
    for d in data.keys():
        if region_name == "Poland":
            try:
                data[d]["test positivity ratio"] = data[d]["daily infected"] / data[d]["daily tests"]
            except (KeyError, ZeroDivisionError, TypeError):
                data[d]["test-positivity ratio"] = None

        try:
            data[d]["infected now per 100k"] = data[d]["infected now"] / stored_data.population[region_name] * 100_000
        except (KeyError, TypeError):
            data[d]["infected now per 100k"] = None

        try:
            data[d]["total infected per 100k"] = data[d]["total infected"] / stored_data.population[region_name] \
                                                 * 100_000
        except (KeyError, TypeError):
            data[d]["total infected per 100k"] = None

        try:
            data[d]["deaths per 100k infected"] = data[d]["daily deceased"] / data[d]["daily infected"] * 100_000
        except (KeyError, ZeroDivisionError, TypeError):
            data[d]["deaths per 100k infected"] = None

        try:
            data[d]["infected delta"] = data[d]["daily infected"] - data[d]["daily cured"]
        except (KeyError, TypeError):
            data[d]["infected delta"] = None

        try:
            data[d]["infections per 100k"] = data[d]["daily infected"] / stored_data.population[region_name] * 100_000
        except (KeyError, TypeError):
            data[d]["infections per 100k"] = None


def _derivate_additional2(data, region_name):
    dates = list(__gen_dates("2020-03-01"))
    first_info = 0
    while "daily infected" not in data[dates[first_info]].keys():
        first_info += 1

    for i in range(first_info, len(dates)):
        if i - first_info >= 6:
            try:
                data[dates[i]]["infections per 100k week avg"] = sum(
                    [data[x]["daily infected"] for x in dates[i - 6: i + 1]]
                ) / 7 / stored_data.population[region_name] * 100_000
            except (KeyError, TypeError):
                data[dates[i]]["infections per 100k week avg"] = None
        else:
            try:
                data[dates[i]]["infections per 100k week avg"] = sum(
                    [data[x]["daily infected"] for x in dates[: i + 1]]
                ) / (i + 1) / stored_data.population[region_name] * 100_000
            except (KeyError, TypeError):
                data[dates[i]]["infections per 100k week avg"] = None
