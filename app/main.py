from fastapi import FastAPI, UploadFile, File
from typing import List
import csv
import motor.motor_asyncio
from pymongo import MongoClient

app = FastAPI()

client = MongoClient('localhost', 27017)
db = client['test_database']
collection = db['test_collection']

@app.post("/uploadcsv/")
async def create_upload_file(file: UploadFile = File(...)):
    contents = await file.read()
    data = csv.reader(contents.decode('utf-8').splitlines())
    header = next(data)
    for row in data:
        doc = {header[i]: row[i] for i in range(len(header))}
        collection.insert_one(doc)
    return {"filename": file.filename}
