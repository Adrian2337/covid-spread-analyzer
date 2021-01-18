## 2021-01-17-20:48:39
- Update failed in: 
```python
Traceback (most recent call last):
  File "/home/mateusz/Dokumenty/team-programming-project/manage.py", line 36, in main
    UpdateService.start()
  File "/home/mateusz/Dokumenty/team-programming-project/covid_spread_analyzer/UpdateService.py", line 17, in start
    DBUpdateService.update_database()
  File "/home/mateusz/Dokumenty/team-programming-project/covid_spread_analyzer/DBUpdateService.py", line 10, in update_database
    data = DataYieldService.yield_data_since(last_update_date)
  File "/home/mateusz/Dokumenty/team-programming-project/data_fetch/twitter/DataYieldService.py", line 23, in yield_data_since
    return DataYieldService.covid_data_yielder.yield_data(date, last_relevant_date, include_first_day)
  File "/home/mateusz/Dokumenty/team-programming-project/data_fetch/twitter/CovidDataYielder.py", line 22, in yield_data
    data_pack = DataMiner.prepare_data_pack(b)
  File "/home/mateusz/Dokumenty/team-programming-project/data_fetch/twitter/DataMiner.py", line 49, in prepare_data_pack
    total_deaths = NumberParser.int_with_space(search(DataMiner.patterns["total_deaths"], info_bundle.text)[0])
  File "/home/mateusz/Dokumenty/team-programming-project/data_fetch/twitter/NumberParser.py", line 5, in int_with_space
    return int(no.replace(" ", ""))
ValueError: invalid literal for int() with base 10: '/t.co/JSvXiQgyhU,prezentującejcodzienneraportyzakażeńodpoziomudanychogólnopolskichdopoziomudanychpowiatowych.📊Wciągudobywykonanoponad78,7tys.testówna#koronawirus.https://t.co/lUk9KpS0BXRT@szczepimysi

```

## 2021-01-17-14:14:23
- Update failed in: 
```python
Traceback (most recent call last):
  File "/home/piotr/Documents/studies/covid_spread_analyzer/manage.py", line 36, in main
    UpdateService.start()
  File "/home/piotr/Documents/studies/covid_spread_analyzer/covid_spread_analyzer/UpdateService.py", line 17, in start
    DBUpdateService.update_database()
  File "/home/piotr/Documents/studies/covid_spread_analyzer/covid_spread_analyzer/DBUpdateService.py", line 10, in update_database
    data = DataYieldService.yield_data_since(last_update_date)
  File "/home/piotr/Documents/studies/covid_spread_analyzer/data_fetch/twitter/DataYieldService.py", line 23, in yield_data_since
    return DataYieldService.covid_data_yielder.yield_data(date, last_relevant_date, include_first_day)
  File "/home/piotr/Documents/studies/covid_spread_analyzer/data_fetch/twitter/CovidDataYielder.py", line 22, in yield_data
    data_pack = DataMiner.prepare_data_pack(b)
  File "/home/piotr/Documents/studies/covid_spread_analyzer/data_fetch/twitter/DataMiner.py", line 49, in prepare_data_pack
    total_deaths = NumberParser.int_with_space(search(DataMiner.patterns["total_deaths"], info_bundle.text)[0])
  File "/home/piotr/Documents/studies/covid_spread_analyzer/data_fetch/twitter/NumberParser.py", line 5, in int_with_space
    return int(no.replace(" ", ""))
ValueError: invalid literal for int() with base 10: '/t.co/JSvXiQgyhU,prezentującejcodzienneraportyzakażeńodpoziomudanychogólnopolskichdopoziomudanychpowiatowych.📊Wciągudobywykonanoponad78,7tys.testówna#koronawirus.https://t.co/lUk9KpS0BXRT@szczepimysi

```

## 2021-01-17-14:13:49
- Update failed in: 
```python
Traceback (most recent call last):
  File "/home/piotr/Documents/studies/covid_spread_analyzer/manage.py", line 36, in main
    UpdateService.start()
  File "/home/piotr/Documents/studies/covid_spread_analyzer/covid_spread_analyzer/UpdateService.py", line 17, in start
    DBUpdateService.update_database()
  File "/home/piotr/Documents/studies/covid_spread_analyzer/covid_spread_analyzer/DBUpdateService.py", line 10, in update_database
    data = DataYieldService.yield_data_since(last_update_date)
  File "/home/piotr/Documents/studies/covid_spread_analyzer/data_fetch/twitter/DataYieldService.py", line 23, in yield_data_since
    return DataYieldService.covid_data_yielder.yield_data(date, last_relevant_date, include_first_day)
  File "/home/piotr/Documents/studies/covid_spread_analyzer/data_fetch/twitter/CovidDataYielder.py", line 22, in yield_data
    data_pack = DataMiner.prepare_data_pack(b)
  File "/home/piotr/Documents/studies/covid_spread_analyzer/data_fetch/twitter/DataMiner.py", line 49, in prepare_data_pack
    total_deaths = NumberParser.int_with_space(search(DataMiner.patterns["total_deaths"], info_bundle.text)[0])
  File "/home/piotr/Documents/studies/covid_spread_analyzer/data_fetch/twitter/NumberParser.py", line 5, in int_with_space
    return int(no.replace(" ", ""))
ValueError: invalid literal for int() with base 10: '/t.co/JSvXiQgyhU,prezentującejcodzienneraportyzakażeńodpoziomudanychogólnopolskichdopoziomudanychpowiatowych.📊Wciągudobywykonanoponad78,7tys.testówna#koronawirus.https://t.co/lUk9KpS0BXRT@szczepimysi

```













