from progress_tracker import calculate_progress_score
from calorie_adjustment import adjust_calories


def generate_progress_report(
        goal,
        previous_weight,
        current_weight,
        workout_consistency,
        sleep_hours,
        activity_level,
        current_calories,
        water_intake=3):

    score_data = calculate_progress_score(
        previous_weight=previous_weight,
        current_weight=current_weight,
        workout_consistency=workout_consistency,
        sleep_hours=sleep_hours,
        activity_level=activity_level,
        water_intake=water_intake
    )

    calorie_data = adjust_calories(
        goal=goal,
        previous_weight=previous_weight,
        current_weight=current_weight,
        current_calories=current_calories
    )

    return {
        **score_data,
        **calorie_data
    }