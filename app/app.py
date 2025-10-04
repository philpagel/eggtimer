#! /usr/bin/env python3
import os
from flask import Flask, request, render_template
from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField
from wtforms.validators import ValidationError, DataRequired, NumberRange
from flask_bootstrap import Bootstrap
import eggtime


app = Flask(__name__)
app.config["SECRET_KEY"] = (
    os.environ.get("SECRET_KEY") or "virus-toilet-cake-eruption-harmony"
)
bootstrap = Bootstrap(app)


@app.route("/", methods=["GET", "POST"])
def home():
    form = EggForm()
    if request.method == "POST":
        min, sec = eggtime.ms(
            eggtime.BoilingTime(
                m=int(request.form["mass"]),
                t0=int(request.form["start_temp"]),
                t1=int(request.form["target_temp"]),
                e=int(request.form["elevation"]),
            )
        )
        return render_template("eggtime.html", title="Egg timer", form=form, btime=(min, sec))
    else:
        return render_template("eggtime.html", title="Egg timer", form=form, btime=(None, None))


class EggForm(FlaskForm):
    mass = IntegerField(
            "Egg mass [g]", default=60, 
            validators=[
                DataRequired(), 
                NumberRange(min=20, max=150, message="Mass must be in [20, 150]g")
                ]
            )
    start_temp = IntegerField(
            "Start temperature [°C]", default=6, 
            validators=[
                DataRequired(),
                NumberRange(min=4, max=40, message="Start temperature must be in [4, 40] °C")
                ]
            )
    target_temp = IntegerField(
            "Target temperature [°C]", default=71, 
            validators=[
                DataRequired(),
                NumberRange(min=30, max=90, message="Target temperature must be in [30, 90] °C")
                ]
            )
    elevation = IntegerField(
            "Elevation [m]", default=340, 
            validators=[
                DataRequired(),
                NumberRange(min=0, max=8000, message="Elevation must be in [0, 8000] m")
                ]
            )
    submit = SubmitField("Compute")


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
