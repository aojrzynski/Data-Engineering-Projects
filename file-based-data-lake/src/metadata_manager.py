import os
import pandas as pd
import json
from datetime import datetime

# Generates metadata for a given dataset, including schema, record count, and last updated timestamp
def generate_metadata(file_path, zone):
    # Load dataset based on file format
    if file_path.endswith('.csv'):
        df = pd.read_csv(file_path)
        file_format = 'CSV'
    elif file_path.endswith('.parquet'):
        df = pd.read_parquet(file_path)
        file_format = 'Parquet'
    else:
        raise ValueError("Unsupported file format.")

    # Create metadata dictionary with dataset details
    metadata = {
        "dataset_name": os.path.basename(file_path),
        "zone": zone,
        "file_path": os.path.abspath(file_path),
        "file_format": file_format,
        "record_count": len(df),
        "schema": df.dtypes.apply(lambda x: str(x)).to_dict(),
        "last_updated": datetime.now().isoformat()
    }
    return metadata

# Updates the metadata catalog JSON file with the latest dataset information
def update_metadata_catalog(metadata, catalog_path="metadata/dataset_catalog.json"):
    # Load existing catalog or initialize a new one
    os.makedirs(os.path.dirname(catalog_path), exist_ok=True)

    # Load existing catalog if it exists
    if os.path.exists(catalog_path):
        with open(catalog_path, "r") as file:
            catalog = json.load(file)
    else:
        catalog = []

    # Check if dataset already exists and update it
    for entry in catalog:
        if entry['dataset_name'] == metadata['dataset_name']:
            entry.update(metadata)
            break
    else:
        catalog.append(metadata) # Add new dataset if not found

    # Save updated catalog to JSON file
    with open(catalog_path, "w") as file:
        json.dump(catalog, file, indent=4)

    print(f"Metadata updated for {metadata['dataset_name']}")

# Processes all datasets in a specified zone and updates the metadata catalog
def process_zone(zone_folder, zone_name):
    for root, _, files in os.walk(zone_folder):
        for file in files:
            if file.endswith(('.csv', '.parquet')):
                file_path = os.path.join(root, file)
                metadata = generate_metadata(file_path, zone_name)
                update_metadata_catalog(metadata)

# Main execution block: processes all data zones when the script runs directly
if __name__ == "__main__":
    # Define paths for raw, processed, and curated zones
    script_dir = os.path.dirname(os.path.abspath(__file__))

    zones = {
        "raw": os.path.join(script_dir, "..", "data", "raw"),
        "processed": os.path.join(script_dir, "..", "data", "processed"),
        "curated": os.path.join(script_dir, "..", "data", "curated")
    }
    # Process each zone to update metadata
    for zone_name, zone_path in zones.items():
        process_zone(zone_path, zone_name)
