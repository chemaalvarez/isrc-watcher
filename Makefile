# VARIABLES
FRONTEND_DIR=frontend
FRONTEND_PORT=5173

# DEFAULT
.PHONY: help
help:
	@echo "Comandos disponibles:"
	@echo "  make dev         → Inicia el frontend en modo desarrollo"
	@echo "  make lint        → Ejecuta ESLint"
	@echo "  make format      → Ejecuta Prettier"
	@echo "  make build       → Compila el frontend"
	@echo "  make start       → Arranca el backend (cuando lo tengas)"
	@echo "  make deploy      → Despliegue (placeholder)"
	@echo "  make clean       → Elimina carpetas de compilación"

# FRONTEND
.PHONY: dev
dev:
	cd $(FRONTEND_DIR) && npm run dev -- --port $(FRONTEND_PORT)

.PHONY: build
build:
	cd $(FRONTEND_DIR) && npm run build

.PHONY: lint
lint:
	cd $(FRONTEND_DIR) && npx eslint src --ext .js,.jsx

.PHONY: format
format:
	cd $(FRONTEND_DIR) && npx prettier --write "src/**/*.{js,jsx,css}"

# BACKEND
.PHONY: start
start:
	@echo "Iniciar el backend aquí (por ejemplo: uvicorn main:app --reload)"

# DEPLOY
.PHONY: deploy
deploy:
	@echo "Aquí iría el script de despliegue"

# CLEAN
.PHONY: clean
clean:
	cd $(FRONTEND_DIR) && rm -rf dist
