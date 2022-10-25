from fastapi import FastAPI

app = FastAPI()


@app.get("/health", include_in_schema=False)
def home():
    ...
