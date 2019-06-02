from flask_sqlalchemy import SQLAlchemy
import logging as lg
import enum

from .views import app
# Create database connection object
db = SQLAlchemy(app)

content1 = """
        Toi, tu n'as pas peur d'être seul ! Les grands espaces et les aventures sont faits pour toi. D'ailleurs, Koh 
        Lanta est ton émission préférée ! Bientôt tu partiras les cheveux au vent sur ton radeau. 
        Tu es aussi un idéaliste chevronné. Quelle chance !
    """

content2 = """
        Toi, tu sais comment utiliser la console ! Jamais à court d'idées pour
        réaliser ton objectif, tu es déterminé-e et persévérant-e. Tes amis disent d'ailleurs volontiers que tu
        as du caractère et que tu ne te laisses pas marcher sur les pieds. Un peu hacker sur les bords, tu aimes
        trouver des solutions à tout problème. N'aurais-tu pas un petit problème d'autorité ? ;-)
    """

content3 = """
        À broyer constamment du noir il est très difficile de sortir des ténèbres sombres de son inconscience, 
        à moins de laisser passer sur soi la luminosité du soleil ou ses rayons chauds qui peuvent nous aider à 
        reprendre conscience et goût avec la vie...
    """

content4 = """
        À chaque fois que vous vous mettez en colère, c'est de l'énergie cérébrale que vous gaspillez inutilement...
        Gardez vos neurones au calme et ils feront en sorte que le choc de vos idées n'en sera
        que plus efficace et plus productif en rendement...
    """

content5 = """
        À continuellement s'en laver les mains, quand vous n'avez pas d'eau, 
        elles demeureront toujours aussi sales et vous serez de plus en plus gêné de serrer
        les mains de gens qui attendent votre appui pour soutenir leurs idées ou leurs projets !
    """

class Gender(enum.Enum):
    female = 0
    male = 1
    other = 2


class Content(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(2000), nullable=False)
    gender = db.Column(db.Enum(Gender), nullable=False)

    def __init__(self, description, gender):
        self.description = description
        self.gender = gender


def init_db():
    db.drop_all()
    db.create_all()
    db.session.add(Content(content1, Gender["male"]))
    db.session.add(Content(content2, Gender["female"]))
    db.session.add(Content(content3, Gender["male"]))
    db.session.add(Content(content2, Gender["female"]))
    db.session.add(Content(content5, Gender["other"]))
    db.session.commit()
    lg.warning('Database initialized!')
