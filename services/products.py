from fastapi import FastAPI
from fastapi.responses import JSONResponse
from httpx import AsyncClient 

app = FastAPI()

@app.get("/")
async def main():
    return {"What a": "page"}

@app.get("/products")
async def getProducts():
    base_url="https://services.odata.org/OData/OData.svc/Products?$format=json"
    async with AsyncClient() as ac:
        response= await ac.get(base_url)
    if response.status_code != 200:
        return JSONResponse(
            content={'error': response.json()['message']},
        status_code=response.status_code)
    #print(response.text)
    response_json = response.json()
    products=[]
    print(response_json['value'])
    for p in response_json['value']:
        products.append(p)
    return JSONResponse(status_code=200,
                        content={'data':products})

'''
docker build -t fastapi-server .
docker run -p 127.0.0.1:4000:8080 fastapi-server => first port 4000 is the containers port. 
                                                    8080 is the host machine port where the service runs.

'''