import requests

my_data = {"name": "Zac", "email": "zac@example.com"}
r = requests.post("https://tryphp.w3schools.com/showphp.php?filename=demo_form_get")

f = open("myfile.html", "w+")
f.write(r.text)