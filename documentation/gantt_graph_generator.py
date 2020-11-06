import random

import plotly
import plotly.express as px
import plotly.figure_factory as ff
import pandas as pd


def add_days(date, days):
    return pd.to_datetime(date) + pd.DateOffset(days=days)


colors = {'Major': 'rgb(255, 0, 0)',
          'Minor': 'rgb(34,139,34)'}

s = (
    "Połączenie serwera z bazą danych( firebase).\item Zaprogramowanie systemu wywołującego odpowiednie zapytania do "
    "API twittera w celu pozyskania danych.\item Parsowanie danych do odpowiedniego formatu.\item Zapisanie "
    "przkształconych danych w bazie online( firebase).\item Przygotowanie systemu do aktualizacji bazy danych( "
    "firebase).\item Funkcjonalności odpowiadjące za komunikację bazy danych( firebase) save, load.\item Utworzenie "
    "responsywnej mapy reagującej na na przykład najechania lub kliknięcia.\item Utworzenie strony głównej i "
    "integracja  responsywnej mapy.\item Wyznaczenie przyjaznego dla oka przedziału kolorów odpowiadającemu ilości "
    "zarażeń.\item Zaprojektowanie układu i struktury strony głównej i odpowiadającej za statystyki.\item Utworzenie "
    "funkcjonalności do generowania wykresów.\item Zaprojektowanie sieci neuronowej rozwiązującej problemy "
    "eksploracyjne.\item Zaimplementowanie funkcjonalności predykcji danych wykorzytując wyżej wymienioną NN.\item "
    "Analiza danych i wytypowanie atrybutów, które w postaci grafu przekazujących największą ilość informacji. \item "
    "Implementacja widoków renderujących odpowiednie strony.\item Obsługa błędów( wejście pod nieodpowiedni link, "
    "...)\item Testy jednostkowe\item Integracja wszystkich osobno powstałych komponentów w jedną spójną całość\item "
    "Stworzenie funkcjonalności odpowiadającej wyświetleniu się danych ogólnych po kliknięciu w dane "
    "województwo.\item Zaimplementowanie możliwości manualnej manipulacji, edycji danymi w bazie danych.\item "
    "Stworzenie i zaprojektowanie bazy danych( struktura przechowywanych danych).\item Utworzenie dokumentacji.")
labels = s.split('\item')
days = [1, 4, 3, 1, 3, 1, 5, 3, 1, 6, 3, 5, 3, 1, 2, 2, 3, 1, 1, 3, 3, 2]
start_dates = dict({1: "2020-11-23", 2: "2020-11-24", 3: "2020-11-28", 4: "2020-12-01", 5: "2020-12-02",
                    6: "2020-12-01", 7: "2020-11-23", 8: "2020-12-02", 9: "2020-11-28", 10: "2020-12-03",
                    11: "2020-12-02", 12: "2020-12-02", 13: "2020-12-07", 14: "2020-12-02", 15: "2020-12-07",
                    16: "2020-12-09", 17: "2020-12-11", 18: "2020-12-06", 19: "2020-12-05", 20: "2020-12-02",
                    21: "2020-11-23", 22: "2020-12-12"})

imp = [1, 2, 3, 4, 6, 7, 10, 12, 14, 18, 20, 21]

df = [dict(Task=t, Start=start_dates[i + 1], Finish=pd.to_datetime(start_dates[i + 1]) + pd.DateOffset(d),
           Resource='Major' if i + 1 in imp else 'Minor') for i, (t, d) in enumerate(zip(labels, days))]
fig = ff.create_gantt(df, colors=colors, index_col='Resource', show_colorbar=True,
                      group_tasks=True)

plotly.offline.plot(fig, filename='gantt.html')
