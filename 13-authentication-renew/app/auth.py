from fastapi import FastAPI

app = FastAPI()

@app.get("/auth/")
async def get_user():
    return {'user': 'authenticated'}