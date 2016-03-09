#LCD.py Documentation



#TODO
- Fix the current line wraping bug
- Make a function that will keep the Top "Calcbar" there through a clear
- Make the "Led stuff" its one function
- **Stuff**

##About
The LCD.py script was devluped for use with the calc.py script to produce a Calculator that was able to use a Python CAS system.

#Configuration
##Dependines
- RPi.GPIO
- python2
- time
- lcd

##Pin Configs
The pin configuration is based off of the **GPIO** Number **NOT** the Pin number. Using the pin number will make it all not work
The pin configs should be made in the "Define GPIO to LCD mapping" section
>### Standerd LCD Pinout
> The wiring for the LCD is as follows:
 1 : GND
 2 : 5V
 3 : Contrast (0-5V)*
 4 : RS (Register Select)
 5 : R/W (Read Write)       - GROUND THIS PIN
 6 : Enable or Strobe
 7 : Data Bit 0             - NOT USED
 8 : Data Bit 1             - NOT USED
 9 : Data Bit 2             - NOT USED
 10: Data Bit 3             - NOT USED
 11: Data Bit 4
 12: Data Bit 5
 13: Data Bit 6
 14: Data Bit 7
 15: LCD Backlight +5V
 16: LCD Backlight GND
* Pin 15 and 16 are for the lcd backlight, this will only work for a lcd with a backligt*
***

#Functions
Check out the lcd.py file for gr8t info aswell

## lcd_init
This function must be called at the beging of a programing wanting to use the lcd, this fuction sets up the GPIO pins with the wiring pi lib and Sets the lcd backlight. **NOTICE** After caling the lcd_init function please allow 2 sec of delay so the lcd can set itself up. Failing to do so will resault in a lcd not printing the approprieat text or the wrong charictors. **NOTICE** 


## lcd_clear
Dose what it says, sends the clear bit code and depending on the git branch prints out calc functions (TBL Y= CALC OPTS)
**Notice** Please allow there to be a delay for the display to clear, clearing the display takes time **Notice**

##lcd_curser
The funcition will simply send a bit code to the display to set a certan curcer type

| ID | Resault|
|----:|:-------|
| 0  | Off       |
| 1  | Underline |
| 2  | Block     |

## lcd_backlight
Dose what it says, turns on the backlight
- Accepts True or false
- lcd_init must have been called inorder to turn on backlight


##lcd_string
This funciton is used to send a string of text to the display
- Accepts ("Message",style)
 - Message is a string and style is a int from 1 to 3

| ID | Resault|
|----:|:-------|
| 1 |Left Justifed|
| 2 | Centered |
|3|Right Justified|

##lcd_byte
Used to send Display spsfick information or costome charactos. (More info coming soon... )
- Accepts (bits, mode)
 - bits are the data you want to send in hex format (ex. 0x0F)
 - mode is True for false
   - True will send the data in character mode
   - False will send the data in command mode
