from fastapi.responses import FileResponse
from pdf_generator import generate_pdf
from fastapi import FastAPI, UploadFile, File
import os
from pydantic import BaseModel
from agents import Runner

from transformx_agents.supervisor_agent import supervisor_agent
from body_analyzer import analyze_body
from progress_report import generate_progress_report


app = FastAPI()

latest_plan = ""
latest_progress_data = None
latest_user_data = None


class UserInput(BaseModel):
    age: int
    gender: str
    height: float
    weight: float
    goal: str

    experience_level: str
    workout_location: str
    diet_preference: str
    activity_level: str
    sleep_hours: float
    injuries: str


class WeeklyProgressInput(BaseModel):
    previous_weight: float
    current_weight: float
    workout_consistency: int
    sleep_hours: float
    activity_level: str


@app.get("/")
def home():
    return {"message": "TransformX AI Backend Running"}


@app.post("/generate-plan")
async def generate_plan(user_data: UserInput):

    global latest_plan
    global latest_user_data

    body_data = analyze_body(
        user_data.height,
        user_data.weight
    )

    latest_user_data = {
        "age": user_data.age,
        "gender": user_data.gender,
        "height": user_data.height,
        "weight": user_data.weight,
        "goal": user_data.goal,
        "experience_level": user_data.experience_level,
        "workout_location": user_data.workout_location,
        "diet_preference": user_data.diet_preference
    }

    prompt = f"""
Age: {user_data.age}

Gender: {user_data.gender}

Height: {user_data.height} cm

Weight: {user_data.weight} kg

Goal: {user_data.goal}

Experience Level: {user_data.experience_level}

Workout Location: {user_data.workout_location}

Diet Preference: {user_data.diet_preference}

Activity Level: {user_data.activity_level}

Average Sleep Hours: {user_data.sleep_hours}

Existing Injuries: {user_data.injuries}

===== BODY ANALYSIS =====

BMI: {body_data["bmi"]}

BMI Category: {body_data["bmi_category"]}

Body Type: {body_data["body_type"]}

Body Fat Category: {body_data["body_fat_category"]}

Create a complete 60-day transformation plan.
"""

    result = await Runner.run(
        supervisor_agent,
        prompt
    )

    latest_plan = result.final_output

    return {
        "body_analysis": body_data,
        "plan": result.final_output
    }


@app.post("/weekly-progress")
def weekly_progress(progress_data: WeeklyProgressInput):

    global latest_progress_data

    latest_progress_data = generate_progress_report(
        goal="weight loss",
        previous_weight=progress_data.previous_weight,
        current_weight=progress_data.current_weight,
        workout_consistency=progress_data.workout_consistency,
        sleep_hours=progress_data.sleep_hours,
        activity_level=progress_data.activity_level,
        current_calories=2200
    )

    return latest_progress_data


@app.post("/upload-photos")
async def upload_photos(
    front_photo: UploadFile = File(...),
    side_photo: UploadFile = File(...),
    back_photo: UploadFile = File(...)
):

    os.makedirs("uploads", exist_ok=True)

    front_path = f"uploads/front_{front_photo.filename}"
    side_path = f"uploads/side_{side_photo.filename}"
    back_path = f"uploads/back_{back_photo.filename}"

    with open(front_path, "wb") as f:
        f.write(await front_photo.read())

    with open(side_path, "wb") as f:
        f.write(await side_photo.read())

    with open(back_path, "wb") as f:
        f.write(await back_photo.read())

    return {
        "message": "Photos uploaded successfully",
        "front_photo": front_path,
        "side_photo": side_path,
        "back_photo": back_path
    }


@app.get("/download-report")
def download_report():

    filename = generate_pdf(
    latest_plan,
    latest_progress_data,
    latest_user_data
   )

    return FileResponse(
        filename,
        media_type="application/pdf",
        filename=filename
    )