import json
from dc import ActionID

with open('action-test.json') as file:
    action_test=json.load(file)

with open('roleactions.json') as file:
    roleactions=json.load(file)

with open('roles.json') as file:
    roles=json.load(file)

role_codes=set()
for i in roles:
    role_codes.add(i["code"])


role_codes=list(role_codes)


def getActionIds(roleactions: dict, role_codes: list, ):
    

    """
    iterates through roles
    """ 
    for role in role_codes:
        action_ids=set()
        action_urls=set()
        action_data=[]


        """
        checks if role code is present in roleactions mapping
        and add the action id to a set
        """
        for obj in roleactions:
            if role==obj["rolecode"]:
                action_ids.add(obj["actionid"])
        
        action_ids=list(action_ids)


        """
        iterates through action_ids list genereated earlier 
        checks if action id is present in action-test and fetches URL
        """
        for aid in action_ids:         
            for obj in action_test:
                if aid==obj["id"]:
                    
                    url=obj["url"]
                    nav_url: str
                    
                    if "navigationURL" in obj:
                        nav_url=obj["navigationURL"]
                    else:
                        nav_url=""
                    
                    data=ActionID(
                        id=aid,
                        url=url,
                        nav_url=nav_url
                    ).__dict__
                    action_data.append(data)


        file_path="exports/"+role+'.json'
        with open(file_path, "w") as file:
            json.dump(action_data, file, indent=4)

    
getActionIds(roleactions=roleactions, role_codes=role_codes)

