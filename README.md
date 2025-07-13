# 🎧 ISRC Watcher

**ISRC Watcher** es una herramienta web diseñada para detectar y vigilar posibles infracciones de copyright sobre canciones mediante análisis de similitud, utilizando tecnologías de inteligencia artificial en audio.

---

## 🚀 Instalación

1. Clona el repositorio:
```bash
git clone https://github.com/chemaalvarez/isrc-watcher.git
cd isrc-watcher
```

2. Instala las dependencias necesarias para desarrollo:
```bash
npm install
```

3. Accede a la carpeta del frontend:
```bash
cd frontend
npm install
```

---

## 💻 Uso

### Frontend

Para iniciar la aplicación de desarrollo:
```bash
npm run dev
```

Esto iniciará el servidor Vite y podrás acceder a la interfaz en `http://localhost:5173`.

### Formateo y linting

Para formatear el código con Prettier:
```bash
npm run format
```

Para ejecutar ESLint:
```bash
npm run lint
```

Para aplicar correcciones automáticas con ESLint:
```bash
npm run lint:fix
```

---

## 🧠 Arquitectura

El proyecto está dividido en dos partes:

- `frontend/`: interfaz de usuario en React + Vite.
- `backend/`: (en construcción) lógica de análisis de similitud y vigilancia de infracciones.

---

## 🧪 Tecnologías

- [React 19](https://reactjs.org/)
- [Vite](https://vitejs.dev/)
- [ESLint](https://eslint.org/)
- [Prettier](https://prettier.io/)
- [Node.js](https://nodejs.org/)

---

## 📦 Estructura del proyecto

```
isrc-watcher/
│
├── frontend/              # Aplicación en React
│   ├── public/
│   ├── src/
│   └── ...
│
├── backend/               # Backend en Node.js/Python (por definir)
│
├── dev.sh                 # Script de desarrollo
├── Makefile               # Tareas automatizadas
├── eslint.config.js       # Configuración moderna de ESLint
├── .prettierignore
├── .prettierrc
└── package.json
```

---

## 📌 Por hacer

- [x] Configurar entorno de desarrollo frontend
- [x] Prettier + ESLint con reglas unificadas
- [ ] Implementar backend de análisis
- [ ] Procesamiento de metadatos (ISRC, YT, Spotify)
- [ ] Dashboard de infracciones

---

## 🧑‍💻 Autor

Creado con 💡 por [Chema Álvarez](https://github.com/chemaalvarez)
