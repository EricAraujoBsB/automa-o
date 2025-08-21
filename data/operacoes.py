# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from .conexao import supabase

def inserir_dados_bd(value_atual):
    """
    realiza a inserção de dados do valor atual na base de dados, será inserida com periodicidade pelo looping da automação
    """
    if value_atual == "":
        raise ValueError('Dados Insuficientes.')
    
    try:
        resposta = (
            supabase.table("ise2")
            .insert({
                "value": value_atual
            })
            .execute()
        )
        return resposta.data
    except Exception as error:
        raise error


if __name__ == "__main__":
    try:
        inserir_dados_bd(32956)
        print("inserção bem sucedida")
    except Exception as error:
        print(f"falha ao comunicar com o banco de dados: {error}")