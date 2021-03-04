import hashlib
import json
import os


def md5(str_v):
    stv = str(str_v).encode('utf-8')
    m = hashlib.md5()
    m.update(stv)
    return m.hexdigest()


def getblock_hash(block_id):
    file = open(os.curdir + "/blocks/" + str(block_id), "rb").read()
    return md5(file)


def getblock(block_id):
    block = json.load(open(os.curdir + "/blocks/" + str(block_id)))
    return block


def check_valid_block(block_id):
    curr_hash = getblock_hash(block_id)
    if os.path.isfile(os.curdir + "/blocks/" + str(block_id+1)):
        next_block = getblock(block_id + 1)
        hash_from_next_block = next_block['hash']
    else:
        hash_from_next_block = curr_hash
    return True if curr_hash == hash_from_next_block else False


def check_intergrity():
    blockchain_dir = os.curdir + "/blocks"
    blocks = sorted([int(i) for i in os.listdir(blockchain_dir)])
    result = []
    for block in blocks:
        result.append({
            "block_id": block,
            "validate": "valid" if check_valid_block(block) else "invalid"
        })
    return result


def write_block(my_id, amount, to_whom_id):
    blockchain_dir = os.curdir + "/blocks"
    blocks = sorted([int(i) for i in os.listdir(blockchain_dir)])
    last_block = blocks[-1]
    new_block = last_block + 1
    data = {"name": my_id, "amount": amount, "to_whom": to_whom_id,
            "hash": getblock_hash(str(last_block))}
    with open(f"{blockchain_dir}/{new_block}", "w") as file_:
        json.dump(data, file_, indent=4, ensure_ascii=False)

def calculate(uid):
    blockchain_dir = os.curdir + "/blocks"
    blocks = sorted([int(i) for i in os.listdir(blockchain_dir)])
    curr_user_val = 0
    for block in blocks:
        block_data = getblock(block)
        block_amount = int(block_data["amount"])
        if block_data["name"] == uid:
            curr_user_val -= block_amount
        elif block_data["to_whom"] == uid:
            curr_user_val += block_amount
        else:
            pass
    return curr_user_val

def main():
    pass


if __name__ == '__main__':
    main()
