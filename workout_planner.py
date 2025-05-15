def calculate_bmi(weight, height_ft):
    height_m = height_ft * 0.3048  # Convert feet to meters
    return weight / (height_m ** 2)

def suggest_plan(bmi):
    if bmi < 18.5:
        return "Underweight: 30 mins of light workout.\nDiet: High-protein, high-calorie meals."
    elif 18.5 <= bmi < 24.9:
        return "Normal: 45 mins of balanced workout.\nDiet: Maintain healthy meals with protein, carbs, and fiber."
    elif 25 <= bmi < 29.9:
        return "Overweight: 60 mins of moderate workout.\nDiet: Low-carb, high-fiber meals."
    else:
        return "Obese: 60–90 mins of cardio and strength.\nDiet: Consult a dietitian; avoid sugar and processed foods."

def get_user_input():
    try:
        weight = input("Enter your weight in kg: ").strip()
        height = input("Enter your height in feet: ").strip()

        if not weight or not height:
            raise ValueError("Fields cannot be empty.")

        weight = float(weight)
        height = float(height)

        if weight <= 0 or height <= 0:
            raise ValueError("Weight and height must be positive numbers.")

        bmi = calculate_bmi(weight, height)
        plan = suggest_plan(bmi)

        print(f"\nYour BMI is: {bmi:.2f}")
        print(plan)

    except ValueError as e:
        print(f"Input Error: {e}")
    except Exception as e:
        print(f"Unexpected error occurred: {e}")

if __name__ == "__main__":
    get_user_input()
