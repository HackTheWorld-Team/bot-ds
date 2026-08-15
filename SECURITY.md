# Política de Seguridad de ATLAS

ATLAS se toma la seguridad en serio. Este documento describe cómo reportar
vulnerabilidades y los estándares que todo colaborador debe cumplir.

## Reporte de vulnerabilidades

**No abras un issue público para reportar vulnerabilidades.**

Contacta al equipo de forma privada:

- Correo: (pendiente de configurar — usa el canal privado del equipo)
- Usuario de contacto en GitHub: `ranto-dev05`

Al reportar, incluye:

1. Descripción del impacto.
2. Pasos para reproducir (sin exponer datos reales).
3. Versión/commit afectado.
4. Sugerencia de mitigación si la tienes.

El equipo responderá en un plazo razonable. Mientras la vulnerabilidad esté
abierta, **no la divulgues públicamente**.

## Alcance

Se consideran dentro de alcance:

- Fuga de secretos (tokens, claves, credenciales).
- Inyección o manipulación de datos (SQL, comandos, etc.).
- Fuga de información privilegiada o PII.
- Ejecución remota de código o abuso de privilegios.
- Dependencias con vulnerabilidades conocidas.

## Estándares de codificación segura

Reglas obligatorias para contribuir al repositorio:

1. **Secretos nunca van en el código.** Todo valor sensible se lee desde
   variables de entorno (`.env` local) y jamás se imprime, loguea ni hardcodea.
   El token de Discord NUNCA debe aparecer en mensajes, logs, commits o issues.
2. **`.env` no se trackea.** Solo se versiona `.env.example` con valores de
   ejemplo (`TU_TOKEN_AQUI`, etc.). Nunca pongas valores reales en `.env.example`.
3. **Pre-commit:** instala y ejecuta los hooks de `.pre-commit-config.yaml`
   (gitleaks + ruff). Los commits con secretos serán rechazados por CI
   (job `secrets` de GitHub Actions).
4. **PR a `main`:** `main` está protegido. Todo cambio entra por PR con al
   menos 1 revisión aprobada y los checks de CI en verde
   (`secrets`, `quality`, `dependencies`).
5. **Dependencias:** no añadas dependencias sin necesidad. Mantén
   `requirements.txt` con versiones fijadas. Dependabot abre PRs de
   actualización: revísalos y meréalos.
6. **Logs:** no registres datos sensibles (tokens, contraseñas, IDs de
   usuarios si no son necesarios). El nivel por defecto es `INFO`.

## Proceso para reportar y parchear

1. Reporta la vulnerabilidad en privado (ver arriba).
2. El equipo prioriza (Severidad CVSS) y coordina el parche.
3. El parche se realiza en una rama, pasa por CI de seguridad y se mergea con
   revisión a `main`.
4. Se comunica la divulgación responsable una vez publicado.
