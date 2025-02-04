class TreatmentRecommendationAgent:
    def __init__(self, patient_data, treatments):
        self.patient_data = patient_data
        self.treatments = treatments

    def calculate_utility(self, treatment):
        matched_symptoms = [symptom for symptom in self.patient_data["symptoms"] if symptom in treatment["treats"]]
        symptom_match_ratio = len(matched_symptoms) / len(self.patient_data["symptoms"]) if self.patient_data["symptoms"] else 0

        if len(matched_symptoms) == 0:
            return -1000  

        dynamic_symptom_weight = self.patient_data["symptom_match_weight"]
        if symptom_match_ratio == 1:
            dynamic_symptom_weight *= 1.5  

        utility = (
            self.patient_data["effectiveness_weight"] * treatment["effectiveness"] -
            self.patient_data["side_effects_weight"] * treatment["side_effects"] -
            self.patient_data["cost_weight"] * treatment["cost"] +
            dynamic_symptom_weight * symptom_match_ratio
        ) 

        return utility

    def recommend_treatment(self):
        best_treatment = None
        max_utility = float("-inf")

        for treatment in self.treatments:
            utility = self.calculate_utility(treatment)
            if utility > max_utility:
                max_utility = utility
                best_treatment = treatment

        return best_treatment


medical_history = input("Enter known medical conditions (comma-separated): ").lower().split(", ")
symptoms = input("Enter current symptoms (comma-separated): ").lower().split(", ")

effectiveness_weight = float(input("Enter weight for effectiveness (higher is better): "))
side_effects_weight = float(input("Enter weight for side effects (lower is better): "))
cost_weight = float(input("Enter weight for cost (lower is better): "))
symptom_match_weight = float(input("Enter weight for symptom match (higher is better): "))

treatments = [
    {"name": "Ibuprofen", "effectiveness": 8, "side_effects": 3, "cost": 2, "treats": ["pain", "inflammation"]},
    {"name": "Paracetamol", "effectiveness": 7, "side_effects": 2, "cost": 1, "treats": ["fever", "pain"]},
    {"name": "Amoxicillin", "effectiveness": 9, "side_effects": 4, "cost": 5, "treats": ["infection"]},
    {"name": "Metformin", "effectiveness": 8, "side_effects": 3, "cost": 4, "treats": ["diabetes"]},
    {"name": "Atorvastatin", "effectiveness": 9, "side_effects": 5, "cost": 6, "treats": ["high cholesterol"]},
    {"name": "Antihistamine", "effectiveness": 7, "side_effects": 2, "cost": 3, "treats": ["allergy", "inflammation"]},
]

patient_data = {
    "medical_history": medical_history,
    "symptoms": symptoms,
    "effectiveness_weight": effectiveness_weight,
    "side_effects_weight": side_effects_weight,
    "cost_weight": cost_weight,
    "symptom_match_weight": symptom_match_weight
}

agent = TreatmentRecommendationAgent(patient_data, treatments)

recommended_treatment = agent.recommend_treatment()

if recommended_treatment:
    print("\nRecommended Treatment:", recommended_treatment["name"])
else:
    print("\nNo suitable treatment found. Consider consulting a doctor.")
