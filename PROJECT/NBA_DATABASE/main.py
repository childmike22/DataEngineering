import pandas as pd
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
SQLALCHEMY_TRACK_MODIFICATIONS = False

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///nba_data.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# TODO 1A: Create a new column that combines name and college for a uniuqe identifier
df = pd.read_csv('nba_data - data.csv')
df['combination'] = df['player_name'] + ' ' + df['college']


# TODO vA Team Class (relationships include: [players, seasons]
class Team(db.Model):
    __tablename__ = 'teams'
    id = db.Column(db.Integer, primary_key=True)
    abbreviation = db.Column(db.String, unique=True)
    # parent relationship - seasons
    seasons = db.relationship('Seasons', backref='team')


# TODO vB Players Class (relationships include: [team, seasons]
class Players(db.Model):
    __tablename__ = 'players'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    college = db.Column(db.String, nullable=False)
    country = db.Column(db.String, nullable=False)
    age_first_season = db.Column(db.Integer, nullable=False)
    # parent relationship - seasons
    seasons = db.relationship('Seasons', backref='players')


# TODO vC Seasons Class (relationships include: [team, players]
class Seasons(db.Model):
    __tablename__ = 'seasons'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    team_abbr = db.Column(db.String, nullable=False)
    season = db.Column(db.String, nullable=False)
    # child relationship - teams
    team_id = db.Column(db.Integer, db.ForeignKey('teams.id'), nullable=False)
    # child relationship - players
    player_id = db.Column(db.Integer, db.ForeignKey('players.id'), nullable=False)

# TODO IMPORTANT - actual creation
# db.create_all()

# steph_curry = Seasons(name='stephen curry', team_abbr='GSW', season='2019-2020', team=Team.query.filter_by(abbreviation='GSW').first())
# db.session.add(steph_curry)
# db.session.commit()

# TODO 1C: Import my Team Data
teams = list(df['team_abbreviation'].unique())
# Add them to my Database
# for abbr in teams:
#     new_team = Team(abbreviation=abbr)
#     db.session.add(new_team)
# db.session.commit()


# TODO 1B: Create my unique player table: columns include:
#  [player_name, college, age, country, ]
# Creates a series - convert it to a DF
players_df = df.groupby(['combination', 'player_name', 'college', 'country'])['age'].min().to_frame()
# # Reset our Index for a clean DF
# players_df.reset_index(inplace=True)
# for index, row in players_df.iterrows():
#     new_player = Players(
#         name=row['player_name'],
#         college=row['college'],
#         country=row['country'],
#         age_first_season=row['age'],
#
#     )
#     db.session.add(new_player)

# db.session.commit()


# TODO 1C: Create my unique seasons table
# First, must fill na values
df.drop(df[df['combination'].isna()].index, inplace=True)
df.drop(df[df['college'].isna()].index, inplace=True)
df.drop(df[df['combination'] == 'Enes Kanter None'].index, inplace=True)

#
# print(df[df['player_name'] == 'Enes Kanter'])
for index, row in df.iterrows():
    new_season = Seasons(
        players=Players.query.filter_by(name=row['player_name']).filter_by(college=row['college']).first(),
        team=Team.query.filter_by(abbreviation=row['team_abbreviation']).first(),
        name=row['player_name'],
        team_abbr=row['team_abbreviation'],
        season=row['season'])
#     db.session.add(new_season)
# db.session.commit()
