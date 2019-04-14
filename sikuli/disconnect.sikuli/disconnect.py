from sikuli import *

def export_berkeley():
    type("d", KeyModifier.WIN)
    click("1553046792554.png")
    wait("1553046835009.png", 20)
    rightClick("1553046835009.png")
    type(Key.UP)
    type(Key.ENTER)