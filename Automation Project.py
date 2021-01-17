import pyautogui as pag
import webbrowser as wb
import time
import randfacts as rf
import os


def double_tab():
    pag.press("tab")
    pag.press("tab")

if __name__ == "__main__":
    # this is a list of my family and their T-shirt size    
    list_ppl = {"Patrick Vargas": "Medium", "Robert Vargas": "Large", "Erick Vargas" : "Medium", "Lupita Vargas": "Small", "Ramon Vargas" : "X-Large"}
    os.chdir("/Users/robertvargas/Documents/Projects/Python/Automation Project")
    #start of automation
    wb.open("https://docs.google.com/forms/d/e/1FAIpQLScZNtLeMjj8esUbkMKT3jymXq9HQ6n0Lu8RuzVcmulSsXd4gw/viewform")
    time.sleep(5)
    
    for key in list_ppl.keys():
        double_tab()
        pag.typewrite(key)
        pag.press("tab")
        if list_ppl[key] == "Small":
            pag.press("down")
            double_tab()
        elif list_ppl[key] == "Medium":
            pag.press("down")
            pag.press("down")
            double_tab()
        elif list_ppl[key] == "Large":
            pag.press("down")
            pag.press("down")
            pag.press("down")
            double_tab()
        elif list_ppl[key] == "X-Large":
            pag.press("down")
            pag.press("down")
            pag.press("down")
            pag.press("down")
            double_tab()
        else: 
            pag.press("tab")
        pag.typewrite(rf.getFact())
        pag.press("tab")
        pag.press("enter")
        wb.open("https://docs.google.com/forms/d/e/1FAIpQLScZNtLeMjj8esUbkMKT3jymXq9HQ6n0Lu8RuzVcmulSsXd4gw/viewform")
        time.sleep(5)
    print("all forms were filled in successfully")
