from bs4 import BeautifulSoup
import requests
import os
import discord
from subprocess import run
from keep_alive import keep_alive

my_secret = os.environ['TOKENN']


client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))




@client.event
async def on_message(message):
    if message.author == client.user:
        return



    #PUBLIC SEARCH
    if message.content.startswith('$intern'):
        

        print("REQUEST:", message.content,'> requested by {}'.format(message.author.name))
        if len(message.content.strip().split()) >= 2:
            await message.reply('you it is gonna take 30 to 40 seconds')
            users = message.content.strip().split()[1:]
            user = str(' '.join(users))
            
            await message.reply('Searching for {}...'.format(user))

            with open('{}.txt'.format(user) ,"w") as file:
              # ("Now the file has more content!")
              intrest = user

              url = "https://internshala.com/internships/keywords-{}".format(intrest)
              # print(url)

              html = requests.get(url).text

              soup = BeautifulSoup(html , "lxml")
              tag = soup.find_all("span" , {"id": "total_pages"})
              loop = int(tag[0].text)
                
                
                ### THIS PART IS UNDER CONSTRUCTION I AM MAKING IN MORE EFFICIENT SOME PART OF CODE IS DELETED

#               try:
#                 for i in range(1 , loop+1):
#                     url = "https://internshala.com/internships/keywords-{}".format(i)
#                     # print(url)
#                     html = requests.get(url).text

#                     tag = soup.find_all("div" , class_ = "individual_internship")

#                     for i in tag:
#                         
#                         file.write("internship offer on  ==>{}\n ".format(cont.text))
#                         file.write("link of intership : {}\n".format("https://internshala.com{}".format(cont.get('href'))))
                        
#                         file.write("start of intern : {}\n".format(conten[0].text.replace(" ","").strip()))
#                         file.write("duration of intern : {}\n" .format(conten[1].text.strip()))
#                         file.write("salery of intern : {}\n".format(conten[2].text.strip()))
#                         file.write("apply to intern by : {}\n".format(conten[3].text.strip()))
#                         file.write("\n")
#                         file.write("\n")
#                         file.write("\n")
              except:
                await message.reply('your entered quiery might be wrong please try again or contact JAYENDRA')


                      
                          

              







            

        
            await message.reply("Generated .txt file of TARGET {} ".format(user), file=discord.File('{}.txt'.format(user)))
            os.remove('{}.txt'.format(user))
                
            
            await message.reply('Successfully processed your request!')
            
            print(users, ' <-- Successful PUBLIC SEARCH!! requested by {} '.format(message.author.name))
        else:
            await message.reply('Check usage guide...')
        #PRIVATE SEARCH
    


keep_alive()
client.run(my_secret)








# intrest = user

# url = "https://internshala.com/internships/keywords-{}".format(intrest)
# # print(url)

# html = requests.get(url).text

# soup = BeautifulSoup(html , "lxml")
# tag = soup.find_all("span" , {"id": "total_pages"})
# loop = int(tag[0].text)

# try:
#     for i in range(1 , loop+1):
#         url = "https://internshala.com/internships/keywords-{}".format(i)
#         # print(url)
#         html = requests.get(url).text
#         soup = BeautifulSoup(html , "lxml")

#         tag = soup.find_all("div" , class_ = "individual_internship")

#         for i in tag:
#             cont = i.a
#             conte = i.find("span" , class_="stipend")
#             conten = i.find_all("div" , class_="item_body")
#             # print(conte)
#             print("internship offer on  " , '==> ',cont.text)
#             print("link of intership : ", "https://internshala.com{}".format(cont.get('href')))
            
#             print("start of intern :" , conten[0].text.replace(" ","").strip())
#             print("duration of intern :" , conten[1].text.strip())
#             print("salery of intern :" , conten[2].text.strip())
#             print("apply to intern by :" , conten[3].text.strip())
#             print()
#             print()
#             input()

            
            

# except:
#     print("i guess your query has mistakes re-enter or contact JAYENDRA discord id jayendra#2616")

