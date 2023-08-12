import time

def generate_unique_number():
    timestamp = int(time.time() * 1000)  # Multiply by 1000 to get milliseconds
    unique_number = f"{timestamp}"
    return unique_number