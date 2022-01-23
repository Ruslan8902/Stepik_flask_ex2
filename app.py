from flask import Flask, render_template, redirect, url_for, request
import os

from forms import UserForm, MoveForm
import story_game

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY') or "any_key"


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/username', methods=['post', 'get'])
def username():
    user_form = UserForm()
    if user_form.validate_on_submit():
        story_game.Game(username=user_form.username.data, x=0, y=2)
        return game()
    return render_template('username.html', form=user_form)


@app.route("/game", methods=['post', 'get'])
def game():
    player = story_game.Game()
    move_form = MoveForm()
    # if move_form.validate_on_submit():
    #     story_game.Game(username=move_form.username.data, x=0, y=2)
    #     return game()
    if player.attempt == 0:
        player.attempt += 1
        message = "Вчерашний поход к барону явно удался. Сейчас вы в пыльной непонятной комнате и Ваше самочувствие после бурной ночи оставляяет желать лучшего. Глоток воздуха - вот лучшее решение. Пора пробираться к <u>балкону</u>."
        return render_template("game.html", username=player.username, map=player.map, form=move_form, message=message,
                               message_class="alert alert-info")
    else:
        message, message_class = player.move(move_form.direction.data, move_form.steps_q.data)
        return render_template("game.html", username=player.username, map=player.map, form=move_form, message=message,
                               message_class=message_class)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
