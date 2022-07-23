from brownie import AdvancedCollectible, network
from metadata.sample_metadata import metadata_template
from pathlib import Path
import requests
import json
import os


def main():
    advanced_collectible = AdvancedCollectible[-1]
    number_of_advanced_collectibles = advanced_collectible.tokenCounter()
    print(f"You have created {number_of_advanced_collectibles} collectibles!")
    for token_id in range(number_of_advanced_collectibles):
        collectible_metadata = metadata_template
        print(f"Creating Metadata file: {metadata_file_name}")
        collectible_metadata["name"] = breed
        collectible_metadata["description"] = f"An adorable {breed} pup!"
        image_path = "./img/" + breed.lower().replace("_", "-") + ".png"

        image_uri = None
        if os.getenv("UPLOAD_IPFS") == "true":
            image_uri = upload_to_ipfs(image_path)
        image_uri = image_uri if image_uri else breed_to_image_uri[breed]

        collectible_metadata["image"] = image_uri
        with open(metadata_file_name, "w") as file:
            json.dump(collectible_metadata, file)
        if os.getenv("UPLOAD_IPFS") == "true":
            upload_to_ipfs(metadata_file_name)


def upload_to_ipfs(filepath):
    with Path(filepath).open("rb") as fp:
        image_binary = fp.read()
        ipfs_url = "http://127.0.0.1:5001"
        endpoint = "/api/v0/add"
        response = requests.post(ipfs_url + endpoint, files={"file": image_binary})
        ipfs_hash = response.json()["Hash"]
        # "./img/0-PUG.png" -> "0-PUG.png"
        filename = filepath.split("/")[-1:][0]
        image_uri = f"https://ipfs.io/ipfs/{ipfs_hash}?filename={filename}"
        print(image_uri)
        return image_uri