import random

# Function to find a hash that meets the target of 5 zeros.
def mine_block(block, difficulty=5):
    prefix = '0' * difficulty
    while not block.hash.startswith(prefix):
        block.timestamp = time.time()  # Ajustar el timestamp para cada intento
        block.data += str(random.random())  # Cambiar ligeramente los datos
        block.hash = calculate_hash(block.index, block.previous_hash, block.timestamp, block.data)
    return block

# Function to simulate a committee that evaluates which block is the best.
def committee_evaluation(blocks, difficulty=5):
    prefix = '0' * difficulty
    valid_blocks = [block for block in blocks if block.hash.startswith(prefix)]
    # Seleccionamos el bloque con el hash más pequeño (más cercano al objetivo)
    return min(valid_blocks, key=lambda block: block.hash) if valid_blocks else None

# Example of use: Creation and validation of blocks with a committee.
blockchain = Blockchain()

# Simulate several blocks that are being "mined" simultaneously.
candidates = [mine_block(Block(i, blockchain.get_latest_block().hash, time.time(), f"Transacción {i}", ""))
              for i in range(1, 4)]

# Evaluate which block is the best and add it to the chain.
best_block
