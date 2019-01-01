"request client"

import requests


file_path = "xxx.png"

result = requests.post("http://localhost:9999/testfile", files={"牛逼的不得了.png": open(file_path, "rb").read()})

