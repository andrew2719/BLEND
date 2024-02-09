from hashlib import sha256
import ed_s


async def chunk(file_data):
    # chunk the data and arrange in a dicct with index use base64 encoding
    file_data = file_data['data']
    chunk_size = len(file_data) // 4
    chunks = [file_data[i:i+chunk_size] for i in range(0, len(file_data), chunk_size)]
    # print(chunks)
    chunks_dict = {}
    '''
    dict format
    {
        0:{'hash':sha256(chunk).hexdigest(),
        'file_id':sha256((file_data['filename']+str(index)+sha256(chunk).hexdigest()).encode()).hexdigest(),
        'data':await ed_s.encode_b64(chunk),
        'index':index,
        'size':chunk_size}
        1:{'hash':sha256(chunk).hexdigest(),
        'file_id':sha256((file_data['filename']+str(index)+sha256(chunk).hexdigest()).encode()).hexdigest(),
        'data':await ed_s.encode_b64(chunk),
        'index':index,
        'size':chunk_size}
        ....
        
    }
    '''
    for index,chunk in enumerate(chunks):
        chunks_dict[index] = {
            # for file id add the original filename, idx, hash . hadh everyting to the file id with sha256
            'hash': sha256(chunk).hexdigest(),
            'file_id': sha256((file_data['filename']+str(index)+sha256(chunk).hexdigest()).encode()).hexdigest(),
            'data': await ed_s.encode_b64(chunk),
            'index': index,
            'size': chunk_size
        }
    return chunks_dict