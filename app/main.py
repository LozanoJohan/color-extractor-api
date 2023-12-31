from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import os
import requests

from app.models.image_model import process_and_upload_image
from app.schemas.image import ImageInput
import app.color_extractor as color_extractor
from app.config import UPLOAD_DIR



app = FastAPI()



# Allow CORS
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])


@app.get("/")
def read_root():
    return {"message": "Hello World"}


@app.post("/images/")
def upload_image(image: ImageInput):
    try:
        print(image.url)
        response = requests.get(image.url)
        if response.status_code != 200:
            raise Exception(response.raw)
        
        data = process_and_upload_image(image, response)

        return JSONResponse(content=vars(data), status_code=200)

    except Exception as e:
        return JSONResponse(content={"message": "An error occurred", "error": str(e)}, status_code=500)


@app.get("/images/")
def get_uploaded_images():
        imgs = list()

        # List all files in the upload directory
        files = os.listdir(UPLOAD_DIR)
        
        for f in files:
            if os.path.isfile(os.path.join(UPLOAD_DIR, f)):

                # Create a response  object
                img = color_extractor.extract(f)
                imgs.append(vars(img))

        return JSONResponse(content=imgs, status_code=200)

    