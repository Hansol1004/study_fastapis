from fastapi import FastAPI

app =FastAPI()


from fastapi.templating import Jinja2Templates
from fastapi import Request

Templates = Jinja2Templates(directory="templates/")

@app.get("/maim.html")
async def main_html(request: Request):

    return Templates.TemplateResponse("main.html",
                                       {"request": request}) 


@app.get("/main_html_context")
async def main_html_context(request: Request):

    context = {
        "request": request,
        "title": "FastAPI + Jinja Example",
        "items": ["Apple", "Banana", "Cherry"],
        "user": {"name": "Sanghun", "age": 33}
    }

    return Templates.TemplateResponse("main_context.html",
                                       context)  


@app.get("/users/list")
async def user_list(request: Request):

    users = [
    {"name": "Alice", "age": 25, "city": "Seoul"},
    {"name": "Bob", "age": 30, "city": "Busan"},
    {"name": "Charlie", "age": 28, "city": "Daegu"}
    ]

    context = {
        "request": request,
        "user_list" : users
        
    }

    return Templates.TemplateResponse("users/list.html",
                                       context)

from fastapi.staticfiles import StaticFiles

app.mount("/images", StaticFiles(directory="resources/images"))
app.mount("/css", StaticFiles(directory="resources/css"))
app.mount("/quests", StaticFiles(directory="quests"), name="quests")

pass