from crew import verify_student


print("\n" + "=" * 60)
print("GATEGUARD AI - STUDENT VERIFICATION TEST")
print("=" * 60)

mis_id = input("\nEnter Student MIS ID: ").strip()

print("\nVerifying student...")
print("-" * 60)

result = verify_student(mis_id)

print("\nFINAL RESULT")
print("-" * 60)
print(result)
print("=" * 60)