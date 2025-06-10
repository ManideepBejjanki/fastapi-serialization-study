from fastapi import FastAPI, Response
import pandas as pd
import numpy as np
import msgpack
import pickle
import pyarrow as pa
import pyarrow.parquet as pq
from joblib import dump

app = FastAPI()

# random matrix from numpy
matrix = np.random.rand(1000, 1000)


# endpoint returning json data.
@app.get("/matrix/json")
def get_matrix_json():
    return matrix.tolist()


# endpoint returning msgpack data.
@app.get("/matrix/msgpack")
def get_matrix_msgpack():
    data = msgpack.packb(matrix.tolist(), use_bin_type=True)
    return Response(content=data, media_type="application/msgpack")


# endpoint returning pickle data.
@app.get("/matrix/pickle")
def get_Matrix_pickle():
    return Response(content=pickle.dumps(matrix), media_type="application/octet-stream")


# endpoint returning parquet data
@app.get("/matrix/parquet")
def get_matrix_parquet():
    df = pd.DataFrame(matrix)
    buffer = io.BytesIO()
    table = pa.Table.from_pandas(df)
    pq.write_table(table, buffer)
    return Response(content=buffer.getvalue(), media_type="application/octet-stream")


# endpoint returning joblib data
@app.get("/matrix/joblib")
def get_matrix_joblib():
    buffer = io.BytesIO()
    dump(matrix, buffer)
    return Response(content=buffer.getvalue(), media_type="application/octet-stream")


# endpoint returning bin data
@app.get("/matrix/bin")
def get_bin():
    return Response(content=matrix.tobytes(), media_type="application/octet-stream")
