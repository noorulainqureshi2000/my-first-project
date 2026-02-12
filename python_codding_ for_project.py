# Student Performance Tracker in Python

# Sample student data (Roll No, Name, Marks in 3 Subjects)
students = [
    {"roll": 111, "name": "ASLAM", "marks": [41, 60, 85]},
    {"roll": 112, "name": "AQIB", "marks": [42, 61, 90]},
    {"roll": 113, "name": "AHAD", "marks": [43, 62, 99]},
    {"roll": 114, "name": "ALI", "marks": [49, 63, 92]},
    {"roll": 115, "name": "BABAR", "marks": [44, 64, 60]},
    {"roll": 116, "name": "DANIAL", "marks": [33, 55, 79]},
    {"roll": 117, "name": "DAWOOD", "marks": [35, 45, 64]},
    {"roll": 118, "name": "FARIS", "marks": [22, 73, 50]},
    {"roll": 119, "name": "FAWAD", "marks": [43, 73, 88]},
    {"roll": 120, "name": "FEROZ", "marks": [41, 54, 99]},
    {"roll": 121, "name": "GHANI", "marks": [34, 65, 77]},
    {"roll": 122, "name": "HUNAIN", "marks": [36, 60, 66]},
    {"roll": 123, "name": "HASNAIN", "marks": [50, 60, 44]},
    {"roll": 124, "name": "HAMID", "marks": [30, 60, 66]},
    {"roll": 125, "name": "IBRAHIM", "marks": [22, 68, 65]},
    {"roll": 126, "name": "IDREES", "marks": [27, 68, 90]},
    {"roll": 127, "name": "JAWAID", "marks": [40, 67, 80]},
    {"roll": 128, "name": "JAWWAD", "marks": [40, 71, 70]},
    {"roll": 129, "name": "KAMAL", "marks": [40, 74, 60]},
    {"roll": 130, "name": "MUEEZ", "marks": [45, 73, 88]},
]

# Function to calculate grade
def calculate_grade(percent):
    if percent >= 80:
        return "A+"
    elif percent >= 70:
        return "A"
    elif percent >= 60:
        return "B"
    else:
        return "C"

# Process each student
results = []
for s in students:
    total = sum(s["marks"])
    percent = (total / 225) * 100  # Assuming each subject max = 75, total = 225
    grade = calculate_grade(percent)
    results.append({
        "roll": s["roll"],
        "name": s["name"],
        "total": total,
        "percent": round(percent, 2),
        "grade": grade
    })

# Print results
print("ROLL | NAME     | TOTAL | PERCENT | GRADE")
print("-------------------------------------------")
for r in results:
    print(f"{r['roll']} | {r['name']:<8} | {r['total']}   | {r['percent']}%   | {r['grade']}")

# Grade distribution summary
from collections import Counter
grades = [r["grade"] for r in results]
distribution = Counter(grades)

print("\nGrade Distribution:")
for grade, count in distribution.items():
    print(f"{grade}: {count} students")