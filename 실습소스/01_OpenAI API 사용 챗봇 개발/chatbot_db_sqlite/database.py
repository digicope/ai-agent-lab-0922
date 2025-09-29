import sqlite3

# DB 초기화 함수
def init_db():
    conn = sqlite3.connect('sample.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS conversations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            question TEXT,
            answer TEXT
        )
    ''')
    
    conn.commit() 
    conn.close()  

# DB 저장 함수
def save_conversation(question,answer):
    conn = sqlite3.connect('sample.db')
    c = conn.cursor()
    c.execute('''
        INSERT INTO conversations (question,answer) VALUES (?,?)
    ''',(question,answer))
    
    conn.commit() 
    conn.close()  

# DB 조회 함수
def get_conversations():
    conn = sqlite3.connect('sample.db')
    c = conn.cursor()
    c.execute("SELECT * FROM conversations")
    conversations = c.fetchall()
    conn.close()   
    return conversations

if __name__ == "__main__":
    init_db()

    question = '하늘은 왜 노란가요?'
    answer = '하늘이 노란 경우는 해가 질 무렵에 보이는 경우입니다'
    save_conversation(question,answer)

    conversations = get_conversations()
    print(conversations)
