from flask import Flask, jsonify, request
from core.API.ton_api import TonAPI
from core.API.exchange_api import ExchangeAPI
from core.services.portfolio_service import PortfolioService
from core.services.trading_service import TradingService
from core.services.transaction_service import TransactionService

app = Flask(__name__)

# Инициализация сервисов
portfolio_service = PortfolioService()
exchange_api = ExchangeAPI()  # Инициализация реального API бирж
ton_api = TonAPI("your_wallet_address", "your_private_key")  # Настройки для API TON
trading_service = TradingService(exchange_api, portfolio_service)
transaction_service = TransactionService(ton_api)

# Главный маршрут для API
@app.route('/api', methods=['GET'])
def index():
    return jsonify({"message": "Добро пожаловать в трейдинговую систему API!"}), 200

# Маршрут для получения портфеля пользователя
@app.route('/api/portfolio/<int:user_id>', methods=['GET'])
def get_portfolio(user_id):
    token_id = request.args.get("token_id")
    if not token_id:
        return jsonify({"error": "Token ID is required"}), 400

    balance = portfolio_service.get_balance(user_id, token_id)
    return jsonify({"user_id": user_id, "token_id": token_id, "balance": balance}), 200

# Маршрут для размещения ставки
@app.route('/api/trade', methods=['POST'])
def place_trade():
    data = request.get_json()

    if not all(k in data for k in ("user_id", "token_id", "amount", "trend")):
        return jsonify({"error": "Missing required fields"}), 400

    try:
        bet_info = trading_service.place_bet(data["user_id"], data["token_id"], data["amount"], data["trend"])
        return jsonify(bet_info), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Маршрут для создания транзакции
@app.route('/api/transaction', methods=['POST'])
def create_transaction():
    data = request.get_json()

    if not all(k in data for k in ("user_id", "to_address", "token_id", "amount")):
        return jsonify({"error": "Missing required fields"}), 400

    try:
        transaction_record = transaction_service.create_transaction(data["user_id"], data["to_address"],
                                                                    data["token_id"], data["amount"])
        return jsonify(transaction_record), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True)
