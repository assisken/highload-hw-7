# Лабораторная работа №7 по Highload

## Установка и запуск
```bash
docker-compose up
```

## Полезные скрипты

Записать кучу данных на редисы:

```bash
for TIME in {0..59}; do curl -X POST "http://127.0.0.1/v1/forecast/" -H  "accept: application/json" -H  "Content-Type: application/json" -d "{\"city\": \"Moscow\", \"timestamp\": \"2020-11-27T00:$TIME:00Z\", \"temperature\": 12}"; done
```

Скан ключей на редисах:

```bash
for PORT in {7001..7006}; do print "$PORT: "; echo keys \* | redis-cli -p "$PORT"; echo; done
``` 

Уронить редис:

```bash
docker stop redis-2
```
