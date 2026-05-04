# proyecto_pipeline_elt_mongodb_airflow_dbt
Implementación de un pipeline ELT completo con MongoDB como fuente, Airflow para orquestación y dbt para transformaciones en un warehouse Postgres, siguiendo arquitectura moderna de datos

# Modern Data Stack Project (MongoDB + Airflow + dbt + Postgres)

## Arquitectura
MongoDB → Airflow → Postgres → dbt → Analytics

## Stack
- MongoDB (fuente)
- Airflow (orquestación)
- Postgres (warehouse)
- dbt (transformación)
- Docker (infraestructura)

## Cómo ejecutar

docker-compose up -d

Abrir Airflow:
http://localhost:8080

## DAG
modern_elt_pipeline

## Flujo
1. Extrae datos de MongoDB
2. Carga a Postgres (raw)
3. dbt transforma datos
4. Genera tabla analítica

## Resultado
Tabla: fact_user_spending 
ejemplo de result en el archivo doc_insertar_datos_y_bash.txt

