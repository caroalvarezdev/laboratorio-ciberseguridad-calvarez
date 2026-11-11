#!/bin/sh

DATOS_SENSIBLES="dato_prueba_ciberseguridad_2026"
DATOS_CODIFICADOS=$(echo -n "$DATOS_SENSIBLES" | base64 | tr -d '=')

echo "=== SIMULACIÓN: EXFILTRACIÓN DE DATOS VÍA DNS ==="
echo "Dato original: $DATOS_SENSIBLES"
echo "Dato codificado: $DATOS_CODIFICADOS"
echo "Consulta DNS simulada:"
echo "${DATOS_CODIFICADOS}.servidor-web-dmz.onrender.com"

echo "=== SIMULACIÓN FINALIZADA ==="

python3 -m http.server 8080
