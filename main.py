import requests

id = input("Episode Number: ")
if id.isdigit() and len(id) <= 4:
    try:
        result = requests.get("https://api.api-onepiece.com/v2/episodes/en/{}".format(id)).json()
        arc = str(result['arc']['title'])
        if "Arc" in arc:
            arc = arc.replace("Arc ", "")
        print("[#] You're in {}!".format(arc))
    except TypeError:
        print("[!] Episode does not exist!")
else:
    print("[!] Incorrect Format! Example: \"323\", \"2222\"")
