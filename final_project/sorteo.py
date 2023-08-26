import json
from web3 import Web3

w3 = Web3(
    Web3.HTTPProvider(
        "https://eth-mainnet.g.alchemy.com/v2/49nOL_LGpB4-vb1pFaT7uLJhM93zxg9n"
    )
)

print(w3.eth.get_block_number())
json_block = w3.eth.get_block("latest")
json_final = Web3.to_json(json_block)
info = json.loads(json_final)
print(info["hash"])

rand_number = info["hash"][2:6] + info["hash"][-4:] + str(info["timestamp"])
print(rand_number)
rand_number_format = int(rand_number.encode("utf-8").hex())

x = rand_number_format % 13
print(x)
