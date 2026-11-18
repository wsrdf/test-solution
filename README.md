# Скрипт для измерения скорости интернета

Консольный скрипт для измерения скорости интернета путём выполнения последовательных загрузок файла.

## Использование с помощью bash-скрипта 

```bash
./run.sh <url>
./run.sh https://dn710100.ca.archive.org/0/items/kendrick-lamar-damn_202411/1-booklet%2001.jpg
```

### Параметры

- `url` — адрес файла для скачивания
  - Примеры: `https://example.com/image.jpg`, `example.com/file.zip`

## Вывод

Скрипт выводит:
1. URL тестирования
2. Количество запросов
3. Общий объём загруженных данных
4. Общее время всех запросов
5. Среднее время одного запроса
6. Средний размер ответа
7. **Итоговая скорость загрузки в выбранных единицах**

### Пример вывода

```bash
$ test % ./run.sh https://dn710100.ca.archive.org/0/items/kendrick-lamar-damn_202411/1-booklet%2001.jpg

Testing URL: https://dn710100.ca.archive.org/0/items/kendrick-lamar-damn_202411/1-booklet%2001.jpg
Making 10 sequential requests...

Request 1: 4.049s (3.29 MiB)
Request 2: 5.335s (3.29 MiB)
Request 3: 5.362s (3.29 MiB)
Request 4: 8.811s (3.29 MiB)
Request 5: 6.720s (3.29 MiB)
Request 6: 6.088s (3.29 MiB)
Request 7: 4.139s (3.29 MiB)
Request 8: 3.805s (3.29 MiB)
Request 9: 4.580s (3.29 MiB)
Request 10: 3.288s (3.29 MiB)

============================================================
SPEED TEST RESULTS
============================================================
URL: https://dn710100.ca.archive.org/0/items/kendrick-lamar-damn_202411/1-booklet%2001.jpg
Number of requests: 10
Total data downloaded: 32.94 MiB
Total time: 52.177 seconds
Average request time: 5.218 seconds
Average download size: 3.29 MiB
------------------------------------------------------------
Download speed: 646.53 KiB/s
============================================================
```

## Требования

- Python 3.6+
- Библиотека `requests`
