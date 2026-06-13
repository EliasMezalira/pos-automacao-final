# Como Usar o Script

## Pré-requisitos
- Python 3.x instalado no computador
- Acesso à internet para executar os testes de integração

## Passo a Passo
### 1. Instale as Dependências
No PowerShell, a partir da raiz do projeto (`c:\Users\elias\Documents\sources\pos-pipelines`), execute o seguinte comando:

```powershell
python -m pip install --user -r requirements.txt
```

### 2. Execute o Script
A partir da raiz do projeto, execute o script principal utilizando o seguinte comando:

```bash
python src/main.py
```

### Argumentos
O script pode ser executado passando um argumento, o CEP a ser buscado, no formato "00000-000". Caso não seja passado nenhum argumento, será solicitado ao usuário para informar o CEP.

## Exemplos
- Executar o script com o CEP "01001-000":

``python src/main.py 01001-000``

- Executar o script sem argumento, informando o CEP ao usuário:

``python src/main.py``
