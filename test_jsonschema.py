from jsonschema import validate

# A sample schema, like what we'd get from json.load()
schema = {
    "type" : "object",
    "properties" : {
        "price" : {"type" : "number"},
        "name" : {"type" : "string"},
    },
}


def test_jsonschemasuccess():
    assert validate(instance={"name" : "Eggs", "price" : 34.99}, schema=schema) == None

def test_jsonschemafailed():
    failed = None
    try:
        validate(instance={"name" : "Eggs", "price" : 23}, schema=schema) 
        failed = False
    except :
        failed = True
        
    assert failed == True               