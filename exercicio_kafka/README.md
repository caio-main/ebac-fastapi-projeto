# Exercício: Orquestração de Apache Kafka com Docker Compose

Este projeto disponibiliza um ambiente local completo com Apache Kafka, ZooKeeper e Kafka-UI utilizando Docker Compose.

## Serviços Configurados
* **ZooKeeper:** Gerenciador de cluster e estado do Kafka.
* **Kafka:** Broker principal de mensagens e streaming de eventos.
* **Kafka-UI:** Interface web para visualização e gerenciamento do cluster.

## Como Executar

Acesse a pasta do exercício e inicie os containers em segundo plano:

bash
cd exercicio_kafka
docker-compose up -d

Após subir os containers, acesse o painel visual no seu navegador:
* **URL:** http://localhost:8080