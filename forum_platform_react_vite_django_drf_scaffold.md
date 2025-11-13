# Forum Platform — React (Vite) + Django (DRF) scaffold

> Full minimal, production-ready scaffold for a forum: backend in Django + Django REST Framework (with Simple JWT), frontend in React (Vite) + Tailwind. Use this as a starting point — everything below is copy/paste-ready.

---

## Project overview

- **Backend**: Django, Django REST Framework, Simple JWT for auth. Models: Category, Thread, Post. ViewSets + routers. CORS allowed for local dev.
- **Frontend**: React (Vite), React Router, Tailwind CSS. JWT auth stored in memory + refresh token in httpOnly cookie (optional) — scaffold uses localStorage for simplicity with clear TODO notes.
- **Dev tools**: Dockerfile + docker-compose example, `Makefile` commands, environment (.env.example).

---

## File tree (suggested)

```
forum-project/
├─ backend/
│  ├─ Dockerfile
│  ├─ docker-compose.yml
│  ├─ requirements.txt
│  ├─ .env.example
│  ├─ manage.py
│  └─ backend/ (django project)
│     ├─ settings.py
│     ├─ urls.py
│     └─ api/ (app)
│        ├─ models.py
│        ├─ serializers.py
│        ├─ views.py
│        ├─ permissions.py
│        └─ urls.py
├─ frontend/
│  ├─ package.json
│  ├─ vite.config.js
│  ├─ tailwind.config.cjs
│  └─ src/
│     ├─ main.jsx
│     ├─ App.jsx
│     ├─ api.js
│     ├─ pages/
│     │  ├─ Login.jsx
│     │  ├─ Register.jsx
│     │  ├─ ThreadList.jsx
│     │  ├─ ThreadDetail.jsx
│     │  └─ NewThread.jsx
│     └─ components/
│        ├─ Navbar.jsx
│        └─ PostComposer.jsx
└─ README.md
```

---

## Backend — key files

### `requirements.txt`

```
Django>=4.2
djangorestframework
djangorestframework-simplejwt
django-cors-headers
psycopg2-binary  # if using Postgres
gunicorn
```


### `backend/settings.py` (important snippets)

```py
# settings.py (snippets)
import os
from datetime import timedelta

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = os.getenv('SECRET_KEY', 'dev-secret')
DEBUG = os.getenv('DEBUG', '1') == '1'
ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'corsheaders',
    'api',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
]

CORS_ALLOW_ALL_ORIGINS = True  # tighten in prod

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    ),
}

from datetime import timedelta
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=60),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=7),
}

STATIC_URL = '/static/'
```


### `api/models.py`

```py
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Category(models.Model):
    name = models.CharField(max_length=120)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

class Thread(models.Model):
    title = models.CharField(max_length=300)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='threads')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='threads')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Post(models.Model):
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE, related_name='posts')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('created_at',)
```


### `api/serializers.py`

```py
from rest_framework import serializers
from .models import Category, Thread, Post
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username')

class PostSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    class Meta:
        model = Post
        fields = ('id','thread','author','content','created_at')
        read_only_fields = ('id','author','created_at')

class ThreadSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    posts = PostSerializer(many=True, read_only=True)
    class Meta:
        model = Thread
        fields = ('id','title','author','category','created_at','posts')

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id','name','slug')
```


### `api/views.py` (DRF viewsets)

```py
from rest_framework import viewsets, permissions
from .models import Category, Thread, Post
from .serializers import CategorySerializer, ThreadSerializer, PostSerializer

class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ThreadViewSet(viewsets.ModelViewSet):
    queryset = Thread.objects.all().order_by('-updated_at')
    serializer_class = ThreadSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_permissions(self):
        if self.action in ['update','partial_update','destroy']:
            return [permissions.IsAuthenticated(),]
        return [permissions.IsAuthenticatedOrReadOnly(),]
```


### `backend/urls.py` and `api/urls.py`

```py
# backend/urls.py
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView, TokenRefreshView,
)

router = routers.DefaultRouter()
from api.views import CategoryViewSet, ThreadViewSet, PostViewSet
router.register('categories', CategoryViewSet, basename='category')
router.register('threads', ThreadViewSet, basename='thread')
router.register('posts', PostViewSet, basename='post')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/', include(router.urls)),
]
```


---

## Frontend — key files

### `package.json` (essentials)

```json
{
  "name": "forum-frontend",
  "private": true,
  "version": "0.0.1",
  "scripts": {
    "dev": "vite",
    "build": "vite build",
    "preview": "vite preview"
  },
  "dependencies": {
    "react": "^18.0.0",
    "react-dom": "^18.0.0",
    "react-router-dom": "^6.0.0",
    "axios": "^1.0.0"
  },
  "devDependencies": {
    "vite": "^5.0.0",
    "tailwindcss": "^3.0.0",
    "postcss": "^8.0.0",
    "autoprefixer": "^10.0.0"
  }
}
```


### `src/api.js` — tiny wrapper using axios

```js
import axios from 'axios';

const API = axios.create({
  baseURL: import.meta.env.VITE_API_BASE || 'http://localhost:8000/api/',
});

export function setAuthToken(token){
  if(token) API.defaults.headers.common['Authorization'] = `Bearer ${token}`;
  else delete API.defaults.headers.common['Authorization'];
}

export default API;
```


### `src/main.jsx` and `src/App.jsx`

```jsx
// main.jsx
import React from 'react'
import { createRoot } from 'react-dom/client'
import { BrowserRouter } from 'react-router-dom'
import App from './App'
import './index.css'

createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <BrowserRouter>
      <App />
    </BrowserRouter>
  </React.StrictMode>
)

// App.jsx (routing + auth state)
import React, {useState, useEffect} from 'react'
import { Routes, Route, Navigate } from 'react-router-dom'
import ThreadList from './pages/ThreadList'
import ThreadDetail from './pages/ThreadDetail'
import NewThread from './pages/NewThread'
import Login from './pages/Login'
import Register from './pages/Register'
import Navbar from './components/Navbar'
import { setAuthToken } from './api'

export default function App(){
  const [token, setToken] = useState(localStorage.getItem('access') || null)
  useEffect(()=>{
    setAuthToken(token)
    if(token) localStorage.setItem('access', token)
    else localStorage.removeItem('access')
  },[token])

  return (
    <div className="min-h-screen bg-gray-50">
      <Navbar token={token} setToken={setToken} />
      <div className="container mx-auto p-4">
        <Routes>
          <Route path='/' element={<ThreadList />} />
          <Route path='/threads/:id' element={<ThreadDetail />} />
          <Route path='/new' element={ token ? <NewThread/> : <Navigate to='/login' />} />
          <Route path='/login' element={<Login setToken={setToken} />} />
          <Route path='/register' element={<Register />} />
        </Routes>
      </div>
    </div>
  )
}
```


### `src/pages/ThreadList.jsx` (example)

```jsx
import React, {useEffect, useState} from 'react'
import API from '../api'
import { Link } from 'react-router-dom'

export default function ThreadList(){
  const [threads, setThreads] = useState([])
  useEffect(()=>{
    API.get('threads/').then(r=>setThreads(r.data))
  },[])
  return (
    <div>
      <h1 className="text-2xl font-bold mb-4">Threads</h1>
      <ul>
        {threads.map(t=> (
          <li key={t.id} className="p-3 border rounded mb-2">
            <Link to={`/threads/${t.id}`} className="font-medium">{t.title}</Link>
            <div className="text-sm text-gray-500">{t.author?.username} • {new Date(t.created_at).toLocaleString()}</div>
          </li>
        ))}
      </ul>
    </div>
  )
}
```


### `src/pages/ThreadDetail.jsx` (example showing posts + composer)

```jsx
import React, {useEffect, useState} from 'react'
import API from '../api'
import { useParams } from 'react-router-dom'
import PostComposer from '../components/PostComposer'

export default function ThreadDetail(){
  const { id } = useParams()
  const [thread, setThread] = useState(null)

  useEffect(()=>{
    API.get(`threads/${id}/`).then(r=>setThread(r.data))
  },[id])

  if(!thread) return <div>Loading…</div>
  return (
    <div>
      <h1 className="text-xl font-bold">{thread.title}</h1>
      <div className="mt-4">
        {thread.posts.map(p=> (
          <div key={p.id} className="mb-3 p-3 border rounded">
            <div className="text-sm text-gray-600">{p.author.username} • {new Date(p.created_at).toLocaleString()}</div>
            <div className="mt-2 whitespace-pre-wrap">{p.content}</div>
          </div>
        ))}
      </div>
      <PostComposer threadId={id} onPosted={()=> API.get(`threads/${id}/`).then(r=>setThread(r.data))} />
    </div>
  )
}
```


### `src/components/PostComposer.jsx`

```jsx
import React, {useState} from 'react'
import API from '../api'

export default function PostComposer({ threadId, onPosted }){
  const [content, setContent] = useState('')
  const submit = async(e)=>{
    e.preventDefault()
    await API.post('posts/', { thread: threadId, content })
    setContent('')
    if(onPosted) onPosted()
  }
  return (
    <form onSubmit={submit} className="mt-4">
      <textarea value={content} onChange={e=>setContent(e.target.value)} rows={5} className="w-full p-2 border rounded" />
      <div className="mt-2"><button className="px-4 py-2 rounded bg-indigo-600 text-white">Post</button></div>
    </form>
  )
}
```


---

## Running locally (quickstart)

### Backend

1. Create and activate a Python virtualenv.
2. `pip install -r requirements.txt`
3. Set `SECRET_KEY` and other env vars or use `.env`.
4. `python manage.py migrate`
5. `python manage.py createsuperuser`
6. `python manage.py runserver 0.0.0.0:8000`

### Frontend

1. `cd frontend`
2. `npm install`
3. `npm run dev`

**Note:** If using Docker, the `docker-compose.yml` in the canvas sets up a web and db service. Adjust env values.

---

## Production notes & next steps

- Harden CORS and `ALLOWED_HOSTS`.
- Serve static files with WhiteNoise or behind a CDN.
- Consider using refresh tokens with httpOnly cookies for better security and to avoid localStorage storing tokens.
- Add pagination, search, moderation, uploads (images), likes/upvotes, reactions, user profiles, notifications.
- Add tests for major API endpoints and components.

---

If you'd like, I can:
- Generate a runnable `docker-compose.yml` + Dockerfiles.
- Produce a complete ready-to-run repo as a ZIP you can download.
- Add features: user profiles, upvotes, moderation dashboards, Markdown support, rich editor, or WebSocket-based live updates.

Tell me which extras you want and I'll extend the scaffold.


---

## Docker + Compose (ready-to-use)

Below are complete Dockerfiles for backend and frontend, a `docker-compose.yml` that runs Postgres + backend + frontend, and a `.env.example` tuned for local development.

### `backend/Dockerfile`

```dockerfile
# backend/Dockerfile
FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

# system deps
RUN apt-get update && apt-get install -y build-essential libpq-dev --no-install-recommends && rm -rf /var/lib/apt/lists/*

# install pipenv / poetry if desired; here we use pip
COPY backend/requirements.txt /app/requirements.txt
RUN pip install --upgrade pip && pip install -r /app/requirements.txt

COPY backend/ /app/

# collect static (optional) and run migrations on container start via entrypoint
CMD ["gunicorn", "backend.wsgi:application", "-w", "2", "-b", "0.0.0.0:8000"]
```


### `frontend/Dockerfile`

```dockerfile
# frontend/Dockerfile
FROM node:20-alpine as build
WORKDIR /app
COPY frontend/package.json frontend/package-lock.json* ./
RUN npm ci
COPY frontend/ ./
RUN npm run build

FROM nginx:stable-alpine
COPY --from=build /app/dist /usr/share/nginx/html
# Replace default nginx conf if you want custom proxying (optional)
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
```


### `docker-compose.yml`

```yaml
version: '3.8'
services:
  db:
    image: postgres:15
    environment:
      POSTGRES_USER: forum
      POSTGRES_PASSWORD: forum
      POSTGRES_DB: forumdb
    volumes:
      - pgdata:/var/lib/postgresql/data
    networks:
      - forumnet

  backend:
    build:
      context: .
      dockerfile: backend/Dockerfile
    env_file:
      - .env
    depends_on:
      - db
    ports:
      - '8000:8000'
    volumes:
      - ./backend/:/app/
    networks:
      - forumnet

  frontend:
    build:
      context: .
      dockerfile: frontend/Dockerfile
    ports:
      - '3000:80'
    depends_on:
      - backend
    networks:
      - forumnet

volumes:
  pgdata:

networks:
  forumnet:
    driver: bridge
```


### `.env.example`

```
# .env.example - copy to .env and fill values
SECRET_KEY=changeme
DEBUG=1
DB_HOST=db
DB_PORT=5432
DB_NAME=forumdb
DB_USER=forum
DB_PASSWORD=forum
```


## Entrypoint notes & helpful commands

- The `backend` image uses `gunicorn` in the Dockerfile CMD; for development you can instead run `python manage.py runserver 0.0.0.0:8000` either by overriding the command or by mounting the code (compose above mounts `./backend` already).
- To run the stack:

```bash
cp .env.example .env
# edit .env if desired
docker compose up --build
```

- To run migrations after containers start:

```bash
docker compose exec backend python manage.py migrate
docker compose exec backend python manage.py createsuperuser
```

- If you prefer HTTPS or a proxy (recommended for production), add an nginx service with TLS or place a load balancer / reverse proxy in front.

---

## Optional: JWT refresh with httpOnly cookies (backend + frontend hints)

A secure refresh flow stores the **access token in memory** and the **refresh token in an httpOnly cookie**. Below are short implementation hints you can apply if you want to replace the simple localStorage method used in the scaffold.

### Backend (Django)
- Add an endpoint that issues a refresh token and sets it as an httpOnly Secure cookie on login.
- Use `rest_framework_simplejwt.tokens.RefreshToken.for_user(user)` to create refresh tokens.
- On a refresh endpoint, read the refresh token from the cookie, verify it, and return a new access token in JSON.
- Make sure to set `CSRF_COOKIE_SECURE=True` and use proper SameSite settings in production.

### Frontend (React)
- Keep access token in React state (not localStorage).
- On app startup, call a `/api/auth/refresh/` endpoint to obtain an access token if a valid refresh cookie exists.
- Intercept 401 responses with an axios interceptor: try refresh once, then retry the original request.

I can implement this flow in the scaffold (server endpoints + React refresh logic)."

---

## Implementation: Secure Refresh-Token Endpoints (Django) + Frontend Axios Refresh Logic

Below I add **concrete code** you can copy into the scaffold to implement a secure refresh-token flow that stores the refresh token in an **httpOnly cookie** while keeping the access token in memory. This minimizes long-lived token exposure and lets the frontend transparently refresh the access token.

> Files to add/update on the backend: `api/auth_views.py`, small changes in `backend/urls.py`, and a couple of settings in `backend/settings.py`.

### `api/auth_views.py`

```py
# api/auth_views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
from rest_framework_simplejwt.authentication import AUTH_HEADER_TYPES
from django.conf import settings
from django.contrib.auth import authenticate

class LoginSetCookieView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if not user:
            return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

        refresh = RefreshToken.for_user(user)
        access = str(refresh.access_token)

        # set refresh token in httpOnly cookie
        resp = Response({'access': access})
        cookie_max_age = int(settings.SIMPLE_JWT['REFRESH_TOKEN_LIFETIME'].total_seconds())
        resp.set_cookie(
            key='refresh_token',
            value=str(refresh),
            httponly=True,
            secure=not settings.DEBUG,  # secure in prod
            samesite='Lax',
            max_age=cookie_max_age,
            path='/'
        )
        return resp

class RefreshFromCookieView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        refresh_token = request.COOKIES.get('refresh_token')
        if not refresh_token:
            return Response({'detail': 'No refresh token'}, status=status.HTTP_401_UNAUTHORIZED)
        try:
            refresh = RefreshToken(refresh_token)
            access = str(refresh.access_token)
            return Response({'access': access})
        except Exception:
            return Response({'detail': 'Invalid refresh token'}, status=status.HTTP_401_UNAUTHORIZED)

class LogoutClearCookieView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        resp = Response({'detail': 'logged out'})
        # Overwrite cookie to expire it
        resp.delete_cookie('refresh_token', path='/')
        return resp
```


### `backend/urls.py` additions

Add the new endpoints so the frontend can call them:

```py
# backend/urls.py (add these imports near top)
from api.auth_views import LoginSetCookieView, RefreshFromCookieView, LogoutClearCookieView

# then add paths inside urlpatterns
path('api/auth/login/', LoginSetCookieView.as_view(), name='login_cookie'),
path('api/auth/refresh/', RefreshFromCookieView.as_view(), name='refresh_cookie'),
path('api/auth/logout/', LogoutClearCookieView.as_view(), name='logout_cookie'),
```


### `backend/settings.py` security tweaks

Ensure cookie and CSRF settings are production-ready. Add / change these settings:

```py
# settings.py additions
CSRF_COOKIE_HTTPONLY = False  # frameworks expect JS to read csrftoken cookie for some flows; keep False unless fully cookie-only
CSRF_COOKIE_SECURE = not DEBUG
SESSION_COOKIE_SECURE = not DEBUG
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SIMPLE_JWT['ROTATE_REFRESH_TOKENS'] = False
SIMPLE_JWT['UPDATE_LAST_LOGIN'] = False
# make sure REFRESH_TOKEN_LIFETIME exists (we set earlier to 7 days in scaffold)
```

Notes: In a stricter setup, you can set `CSRF_COOKIE_HTTPONLY = True` and implement a double-submit CSRF token using a separate endpoint; the above is a pragmatic setup to avoid breaking common scenarios.


---

## Frontend: Axios + React Implementation (refresh from cookie)

Goal: Keep the access token **in React state**; store refresh token in httpOnly cookie (handled by the backend). Use an axios instance with an interceptor that attempts a refresh on 401, once per request.

### `src/api.js` (replace with the following)

```js
// src/api.js
import axios from 'axios'

const API = axios.create({
  baseURL: import.meta.env.VITE_API_BASE || 'http://localhost:8000/api/',
  withCredentials: true, // important: send cookies (refresh token)
})

let inMemoryAccessToken = null
let isRefreshing = false
let refreshCall = null

export function setAccessToken(token){
  inMemoryAccessToken = token
  if(token) API.defaults.headers.common['Authorization'] = `Bearer ${token}`
  else delete API.defaults.headers.common['Authorization']
}

// Call refresh endpoint which reads httpOnly cookie and returns a new access token
async function fetchNewAccessToken(){
  return API.post('auth/refresh/').then(r => r.data.access)
}

// Axios response interceptor
API.interceptors.response.use(
  resp => resp,
  async error => {
    const originalRequest = error.config
    if (error.response && error.response.status === 401 && !originalRequest._retry) {
      // avoid infinite loop
      originalRequest._retry = true
      try {
        if(!isRefreshing){
          isRefreshing = true
          refreshCall = fetchNewAccessToken()
          const newAccess = await refreshCall
          setAccessToken(newAccess)
        } else {
          // wait for existing refresh
          await refreshCall
        }
        isRefreshing = false
        // retry original request
        originalRequest.headers['Authorization'] = `Bearer ${inMemoryAccessToken}`
        return API(originalRequest)
      } catch (e) {
        isRefreshing = false
        setAccessToken(null)
        // if refresh fails, forward the error
        return Promise.reject(e)
      }
    }
    return Promise.reject(error)
  }
)

export { API as default }
```


### Login / Logout changes (examples)

- In `src/pages/Login.jsx`, on successful login POST to `/api/auth/login/` with `{username,password}` and the response will contain `{access}`. Call `setAccessToken(access)` with that value.
- For logout call `POST /api/auth/logout/` (with credentials) and then `setAccessToken(null)`.

Example (login handler):

```js
// inside Login component after successful form submit
const res = await API.post('auth/login/', { username, password })
setAccessToken(res.data.access)
```

Example (on app start):

```js
// in App.jsx useEffect on mount
// try to refresh access token (if refresh cookie exists)
useEffect(()=>{
  async function bootstrap(){
    try{
      const r = await API.post('auth/refresh/')
      setAccessToken(r.data.access)
    }catch(e){
      setAccessToken(null)
    }
  }
  bootstrap()
}, [])
```

Notes: `withCredentials: true` on the axios instance is critical so the browser sends the refresh cookie. The refresh endpoint returns the new access token only; the refresh cookie remains unchanged and will keep working until it expires (or you rotate it).

---

## Nginx: Reverse Proxy + TLS Hints (production-ready skeleton)

Below is a recommended nginx configuration. In production you should terminate TLS at a load balancer or nginx, keep HTTP -> HTTPS redirects, enable HSTS, and proxy to your upstream backend and static frontend files. This example assumes nginx terminates TLS and proxies API requests to an internal backend service.

### `nginx/conf.d/forum.conf`

```nginx
server {
    listen 80;
    server_name example.com www.example.com;
    # Redirect all HTTP to HTTPS
    return 301 https://$host$request_uri;
}

server {
    listen 443 ssl http2;
    server_name example.com www.example.com;

    ssl_certificate /etc/letsencrypt/live/example.com/fullchain.pem; # use certbot or your CA
    ssl_certificate_key /etc/letsencrypt/live/example.com/privkey.pem;
    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_prefer_server_ciphers on;
    ssl_session_cache shared:SSL:10m;

    add_header Strict-Transport-Security "max-age=31536000; includeSubDomains; preload";

    # Static frontend
    location / {
        root /usr/share/nginx/html; # where frontend build is deployed
        try_files $uri $uri/ /index.html;
    }

    # API proxy
    location /api/ {
        proxy_pass http://backend:8000/api/; # backend service name in your docker-compose or internal network
        proxy_http_version 1.1;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;

        # allow cookies and credentials to pass through
        proxy_set_header Connection "";
    }

    # Optional: admin/media
    location /static/ {
        alias /var/www/forum/static/;
    }

    # Optional: gzip / caching headers for static
    location ~* \.(?:manifest|appcache|html?|xml|json)$ {
        expires -1;
    }
    location ~* \.(?:css|js|woff2?|ttf|svg|png|jpg|jpeg|gif|ico)$ {
        expires 7d;
        add_header Cache-Control "public";
    }
}
```

Production checklist & TLS hints:
- Use Let's Encrypt + Certbot, or a managed TLS certificate (Cloud Load Balancer / CDN).
- Ensure `ssl_certificate` paths are correct and renew with a cron/systemd timer or use the ACME client.
- Consider a CDN (Cloudflare, Fastly, CloudFront) in front of nginx for caching and DDoS protection.
- Ensure backend sees the original client IP by passing `X-Forwarded-For` and configuring Django `SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')` and `USE_X_FORWARDED_HOST = True`.

---

## What I changed / added to the canvas

I added the following to the scaffold document:
- Backend: `api/auth_views.py` code, instructions to add URL routes and settings suggestions.
- Frontend: full `src/api.js` replacement implementing refresh logic and examples for login/bootstrap.
- Nginx `conf.d/forum.conf` example with TLS and proxy config and production checklist.

If you'd like, I can (pick any):
- Apply these changes directly into the repo files in the canvas and produce a ZIP you can download.
- Add an `nginx` service to `docker-compose.yml` and update the frontend backend images to work behind nginx.
- Implement rotating refresh tokens and revoke-list support (requires DB-backed token store).

Which of those should I do next?"
