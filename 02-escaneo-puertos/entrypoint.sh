#!/bin/sh

HOST="laboratorio-ciberseguridad-calvarez.onrender.com"

echo "=== INICIANDO ESCANEO DE PUERTOS Y RECONOCIMIENTO EN LA DMZ ==="
echo "Analizando puertos comunes sobre $HOST..."

for port in 21 22 80 443 8080 3306; do
  nc -zv -w 2 $HOST $port 2>&1
done

echo "=== ESCANEO DE PUERTOS FINALIZADO ==="

python3 -m http.server 8080
