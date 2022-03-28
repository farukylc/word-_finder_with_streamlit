import pandas as pd
import streamlit as st 
from PIL import Image
import random
from itertools import permutations
from word_list import turkish_words


image = Image.open('logo.png')


st.image(image, use_column_width=True)


st.write("""
Kelime Bulucu


Bu uygulama kullanıcı tarafından verilen harfler ile yazılabilecek Türkçe kelimeleri bulur!
***""")


st.header('Harfleri Buraya Gir')


sequence_input = ""


sequence_input = st.text_area("Harfler", sequence_input, height=10, max_chars=8)


st.button("Bul", sequence_input)


letter_list = []
founded = []
sorted_list = []
letter_list_seperated = []


for elements in sequence_input:
    letter_list.append(sequence_input)

    for letters in letter_list[0]:
        letter_list_seperated.append(letters)
    break


df_letter_list_seperated = pd.DataFrame(letter_list_seperated)
df_letter_list_seperated.rename(columns = {int(0) : 'Girilen Harfler: '}, inplace = True)


if df_letter_list_seperated.empty is False:
    st.header('Girilen Harfler: ')
    df_letter_list_seperated

count = len(letter_list_seperated)


while 3 <= count:

    for perm in permutations(letter_list_seperated, count):
        x = ("".join(perm))
        for all in x:
            founded.append(x)
    count = count - 1
        


sorted_list = sorted((set(founded).intersection(turkish_words)), key =len)


three_list = []
four_list = []
five_list = []
six_list = []
seven_list = []
eight_list = []





for elements in sorted_list:
        
    if len(elements) == 3:
            three_list.append(elements)
            
            three_df = pd.DataFrame(three_list)
            three_df.rename(columns = {int(0) : '3 Harfli'}, inplace = True)
        
    
    elif len(elements) == 4:
            four_list.append(elements)
            four_df = pd.DataFrame(four_list)
            four_df.rename(columns = {int(0) : '4 Harfli'}, inplace = True)
        
    
    elif len(elements) == 5:
            five_list.append(elements)
            five_df = pd.DataFrame(five_list)
            five_df.rename(columns = {int(0) : '5 Harfli'}, inplace = True)
        
    
    elif len(elements) == 6:
            six_list.append(elements)
            six_df = pd.DataFrame(six_list)
            six_df.rename(columns = {int(0) : '6 Harfli'}, inplace = True)
        
    
    elif len(elements) == 7:
            seven_list.append(elements)
            seven_df = pd.DataFrame(seven_list)
            seven_df.rename(columns = {int(0) : '7 Harfli'}, inplace = True)
        
    
    elif len(elements) >= 8:
            eight_list.append(elements)
            eight_df = pd.DataFrame(eight_list)
            eight_df.rename(columns = {int(0) : '8 Harfli'}, inplace = True)
    
try:
    if df_letter_list_seperated.empty is False:
        st.header('Yazılabilecek Kelimeler: ')
        
        three_df
        four_df
        five_df
        six_df
        seven_df
        eight_df
        

except NameError:  
    pass

        




    
    
    
    

    
    
    

    
    




