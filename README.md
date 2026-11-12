# Fornos para a cozinha

Site estático (nginx) para comparar fornos. Veja CONTEXTO.md.

## Deploy
    git clone https://github.com/herbertsds/fornos && cd fornos
    docker network ls            # descubra a rede do Nginx Proxy Manager
    NPM_NETWORK=<rede> docker compose up -d --build

No NPM: Proxy Host -> Forward Hostname `fornos`, porta `80`, SSL Let's Encrypt.
