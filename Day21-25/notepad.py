#!/usr/bin/env python
import json
class NotePad:
    def __init__(self, x, y, z):
        self._x = x
        self._y = y
        self._z = z

    def sum(self):
        return self._x + self._y + self._z

    def convert_to_dict(self):
        # object properties are converted to key-value pairs python dictionary object
        return self.__dict__

    def json_serialization(self):
        # json.dumps() function converts a Python object (dictionary) into string and stores it in json_string.
        # Equivalent json string of input dictionary:
        return json.dumps(self.convert_to_dict())


if __name__ == "__main__":
    note1 = NotePad('5', '6', '7')
    print(note1.sum())
    note_dict = note1.convert_to_dict()
    print(note_dict)
    json_string = note1.json_serialization()
    print(json_string, type(json_string))
