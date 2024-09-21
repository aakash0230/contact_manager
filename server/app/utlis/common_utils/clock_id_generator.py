import time
import threading
import random

class ClockIDGenerator():
    def __init__(self, prefix='', suffix='', use_random=True):
        self.prefix = prefix
        self.suffix = suffix
        self.use_random = use_random
        self.counter = 0
        self.lock = threading.Lock()

    def _current_milliseconds(self):
        """
        Get the current time in milliseconds since epoch.
        """
        return int(time.time() * 1000)

    def _increment_counter(self):
        """
        Safely increment the counter with thread locking.
        """
        with self.lock:
            self.counter += 1
            return self.counter

    def generate_id(self):
        """
        Generate a unique ID using the current timestamp and a counter or random value.
        """
        current_time = self._current_milliseconds()
        
        if self.use_random:
            random_component = random.randint(1000, 9999)
            unique_part = f'{current_time}{random_component}'
        else:
            unique_part = f'{current_time}{self._increment_counter()}'
        
        return f'{self.prefix}{unique_part}{self.suffix}'

# Example usage:
if __name__ == '__main__':
    generator = ClockIDGenerator(prefix='ID-', suffix='-2024', use_random=False)

    # Generate a few IDs
    for _ in range(5):
        print(generator.generate_id())
