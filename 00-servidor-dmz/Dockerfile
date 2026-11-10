
FROM alpine:latest

RUN apk add --no-cache python3

COPY entrypoint.sh /entrypoint.sh

RUN chmod +x /entrypoint.sh

WORKDIR /app

EXPOSE 8080

ENTRYPOINT ["/entrypoint.sh"]
