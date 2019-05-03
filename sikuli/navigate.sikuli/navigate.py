from sikuli import *
from platform import node
from os import system

def export_to_pasture_and_climate():
    type("d", KeyModifier.ALT)
    if node() == "DESKTOP-VUFG094":
        system("echo D:\\Dropbox\\projects_ac\\Team_folder\\Papers\\pasture_and_climate|clip")
    else:
        system("echo X:\\projects_ac\\Team_folder\\Papers\\pasture_and_climate|clip")
    type("v", KeyModifier.CTRL)
    type(Key.ENTER)

def export_to_team_folder():
    Settings.TypeDelay = 0
    type("d", KeyModifier.ALT)
    if node() == "DESKTOP-VUFG094":
        system("echo D:\\Dropbox\\projects_ac\\Team_folder|clip")
    else:
        system("echo X:\\projects_ac\\Team_folder|clip")
    type("v", KeyModifier.CTRL)
    type(Key.ENTER)

def export_to_pasture_writing():
    Settings.TypeDelay = 0
    type("d", KeyModifier.ALT)
    if node() == "DESKTOP-VUFG094":
        system("echo D:\\Dropbox\\Apps\\Overleaf\\pasture\\writeup|clip")
    else:
        system("echo X:\\Apps\\Overleaf\\pasture\\writeup|clip")
    type("v", KeyModifier.CTRL)
    type(Key.ENTER)