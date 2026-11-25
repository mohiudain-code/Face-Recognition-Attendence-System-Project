import firebase_admin
from firebase_admin import credentials


from firebase_admin import db

cred = credentials.Certificate("venu/serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    "databaseURL":'https://faceattendencerealtime-f2ac9-default-rtdb.firebaseio.com/'
})


ref=db.reference('Students')
data={
    '1':{
        'name':'Ghulam mohi u dain',
        'major':'AI Engineer',
        'Starting_year':2024,
        'total_attendence':0,
        'standing':'Good',
        'year':2,
        'Last_attendence_time':'2022-12-11 00:54:34'
    },
    '2':{
        'name':'Muhammad Azeem Iqbal',
        'major':'Python Developer',
        'Starting_year':2024,
        'total_attendence':0,
        'standing':'Better',
        'year':2,
        'Last_attendence_time':'2022-12-11 12:54:34'
    },
    '3':{
        'name':'Muhammad Usman Yasin',
        'major':'ML Engineer',
        'Starting_year':2024,
        'total_attendence':0,
        'standing':'Better',
        'year':2,
        'Last_attendence_time':'2022-12-11 12:54:34'
    }
}

for key,value in data.items():
    ref.child(key).set(value)