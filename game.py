import tkinter as tk
from tkinter import messagebox

def remove_match_char(list1, list2):
    for i in range(len(list1)):
        for j in range(len(list2)):
            if list1[i] == list2[j]:
                c = list1[i]
                list1.remove(c)
                list2.remove(c)
                return [list1 + ["*"] + list2, True]
    return [list1 + ["*"] + list2, False]

def calculate_relationship():
    p1 = entry_p1.get().lower().replace(" ", "")
    p2 = entry_p2.get().lower().replace(" ", "")
    
    if not p1 or not p2:
        messagebox.showerror("Error", "Please enter both names.")
        return
    
    p1_list = list(p1)
    p2_list = list(p2)
    
    proceed = True
    while proceed:
        ret_list = remove_match_char(p1_list, p2_list)
        con_list = ret_list[0]
        proceed = ret_list[1]
        star_index = con_list.index("*")
        p1_list = con_list[:star_index]
        p2_list = con_list[star_index+1:]
    
    count = len(p1_list) + len(p2_list)
    result = ["Friends", "Love", "Affection", "Marriage", "Enemy", "Siblings"]
    
    while len(result) > 1:
        split_index = (count % len(result) - 1)
        if split_index >= 0:
            right = result[split_index + 1:]
            left = result[:split_index]
            result = right + left
        else:
            result = result[:len(result) - 1]
    
    relationship_label.config(text="Relationship status: " + result[0])

root = tk.Tk()
root.title("Flames Game")
root.geometry("400x400")
root.configure(bg="#ffb6c1")

heading_label = tk.Label(root, text="Flames Game", font=("Arial", 20, "bold"), fg="black", bg="#ffb6c1")
heading_label.pack(pady=20)

label_p1 = tk.Label(root, text="Player 1 name:", font=("Arial", 12), fg="black", bg="#ffb6c1")
label_p1.pack()

entry_p1 = tk.Entry(root, font=("Arial", 12))
entry_p1.pack()

label_p2 = tk.Label(root, text="Player 2 name:", font=("Arial", 12), fg="black", bg="#ffb6c1")
label_p2.pack()

entry_p2 = tk.Entry(root, font=("Arial", 12))
entry_p2.pack()

calculate_button = tk.Button(root, text="Calculate", font=("Arial", 12, "bold"), command=calculate_relationship)
calculate_button.pack(pady=20)

relationship_label = tk.Label(root, text="", font=("Arial", 14, "bold"), fg="black", bg="#ffb6c1")
relationship_label.pack()

root.mainloop()
