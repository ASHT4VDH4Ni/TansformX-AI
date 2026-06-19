def generate_coach_message(
        transformation_score,
        plateau_detected=False):

    if plateau_detected:

        return (
            "Progress isn't always linear.\n\n"
            "Plateaus are normal.\n\n"
            "Stay patient and trust the process.\n\n"
            "Small adjustments lead to big results."
        )

    if transformation_score >= 90:

        return (
            "Outstanding work.\n\n"
            "You're building habits that will last a lifetime.\n\n"
            "Stay disciplined and trust the process."
        )

    elif transformation_score >= 80:

        return (
            "Great progress.\n\n"
            "Consistency beats perfection.\n\n"
            "Keep showing up every day."
        )

    elif transformation_score >= 70:

        return (
            "Week 3 is where many people quit.\n\n"
            "Progress isn't always linear.\n\n"
            "Stay patient and keep going."
        )

    elif transformation_score >= 60:

        return (
            "Small improvements compound over time.\n\n"
            "Focus on habits rather than motivation."
        )

    else:

        return (
            "Everyone starts somewhere.\n\n"
            "Forget perfection.\n\n"
            "Just aim to become better than yesterday."
        )