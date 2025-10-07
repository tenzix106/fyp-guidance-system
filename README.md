# test-project

This template should help get you started developing with Vue 3 in Vite.

## Recommended IDE Setup

[VS Code](https://code.visualstudio.com/) + [Vue (Official)](https://marketplace.visualstudio.com/items?itemName=Vue.volar) (and disable Vetur).

## Recommended Browser Setup

- Chromium-based browsers (Chrome, Edge, Brave, etc.):
  - [Vue.js devtools](https://chromewebstore.google.com/detail/vuejs-devtools/nhdogjmejiglipccpnnnanhbledajbpd) 
  - [Turn on Custom Object Formatter in Chrome DevTools](http://bit.ly/object-formatters)
- Firefox:
  - [Vue.js devtools](https://addons.mozilla.org/en-US/firefox/addon/vue-js-devtools/)
  - [Turn on Custom Object Formatter in Firefox DevTools](https://fxdx.dev/firefox-devtools-custom-object-formatters/)

## Customize configuration

See [Vite Configuration Reference](https://vite.dev/config/).

## Project Setup

```sh
npm install
```

### Compile and Hot-Reload for Development

```sh
npm run dev
```

## Backend (Flask)

A minimal Flask backend is included under `backend/` with two endpoints:

- `GET /api/health` – health check
- `POST /api/generate-fyp-ideas` – accepts `{ "profile": { "interest": string, "coursework": string, "fieldOfStudy": string, "skills": string } }` and returns `{ ideas: [], resources: [] }`.

### Setup and Run (Windows PowerShell)

```powershell
cd backend
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python app.py
```

The backend runs at `http://localhost:5000`.

### Frontend ↔ Backend (Dev Proxy)

The Vite dev server proxies `/api/*` to `http://localhost:5000`. Start both:

```powershell
# Terminal 1 (backend)
cd backend
.\.venv\Scripts\Activate.ps1
python app.py

# Terminal 2 (frontend)
npm run dev
```

### Compile and Minify for Production

```sh
npm run build
```
