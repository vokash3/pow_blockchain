import json
import random
from datetime import datetime
from hashlib import sha256


class Blockchain(object):

    def __init__(self):
        self.chain = []  # начальнуя пустая цепочка списков (для хранения цепочки блоков)
        self.pending_transactions = []  # список задержанных транзакций
        # Создает блок генезиса
        print("Создание блока Генезиса")
        self.new_block()

    def new_block(self):  # Генерирует новый блок и добавляет его в цепь
        block: dict = {'index': len(self.chain),
                       'timestamp': datetime.utcnow().isoformat(),
                       'transactions': self.pending_transactions,
                       'previous_hash': self.last_block()["hash"] if self.last_block() else None,
                       'nonce': format(random.getrandbits(64), "x")}
        # Возвращает хэш этого нового блока и добавляет его в блок
        block_hash = self.hash(block)
        block["hash"] = block_hash
        # Сбрасывает список незавершенных транзакций
        self.pending_transactions = []
        # Добавляет блок в цепочку
        # self.chain.append(block)
        # print(f"Создан блок {block['index']}")
        return block

    @staticmethod
    def hash(block):  # Хэширование (sha256 дайджест) блока, который в json формате
        # словарь отсортирован, иначе у нас будут несогласованные хэши
        block_string: bytes = json.dumps(block, sort_keys=True).encode()
        return sha256(block_string).hexdigest()

    def last_block(self):  # Возвращает последний блок в цепочке (если есть блоки)
        return self.chain[-1] if self.chain else None

    def new_transaction(self, sender, recipient, amount):  # добавляет новую транзакцию в список задержанных транзакций
        self.pending_transactions.append({
            "recipient": recipient, "sender": sender, "amount": amount,
        })

    def proof_of_work(self): # генерируем блоки, пока не получим хэш с 4-мя нулями в начале
        while True:
            new_block = self.new_block()
            if self.valid_hash(new_block):
                break
        self.chain.append(new_block) # Интересная область видимости в пайтоне xD
        print("Добыт новый блок: ", new_block)

    @staticmethod
    def valid_hash(block: dict): # Проверка хэша на нули в начале
        return block["hash"].startswith("0000")
