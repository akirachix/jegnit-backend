
from datetime import datetime
import random
def timestamp_conversation():
    unformatted_time = datetime.now()
    formatted_time = unformatted_time.strftime("%Y%m%d%H%M%S")
    return formatted_time
def send_otp_sms(phone, otp):
    print(f"Sending OTP {otp} to phone {phone}")
def generate_otp():
    return str(random.randint(100000, 999999))