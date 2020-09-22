import json

# json string data
data = '{"name" : "rheno", "personal_data" : { "age" : 25, "sex" : "male", "location" : { "country" : "Indonesia", "area" : {"city" : "jakarta", "district" : "cibubur"} } } }'

# loads as dictionary
obj = json.loads(data)

# recursive function to check key exist in dict
def get_object(dict_data, object_key):

        # if object key is exist in dict_data return the dict
        if object_key in dict_data :
                return dict_data


        for key, value in dict_data.items() :

                # if the dict_data contains another dictionary. Then search recursively to the object
                if type(dict_data[key]) == dict :
                        return get_object(dict_data[key], object_key)

        # key is not found
        return None

p = get_object(obj, 'city')

print(p.get('city'))
