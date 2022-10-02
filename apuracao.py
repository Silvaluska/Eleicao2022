import time
import requests
import json
import pandas as pd

while True:
	data = requests.get('https://resultados.tse.jus.br/oficial/ele2022/544/dados-simplificados/br/br-c0001-e000544-r.json')
	json_data = json.loads(data.content)

	candidatos = []
	partido = []
	votos = []
	porcentagem = []

	for informacoes in json_data['cand']:
		if informacoes['seq'] == '1' or informacoes['seq'] == '2' or informacoes['seq'] == '3' or informacoes['seq'] == '4' or informacoes['seq'] == '5' or informacoes['seq'] == '6' or informacoes['seq'] == '7' or informacoes['seq'] == '8' or informacoes['seq'] == '9':
			candidatos.append(informacoes['nm'])
			partido.append(informacoes['cc'])
			votos.append(informacoes['vap'])
			porcentagem.append(informacoes['pvap'])

	apuracao = pd.DataFrame(list(zip(candidatos,partido, votos, porcentagem)), columns=['Candidato', 'Partido', 'Nº Votos', 'Porcentagem'])
	print(apuracao)
	time.sleep(20)
	for i in range(10):
		print('')