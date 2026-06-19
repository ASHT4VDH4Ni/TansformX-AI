from health_scores import calculate_health_scores
from coach_personality import generate_coach_message


def calculate_progress_score(
        previous_weight,
        current_weight,
        workout_consistency,
        sleep_hours,
        activity_level,
        water_intake=3):

    score = 50

    # Weight progress
    weight_change = abs(previous_weight - current_weight)

    score += min(weight_change * 5, 20)

    # Workout consistency
    score += workout_consistency * 3

    # Sleep quality
    if sleep_hours >= 7:
        score += 10

    # Activity level
    activity_level = activity_level.lower()

    if activity_level == "active":
        score += 10

    elif activity_level == "moderate":
        score += 5

    score = min(round(score), 100)

    # Health scores
    health_scores = calculate_health_scores(
        sleep_hours=sleep_hours,
        water_intake=water_intake,
        workout_days=workout_consistency
    )

    # Transformation score
    transformation_score = round(
        (
            score
            + health_scores["sleep_score"]
            + health_scores["hydration_score"]
            + health_scores["habit_score"]
        ) / 4
    )

    coach_message = generate_coach_message(
        transformation_score
    )

    return {
        "progress_score": score,
        "sleep_score": health_scores["sleep_score"],
        "hydration_score": health_scores["hydration_score"],
        "habit_score": health_scores["habit_score"],
        "transformation_score": transformation_score,
        "coach_message": coach_message
    }