import customtkinter as ctk
import random
import string

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# --- Strength calculation ---
def calculate_strength(password):
    length = len(password)
    score = 0

    if length >= 8:
        score += 1
    if length >= 12:
        score += 1
    if any(c.isupper() for c in password):
        score += 1
    if any(c.islower() for c in password):
        score += 1
    if any(c.isdigit() for c in password):
        score += 1
    if any(c in string.punctuation for c in password):
        score += 1

    return min(score, 5)

# --- Generate password ---
def generate_password():
    try:
        length = int(length_entry.get())
        chars = ""

        similar = "O0oIl1"

        if var_upper.get():
            chars += string.ascii_uppercase
        if var_lower.get():
            chars += string.ascii_lowercase
        if var_digits.get():
            chars += string.digits
        if var_symbols.get():
            chars += string.punctuation

        if avoid_similar.get():
            chars = ''.join(c for c in chars if c not in similar)

        if not chars:
            result_var.set("Select options!")
            return

        password = ''.join(random.choice(chars) for _ in range(length))
        result_var.set(password)

        update_strength(password)

    except:
        result_var.set("Invalid input!")

# --- Strength meter UI ---
def update_strength(password):
    score = calculate_strength(password)

    levels = ["Very Weak", "Weak", "Okay", "Strong", "Very Strong"]
    progress.set(score / 5)

    if score == 0:
        strength_label.configure(text="Very Weak")
    else:
        strength_label.configure(text=levels[score - 1])

# --- Copy ---
def copy_password():
    root.clipboard_clear()
    root.clipboard_append(result_var.get())

# --- UI ---
root = ctk.CTk()
root.title("Python Password")
root.geometry("400x500")

title = ctk.CTkLabel(root, text="Python Password", font=("Arial", 20))
title.pack(pady=10)

length_entry = ctk.CTkEntry(root, placeholder_text="Password Length")
length_entry.pack(pady=10)

var_upper = ctk.BooleanVar(value=True)
var_lower = ctk.BooleanVar(value=True)
var_digits = ctk.BooleanVar(value=True)
var_symbols = ctk.BooleanVar(value=False)
avoid_similar = ctk.BooleanVar(value=True)

ctk.CTkCheckBox(root, text="Uppercase", variable=var_upper).pack(anchor="w", padx=40)
ctk.CTkCheckBox(root, text="Lowercase", variable=var_lower).pack(anchor="w", padx=40)
ctk.CTkCheckBox(root, text="Digits", variable=var_digits).pack(anchor="w", padx=40)
ctk.CTkCheckBox(root, text="Symbols", variable=var_symbols).pack(anchor="w", padx=40)
ctk.CTkCheckBox(root, text="Avoid similar (O,0,l,1)", variable=avoid_similar).pack(anchor="w", padx=40)

generate_btn = ctk.CTkButton(root, text="Generate", command=generate_password)
generate_btn.pack(pady=15)

result_var = ctk.StringVar()
result_entry = ctk.CTkEntry(root, textvariable=result_var, width=300)
result_entry.pack(pady=10)

copy_btn = ctk.CTkButton(root, text="Copy", command=copy_password)
copy_btn.pack(pady=5)

# Strength meter
progress = ctk.CTkProgressBar(root, width=300)
progress.set(0)
progress.pack(pady=10)

strength_label = ctk.CTkLabel(root, text="Strength")
strength_label.pack()

root.mainloop()