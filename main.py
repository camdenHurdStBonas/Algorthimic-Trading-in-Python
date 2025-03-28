"""
main.py - Example daily trading bot using Python, ccxt, 
and basic ML signals. 
"""
import os
import time
import logging
import schedule
from queue import Queue
from threading import Thread
from datetime import datetime
# Import local modules
from trading_strategies import run_strategy, monitor_risk, monitor_account_value
# from data_utils import ...
# from config import ...  # or load environment variables

logging.basicConfig(level=logging.INFO)

def monitor_input(queue):
    """Non-blocking way to detect user 'q' input to quit."""
    while True:
        user_input = input("Enter 'q' to quit:\n").strip().lower()
        if user_input == "q":
            queue.put("quit")
            break

if __name__ == "__main__":
    try:
        logging.info("Starting Trading Bot...")

        # Example scheduling
        schedule.every().day.at("00:01").do(run_strategy)
        schedule.every(5).minutes.do(monitor_risk)
        schedule.every(5).minutes.do(monitor_account_value)

        # Listen for 'q' key to exit
        input_queue = Queue()
        input_thread = Thread(target=monitor_input, args=(input_queue,), daemon=True)
        input_thread.start()

        # Main loop
        while True:
            schedule.run_pending()
            if not input_queue.empty():
                if input_queue.get() == "quit":
                    logging.info("Quit command received. Exiting program...")
                    break
            time.sleep(1)

    except KeyboardInterrupt:
        logging.info("Keyboard interrupt detected. Exiting gracefully...")
    except Exception as e:
        logging.error(f"Unexpected error in main loop: {e}")
    finally:
        logging.info("Shutting down the trading bot.")