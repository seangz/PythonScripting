
def gather_info():
    height = float(input("What is your height? (Inches or Meters) "))
    weight = float(input("What is your weight? (lbs or kgs) "))
    unit = input("Are your measurements in metric or imperial units? ").lower() .strip()
    return (height, weight, unit)

def calculate_bmi(weight, height, unit='metric'):
    if unit == 'metric':
        bmi = (weight / (height ** 2))
    else:
        bmi = 703 * (weight / (height ** 2))
    print ("Your BMI is %s" % bmi)


while True:
    height, weight, unit = gather_info()
    if unit.startswith('i'):
        calculate_bmi(weight = weight, height = height, unit = 'imperial')
    elif unit.startswith('m'):
        calculate_bmi(weight, height, unit)
        break
    else:
        print("Error: Unknown measurement system. Please use imperial or metric.")      

    
    