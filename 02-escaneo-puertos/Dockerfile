FROM alpine:latest

RUN apk add --no-cache netcat-openbsd python3 bind-tools

WORKDIR /app

COPY entrypoint.sh /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh

EXPOSE 8080

ENTRYPOINT ["/app/entrypoint.sh"]
