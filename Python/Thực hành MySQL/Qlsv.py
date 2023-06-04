import mysql.connector

# kết nối
mysql_sever = mysql.connector.connect(
  host = 'localhost',
  user = 'root',
  password = '123456'
)

cursor = mysql_sever.cursor()

cursor.execute('CREATE DATABASE qlsv')

# kết nối đên csdl 

mydb = mysql.connector.connect(
  host = 'localhost',
  user = 'root',
  password = '123456',
  database = 'qlsv'
)

# Tạo đối tượng cursor 

cursor = mydb.cursor()

# Tạo bảng khoa
sql = '''CREATE TABLE khoa (
  ma_khoa INT PRIMARY KEY,
  ten_khoa VARCHAR(255)
)'''

cursor.execute(sql)

# Tạo bảng bo_mon
sql = '''CREATE TABLE bo_mon (
  ma_bo_mon INT PRIMARY KEY,
  ten_bo_mon VARCHAR(255),
  ma_khoa INT,
  FOREIGN KEY (ma_khoa) REFERENCES khoa(ma_khoa)
)'''

cursor.execute(sql)


# Chèn dữ liệu vào bảng khoa
sql = '''INSERT INTO khoa (ma_khoa, ten_khoa) VALUES
    (01, "Công nghệ thông tin"),
    (02, "Trắc địa - Bản đồ và Quản lý đất đai")
'''

cursor.execute(sql)

mydb.commit()


# Chèn dữ liệu vào bảng bo mon

sql = '''INSERT INTO bo_mon (ma_bo_mon, ten_bo_mon, ma_khoa ) VALUES
    (01, "Công nghệ thông tin địa học", 01),
    (02, "Hệ thống thông tin và tri thức", 01),
    (03, "Trắc địa công trình", 02),
    (04, "Địa chính", 02),
    (05, "Bản đồ", 02)
'''

cursor.execute(sql)

mydb.commit()


# Lấy và in ra dữ liệu trong khoa

sql = '''SELECT * FROM khoa'''
cursor.execute(sql)
result = cursor.fetchall()

print('Danh sách khoa hiện có trong csdl: ')
for row in result:
  print(f'Mã khoa: {row[0]}, tên khoa: {row[1]}')

# lấy và in ra dữ liệu trong bo mon

sql = '''SELECT * FROM bo_mon WHERE ma_khoa = 01'''
cursor.execute(sql)
result = cursor.fetchall()

print('Danh sách bộ môn thuộc khoa công nghệ thong tin:')

for row in result:
  print(f'Mã bộ môn: {row[0]}, tên bộ môn: {row[1]}')        
  
  
# Cập nhật tên bô môn cho bản ghi

sql = '''UPDATE bo_mon
    SET ten_bo_mon = "Trắc địa cao cấp"
    WHERE ma_bo_mon = 03
'''

cursor.execute(sql)
mydb.commit()

# Xóa toàn bộ môn có mã bộ môn là 05

sql = '''DELETE from bo_mon WHERE ma_bo_mon = 05'''
cursor.execute(sql)
mydb.commit()