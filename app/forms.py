from flask_wtf import FlaskForm
from wtforms import DecimalField, SelectField, SubmitField
from wtforms.validators import DataRequired


class BeamForm(FlaskForm):
    lenght = DecimalField("Довжина, м (L)", validators=[DataRequired()])
    step = DecimalField("Крок, м (B)", validators=[DataRequired()])

    building_type = SelectField(
        "Тип будівлі",
        choices=[("beam", "ТРЦ"), ("A_office", "Офіс класу А"), ("column", "Колони")],
    )

    beam_type = SelectField(
        "Тип будівлі",
        choices=[("beam", "ТРЦ"), ("truss", "Ферми"), ("column", "Колони")],
    )

    g_load = DecimalField("Постійне навантаження, кг/м2", validators=[DataRequired()])
    q_load = DecimalField(
        "Довготривале навантаження, кг/м2", validators=[DataRequired()]
    )
    payload = DecimalField("Корисне навантаження, кг/м2", validators=[DataRequired()])

    submit = SubmitField("Розрахувати")