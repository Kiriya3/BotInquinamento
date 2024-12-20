import random
import os

def random_tip():
    txt_name = random.choice(os.listdir('File_txt'))
    with open(f"File_txt/{txt_name}", "r", encoding="utf-8") as file:
                    text_template = file.read()
    return text_template