#!/usr/bin/python3
""" JSON file-writing function"""
    import json


    def save_to_json_file(my_obj, filename):
        """ opens and closes using with and Writes an into object to a text file using JSON format"""
        with open(filename, "w") as f:
            json.dump(my_obj, f)
