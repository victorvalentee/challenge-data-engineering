# Remover arquivos de saída do ETL
rm -rf ./etl/output/categorical
rm -rf ./etl/output/final

# Remover containers ativos gerados pelo docker-compose
docker compose down

# Construir imagens, baixar dependências e subir containers
docker compose build
docker compose up