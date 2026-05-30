import json
import sys
import urllib.parse
import urllib.request

USER_AGENT = "pos-pipelines-weather-script/1.0"


def get_json(url: str) -> dict:
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(request, timeout=20) as response:
        body = response.read().decode("utf-8")
        return json.loads(body)


def normalize_cep(cep: str) -> str:
    only_digits = "".join(ch for ch in cep if ch.isdigit())
    if len(only_digits) != 8:
        raise ValueError("CEP deve conter 8 dígitos.")
    return only_digits


def cep_to_coordinates(cep: str) -> tuple[float, float]:
    cep = normalize_cep(cep)
    query = urllib.parse.urlencode({
        "postalcode": cep,
        "country": "Brazil",
        "format": "json",
        "limit": 1,
    })
    url = f"https://nominatim.openstreetmap.org/search?{query}"
    results = get_json(url)
    if not results:
        raise ValueError(f"Nenhum local encontrado para o CEP {cep}.")
    item = results[0]
    return float(item["lat"]), float(item["lon"])


def get_temperature_celsius(lat: float, lon: float) -> float:
    query = urllib.parse.urlencode({
        "latitude": lat,
        "longitude": lon,
        "current_weather": "true",
        "temperature_unit": "celsius",
        "timezone": "auto",
    })
    url = f"https://api.open-meteo.com/v1/forecast?{query}"
    data = get_json(url)
    current = data.get("current_weather")
    if not current or "temperature" not in current:
        raise RuntimeError("Não foi possível obter a temperatura atual.")
    return float(current["temperature"])


def celsius_to_kelvin(celsius: float) -> float:
    return celsius + 273.15


def celsius_to_fahrenheit(celsius: float) -> float:
    return (celsius * 9.0 / 5.0) + 32.0


def main() -> None:
    if len(sys.argv) > 1:
        cep = sys.argv[1]
    else:
        cep = input("Informe o CEP (apenas números ou formatado): ").strip()

    try:
        lat, lon = cep_to_coordinates(cep)
        temperatura_c = get_temperature_celsius(lat, lon)

        temperatura_k = celsius_to_kelvin(temperatura_c)
        temperatura_f = celsius_to_fahrenheit(temperatura_c)

        print("Temperaturas para o CEP", cep)
        print(f"isso é um teste de commit")
        print(f"- Celsius   : {temperatura_c:.1f} °C")
        print(f"- Kelvin    : {temperatura_k:.2f} K")
        print(f"- Fahrenheit: {temperatura_f:.1f} °F")
    except Exception as error:
        print("Erro:", error)
        sys.exit(1)


if __name__ == "__main__":
    main()