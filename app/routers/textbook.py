# users.py
from urllib.parse import unquote

from fastapi import APIRouter
from fastapi import Depends, FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from . import examples as exmp
from .. import marker as mark

router = APIRouter()
#app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@router.get("/textbook/refresher")
async def refresher(request: Request):
    #return [{"chapter": "Refresher"}]
    return templates.TemplateResponse("refresher.html", {"request": request})


@router.get("/textbook/arithmetic_of_fractions")
async def arithmetic_of_fractions(request: Request):
    exmpls = exmp.getExamples(1)  #'<h1>fractions</h1>'  
    print('t25', exmpls)
    exdata = {
        'examples' : exmpls
    }
    #return render_template('11_Vectors.html', data=exdata)

    return templates.TemplateResponse("arithmetic_of_fractions.html", {"request": request, "data": exdata})


@router.get("/textbook/expressions_involving_indices")
async def expressions_involving_indices(request: Request):
    #return [{"chapter": "Refresher"}]
    return templates.TemplateResponse("expressions_involving_indices.html", {"request": request})


# ==========================================================
@router.post("/textbook/mark_example")
async def mark_example(request: Request):  #inSAns, inCans, p=10):
  print('\n\n==== mark_example Start =============================')
  print(41, request, request.body, request.url.path)
  tmp = b''
  async for chunk in request.stream():
    tmp += chunk
  tmp1 = str(tmp)  
  tmp1 = tmp1[2:-1]
  print(47, tmp1)
  tmp1 = tmp1.replace('+', ' ')
  tmp2 = unquote(tmp1)
  print(49, tmp2)
  lst = tmp2.split('&')
  for l in lst:
    print(52, l)

  tmp3 = await mark.mark_example(lst[0], lst[1])
  print(61, tmp3)
  
  return tmp3
# ==========================================================


'''
@router.post("/mark_example", response_class=HTMLResponse)
async def mark_example(request: Request):
    print(41, request, request.body, request.url.path)
    tmp = b''
    async for chunk in request.stream():
        tmp += chunk
    tmp1 = str(tmp)  
    tmp1 = tmp1[2:-1]
    print(47, tmp1)
    tmp2 = urllib.parse.urlparse(tmp1)
    print(49, tmp2)
    lst = tmp1.split('&')
    for l in lst:
        print(52, l)
    #form_data = request.form()
    #print(189, form_data)
    #return {"item_id": item.id, "item_description": item.description}
    return 'done'  #form_data



@router.get("/users/me", tags=["users"])
async def read_user_me():
    return {"username": "fakecurrentuser"}


@router.get("/users/{username}", tags=["users"])
async def read_user(username: str):
    return {"username": username}
'''