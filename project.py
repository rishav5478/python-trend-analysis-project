import numpy as np
import matplotlib.pyplot as plt
years = np.array([2019, 2020, 2021, 2022, 2023, 2024, 2025])
total_students = np.array([4000, 3500, 3300, 3800, 3500, 3000, 2000])
yearly_drop = np.diff(total_students) 
student_feedback = {
    2019: "Best faculty in South Delhi, highly recommended.",
    2022: "Good, internal issues (there were notable complaints regarding salary cuts(reported as early as april 2022 in some centres)).",
    2024: "Total mess. many student warned prospective joiners to avoid the institute,calling it unstable and unpredictable.",
    2025: "Kalu Sarai center is locked. Trying to get a refund for months."
}
print("--- A Leading Coaching INstitute Analysis Project ---")
print(f"Overall Decline (2019 to 2025): {total_students[0] - total_students[-1]} students")
print(f"Sharpest Drop observed: {np.min(yearly_drop)} students in a single year")
crisis_keywords = ["refund", "closed", "no classes", "locked", "leaving"]
found_keywords = [word for word in crisis_keywords if any(word in f.lower() for f in student_feedback.values())]
print(f"Crisis Indicators found in reviews: {found_keywords}")
plt.figure(figsize=(10, 5))

plt.plot(years, total_students, marker='o', color='red', linewidth=2, label="Demand Trend")

plt.axvspan(2023.5, 2025, color='yellow', alpha=0.3, label="Major Crisis Period")

plt.title("The Decline of A Leading Coachung Institute South Delhi (2019-2025)")
plt.xlabel("Year")
plt.ylabel("Number of students")
plt.legend()
plt.grid(True, linestyle='--')
plt.show()
