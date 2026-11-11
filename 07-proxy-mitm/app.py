
from flask import Flask, request, Response

app = Flask(__name__)

@app.route("/", defaults={"path": ""}, methods=["GET", "POST"])
@app.route("/<path:path>", methods=["GET", "POST"])
def mitm_proxy(path):

    print(f"[SIMULACIÓN MITM] Solicitud recibida: /{path}")
    print(f"[MÉTODO] {request.method}")

    contenido_original = """
    <html>
    <body>
        <h1>Servidor de prueba</h1>
        <p>Respuesta original del laboratorio.</p>
    </body>
    </html>
    """

    contenido_alterado = contenido_original.replace(
        "</body>",
        "<p>ALERTA MITM: contenido modificado en la simulación.</p></body>"
    )

    print("[MITM ALERTA] Modificación simulada correctamente.")

    return Response(
        contenido_alterado,
        status=200,
        mimetype="text/html"
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
