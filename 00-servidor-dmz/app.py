
from http.server import HTTPServer, BaseHTTPRequestHandler
import os

class CustomHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path != "/":
            self.send_error(404, "Ruta no encontrada")
            return

        estudiante = os.getenv(
            "ESTUDIANTE_NOMBRE",
            "Carolina Alvarez"
        )

        html_content = f"""
        <!DOCTYPE html>
        <html lang="es">
        <head>
            <meta charset="UTF-8">
            <title>Servidor Web DMZ</title>
        </head>
        <body>
            <h1>🛡️ Servidor Objetivo DMZ</h1>
            <p>Estado del servicio: <strong>ONLINE / ACTIVO</strong></p>
            <hr>
            <p><strong>Laboratorio de Ciberseguridad:</strong>
            {estudiante}</p>
            <p>Este nodo actúa como objetivo central
            para las pruebas de tráfico y análisis de logs.</p>
        </body>
        </html>
        """

        self.send_response(200)
        self.send_header(
            "Content-type",
            "text/html; charset=utf-8"
        )
        self.end_headers()
        self.wfile.write(html_content.encode("utf-8"))


if __name__ == "__main__":
    server_address = ("", 8080)
    httpd = HTTPServer(server_address, CustomHandler)
    print("Servidor DMZ iniciado en el puerto 8080...")
    httpd.serve_forever()
