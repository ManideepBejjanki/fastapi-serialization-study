import os
from datetime import datetime
import msgpack


user_data = {
    "name": "SomeOne",
    "age": 20,
    "is_engineer": True,
    "skills": ["Python", "JavaScript", "Java"],
    "experience_years": 2,
    "last_login": datetime(2025, 6, 4, 17, 10, 30),
    "metadata": None,
    "config_id": 1234567890,
}

print("Original Data: ", user_data)
print("Type: ", type(user_data))

# pack to bytes.

binary_packed_data = msgpack.packb(user_data, use_bin_type=True)

print("Binary Packed data: ", binary_packed_data)
print("Type: ", type(binary_packed_data))

un_packed_bin_data = msgpack.unpackb(binary_packed_data, raw=False)
print("UnPacked Binary Data: ", un_packed_bin_data)
print("Type: ", type(un_packed_bin_data))

# pack to file.

file_name = "msgpack_data.mpac"

with open(file_name, "wb") as f:
    msgpack.pack(user_data, f, use_bin_type=True, default=str)

with open(file_name, "rb") as f:
    unpacked_data_from_file = msgpack.unpack(f, raw=False)
