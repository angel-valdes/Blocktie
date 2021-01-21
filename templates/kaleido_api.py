import requests
from requests.auth import HTTPBasicAuth


def retrieve_nombre(contract_instance, node, account, credential, key):
    url = 'https://u0nik2513u-' + node + '-connect.us0-aws.kaleido.io/instances/' + contract_instance + '/retreive_nombre'
    myobj = {'kld-from': account}
    x = requests.get(url, params=myobj, auth=HTTPBasicAuth(credential, key))
    return x.text


def retrieve_apellido(contract_instance, node, account, credential, key):
    url = 'https://u0nik2513u-' + node + '-connect.us0-aws.kaleido.io/instances/' + contract_instance + '/retreive_apellido'
    myobj = {'kld-from': account}
    x = requests.get(url, params=myobj, auth=HTTPBasicAuth(credential, key))
    return x.text


def retrieve_titulo(contract_instance, node, account, credential, key):
    url = 'https://u0nik2513u-' + node + '-connect.us0-aws.kaleido.io/instances/' + contract_instance + '/retreive_titulo'
    myobj = {'kld-from': account}
    x = requests.get(url, params=myobj, auth=HTTPBasicAuth(credential, key))
    return x.text


def retrieve_mencion(contract_instance, node, account, credential, key):
    url = 'https://u0nik2513u-' + node + '-connect.us0-aws.kaleido.io/instances/' + contract_instance + '/retreive_mencion'
    myobj = {'kld-from': account}
    x = requests.get(url, params=myobj, auth=HTTPBasicAuth(credential, key))
    return x.text


def retrieve_universidad(contract_instance, node, account, credential, key):
    url = 'https://u0nik2513u-' + node + '-connect.us0-aws.kaleido.io/instances/' + contract_instance + '/retreive_universidad'
    myobj = {'kld-from': account}
    x = requests.get(url, params=myobj, auth=HTTPBasicAuth(credential, key))
    return x.text


def retrieve_fecha_egreso(contract_instance, node, account, credential, key):
    url = 'https://u0nik2513u-' + node + '-connect.us0-aws.kaleido.io/instances/' + contract_instance + '/retreive_fecha_egreso'
    myobj = {'kld-from': account}
    x = requests.get(url, params=myobj, auth=HTTPBasicAuth(credential, key))
    return x.text


def retrieve_edad(contract_instance, node, account, credential, key):
    url = 'https://u0nik2513u-' + node + '-connect.us0-aws.kaleido.io/instances/' + contract_instance + '/retreive_edad'
    myobj = {'kld-from': account}
    x = requests.get(url, params=myobj, auth=HTTPBasicAuth(credential, key))
    return x.text


def retrieve_numero_telefonico(contract_instance, node, account, credential, key):
    url = 'https://u0nik2513u-' + node + '-connect.us0-aws.kaleido.io/instances/' + contract_instance + '/retreive_numero_telefonico'
    myobj = {'kld-from': account}
    x = requests.get(url, params=myobj, auth=HTTPBasicAuth(credential, key))
    return x.text


def retrieve_extras(contract_instance, node, account, credential, key):
    url = 'https://u0nik2513u-' + node + '-connect.us0-aws.kaleido.io/instances/' + contract_instance + '/retreive_extras'
    myobj = {'kld-from': account}
    x = requests.get(url, params=myobj, auth=HTTPBasicAuth(credential, key))
    return x.text


def store_nombre(contract_instance, node, account, credential, key, nombre):
    url = 'https://u0nik2513u-' + node + '-connect.us0-aws.kaleido.io/instances/' + contract_instance + '/store_nombre'
    body = {"nom": nombre}
    myobj = {'kld-from': account}
    x = requests.post(url, data=body, params=myobj, auth=HTTPBasicAuth(credential, key))
    return x.text


def store_apellido(contract_instance, node, account, credential, key, apellido):
    url = 'https://u0nik2513u-' + node + '-connect.us0-aws.kaleido.io/instances/' + contract_instance + '/store_apellido'
    body = {"ape": apellido}
    myobj = {'kld-from': account}
    x = requests.post(url, data=body, params=myobj, auth=HTTPBasicAuth(credential, key))
    return x.text


def store_titulo(contract_instance, node, account, credential, key, titulo):
    url = 'https://u0nik2513u-' + node + '-connect.us0-aws.kaleido.io/instances/' + contract_instance + '/store_titulo'
    body = {"tit": titulo}
    myobj = {'kld-from': account}
    x = requests.post(url, data=body, params=myobj, auth=HTTPBasicAuth(credential, key))
    return x.text


def store_mencion(contract_instance, node, account, credential, key, mencion):
    url = 'https://u0nik2513u-' + node + '-connect.us0-aws.kaleido.io/instances/' + contract_instance + '/store_mencion'
    body = {"men": mencion}
    myobj = {'kld-from': account}
    x = requests.post(url, data=body, params=myobj, auth=HTTPBasicAuth(credential, key))
    return x.text


def store_universidad(contract_instance, node, account, credential, key, universidad):
    url = 'https://u0nik2513u-' + node + '-connect.us0-aws.kaleido.io/instances/' + contract_instance + '/store_universidad'
    body = {"uni": universidad}
    myobj = {'kld-from': account}
    x = requests.post(url, data=body, params=myobj, auth=HTTPBasicAuth(credential, key))
    return x.text


def store_fecha_egreso(contract_instance, node, account, credential, key, fecha_egreso):
    url = 'https://u0nik2513u-' + node + '-connect.us0-aws.kaleido.io/instances/' + contract_instance + '/store_fecha_egreso'
    body = {"fec": fecha_egreso}
    myobj = {'kld-from': account}
    x = requests.post(url, data=body, params=myobj, auth=HTTPBasicAuth(credential, key))
    return x.text


def store_edad(contract_instance, node, account, credential, key, edad):
    url = 'https://u0nik2513u-' + node + '-connect.us0-aws.kaleido.io/instances/' + contract_instance + '/store_edad'
    body = {"eda": edad}
    myobj = {'kld-from': account}
    x = requests.post(url, data=body, params=myobj, auth=HTTPBasicAuth(credential, key))
    return x.text


def store_numero_telefonico(contract_instance, node, account, credential, key, numero_telefonico):
    url = 'https://u0nik2513u-' + node + '-connect.us0-aws.kaleido.io/instances/' + contract_instance + '/store_numero_telefonico'
    body = {"tel": numero_telefonico}
    myobj = {'kld-from': account}
    x = requests.post(url, data=body, params=myobj, auth=HTTPBasicAuth(credential, key))
    return x.text


def store_extras(contract_instance, node, account, credential, key, extras):
    url = 'https://u0nik2513u-' + node + '-connect.us0-aws.kaleido.io/instances/' + contract_instance + '/store_extras'
    body = {"ext": extras}
    myobj = {'kld-from': account}
    x = requests.post(url, data=body, params=myobj, auth=HTTPBasicAuth(credential, key))
    return x.text


def constructor(node, account, credential, key):
    url = 'https://u0nik2513u-' + node + '-connect.us0-aws.kaleido.io/gateways/u0urhd24kn/'
    myobj = {'kld-from': account, 'kld-sync': 'true'}
    x = requests.post(url, params=myobj, auth=HTTPBasicAuth(credential, key))
    return x.text


nodo = 'u0hfw6oxln' # nodo
cuenta = '0xbf330abd2c67eedccf6bf70e9a353dbd3e14c11d' # cuenta
credencial = 'u0ttm7jh4b' # usuario
estudiante = '0xe98270e870227257b325f656ea7b17032574d57c'
llave = 'GzFQoxBhtXAgV7o7wKgvLnJrCe-e_1LQnJ-p7Id_Vr0' # password

