import hashlib
import time

# Definition of a block in the chain, following good software practices
class Block:
    def __init__(self, index, previous_hash, timestamp, data, hash_value):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.hash = hash_value

    def __repr__(self):
        # Proporcionar una representación legible del bloque para facilitar la depuración
        return (f"Block({self.index}, "
                f"Previous: {self.previous_hash}, "
                f"Time: {self.timestamp}, "
                f"Datos: {self.data}, "
                f"Hash: {self.hash})")

# Function to calculate the hash of a block with explanations
def calculate_hash(index, previous_hash, timestamp, data):
    value = f"{index}{previous_hash}{timestamp}{data}"
    return hashlib.sha256(value.encode('utf-8')).hexdigest()

# Create the first block (genesis) in the chain
def create_genesis_block():
    genesis_timestamp = time.time()
    genesis_hash = calculate_hash(0, "0", genesis_timestamp, "Genesis Block")
    return Block(0, "0", genesis_timestamp, "Genesis Block", genesis_hash)

# Class to handle the complete blockchain
class Blockchain:
    def __init__(self):
        # Iniciar la cadena con el bloque génesis
        self.chain = [create_genesis_block()]

    def get_latest_block(self):
        # Obtener el último bloque de la cadena
        return self.chain[-1]

    def add_block(self, data):
        # Añadir un nuevo bloque a la cadena
        latest_block = self.get_latest_block()
        new_index = latest_block.index + 1
        new_timestamp = time.time()
        new_hash = calculate_hash(new_index, latest_block.hash, new_timestamp, data)
        new_block = Block(new_index, latest_block.hash, new_timestamp, data, new_hash)
        self.chain.append(new_block)

# Function to validate blockchain integrity
def is_chain_valid(blockchain):
    for i in range(1, len(blockchain.chain)):
        current_block = blockchain.chain[i]
        previous_block = blockchain.chain[i - 1]

        # Verificar que el hash actual sea correcto
        if current_block.hash != calculate_hash(current_block.index, current_block.previous_hash, current_block.timestamp, current_block.data):
            return False

        # Verificar que el hash previo concuerde con el bloque anterior
        if current_block.previous_hash != previous_block.hash:
            return False

    return True

# Example of use
blockchain = Blockchain()
blockchain.add_block("Transaction 1: Alice send 2 BTC a Bob")
blockchain.add_block("Transaction 2: Bob send 3 BTC a Charlie")
blockchain.add_block("Transaction 3: Charlie send 1 BTC a Alice")

for block in blockchain.chain:
    print(block)

print("Is the block chain valid?", is_chain_valid(blockchain))
