import pandas as pd


dados_viagem = {
    'Destino': ['Alicante', 'Valência', 'Moscou', 'Tóquio', 'Roma'],
    'Clima': ['Praia', 'Praia', 'Frio', 'Urbano', 'Histórico'],
    'Orcamento': ['Moderado', 'Moderado', 'Alto', 'Alto', 'Moderado'],
    'Estilo': ['Relaxar', 'Praia e Sol', 'Cutura', 'Tecnologia', 'Cultura']
}

df_destinos = pd.DataFrame(dados_viagem)
print(df_destinos)


print("\n --- SISTEMA DE RECOMENDAÇÃO DE VIAGEM ---")
print("Escolha o Clima:")
print("1 - Praia")
print("2 - Frio")
print("3 - Urbano")
print("4 - Histórico")

opcao_clima = input("Digite o número do clima desejado: ")



if opcao_clima == '1':
    clima_escolhido = 'Praia'
elif opcao_clima == '2':
    clima_escolhido = 'Frio'
elif opcao_clima == '3':
    clima_escolhido = 'Urbano'
elif opcao_clima == '4':
    clima_escolhido = 'Histórico'
else:
    clima_escolhido = 'Inválido'


if clima_escolhido != 'Inválido':
    recomendados = df_destinos[df_destinos['Clima'] == clima_escolhido]
    
    print("\n--- DESTINOS RECOMENDADOS PARA VOCÊ ---")
    print(recomendados[['Destino', 'Orcamento', 'Estilo']])
else:
    print("Opção inválida! Reinicie o programa.")