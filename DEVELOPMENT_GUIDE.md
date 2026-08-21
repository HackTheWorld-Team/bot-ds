# Desarrollo - ATLAS Discord Bot

## Estructura del Proyecto

```
atlas-discord-bot/
├── main.py              # Punto de entrada del bot
├── bot/
│   ├── __init__.py
│   ├── config/          # Configuración y variables de entorno
│   ├── database/        # Capa de base de datos
│   ├── models/          # Modelos de SQLAlchemy
│   ├── services/        # Servicios de lógica de negocio
│   ├── cogs/            # Cogs (command groups)
│   └── utils/           # Utilidades diversas
├── .github/workflows/    # Flujos de CI/CD
├── CHANGELOG.md         # Registro de cambios
├── requirements.txt     # Dependencias del proyecto
└── README.md            # Documentación de setup inicial
```

## Configuración del Entorno de Desarrollo

1. **Clonar el repositorio**
   ```bash
   git clone https://github.com/HackTheWorld-Team/bot-ds.git
   cd bot-ds
   ```

2. **Crear entorno virtual**
   ```bash
   python -m venv venv
   .\venv\Scripts\activate
   ```

3. **Instalar dependencias**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configurar variables de entorno**
   ```powershell
   Copy-Item .env.example .env
   ```
   Editar `.env` y completar:
   - `DISCORD_TOKEN` - Token del bot de Discord
   - `DISCORD_GUILD_ID` - ID del servidor de prueba
   - `GITHUB_URL` - URL del repositorio

5. **Ejecutar el bot**
   ```bash
   python main.py
   ```

## Añadir Nuevas Funcionalidades

### Crear un nuevo Cog

1. Crear un nuevo archivo en `bot/cogs/` siguiendo el patrón existente
2. El cog debe heredar de `commands.Cog` o usar el patrón de `setup_hook`
3. Registrar el cog en `main.py` dentro de `setup_hook()`:
   ```python
   await bot.load_extension("bot.cogs.nuevo_cog")
   ```

### Convenções de Código

- Usar typing completo (type hints)
- Seguir el estilo de PEP 8
- Documentar funciones con docstrings
- Usar logging en lugar de print()
- Mantener los handlers de rotación de logs configurados como en `main.py`

### Estilo de Commits

Usar [Conventional Commits](https://www.conventionalcommits.org/):
```
<tipo>(<ámbito>): <descripción>

[Opcional: cuerpo]

[Opcional: pie de página]

Tipos:
- feat: nueva funcionalidad
- fix: corrección de bug
- docs: documentación
- style: formato, missing semi, etc.
- refactor: refactorización
- test: añadir pruebas
- chore: tareas menores
```

## Workflow de Git

1. Crear una rama para la nueva funcionalidad: `git checkout -b feature/nombre-caracteristica`
2. Realizar commits con mensajes convencionales
3. Hacer push a la rama
4. Abrir un Pull Request contra `main`

## Testing

- Verificar que el código pase el lint: `ruff check .`
- Ejecutar análisis estático: `python -m compileall -q main.py bot`
- Probar que los comandos slash funcionen después de sincronizar

## Deploy

El flujo CI/CD se encarga de:
- Escanear secretos con Gitleaks
- Verificar quality con Ruff y Bandit
- Auditar dependencias con pip-audit