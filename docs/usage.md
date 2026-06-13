# Uso do Script de Previsão do Tempo

## Preparação

Certifique-se de ter instalado as dependências necessárias executando os comandos descritos no arquivo `README.md`.

## Uso do Script

Para usar o script, execute o seguinte comando no PowerShell:

```powershell
python src/main.py [cep]
```

Se você não fornecer o CEP como argumento, você será prompted a inseri-lo no terminal.

## Exemplos

Exemplo de uso com CEP forneido como argumento:

```powershell
python src/main.py 01001-000
```
Exemplo de uso sem CEP fornecido como argumento:

```powershell
python src/main.py
```

## Saída do Script

O script exibe as temperaturas para o CEP forneido (ou inserido) em diferentes unidades (celsius, kelvin e fahrenheit).