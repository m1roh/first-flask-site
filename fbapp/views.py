#! /usr/bin/env python
from flask import Flask, render_template, url_for, request

app = Flask(__name__)

app.config.from_object('config')


from .utils import find_content

description = """
        Toi, tu sais comment utiliser la console ! Jamais à court d'idées pour
        réaliser ton objectif, tu es déterminé-e et persévérant-e. Tes amis disent d'ailleurs volontiers que tu
        as du caractère et que tu ne te laisses pas marcher sur les pieds. Un peu hacker sur les bords, tu aimes
        trouver des solutions à tout problème. N'aurais-tu pas un petit problème d'autorité ? ;-)
    """


@app.route('/')
def index():
    return render_template('index.html',
                           user_name='Julio',
                           user_image=url_for('static', filename='img/profile.png'),
                           description=description,
                           blur=True)


@app.route('/result/')
def result():
    try:
        gender = request.args.get('gender')
        user_name = request.args.get('first_name')
        uid = request.args.get('id')
        profile_pic = 'http://graph.facebook.com/' + uid + '/picture?type=large'

        return render_template('result.html',
                               user_name=user_name,
                               user_image=profile_pic,
                               description=find_content(gender))
    except KeyError:
        return render_template('result.html',
                               user_name=user_name,
                               user_image=profile_pic,
                               description=find_content('other'))


if __name__ == "__main__":
    app.run()
