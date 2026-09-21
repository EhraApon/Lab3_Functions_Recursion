import exercise3 as tp

LAST_NAME = "APON"
SEED_NUM = 4
FAVORITE_ARTIST = "TEETEEPOR"

NAME_LENGTH = len(LAST_NAME)
ARTIST_LENGTH = len(FAVORITE_ARTIST)

@tp.monitor_pipeline
def run_telemetry_pipeline():
    stream = tp.telemetry_generator(SEED_NUM, NAME_LENGTH, ARTIST_LENGTH, 10)

    raw_data = []
    valid_readings =[]
    invalid_readings = []
    recursive_traces = []

    for raw_point in stream:
        raw_data.append(raw_point)
        is_valid, result = tp.validate_telemetry(raw_point)
        if is_valid:
            valid_readings.append(result)
        else:
            invalid_readings.append(raw_point)

    calibrate = lambda val: round(val * 1.05,2)
    calibrated_readings = list(map(calibrate, valid_readings))

    filter_anomalies = lambda val: val > 80.0
    anomaly_readings = list(filter(filter_anomalies, calibrated_readings))

    for anomaly in anomaly_readings:
        steps, terminal_val = tp.recursive_anomaly_trace(anomaly)
        recursive_traces.append((anomaly, steps, terminal_val))

    avg_reading = sum(calibrated_readings) / len(calibrated_readings) if calibrated_readings else 0.0
    system_status = tp.determine_system_health(avg_reading, len(anomaly_readings))

    return {
        "raw": raw_data,
        "valid": valid_readings,
        "invalid": invalid_readings,
        "calibrated": calibrated_readings,
        "anomalies": anomaly_readings,
        "traces": recursive_traces,
        "average": avg_reading,
        "status": system_status
    }

report = run_telemetry_pipeline()

print("=" * 40)
print(f"System: {LAST_NAME} Nonitoring Pipeline")
print(f"Config: SEED_NUMB={SEED_NUM} | ARTIST={FAVORITE_ARTIST}")
print("=" * 40)
print(f"Total Stream Points Processed: {len(report['raw'])}")
print(f"Valid telemetry Count: {len(report['valid'])}")
print(f"Invalid telemetry Count: {len(report['invalid'])}")
print(f"Calibrated Reading: {report['calibrated']}")
print(f"Abnormal Conditions Detected: {len(report['anomalies'])}")
for orig, steps, final in report['traces']:
    print(f" Anomaly {orig} -> Resolved to {final} across {steps} recursive steps")
print(f"Average Calibrated value: {round(report['average'], 2)}")
print(f"Overall Equipment Status: {report['status']}")
print("=" * 40)