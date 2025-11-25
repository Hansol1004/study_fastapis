from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app =FastAPI()

app.mount("/resources", StaticFiles(directory="resources"), name="resources")



from fastapi.templating import Jinja2Templates
from fastapi import Request

Templates = Jinja2Templates(directory="templates/")

@app.get("/")
async def main_root(request: Request):
    return Templates.TemplateResponse(
        "20_vibecodings_concepts.html", {"request": request}
    )

@app.get("/html")
async def main_html(request: Request):

    return Templates.TemplateResponse("20_vibecodings_concepts.html",
                                       {"request": request})     