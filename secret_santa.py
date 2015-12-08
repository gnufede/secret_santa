#!/bin/env python2
# -*- coding: utf-8 -*-

from smtplib import SMTP
from itertools import permutations
from email.mime.text import MIMEText

from data import (
    EMAIL_SERVER, EMAIL_USERNAME, EMAIL_PASSWORD,
    EMAIL_SUBJECT, EMAIL_TEXT,
    DATA_NAME, DATA_EMAIL, DATA_EXCLUDED, DATA_SECRET_SANTA,
    players
    )


def login_email():
    server = SMTP(EMAIL_SERVER)
    server.starttls()
    server.login(EMAIL_USERNAME, EMAIL_PASSWORD)
    return server


def send_mail(server, email_to, subject, text):
    # Create a text/plain message
    msg = MIMEText(text)

    msg['Subject'] = subject
    msg['From'] = EMAIL_USERNAME
    msg['To'] = email_to

    # Send the message via our SMTP server, but don't include the
    # envelope header.
    server.sendmail(EMAIL_USERNAME, [email_to, ], msg.as_string())


def notify_players():
    server = login_email()
    for player in players:
        send_mail(
            server,
            player[DATA_EMAIL],
            EMAIL_SUBJECT,
            EMAIL_TEXT.format(
                player[DATA_NAME],
                player[DATA_SECRET_SANTA][DATA_NAME].upper()
            )
        )
    server.quit()


def find_valid_permutation():
    player_permutations = permutations([x for x in range(len(players))])
    excluded = [player[DATA_EXCLUDED] for player in players]
    for sample_result in player_permutations:
        if all([k not in v for k, v in zip(sample_result, excluded)]):
            return sample_result


def find_secret_santas():
    permutation = find_valid_permutation()
    for player, secret_santa in zip(players, permutation):
        player[DATA_SECRET_SANTA] = players[secret_santa]

find_secret_santas()
notify_players()
