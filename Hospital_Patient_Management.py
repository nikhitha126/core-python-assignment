def search(patients, disease):
    result = []
    for patient in patients:
        if patient["Disease"].lower() == disease.lower():
            result.append(patient["Name"])
    return result
patients_record = [
    {"Name": "Alice", "Age": 30, "Disease": "Flu"},
    {"Name": "Bob", "Age": 45, "Disease": "Diabetes"},
    {"Name": "Charlie", "Age": 35, "Disease": "Flu"}]
search_disease = "Flu"
match= search(patients_record, search_disease)
print(f"Patients with {search_disease}: {match}")
