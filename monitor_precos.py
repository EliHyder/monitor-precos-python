import pandas as pd
from pathlib import Path
from datetime import datetime
import time # Adicionado para simular diferentes precos

def salvar_preco(preco, arquivo='precos.csv'):
    """Salva um preço com timestamp no histórico CSV."""
    
    # Cria o DataFrame de um único registro
    df = pd.DataFrame([[datetime.now(), preco]], columns=['Data', 'Preco'])
    
    # Verifica se o arquivo existe
    if Path(arquivo).is_file():
        # Se existe, adiciona sem cabeçalho no modo 'append'
        df.to_csv(arquivo, mode='a', header=False, index=False)
    else:
        # Se não existe, cria com cabeçalho
        df.to_csv(arquivo, index=False)

    print(f'Preço {preco} salvo com sucesso! em {arquivo}')

def analisar_historico(arquivo='precos.csv'):
    """Lê o histórico de preços e calcula métricas estatísticas."""
    try:
        df = pd.read_csv(arquivo)
        
        # Garante que 'Preco' é numérico para cálculos
        df['Preco'] = pd.to_numeric(df['Preco'], errors='coerce') 

        print("\n--- Análise do Histórico de Preços ---")
        print(f"Preço Mínimo: R$ {df['Preco'].min():.2f}")
        print(f"Preço Máximo: R$ {df['Preco'].max():.2f}")
        print(f"Preço Médio: R$ {df['Preco'].mean():.2f}")
        print(f"Total de Registros: {len(df)}")
        print("--------------------------------------")
        
    except FileNotFoundError:
        print("Arquivo de preços não encontrado para análise.")
        
# --- Simulação de uso ---

# 1. Primeira execução: Salva 125.50
salvar_preco(125.50)
time.sleep(1) # Espera 1 segundo para garantir timestamps diferentes

# 2. Simulação de queda de preço
salvar_preco(120.00)
time.sleep(1)

# 3. Simulação de alta de preço
salvar_preco(130.25)
time.sleep(1)

# 4. Analisa os três registros
analisar_historico()