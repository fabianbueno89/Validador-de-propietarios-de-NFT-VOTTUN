# Check NFT Ownership

Este proyecto incluye un fragmento de código en Python que permite consultar si una cuenta es propietaria de un NFT específico utilizando la API de OpenSea.

## Requisitos

- Python 3.x
- Requests library (puedes instalarla usando `pip install requests`)

## Uso

1. Clona este repositorio:

   ```bash
   git clone https://github.com/tu-usuario/nft-ownership-checker.git
   cd nft-ownership-checker
   ```

2. Abre el archivo `nft_checker.py` y reemplaza las variables:

   ```python
   contract_address = "0xYourContractAddress"  # Reemplaza con la dirección del contrato NFT
   token_id = "1"  # Reemplaza con el ID del NFT
   owner_address = "0xOwnerAddress"  # Reemplaza con la dirección del propietario
   ```

3. Ejecuta el script:

   ```bash
   python nft_checker.py
   ```

4. El resultado mostrará si la cuenta es propietaria del NFT.

## Uso con Postman

1. Asegúrate de tener una API que exponga el script de Python como un endpoint.
2. Configura un endpoint en Postman que apunte a tu API.
3. Realiza una solicitud GET a tu API, pasando los parámetros `contract_address`, `token_id`, y `owner_address`.
4. La respuesta será un JSON que indicará si la dirección es propietaria del NFT o no.
