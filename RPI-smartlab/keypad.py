import RPi.GPIO as GPIO
# GPIO.setmode(GPIO.BOARD)
GPIO.setmode(GPIO.BCM)
key = [0,1,2,3,4,5,6,7,8,9,'*','#']
pin = [21,20,16,19,26]
pad = [0,0,0,0]
password_user = ["1234","6789"]
# 0000 = 0
# 1000 = 1
# 0100 = 2
# 1100 = 3
# 0010 = 4
# 1010 = 5
# 0110 = 6
# 1110 = 7
# 0001 = 8
# 1001 = 9
# 1011 = *
# 1111 = #
for i in range(len(pin)):
    GPIO.setup(pin[i], GPIO.IN)


def key():
    num = 0
    if (GPIO.input(pin[0]) == 1):num = num + 1
    if (GPIO.input(pin[1]) == 1):num = num + 2
    if (GPIO.input(pin[2]) == 1):num = num + 4
    if (GPIO.input(pin[3]) == 1):num = num + 8
    return num


def ticker():

    ticker = GPIO.input(pin[4])
    return ticker


if __name__ == '__main__':

    stage = 1
    password = ""
    pas = ticker()
    inp = 0
    lastinp = 0
    while True:
        pas = ticker()
        inp = key()
        lastinp = inp
        if(pas == 0):
            stage = 0
        elif(pas == 1):
            if(stage == 0):
                if(inp == lastinp) : password += str(inp)
                stage = 1

                while True :
                     if(key() == 15): break
                     if(key() == 13):
                         password = ""
                     tg = ticker()
                     if(tg == 0):
                         stage = 0
                     elif(tg == 1):
                         if(stage == 0):
                             password += str(key())
                             stage = 1
                if(password != str(lastinp)):print password
        password = ""
