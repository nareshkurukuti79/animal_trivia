import json 

def load_db():
    with open("questions.json") as file:
        return json.load(file)
    
db = load_db()

def save_db():
    with open('questions.json','w') as file:
        return json.dump(db, file)