import tkinter as tk
from tkinter import font
import requests

HEIGHT = 500
WIDTH = 600

# api.openweathermap.org/data/2.5/forecast?q={city name},{state code},{country code}&appid={API key}
# api key - 7b8bf1f0ccc6ffbab8c238ec3b91d63b

def test_function(entry):
    print("This is the entry: ",entry)

def format_response(weather):
    try:
        name = weather['name']
        desc = weather['weather'][0]['description']
        temp = weather['main']['temp']
        temp = (temp - 32)*(5/9)
        temp_c = "{:.2f}".format(temp)
        final_str = 'City: %s\nConditions: %s\nTemperature(C): %s' % (name,desc,temp_c)
    except:
        final_str = 'Input is not valid'
        
    return final_str
    
def get_weather(city):
    weather_key = '7b8bf1f0ccc6ffbab8c238ec3b91d63b'
    url='https://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': weather_key, 'q':city, 'units':'imperial'}
    response = requests.get(url, params=params)
    weather = response.json()
    
    label['text'] = format_response(weather)

root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

background_image = tk.PhotoImage(file="landscape.png")
background_label = tk.Label(root, image=background_image)
background_label.place(x=0,y=0,relwidth=1,relheight=1)

frame = tk.Frame(root, bg='#80c1ff', bd=5)
frame.place(relx=0.5, rely=0.1,relwidth=0.75, relheight=0.1, anchor='n')

entry = tk.Entry(frame, font=40)
entry.place(relwidth=0.65, relheight=1)

button = tk.Button(frame, text="Get Weather", font=40, command=lambda: get_weather(entry.get()))
button.place(relx=0.7, relheight=1,relwidth=0.3)

lower_frame = tk.Frame(root, bg='#80c1ff', bd=10)
lower_frame.place(relx=0.5, rely=0.25,relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame, font=('Britannic Bold',18), anchor='nw', justify='left', bd=4)
label.place(relwidth=1, relheight=1)

root.mainloop()