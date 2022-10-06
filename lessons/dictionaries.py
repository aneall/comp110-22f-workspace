"""Demonstrations of dictionary capabilities."""


# declaring the type of a dictionary
schools: dict[str, int]

# initializing to an empty dictionary
schools = dict()

# set a key-value pairing in the dictionary
schools["UNC"] = 19400
schools["Duke"] = 6717
schools["NCSU"] = 26150

# print a dictionary literal representation
print(schools)

# access a value by its key (aka "lookup")
print(f"UNC has {schools['UNC']} students")

# remove a key-value pair from a dictionary - by its key!
schools.pop("Duke")

# test for existence of a key
if "Duke" in schools:
    print("Found the key'Duke' in schools")
else:
    print("No key 'Duke' in schools")


# update / reassign a key-value pair
schools["UNC"] = 20000
schools["NCSU"] += 200


# demonstration of dictionary literals


# example of an empty dictionary below:
schools = {} # same as dict()
print(schools)

# we could also initialize the key-value pairs:
schools = {"UNC": 19400, "Duke": 6717, "NSCU": 26150}
print(schools)

# what happens when a key does not exist?
# print(schools["UNCC"])

# Example looping over the keys of a dict
for school in schools:
    print(f"Key: {school} -> Value: {schools[school]}")