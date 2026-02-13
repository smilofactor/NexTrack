
import argparse
import subprocess
import os
import sys

def main():
    parser = argparse.ArgumentParser(description="NexTrack Launcher")
    parser.add_argument(
        "--store",
        type=str,
        default="sqlite",
        help="Specify datastore (default: sqlite)"
    )

    args = parser.parse_args()

    # 1. Set the Environment Variable for the store choice
    os.environ["NEXTRACK_STORE"] = args.store

    # 2. Add the project root to PYTHONPATH
    # This ensures ui/ui_main.py can still 'import modules'
    current_dir = os.path.abspath(os.path.dirname(__file__))
    os.environ["PYTHONPATH"] = current_dir

    # 3. Path to the UI script
    ui_script = os.path.join(current_dir, "ui", "ui_main.py")

    print(f"--- Launching NexTrack with {args.store.upper()} store ---")

    try:
        # Run streamlit pointing to the new directory
        subprocess.run(["streamlit", "run", ui_script])
    except KeyboardInterrupt:
        print("\nShutting down NexTrack...")
        sys.exit(0)

if __name__ == "__main__":
    main()
