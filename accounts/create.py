from datetime import datetime
from pymongo import MongoClient
import re

# 連接到 MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['user_database']
collection = db['users']

def create_user(name, department, student_id, email, password):
    """將新用戶資料存入資料庫"""
    user_data = {
        'name': name,
        'department': department,
        'student_id': student_id,
        'email': email,
        'password': password,  # 不加密密碼
        'created_at': datetime.now()
    }
    result = collection.insert_one(user_data)
    return result.inserted_id

def validate_student_id(student_id):
    """檢查學號是否為9位數字"""
    return bool(re.match(r'^\d{9}$', student_id))

def validate_email(email):
    """檢查 Email 格式是否正確"""
    return bool(re.match(r'^[a-zA-Z0-9._%+-]+@m365\.fju\.edu\.tw$', email))

def input_user_data():
    """處理用戶輸入，驗證資料並存入資料庫"""
    name = input('請輸入姓名: ').strip()
    department = input('請輸入系及: ').strip()

    # 驗證學號
    student_id = input_with_validation('請輸入學號 : ', validate_student_id, "學號格式不正確，請重新輸入。")
    
    # 驗證Email
    email = input_with_validation('請輸入Email (@m365.fju.edu.tw): ', validate_email, "Email格式不正確，請重新輸入。")
    
    # 讓使用者輸入密碼
    password = input('請建立登入密碼: ').strip()
    
    # 將資料存入資料庫
    new_user_id = create_user(name, department, student_id, email, password)
    print(f'新使用者已建立，ID: {new_user_id}')

def input_with_validation(prompt, validation_func, error_message):
    """通用輸入和驗證函式"""
    while True:
        user_input = input(prompt).strip()
        if validation_func(user_input):
            return user_input
        else:
            print(error_message)

# 開始輸入使用者資料
if __name__ == '__main__':
    input_user_data()
