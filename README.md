# WebGIS Ambiental

Painel cartográfico ambiental das áreas protegidas, corredores ecológicos e pontos ambientais da Região Metropolitana de Belém.

A apresentação usa um layout mapa-em-primeiro-plano, com viewport fixo e painel compacto, evitando rolagem da página durante a demonstração.

## Recursos

- Alternância, enquadramento e controle de opacidade das camadas vetoriais.
- Pesquisa por atributos (nome, categoria, responsável e descrição), com destaque no mapa.
- Tabela de atributos da camada selecionada e indicadores de área, extensão e quantidade.
- Medição de distância e área diretamente no mapa.
- Criação de buffers em quilômetros a partir de um clique.
- A aplicação consulta prioritariamente os endpoints Flask/PostGIS (`/api/poligonos`, `/api/linhas` e `/api/pontos`) e usa `data/*.geojson` apenas como fallback para demonstração sem banco.

## Uso

Execute `python app.py` e abra `http://127.0.0.1:5000`. Use o painel lateral para ativar as camadas. Clique nas feições para consultar seus atributos. Na seção **Geoprocessamento**, escolha uma ferramenta e clique no mapa para executar a análise. Com PostGIS configurado, as camadas são carregadas pelos três endpoints da API; sem banco, o fallback local mantém a demonstração navegável.

## Autor

Leandro Haick
