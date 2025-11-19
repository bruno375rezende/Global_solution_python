import pandas as pd

def coletar_dados():
    def input_questao(pergunta):
        return input(pergunta + ": ")
    
    nome = input_questao("Digite seu nome")
    idade = int(input_questao("Digite sua idade"))
    area_interesse = input_questao("Área de interesse (ex: TI, Gestão, Design, Ciências Humanas)")
    return {"Nome": nome, "Idade": idade, "Área": area_interesse}

def coletar_varios_usuarios():
    usuarios = []
    while True:
        usuario = coletar_dados()
        usuarios.append(usuario)
        continuar = input("Deseja adicionar outro usuário? (s/n): ").lower()
        if continuar != "s":
            break
    return usuarios

def criar_dataframe(dados):
    df = pd.DataFrame(dados)
    return df

def recomendar_carreira(df):
    recomendacoes = []
    for i, row in df.iterrows():
        if row["Área"].lower() == "ti":
            recomendacao = "Especialista em IA ou Robótica"
        elif row["Área"].lower() == "gestão":
            recomendacao = "Gestor de Transformação Digital"
        elif row["Área"].lower() == "design":
            recomendacao = "Designer de Ambientes Imersivos"
        else:
            recomendacao = "Consultor de Soft Skills e Futuro do Trabalho"
        recomendacoes.append(recomendacao)
    df["Recomendação"] = recomendacoes
    return df

def mostrar_resultados(df):
    print("\n=== Relatório de Recomendações ===")
    print(df)

def main():
    dados_usuarios = coletar_varios_usuarios()
    df = criar_dataframe(dados_usuarios)
    df = recomendar_carreira(df)
    mostrar_resultados(df)

if __name__ == "__main__":
    main()
