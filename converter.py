import pandas as pd
from bs4 import BeautifulSoup
from tqdm import tqdm

file_to_convert = input("Which file would you like to convert? ")

html = open(file_to_convert, encoding="utf8")
soup = BeautifulSoup(html, 'html.parser')
list_of_messages_from_soup = soup.find_all("div", class_="pam _3-95 _2ph- _a6-g uiBoxWhite noborder")
list_of_messages_from_soup = list(list_of_messages_from_soup)

sender_list = []
datetime_list = []
liked_list = []
texts = []
attachments = []

for i in tqdm(range(len(list_of_messages_from_soup))):
    # attachments
    image_loc_string = ""
    try:
        if len(((list_of_messages_from_soup[i].find_all("div", class_="_3-95 _a6-p")[0]).find_all("img", class_="_a6_o _3-96"))) != 0: # if image attachments are not 0
            for x in range(len(((list_of_messages_from_soup[i].find_all("div", class_="_3-95 _a6-p")[0]).find_all("img", class_="_a6_o _3-96")))): # for every image attachment
                image_loc_string = image_loc_string + str((((list_of_messages_from_soup[i].find_all("div", class_="_3-95 _a6-p")[0]).find_all("img", class_="_a6_o _3-96")[x]["src"]) + ", ")) # append the image location to a string
            attachments.append(image_loc_string[:-1]) # append that string to the list of attachments
        else:
            attachments.append("")
    except AttributeError:
        if len(((list_of_messages_from_soup[i].find_all("div", class_="_3-95 _a6-p")[0]).find_all("img", class_="_a6_o _3-96"))) != 0: # if image attachments are not 0
            for x in range(len(((list_of_messages_from_soup[i].find_all("div", class_="_3-95 _a6-p")[0]).find_all("img", class_="_a6_o _3-96")))): # for every image attachment
                image_loc_string = image_loc_string + str((((list_of_messages_from_soup[i].find_all("div", class_="_3-95 _a6-p")[0]).find_all("img", class_="_a6_o _3-96")[x]["src"]) + ", ")) # append the image location to a string
            attachments.append(image_loc_string[:-1]) # append that string to the list of attachments
        else:
            attachments.append("")
        pass  
    
     # likes
    try:
        liked_list.append((list_of_messages_from_soup[i].find_all("div", class_="_3-95 _a6-p")[0]).find("ul", class_="_a6-q").get_text())
    except AttributeError:
        liked_list.append("")
        
    # datetime
    datetime_list.append(list_of_messages_from_soup[i].find("div", class_="_3-94 _a6-o").get_text())
    
    # senders
    sender_list.append(list_of_messages_from_soup[i].find_all("div", class_="_3-95 _2pim _a6-h _a6-i")[0].get_text()) 
    
# messages    
for i in tqdm(range(len(list_of_messages_from_soup))):
    try:
        decomposed_message = (list_of_messages_from_soup[i].find_all("div", class_="_3-95 _a6-p")[0]).find("ul", class_="_a6-q").decompose()
        texts.append(decomposed_message.get_text())
    except AttributeError:
        texts.append((list_of_messages_from_soup[i].find_all("div", class_="_3-95 _a6-p")[0]).get_text())
        pass

datetime_list = pd.to_datetime(datetime_list)
datetime_list = list(datetime_list)    
    
final_dict = {
    "Datetime" : datetime_list,
    "From" : sender_list,
    "Text" : texts,
    "Attachments" : attachments,
    "Liked By" : liked_list
}

df = pd.DataFrame(final_dict)
df.to_csv(file_to_convert[:-5]+".csv", index=False)
print("File Converted!")