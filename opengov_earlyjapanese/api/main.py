"""FastAPI app exposing minimal endpoints."""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from opengov_earlyjapanese.config import settings
from opengov_earlyjapanese.core.hiragana import HiraganaTeacher

app = FastAPI(title=settings.api_title, version=settings.api_version)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {"name": settings.api_title, "version": settings.api_version}


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/hiragana/{row}")
def get_hiragana_row(row: str):
    teacher = HiraganaTeacher()
    try:
        lesson = teacher.get_lesson(row)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    return lesson.model_dump()



