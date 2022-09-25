import json
from datetime import datetime
from hashlib import sha256


class Blockchain(object):

    def __init__(self):
        self.chain = []  # начальнуя пустая цепочка списков (для хранения цепочки блоков)
        self.pending_transactions = []  # список задержанных транзакций
        # Создает блок генезиса
        print("Creating genesis block")
        self.new_block()

    def new_block(self, previous_hash=None):  # Генерирует новый блок и добавляет его в цепь
        block: dict = {'index': len(self.chain), 'timestamp': datetime.utcnow().isoformat(),
                       'transactions': self.pending_transactions, 'previous_hash': previous_hash,
                       'nonce': None}
        # Возвращает хэш этого нового блока и добавляет его в блок
        block_hash = self.hash(block)
        block["hash"] = block_hash
        # Сбрасывает список незавершенных транзакций
        self.pending_transactions = []
        # Добавляет блок в цепочку
        self.chain.append(block)
        print(f"Created block {block['index']}")
        return block

    @staticmethod
    def hash(block):  # Хэширование (sha256 дайджест) блока, который в json формате
        block_string: bytes = json.dumps(block, sort_keys=True).encode()
        return sha256(block_string).hexdigest()

    def last_block(self):  # Возвращает последний блок в цепочке (если есть блоки)
        return self.chain[-1] if self.chain else None

    def new_transaction(self, sender, recipient, amount):  # добавляет новую транзакцию в список задержанных транзакций
        self.pending_transactions.append({
            "recipient": recipient, "sender": sender, "amount": amount,
        })

    def proof_of_work(self):
        pass

    def valid_hash(self):
        pass

