from flask_wtf import FlaskForm
from wtforms import DecimalField, SelectField, SubmitField


class BeamForm(FlaskForm):
    length = DecimalField("Довжина, м (L)")
    step = DecimalField("Крок, м (B)")
    construction_type = SelectField(
        "Тип конструкції",
        choices=[("floor", "Перекриття"), ("roof", "Покриття")],
    )

    building_type = SelectField(
        "Тип будівлі",
        choices=[
            ("mall", "ТРЦ"),
            ("A_office", "Офіс класу А"),
            ("B_office", "Офіс класу В або нижче"),
            ("prom", "Промислова будвіля"),
            ("other", "Інше"),
        ],
    )

    g_load = DecimalField("Постійне")
    q_load = DecimalField("Довготривале")
    payload = DecimalField("Корисне")

    submit = SubmitField("Розрахувати")