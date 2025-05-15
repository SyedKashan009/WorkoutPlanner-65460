def calculate_bmi(weight, height_ft):
    height_m = height_ft * 0.3048  # Convert feet to meters
    return weight / (height_m ** 2)

def suggest_plan(bmi):
    if bmi < 18.5:
        workout_plan = "Underweight: 30 mins of light workout. Diet: High-protein, high-calorie meals."
        gym_recommendation = "Recommend working out at home with bodyweight exercises."
    elif 18.5 <= bmi < 24.9:
        workout_plan = "Normal: 45 mins of balanced workout. Diet: Maintain healthy meals with protein, carbs, and fiber."
        gym_recommendation = "Recommend working out at the gym for balanced exercises (strength and cardio)."
    elif 25 <= bmi < 29.9:
        workout_plan = "Overweight: 60 mins of moderate workout. Diet: Low-carb, high-fiber meals."
        gym_recommendation = "Recommend working out at the gym for effective weight management and strength training."
    else:
        workout_plan = "Obese: 60–90 mins of cardio and strength. Diet: Consult a dietitian; avoid sugar and processed foods."
        gym_recommendation = "Recommend working out at the gym for structured and supervised workouts."
    
    return workout_plan, gym_recommendation

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
        workout_plan, gym_recommendation = suggest_plan(bmi)

        print(f"\nYour BMI is: {bmi:.2f}")
        print(workout_plan)
        print(gym_recommendation)

    except ValueError as e:
        print(f"Input Error: {e}")
    except Exception as e:
        print(f"Unexpected error occurred: {e}")

# Run the app
if __name__ == "__main__":
    get_user_input()
