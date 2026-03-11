import requests
import time

# ================= CONFIG =================
WEBHOOK_URL = "YOUR_WEBHOOK_URL_HERE"   # Webhook URL
TRIGGER = ""     # Type something in console to begin
LOOP = True      # Infinite loop?
NUM_CHANNELS = 3 # How many messages per loop batch
BATCH_DELAY =    # Seconds to wait between batches
BATCH_AMOUNT = 5 # How many batches to send before stopping (ignored if LOOP=True)
DELETE_WEBHOOK = False     # Set to True to delete webhook at end
MESSAGE_CONTENT = "@everyone, this is spam"  # The message to send
# ==========================================

def send_message():
    data = {"content": MESSAGE_CONTENT}
    try:
        response = requests.post(WEBHOOK_URL, json=data)
        if response.status_code == 204:
            print("[+] Message sent successfully")
        else:
            print(f"[!] Failed: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"[!] Error: {e}")

def delete_webhook():
    try:
        response = requests.delete(WEBHOOK_URL)
        if response.status_code == 204:
            print("[+] Webhook deleted successfully")
        else:
            print(f"[!] Delete failed: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"[!] Error deleting webhook: {e}")

if __name__ == "__main__":
    trigger = input("Type trigger to start: ")
    if trigger.lower() == TRIGGER:
        batch_count = 0
        while True:
            for _ in range(NUM_CHANNELS):
                send_message()
            batch_count += 1
            print(f"Batch {batch_count} sent. Waiting {BATCH_DELAY}s...")
            time.sleep(BATCH_DELAY)

            if not LOOP and batch_count >= BATCH_AMOUNT:
                break

        if DELETE_WEBHOOK:
            delete_webhook()
    else:
        print("Trigger did not match. Exiting...")
