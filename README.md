# fastapi-serialization-study

Profile JSON vs. MessagePack response times for an endpoint returning large matrices. 

Submit benchmark scripts that: 

* Expose an endpoint returning a large matrix serialized as JSON
* Expose the same endpoint returning MessagePack
* Tabulate request/response times and payload sizes
* Recommend which format to use in production based on your findings

## Getting Started 

* Setup a Python project.
* Install dependencies: pip install fastapi uvicorn numpy msgpack httpx
* Run benchmark.py file

## Output
![Screenshot (7)](https://github.com/user-attachments/assets/7ad2b003-e3c1-41c3-897b-74abef0ecb6a)

## Findings

* When compared with having 1000/1000 matrices, MessagePacks has less payload size and response time.
* JSON serialization has more payload size and response time with large matrices.
* I can recommand, MessagePacks to use in production when compared to JSON on basis of response times and payload sizes. But it comes to human-readable JSON is recommanded.
