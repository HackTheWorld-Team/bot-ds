# ATLAS Discord Bot

ATLAS es un bot centralizado para la comunidad HackTheWorld.

Actualmente se encuentra en fase de MVP y está diseñado para crecer de forma modular a medida que se incorporen nuevas funciones.

## Estado actual

Funciones implementadas:

- `/ping` — Comprueba si ATLAS está funcionando.
- `/github` — Muestra el repositorio oficial de la comunidad.
- `/ayuda` — Muestra los comandos disponibles.

## Base técnica

El proyecto actualmente utiliza:

- Python
- discord.py
- SQLAlchemy
- SQLite
- python-dotenv
- Git y GitHub

## Configuración local

1. Crear un entorno virtual.
2. Instalar las dependencias:

```bash
pip install -r requirements.txt

```

3. Copiar el archivo de ejemplo:

```powershell
Copy-Item .env.example .env
```

4. Abrir `.env` y completar las variables:

```text
DISCORD_TOKEN=TU_TOKEN_REAL
DISCORD_GUILD_ID=TU_ID_DE_SERVIDOR
GITHUB_URL=https://github.com/HackTheWorld-Team/bot-ds
```

5. Ejecutar ATLAS:

```powershell
python main.py
```
