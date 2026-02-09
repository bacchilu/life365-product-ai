# life365-product-ai

Build a backend service that allows users to ask natural-language questions about the Life365 product catalog, using semantic search + LLMs, with asynchronous ingestion and clean architecture.

## What the System Does

### Ingest Life365 data

- Fetch category tree
- Fetch products for each level_3 category
- Normalize product data

### Index products

- Convert products into vector embeddings
- Store them in a vector database
- Attach metadata (category, brand, language, etc.)

### Answer questions

- Accept a natural language question
- Retrieve relevant products
- Ask an LLM to generate an answer grounded in retrieved data

### Run asynchronously

- Ingestion and indexing happen via Celery
- API remains responsive

## High Level Architecture

### Backend

- FastAPI
- Clean Architecture layers (routers, services, domain, infrastructure)

### Async processing

- Celery
- RabbitMQ

### AI / Search

- LlamaIndex for orchestration
- Embeddings (OpenAI or Free/local LLM)

### Infra

- Docker
- docker-compose
