from api import app

if __name__ == '__main__':
    host = '0.0.0.0'  # or '127.0.0.1'
    port = 5000
    app.run(host, port)

