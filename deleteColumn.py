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
all_user_ids = db.collection("Attraction").stream()
ID=[]
for doc in all_user_ids:
    ID.append(doc.id)
    
print(ID)

#刪掉一個colname 用 '指定要刪掉的col':firestore.DELETE_FIELD
for key in ID:
  path = "Attraction/"+key
  doc_ref = db.document(path)
  doc = {
      'Similar': firestore.DELETE_FIELD
  }
  doc_ref.update(doc)