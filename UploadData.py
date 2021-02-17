import csv
import firebase_admin
from firebase_admin import credentials, firestore

# 引用私密金鑰
# path/to/serviceAccount.json 請用自己存放的路徑
if (not len(firebase_admin._apps)):
    cred = credentials.Certificate('FirebaseAdminSDK.json') 
    default_app = firebase_admin.initialize_app(cred)

store = firestore.client()


#存DATA用這邊
file_path = "TravelAgencySpot.csv"    
collection_name = "Attraction"    




def batch_data(iterable, n=1):
    l = len(iterable)
    for ndx in range(0, l, n):
        yield iterable[ndx:min(ndx + n, l)]


data = []
headers = []
with open(file_path) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            for header in row:
                headers.append(header)
            line_count += 1
        else:
            obj = {}
            for idx, item in enumerate(row):
                obj[headers[idx]] = item
            data.append(obj)
            line_count += 1
    print(f'Processed {line_count} lines.')

for batched_data in batch_data(data, 499):
    batch = store.batch()
    for data_item in batched_data:
        doc_ref = store.collection(collection_name).document()
        batch.set(doc_ref, data_item)
    batch.commit()

print('Done')



