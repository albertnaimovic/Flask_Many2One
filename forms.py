from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, SubmitField
from wtforms.validators import DataRequired
from wtforms_sqlalchemy.fields import QuerySelectField
from app import Vaikas


def vaikas_query():
    return Vaikas.query.all()


class TevasForm(FlaskForm):
    vardas = StringField("Vardas", [DataRequired()])
    pavarde = StringField("Pavardė", [DataRequired()])
    vaikas = StringField("Vaiko_id")
    # vaikas = QuerySelectField(
    #     query_factory=vaikas_query,
    #     allow_blank=True,
    #     get_label="vardas",
    #     get_pk=lambda obj: str(obj),
    # )
    submit = SubmitField("Įvesti")


class VaikasForm(FlaskForm):
    vardas = StringField("Vardas", [DataRequired()])
    pavarde = StringField("Pavardė", [DataRequired()])
    submit = SubmitField("Įvesti")
