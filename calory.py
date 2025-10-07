def calculate_bmr(weight, height, age, gender='male'):
    if gender == 'male':
        return 10 * weight + 6.25 * height - 5 * age + 5
    else:
        return 10 * weight + 6.25 * height - 5 * age - 161

def calculate_tdee(bmr, activity_level):
    return bmr * activity_level

def calculate_macros(total_calories, protein_ratio=0.3, carb_ratio=0.4, fat_ratio=0.3):
    protein_cal = total_calories * protein_ratio
    carb_cal = total_calories * carb_ratio
    fat_cal = total_calories * fat_ratio
    
    protein_g = protein_cal / 4
    carb_g = carb_cal / 4
    fat_g = fat_cal / 9
    
    return protein_g, carb_g, fat_g

def main():
    weight = 85  # kg
    height = 183  # cm
    age = int(input("Enter your age: "))
    gender = input("Enter your gender (male/female): ").strip().lower()
    print("Activity levels:\n1 - Sedentary (little or no exercise)\n2 - Light exercise (1-3 days/week)\n3 - Moderate exercise (3-5 days/week)\n4 - Heavy exercise (6-7 days/week)\n5 - Very heavy exercise (twice per day, extra heavy)")
    activity_choice = int(input("Choose your activity level (1-5): "))

    activity_multipliers = {1:1.2, 2:1.375, 3:1.55, 4:1.725, 5:1.9}
    activity_level = activity_multipliers.get(activity_choice, 1.2)

    goal = input("Enter your goal (bulk/cut/maintain): ").strip().lower()
    
    bmr = calculate_bmr(weight, height, age, gender)
    tdee = calculate_tdee(bmr, activity_level)
    
    if goal == "bulk":
        total_calories = tdee * 1.15  # +15% surplus
    elif goal == "cut":
        total_calories = tdee * 0.8   # -20% deficit
    else:
        total_calories = tdee         # maintain

    protein_g, carb_g, fat_g = calculate_macros(total_calories)

    print(f"\nYour BMR: {bmr:.2f} kcal")
    print(f"Your TDEE (maintenance calories): {tdee:.2f} kcal")
    print(f"Your target calories ({goal}): {total_calories:.2f} kcal")
    print(f"Recommended daily macros:")
    print(f"Protein: {protein_g:.2f} g")
    print(f"Carbohydrates: {carb_g:.2f} g")
    print(f"Fats: {fat_g:.2f} g")

if __name__ == "__main__":
    main()
