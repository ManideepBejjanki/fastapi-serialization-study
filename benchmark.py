import httpx
import time

JSON_URL = "http://127.0.0.1:8000/matrix/json"
MSGPACK_URL = "http://127.0.0.1:8000/matrix/msgpack"
PICKLE_URL = "http://127.0.0.1:8000/matrix/pickle"


def benchmark(url: str, headers=None):
    start = time.time()
    response = httpx.get(url, headers=headers)
    time_taken = time.time() - start
    matrix_size = len(response.content)
    return time_taken, matrix_size


def run_benchmark():
    print("Benchmarking....")

    # run benchmark for json data.
    json_time, json_size = benchmark(JSON_URL)
    print(f"JSON: {json_time:.4f}s | Payload: {json_size / 1024:.2f} KB")

    # run benchmark for msgpack data.
    msgpack_time, msgpack_size = benchmark(
        MSGPACK_URL, headers={"Accept": "application/msgpack"}
    )
    print(f"MessagePack: {msgpack_time:.4f}s | Payload: {msgpack_size / 1024:.2f} KB")

    # run benchmark for pickle data.
    pickle_time, pickle_size = benchmark(
        PICKLE_URL, headers={"Accept": "application/octet-stream"}
    )
    print(f"Pickle: {pickle_time:.4f}s | Payload: {pickle_size / 1024:.2f} KB")


if __name__ == "__main__":
    run_benchmark()
