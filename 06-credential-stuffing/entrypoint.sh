#!/bin/sh

USUARIOS="admin root user docente gestor"
CLAVE="password123"

echo "=== SIMULACION DE CREDENTIAL STUFFING ==="
echo "Evaluando combinaciones de credenciales..."
echo "Entorno: laboratorio local"

for user in $USUARIOS; do
    echo "Simulando intento para usuario: $user"
    echo "Respuesta HTTP simulada: 401"
done

echo "=== SIMULACION FINALIZADA ==="
echo "Recomendacion: implementar MFA y bloqueo de intentos."

python3 -m http.server 8080
