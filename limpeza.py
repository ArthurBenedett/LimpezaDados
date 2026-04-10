import pandas as pd
import json

#leitura dos dados criados
dados = pd.read_csv('dados_hospitalares.csv').to_dict('records')
sensores = json.load(open('sensores.json'))

with open('notas.txt', 'r', encoding='latin-1') as f:
    texto = f.read()

if 'Hipertensão' in texto:
    print("A palavra 'Hipertensão' foi encontrada nas notas.")
else:
    print("A palavra 'Hipertensão' NÃO foi encontrada nas notas.")

hip = {101: True, 103: False, 105: True}

bpm = {}

for s in sensores:
    if len(s['leituras']) > 0:
        media = sum(s['leituras']) / len(s['leituras'])

        if s['unidade'] == 'Hz':
            media = media * 60

        bpm[s['id']] = media

for p in dados:
    idade = int(p['v1'])

    if idade < 0 or idade > 120:
        idade = 0

    uid = p['uid']

    p['bpm_medio'] = bpm.get(uid, 0)
    p['tem_hipertensao'] = hip.get(uid, False)

soma = 0
cont = 0

for p in dados:
    if p['local'] == 'São Paulo' and p['tem_hipertensao']:
        soma += p['bpm_medio']
        cont += 1

print("-" * 20)

if cont > 0:
    print("media BPM:", soma / cont)
else:
    print("media BPM: 0")

print("-" * 20)

