from datetime import datetime
import pytz

# Function to convert IST to UTC
def convert_ist_to_utc(ist_time_str):
    # Define IST and UTC timezones
    ist = pytz.timezone('Asia/Kolkata')
    utc = pytz.utc

    # Parse the input time string into a datetime object
    ist_time = datetime.strptime(ist_time_str, '%Y-%m-%d %H:%M:%S')

    # Localize the time to IST timezone
    ist_time = ist.localize(ist_time)

    # Convert the IST time to UTC
    utc_time = ist_time.astimezone(utc)

    return utc_time.strftime('%Y-%m-%d %H:%M:%S')

# Get input time in IST from the user
ist_time_str = input("Enter time in IST (YYYY-MM-DD HH:MM:SS format): ")

# Convert and print the UTC time
utc_time_str = convert_ist_to_utc(ist_time_str)
print(f"Original IST Time: {ist_time_str}")
print(f"Converted UTC Time: {utc_time_str}")

