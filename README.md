# Bipagem de Placas — Multilaser

Site estático para bipar o serial (S/N) de uma placa e consultar o código correspondente, sem precisar instalar nada. Qualquer pessoa da empresa com o link consegue usar.

🔗 **Site no ar:** https://godoi7518-stack.github.io/placas_serial/

---

## O que é

Esse site nasceu de um script Python (pandas) que bipava o serial de uma placa e retornava o código dela consultando uma planilha. A ideia aqui foi transformar isso num site que todo mundo da empresa acessa direto do navegador — sem instalar Python, sem rodar script, sem depender de máquina específica.

O usuário final só bipa. Quem altera dados ou funcionamento do site é só o dono do projeto (via GitHub).

## Arquivos do projeto

| Arquivo | Para que serve |
|---|---|
| `index.html` | O site em si — tema claro/escuro, campo de bipagem, histórico da sessão, painel de sugestão de placa nova |
| `dados.js` | Base de dados (S/N → código) já embutida no site, gerada a partir da planilha |
| `gerar_dados.py` | Script que regenera o `dados.js` sempre que a planilha muda |
| `serial_placas_oppo_corrigido.xlsx` | Planilha oficial, fonte da verdade dos dados |
| `README.md` | Este arquivo |

## Como usar (usuário final)

1. Acessa o link do site
2. Bipa o serial no campo de leitura
3. O código aparece na hora — encontrado (verde) ou não encontrado (vermelho)
4. O histórico da sessão fica visível na tabela abaixo, com contagem de bipados/encontrados/não encontrados
5. **Sempre confirme o código no SAP antes de usar.** Os dados ficam só no navegador — nada é enviado a servidor nenhum, exceto sugestões de placa nova (ver abaixo)

## Como atualizar a base de dados (dono do projeto)

1. Edita a planilha oficial (`serial_placas_oppo_corrigido.xlsx`) com os dados novos/corrigidos
2. Roda no terminal, dentro da pasta do projeto:
   ```
   python gerar_dados.py nome_da_planilha.xlsx
   ```
   Isso substitui o `dados.js`
3. Sobe a alteração:
   ```
   git add .
   git commit -m "Atualiza base de dados"
   git push
   ```
4. O site atualiza sozinho no GitHub Pages em 1–2 minutos

## Sugestão de placa nova (usuário final → aprovação do dono)

A partir da v1.0.0, quem usa o site pode sugerir a inclusão de uma placa que não está na base:

1. Preenche descrição, modelo e código sugerido
2. Bipa o mesmo S/N **3 vezes seguidas** para confirmar a leitura
3. Se as 3 bipagens baterem, o botão de envio libera
4. Ao enviar, a sugestão vai por e-mail (via Formspree) para o dono do projeto

**Importante:** nada entra na base de dados automaticamente. Toda sugestão é validada manualmente pelo dono, que decide se inclui na planilha oficial e roda o fluxo de atualização normal (`gerar_dados.py` → commit → push).

### Configuração necessária (só uma vez)

Antes desse recurso funcionar em produção, o dono do projeto precisa:

1. Criar uma conta grátis em [formspree.io](https://formspree.io)
2. Criar um form e copiar o endpoint gerado (formato `https://formspree.io/f/xxxxxxx`)
3. Abrir o `index.html`, achar a linha:
   ```javascript
   const FORMSPREE_ENDPOINT = "https://formspree.io/f/SEU_ID_AQUI";
   ```
   e trocar `SEU_ID_AQUI` pelo endpoint real
4. Confirmar o e-mail de verificação que o Formspree envia
5. Subir a alteração (`git add . && git commit && git push`)

Sem esse passo, o botão de enviar sugestão retorna erro.

## Quem pode ver vs. alterar

- **Ver e usar:** qualquer pessoa com o link. Pode até "forkar" (copiar) o repositório, já que é público
- **Alterar dados ou funcionamento:** só quem tem acesso de escrita no repositório `godoi7518-stack/placas_serial` (por padrão, só o dono)

## Versionamento

O número de versão aparece no rodapé do site (`vX.Y.Z`), controlado pela constante `APP_VERSION` no `index.html`. Segue [semver](https://semver.org/lang/pt-BR/) (major.minor.patch):

- **major**: mudança que quebra algo ou muda o funcionamento de forma significativa
- **minor**: nova funcionalidade, sem quebrar o que já existe
- **patch**: correção de bug ou ajuste pequeno

### Histórico de versões

| Versão | O que mudou |
|---|---|
| **1.0.0** | Primeira release pública. Site funcional com bipagem, histórico, tema claro/escuro. Adiciona painel de sugestão de placa nova (3 bipagens + aprovação por e-mail) e número de versão no rodapé |

---

*Dúvidas ou problemas: fale com o responsável pelo projeto antes de alterar qualquer arquivo.*
