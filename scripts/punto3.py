import json
import datetime
try:
with open('/home/devasc/labs/devnet-src/parsing/myfile.json') as f:
json_file = json.load(f)

token = json_file["access_token"]
expiration_time = datetime.datetime.now() + datetime.timedelta(seconds=json_file["expires_in"])
time_left = expiration_time - datetime.datetime.now()

print("token: {}".format(token))
print("Tiempo sobrante: {}".format(time_left))

except FileNotFoundError:
print("archivo no encontrado.")
except json.JSONDecodeError:
print("El archivo es inválido.")
except KeyError:
print("El archivo no contiene el campo 'access_token'.")

