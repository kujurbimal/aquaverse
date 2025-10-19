# AquaVerse - Aquarium Enthusiasts Social App (Scaffold)

This scaffold contains a minimal backend (FastAPI) and a simple frontend (static HTML/JS) for AquaVerse — a niche community app for aquarium hobbyists.

## What is included
- backend/: FastAPI app with simple in-memory stores for users, posts, and aquarium logs
- frontend_web/: Static single-page app (index.html) that interacts with the backend via fetch
- infra/: Dockerfile to run the backend
- sample_data/: sample images and example data

## Quickstart (backend)
```bash
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```

## Frontend
Open `frontend_web/index.html` in a browser. By default it expects the backend at http://localhost:8000

## Notes
- This is a scaffold for development and demo purposes only. Replace the in-memory stores with a real DB (Postgres) and add secure auth for production.
- To deploy, containerize the backend or use Render/Heroku and host the static frontend on GitHub Pages / Vercel.
