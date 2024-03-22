class PersonMetrics:
    def __init__(self, weight_kg, height_m):
        self.weight = weight_kg
        self.height = height_m

    def BMI_Value(self):
        return self.weight / (self.height ** 2)

person = PersonMetrics(70, 1.75)
print(f"BMI: {person.BMI_Value():.2f}")
