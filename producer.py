from pika import BlockingConnection, ConnectionParameters

connection_params = ConnectionParameters(
    host='localhost',
    port=5672
)


def main():
    """Основная функция отправки сообщений."""
    with BlockingConnection(connection_params) as connection:
        with connection.channel() as channel:
            channel.queue_declare(queue='messages')
            channel.basic_publish(
                exchange='',  # дефолтная очередь
                routing_key='messages',
                body='Тестовое сообщение RabbitMQ.'
            )
            print('Сообщение отправлено.')


if __name__ == '__main__':
    main()
