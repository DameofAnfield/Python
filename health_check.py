import tkinter as tk
from tkinter import ttk

def calculate_bmi(weight, height):
    return weight / (height ** 2)

def check_blood_pressure(systolic_bp, diastolic_bp):
    if systolic_bp >= 140 or diastolic_bp >= 90:
        return "High blood pressure"
    elif systolic_bp < 90 or diastolic_bp < 60:
        return "Low blood pressure"
    else:
        return "Normal blood pressure"

def check_diabetes(glucose_level):
    if glucose_level >= 126:
        return "Diabetes"
    elif 100 <= glucose_level < 126:
        return "Pre-diabetes"
    else:
        return "Normal"

def check_bone_density(t_score):
    if t_score < -2.5:
        return "Osteoporosis"
    elif -1 <= t_score < -2.5:
        return "Osteopenia"
    else:
        return "Normal bone density"

def check_cancer_risk(age, gender, family_history):
    if age >= 50 and gender == "Male":
        return "Higher risk of prostate cancer"
    elif age >= 40 and gender == "Female" and family_history:
        return "Higher risk of breast cancer"
    else:
        return "Average cancer risk"

def calculate_health():
    weight = float(weight_entry.get())
    height = float(height_entry.get())
    systolic_bp = int(systolic_bp_entry.get())
    diastolic_bp = int(diastolic_bp_entry.get())
    glucose_level = int(glucose_level_entry.get())
    t_score = float(t_score_entry.get())
    age = int(age_entry.get())
    gender = gender_var.get()
    family_history = family_history_var.get()

    bmi = calculate_bmi(weight, height)
    blood_pressure_result = check_blood_pressure(systolic_bp, diastolic_bp)
    diabetes_result = check_diabetes(glucose_level)
    bone_density_result = check_bone_density(t_score)
    cancer_risk_result = check_cancer_risk(age, gender, family_history)

    result_text.set(f"Body Mass Index (BMI): {bmi:.2f}\n"
                    f"Blood Pressure: {blood_pressure_result}\n"
                    f"Diabetes: {diabetes_result}\n"
                    f"Bone Density: {bone_density_result}\n"
                    f"Cancer Risk: {cancer_risk_result}")

app = tk.Tk()
app.title("Health Diagnostic System")

weight_label = ttk.Label(app, text="Weight (kg):")
weight_entry = ttk.Entry(app)

height_label = ttk.Label(app, text="Height (m):")
height_entry = ttk.Entry(app)

systolic_bp_label = ttk.Label(app, text="Systolic Blood Pressure:")
systolic_bp_entry = ttk.Entry(app)

diastolic_bp_label = ttk.Label(app, text="Diastolic Blood Pressure:")
diastolic_bp_entry = ttk.Entry(app)

glucose_level_label = ttk.Label(app, text="Glucose Level:")
glucose_level_entry = ttk.Entry(app)

t_score_label = ttk.Label(app, text="Bone Density T-score:")
t_score_entry = ttk.Entry(app)

age_label = ttk.Label(app, text="Age:")
age_entry = ttk.Entry(app)

gender_label = ttk.Label(app, text="Gender:")
gender_var = tk.StringVar()
gender_combobox = ttk.Combobox(app, textvariable=gender_var, values=["Male", "Female"])
gender_combobox.set("Male")

family_history_label = ttk.Label(app, text="Family History of Cancer:")
family_history_var = tk.BooleanVar()
family_history_checkbox = ttk.Checkbutton(app, variable=family_history_var)

result_text = tk.StringVar()
result_label = ttk.Label(app, textvariable=result_text, wraplength=400, justify="left")

calculate_button = ttk.Button(app, text="Calculate", command=calculate_health)

weight_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
weight_entry.grid(row=0, column=1, padx=10, pady=5)

height_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
height_entry.grid(row=1, column=1, padx=10, pady=5)

systolic_bp_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")
systolic_bp_entry.grid(row=2, column=1, padx=10, pady=5)

diastolic_bp_label.grid(row=3, column=0, padx=10, pady=5, sticky="w")
diastolic_bp_entry.grid(row=3, column=1, padx=10, pady=5)

glucose_level_label.grid(row=4, column=0, padx=10, pady=5, sticky="w")
glucose_level_entry.grid(row=4, column=1, padx=10, pady=5)

t_score_label.grid(row=5, column=0, padx=10, pady=5, sticky="w")
t_score_entry.grid(row=5, column=1, padx=10, pady=5)

age_label.grid(row=6, column=0, padx=10, pady=5, sticky="w")
age_entry.grid(row=6, column=1, padx=10, pady=5)

gender_label.grid(row=7, column=0, padx=10, pady=5, sticky="w")
gender_combobox.grid(row=7, column=1, padx=10, pady=5)

family_history_label.grid(row=8, column=0, padx=10, pady=5, sticky="w")
family_history_checkbox.grid(row=8, column=1, padx=10, pady=5)

calculate_button.grid(row=9, column=0, columnspan=2, padx=10, pady=10)
result_label.grid(row=10, column=0, columnspan=2, padx=10, pady=5)

app.mainloop()