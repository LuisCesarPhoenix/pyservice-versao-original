# send_test_message.py

from src.utils.rabbitmq_utils import publish_message

def send_test():
    # Mensagem de teste (ajuste o caminho conforme necessário)
    message = {
        "file_path": "work/teste_arquivo.csv"
    }

    publish_message(message)

if __name__ == "__main__":
    send_test()
