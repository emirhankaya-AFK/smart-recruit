import re

from fastapi import FastAPI
from pydantic import BaseModel, Field


class MatchRequest(BaseModel):
    resume: str = Field(min_length=20, max_length=20_000)
    job_description: str = Field(min_length=20, max_length=20_000)


class MatchResponse(BaseModel):
    score: float
    matched_skills: list[str]
    missing_skills: list[str]


def words(text: str) -> set[str]:
    return {word.lower() for word in re.findall(r"[a-zA-Z+#.]{2,}", text)}


def match(resume: str, job_description: str) -> MatchResponse:
    resume_words, job_words = words(resume), words(job_description)
    matched = sorted(resume_words & job_words)
    missing = sorted(job_words - resume_words)
    score = round(len(matched) / len(job_words) * 100, 2) if job_words else 0
    return MatchResponse(score=score, matched_skills=matched, missing_skills=missing[:30])


def create_app() -> FastAPI:
    app = FastAPI(title="SmartRecruit", version="0.1.0")

    @app.get("/health")
    async def health() -> dict[str, str]:
        return {"status": "ok", "service": "smart-recruit"}

    @app.post("/api/v1/matches", response_model=MatchResponse)
    async def create_match(request: MatchRequest) -> MatchResponse:
        return match(request.resume, request.job_description)

    return app


app = create_app()
