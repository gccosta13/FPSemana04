import json

path = input()

try:
    with open(path, 'r', encoding='utf8') as file:
        data = json.load(file)
        # imprimir os dados do ficheiro json
        print(data)
except Exception:
    print("Ocorreu um erro!")
finally:
    print("Processo concluído!")
