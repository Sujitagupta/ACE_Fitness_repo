from flask import Flask, request, jsonify, render_template, redirect, url_for

app = Flask(__name__)

# store workouts per gym_id
workouts_by_gym = {}

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

@app.route("/add_workout_form", methods=["POST"])
def add_workout_form():
    gym_id = request.form.get("gym_id")
    workout = request.form.get("workout")
    duration = request.form.get("duration")

    if not gym_id or not workout or not duration:
        return "Gym ID, workout, and duration are required", 400

    try:
        duration = int(duration)
        if gym_id not in workouts_by_gym:
            workouts_by_gym[gym_id] = []
        workouts_by_gym[gym_id].append({"workout": workout, "duration": duration})
        return redirect(url_for("home"))
    except ValueError:
        return "Duration must be a number", 400

@app.route("/view_workouts", methods=["POST"])
def view_workouts():
    gym_id = request.form.get("gym_id")

    if not gym_id:
        return "Gym ID required", 400

    gym_workouts = workouts_by_gym.get(gym_id, [])
    return render_template("view_workouts.html", gym_id=gym_id, workouts=gym_workouts)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
