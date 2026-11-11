-- WebGIS Ambiental Tri-Camada
-- Banco esperado: geodb | SRID: EPSG:4326 (WGS 84)
CREATE EXTENSION IF NOT EXISTS postgis;

DROP TABLE IF EXISTS pontos_ambientais, corredores_ecologicos, areas_protegidas CASCADE;

CREATE TABLE areas_protegidas (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(120) NOT NULL,
    categoria VARCHAR(80) NOT NULL,
    area_km2 NUMERIC(10, 2) NOT NULL,
    descricao TEXT,
    geom geometry(MultiPolygon, 4326) NOT NULL
);

CREATE TABLE corredores_ecologicos (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(120) NOT NULL,
    categoria VARCHAR(80) NOT NULL,
    extensao_km NUMERIC(10, 2) NOT NULL,
    descricao TEXT,
    geom geometry(MultiLineString, 4326) NOT NULL
);

CREATE TABLE pontos_ambientais (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(120) NOT NULL,
    categoria VARCHAR(80) NOT NULL,
    responsavel VARCHAR(120),
    descricao TEXT,
    geom geometry(Point, 4326) NOT NULL
);

INSERT INTO areas_protegidas (nome, categoria, area_km2, descricao, geom) VALUES
('Parque Ambiental de Ananindeua', 'Parque urbano', 1.85, 'Área demonstrativa para validação do WebGIS.',
 ST_GeomFromText('MULTIPOLYGON(((-48.390 -1.365, -48.375 -1.365, -48.375 -1.350, -48.390 -1.350, -48.390 -1.365)))', 4326)),
('Área de Proteção do Igarapé Maguari', 'Proteção de margem', 3.40, 'Faixa de proteção ambiental do igarapé.',
 ST_GeomFromText('MULTIPOLYGON(((-48.475 -1.330, -48.450 -1.330, -48.450 -1.310, -48.475 -1.310, -48.475 -1.330)))', 4326));

INSERT INTO corredores_ecologicos (nome, categoria, extensao_km, descricao, geom) VALUES
('Corredor Guajará-Maguari', 'Conexão hídrica', 8.20, 'Traçado demonstrativo para a camada de linhas.',
 ST_GeomFromText('MULTILINESTRING((-48.500 -1.300, -48.480 -1.315, -48.455 -1.330, -48.430 -1.350))', 4326)),
('Ciclorrota Verde Metropolitana', 'Mobilidade sustentável', 5.70, 'Rota demonstrativa de mobilidade não motorizada.',
 ST_GeomFromText('MULTILINESTRING((-48.420 -1.390, -48.405 -1.375, -48.390 -1.360, -48.370 -1.345))', 4326));

INSERT INTO pontos_ambientais (nome, categoria, responsavel, descricao, geom) VALUES
('Ponto de coleta seletiva Cidade Nova', 'Coleta seletiva', 'Prefeitura de Ananindeua', 'Local demonstrativo de entrega voluntária.',
 ST_SetSRID(ST_Point(-48.395, -1.365), 4326)),
('Viveiro municipal', 'Reflorestamento', 'Secretaria de Meio Ambiente', 'Produção de mudas nativas.',
 ST_SetSRID(ST_Point(-48.415, -1.350), 4326)),
('Estação de monitoramento do ar', 'Monitoramento', 'UFPA', 'Ponto demonstrativo de monitoramento ambiental.',
 ST_SetSRID(ST_Point(-48.455, -1.325), 4326));

CREATE INDEX areas_protegidas_geom_gix ON areas_protegidas USING GIST (geom);
CREATE INDEX corredores_ecologicos_geom_gix ON corredores_ecologicos USING GIST (geom);
CREATE INDEX pontos_ambientais_geom_gix ON pontos_ambientais USING GIST (geom);
