# Smart Recruit

[English](README.md) | [Türkçe](README_TR.md)

Açıklanabilir aday/pozisyon eşleştirme API'si. Becerileri normalize eder, kesişimi hesaplar ve eşleşen/eksik becerileri döndürür.

POST /api/v1/matches candidate_skills ve job_skills alır. Bu deterministik MVP otomatik işe alım kararı değildir. Üretimde rıza, silme, önyargı ölçümü, embedding/reranking ve PostgreSQL tenant yapısı eklenmelidir.

    pip install -e ".[dev]"
    uvicorn app.main:app --reload
    pytest -q

