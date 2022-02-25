"""
เขียนโปรแกรม login โดยรับ Input จากผู็ใช้
คือ username และ password หากผู้ใช้กรอกข้อความ
ถูกต้องให้แสดงข้อความ "Welcome {name}"
แต่ถ้าไม่ถูกต้อง ให้ผู้ใช้กรอกข้อมูลใหม่
หากกรอกข้อมูลผิดครบ 3 ครั้ง ให้แสดงข้ความ
"Your account has been locked, please contact admin."

"""
user = 'admin'
passwod = '1234'

count = 0
while count < 3:
    u = input('enter username: ')
    p = input('enter password: ')
    if u == user and p == passwod:
        print(f'Hello, {u}')
        break
    else:
        print(f'username or password is not correct. {count+1}')
        if count < 2:
            print(f'please, login again.')
        count+=1
else:
    print('your account has been locked, '
          'please contact admin')
