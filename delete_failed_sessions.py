import os
import sys
import requests
import logging

# This script requires the 'requests' library.
# pip install requests

# --- Configuration ---
API_BASE_URL = "https://jules.googleapis.com/v1alpha"
LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
DATE_FORMAT = "%Y-%m-%d %H:%M:%S"

# Configure Logging
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT, datefmt=DATE_FORMAT)
logger = logging.getLogger("jules_session_deleter")

# -------------------------------------------------------------------------
# JULES CLIENT (adapted from jules_ops.py)
# -------------------------------------------------------------------------
class JulesClient:
    """A client for interacting with the Jules API."""
    def __init__(self, api_key=None):
        self.api_key = api_key or os.environ.get("JULES_API_KEY")

        if not self.api_key:
            logger.error(
                "No API key found. Please set the JULES_API_KEY environment variable."
            )
            sys.exit(1)

        self.headers = {
            "Content-Type": "application/json",
            "X-Goog-Api-Key": self.api_key,
        }

    def _request(self, method, endpoint, data=None, params=None):
        """Makes a request to the Jules API."""
        url = f"{API_BASE_URL}/{endpoint}"
        try:
            response = requests.request(
                method, url, headers=self.headers, json=data, params=params
            )
            response.raise_for_status()
            if response.status_code == 204 or not response.content:
                return {}
            return response.json()
        except requests.exceptions.HTTPError as e:
            logger.error(
                f"HTTP Error: {e.response.status_code} - {e.response.text}"
            )
            return None
        except Exception as exc:
            logger.error(f"Request Failed: {exc}")
            return None

    def list_sessions(self):
        """Retrieves a list of all sessions, handling pagination."""
        all_sessions = []
        next_page_token = None
        while True:
            params = {}
            if next_page_token:
                params["pageToken"] = next_page_token

            response_json = self._request("GET", "sessions", params=params)

            if response_json:
                all_sessions.extend(response_json.get("sessions", []))
                next_page_token = response_json.get("nextPageToken")
                if not next_page_token:
                    break
            else:
                break  # Error occurred
        return all_sessions

    def delete_session(self, session_name):
        """Deletes a session."""
        logger.info(f"🗑️  Deleting session {session_name}...")
        return self._request("DELETE", session_name)

def delete_all_sessions():
    """Deletes all Jules sessions."""
    client = JulesClient()
    logger.info("Fetching all sessions from Jules to delete them...")
    sessions = client.list_sessions()
    if not sessions:
        logger.info("No sessions found to delete.")
        return

    sessions_to_delete = [session.get("name") for session in sessions if session.get("name")]
    
    if not sessions_to_delete:
        logger.info("No valid session names found to delete.")
        return

    logger.info(f"Found {len(sessions_to_delete)} sessions to delete.")
    
    deleted_count = 0
    for session_name in sessions_to_delete:
        response = client.delete_session(session_name)
        if response is not None:
             deleted_count +=1

    logger.info(f"Finished. Successfully deleted {deleted_count} of {len(sessions_to_delete)} sessions.")

if __name__ == "__main__":
    delete_all_sessions()