import winsound
import time
from plyer import notification


if __name__ == "__main__":
    i = 0
    while i==0:
        notification.notify(title = "***IT'S TIME!!!!!MEDICINE TIME***",
                            message = "Eat medicine on time!!!!!!!!!!!",
                            app_icon = "C:\\Users\\rajesh\\Downloads\\clock.ico",timeout =2)

        winsound.Beep(2500,1000)  #freq,millisec


        time.sleep(6)
        i = 1
