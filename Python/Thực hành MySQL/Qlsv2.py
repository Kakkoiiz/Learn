import mysql.connector
import pandas as pd
import datetime

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



# # Xóa toàn bộ môn có mã bộ môn là 05

# sql = '''DELETE from bo_mon WHERE ma_bo_mon = 05'''
# cursor.execute(sql)
# mydb.commit()



# create the sinh_vien table if it doesn't exist



cursor.execute('''CREATE TABLE IF NOT EXISTS sinh_vien (
    ma_sinh_vien BIGINT PRIMARY KEY,
    ho_ten VARCHAR(255),
    ngay_sinh DATE,
    gioi_tinh VARCHAR(10),
    so_dien_thoai BIGINT,
    que_quan VARCHAR(255),
    ma_bo_mon INT,
    FOREIGN KEY (ma_bo_mon) REFERENCES bo_mon(ma_bo_mon)
)''')

# read the csv file into a dataframe
df = pd.read_csv('Python\Thực hành MySQL\sinh_vien.csv')

# insert each row into the database
for index, row in df.iterrows():
    ma_sinh_vien = int(row[0])
    ho_ten = row[1] +" " + row[2]
    ngay_sinh = row[3]
    gioi_tinh = row[4]
    so_dien_thoai = int(row[5])
    que_quan = row[6]
    ma_bo_mon = int(row[7])
    
    sql = '''INSERT INTO sinh_vien (ma_sinh_vien, ho_ten, ngay_sinh, gioi_tinh, so_dien_thoai, que_quan, ma_bo_mon) 
             VALUES (%s, %s, %s, %s, %s, %s, %s)'''
    val = (ma_sinh_vien, ho_ten, ngay_sinh, gioi_tinh, so_dien_thoai, que_quan, ma_bo_mon)
    cursor.execute(sql, val)

# commit the changes
mydb.commit()


# Thêm thông tin vào bảng sv

sql = '''INSERT INTO sinh_vien (ma_sinh_vien, ho_ten, ngay_sinh, gioi_tinh, so_dien_thoai, que_quan, ma_bo_mon)
         VALUES (%s, %s, %s, %s, %s, %s, %s)'''
val = (2121050556, "Nguyễn Mạnh Dũng", "2003-10-30", "Nam", 84326680326, "Thanh hóa", 1 )
cursor.execute(sql,val)
mydb.commit()

# in ra số lượng sinh viên khoa công nghệ thông tin
sql = '''SELECT COUNT(*) FROM sinh_vien sv
         JOIN bo_mon bm ON sv.ma_bo_mon = bm.ma_bo_mon
         JOIN khoa k ON bm.ma_khoa = k.ma_khoa
         WHERE k.ten_khoa = 'Công nghệ thông tin' '''
cursor.execute(sql)
result = cursor.fetchone()

print(f'Số lượng sinh viên khoa công nghệ thông tin: {result[0]}')
         

# In ra màn hình số lượng sinh viên có tuổi lớn hơn 20
# Tính năm hiện tại
now = datetime.datetime.now()
year_now = now.year

# Lấy dữ liệu từ bảng sinh_vien
sql = '''SELECT * FROM sinh_vien'''
cursor.execute(sql)
result = cursor.fetchall()

count = 0
for row in result:
  year = row[2].year
  age = year_now - year
  if age > 20:
    count += 1
print(f'Số lượng sinh viên có tuổi lớn hơn 20: {count}')

# in ra màn hính sinh viên có quê quán hà nội

sql = '''SELECT COUNT(*) FROM sinh_vien 
         WHERE que_quan LIKE "%Hà nội%" '''
cursor.execute(sql)
result = cursor.fetchone()
print(f'Số lượng sinh viên ở hà nội: {result[0]}')

# In ra màn hình danh sách sinh viên thuộc bộ môn Công nghệ thông tin địa học

sql = ''' SELECT COUNT(*) FROM sinh_vien sv
        JOIN bo_mon bm ON sv.ma_bo_mon = bm.ma_bo_mon
        WHERE bm.ten_bo_mon = 'Công nghệ thông tin địa học' '''
cursor.execute(sql)
result = cursor.fetchall()

print("Số lượng sinh viên thuộc bộ môn Công nghệ thông tin địa học là:", result[0][0])


# In ra màn hình danh sách sinh viên thuộc bộ môn Công nghệ thông tin địa học, bao gồm mã sinh viên, họ tên, ngày sinh, giới tính, số điện thoại, quê quán, tên bộ môn
sql = ''' SElECT sv.ma_sinh_vien, sv.ho_ten, sv.ngay_sinh, sv.gioi_tinh, sv.so_dien_thoai, sv.que_quan, bm.ten_bo_mon
          FROM sinh_vien sv
          JOIN bo_mon bm ON sv.ma_bo_mon = bm.ma_bo_mon
          WHERE bm.ten_bo_mon = 'Công nghệ thông tin địa học' '''
cursor.execute(sql)
result = cursor.fetchall()

for row in result:
  ma_sinh_vien = row[0]
  ho_ten = row[1]
  ngay_sinh = row[2]
  gioi_tinh = row[3]
  so_dien_thoai = row[4]
  que_quan = row[5]
  ten_bo_mon = row[6]
  print("Họ và tên : ",ho_ten)
  print("Mã sinh viên: ",ma_sinh_vien)
  print("Ngày sinh: ",ngay_sinh)
  print("Giới tính: ",gioi_tinh)
  print("Số điện thoại: ",so_dien_thoai)
  print("Quê quán: ",que_quan)
  print("Tên bộ môn: ",ten_bo_mon)
  print("====================")
  
# In ra màn hính thông tin sinh viên  1904007638
sql = '''SELECT * FROM sinh_vien WHERE ma_sinh_vien = '1904007638' '''
cursor.execute(sql)
result = cursor.fetchall()
print(result)
print("====================")


# cách 2

sql = ''' SElECT sv.ma_sinh_vien, sv.ho_ten, sv.ngay_sinh, sv.gioi_tinh, sv.so_dien_thoai, sv.que_quan, bm.ten_bo_mon
          FROM sinh_vien sv
          JOIN bo_mon bm ON sv.ma_bo_mon = bm.ma_bo_mon
          WHERE sv.ma_sinh_vien = '1904007638' '''
cursor.execute(sql)
result = cursor.fetchone()

if result:
  ma_sinh_vien = result[0]
  ho_ten = result[1]
  ngay_sinh = result[2]
  gioi_tinh = result[3]
  so_dien_thoai = result[4]
  que_quan = result[5]
  ten_bo_mon = result[6]
  print("Thông tin của sinh viên có mã sinh viên là 1904007638 ")
  print("Họ và tên : ",ho_ten)
  print("Mã sinh viên: ",ma_sinh_vien)
  print("Ngày sinh: ",ngay_sinh)
  print("Giới tính: ",gioi_tinh)
  print("Số điện thoại: ",so_dien_thoai)
  print("Quê quán: ",que_quan)
  print("Tên bộ môn: ",ten_bo_mon)
else:
  print("adu bro ")


#  Cập nhật bộ môn của sinh viên có mã sinh viên là 2183070252 thành Trắc địa cao cấp

sql = ''' UPDATE sinh_vien
          SET ma_bo_mon = (SELECT ma_bo_mon FROM bo_mon WHERE ten_bo_mon = 'Trắc địa cao cấp')
          WHERE ma_sinh_vien = '2183070252' '''
cursor.execute(sql)

# xóa thông tin của idol

# sql = ''' DELETE from sinh_vien WHERE ma_sinh_vien = '2121050556' '''
# cursor.execute(sql)


