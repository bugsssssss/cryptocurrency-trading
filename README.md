Это руководство описывает основные функции Криптовалютного вычислителя, включая чтение данных о сделках из CSV-файла, агрегацию сделок в свечи (candlesticks) и расчет экспоненциально взвешенного среднего (EMA).

## Чтение данных о сделках из CSV
Для того чтобы прочитать данные о сделках из CSV-файла, используйте функцию `read_trades_csv`. Передайте путь к файлу в качестве аргумента.

## Агрегация сделок в свечи (Candlesticks)

Функция `aggregate_into_candlesticks`  агрегирует сделки в свечи с заданным временным интервалом.


## Расчет EMA (Экспоненциально Взвешенное Среднее)

Функция `calculate_ema` рассчитывает EMA с заданной длиной.

## Запуск тестов

Чтобы убедиться, что функции работают корректно, запустите тесты из файла `tests.py`.

```bash
python tests.py
```

Убедитесь, что у вас установлены библиотеки `pandas` и `numpy`. 

## P.S 

Написал readme на русском хоть таск и был на англ. Честно скажу не очень разбираюсь в крипте, но эти почти 32 часа своей жизни я посвятил изучению основ, прощу взять этот факт во внимание, если не правильно понял задание. 
