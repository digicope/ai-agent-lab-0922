from pymongo import MongoClient

# MongoDB에 연결 (localhost:27017이 기본 설정)
client = MongoClient('localhost',27017)

db = client['chatbot']
conversation_collection = db['converstion']

# DB 초기화
def init_db():
    pass

# DB 저장 함수
def save_conversation(question,answer):
    conversation = {
        'question' : question,
        'answer' : answer
    }
    conversation_collection.insert_one(conversation)

# DB 조회 함수
def get_conversations():
    conversations = conversation_collection.find({})
    return list(conversations)

# DB 연결 종료
def close_connection():
    client.close()
