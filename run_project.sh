# Color codes para output colorido no terminal
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
NC='\033[0m'


# Verificar se o docker engine está rodando
if ! docker ps > /dev/null 2>&1; then
  echo "O docker engine precisa estar rodando para executar esse script."
  echo -e "${RED}Por favor, inicie o docker e tente novamente!${NC}"
  exit 1
fi


# Remover arquivos de saída do ETL
echo -e "\n\n${GREEN}Excluindo arquivos parquet criados em execuções prévias ...${NC}"
rm -rf ./etl/output


# Remover containers ativos gerados pelo docker-compose
echo -e "${GREEN}Excluindo containers criados em execuções prévias pelo 'docker compose' ...${NC}\n\n"
docker compose down --remove-orphans --volumes


# Construir imagens, baixar dependências e subir containers
echo -e "\n\n${GREEN}Baixando e construindo as imagens docker ...${NC}\n\n"
docker compose build


# Subir containers e inicializar Airflow
echo -e "\n----------------------------------\n\n${YELLOW}Inicalizando Airflow...${NC}"
echo -e "${YELLOW}A DAG irá rodar automaticamente após o airflow-webserver ser inicializado.${NC}\n\n"
docker compose up -d


# Excluir containers após 1h
echo -e "\n----------------------------------\n\n${YELLOW}Daqui a alguns minutos você poderá acessar o dashboard do airflow no seguinte link:${NC}"
echo "http://localhost:8080"
echo -e "${YELLOW}user: ${RED}airflow${NC}\n${YELLOW}password: ${RED}airflow${NC}"
echo -e "\n\n----------------------------------\n\n${YELLOW}Os containers serão destruidos após ${RED}1 hora${YELLOW}, caso você não o faça manualmente.${NC}\n\n"
sleep 1h && docker compose down --remove-orphans --volumes
