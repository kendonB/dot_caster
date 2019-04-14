from sikuli import *

def export_to_pasture_and_climate_folder():
    type("d", KeyModifier.ALT)
    Settings.TypeDelay = 0
    type("X:\\projects_ac\\Team_folder\\Papers\\pasture_and_climate")
    type(Key.ENTER)

def export_to_team_folder():
    type("d", KeyModifier.ALT)
    type("X:\\projects_ac\\Team_folder")
    type(Key.ENTER)

def export_to_pasture_writing_folder():
    type("d", KeyModifier.ALT)
    type("X:\\Apps\\Overleaf\\pasture\\writeup")
    type(Key.ENTER)