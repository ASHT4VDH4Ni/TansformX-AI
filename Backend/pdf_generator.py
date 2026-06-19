from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import cm
from datetime import datetime


def generate_pdf(
        plan_text,
        progress_data=None,
        user_data=None,
        filename=None):

    now = datetime.now()

    if filename is None:

        filename = (
            "TransformX_"
            + now.strftime("%d-%b-%Y_%I-%M-%p")
            + ".pdf"
        )
    
    doc = SimpleDocTemplate(filename)

    styles = getSampleStyleSheet()

    story = []

    # Cover Page
    story.append(
        Paragraph(
            "TransformX AI",
            styles["Title"]
        )
    )

    story.append(
        Paragraph(
            "60-Day Transformation Report",
            styles["Heading2"]
        )
    )

    story.append(Spacer(1, 1 * cm))

    story.append(
        Paragraph(
            "Personalized AI-generated fitness report powered by TransformX AI.",
            styles["BodyText"]
        )
    )

    story.append(Spacer(1, 1 * cm))

    story.append(
        Paragraph(
            f"Generated on: {now.strftime('%d %B %Y, %I:%M %p')}",
            styles["BodyText"]
        )
    )

    story.append(
        Spacer(1, 0.5 * cm)
    )
    

        # User Profile
    if user_data:

        story.append(
            Paragraph(
                "User Profile",
                styles["Heading1"]
            )
        )

        story.append(
            Spacer(1, 0.3 * cm)
        )

        profile_items = [
            f'Age: {user_data["age"]}',
            f'Gender: {user_data["gender"]}',
            f'Height: {user_data["height"]} cm',
            f'Weight: {user_data["weight"]} kg',
            f'Goal: {user_data["goal"]}',
            f'Experience Level: {user_data["experience_level"]}',
            f'Workout Location: {user_data["workout_location"]}',
            f'Diet Preference: {user_data["diet_preference"]}'
        ]

        for item in profile_items:

            story.append(
                Paragraph(
                    "• " + item,
                    styles["BodyText"]
                )
            )

        story.append(
            Spacer(1, 1 * cm)
        )

    # Weekly Progress Section
    if progress_data:

        story.append(
            Paragraph(
                "Weekly Progress Summary",
                styles["Heading1"]
            )
        )

        story.append(Spacer(1, 0.3 * cm))

        items = [
            f'Progress Score: {progress_data["progress_score"]}/100',
            f'Sleep Score: {progress_data["sleep_score"]}/100',
            f'Hydration Score: {progress_data["hydration_score"]}/100',
            f'Habit Score: {progress_data["habit_score"]}/100',
            f'Transformation Score: {progress_data["transformation_score"]}/100'
        ]

        for item in items:

            story.append(
                Paragraph(
                    "• " + item,
                    styles["BodyText"]
                )
            )

        story.append(Spacer(1, 0.5 * cm))

        story.append(
            Paragraph(
                "AI Coach Message",
                styles["Heading2"]
            )
        )

        story.append(
            Paragraph(
                progress_data["coach_message"],
                styles["BodyText"]
            )
        )

        story.append(Spacer(1, 0.5 * cm))

        story.append(
            Paragraph(
                "Calorie Recommendation",
                styles["Heading2"]
            )
        )

        story.append(
            Paragraph(
                f'Recommended Calories: {progress_data["recommended_calories"]}',
                styles["BodyText"]
            )
        )

        story.append(
            Paragraph(
                progress_data["recommendation"],
                styles["BodyText"]
            )
        )

        story.append(Spacer(1, 1 * cm))

        # Main AI Plan
    lines = plan_text.split("\n")

    for line in lines:

        line = line.strip()

        # Remove markdown artifacts
        line = line.replace("***", "")
        line = line.replace("---", "")

        if not line:
            continue

        if line.startswith("### "):

            story.append(
                Paragraph(
                    line[4:],
                    styles["Heading2"]
                )
            )

        elif line.startswith("## "):

            story.append(
                Paragraph(
                    line[3:],
                    styles["Heading2"]
                )
            )

        elif line.startswith("# "):

            story.append(
                Paragraph(
                    line[2:],
                    styles["Title"]
                )
            )

        elif line.startswith("* "):

            story.append(
                Paragraph(
                    "• " + line[2:],
                    styles["BodyText"]
                )
            )

        elif line.startswith("- "):

            story.append(
                Paragraph(
                    "• " + line[2:],
                    styles["BodyText"]
                )
            )

        else:

            story.append(
                Paragraph(
                    line,
                    styles["BodyText"]
                )
            )

        story.append(
            Spacer(1, 0.15 * cm)
        )

    doc.build(story)

    return filename