import tkinter as tk

import requests
import json
from datetime import datetime, date
from PIL import ImageTk, Image

class Weather_Backend():
    ''' This is the back-end code.
    '''
    def __init__(self):
        self._city_name = "Duarte"  
        self._current_temp = 0
        self._max_temp = 0
        self._min_temp = 0
        self._current_humid = 0
        self._date_time = "Today"
        
    def pull_city_data(self):
        api = "81e93efb85d3990e35b5aa67a245f94c"
        base_url = "http://api.openweathermap.org/data/2.5/weather?"
        complete_url = base_url + "appid=" + api + "&q=" + self._city_name
        response = requests.get(complete_url)
        data = response.json()
        if data["cod"] != "404":
            ''' code 404 means the city has been found.
            '''
            date_time = datetime.now()
            self._date_time = date_time.strftime("%m/%d/%Y %H:%M")
            ##saving main
            data_main = data["main"]
            self._current_temp = self.kelvin_to_fahrenheit(data_main["temp"])
            self._max_temp = self.kelvin_to_fahrenheit(data_main["temp_max"])
            self._min_temp = self.kelvin_to_fahrenheit(data_main["temp_min"])
            self._current_humid = data_main["humidity"]
        else:
            self._date_time = "Error - city not found"
            self._current_temp = ""
            self._max_temp = ""
            self._min_temp = ""
            self._current_humid = ""
        
    def kelvin_to_fahrenheit(self, kelvin):
        ''' The data is calculated originally in kelvin, so this 
        function converts our data to fahrenheit.
        '''
        return(round((kelvin - 273.15) * 9/5 + 32))



class Weather_GUI():
    def __init__(self, root):
        root.title("Weather App") 
        root.columnconfigure( 2, weight = 1)
        root['background'] = 'blue'
        self._backend = Weather_Backend()
        ##Instruction label
        self._label = tk.Label(text = "Please enter the city you'd like the weather for:", bg = "black", fg = "white")
        self._label.grid()
        ##Search box
        self._entry = tk.Entry(fg = "white", bg = "black", width = 50)
        self._entry.insert(0,"Search")
        self._entry.grid( row = 2)
        ##Output labels and entry boxes
        self._date_time_output = tk.Entry( fg = "black", bg = "white")
        self._date_time_label = tk.Label(text = "Date - Time")
        self._date_time_label.grid( row = 4, pady = 5)
        self._date_time_output.grid(row = 5, pady = 5)
        self._temp_output = tk.Entry( fg = "black", bg = "white")
        self._temp_label = tk.Label(text = "Current Temperature")
        self._temp_label.grid(row = 6, pady = 5)
        self._temp_output.grid(row = 7, pady = 5)
        self._temp_high_output = tk.Entry(fg = "black", bg = "white")
        self._temp_high_label = tk.Label(text = "Today's High:")
        self._temp_high_label.grid(row = 8, pady = 5)
        self._temp_high_output.grid( row = 9, pady = 5)
        self._temp_low_output = tk.Entry(fg = "black", bg = "white")
        self._temp_low_label = tk.Label(text = "Today's Low:")
        self._temp_low_label.grid(row = 10, pady = 5)
        self._temp_low_output.grid(row = 11, pady = 5)
        self._humidity_output = tk.Entry(fg = "black", bg = "white")
        self._humidity_label = tk.Label(text = "Humidity")
        self._humidity_label.grid(row = 12, pady = 5)
        self._humidity_output.grid(row = 13, pady = 5)
        ##Search buttons and warning label
        self._search_button = tk.Button(text = "Enter", fg = "green", command = self.city_search)
        self._search_button.grid(row = 2, column = 1)
        self._warning = tk.Label(text = "All temperatures are in fahrenheit.", fg = "red", bg = "black")
        self._warning.grid(row = 17, pady = 15)

        
    def city_search(self):
        ''' This function returns and prints the weather data
        for the city the user is interested in.
        '''
        self._backend._city_name = self._entry.get()
        self._backend.pull_city_data()
        self._date_time_output.delete(0, tk.END)
        self._date_time_output.insert(0, self._backend._date_time)
        self._temp_output.delete(0, tk.END)
        self._temp_output.insert(0, self._backend._current_temp)
        self._temp_high_output.delete(0, tk.END)
        self._temp_high_output.insert(0, self._backend._max_temp)
        self._temp_low_output.delete(0, tk.END)
        self._temp_low_output.insert(0, self._backend._min_temp)
        self._humidity_output.delete(0, tk.END)
        self._humidity_output.insert(0, self._backend._current_humid)
        
if __name__ == "__main__":  
    root= tk.Tk()
    app = Weather_GUI(root)
    root.mainloop()
