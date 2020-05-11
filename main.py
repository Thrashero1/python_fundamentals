import simplejson as json
import os

"""
# creates a files we can write to (w+) or read from (r+)
new_file = open("new_file.txt", "w+")

string = "This is what will be written to the file"

new_file.write(string)
"""

# Here we write and read from a json file
# we check if the files exists and is not empty
if os.path.isfile("./age.json") and os.stat("./age.json").st_size != 0:
    old_file = open("./age.json", "r+")
    # convert the json obj into a python obj
    data = json.loads(old_file.read())
    print("current age is", data["age"])
    data["age"] += 1
    print("new age is:", data["age"])

else:
    old_file = open("./age.json", "w+")
    data = {"name": "David",
            "age": 37}
    print("no file found, file created")

# sets is to a position from where it will start from (in this case 0 meaning the start)
old_file.seek(0)
# The json.dumps converts the python object into a json object
old_file.write(json.dumps(data))
