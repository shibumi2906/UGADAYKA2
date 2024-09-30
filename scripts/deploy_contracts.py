import subprocess
import os
from pathlib import Path

# Пути к контрактам
CONTRACTS_DIR = Path(__file__).parent / "../contracts"
BUILD_DIR = CONTRACTS_DIR / "build"
IDEA_CONTRACT_PATH = BUILD_DIR / "IdeaToken.tvc"
MATTER_CONTRACT_PATH = BUILD_DIR / "MatterToken.tvc"

# Адреса получателей контрактов (например, кошелек)
DESTINATION_ADDRESS = "EQ...your_ton_address..."  # Заменить на реальный адрес


def deploy_contract(contract_path, destination_address):
    """
    Функция для развертывания смарт-контракта на блокчейне TON.
    :param contract_path: Путь к скомпилированному контракту (tvc).
    :param destination_address: Адрес получателя контракта.
    """
    try:
        # Используем Fift для отправки контракта в сеть
        print(f"Развертывание контракта: {contract_path.name} на адрес {destination_address}")

        # Команда развертывания контракта через Fift или аналогичный инструмент
        result = subprocess.run(
            [
                "toncli", "sendfile",
                str(contract_path),
                destination_address
            ],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        print(f"Результат: {result.stdout.decode('utf-8')}")
        return True

    except subprocess.CalledProcessError as e:
        print(f"Ошибка при развертывании контракта: {contract_path.name}")
        print(e.stderr.decode('utf-8'))
        return False


def main():
    # Проверяем наличие скомпилированных контрактов
    if not IDEA_CONTRACT_PATH.exists() or not MATTER_CONTRACT_PATH.exists():
        print("Скомпилированные контракты не найдены. Выполните компиляцию.")
        return

    # Развертывание контрактов для токенов Идея и Материя
    deploy_contract(IDEA_CONTRACT_PATH, DESTINATION_ADDRESS)
    deploy_contract(MATTER_CONTRACT_PATH, DESTINATION_ADDRESS)


if __name__ == "__main__":
    main()
