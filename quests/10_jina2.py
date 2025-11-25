from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import os

# FastAPI 앱 인스턴스 생성
app = FastAPI()

# Jinja2 템플릿 디렉토리 설정
# 이 코드를 실행하려면 'templates' 폴더 안에 'quests' 폴더를 만들고, 
# 그 안에 '10_jina2.html' 파일을 두어야 합니다.
templates = Jinja2Templates(directory="templates")

# 정적 파일 마운트 (리소스 경로가 필요하다면 사용)
# os.getcwd()는 현재 작업 디렉토리를 반환합니다. 
# 실제 경로가 있다면 수정이 필요할 수 있습니다.
if os.path.exists("resources/images"):
    app.mount("/images", StaticFiles(directory="resources/images"), name="images")
if os.path.exists("resources/css"):
    app.mount("/css", StaticFiles(directory="resources/css"), name="css")

# 테스트용 루트 경로 (옵션)
@app.get("/")
async def root():
    return {"message": "Go to /quests/10_jina2 to see the product list."}

# 메인 기능: 상품 목록을 템플릿에 전달하고 렌더링
@app.get("/quests/10_jina2")
async def product_list_page(request: Request):
    
    # 템플릿에 전달할 상품 데이터 목록 (List of Dictionaries)
    products_data = [
        {
            "name": "Laptop Pro",
            "price": 1200,
            "tags": ["electronics", "office", "high-end"]
        },
        {
            "name": "Smartphone X",
            "price": 800,
            "tags": ["mobile", "electronics"]
        },
        {
            "name": "Mechanical Keyboard",
            "price": 100,
            "tags": ["accessories", "input"]
        }
    ]

    # context 딕셔너리 생성. Jinja2 템플릿에서 'Products' 키로 접근 가능합니다.
    context = {
        "request": request,
        "Products" : products_data  # 대문자 'P' 유지 (HTML 템플릿에서 이 이름으로 접근)
    }

    # 템플릿 렌더링 및 응답
    return templates.TemplateResponse("quests/10_jina2.html", context)

# 참고: /main.html 라우트는 주석 처리하거나 제거했습니다.
# 현재 기능과 무관하며, 불필요한 코드는 제거하는 것이 좋습니다.
# @app.get("/main.html")
# async def main_html(request: Request):
#     return templates.TemplateResponse("main.html", {"request": request})