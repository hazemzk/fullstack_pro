from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
from routers import supplier, product, mails
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

@app.get('/')
def index():
    return {'msg':'Hello World'}

app.include_router(supplier.router)
app.include_router(product.router)
app.include_router(mails.router)

register_tortoise(
    app,
    db_url = 'sqlite://database.sqlite3',
    modules={'models':['models']},
    generate_schemas= True,
    add_exception_handlers=True
)

# adding cors urls 

origins = [
    "http://localhost:3000",
    "https://example.com",
    "https://www.example.com",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)