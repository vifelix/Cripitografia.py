import hashlib
import time

string = input("Digite a senha a ser codificada: ")

menu= int(input(''' #### MENU - ESCOLHA O TIPO DE CRIPTOGRAFIA ####
                1) MD5
                2) SHA1
                3) SHA256
                4) SHA512
                Digite o tipo de Criptografia:'''))
if menu == 1:
    resultado = hashlib.md5(string.encode('utf-8'))
    print("Sua senha codificada em MD5 é: ", resultado.hexdigest())
elif menu == 2:
    resultado = hashlib.sha1(string.encode('utf-8'))
    print("Sua senha codificada em SHA1 é: ", resultado.hexdigest())
elif menu == 3:
    resultado = hashlib.sha256(string.encode('utf-8'))
    print("Sua senha codificada em SHA256 é: ", resultado.hexdigest())
elif menu == 4:
    resultado = hashlib.sha512(string.encode('utf-8'))
    print("Sua senha codificada em SHA512 é: ", resultado.hexdigest())
else:
    print('Algo de errado não esta certo')

time.sleep(60)