a = {
    "Aditya" : "Bhutada",
    "Adityaa" : "20",
    'age': 22
}

a_copy = a.copy()
print("\nCopy of the Dictionary: ", a_copy)
value = a.get('age')
print("Value of age is: ", value)
key_value_pairs = a.items()
print("\nKey Value Pair List: ", key_value_pairs)
keys = a.keys()
print("Keys in the dictionary: \n", keys)

values = a.values()
print("Values in the dictionary:\n", values)

removed_value = a.pop('age')
print(removed_value)

a.update({'age': 23})
print("\nAfter updating the dictionary: ")
print(a)

del a['Aditya']
print("\nDictionary after deleting an element:")
print(a)

