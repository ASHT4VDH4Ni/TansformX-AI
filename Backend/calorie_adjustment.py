def adjust_calories(
        goal,
        previous_weight,
        current_weight,
        current_calories):

    goal = goal.lower()

    weight_change = previous_weight - current_weight

    recommendation = "Maintain current calories."

    # Plateau detection
    if abs(weight_change) < 0.3:

        if goal == "weight loss":

            current_calories -= 150

            recommendation = (
                "Weight loss plateau detected. "
                "Reduce calories slightly and increase activity."
            )

        elif goal == "muscle gain":

            current_calories += 150

            recommendation = (
                "Muscle gain plateau detected. "
                "Increase calories slightly."
            )

    return {
        "recommended_calories": current_calories,
        "recommendation": recommendation
    }