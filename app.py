import os
from flask import Flask, request, render_template
from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField
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
        #return f"Boiling time:  {m}min {s}sec"
        return render_template("eggtime.html", title="Egg timer", form=form, btime=(min, sec))
    else:
        return render_template("eggtime.html", title="Egg timer", form=form, btime=(0, 0))


class EggForm(FlaskForm):
    mass = IntegerField("Egg mass [g]", default=70)
    start_temp = IntegerField("Start temperature [°C]", default=6)
    target_temp = IntegerField("Target temperature [°C]", default=70)
    elevation = IntegerField("Elevation [m]", default=0)
    submit = SubmitField("Compute")
