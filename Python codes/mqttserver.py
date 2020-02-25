import time
import ttn
import base64
import requests

app_id = "rpigladiolen"
access_key = "ttn-account-v2.n1GeQ2DCwg0_gXyay00RcSJ-lmNPwRKnyd-2-c3Nebw"

def uplink_callback(msg, client):
  print("Received uplink from ", msg.dev_id)
  print(msg)
  asci_code = msg.payload_raw 
  code_legit=base64.b64decode(asci_code)
  print(code_legit)
  data = {'api_paste_code':code_legit} 
  r = requests.post('https://back-end.vzwkeizerkarel.be/api/Tijdsregistratie/loraTijdsregistratie/', data = data) 
  pastebin_url = r.text
  print(pastebin_url)



handler = ttn.HandlerClient(app_id, access_key)

# using mqtt client
mqtt_client = handler.data()
mqtt_client.set_uplink_callback(uplink_callback)
mqtt_client.connect()	
time.sleep(608000)
mqtt_client.close()

# using application manager client
app_client =  handler.application()
my_app = app_client.get()
print(my_app)
my_devices = app_client.devices()
print(my_devices)