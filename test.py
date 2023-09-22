from fastapi import FastAPI

app = FastAPI()

@app.get("/test")
async def get_data():
    return {'data': 'ok'}