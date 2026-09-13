import os
import time
from livetennisapi import LiveTennisAPI

API_KEY = os.environ.get("LIVETENNISAPI_KEY", "")

def main():
    if not API_KEY:
        print("[-] Error: Set $env:LIVETENNISAPI_KEY before running.")
        print("[*] Get your API key at: https://livetennisapi.com/?ref=themarconipulse")
        return

    print("[+] Initializing Live Tennis Monitor...")
    
    try:
        with LiveTennisAPI(api_key=API_KEY) as client:
            print("[*] Fetching live matches...")
            matches = list(client.list_matches(status="live"))
            
            if not matches:
                print("[*] No live matches currently underway.")
                return

            print(f"\n[Found {len(matches)} Live Matches]\n" + "-" * 50)
            for m in matches:
                p1 = getattr(m.p1, "name", "Player 1")
                p2 = getattr(m.p2, "name", "Player 2")
                tournament = getattr(m.tournament, "Unknown Tournament", "Tournament")
                score = getattr(m.score, "sets", "0-0")
                print(f"Tournament: {tournament}")
                print(f"  {p1} vs {p2}")
                print(f"  Score (Sets): {score}\n" + "-" * 50)
                
    except Exception as e:
        print(f"[!] Error fetching data: {e}")

if __name__ == "__main__":
    main()
