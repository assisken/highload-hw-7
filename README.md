# Лабораторная работа №1/2 по Highload

## О сервисе
Наприсан на Python / Flask, можно поднять через докер.

## Установка и запуск
```bash
$ docker build -t highload .
$ docker run -e API_KEY="<api key>" -p 8000:8000 --rm -it highload
```

## API

### `/v1/forecast/`
Показывает погоду в заданном городе в заданном времени.

#### Аргументы
city `str` — название города на английском,

dt `str` — время в формате ISO.  

#### Пример
```bash
$ curl "http://localhost:8000/v1/forecast/?city=Moscow&dt=2020-10-02T00:00:00"
{"city":"Moscow","temperature":100.500,"unit":"celsius"}
```

### `/v1/current/`
Показывает погоду на текущее время в заданном городе.

#### Аргументы
city `str` — название города на английском,

#### Пример
```bash
$ curl "http://localhost:8000/v1/current/?city=Moscow"
{"city":"Moscow","temperature":100.500,"unit":"celsius"}
```
