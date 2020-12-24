# Лабораторная работа №7 по Highload

## Установка и запуск кластера

```bash
docker-compose up
```

Чтобы объединить редисы в кластер:

```bash
docker exec -it redis-1 redis-cli --cluster create 127.0.0.1:7001 127.0.0.1:7002 127.0.0.1:7003 127.0.0.1:7004 127.0.0.1:7005 127.0.0.1:7006 --cluster-replicas 1 --verbose
```

Далее записываем кучу данных на редисы:

```bash
for TIME in {0..29}; do curl -X POST "http://127.0.0.1/v1/forecast/" -H  "accept: application/json" -H  "Content-Type: application/json" -d "{\"city\": \"Moscow\", \"timestamp\": \"2020-11-27T00:$TIME:00Z\", \"temperature\": 12}"; done
```

Просканим ключи на всех редисах:

```bash
for PORT in {7001..7006}; do print "$PORT: "; echo keys \* | redis-cli -p "$PORT"; echo; done
``` 

Заметим, что на любых двух редисах одинаковые данные.

Попробуем уронить редис:

```bash
docker stop redis-2
```

Проверим, что он пропал:

```bash
for PORT in {7001..7006}; do print "$PORT: "; echo keys \* | redis-cli -p "$PORT"; echo; done
``` 

Ещё кучу данных напишем в редисы, чтобы проверить, как вновь поднятый редис догонит.

```bash
for TIME in {30..59}; do curl -X POST "http://127.0.0.1/v1/forecast/" -H  "accept: application/json" -H  "Content-Type: application/json" -d "{\"city\": \"Moscow\", \"timestamp\": \"2020-11-27T00:$TIME:00Z\", \"temperature\": 12}"; done
```

Посмотрим, как записалось:

```bash
for PORT in {7001..7006}; do print "$PORT: "; echo keys \* | redis-cli -p "$PORT"; echo; done
``` 

Подымим упавший редис:

```bash
docker-compose up -d redis-2
```

Посмотрим, как догнал:

```bash
for PORT in {7001..7006}; do print "$PORT: "; echo keys \* | redis-cli -p "$PORT"; echo; done
``` 

Всё!
