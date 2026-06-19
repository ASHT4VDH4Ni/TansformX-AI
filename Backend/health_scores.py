def calculate_health_scores(
        sleep_hours,
        water_intake,
        workout_days):

    # Sleep score
    if sleep_hours >= 8:
        sleep_score = 100
    elif sleep_hours >= 7:
        sleep_score = 85
    elif sleep_hours >= 6:
        sleep_score = 70
    else:
        sleep_score = 50

    # Hydration score
    if water_intake >= 3:
        hydration_score = 100
    elif water_intake >= 2:
        hydration_score = 80
    else:
        hydration_score = 60

    # Habit score
    habit_score = min(workout_days * 15, 100)

    return {
        "sleep_score": sleep_score,
        "hydration_score": hydration_score,
        "habit_score": habit_score
    }