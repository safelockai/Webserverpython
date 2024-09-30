import os
from http.server import SimpleHTTPRequestHandler, HTTPServer

class CustomHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        # Verifica se o caminho acessado é apenas a raiz
        if self.path == '/':
            # Busca automaticamente por um arquivo HTML
            html_files = [f for f in os.listdir('.') if f.endswith('.html')]
            if html_files:
                # Se existir um arquivo HTML, redireciona para o primeiro encontrado
                self.send_response(302)
                self.send_header('Location', html_files[0])
                self.end_headers()
            else:
                self.send_error(404, "Arquivo HTML não encontrado.")
            return
        
        # Restringe o acesso a arquivos que não sejam o HTML principal
        if not self.path.endswith('.html'):
            self.send_error(403, "Acesso negado a este recurso.")
            return
        
        return SimpleHTTPRequestHandler.do_GET(self)

if __name__ == "__main__":
    port = 8000
    server_address = ('', port)
    httpd = HTTPServer(server_address, CustomHandler)
    print(f"Servidor rodando em http://localhost:{port}/")
    httpd.serve_forever()
