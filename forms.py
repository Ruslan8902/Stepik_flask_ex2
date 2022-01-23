from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, IntegerField
from wtforms.validators import DataRequired, Length, NumberRange


class UserForm(FlaskForm):
    username = StringField("Введите имя вашего героя:",
                           validators=[DataRequired(), Length(min=2, message="Имя слишком короткое.")])
    submit = SubmitField("Начать испытание")


class MoveForm(FlaskForm):
    direction = SelectField(
        "Выберете сторону света, в которую желаете отправиться",
        coerce=int,
        choices=[
            (0, "Север"),
            (1, "Восток"),
            (2, "Юг"),
            (3, "Запад")
        ],
        render_kw={
            'class': 'form-control'
        }
    )
    steps_q = IntegerField(
        "Как далеко планируете продвинуться?",
        validators=[NumberRange(min=1), DataRequired()],
        default=1,
        render_kw={
            'class': 'form-control'
        }
    )
    submit = SubmitField("В путь")
