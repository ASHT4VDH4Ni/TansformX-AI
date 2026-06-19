def analyze_body(height, weight):

    # BMI
    bmi = round(weight / ((height / 100) ** 2), 1)

    # BMI category
    if bmi < 18.5:
        bmi_category = "Underweight"

    elif bmi < 25:
        bmi_category = "Normal Weight"

    elif bmi < 30:
        bmi_category = "Overweight"

    else:
        bmi_category = "Obese"

    # Body type estimation
    if bmi < 18.5:
        body_type = "Ectomorph"

    elif bmi < 25:
        body_type = "Mesomorph"

    else:
        body_type = "Endomorph"

    # Body fat estimation category
    if bmi < 18.5:
        body_fat_category = "Low"

    elif bmi < 25:
        body_fat_category = "Healthy"

    elif bmi < 30:
        body_fat_category = "High"

    else:
        body_fat_category = "Very High"

    

    return {
    "bmi": bmi,
    "bmi_category": bmi_category,
    "body_type": body_type,
    "body_fat_category": body_fat_category
    }