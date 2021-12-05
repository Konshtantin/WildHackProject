import requests
import json
import time
import sys
def vkParser(token):
  keyWords=["морск", "лосос", "икра", "краб", "минтай", "рыбопромышленни", "волонтер", "опасн", "Командорск", "Корякс", "Охотск", "штраф", "незаконн", "учёны","экосистем","природ", "Камчатк", "Камчатск", "животн", "браконьер", "эколог", "мусор", "загрязнен", "угрожа", "угроз", "ущерб", "защит", "заповедник", "заказник", "млекопитающ", "медвед", "олен", "лис", "океан", "побереж", "река", "озер", "лес", "Кроноцкий", "Курильск", "пожар"]
  def json2arr(jsonObj):
        return json.loads(jsonObj.content)
  def getArrPhotos(currentPost):
        try:
          arrAttachments=currentPost["attachments"]
        except AttributeError:
              arrAttachments=[]
        for item in arrAttachments:       
             arrPhotos=[]
             if item["type"]=="photo":
                  arrPhotos.append(item["photo"]["sizes"][3]["url"])
        return arrPhotos
  def isImportant(currentPost):
      text=currentPost["text"]           
      for word in keyWords:
          if word in text:
             head=text.split('\n')[0]
             arrPhotos=getArrPhotos(currentPost)    
             date=currentPost["date"]
             link="https://vk.com/wall"+str(currentPost["owner_id"])+"_"+str(currentPost["id"])+""
             post={}
             post["head"]=head
             post["date"]=date
             post["text"]=text
             post["img"]=arrPhotos
             post["link"]=link
             return post
           
           
           
  arrResult=[]         
  #token="b79f9a0ace5405c3819075b0a5e1a2592c2e9fd219bede6a3a3717e5954a94c629eec67a9dd10e86fb413"
  groupid=-49796420
  offset=0
  v=5.126
  importantNews=[]
  URL="https://api.vk.com/method/wall.get?owner_id="+str(groupid)+"&offset="+str(offset)+"&count=1&access_token="+token+"&v=5.126"
  posts=json2arr(requests.get(URL))



  URL="https://api.vk.com/method/wall.get?owner_id="+str(groupid)+"&offset="+str(offset)+"&count=2&access_token="+token+"&v=5.126"
  posts=json2arr(requests.get(URL))

  newsCount=posts["response"]["count"]

  while offset<newsCount:
     URL="https://api.vk.com/method/wall.get?owner_id="+str(groupid)+"&offset="+str(offset)+"&count=100&access_token="+token+"&v=5.126"
     posts=json2arr(requests.get(URL))["response"]["items"]
   
     for item in posts:
           try:
              arrResult.append(isImportant(item))
           except AttributeError:
                pass 
     offset+=100
  return arrResult

def getNewNews(lastDate,token):
  keyWords=["морск", "лосос", "икра", "краб", "минтай", "рыбопромышленни", "волонтер", "опасн", "Командорск", "Корякс", "Охотск", "штраф", "незаконн", "учёны","экосистем","природ", "Камчатк", "Камчатск", "животн", "браконьер", "эколог", "мусор", "загрязнен", "угрожа", "угроз", "ущерб", "защит", "заповедник", "заказник", "млекопитающ", "медвед", "олен", "лис", "океан", "побереж", "река", "озер", "лес", "Кроноцкий", "Курильск", "пожар"]
  def json2arr(jsonObj):
      return json.loads(jsonObj.content)
  def getArrPhotos(currentPost):
        try:
          arrAttachments=currentPost["attachments"]
        except AttributeError:
              arrAttachments=[]
        for item in arrAttachments:       
             arrPhotos=[]
             if item["type"]=="photo":
                  arrPhotos.append(item["photo"]["sizes"][3]["url"])
        return arrPhotos
  def isImportant(currentPost):
      text=currentPost["text"]           
      for word in keyWords:
          if word in text:
             head=text.split('\n')[0]
             arrPhotos=getArrPhotos(currentPost)    
             date=currentPost["date"]
             link="https://vk.com/wall"+str(currentPost["owner_id"])+"_"+str(currentPost["id"])+""
             post={}
             post["title"]=head
             post["date"]=date
             post["text"]=text
             post["imgUrls"]=arrPhotos
             post["url"]=link
          
             return post
           
           
           
  arrResult=[]         
  #token="b79f9a0ace5405c3819075b0a5e1a2592c2e9fd219bede6a3a3717e5954a94c629eec67a9dd10e86fb413"
  groupid=-49796420
  offset=1
  v=5.126
  importantNews=[]
  URL="https://api.vk.com/method/wall.get?owner_id="+str(groupid)+"&offset="+str(offset)+"&count=1&access_token="+token+"&v=5.126"
  posts=json2arr(requests.get(URL))



  URL="https://api.vk.com/method/wall.get?owner_id="+str(groupid)+"&offset="+str(offset)+"&count=1&access_token="+token+"&v=5.126"
  posts=json2arr(requests.get(URL))

  date=posts["response"]["items"][0]["date"]





  
  while date>lastDate:
     
     URL="https://api.vk.com/method/wall.get?owner_id="+str(groupid)+"&offset="+str(offset)+"&count=1&access_token="+token+"&v=5.126"
     posts=json2arr(requests.get(URL))["response"]["items"]
   
     for item in posts:
        
           try:
            
              arrResult.append(isImportant(item))
           except AttributeError:
                pass
           date=item["date"]
           
      
     offset+=10
  return arrResult
print(getNewNews(1637977210))

print(vkParser())

        
        
    
    


