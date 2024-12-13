from fastapi import FastAPI
from sqlalchemy.sql import text

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello, Savify!"}


from app.database import engine



@app.get("/test-db")
async def test_db():
    try:
        async with engine.connect() as conn:
            result = await conn.execute(text("SELECT 1"))
            return {"message": "Database connection successful"}
    except Exception as e:
        return {"error": str(e)}

