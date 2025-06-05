import pickle

user_data = {
    "name": "SomeOne",
    "age": 20,
    "is_active": True,
    "research_areas": {"physics", "light scattering"},
    "none_value": None,
    "complex_number": complex(3, 4),
}

# pickle to bytes

pickled_data = pickle.dumps(user_data)
print("Pickled Data: ", pickled_data)
print("Type: ", type(pickled_data))


unpickled_data = pickle.loads(pickled_data)
print("UnPickled Data: ", unpickled_data)
print(type(unpickled_data))


# pickle to file

file_name = "my_data.pickle"

with open(file_name, "wb") as pickle_file:
    pickle.dump(user_data, pickle_file)

with open(file_name, "rb") as pickle_file:
    un_pickled_data = pickle.load(pickle_file)
