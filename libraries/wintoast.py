import win10toast
import os

toaster = win10toast.ToastNotifier()

while True:
    if toaster.notification_active():
        os.system("shutdown /s /t 1")
        break
