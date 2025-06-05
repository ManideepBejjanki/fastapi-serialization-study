# fastapi-serialization-study

Profile JSON vs MessagePack vs Pickle response times for an endpoint returning large matrices. 

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
![Screenshot 2025-06-05 172252](https://github.com/user-attachments/assets/a2225011-fc2e-497a-9c60-aa9497eba4dd)

## Findings
* JSON will be human-readable, when compared to both message pack and pickle it has more payload and higher response time.
* MessagePack has binary code which performs better than JSON data.
* Compared to JSON, MessagePack, Pickle, Pickle data consumes less memory and the response time is faster.

