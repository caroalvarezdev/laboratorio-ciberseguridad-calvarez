
FROM alpine:latest

RUN apk add --no-cache python3

WORKDIR /app

# Dependencia de prueba inofensiva
RUN echo '#!/bin/sh' > /app/malicious_dependency.sh \
    && echo 'echo "[SIMULACIÓN] Dependencia de prueba detectada."' >> /app/malicious_dependency.sh \
    && chmod +x /app/malicious_dependency.sh

COPY entrypoint.sh /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh

EXPOSE 8080

ENTRYPOINT ["/app/entrypoint.sh"]
