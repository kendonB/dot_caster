from sikuli import *

def export_berkeley():
    cisco = App("vpnui") 
    cisco.open("c:\\Program Files (x86)\\Cisco\\Cisco AnyConnect Secure Mobility Client\\vpnui.exe")
    cisco.focus()
    wait("1553046081451.png",20)
    print "test"
    type(Key.ENTER)
    wait("1553027960331.png",20)
    myApp = App("chrome") 
    myApp.open("c:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe")
    myApp.focus()
    sleep(1)
    wait("1556570762238.png", 20)
    sleep(1)
    click("1556570762238.png")
    sleep(0.5)
    type("berkeley")
    wait("1553029567872.png", 20)
    rightClick("1553029567872.png")
    wait( "1552976558516.png", 5)
    click( "1552976558516.png")
    cisco.focus()
    type("v", KeyModifier.CTRL)
    type(Key.ENTER)

def export_nessie():
    type("nes")
    type(Key.ENTER)
    rsApp = App("rstudio") 
    wait("1553546938544.png",20)
    chrApp = App("chrome") 
    chrApp.open("c:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe")
    chrApp.focus()
    chrome_win = chrApp.window()
    sleep(1)
    bounds = getBounds()
    if bounds.width == 2560:
        myregion = Region(1815,0,745,592)
        myregion.wait("1556921910501.png", 20)
        sleep(1)
        myregion.click("1556921910501.png")
        sleep(0.5)
        type("nesi")
        myregion.wait("1556924242319.png", 20)
        myregion.hover("1556924242319.png")
        myregion.click("1556922131105.png")
        myregion.wait("1556922146447.png", 5)
        myregion.click("1556922146447.png")
    rsApp.focus()
    wait("1553546938544.png",20)
    type(Key.INSERT, KeyModifier.SHIFT)
    type(Key.ENTER)
    wait("1556925563954.png", 10)
    authApp = App("Authy Desktop") 
    authApp.open("C:\\Users\\kmbel\\AppData\\Local\\authy-electron\\app-1.7.0\\Authy Desktop.exe")
    authApp.focus()
    if bounds.width == 2560:
        wait("1556925997888.png", 20)
        click("1556925997888.png")
        wait("1556926051509.png")
        click("1556926088228.png")
    authApp.close()
    rsApp.focus()
    wait("1553546938544.png", 20)
    type(Key.INSERT, KeyModifier.SHIFT)
    type(Key.ENTER)
    chrApp.focus()
    if bounds.width == 2560:
        myregion = Region(1815,0,745,592)
        myregion.wait("1556921910501.png", 20)
        sleep(1)
        myregion.click("1556921910501.png")
        sleep(0.5)
        type("nesi")
        myregion.wait("1556924242319.png", 20)
        myregion.hover("1556924242319.png")
        myregion.click("1556922131105.png")
        myregion.wait("1556922146447.png", 5)
        myregion.click("1556922146447.png")
    rsApp.focus()
    wait("1553546938544.png",20)
    type(Key.INSERT, KeyModifier.SHIFT)
    type(Key.ENTER)
    type(Key.ENTER)
    
    
    
    
        
    #type(Key.INSERT, KeyModifier.SHIFT)
    #type(Key.ENTER)
    #type(Key.ENTER)
     
def export_nessie_files():
    myApp = App("WinSCP") 
    myApp.open("C:\\Program Files (x86)\\WinSCP\\WinSCP.exe")
    myApp.focus()
    wait("1554876402597.png", 20)
    click("1554876423572.png")
    sleep(1) 
    type(Key.ENTER)   
        
def export_manaaki_whenua():
    ie = App("iexplore") 
    ie.open("c:\\Program Files\\Internet Explorer\\iexplore.exe")
    ie.focus()
    wait("1553559247901.png", 20)
    click("1553559247901.png")
    bounds = getBounds()
    i = 0
    while (not exists("1553559866667.png", 0)) and (not exists("1556932004469.png", 0)) and i < 20:
        i = i + 1
        sleep(1)
    if exists("1556932004469.png", 0) == None:
        click("1553559866667.png")
    wait("1556932004469.png", 20)
    click("1556932004469.png")
    i = 0
    while (not exists("1553559518312.png", 0)) and (not exists("1556933256581.png", 0)) and i < 20:
        i = i + 1
        sleep(1)
    if exists("1553559518312.png", 0) != None:
        click("1553559518312.png")
    i = 0
    while (not exists("1553559545546.png", 0)) and (not exists("1556933256581.png", 0)) and i < 20:
        i = i + 1
        sleep(1)
    if exists("1553559545546.png", 0) == None:
        click("1556933256581.png")
    else:
        click("1553559545546.png")
    type("landcare\\bellk")
    type(Key.TAB)
    myApp = App("chrome") 
    myApp.open("c:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe")
    myApp.focus()
    sleep(0.2)
    bounds = getBounds()
    if bounds.width == 2560:
        corner = Region(1761,0,799,662)
    else:    
        corner = Region(1519,3,311,93)
    corner.wait("1552968938463.png", 20)
    sleep(1)
    corner.click("1552968938463.png")
    sleep(0.5)
    type("landcare")
    corner.wait("1556934099307.png", 20)
    corner.hover("1556934099307.png")
    corner.wait("1556934268444.png", 5)
    corner.click("1556934268444.png")
    corner.wait("1556934302000.png", 5)
    corner.click("1556934302000.png")
    type(Key.TAB, KeyModifier.ALT)
    sleep(0.2)
    type("v", KeyModifier.CTRL) 
    type(Key.ENTER) 

def export_kupe():
    type("kup")
    type(Key.ENTER)
    wait("1554854935912.png",20)
    myApp = App("chrome") 
    myApp.open("c:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe")
    myApp.focus()
    chrome_win = myApp.window()
    sleep(1)
    wait("1552968938463.png", 20)
    sleep(1)
    click("1552968938463.png")
    sleep(0.5)
    type("kupe")
    wait("1554854984864.png" or "1554855009038.png", 20)
    hover("1554854984864.png" or "1554855009038.png")
    click("1554852022818.png")
    wait("1554852045701.png", 5)
    click("1554852045701.png")
    type(Key.TAB, KeyModifier.ALT)
    wait("1554854935912.png",20)
    type(Key.INSERT, KeyModifier.SHIFT)
    type(Key.ENTER)

