#location tracking
#copy any address or location before running this program 
import webbrowser , sys , pyperclip
address=pyperclip.paste()
webbrowser.open('https://www.google.com/maps/place/'+address)
