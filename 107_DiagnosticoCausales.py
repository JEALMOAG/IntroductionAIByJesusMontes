"""
Created on 17 April  01:19:16 2024
@author: Jesus Alejandro Montes Aguila 
"""
'''

Este código simula un sistema de diagnóstico médico basado en reglas. Utiliza 
síntomas inventados como "fever" (fiebre), "rash" (erupción) y "cough" (tos)
 para diagnosticar enfermedades como "flu" (gripe) y "measles" (sarampión).
 Las reglas establecidas determinan qué enfermedad se diagnostica según los 
 síntomas presentes. Además, se proporciona un tratamiento correspondiente 
 para cada enfermedad diagnosticada.
'''
# Definición de reglas de diagnóstico y tratamiento
rules = {
    "R1": ("fever", "flu"),             # If fever is present, then it's flu
    "R2": ("rash", "measles"),          # If rash is present, then it's measles
    "R3": ("cough", "flu"),             # If cough is present, then it's flu
    "R4": ("measles", "antibiotics")    # If it's measles, then antibiotics
}

# Function to diagnose a disease based on symptoms
def diagnose(symptoms):
    diseases = set()  # Set to store diagnosed diseases

    # Iterate over all rules
    for rule, (symptom, disease) in rules.items():
        if symptom in symptoms:  # If the symptom in the rule is present in the given symptoms
            diseases.add(disease)  # Add the associated disease to the set of diagnosed diseases

    return diseases

# Function to find treatment for a diagnosed disease
def find_treatment(disease):
    for rule, (dis, treat) in rules.items():
        if dis == disease:
            return treat
    return "Treatment not found"

# Example symptoms
patient_symptoms = ["fever", "cough"]

# Diagnose disease(s) based on symptoms
diagnosed_diseases = diagnose(patient_symptoms)

# Print diagnosis
print("Diagnosed disease(s):", diagnosed_diseases)

# Find treatment for each diagnosed disease
for disease in diagnosed_diseases:
    treatment = find_treatment(disease)
    print(f"Treatment for {disease}: {treatment}")

