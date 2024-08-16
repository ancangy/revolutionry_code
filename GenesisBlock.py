# Example of blockchain compression and the creation of a new genesis.
def compress_blockchain(blockchain):
    combined_hash = hashlib.sha256()
    for block in blockchain.chain:
        combined_hash.update(block.hash.encode('utf-8'))
    return combined_hash.hexdigest()

def create_new_genesis_block(compressed_hash):
    return Block(0, "0", time.time(), "Bloque Génesis Comprimido", compressed_hash)

# Use of compression and creation of new genesis
compressed_hash = compress_blockchain(blockchain)
new_genesis_block = create_new_genesis_block(compressed_hash)
print(new_genesis_block)
