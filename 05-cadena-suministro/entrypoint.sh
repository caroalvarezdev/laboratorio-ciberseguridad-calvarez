
#!/bin/sh

echo "=== INICIANDO SERVICIO COMPROMETIDO EN LA CADENA DE SUMINISTRO ==="
echo "Verificando integridad del contenedor..."

if [ -f "/app/malicious_dependency.sh" ]; then
    echo "[ALERTA DE SEGURIDAD] Se ha detectado una dependencia no autorizada."
    echo "[SIMULACIÓN] Se omite su ejecución por seguridad."
else
    echo "[OK] Artefacto limpio."
fi

python3 -m http.server 8080
