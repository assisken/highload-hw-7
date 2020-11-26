import os

from app.create_app import create_app

DEBUG = os.getenv("DEBUG", "").lower() in ("true", "1")
HOST = os.getenv("HOST", "127.0.0.1")
PORT = int(os.getenv("PORT", "80"))
app = create_app()

if __name__ == "__main__":
    app.run(host=HOST, debug=DEBUG, port=PORT)
