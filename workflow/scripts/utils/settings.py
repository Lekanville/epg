from environs import Env

# Loads environmental variables from .env
env = Env()
env.read_env()

import_dir = env("NEO4J_IMPORT_DIR", "test/neo4j/import")
snakemake_logs = env("SNAKEMAKE_LOGS", "test/results/logs")
data_dir = env("DATA_DIR", "test/source_data")
processing_dir = env("PROCESSING_DIR", "test/scripts/processing")
log_dir = env("NEO4J_LOG_DIR", "test/neo4j/0.0.1/logs")
graph_dir = env("GRAPH_DIR", "test/results/graph_data")
server_name = env("SERVER_NAME", None)
graph_version = env("GRAPH_VERSION","0.0.1")
container_name = env("GRAPH_CONTAINER_NAME","neo4j-pipeline-demo-graph")
config_path = env("CONFIG_PATH","test/config")
threads = env("THREADS", 4)

graph_bolt = env("GRAPH_BOLT_PORT","7687")
graph_pass = env("GRAPH_PASSWORD","neo4j")
graph_user = env("GRAPH_USER","neo4j")
graph_host = env("GRAPH_HOST","localhost")

env_configs = {
    "import_dir": import_dir,
    "snakemake_logs": snakemake_logs,
    "data_dir": data_dir,
    "processing_dir": processing_dir,
    "log_dir": log_dir,
    "graph_dir": graph_dir,
    "server_name": server_name,
    "graph_version": graph_version,
    "graph_bolt": graph_bolt,
    "graph_pass": graph_pass,
    "graph_user": graph_user,
    "graph_host": graph_host,
    "container_name": container_name,
    "config_path": config_path,
    "threads": threads,
}
