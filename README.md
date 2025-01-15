## Описание

Мини-проект по работе с RabbitMQ.

#### Технологии

- Python 3.9
- RabbitMQ
- pika

#### Локальный запуск проекта

- Предварительно необходимо установить RabbitMQ для вашей системы.

- Включите RabbitMQ Management Plugin:

```bash
rabbitmq-plugins enable rabbitmq_management
```

- Интерфейс управления RabbitMQ будет доступен по адресу:

```bash
http://localhost:15672/
```

#### Запуск проекта на удаленном сервере

- Предварительно необходимо установить Docker и docker-compose на удаленном сервере.

- Cоздать файл docker-compose.yml c кодом по образцу.

- Интерфейс управления RabbitMQ будет доступен по адресу:

```bash
http://<ip>:15672/
```
