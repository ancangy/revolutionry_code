import hashlib

def hash_data(data):
    return hashlib.sha256(data.encode('utf-8')).hexdigest()

def merkle_tree(leaf_hashes):
    if len(leaf_hashes) == 1:
        return leaf_hashes[0]

    if len(leaf_hashes) % 2 != 0:
        leaf_hashes.append(leaf_hashes[-1])

    parent_hashes = []
    for i in range(0, len(leaf_hashes), 2):
        combined_hash = hash_data(leaf_hashes[i] + leaf_hashes[i + 1])
        parent_hashes.append(combined_hash)

    return merkle_tree(parent_hashes)

# Original data sent by the server
data_blocks = ["data1", "data2", "data3", "data4"]
leaf_hashes = [hash_data(data) for data in data_blocks]
original_merkle_root = merkle_tree(leaf_hashes)

# Suppose a malicious intermediary modifies one of the data blocks in transit
# This simulates a Man-in-the-Middle attack
modified_data_blocks = ["data1", "data2", "dataX", "data4"]  # 'data3' was changed to 'dataX'
modified_leaf_hashes = [hash_data(data) for data in modified_data_blocks]
received_merkle_root = merkle_tree(modified_leaf_hashes)

# Verification by the client
if original_merkle_root == received_merkle_root:
    print("The data has not been altered.")
else:
    print("Alert! Possible Man-in-the-Middle attack detected. The data has been modified.")
