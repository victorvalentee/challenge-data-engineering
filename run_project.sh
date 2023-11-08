# Remover arquivos de saída do ETL
rm -rf ./etl/output

# Remover containers ativos gerados pelo docker-compose
docker compose down

# Construir imagens, baixar dependências e subir containers
docker compose build
docker compose up