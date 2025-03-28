#!/usr/bin/env python3
"""
main.py - Schedules tasks and runs the trading bot.
"""
import logging
import time
import schedule
from threading import Thread
from queue import Queue

from strategy import run_strategy
from risk_management import monitor_risk, monitor_account_value

logging.basicConfig(level=logging.INFO)

def monitor_input(queue):
    """
    Non-blocking way to detect user 'q' input to quit.
    """
    while True:
        user_input = input("Enter 'q' to quit:\n").strip().lower()
        if user_input == "q":
            queue.put("quit")
            break

if __name__ == "__main__":
    logging.info("Starting Trading Bot...")

    # Example scheduling
    # - Run the strategy daily
    schedule.every().day.at("00:01").do(run_strategy)
    # - Check risk every 5 minutes
    schedule.every(5).minutes.do(monitor_risk)
    # - Check account value every 5 minutes
    schedule.every(5).minutes.do(monitor_account_value)

    input_queue = Queue()
    input_thread = Thread(target=monitor_input, args=(input_queue,), daemon=True)
    input_thread.start()

    try:
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
        logging.error(f"Unexpected error: {e}")
    finally:
        logging.info("Shutting down trading bot. Ensure all trades are closed properly.")
