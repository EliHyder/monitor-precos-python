import pandas as pd
from pathlib import Path
from datetime import datetime

def salvar_preco(preco, arquivo='precos.csv'):
    
    if Path(arquivo).is_file():
        df = pd.DataFrame([[datetime.now(), preco]], columns=['Data', 'Preco'])
        df.to_csv(arquivo, mode='a', header=False, index=False)
    else:
        df = pd.DataFrame([[datetime.now(), preco]], columns=['Data', 'Preco'])
        df.to_csv(arquivo, index=False)

    print(f'Preço {preco} salvo com sucesso! em {arquivo}')

preco_simulado = 125.50
salvar_preco(preco_simulado)