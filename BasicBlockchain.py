import hashlib
import time

# Definición de un bloque en la cadena, siguiendo buenas prácticas de software
class Block:
    def __init__(self, index, previous_hash, timestamp, data, hash_value):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.hash = hash_value

    def __repr__(self):
        # Proporcionar una representación legible del bloque para facilitar la depuración
        return (f"Bloque({self.index}, "
                f"Anterior: {self.previous_hash}, "
                f"Tiempo: {self.timestamp}, "
                f"Datos: {self.data}, "
                f"Hash: {self.hash})")

# Función para calcular el hash de un bloque con explicaciones
def calculate_hash(index, previous_hash, timestamp, data):
    value = f"{index}{previous_hash}{timestamp}{data}"
    return hashlib.sha256(value.encode('utf-8')).hexdigest()

# Crear el primer bloque (génesis) en la cadena
def create_genesis_block():
    genesis_timestamp = time.time()
    genesis_hash = calculate_hash(0, "0", genesis_timestamp, "Bloque Génesis")
    return Block(0, "0", genesis_timestamp, "Bloque Génesis", genesis_hash)

# Clase para manejar la cadena de bloques completa
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
