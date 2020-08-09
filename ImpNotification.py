import time
from plyer import notification

while True:
    notification.notify(
        title = "WATER TIME",
        message = "There are many different opinions on how much water you should be drinking every day. Health authorities commonly recommend eight 8-ounce glasses, which equals about 2 liters, or half a gallon",
        # app_icon = "E:\Practice\Python practice\Projects\Notification\icon.ico",
        timeout= 10
    )
    time.sleep(3600)