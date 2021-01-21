import requests
from requests.auth import HTTPBasicAuth

def retrieve_nombre(contract_instance, node, account, credential, key):
    url = 'https://u0z93so5ob-'+ node +'-connect.us0-aws.kaleido.io/instances/'+ contract_instance + '/retrieve_nombre'
    myobj = {'kld-from': account}
    x = requests.get(url, params = myobj, auth=HTTPBasicAuth(credential, key))
    return x.text

def retrieve_apellido(contract_instance, node, account, credential, key):
    url = 'https://u0z93so5ob-'+ node +'-connect.us0-aws.kaleido.io/instances/'+ contract_instance + '/retrieve_apellido'
    myobj = {'kld-from': account}
    x = requests.get(url, params = myobj, auth=HTTPBasicAuth(credential, key))
    return x.text

def retrieve_titulo(contract_instance, node, account, credential, key):
    url = 'https://u0z93so5ob-'+ node +'-connect.us0-aws.kaleido.io/instances/'+ contract_instance + '/retrieve_titulo'
    myobj = {'kld-from': account}
    x = requests.get(url, params = myobj, auth=HTTPBasicAuth(credential, key))
    return x.text

def retrieve_mencion(contract_instance, node, account, credential, key):
    url = 'https://u0z93so5ob-'+ node +'-connect.us0-aws.kaleido.io/instances/'+ contract_instance + '/retrieve_mencion'
    myobj = {'kld-from': account}
    x = requests.get(url, params = myobj, auth=HTTPBasicAuth(credential, key))
    return x.text

def retrieve_universidad(contract_instance, node, account, credential, key):
    url = 'https://u0z93so5ob-'+ node +'-connect.us0-aws.kaleido.io/instances/'+ contract_instance + '/retrieve_universidad'
    myobj = {'kld-from': account}
    x = requests.get(url, params = myobj, auth=HTTPBasicAuth(credential, key))
    return x.text

def retrieve_fecha_egreso(contract_instance, node, account, credential, key):
    url = 'https://u0z93so5ob-'+ node +'-connect.us0-aws.kaleido.io/instances/'+ contract_instance + '/retrieve_fecha_egreso'
    myobj = {'kld-from': account}
    x = requests.get(url, params = myobj, auth=HTTPBasicAuth(credential, key))
    return x.text

def retrieve_edad(contract_instance, node, account, credential, key):
    url = 'https://u0z93so5ob-'+ node +'-connect.us0-aws.kaleido.io/instances/'+ contract_instance + '/retrieve_edad'
    myobj = {'kld-from': account}
    x = requests.get(url, params = myobj, auth=HTTPBasicAuth(credential, key))
    return x.text

def retrieve_numero_telefonico(contract_instance, node, account, credential, key):
    url = 'https://u0z93so5ob-'+ node +'-connect.us0-aws.kaleido.io/instances/'+ contract_instance + '/retrieve_numero_telefonico'
    myobj = {'kld-from': account}
    x = requests.get(url, params = myobj, auth=HTTPBasicAuth(credential, key))
    return x.text

def retrieve_extras(contract_instance, node, account, credential, key):
    url = 'https://u0z93so5ob-'+ node +'-connect.us0-aws.kaleido.io/instances/'+ contract_instance + '/retrieve_extras'
    myobj = {'kld-from': account}
    x = requests.get(url, params = myobj, auth=HTTPBasicAuth(credential, key))
    return x.text

def retrieve_full(contract_instance, node, account, credential, key):
    url = 'https://u0z93so5ob-'+ node +'-connect.us0-aws.kaleido.io/instances/'+ contract_instance + '/retrieve_full'
    myobj = {'kld-from': account}
    x = requests.get(url, params = myobj, auth=HTTPBasicAuth(credential, key))
    return x.text

def store_nombre(contract_instance, node, account, credential, key, nombre):
    url = 'https://u0z93so5ob-'+ node +'-connect.us0-aws.kaleido.io/instances/'+ contract_instance + '/store_nombre'
    body = {"nom": nombre}
    myobj = {'kld-from': account}
    x = requests.post(url, data = body, params = myobj, auth=HTTPBasicAuth(credential, key))
    return x.text

def store_apellido(contract_instance, node, account, credential, key, apellido):
    url = 'https://u0z93so5ob-'+ node +'-connect.us0-aws.kaleido.io/instances/'+ contract_instance + '/store_apellido'
    body = {"ape": apellido}
    myobj = {'kld-from': account}
    x = requests.post(url, data = body, params = myobj, auth=HTTPBasicAuth(credential, key))
    return x.text

def store_titulo(contract_instance, node, account, credential, key, titulo):
    url = 'https://u0z93so5ob-'+ node +'-connect.us0-aws.kaleido.io/instances/'+ contract_instance + '/store_titulo'
    body = {"tit": titulo}
    myobj = {'kld-from': account}
    x = requests.post(url, data = body, params = myobj, auth=HTTPBasicAuth(credential, key))
    return x.text

def store_mencion(contract_instance, node, account, credential, key, mencion):
    url = 'https://u0z93so5ob-'+ node +'-connect.us0-aws.kaleido.io/instances/'+ contract_instance + '/store_mencion'
    body = {"men": mencion}
    myobj = {'kld-from': account}
    x = requests.post(url, data = body, params = myobj, auth=HTTPBasicAuth(credential, key))
    return x.text

def store_universidad(contract_instance, node, account, credential, key, universidad):
    url = 'https://u0z93so5ob-'+ node +'-connect.us0-aws.kaleido.io/instances/'+ contract_instance + '/store_universidad'
    body = {"uni": universidad}
    myobj = {'kld-from': account}
    x = requests.post(url, data = body, params = myobj, auth=HTTPBasicAuth(credential, key))
    return x.text

def store_fecha_egreso(contract_instance, node, account, credential, key, fecha_egreso):
    url = 'https://u0z93so5ob-'+ node +'-connect.us0-aws.kaleido.io/instances/'+ contract_instance + '/store_fecha_egreso'
    body = {"fec": fecha_egreso}
    myobj = {'kld-from': account}
    x = requests.post(url, data = body, params = myobj, auth=HTTPBasicAuth(credential, key))
    return x.text

def store_edad(contract_instance, node, account, credential, key, edad):
    url = 'https://u0z93so5ob-'+ node +'-connect.us0-aws.kaleido.io/instances/'+ contract_instance + '/store_edad'
    body = {"eda": edad}
    myobj = {'kld-from': account}
    x = requests.post(url, data = body, params = myobj, auth=HTTPBasicAuth(credential, key))
    return x.text

def store_numero_telefonico(contract_instance, node, account, credential, key, numero_telefonico):
    url = 'https://u0z93so5ob-'+ node +'-connect.us0-aws.kaleido.io/instances/'+ contract_instance + '/store_numero_telefonico'
    body = {"tel": numero_telefonico}
    myobj = {'kld-from': account}
    x = requests.post(url, data = body, params = myobj, auth=HTTPBasicAuth(credential, key))
    return x.text

def store_extras(contract_instance, node, account, credential, key, extras):
    url = 'https://u0z93so5ob-'+ node +'-connect.us0-aws.kaleido.io/instances/'+ contract_instance + '/store_extras'
    body = {"ext": extras}
    myobj = {'kld-from': account}
    x = requests.post(url, data = body, params = myobj, auth=HTTPBasicAuth(credential, key))
    return x.text

def store_full(contract_instance, node, account, credential, key, nombre, apellido, titulo, mencion, universidad, fecha_egreso, edad, numero_telefonico, extras):
    url = 'https://u0z93so5ob-'+ node +'-connect.us0-aws.kaleido.io/instances/'+ contract_instance + '/store_full'
    body = {"nom": nombre
            ,"ape": apellido
            ,"tit": titulo
            ,"men": mencion
            ,"uni": universidad
            ,"fec": fecha_egreso
            ,"eda": edad
            ,"tel": numero_telefonico
            ,"ext": extras}
    myobj = {'kld-from': account}
    x = requests.post(url, data = body, params = myobj, auth=HTTPBasicAuth(credential, key))
    return x.text

def constructor(node, account, credential, key):
    url = 'https://u0z93so5ob-'+ node +'-connect.us0-aws.kaleido.io/gateways/egresadov3/'
    myobj = {'kld-from': account, 'kld-sync': 'true'}
    x = requests.post(url, params = myobj, auth=HTTPBasicAuth(credential, key))
    return x.text




nodo = 'u0pa9ea7pt'
estudiante = '0x135f66683cad7e41ab1ad8b4cde47a1989d1a2ed'
cuenta = '0xce323273d94650803cf40c8654251af40b52455d'
credencial = 'u0gclpyeq3'
llave = 'l2hh8JBMo2O_HIrEyarNg2dkTZQ98Zjd-9k5-wrTe24'







