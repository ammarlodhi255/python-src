import pywhatkit

# Set the time in 24-hour format (HH:MM:SS) when you want the message to be sent
time = "12:56:15"
# Set the phone number that you want to send the message to
phone_number = "123"
# Set the message that you want to send
message = "Your message goes here"
# Use the sendwhatmsg method to send the message at the specified time
pywhatkit.sendwhatmsg(time, phone_number, message, 2)
