import musicalbeeps as mb
import tkinter as tk
import functools


class Tuner():
    '''
    by default the tuner note is "E", the series of notes are notes in standard 
    tuning, and the timer is set to 3.
    '''
    def __init__(self):
        self._note = "E"
        self._series = ["E","A","D","G","B","E"]
        self._timer = 3
        
    def play_note(self):
        '''
        this plays a single note.
        '''
        player = mb.Player( volume = .5, mute_output= False)
        ##change
        time = self._timer
        note = self._note
        player.play_note(note, time)
    
    def play_series(self):
        '''
        this plays a series of notes.
        '''
        player = mb.Player( volume = .5, mute_output= False)
        ##change
        time = self._timer
        for note in self._series:
            player.play_note(note, time)
    def set_timer(self):
        '''
        this method will update the timer as the user clicks on it.
        '''
        while True:
            if self._timer == 3:
                self._timer = 5
                break
            elif self._timer == 5:
                self._timer = 10
                break
            elif self._timer == 10:
                self._timer = 3
                break        
            
class Tuner_GUI():
    
    def __init__(self, root):
        self._backend = Tuner()
        root.title("Guitar Tuner")
        self._entry = tk.Entry(root, width=40, borderwidth=5)
        self._entry.grid(row=0, column=0, columnspan=4, 
                         padx=10, pady=10)
        self._entry.insert(0, "Select a note or a series of notes.")
        ## lines 60 through 97 is code to add buttons onto the GUI.
        c = 0
        r = 2
        buttons = 0
        self._buttons = ["A", "A#", "B", "C","C#", "D", "E", "F", "F#", "G", "G#"]
        for i in self._buttons:
            function = functools.partial(self.button_function, i)
            if len(i) == 1:
                scale = tk.Button(root, text= i, padx=40, pady=20, command = function, fg = "blue")
                scale.grid(row=r, column=c)
                self._buttons[buttons] = scale
                buttons +=1
                c += 1
                if c == 4:
                    r += 1
                    c = 0
            if len(i) == 2:
                scale = tk.Button(root, text= i, padx=35, pady=20, command = function, fg = "blue")
                scale.grid(row=r, column=c)
                self._buttons[buttons] = scale
                buttons +=1
                c += 1
                if c == 4:
                    r += 1
                    c = 0
        self._buttons.append("Time")
        function = self.adjust_timer
        self._buttons[11] = tk.Button(root, text= "Time", padx=28, pady=20, command = function, fg = "red")
        self._buttons[11].grid(row = r, column = c)

        
        self._buttons.append("Play")
        function = self.play_note
        self._buttons[12] = tk.Button(root, text= "Play Note", padx=80, pady=20, command = function, fg = "green")
        self._buttons[12].grid(row = 5, column = 0, columnspan = 4)
        
        self._buttons.append("Series")
        function = self.series
        self._buttons[13] = tk.Button(root, text= "Custom Tuning", padx=80, pady=20, command = function, fg = "green")
        self._buttons[13].grid(row = 6, column = 0, columnspan = 4)
        
        
    def button_function(self, text):
        '''
        once a user clicks a note button, that note will be displayed on 
        the entry box.
        '''
        self._entry.delete(0, tk.END) 
        self._entry.insert(0, text)
        self._backend._note = text
    def play_note(self):
        '''
        this plays the note the user selected.
        '''
        self._entry.delete(0, tk.END)
        self._entry.insert(0, f"Note {self._backend._note} played.")
        self._backend.play_note()
    def adjust_timer(self):
        ''' 
        this method is coded to the timer button, which will update the timer
        everytime that button is clicked.
        '''
        self._entry.delete(0, tk.END)
        self._backend.set_timer()
        self._entry.insert(0, f"Changed to: {self._backend._timer} seconds")
    def series(self):
        '''
        this method will play the series of notes the user has inputed.
        '''
        self._backend._series = []
        for note in self._entry.get().split(', '):
            self._backend._series.append(note)
        self._backend.play_series()
        self._entry.delete(0, tk.END)
        self._entry.insert(0, f"Your custom tuning has been played.")
        
if __name__ == "__main__":  
    root = tk.Tk()
    tuner = Tuner_GUI(root)
    root.mainloop()
 