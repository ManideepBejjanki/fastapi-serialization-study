from fastapi import FastAPI, Response
import numpy as np
import msgpack
import pickle

app = FastAPI()

# random matrix from numpy
matrix = np.random.rand(1000, 1000)


# endpoint for json data.
@app.get("/matrix/json")
def get_matrix_json():
    return matrix.tolist()


# endpoint for msgpack data.
@app.get("/matrix/msgpack")
def get_matrix_msgpack():
    data = msgpack.packb(matrix.tolist(), use_bin_type=True)
    return Response(content=data, media_type="application/msgpack")


# endpoint for pickle data.
@app.get("/matrix/pickle")
def get_Matrix_pickle():
    return Response(content=pickle.dumps(matrix), media_type="application/octet-stream")
