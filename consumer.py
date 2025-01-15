from pika import BlockingConnection, ConnectionParameters

connection_params = ConnectionParameters(
    host='localhost',
    port=5672
)


def process_manager(channel, method, properties, body):
    """Функция обработки сообщения."""
    print(f'Получено сообщение: {body.decode()}.')
    # подтверждение обработки сообщения
    channel.basic_ack(delivery_tag=method.delivery_tag)


def main():
    """Основная функция приёма сообщений."""
    with BlockingConnection(connection_params) as connection:
        with connection.channel() as channel:
            channel.queue_declare(queue='messages')
            channel.basic_consume(
                queue='messages',
                on_message_callback=process_manager
            )
            print('Ожидание сообщений.')
            channel.start_consuming()


if __name__ == '__main__':
    main()
