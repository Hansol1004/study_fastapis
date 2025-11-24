from fastapi import FastAPI

app =FastAPI()


from fastapi.templating import Jinja2Templates
from fastapi import Request

Templates = Jinja2Templates(directory="templates/")

@app.get("/html")
async def main_html(request: Request):

    return Templates.TemplateResponse("20_vibecodings_concepts.html",
                                       {"request": request})    
