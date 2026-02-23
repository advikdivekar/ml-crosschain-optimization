from web3 import Web3
import pymysql

INFURA_URL = ""

# Connect to Ethereum
w3 = Web3(Web3.HTTPProvider(INFURA_URL))

if not w3.is_connected():
    print("Connection failed")
    exit()

conn = pymysql.connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    password="StrongPassword123",
    database="eth_research",
    autocommit=True
)


cursor = conn.cursor()

# Force bulk backfill (temporary)
latest_block = w3.eth.block_number
last_block = latest_block - 20000

# Collect new blocks
for block_number in range(last_block + 1, latest_block + 1):

    try:
        block = w3.eth.get_block(block_number)

        base_fee = block.get("baseFeePerGas", 0)

        gas_used = block["gasUsed"]
        gas_limit = block["gasLimit"]
        fullness = gas_used / gas_limit if gas_limit != 0 else 0

        cursor.execute("""
            INSERT IGNORE INTO blocks
            (block_no, timestamp_data, base_fee, gas_used, gas_limit, block_fullness)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (
            block.number,
            block.timestamp,
            base_fee,
            gas_used,
            gas_limit,
            fullness
        ))

        print(f"Data traced from Infura Server to Local Server MariaDB for Block Number :{block.number}")

    except Exception as e:
        continue

conn.commit()
conn.close()

print("Infura --> MariaDB connection completed.")
