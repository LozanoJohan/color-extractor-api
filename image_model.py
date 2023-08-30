from database import db, bucket
from config import UPLOAD_DIR
from image import ImageInput
import shutil
from pathlib import Path
import color_extractor


def upload_image_to_db(bucket, file_path):
    blob = bucket.blob(file_path)
    blob.upload_from_filename(file_path)


def upload_image_to_sys(image: ImageInput, birary_data):    
    file_name = image.name + '.' + image.ext
    file_path = f"{Path(UPLOAD_DIR)}/{file_name}"

    with open(file_path,"wb") as f:
        f.write(birary_data.content)
        shutil.copyfileobj(birary_data.raw, f)

    return file_name, file_path


def process_and_upload_image(image: ImageInput, birary_data):
    file_name, file_path = upload_image_to_sys(image, birary_data)
    upload_image_to_db(bucket, file_path)

    image_data = color_extractor.extract(file_name)
    db.collection("images").add(vars(image_data))

    return image_data