import csv
import os
import subprocess
import time
from datetime import datetime, timedelta

# --- Configuration ---
CONSOLIDATED_WORKSTREAMS_CSV = "consolidated_workstreams.csv"
JULES_OPS_SCRIPT = "jules_ops.py"
# Assuming this script is in `scripts/`, and `consolidated_workstreams.csv` and `jules_ops.py` are also in `scripts/`
SCRIPTS_DIR = os.path.dirname(os.path.abspath(__file__))
JULES_OPS_PATH = os.path.join(SCRIPTS_DIR, JULES_OPS_SCRIPT)
CONSOLIDATED_WORKSTREAMS_PATH = os.path.join(
    SCRIPTS_DIR, CONSOLIDATED_WORKSTREAMS_CSV
)


def get_unpublished_sessions(csv_path):
    """
    Reads the consolidated_workstreams.csv and returns a list of completed sessions
    that do not have an associated PR.
    """
    sessions_to_publish = []
    try:
        with open(csv_path, mode="r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Assuming session_id is not '-' (which indicates an orphaned PR)
                if (
                    row["session_state"] == "COMPLETED"
                    and not row["pr_id"].strip()
                    and row["session_id"].strip() != "-"
                ):
                    sessions_to_publish.append(
                        {
                            "session_id": row["session_id"],
                            "session_title": row["session_title"],
                        }
                    )
    except FileNotFoundError:
        print(f"Error: {csv_path} not found.")
    except Exception as e:
        print(f"Error reading CSV: {e}")
    return sessions_to_publish


def publish_session_with_timeout(session_id, timeout_seconds=60):
    """
    Attempts to publish a single Jules session with a specified timeout.
    """
    print(
        f"\nAttempting to publish session: {session_id} with a {timeout_seconds}s timeout..."
    )
    # Execute jules_ops.py from the workspace root (where it expects its data/configs)
    # The path to jules_ops.py needs to be relative to the cwd where subprocess.run is executed.
    command = [
        "timeout",
        str(timeout_seconds),
        "python3",
        os.path.join("scripts", JULES_OPS_SCRIPT),
        "publish",
        session_id,
    ]

    try:
        result = subprocess.run(
            command,
            cwd="/home/ari/workspace",
            capture_output=True,
            text=True,
            check=False,
        )

        print(f"--- Output for session {session_id} ---")
        if result.stdout:
            print(result.stdout)
        if result.stderr:
            print(result.stderr)
        print(f"--- End Output for session {session_id} ---")

        if result.returncode == 0:
            print(
                f"✅ Publish request for session {session_id} completed (or initiated)."
            )
            return True
        elif result.returncode == 124:  # Timeout exit code
            print(
                f"❌ Publish request for session {session_id} timed out after {timeout_seconds} seconds."
            )
            return False
        else:
            print(
                f"❌ Publish request for session {session_id} failed with exit code {result.returncode}."
            )
            return False

    except FileNotFoundError:
        print(
            f"Error: '{os.path.join('scripts', JULES_OPS_SCRIPT)}' or 'timeout' command not found."
        )
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    return False


def main():
    print("Collecting unpublished Jules sessions...")

    sessions = get_unpublished_sessions(CONSOLIDATED_WORKSTREAMS_PATH)

    if not sessions:
        print("No completed, unpublished sessions found.")
        return

    print(f"Found {len(sessions)} completed, unpublished sessions.")

    for session in sessions:
        session_id = session["session_id"]
        session_title = session["session_title"]
        print(f"\nProcessing session ID: {session_id}, Title: {session_title}")
        publish_session_with_timeout(session_id)
        time.sleep(1)  # Small delay to prevent overwhelming the API


if __name__ == "__main__":
    main()
