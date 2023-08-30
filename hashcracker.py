import hashlib

hash_file = ""

dic_file = input("Ingrese la direccion del archivo del diccionario: ")
with open(dic_file, 'r') as file:
    diccionario = [line.strip for line in file]
    for password in diccionario:
        hash_calculado = hashlib.sha256(password.encode()).hexdigest()
