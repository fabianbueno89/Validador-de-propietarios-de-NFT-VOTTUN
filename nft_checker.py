python
import requests

def is_owner_of_nft(contract_address, token_id, owner_address):
    url = f"https://api.opensea.io/api/v1/asset/{contract_address}/{token_id}/"

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data['owner']['address'].lower() == owner_address.lower()
    else:
        raise Exception("Error fetching NFT data from OpenSea API.")

if __name__ == "__main__":
    # Example usage
    contract_address = "0xYourContractAddress"  # Replace with your NFT contract address
    token_id = "1"  # Replace with the NFT token ID
    owner_address = "0xOwnerAddress"  # Replace with the owner's address

    is_owner = is_owner_of_nft(contract_address, token_id, owner_address)
    print(f"Is the owner of the NFT? {'Yes' if is_owner else 'No'}")
