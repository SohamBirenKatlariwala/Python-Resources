def calculate_bmi(weight, height):
    """
    Calculate BMI (Body Mass Index)
    Formula: weight (kg) / (height (m) * height (m))
    """
    return weight / (height * height)


def classify_bmi(bmi):
    """
    Classify BMI into categories
    """
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal weight"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"


def main():
    print("Welcome to the BMI calculator!")
    weight = float(input("Enter your weight in kilograms: "))
    height = float(input("Enter your height in meters: "))

    bmi = calculate_bmi(weight, height)
    category = classify_bmi(bmi)

    print(f"Your BMI is: {bmi:.2f}")
    print(f"You are classified as: {category}")


if __name__ == "__main__":
    main()
 
