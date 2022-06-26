import json

employees_string = '''
{
    "employees" : [
       {
           "first_name": "Michael", 
           "last_name": "Rodgers", 
           "department": "Marketing"
           
        },
       {
           "first_name": "Michelle", 
           "last_name": "Williams", 
           "department": "Engineering"
        }
    ]
}
'''

json_from_str = json.loads(employees_string)
print(json_from_str)

json_to_str = json.dumps(json_from_str.__dict__)
print(json_to_str)

