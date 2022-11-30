import math
print("""
-----------------------------------------------------------
Pythagorean theorem calculator! Enter '?' if it's unknown.
-----------------------------------------------------------
""")
A1 = input("Length of A: ")
B2 = input("Length of B: ")
C3 = input("Length of C: ")
if C3 == "?":
    combined_terms = int(A1) ** 2 + int(B2) ** 2
    solution = math.sqrt(combined_terms)
    print(f"C = {solution}!")
elif A1 == "?":
    combined_terms = int(C3) ** 2 - int(B2) ** 2
    solution = math.sqrt(combined_terms)
    print(solution)
elif B2 == "?":
    combined_terms = int(C3) ** 2 - int(A1) ** 2
    solution = math.sqrt(combined_terms)
    print(f"B = {solution}!")
else:
    print("Invalid equation!")
exit()

