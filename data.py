# -*- coding: utf-8 -*-

EMAIL_SERVER = 'smtp.example.com'
EMAIL_USERNAME = 'example@example.com'
EMAIL_PASSWORD = 'example_password'
EMAIL_SUBJECT = 'Secret Santa'
EMAIL_TEXT = """
             Dear {},
             This year your secret santa is:
             {}
             Merry Christmas
             """

DATA_NAME = 'name'
DATA_EMAIL = 'email'
DATA_EXCLUDED = 'excluded'
DATA_SECRET_SANTA = 'secret_santa'

players = [
    {
        DATA_NAME: 'Player 0',
        DATA_EMAIL: 'player1@example.com',
        DATA_EXCLUDED: (0, )
    },  # 0 will not be assigned himself
    {
        DATA_NAME: 'Player 1',
        DATA_EMAIL: 'player1@example.com',
        DATA_EXCLUDED: (1, 2)
    },  # 1 will not be assigned neither himself nor the next player
    {
        DATA_NAME: 'Player 2',
        DATA_EMAIL: 'player2@example.com',
        DATA_EXCLUDED: (2, )
    },  # 2 will not be assigned himself
]
