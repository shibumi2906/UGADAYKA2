class TradingService:
    def __init__(self, exchange_api, portfolio_service):
        """
        Инициализация сервиса торговли.
        :param exchange_api: Инстанс API для получения данных с бирж.
        :param portfolio_service: Инстанс сервиса управления портфелем.
        """
        self.exchange_api = exchange_api
        self.portfolio_service = portfolio_service

    def place_bet(self, user_id, token_id, amount, trend):
        """
        Размещение ставки на изменение курса токена.
        :param user_id: ID пользователя.
        :param token_id: ID токена.
        :param amount: Сумма ставки.
        :param trend: "up" (ставка на повышение) или "down" (ставка на понижение).
        """
        balance = self.portfolio_service.get_balance(user_id, token_id)
        if balance < amount:
            raise Exception("Недостаточно средств для ставки.")

        # Получение текущей цены токена
        current_price = self.exchange_api.get_token_price(token_id)

        # Логика обработки ставки
        # Мы можем сохранить информацию о ставке и отслеживать результаты на основе изменений курса
        bet_info = {
            "user_id": user_id,
            "token_id": token_id,
            "amount": amount,
            "trend": trend,
            "initial_price": current_price
        }

        # Сохранение ставки в портфель пользователя
        self.portfolio_service.save_bet(user_id, bet_info)
        return bet_info

    def calculate_profit(self, user_id, bet):
        """
        Рассчитывает доходность на основе завершенной ставки.
        :param user_id: ID пользователя.
        :param bet: Данные о ставке.
        """
        current_price = self.exchange_api.get_token_price(bet["token_id"])
        profit = 0

        if bet["trend"] == "up" and current_price > bet["initial_price"]:
            profit = (current_price - bet["initial_price"]) * bet["amount"]
        elif bet["trend"] == "down" and current_price < bet["initial_price"]:
            profit = (bet["initial_price"] - current_price) * bet["amount"]

        # Обновляем баланс пользователя
        self.portfolio_service.update_balance(user_id, bet["token_id"], profit)
        return profit
