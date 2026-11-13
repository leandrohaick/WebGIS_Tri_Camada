# WebGIS Ambiental

Mapa interativo das áreas protegidas, corredores ecológicos e pontos ambientais da Região Metropolitana de Belém.

## Recursos

- Alternância, enquadramento e controle de opacidade das camadas vetoriais.
- Pesquisa por atributos (nome, categoria, responsável e descrição), com destaque no mapa.
- Tabela de atributos da camada selecionada e indicadores de área, extensão e quantidade.
- Medição de distância e área diretamente no mapa.
- Criação de buffers em quilômetros a partir de um clique.
- Dados locais em `data/*.geojson`, sem necessidade de banco para explorar o mapa.

## Uso

Abra o endereço publicado e use o painel lateral para ativar as camadas. Clique nas feições para consultar seus atributos. Na seção **Geoprocessamento**, escolha uma ferramenta e clique no mapa para executar a análise. A API Flask/PostGIS continua disponível para ambientes que tenham o banco configurado.

## Autor

Leandro Haick
