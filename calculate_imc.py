def calculate_bmi(peso,altura):
    return peso /(altura **2)

def classify_bmi(imc):
    if imc < 18.5:
        return "Underweight"
    elif imc < 24.5:
        return"Normal weight"
    elif imc < 29.9:
        return "Overweight"
    elif imc < 34.9:
        return "Obesity grade 1"
    elif imc < 39.9:
        return "Obesity grade 2"
    else:
        return "Obesity grade 3(morbid)"
while True:
    try:
        print("\n=== BMI Calculator ===")
        print("Enter -1 as weight to exit.")
        peso = float(input("Enter your weight (kg): "))
        if peso == -1:
            print("Exiting the program. See you!")
            break
        altura = float(input("Enter your height(m): " ))
        if peso <=0 or altura <=0:
            print("Error:  weight and height must be positive values")
            continue
        imc = calculate_bmi(peso,altura)
        situacao = classify_bmi(imc)

        print(f"\nYour BMI is: {imc:.2f}")
        print(f"Status: {situacao}")

    except ValueError:
     print("Invalid input! Please enter numeric values!")

