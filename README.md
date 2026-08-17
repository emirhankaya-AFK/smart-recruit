# Smart Recruit

[English](README.md) | [Türkçe](README_TR.md)

Explainable candidate/job matching API. It normalizes skills, calculates overlap, and returns matched and missing skills.

POST /api/v1/matches accepts candidate_skills and job_skills. This deterministic MVP is not an automated hiring decision. Production should add consent, deletion controls, bias evaluation, embeddings/reranking and PostgreSQL tenancy.

    pip install -e ".[dev]"
    uvicorn app.main:app --reload
    pytest -q

