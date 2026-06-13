# API do Script de Previsão do Tempo

## Funções

### normalize_cep(cep: str) -> str

Remoce formatação do número do CEP e verifica se tem 8 dígitos.

### celsius_to_kelvin(celsius: float) -> float

Converte a temperatura de celsius para kelvin.

### celsius_to_fahrenheit(celsius: float) -> float

Converte a temperatura de celsius para fahrenheit.

### cep_to_coordinates(cep: str) -> tuple[float, float]

Obtem as coordenadas geográficas para o CEP fornecido.

### get_temperature_celsius(lat: float, lon: float) -> float

Obtem a temperatura atual em celsius para as coordenadas geográficas fornecidas.