"""
Gera o arquivo dados.js do site a partir da planilha oficial (.xlsx).

Uso:
    pip install pandas openpyxl
    python gerar_dados.py serial_placas_oppo.xlsx

Isso sobrescreve dados.js. Depois é só subir o arquivo atualizado pro
mesmo lugar onde o site está hospedado (substituindo o antigo).
"""
import sys
import json
import pandas as pd

def main():
    if len(sys.argv) < 2:
        print("Uso: python gerar_dados.py caminho_da_planilha.xlsx")
        sys.exit(1)

    caminho_arquivo = sys.argv[1]
    df = pd.read_excel(caminho_arquivo)

    df["S/N"] = df["S/N"].astype(str).str.strip()
    df["CODIGO"] = df["CODIGO"].astype(str).str.strip()

    col_desc = "DESCRIÇÃO" if "DESCRIÇÃO" in df.columns else ("DESCRICAO" if "DESCRICAO" in df.columns else None)
    col_modelo = "MODELO" if "MODELO" in df.columns else None

    registros = []
    for _, row in df.iterrows():
        sn = str(row["S/N"]).strip()
        if not sn or sn.lower() == "nan":
            continue

        def val(col):
            if not col or col not in df.columns:
                return ""
            v = row[col]
            if pd.isna(v):
                return ""
            return str(v).strip()

        registros.append({
            "sn": sn,
            "codigo": val("CODIGO"),
            "descricao": val(col_desc),
            "modelo": val(col_modelo),
        })

    with open("dados.js", "w", encoding="utf-8") as f:
        f.write("// Base de dados das placas — gerado automaticamente por gerar_dados.py\n")
        f.write("// Não editar manualmente: atualize a planilha e rode o script de novo.\n")
        f.write("const DADOS_PLACAS = ")
        json.dump(registros, f, ensure_ascii=False, indent=2)
        f.write(";\n")

    print(f"OK: {len(registros)} seriais escritos em dados.js")

if __name__ == "__main__":
    main()
