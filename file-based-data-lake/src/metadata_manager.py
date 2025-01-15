import os
import pandas as pd
import json
from datetime import datetime

def generate_metadata(file_path, zone):
    """Generate metadata for a given dataset."""
    if file_path.endswith('.csv'):
        df = pd.read_csv(file_path)
        file_format = 'CSV'
    elif file_path.endswith('.parquet'):
        df = pd.read_parquet(file_path)
        file_format = 'Parquet'
    else:
        raise ValueError("Unsupported file format.")

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

def update_metadata_catalog(metadata, catalog_path="metadata/dataset_catalog.json"):
    """Update the metadata catalog with new dataset info."""
    # Ensure the metadata folder exists
    os.makedirs(os.path.dirname(catalog_path), exist_ok=True)

    # Load existing catalog if it exists
    if os.path.exists(catalog_path):
        with open(catalog_path, "r") as file:
            catalog = json.load(file)
    else:
        catalog = []

    # Check if the dataset already exists and update it
    for entry in catalog:
        if entry['dataset_name'] == metadata['dataset_name']:
            entry.update(metadata)
            break
    else:
        catalog.append(metadata)

    # Save the updated catalog
    with open(catalog_path, "w") as file:
        json.dump(catalog, file, indent=4)

    print(f"Metadata updated for {metadata['dataset_name']}")

def process_zone(zone_folder, zone_name):
    """Generate and update metadata for all files in a zone."""
    for root, _, files in os.walk(zone_folder):
        for file in files:
            if file.endswith(('.csv', '.parquet')):
                file_path = os.path.join(root, file)
                metadata = generate_metadata(file_path, zone_name)
                update_metadata_catalog(metadata)

if __name__ == "__main__":
    # Define the data zones
    script_dir = os.path.dirname(os.path.abspath(__file__))

    zones = {
        "raw": os.path.join(script_dir, "..", "data", "raw"),
        "processed": os.path.join(script_dir, "..", "data", "processed"),
        "curated": os.path.join(script_dir, "..", "data", "curated")
    }
    # Process each zone
    for zone_name, zone_path in zones.items():
        process_zone(zone_path, zone_name)
