FROM redis:5.0

ARG PORT_CONFIG

COPY redis.conf /usr/local/etc/redis/redis.conf

RUN sed -i "s/7000/${PORT_CONFIG}/g" "/usr/local/etc/redis/redis.conf"

CMD ["redis-server", "/usr/local/etc/redis/redis.conf"]
