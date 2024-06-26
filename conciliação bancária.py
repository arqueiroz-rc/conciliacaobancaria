
import pandas as pd

def reconciliacao_bancaria(extrato_empresa_csv, extrato_banco_csv):
   
    extrato_empresa = pd.read_csv(extrato_empresa_csv)
    extrato_banco = pd.read_csv(extrato_banco_csv)
    
    discrepancias = pd.merge(extrato_empresa, extrato_banco, on=['data', 'lançamento', 'número do documento', 'valor', 'tipo do lançamento'], how='outer', indicator=True).query('_merge != "both"')
    return discrepancias

extrato_empresa_csv = 'extrato_empresa.csv'
extrato_banco_csv = 'extrato_banco.csv'

discrepancias = reconciliacao_bancaria(extrato_empresa_csv, extrato_banco_csv)

print("Discrepâncias encontradas:")
print(discrepancias)
