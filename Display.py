import I2C_LCD_driver

class Display:

    _currentLines = ["","","","",""]

    def __init__(self):
        self.initDisplay()

    def display(self, text, regelnr):
        self.writeDisplay(text,regelnr)

    def clear(self):
        self.clearDisplay()

    def initDisplay(self):
        global mylcd
        mylcd = I2C_LCD_driver.lcd()
        return

    def writeDisplay(self, text, line):
        global mylcd
        oldText = self._currentLines[line]
        if (not text == oldText):
            mylcd.lcd_display_string(text.ljust(20), line)
            self._currentLines[line] = text

    def clearDisplay(self):
        global mylcd
        mylcd.lcd_display_string(" ".ljust(20), 1)
        mylcd.lcd_display_string(" ".ljust(20), 2)
        mylcd.lcd_display_string(" ".ljust(20), 3)
        mylcd.lcd_display_string(" ".ljust(20), 4)
