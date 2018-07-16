user = "kkuang"
password = ""





















import requests, urllib3
outsideTemp = "https://oakpicoresight.osisoft.int:8443/piwebapi/streams/F1AbEnqdqScCm70aDbETKiwGLjw_rj0BjAl5xGJN3xc-DlStAf8t01_W2UlkBVX-MbuLDQgT0FLUElBRlxGQUNJTElUSUVTLTE2MDAgQUxWQVJBRE9cU0xUQ1xXRUFUSEVSfE9VVFNJREUgQUlSIFRFTVBFUkFUVVJF/value"
#outsideTemp = requests.get(outsideTemp,verify=False,auth=(user,password),cert="certificate.cer").json()
print (outsideTemp)

numRounds = 3
numReload = numRounds

speedx = 4
speedy = speedx + 2
score = 10
timer = 10







roundSpeed = 1
frames = 60
#amount of ducks available per round.
testnum = 10

#amt of ducks + 2
amtDucks = 0
miss = 4

posSensitivity = 10
COUNTER = 0
JSMOVEMENT = False






