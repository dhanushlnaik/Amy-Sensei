import json
import os
import random

current_directory = os.path.dirname(__file__)
file_path = os.path.join(current_directory,  'data')


def get_momma_jokes():
    with open(os.path.join(file_path, "jokes.json"), encoding="utf8") as joke_file:
        jokes = json.load(joke_file)
    random_category = random.choice(list(jokes.keys()))
    insult = random.choice(list(jokes[random_category]))
    return insult


def get_truth():
    with open(os.path.join(file_path, "tord.json"), encoding="utf8") as tord_file:
        ques = json.load(tord_file)
    truth = random.choice(list(ques["truth"]))
    return truth


def get_dare():
    with open(os.path.join(file_path, "tord.json"), encoding="utf8") as tord_file:
        ques = json.load(tord_file)
    dare = random.choice(list(ques["dare"]))
    return dare


def get_wyr():
    with open(os.path.join(file_path, "tord.json"), encoding="utf8") as tord_file:
        ques = json.load(tord_file)
    wyr = random.choice(list(ques["wyr"]))
    return wyr


def get_nhie():
    with open(os.path.join(file_path, "tord.json"), encoding="utf8") as tord_file:
        ques = json.load(tord_file)
    nhie = random.choice(list(ques["nhie"]))
    return nhie
