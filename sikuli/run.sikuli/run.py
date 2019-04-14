from sikuli import *

def export_change_location_of_none():
    wait("1554075375588.png", 20)
    click("1554075375588.png")
    wait("1554075417741.png", 20)
    click("1554075417741.png")
    wait("1554075445476.png", 20)
    click("1554075445476.png")
    wait("1554075470527.png" or "1554075896836.png", 20)
    click("1554075470527.png" or "1554075896836.png")
    wait("1554075509907.png", 20)
    click("1554075509907.png")
    wait("1554075534832.png", 20)
    click("1554075534832.png")
    wait("1554075562637.png", 20)
    click("1554075562637.png")
    wait("1554075591401.png", 20)
    click("1554075591401.png")
    wait("1554075618567.png", 20)
    click("1554075618567.png")
    wait("1554075673330.png", 20)
    click("1554075673330.png")

def export_book_small_courier():
    wait("1554947668161.png", 20)
    click("1554947668161.png")
    wait("1554947244570.png", 20)
    click("1554947244570.png")
    i = 1
    max = 3
    while not exists("1554947768600.png") and i < max:
        i = i + 1
        type(Key.PAGE_DOWN)
    click("1554947864809.png")
    type(Key.TAB)
    type(Key.UP)
    type(Key.UP)
    i = 1
    while not exists("1554948261120.png") and i < max:
        i = i + 1
        type(Key.PAGE_DOWN)
    click("1554948261120.png")
    wait("1554948289732.png", 20)
    click("1554948289732.png")
    sleep(0.5)
    type(Key.DOWN)
    type(Key.ENTER)
    click("1554948425029.png")
    i = 1
    while not exists("1554948456076.png") and i < max:
        i = i + 1
        type(Key.PAGE_DOWN)
    click("1554948474619.png")    
    i = 1
    while not exists("1554948557935.png" or "1554948957756.png") and i < max:
        i = i + 1
        type(Key.PAGE_DOWN)
    if exists("1554948918448.png"):
        click("1554948557935.png" or "1554948957756.png")
    i = 1
    wait("1554967794511.png", 20)
    while not exists("1554966159289.png") and i < max:
        i = i + 1
        type(Key.PAGE_DOWN)
    click("1554966159289.png")
    i = 1
    while not exists("1554966237620.png") and i < max:
        i = i + 1
        type(Key.PAGE_DOWN)
    click("1554966237620.png")
    i = 1
    while not exists("1554966267666.png") and i < max:
        i = i + 1
        type(Key.PAGE_DOWN)
    click("1554966290738.png")
    i = 1
    while not exists("1554966374989.png" or "1554966388789.png") and i < max:
        i = i + 1
        type(Key.PAGE_DOWN)
    if exists("1554966424381.png"):
        click("1554966499162.png")
        type(Key.F10, KeyModifier.SHIFT)
        wait("1554966793979.png")
        type("l")
        wait("1554966817132.png")
        type(Key.RIGHT)
        type(Key.RIGHT)
        type(Key.DOWN)
        type(Key.DOWN)
        type(Key.DOWN)
        type(Key.ENTER)
        type("v", KeyModifier.CTRL)

def export_confirm_courier():
    click("1554966374989.png" or "1554966388789.png")
    
    
    
    
    