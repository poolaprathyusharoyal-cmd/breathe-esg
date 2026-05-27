# MODEL

The application uses an EmissionRecord model to store uploaded emission data.

Fields:
- source
- category
- amount
- unit
- status

The model supports ingestion of fuel, electricity, and travel emission data.

Django ORM is used for database management and normalization.

The system is designed as a prototype for enterprise ESG emission tracking.