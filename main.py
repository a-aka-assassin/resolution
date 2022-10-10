# import FastApi, File and Uploadfile to work with the uploaded file
from fastapi import FastAPI, File, UploadFile

# import glob for making the list of images present in directory
import glob

# import Image from Pil to play around with image
from PIL import Image

# imprt hashlib for hashing the content
import hashlib


app = FastAPI()


# POST request
@app.post("/")
def image_filter(img: UploadFile = File(...)):

    # making a list of files in the directory
    files = glob.glob('./*.jpeg')

    original_image = Image.open(img.file)

    # hashing the name of the file
    fname = img.filename
    str = hashlib.sha256(fname.encode('utf-8'))
    fname_hashed = str.hexdigest()

    # converting the image to JPEG and Saving
    converted_image = original_image.convert('RGB')
    stored_image = converted_image.save(fname_hashed+".JPEG")

    # checking if the image is present and returning the response
    check_name = ".\\" + fname_hashed + ".JPEG"
    for i in files:
        if check_name == i:
            return {
                "new": "false",
                       "url": "/images/" + fname_hashed
            }

    return {
        "new": "true",
        "url": "/images/" + fname_hashed
    }


# Get Request
@app.get('/images/{user_id}')
async def get_user_from_string(user_id: str):

    # Opening the Image and showing
    image1 = Image.open(user_id+".jpeg")
    image1.show()
