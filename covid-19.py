# Criado por Rafael Sousa Pereira
# GitHub : https://github.com/rafaellsousadev/covid-19

# Documentação do Pacote Covid : https://pypi.org/project/covid/

# Importando as bibliotecas necessárias
from covid import Covid
from datetime import datetime as dt


# definindo uma função CovidAtualizacaoMundo() para pegar as informações dos Casos de Covid-19brazil

def CovidAtualizacaoMundo():
    # buscar número de casos ativos confirmados & total de recuperadores & mortes
    total_casos_mundo_ativos = Covid().get_total_active_cases()
    total_casos_mundo_confirmados = Covid().get_total_confirmed_cases()
    total_casos_mundo_recuperado = Covid().get_total_recovered()
    total_casos_mundo_mortos = Covid().get_total_deaths()

    # Imprimindo os resultados
    print("\n============= INFORMAÇÕES DE CASOS DE COVID-19 =============")
    print("TOTAL ATIVOS :                   " + str(total_casos_mundo_ativos))
    print("TOTAL CONFIRMADOS :              " + str(total_casos_mundo_confirmados))
    print("TOTAL RECUPERADO :               " + str(total_casos_mundo_recuperado))
    print("TOTAL MORTOS :                   " + str(total_casos_mundo_mortos))


# Definindo CovidatualizacaoPorPaisEspecifico(): como país com argumento i_pais para obter N paises.
def CovidAtualizacaoPorPaisEspecifico(i_pais):
    # buscando informações do país de entrada do usuário
    info_especifica_pais_covid: dict = Covid().get_status_by_country_name(i_pais)

    total_casos_pais_ativos = info_especifica_pais_covid['active']
    total_casos_pais_confirmados = info_especifica_pais_covid['confirmed']
    total_casos_pais_recuperado = info_especifica_pais_covid['recovered']
    total_casos_pais_mortos = info_especifica_pais_covid['deaths']
    total_casos_pais_epoca = info_especifica_pais_covid['last_update']
    dados_atualizados_as = dt.fromtimestamp(total_casos_pais_epoca / 1000)

    # Imprimindo os resultados
    print("\n" + i_pais + " : INFORMAÇÕES DO COVID-19")
    print("TOTAL ATIVOS :                   " + str(total_casos_pais_ativos))
    print("TOTAL CONFIRMADOS :              " + str(total_casos_pais_confirmados))
    print("TOTAL RECUPERADO :               " + str(total_casos_pais_recuperado))
    print("TOTAL MORTOS :                   " + str(total_casos_pais_mortos))
    print("ÚLTIMOS CASOS ÁS :               " + str(dados_atualizados_as))


# Run Code
if __name__ == '__main__':
    CovidAtualizacaoMundo()
    pais = str(input("\nEntre com o nome do País :       \n"))
    CovidAtualizacaoPorPaisEspecifico(pais)
