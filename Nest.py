# 引用必要套件
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# 引用私密金鑰
# path/to/serviceAccount.json 請用自己存放的路徑
cred = credentials.Certificate('FirebaseAdminSDK.json')

# 初始化firebase，注意不能重複初始化
firebase_admin.initialize_app(cred)

# 初始化firestore
db = firestore.client()


#拿出所有ID放到list裡面
#拿出所有AttractionName放到list裡面
all_user_ids = db.collection("Attraction").stream()
ID=[]
AttractionName=[]   
for doc in all_user_ids:
    ID.append(doc.id)
    AttractionName.append(doc.to_dict()['AttractionName'])
  
print(ID)
print(AttractionName)

import pandas as pd
#df = pd.DataFrame(ID, columns = "ID")
dict = {"ID": ID,  
        "AttractionName": AttractionName
       }
select_df = pd.DataFrame(dict)

print(select_df)            
select_df.to_csv('C:/Users/Jacky/Downloads/NameID.csv')


for key in ID:
  path = "Attraction/"+key
  doc_ref = db.document(path)
  doc = doc_ref.get(AttractionName)
  AttractionName.append(doc)
#for business in Inventory.each():
 # print(str(business))
import random  
for key in ID:
  path = "Attraction/"+key
  doc_ref = db.document(path)
  #print(path)
  
  dic = {}
  for key in ID:
      #calculate x
      dic['\''+key+'\''] = random.randint(0,100)
  #print(dic)
     
  doc = {
      'Similar': dic
  }  
  doc_ref.update(doc)