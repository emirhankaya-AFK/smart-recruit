## English

**Purpose**  
Explainable candidate/job matching API that normalizes skills, calculates overlap, and returns matched and missing skills.

**Verified features**  
- POST `/api/v1/matches` accepts `candidate_skills` and `job_skills`.  
- Skill normalization and overlap calculation.  
- Deterministic matching (no randomness).  
- Returns both matched and missing skills.

**Stack**  
- Python (project defined by `pyproject.toml`).  
- API served with Uvicorn (`app.main:app`).  
- Testing with `pytest`.  
- Containerization support via `Dockerfile` and `compose.yaml`.  
- Continuous integration defined in `.github/workflows/ci.yml`.

**Setup & usage**  
```bash
pip install -e ".[dev]"
uvicorn app.main:app --reload
```

**Testing**  
```bash
pytest -q
```

**Limitations**  
- This is a deterministic minimum viable product (MVP) and is **not** intended for automated hiring decisions.  
- For production use, consider adding consent mechanisms, data deletion controls, bias evaluation, embeddings/reranking, and a multi‑tenant PostgreSQL storage layer.

**License**  
See the `LICENSE` file.

---

## Türkçe

**Amaç**  
Becerileri normalize eden, overlap hesaplayan ve eşleşen ile eksik becerileri dönen açıklarlayıcı aday/iş eşleştirme API'si.

**Doğrulanmış özellikler**  
- `POST /api/v1/matches` endpointi `candidate_skills` ve `job_skills` kabul eder.  
- Beceri normalizasyonu ve overlap hesaplaması.  
- Deterministik eşleştirme (rastgelelik yok).  
- Eşleşen ve eksik becerileri döndürür.

**Yığın**  
- Python (`pyproject.toml` ile tanımlanır).  
- API Uvicorn ile sunulur (`app.main:app`).  
- Testler `pytest` ile çalıştırılır.  
- Konteyner desteği `Dockerfile` ve `compose.yaml` ile sağlanır.  
- Sürekli entegrasyon `.github/workflows/ci.yml` dosyasında tanımlanır.

**Kurulum & kullanım**  
```bash
pip install -e ".[dev]"
uvicorn app.main:app --reload
```

**Test**  
```bash
pytest -q
```

**Sınırlamalar**  
- Bu bir deterministik minimum ürün (MVP) olup otomatik işe alım kararları için **tasarlanmamıştır**.  
- Üretimde kullanım için onay mekanizmaları, veri silme kontrolleri, bias değerlendirmesi, embeddings/reranking ve çok kiracılı PostgreSQL depolama eklenmelidir.

**Lisans**  
`LICENSE` dosyasına bakınız.

---

## Deutsch

**Zweck**  
Eine erklärbare API zum Matching von Kandidaten und Stellen, die Fähigkeiten normalisiert, die Überschneidung berechnet und übereinstimmende sowie fehlende Fähigkeiten zurückgibt.

**Überprüfte Funktionen**  
- Der Endpunkt `POST /api/v1/matches` nimmt `candidate_skills` und `job_skills` entgegen.  
- Fähigkeitsnormalisierung und Überschneidungsberechnung.  
- Deterministisches Matching (keine Zufälligkeit).  
- Rückgabe sowohl der übereinstimmenden als auch der fehlenden Fähigkeiten.

**Stack**  
- Python (definiert durch `pyproject.toml`).  
- Der API-Dienst wird mit Uvicorn bereitgestellt (`app.main:app`).  
- Tests werden mit `pytest` ausgeführt.  
- Containerisierung wird durch `Dockerfile` und `compose.yaml` unterstützt.  
- Continuous Integration ist in `.github/workflows/ci.yml` konfiguriert.

**Einrichtung & Nutzung**  
```bash
pip install -e ".[dev]"
uvicorn app.main:app --reload
```

**Tests**  
```bash
pytest -q
```

**Einschränkungen**  
- Es handelt sich um ein deterministisches Minimum Viable Product (MVP), das **nicht** für automatisierte Einstellungsentscheidungen vorgesehen ist.  
- Für den Produktiveinsatz sollten Einwilligungsmechanismen, Löschkontrollen, Bias‑Evaluierung, Embeddings/Re‑Ranking sowie eine mehr‑Mandanten‑PostgreSQL‑Speicherung berücksichtigt werden.

**Lizenz**  
Siehe die Datei `LICENSE`.
