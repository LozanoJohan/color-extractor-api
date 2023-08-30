from pydantic import BaseModel


class ImageInput(BaseModel):
    name: str
    ext: str
    url: str



class ImageResponse:
    def __init__(self, name, ext, width, height, colors):
        self.name = name
        self.ext = ext
        self.width = width
        self.height = height
        self.colors = colors