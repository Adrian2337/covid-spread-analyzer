import site_fetch
import data_parse
from datetime import datetime
import stored_data


def prepare_new_data(start_date, end_date=datetime.now().strftime("%Y-%m-%d")):
    sites = site_fetch.fetch_all()
    data = prepare_all_data(sites)
    formatted_data = format_data(data, start_date, end_date)
    return formatted_data


def prepare_all_data(sites):
    data = {
        "Poland": data_parse.parse_all("Poland", sites["Poland"]),
        "Voivodeships": dict()
    }
    for v_name, v_proper_name in stored_data.v_names.items():
        data["Voivodeships"][v_proper_name] = data_parse.parse_all(v_proper_name, sites["Voivodeships"][v_name])

    return data


def format_data(data, start_date, end_date):
    final_data = {
        "Map Data": dict(),
        "Poland": dict(),
        "Voivodeships": dict()
    }

    for v in stored_data.v_names.values():
        final_data["Voivodeships"][v] = dict()

    for date in data["Poland"].keys():
        if start_date <= date <= end_date:
            final_data["Map Data"][date] = {
                "date": date,
                "daily infected": __retrieve_value(data["Poland"][date], "daily infected"),
                "daily cured": __retrieve_value(data["Poland"][date], "daily cured"),
                "daily deceased": __retrieve_value(data["Poland"][date], "daily deceased")
            }

            final_data["Map Data"][date]["Voivodeships"] = dict()
            for v in stored_data.v_names.values():
                final_data["Map Data"][date]["Voivodeships"][v] = {
                    "daily infected": __retrieve_value(data["Voivodeships"][v][date], "daily infected"),
                    "daily cured": __retrieve_value(data["Voivodeships"][v][date], "daily cured"),
                    "daily deceased": __retrieve_value(data["Voivodeships"][v][date], "daily deceased")
                }

            final_data["Poland"][date] = data["Poland"][date]

            for v in stored_data.v_names.values():
                final_data["Voivodeships"][v][date] = data["Voivodeships"][v][date]
        elif date > end_date:
            break

    return final_data


def __retrieve_value(source, name):
    return source[name] if name in source.keys() else None
