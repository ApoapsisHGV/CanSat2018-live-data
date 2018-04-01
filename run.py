from app import create_app
from config import RunConfig

app = create_app(RunConfig)
if __name__ == "__main__":
    app.run()
