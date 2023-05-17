from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
from seeders import insertMember


main = FastAPI()

@main.get('/')
def hello():
    return 'hello'




# Register Tortoise ORM
register_tortoise(
    main,
    db_url="sqlite://data.db",
    modules={"models": ["models", "aerich.models"]},
    generate_schemas=True,
    add_exception_handlers=True,
)

@main.on_event("startup")
async def startup_event():
    await insertMember()
    print("Hello world")
    