from fastapi import FastAPI
from app.routers.rainbow import router as rainbow_router
from app.routers.llama import router as llama_router

app = FastAPI()

# Include the routers in the main app
app.include_router(rainbow_router)
app.include_router(llama_router)


@app.get("/")
def read_root():
    return {"Hello": "World"}