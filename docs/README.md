# pos-pipelines — Test Coverage

Comandos para analisar cobertura de testes usando `coverage` (unittest).

## Instalação de Dependências

Para instalar as dependências necessárias, execute o seguinte comando no PowerShell:

```powershell
python -m pip install --user -r requirements.txt
```

## Execução de Cobertura de Testes

Para executar a cobertura de testes para todos os testes (unitários + integração), execute os seguintes comandos:

```powershell
python -m coverage run -m unittest discover -s tests
python -m coverage report -m
python -m coverage html
```

Para executar a cobertura de testes apenas para testes de unidade, execute os seguintes comandos:

```powershell
python -m coverage run -m unittest tests.test_main_unit
python -m coverage report -m
python -m coverage html
```

## Resultados da Cobertura de Testes

Os resultados textuais da cobertura de testes serão exibidos no terminal; o relatório HTML será gerado em `htmlcov/`.