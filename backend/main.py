from fastapi import FastAPI, UploadFile, File

from models.prediction import predict_image, read_file

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    extension = file.filename.split(".")[-1] in ("jpg", "jpeg", "png")
    if not extension:
        return {"error": "File extension not allowed"}
    image = read_file( await file.read())
    result = predict_image(image)
    return {"result": result}