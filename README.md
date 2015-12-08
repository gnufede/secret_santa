# Secret santa email sender

This script is intended to play secret santa tradition.

Each player has an exclusion list, where not only himself/herself, but also another
players can be listed (for example to assign last year's results).

## Usage:

1. Modify `data.py` specifying the email account from where emails will be sent,
the players information (name, email, and exclusion list), and email subject and text.

2. Run `python2 secret_santa.py`
