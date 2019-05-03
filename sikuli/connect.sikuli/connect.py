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
    myApp = App("chrome") 
    myApp.open("c:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe")
    myApp.focus()
    chrome_win = myApp.window()
    sleep(1)
    myregion = Region(1515,31,177,118)
    myregion.wait("1556572425014.png", 20)
    sleep(1)
    myregion.click("1556572425014.png")
    sleep(0.5)
    type("nesi")
    wait("1556573000290.png" or "1556573014366.png", 20)
    hover("1556573000290.png" or "1556573014366.png")
    click("1556573035955.png")
    wait("1556573052115.png", 5)
    click("1556573052115.png")
    rsApp.focus()
    wait("1553546938544.png",20)
    type(Key.INSERT, KeyModifier.SHIFT)
    type(Key.ENTER)
    #wait("1553547481815.png", 40)
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
    wait("1553559866667.png" or "1553559453521.png", 60)
    click("1553559866667.png")
    wait("1553559453521.png", 20)
    click("1553559453521.png")
    wait("1553559518312.png", 20)
    click("1553559518312.png")
    wait("1553559545546.png", 20)
    click("1553559545546.png")
    type("landcare\\bellk")
    type(Key.TAB)
    myApp = App("chrome") 
    myApp.open("c:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe")
    myApp.focus()
    sleep(1)
    corner = Region(1519,3,311,93)
    corner.wait("1552968938463.png", 20)
    sleep(1)
    corner.click("1552968938463.png")
    sleep(0.5)
    type("landcare")
    wait("1554883299729.png" or "1554883318010.png", 20)
    hover("1554884096651.png" or "1554883318010.png")
    wait("1554884619671.png", 5)
    click("1554884619671.png")
    wait("1554884698064.png", 5)
    click("1554884698064.png")
    type(Key.TAB, KeyModifier.ALT)
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

