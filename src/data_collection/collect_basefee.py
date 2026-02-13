from web3 import Web3
import csv

INFURA_URL = "https://mainnet.infura.io/v3/f6dccf73ccd64c06a5e7734325927bb9"

w3 = Web3(Web3.HTTPProvider(INFURA_URL))

if not w3.is_connected():
    print("Connection failed")
    exit()

file_path = "data/raw/eth_basefee.csv"

latest_block = w3.eth.block_number

# Change this number to 5000 or 10000
BLOCK_RANGE = 5000

start_block = latest_block - BLOCK_RANGE

with open(file_path, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["block_number", "timestamp", "base_fee_per_gas"])

    for block_number in range(start_block, latest_block):
        block = w3.eth.get_block(block_number)

        base_fee = block.get("baseFeePerGas", 0)

        writer.writerow([
            block.number,
            block.timestamp,
            base_fee
        ])

        print(f"Block Collected from the Ethereum Gas along with Gas Fee and its block number is : {block.number}")

print("Finished collecting large dataset.")

