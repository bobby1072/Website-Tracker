from location_grab import *
import tkinter as tk
from map_generator import *
import os
def show_all_butt():
    gen_map = show_all()
    os.startfile(gen_map)
def input_grab():
    try:
        web_dom = web_dom_entry.get()
        web_ip = ip_get(web_dom)
        map_data = data_grab(web_ip, web_dom)
        gen_map = map_gen(map_data, web_dom)
        os.startfile(gen_map)
    except:
        tk.Label(master, text = "please enter a valid URL").grid(row  = 5, column =1)
if __name__ == "__main__":
    master = tk.Tk()
    master.geometry("440x200")
    master.title("ip locater")
    tk.Label(master, text = "please enter the url you would like to see the location of:").grid(row = 0, sticky = "w")
    web_dom_entry = tk.Entry(master)
    web_dom_entry.grid(row = 0, column = 1, sticky = "w")
    tk.Button(text="search location", command=input_grab).grid(row=3, column=1)
    tk.Button(text="show all locations", command=show_all_butt).grid(row=3, column=0)
    master.mainloop()
