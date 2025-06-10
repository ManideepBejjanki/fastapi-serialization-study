import requests
import time

ENDPOINTS = {
    "JSON": "http://127.0.0.1:8000/matrix/json",
    "MessagePack": "http://127.0.0.1:8000/matrix/msgpack",
    "Pickle": "http://127.0.0.1:8000/matrix/pickle",
    "Parquet": "http://127.0.0.1:8000/matrix/parquet",
    "Joblib": "http://127.0.0.1:8000/matrix/joblib",
    "Binary": "http://127.0.0.1:8000/matrix/bin",
}

results = []


for name, url in ENDPOINTS.items():
    start_time = time.time()
    response = requests.get(url)
    end_time = time.time()

    results.append(
        {
            "Format": name,
            "Time (s)": round(end_time - start_time, 4),
            "Payload Size (KB)": round(len(response.content) / 1024, 2),
        }
    )

print(f"{'Format':<15} {'Time (s)':<10} {'Payload Size (KB)':<20}")
print("-" * 45)
for res in results:
    print(f"{res['Format']:<15} {res['Time (s)']:<10} {res['Payload Size (KB)']:<20}")
