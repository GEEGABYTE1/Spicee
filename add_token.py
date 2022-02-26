from script import Spicee
from tokenizing import token_block

genesis_block = Spicee.chain[0]
rest_of_chain = Spicee.chain[1:]
if len(rest_of_chain) == 0:
    token_block.generate_hash()
    Spicee.chain.append(token_block)
    print(Spicee.chain)
