class Blockchain(object):

    def __init__(self):
        self.chain = []  # начальнуя пустая цепочка списков (для хранения цепочки блоков)
        self.pending_transactions = []  # список задержанных транзакций

    def new_block(self):  # Генерирует новый блок и добавляет его в цепь
        return None  # FIXME

    @staticmethod
    def hash(block):  # Hashes a Block pass
        return None  # FIXME

    def last_block(self):  # Получает последний блок в проходе цепочки
        return None  # FIXME

    def new_transaction(self, sender, recipient, amount):  # добавляет новую транзакцию в список задержанных транзакций
        self.pending_transactions.append({
            "recipient": recipient, "sender": sender, "amount": amount,
        })
