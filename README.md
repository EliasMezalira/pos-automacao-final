# pos-pipelines — Test Coverage

Comandos para analisar cobertura de testes usando `coverage` (unittest).

No PowerShell, a partir da raiz do projeto (`c:\Users\elias\Documents\sources\pos-pipelines`):

- Instalar dependências:

```powershell
python -m pip install --user -r requirements.txt
```

- Executar cobertura para todos os testes (unitários + integração):

```powershell
python -m coverage run -m unittest discover -s tests
python -m coverage report -m
python -m coverage html
```

- Executar cobertura apenas para testes de unidade (recomendado para evitar dependências de rede):

```powershell
python -m coverage run -m unittest tests.test_main_unit
python -m coverage report -m
python -m coverage html
```

Os resultados textuais aparecerão no terminal; o relatório HTML será gerado em `htmlcov/`.
