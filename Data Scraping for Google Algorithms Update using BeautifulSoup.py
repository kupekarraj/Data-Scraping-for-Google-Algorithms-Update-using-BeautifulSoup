#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#importing all the required libraries
from bs4 import BeautifulSoup
import requests
import pandas as pd
from IPython.display import display_html 


# In[ ]:


#creating a data frame to append the output results
algorithm_update=pd.DataFrame(columns=["Update Date","Update Name"])


# In[ ]:


#initializing the Beautiful Soup library
html_text=requests.get("https://www.searchenginejournal.com/google-algorithm-history/").text
soup=BeautifulSoup(html_text,'lxml')


# In[ ]:


#pulling the update date and name information
date=soup.find_all('h3',class_="panda-coltitle green")
name = soup.find_all('h4',class_="panda-sub")


# In[ ]:


for i in range(len(date)):
    update_date=date[i].text
    update_name=name[i].text
    #saving the data
    algorithm_update=algorithm_update.append({"Update Date":update_date,"Update Name":update_name},ignore_index=True)


# In[ ]:


#printing the top rows of the output
print(algorithm_update)


# In[ ]:


display_html(algorithm_update) 
#AIzaSyBBwq0VNlY3it2mAMv7AT3N5Iusd2T3pbQ

