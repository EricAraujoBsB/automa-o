from reportlab.lib.validators import isNumber
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from data.conexao import supabase

def inserir_dados_bd(value_atual):
    """
    realiza a inserção de dados do valor atual na base de dados, será inserida com periodicidade pelo looping da automação
    """
    if value_atual == "":
        raise ValueError('Dados Insuficientes.')
    
    try:
        resposta = (
            supabase.table("ISE2")
            .insert({
                "value": value_atual
            })
            .execute()
        )
        return resposta.data
    except Exception as error:
        raise error
