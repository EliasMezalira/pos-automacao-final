# Documentação Técnica

## Introdução
Esse é o repositório do projeto "pos-pipelines - Test Coverage", que visa analisar cobertura de testes usando `coverage` (unittest).

## Requisitos
- Python 3.x instalado no computador
- Acesso à internet para executar os testes de integração

## Comandos
### Instalar Dependências
No PowerShell, a partir da raiz do projeto (`c:\Users\elias\Documents\sources\pos-pipelines`):

```powershell
python -m pip install --user -r requirements.txt
```

### Executar Cobertura
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
