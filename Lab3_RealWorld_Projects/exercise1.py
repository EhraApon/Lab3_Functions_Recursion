def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Log: Executing {func.__name__}...")
        result = func(*args, **kwargs)
        print(f"Log : Completed {func.__name__}.")
        return result
    return wrapper

def validate_reading(val):
    try:
        num = float(val)
        if num < 0 or num > 300:
            raise ValueError(f"Out of operational range:{num}")
        return True, num
    except (ValueError, TypeError) as err:
        return False, str(err)

@logger
def process_readings(readings):
    valid_list = []
    invalid_list = []
    for item in readings:
        is_valid, res = validate_reading(item)
        if is_valid:
            valid_list.append(res)
        else:
            invalid_list.append(item)
    return valid_list, invalid_list

def compute_diagnostic(valid_readings):
    if not valid_readings:
        return 0.0, 0.0, 0.0
    avg_val = sum(valid_readings) / len(valid_readings)
    max_val = max(valid_readings)
    min_val = min(valid_readings)
    return avg_val, max_val, min_val

def classify_status(avg_val):
    if avg_val >= 80:
        return "CRITICAL"
    elif avg_val >= 50:
        return "WARNING"
    elif avg_val >= 20:
        return "NORMAL"
    else:
        return "OPTIMAL"

LAST_NAME = "APON"
SEED_NUM = 6
FAVORITE_ARTIST = "TEETEEPOR"

name_factor = len(LAST_NAME)
artist_factor = len(FAVORITE_ARTIST)

raw_readings = [
    SEED_NUM * 12.5,
    name_factor * 8.0,
    "FAULTY_SENSOR",
    artist_factor * 11.2,
    -15.0,
    (SEED_NUM + name_factor) * 4.5,
    None,
    (artist_factor + SEED_NUM) * 6.0
]

valid_data, invalid_data = process_readings(raw_readings)
avg_reading, max_reading, min_reading = compute_diagnostic(valid_data)
status = classify_status(avg_reading)

print("=" * 40)
print(f"Techninician: {LAST_NAME}")
print(f"Seed Digit: {SEED_NUM}")
print(f"Artist tag: {FAVORITE_ARTIST}")
print("=" * 40)
print(f"Total Readings: {len(raw_readings)}")
print(f"Valid Readings: {valid_data}")
print(f"Invalid Readings: {invalid_data}")
print(f"Average Reading: {round(avg_reading, 2)}")
print(f"Peak Reading: {round(max_reading, 2)}")
print(f"Minimum Reading: {round(min_reading, 2)}")
print(f"Equipment Status: {status}")
print("=" * 40)