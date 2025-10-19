from fastapi import FastAPI, HTTPException, UploadFile, File, Form
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime
import uuid

app = FastAPI(title="AquaVerse - Scaffold API")

# In-memory stores (for demo only)
USERS = {}
POSTS = {}
TANK_LOGS = {}
PRODUCTS = {}

class UserCreate(BaseModel):
    username: str
    display_name: Optional[str] = None

class PostCreate(BaseModel):
    user_id: str
    caption: str
    image_url: Optional[str] = None

class TankLogCreate(BaseModel):
    user_id: str
    temperature_c: Optional[float] = None
    ph: Optional[float] = None
    ammonia_ppm: Optional[float] = None
    notes: Optional[str] = None

@app.post('/users', status_code=201)
def create_user(u: UserCreate):
    if u.username in USERS:
        raise HTTPException(400, 'username exists')
    uid = str(uuid.uuid4())
    USERS[u.username] = {'id': uid, 'username': u.username, 'display_name': u.display_name}
    return USERS[u.username]

@app.get('/users')
def list_users():
    return list(USERS.values())

@app.post('/posts', status_code=201)
def create_post(p: PostCreate):
    pid = str(uuid.uuid4())
    POSTS[pid] = {'id': pid, 'user_id': p.user_id, 'caption': p.caption, 'image_url': p.image_url, 'created_at': datetime.utcnow().isoformat()}
    return POSTS[pid]

@app.get('/posts')
def get_posts():
    # return posts sorted by created_at desc
    items = list(POSTS.values())
    items.sort(key=lambda x: x.get('created_at',''), reverse=True)
    return items

@app.post('/tank_logs', status_code=201)
def create_tank_log(t: TankLogCreate):
    lid = str(uuid.uuid4())
    TANK_LOGS[lid] = {'id': lid, 'user_id': t.user_id, 'temperature_c': t.temperature_c, 'ph': t.ph, 'ammonia_ppm': t.ammonia_ppm, 'notes': t.notes, 'created_at': datetime.utcnow().isoformat()}
    return TANK_LOGS[lid]

@app.get('/tank_logs/{user_id}')
def get_tank_logs(user_id: str):
    return [l for l in TANK_LOGS.values() if l['user_id'] == user_id]

@app.get('/products')
def list_products(q: Optional[str] = None):
    items = list(PRODUCTS.values())
    if q:
        items = [p for p in items if q.lower() in p['name'].lower()]
    return items

# Seed sample product
pid = str(uuid.uuid4())
PRODUCTS[pid] = {'id': pid, 'name': 'Nano Aquarium LED Light', 'price_usd': 49.99, 'description': 'Energy-efficient LED suitable for planted nano tanks.'}
