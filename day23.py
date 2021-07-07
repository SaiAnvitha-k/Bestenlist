# creating jpeg file to png
import tkinter as tk
from tkinter import filedialog
from PIL import Image
root = tk.Tk()

canvas1 = tk.Canvas(root, width = 550, height = 550, bg='lavender', relief='raised')
canvas1.pack()
label1 = tk.Label(root, text='Image conversion from JPEG to PNG')
label1.config(font=('calibre', 20))
canvas1.create_window(250,40, window=label1)

def getJPG():
    global im1
    import_file_path = filedialog.askopenfilename()
    im1 = Image.open(import_file_path)


browseButton_JPG = tk.Button(text="Import JPG File", command=getJPG, bg='pink', fg='white', font=('calibre', 12, 'bold'))
canvas1.create_window(250, 200, window=browseButton_JPG)

def converttoPNG():
    global im1
    export_file_path = filedialog.asksaveasfilename(defaultextension='.png')
    im1.save(export_file_path)

saveasbutton_PNG = tk.Button(text='convert JPG to PNG', command=converttoPNG, bg='pink', fg='white', font=('calibri', 12, 'bold'))
canvas1.create_window(250, 280, window=saveasbutton_PNG)
root.mainloop()



# create weather forecast app
from configparser import ConfigParser
import requests
from tkinter import *
from tkinter import messagebox

# extract key from the
# configuration file
config_file = "config.ini"
config = ConfigParser()
config.read(config_file)
api_key = config['gfg']['api']
url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}'


# explicit function to get
# weather details
def getweather(city):
    result = requests.get(url.format(city, api_key))

    if result:
        json = result.json()
        city = json['name']
        country = json['sys']
        temp_kelvin = json['main']['temp']
        temp_celsius = temp_kelvin - 273.15
        weather1 = json['weather'][0]['main']
        final = [city, country, temp_kelvin,
                 temp_celsius, weather1]
        return final
    else:
        print("NO Content Found")


# explicit function to
# search city
def search():
    city = city_text.get()
    weather = getweather(city)
    if weather:
        location_lbl['text'] = '{} ,{}'.format(weather[0], weather[1])
        temperature_label['text'] = str(weather[3]) + "   Degree Celsius"
        weather_l['text'] = weather[4]
    else:
        messagebox.showerror('Error', "Cannot find {}".format(city))


# Driver Code
# create object
app = Tk()
# add title
app.title("Weather App")
# adjust window size
app.geometry("300x300")

# add labels, buttons and text
city_text = StringVar()
city_entry = Entry(app, textvariable=city_text)
city_entry.pack()
Search_btn = Button(app, text="Search Weather",
                    width=12, command=search)
Search_btn.pack()
location_lbl = Label(app, text="Location", font={'bold', 20})
location_lbl.pack()
temperature_label = Label(app, text="")
temperature_label.pack()
weather_l = Label(app, text="")
weather_l.pack()
app.mainloop()


# create a button for pdf file and add merge option to it
from tkinter import *

# Importing tkPDFViewer to place pdf file in gui.
# In tkPDFViewer library there is
# an tkPDFViewer module. That I have imported as pdf

from tkPDFViewer import tkPDFViewer as pdf

# Initializing tk

root = Tk()

# Set the width and height of our root window.

root.geometry("550x750")

# creating object of ShowPdf from tkPDFViewer.
v1 = pdf.ShowPdf()

# Adding pdf location and width and height.

v2 = v1.pdf_view(root,

                 pdf_location=r"location",

                 width=50, height=100)

# Placing Pdf in my gui.
v2.pack()
pdf_merge = tk.Tk()
pdf_merge.pack()
def pdfmerge():
    global pdf1
    import_file_path = filedialog.askopenfilename()
    pdf1 = Image.open(import_file_path)

browseButton_merge = tk.Button(text="Merge pdf file", command=pdfmerge, bg='pink', fg='white', font=('calibre', 12, 'bold'))

pdf_merge.create_window(250, 200, window=browseButton_merge)
root.mainloop()

