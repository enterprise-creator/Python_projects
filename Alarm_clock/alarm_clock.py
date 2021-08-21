from datetime import datetime
from playsound import playsound

alarm_time = input("Enter alarm time in HH:MM:SS ")
alarm_hr = alarm_time[0:2]
alarm_minutes = alarm_time[3:5]
alarm_seconds = alarm_time[6:8]
alarm_period = alarm_time[9:11].upper()

print("Alarm set up in progress")

while True:
    now = datetime.now()
    hr = now.strftime("%H")
    mint = now.strftime("%M")
    sec = now.strftime("%S")
    period = now.strftime("%p")

    if alarm_hr == hr and alarm_minutes == mint and alarm_seconds == sec and alarm_period == period:
        print("WAKE UPPP!")
        playsound('sci_fi_alarm.wav')
        break














