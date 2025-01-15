import subprocess
import os

def run_script(script_name):
    """Run a Python script in the src directory."""
    script_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), script_name)
    try:
        print(f"\nRunning {script_name}...")
        subprocess.run(["python", script_path], check=True)
        print(f"{script_name} completed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error while running {script_name}: {e}")

def main():
    print("\n🚀 Starting the Data Pipeline...")

    # Step 1: Extract - Generate raw data
    run_script("extract.py")

    # Step 2: Transform - Clean and process data
    run_script("transform.py")

    # Step 3: Validate - Check data quality
    run_script("validate.py")  # Added validation step here

    # Step 4: Load - Aggregate and save curated data
    run_script("load.py")

    # Step 5: Metadata - Update metadata catalog
    run_script("metadata_manager.py")

    print("\n✅ Data Pipeline completed successfully!")


if __name__ == "__main__":
    main()
