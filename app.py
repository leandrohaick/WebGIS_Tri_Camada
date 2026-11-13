import json
import os
from typing import Any

import psycopg2
from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS


app = Flask(__name__)
CORS(app)


DB_CONFIG = {
    "host": os.getenv("POSTGIS_HOST", "localhost"),
    "port": os.getenv("POSTGIS_PORT", "5432"),
    "dbname": os.getenv("POSTGIS_DB", "geodb"),
    "user": os.getenv("POSTGIS_USER", "postgres"),
    "password": os.getenv("POSTGIS_PASSWORD", "postgres"),
}


@app.get("/")
def index() -> Any:
    """Entrega a aplicação web quando o Flask é executado diretamente."""
    return send_from_directory(".", "index.html")


@app.get("/data/<path:filename>")
def data_files(filename: str) -> Any:
    """Serve os arquivos GeoJSON locais usados no fallback de demonstração."""
    return send_from_directory("data", filename)


def consultar_geojson(query: str) -> dict[str, Any]:
    """Executa uma consulta espacial e monta uma FeatureCollection GeoJSON."""
    features = []
    with psycopg2.connect(**DB_CONFIG) as connection:
        with connection.cursor() as cursor:
            cursor.execute(query)
            for properties, geometry in cursor.fetchall():
                features.append(
                    {
                        "type": "Feature",
                        "geometry": json.loads(geometry),
                        "properties": properties,
                    }
                )

    return {"type": "FeatureCollection", "features": features}


@app.get("/api/saude")
def health() -> tuple[Any, int]:
    try:
        with psycopg2.connect(**DB_CONFIG) as connection:
            with connection.cursor() as cursor:
                cursor.execute("SELECT PostGIS_Full_Version()")
                version = cursor.fetchone()[0]
        return jsonify({"status": "ok", "postgis": version})
    except psycopg2.Error as error:
        return jsonify({"status": "erro", "mensagem": str(error)}), 503


@app.get("/api/poligonos")
def get_poligonos() -> tuple[Any, int]:
    try:
        data = consultar_geojson(
            """
            SELECT jsonb_build_object(
                       'id', id, 'nome', nome, 'categoria', categoria,
                       'area_km2', area_km2, 'descricao', descricao
                   )::text,
                   ST_AsGeoJSON(geom)
            FROM areas_protegidas
            ORDER BY nome
            """
        )
        data["features"] = [
            {**feature, "properties": json.loads(feature["properties"])}
            for feature in data["features"]
        ]
        return jsonify(data)
    except psycopg2.Error as error:
        return jsonify({"erro": "Não foi possível consultar os polígonos.", "detalhe": str(error)}), 500


@app.get("/api/linhas")
def get_linhas() -> tuple[Any, int]:
    try:
        data = consultar_geojson(
            """
            SELECT jsonb_build_object(
                       'id', id, 'nome', nome, 'categoria', categoria,
                       'extensao_km', extensao_km, 'descricao', descricao
                   )::text,
                   ST_AsGeoJSON(geom)
            FROM corredores_ecologicos
            ORDER BY nome
            """
        )
        data["features"] = [
            {**feature, "properties": json.loads(feature["properties"])}
            for feature in data["features"]
        ]
        return jsonify(data)
    except psycopg2.Error as error:
        return jsonify({"erro": "Não foi possível consultar as linhas.", "detalhe": str(error)}), 500


@app.get("/api/pontos")
def get_pontos() -> tuple[Any, int]:
    try:
        data = consultar_geojson(
            """
            SELECT jsonb_build_object(
                       'id', id, 'nome', nome, 'categoria', categoria,
                       'responsavel', responsavel, 'descricao', descricao
                   )::text,
                   ST_AsGeoJSON(geom)
            FROM pontos_ambientais
            ORDER BY nome
            """
        )
        data["features"] = [
            {**feature, "properties": json.loads(feature["properties"])}
            for feature in data["features"]
        ]
        return jsonify(data)
    except psycopg2.Error as error:
        return jsonify({"erro": "Não foi possível consultar os pontos.", "detalhe": str(error)}), 500


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
