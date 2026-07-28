# RAG Agent

Agente desarrollado en Python para responder preguntas sobre los principios fundamentales y la estructura organizativa que rigen la Asociacion de Guias y Scouts de Chile. Consulta los estatutos para conocer las bases legales y normativas que nos guían.
Ademas, Accede al reglamento que detalla las normas y procedimientos para el funcionamiento de nuestra organizacion. Encuentra toda la información necesaria para cumplir con nuestras directrices.

## Tecnologías

- Python
- FastAPI
- FAISS
- Sentence Transformers
- LM Studio
- Docker

## Instalación

pip install -r requirements.txt

## Ejecutar

uvicorn app.main:app --reload

## Endpoint

POST /ask

{
   "question":"..."
}
"# Alura" 
