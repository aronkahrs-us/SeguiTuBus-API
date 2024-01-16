# Seguí Tu Bus (Tres Cruces) API Wrapper 🇺🇾

This Python package provides a convenient wrapper for interacting with the [Seguí Tu Bus (Tres Cruces)](https://trescruces.com.uy/seguitubus/) API in Uruguay 🇺🇾. It allows you to retrieve various information related to Bus services.

## Table of Contents
- [Usage](#usage)
- [Examples](#examples)
- [Contributing](#contributing)
- [License](#license)


## Usage

Import the `STB` class from the package and create an instance:

```python
from SeguiTuBus import STB

client = STB()
```

### Available Methods

- `list_serv(Empresa, HoraInicio, Origen, Destino, NroServicio, VarianteServicio)`: Get bus services and filters according to parameters.
- `info_bus(Bus)`: Get specific bus information.
- `list_serv_map(Empresa, HoraInicio, Origen, Destino, NroServicio, VarianteServicio)`: Same to `list_serv` but has a `myLatLongs` list containing only buses location.
- `list_arrays()`: Get a list of Companies, Cities(destination and origin) adn service type.

## Examples

### Get all buses with Montevideo as destination

```python
buses = client.list_serv_map(Destino='montevideo')['response']['servicios']
print(buses)
#[{'idServicioActivo': 9128277, 'idServicioProg': 1161, 'EmpresaPropBus': 25, 'nroServicio': 20, 'nroOrden': '--', 'NumBus': '217', 'CiudadOrigen': 16, 'CiudadDestino': 1, 'estado': 0, 'plataforma': 0, 'HoraLlegadaProg': '2024-01-16 13:10:00', 'HoraPartidaProg': '2024-01-16 13:25:00', 'HoraLlegadaReal': '0001-01-01 00:00:00', 'EmpresaServicio': 0, 'HoraPartidaReal': '0001-01-01 00:00:00', 'HoraInicioTeorica': '2024-01-16 05:45:00', 'HoraFinTeorica': '2024-01-16 13:10:00', 'comentarios': 'DNT', 'observaciones': None, 'ultimaPlataforma': 0, 'anunciado': 1, 'VarianteServicio': 'Camino', 'idCoche': 2569, 'idTerminal': 1, 'tieneGPS': 1, 'idPlataformaAsig': 0, 'esActivo': 1, 'horaDesvincular': None, 'HoraInicioTeoricaTime': '05:45', 'HoraFinTeoricaTime': '13:10', 'Empresa': 'TURIL', 'EmpresaProp': 'TURIL', 'Origen': 'RIVERA', 'Destino': 'MONTEVIDEO', 'latitude': -33.887, 'longitude': -56.2607, 'VarianteServicioOk': 'Camino', 'GPS': 1, 'horaEstimada': '22:00'},...]
```

### Get Companies

```python
companies = client.list_arrays()['response']['empresas']
print(companies)
#[{'id': 0, 'name': 'Todas'}, {'id': 1, 'name': 'AGENCIA CENTRAL'}, {'id': 48, 'name': 'BELGRANO'}, {'id': 2, 'name': 'BRUNO'}, {'id': 28, 'name': 'BUQUEBUS'}, {'id': 43, 'name': 'CAUVI'}, {'id': 3, 'name': 'CHADRE'},...]
```

## Contributing

Contributions are welcome! If you find a bug or have a suggestion, please create an issue or submit Merge Request.

## License

This project is licensed under the GNU General Public License, version 3.0. For more details, see [LICENSE](LICENSE).

---

*This project is not affiliated with Tres Cruces or its affiliates in any way.*

