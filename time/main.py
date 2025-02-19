from datetime import datetime, timedelta
import time

class TimestampPrinter:
    def __init__(self):
        self.current_time = datetime.now()
        self.end_time = self.current_time + timedelta(hours=1)

    def display_timestamps(self):
        # Loop until the current time reaches the end time
        while self.current_time <= self.end_time:
            # Print the timestamp
            print(self.current_time.strftime('%Y-%m-%d %H:%M:%S'))
            # Wait for 30 seconds
            time.sleep(30)
            # Increment the time by 30 seconds
            self.current_time += timedelta(seconds=30)

    def print(self):
        print(self.current_time)

    def update(self):
        self.current_time = datetime.now()

    def update_with_delay(self, delay):
        time.sleep(delay)
        self.current_time = datetime.now()

if __name__ == "__main__":
    printer = TimestampPrinter()
    printer.display_timestamps()