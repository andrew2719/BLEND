#encoding and decoding with b64
# channging thr json formats to dict and back to json

import base64
import pickle


async def encode_b64(data):
    return base64.b64encode(data)

async def decode_b64(data):
    return base64.b64decode(data)

async def serialize(data):
    return pickle.dumps(data)

async def deserialize(data):
    return pickle.loads(data)
