# traefik-inwx

Træfik, a modern reverse proxy with INWX api support for DNS challenge

## Test INWX api

```
docker build -t traefik:inwx .
docker run --rm -e INWX_USER="$INWX_USER" -e INWX_PASSWORD="$INWX_PASSWORD" traefik:inwx /opt/acme.py present _acme-challenge.example.com. 3Aqn46_JLMB7IUxBegBURt6_iEOAX20KGEygi1lnbeM 120
docker run --rm -e INWX_USER="$INWX_USER" -e INWX_PASSWORD="$INWX_PASSWORD" traefik:inwx /opt/acme.py cleanup _acme-challenge.example.com. 3Aqn46_JLMB7IUxBegBURt6_iEOAX20KGEygi1lnbeM 120
```
