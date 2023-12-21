from datetime import datetime, timedelta

def calcular_data_apos_dias(numero_de_dias):
    # Obtendo a data atual
    data_atual = datetime.now()

    # Calculando a data após o número de dias especificado
    data_resultante = data_atual + timedelta(days=numero_de_dias)

    return data_resultante

# Definindo o número de dias desejado
numero_de_dias = 0

# Calcular a data resultante
data_resultante = calcular_data_apos_dias(numero_de_dias)

# Exibindo o resultado
print(f"A data daqui a {numero_de_dias} dias será: {data_resultante.strftime('%Y-%m-%d')}")
