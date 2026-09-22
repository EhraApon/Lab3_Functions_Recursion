def trace_fault(fault_code, call_count= 1):
    print(f"Call {call_count}: Tracing Fault Code -> {fault_code}")
    if fault_code <= 10:
        print(f"Base condition reached at fault level {fault_code}.")
        return fault_code, call_count
    if fault_code % 2 == 0:
        next_code = fault_code // 2
    else:
        next_code = fault_code - 7
    return trace_fault(next_code, call_count + 1)

LAST_NAME = "APON"
SEED_NUM = 6
FAVORITE_ARTIST = "TEETEEPOR"

fault_code = (len(LAST_NAME)* 100) + (SEED_NUM * 10) + len(FAVORITE_ARTIST)

print("=" * 40)
print(f"System Identifier: {LAST_NAME}_{FAVORITE_ARTIST}_{SEED_NUM}")
print(f"Initial Fault Code: {fault_code}")
print("=" * 40)
print(f"Beginning Recursive Fault Trace:")

final_fault, total_calls = trace_fault(fault_code)

print("=" * 40)
print("Trace Complete.")
print(f"Final Resolved Fault State: {final_fault}")
print(f"Total Recursive Invocations: {total_calls}")
print("=" * 40)