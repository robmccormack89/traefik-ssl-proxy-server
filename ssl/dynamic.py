import yaml
import os
import json

# Nested data
static_data = {
    "tls": {
        "certificates": [
            {
                "certFile": "/etc/certs/localhost/server.crt",
                "keyFile": "/etc/certs/localhost/server.key",
                "stores": ["default"],
            },
            {
                "certFile": "/etc/certs/mysite.com/server.crt",
                "keyFile": "/etc/certs/mysite.com/server.key",
                "stores": ["default"],
            },
            {
                "certFile": "/etc/certs/blech.com/server.crt",
                "keyFile": "/etc/certs/blech.com/server.key",
                "stores": ["default"],
            },
            {
                "certFile": "/etc/certs/example.com/server.crt",
                "keyFile": "/etc/certs/example.com/server.key",
                "stores": ["default"],
            },
            {
                "certFile": "/etc/certs/traefik.com/server.crt",
                "keyFile": "/etc/certs/traefik.com/server.key",
                "stores": ["default"],
            },
            {
                "certFile": "/etc/certs/proxy.com/server.crt",
                "keyFile": "/etc/certs/proxy.com/server.key",
                "stores": ["default"],
            },
            {
                "certFile": "/etc/certs/testwp.com/server.crt",
                "keyFile": "/etc/certs/testwp.com/server.key",
                "stores": ["default"],
            },
            {
                "certFile": "/etc/certs/test.com/server.crt",
                "keyFile": "/etc/certs/test.com/server.key",
                "stores": ["default"],
            },
        ],
        "stores": {
            "default": {
                "defaultCertificate": {
                    "certFile": "/etc/certs/localhost/server.crt",
                    "keyFile": "/etc/certs/localhost/server.key",
                }
            }
        },
    }
}

def create_folder_structure_json(path):
    # Initialize the result dictionary with folder
    # name, type, and an empty list for children
    result = {'name': os.path.basename(path),
              'type': 'folder', 'children': []}

    # Check if the path is a directory
    if not os.path.isdir(path):
        return result

    # Iterate over the entries in the directory
    for entry in os.listdir(path):
       # Create the full path for the current entry
        entry_path = os.path.join(path, entry)

        # If the entry is a directory, recursively call the function
        if os.path.isdir(entry_path):
            result['children'].append(create_folder_structure_json(entry_path))
        # If the entry is a file, create a dictionary with name and type
        else:
            result['children'].append({'name': entry, 'type': 'file'})

    return result

# Specify the path to the folder you want to create the JSON for
folder_path = 'certs'

# Call the function to create the JSON representation
folder_json = create_folder_structure_json(folder_path)

# Convert the dictionary to a JSON string with indentation
folder_json_str = json.dumps(folder_json, indent=4)

# To print specific objects within the data, we use loads()
dyndata = json.loads(folder_json_str)
# print(dyndata['children'])

def create_new_json_structure(path):
    
    tls = {
        'certificates': [],
        'stores': { 
            'default': { 
                'defaultCertificate': {
                    'certFile':'','keyFile':''
                }
            }
        }
    }
    
    if not os.path.isdir(path):
        return result
        
    if 'localhost' not in os.listdir(path):
        for site in os.listdir(path):
            # Create the full path for the current entry
            entry_path = os.path.join(path, site)
            tls['certificates'].append({'certFile': '/etc/certs/' + site + '/server.crt', 'keyFile': '/etc/certs/' + site + '/server.key', 'stores': ['default']})
            tls['stores']['default']['defaultCertificate']['certFile'] = '/etc/certs/' + site + '/server.crt'
            tls['stores']['default']['defaultCertificate']['keyFile'] = '/etc/certs/' + site + '/server.key'
        return {'tls':tls}
        
    if 'localhost' in os.listdir(path):
        for site in os.listdir(path):
            # Create the full path for the current entry
            entry_path = os.path.join(path, site)
            tls['certificates'].append({'certFile': '/etc/certs/' + site + '/server.crt', 'keyFile': '/etc/certs/' + site + '/server.key', 'stores': ['default']})
            tls['stores']['default']['defaultCertificate']['certFile'] = '/etc/certs/localhost/server.crt'
            tls['stores']['default']['defaultCertificate']['keyFile'] = '/etc/certs/localhost/server.key'
        return {'tls':tls}

# Specify the path to the folder you want to create the JSON for
s_folder_path = 'certs'

# Call the function to create the JSON representation
s_folder_json = create_new_json_structure(s_folder_path)

# Convert the dictionary to a JSON string with indentation
s_folder_json_str = json.dumps(s_folder_json, indent=4)

# To print specific objects within the data, we use loads()
s_dyndata = json.loads(s_folder_json_str)
# print(dyndata['children'])

# Writing nested data to a YAML file
with open('dynamic.yml', 'w') as file:
    yaml.dump(s_dyndata, file)

print("Data has been written to 'dynamic.yaml'")