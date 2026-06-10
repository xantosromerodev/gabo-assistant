# Gabo Assistant

Asistente virtual para Gabo Podólogo.

## Objetivo

Gabo Assistant es un asistente basado en Inteligencia Artificial diseñado para responder consultas iniciales de pacientes sobre servicios podológicos.

El objetivo principal es brindar orientación básica, resolver preguntas frecuentes y promover la reserva de valoraciones profesionales.

---

## Funcionalidades actuales

* Respuestas conversacionales mediante IA.
* Atención simulada desde consola.
* Prompt especializado para podología.
* Integración con OpenRouter.
* Configuración mediante variables de entorno.

---

## Tecnologías

* Python
* OpenRouter API
* OpenAI SDK
* Python Dotenv

---

## Estructura del proyecto

```bash
gabo-assistant/

├── app.py
├── .env
├── .gitignore
├── requirements.txt
│
├── prompts/
│   └── system_prompt.txt
│
├── tests/
│   └── faq.txt
│
└── README.md
```
---

## Instalación

Crear entorno virtual:

```bash
python -m venv venv
```

Activar entorno:

Windows:

```bash
venv\Scripts\activate
```

Instalar dependencias:

```bash
pip install -r requirements.txt
```

---

## Configuración

Crear archivo .env

```bash
OPENROUTER_API_KEY=TU_API_KEY
```

---

## Ejecución

```bash
python app.py
```

---

## Próximas versiones

* Memoria conversacional.
* Historial de pacientes.
* Base de conocimiento avanzada.
* Integración con WhatsApp.
* Análisis de imágenes.
* Análisis de audio.
* Agenda automática.
* Panel administrativo.

---

## Autor

Proyecto desarrollado por Santos Romero.
