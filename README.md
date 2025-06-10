# fastapi-serialization-study

Profile JSON v/s MessagePack v/s Pickle v/s Parquet v/s Joblib v/s Binary  response times for an endpoint returning large matrices. 

Submit benchmark scripts that: 

* Expose an endpoint returning a large matrix serialized as JSON
* Expose the same endpoint returning MessagePack, Pickle, Parquet, Joblib, Binary
* Tabulate request/response times and payload sizes
* Recommend which format to use in production based on your findings

## Getting Started 

* Setup a Python project.
* Install dependencies: pip install fastapi uvicorn numpy pandas pyarrow msgpack joblib requests
* Run benchmark.py file

## Output
![Screenshot 2025-06-10 062023](https://github.com/user-attachments/assets/39511277-3557-4f23-a15b-2bc5b3899c4a)

## Findings
* JSON will be human-readable, when compared to message pack, parquet, Joblib, Binary and pickle it has more payload and higher response time.
* Response Time: Parquet is having very less response time compared to other types. (Parquet < Binary < Pickle < MessagePack < Joblib, JSON).
* Payload: Parquet and Joblib is having less payloads compared to other types. (Parquet < Joblib < Binary < Pickle < MessagePack < JSON).
