from fastapi import FastAPI, Form, Depends, HTTPException, Request, status
from fastapi.templating import Jinja2Templates
from jinja2 import Environment, PackageLoader, select_autoescape, filters
import sqlalchemy
from fastapi.responses import HTMLResponse, RedirectResponse, JSONResponse
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from pydantic import BaseModel, validator, constr, ValidationError
from fastapi.encoders import jsonable_encoder
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.gzip import GZipMiddleware
from fastapi import UploadFile, File
import os
import uuid

app = FastAPI()
firmware_dir = "firmware_dir"


@app.post("/upload-firmware/")   
async def upload_firmware(product_name: str, version: str, firmwere: UploadFile() ):
    context = {"request": request}
    filePath = os.path.join(firmware_dir, "{}-{}".format(product_name, version))

    with open(filePath, "wb") as buffer:
        buffer.write(await firmware.read())

    context.update({"UUID" : str(uuid.uuid4)})
    return templates.TemplateResponse(name="upload_firmware.html", context=context)

@app.get("/list_firmware/")
async def list_firmware():
    pass

@app.get("/get_firmware/")
async def get_firmware():
    pass
