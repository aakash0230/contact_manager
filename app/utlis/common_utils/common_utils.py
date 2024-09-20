import random

def generate_otp():
    print("inside generate otp")
    """Generate a random 6-digit OTP."""
    otp = ''.join([str(random.randint(0, 9)) for _ in range(6)])
    return otp
