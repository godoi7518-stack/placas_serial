# Bipagem de Placas — Busca de Código por Serial

Site interno para bipar o serial (S/N) de uma placa e encontrar o código correspondente, consultando uma base de dados própria. Feito pra substituir a busca manual em planilha.

🔗 **Site publicado:** https://godoi7518-stack.github.io/placas_serial/

## Como usar

1. Abra o link acima em qualquer dispositivo (celular, PC, tablet).
2. Clique no campo de bipagem e bipe o serial da placa com o leitor (ou digite e aperte Enter).
3. O código correspondente aparece na hora, junto com modelo/descrição quando disponíveis.
4. Um histórico da sessão fica logo abaixo, com contador de bipados / encontrados / não encontrados.

Não precisa instalar nada nem fazer login — é só abrir o link.

## Arquivos do projeto

| Arquivo | Para que serve |
|---|---|
| `index.html` | O site em si (interface, tema claro/escuro, lógica de busca) |
| `dados.js` | Base de dados (serial → código) já embutida no site |
| `gerar_dados.py` | Script Python que gera o `dados.js` a partir da planilha oficial |

Só quem tem acesso a este repositório consegue alterar a base de dados ou o funcionamento do site — a página pública não tem nenhuma opção de edição, upload ou configuração para o usuário final.

## Como atualizar a base de dados

Quando a planilha oficial mudar (placa nova, código corrigido, etc.):

```bash
pip install pandas openpyxl
python gerar_dados.py nome_da_planilha.xlsx
```

Isso sobrescreve o `dados.js` com os dados novos. Depois, suba a alteração:

```bash
git add .
git commit -m "atualiza base de dados"
git push
```

Em 1–2 minutos o site publicado já reflete a mudança.

## Observação sobre os dados

Este repositório é público (exigência do GitHub Pages no plano gratuito), então qualquer pessoa com acesso ao link consegue ver o conteúdo de `dados.js` pelo código-fonte da página, não só usar a busca.
