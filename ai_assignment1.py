class HealthcareDiagnosticAgent:
    def __init__(self):  
        self.conditions = {
            "Flu": ["fever", "cough", "sore throat", "fatigue"],
            "COVID-19": ["fever", "cough", "shortness of breath", "loss of taste", "fatigue"],
            "Diabetes": ["increased thirst", "frequent urination", "unexplained weight loss", "fatigue"],
            "Hypertension": ["headache", "dizziness", "blurred vision", "chest pain"],
            "Migraine": ["headache", "nausea", "sensitivity to light", "blurred vision"]
        }
        self.patient_symptoms = []

    def display_conditions(self):
        print("Known medical conditions:")
        for condition in self.conditions.keys():
            print(f"- {condition}")

    def input_symptoms(self):
        print("\nEnter symptoms (comma-separated):")
        symptoms = input().lower().split(", ")
        self.patient_symptoms.extend(symptoms)
        print("Symptoms recorded.")

    def diagnose(self):
        if not self.patient_symptoms:
            print("No symptoms provided.")
            return
        
        possible_diagnoses = []
        for condition, symptoms in self.conditions.items():
            if any(symptom in self.patient_symptoms for symptom in symptoms):
                possible_diagnoses.append(condition)

        if possible_diagnoses:
            print("\nPossible diagnoses based on symptoms:")
            for diagnosis in possible_diagnoses:
                print(f"- {diagnosis}")
        else:
            print("\nNo matching conditions found. Consider further medical tests.")

    def reset(self):
        self.patient_symptoms = []
        print("Patient data reset.")

agent = HealthcareDiagnosticAgent()

while True:
    print("\nWhat would you like to do?")
    print("1. View known medical conditions")
    print("2. Enter patient symptoms")
    print("3. Get diagnosis")
    print("4. Reset patient data")
    print("5. Exit")
    
    choice = input("Enter your choice: ")

    if choice == '1':
        agent.display_conditions()
    elif choice == '2':
        agent.input_symptoms()
    elif choice == '3':
        agent.diagnose()
    elif choice == '4':
        agent.reset()
    elif choice == '5':
        print("Thank you for using the Healthcare Diagnostic Agent!")
        break
    else:
        print("Invalid choice. Please select a valid option.")
