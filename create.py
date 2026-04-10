import pandas as pd
import json

# Criando CSV Mascarado (uid=ID, v1=Idade, v2=Escolaridade)
csv_data = {
    'uid': [101, 102, 103, 104, 105],
    'v1': [45, -5, '62', 50, 250], 
    'v2': ['Superior', 'médio', 'Pós-Graduação', 'superior', 'médio'],
    'local': ['São Paulo', 'Curitiba', 'São Paulo', 'Belo Horizonte', 'Curitiba']
}
pd.DataFrame(csv_data).to_csv('dados_hospitalares.csv', index=False)

# Criando JSON com escalas variadas (Hz vs BPM)
json_data = [
    {'id': 101, 'unidade': 'BPM', 'leituras': [80, 85, 90]},
    {'id': 103, 'unidade': 'Hz',  'leituras': [1.5, 1.6, 1.7]}, 
    {'id': 105, 'unidade': 'BPM', 'leituras': []}
]
with open('sensores.json', 'w') as f:
    json.dump(json_data, f)

# Criando Notas Médicas (Não Estruturado)
with open('notas.txt', 'w') as f:
    f.write('ID:101 - Paciente com Hipertensão severa. ID:103 - Quadro estável. ID:105 - Apresenta Hipertensão.')

print('✅ Arquivos gerados com sucesso!')