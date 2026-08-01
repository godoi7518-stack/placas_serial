import pandas as pd

# 1. Caminho do arquivo
caminho_arquivo = "serial_placas_oppo.xlsx"

# 2. Carrega a planilha e limpa as colunas
df = pd.read_excel(caminho_arquivo)
df["S/N"] = df["S/N"].astype(str).str.strip()
df["CODIGO"] = df["CODIGO"].astype(str).str.strip()

# 3. Cria o mapa de consulta
mapa_seriais = dict(zip(df["S/N"], df["CODIGO"]))

print("--- SISTEMA DE BUSCA DE CÓDIGOS ---")
print("Para encerrar o programa, digite 'sair' e aperte Enter.\n")

while True:
    entrada = input("Bipe o próximo serial: ").strip()

    # Verifica encerramento
    if entrada.lower() == "sair":
        print("\nEncerrando o programa. Até logo!")
        break

    # Se pressionar Enter sem digitar nada
    if not entrada:
        continue

    # Corta o serial (ajuste entrada[2:7] se necessário)
    serial_busca = entrada[2:7]

    # Busca na planilha
    codigo_encontrado = mapa_seriais.get(serial_busca)

    if codigo_encontrado:
        print(f"-> Código correspondente: {codigo_encontrado}")
    else:
        print(f"-> Serial '{serial_busca}' não foi encontrado na planilha.")

    print("-" * 40)