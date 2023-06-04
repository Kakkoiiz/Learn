import mysql.connector

# Kết nối đến mySQL

# mysql_sever = mysql.connector.connect(
#     host = 'localhost',
#     user = 'root',
#     password = '123456'
# )

# cursor = mysql_sever.cursor()
# cursor.execute('CREATE DATABASE qlhh')

# Kết nối đến csdl

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '123456',
    database = 'qlhh'
)

# Tạo đối tượng cursor

cursor = mydb.cursor()


# # Tạo bảng hàng hóa
# sql = '''CREATE TABLE HANGHOA (
#     MaHH INT PRIMARY KEY,
#     TenHH VARCHAR(255),
#     GiaBan BIGINT,
#     SoLuongTonKho INT,
#     SoLuongDaBan INT
# )'''

# cursor.execute(sql)

# Tạo bảng Chi tiết hóa đơn

# sql = ''' CREATE TABLE CHITIETHOADON (
#     MaHD INT,
#     MaHH INT PRIMARY KEY,
#     TenHH VARCHAR(255),
#     SoLuongDaBan INT,
#     GiaBan BIGINT
# )'''

# cursor.execute(sql)

# # Tạo bảng hóa đơn

# sql = ''' CREATE TABLE HOADON (
#     MaHD INT PRIMARY KEY,
#     NgayBan DATE,
#     TongGiaTri BIGINT
# )'''

# cursor.execute(sql)



# Thêm mặt hàng vào bảng hàng hóa

def them_hang_hoa(ma_hh, ten_hh,gia_ban, so_luong_ton_kho, so_luong_da_ban ):
    try:
        sql = '''INSERT INTO HANGHOA (MaHH, TenHH, GiaBan, SoLuongTonKho, SoLuongDaBan) 
                 SELECT %s, %s, %s, %s, %s FROM DUAL
                 WHERE NOT EXISTS (SELECT * FROM HANGHOA WHERE TenHH = %s)'''
        val = (ma_hh, ten_hh, gia_ban, so_luong_ton_kho, so_luong_da_ban, ten_hh)
        cursor.execute(sql,val)
        mydb.commit()
        if cursor.rowcount > 0:
            print(cursor.rowcount, "Mặt hàng đã thêm vào bảng HANGHOA.")
        else:
            print("Mặt hàng đã tồn tại trong bảng HANGHOA.")
    except mysql.connector.Error as error:
        print("Lỗi khi thêm hàng hóa:", format(error))
        
        
        
# Cập nhật thông tin mặt hàng

def cap_nhap_hang_hoa(ma_hh, ten_hh, gia_ban, so_luong_ton_kho, so_luong_da_ban):
    try:
        sql = "UPDATE HANGHOA SET MaHH = %s, GiaBan = %s, SoLuongTonKho = %s, SoLuongDaBan = %s WHERE TenHH = %s"
        val = (ma_hh, gia_ban, so_luong_ton_kho, so_luong_da_ban, ten_hh)
        cursor.execute(sql, val)
        mydb.commit()
        if cursor.rowcount > 0:
            print(cursor.rowcount, "Mặt hàng đã được cập nhật.")
        else:
            print("Mặt hàng không tồn tại trong bảng HANGHOA.")
    except mysql.connector.Error as error:
        print("Lỗi khi cập nhật hàng hóa:", format(error))
        

def xoa_mat_hang(ma_hh):
    try:
        sql = "DELETE FROM HANGHOA WHERE MaHH = %s"
        val = (ma_hh, )
        cursor.execute(sql,val)
        mydb.commit()
        if cursor.rowcount > 0:
            print("Mặt hàng này đã được xóa")
        else:
            print("Mặt hàng này không tồn tại")
    except mysql.connector.Error as error:
        print("Lỗi khi xóa mặt hàng: ", format(error))
        
def kiem_tra_so_luong(ten_hh):
    try:
        sql = "SELECT SoLuongTonKho FROM HANGHOA WHERE TenHH = %s"
        val = (ten_hh,)
        cursor.execute(sql, val)
        result = cursor.fetchone()
        if result:
            print("Số lượng", ten_hh, "là ", result[0])
        else:
            print("Mặt hàng không tồn  tại")
    except mysql.connector.Error as error:
        print("Lỗi kiểm tra số lượng: ",format(error))

def tim_kiem_hang_hoa(keyword):
    try:
        sql = "SELECT * FROM HANGHOA WHERE TenHH LIKE %s OR MaHH = %s"
        val = ("%" + str(keyword) + "%", keyword)
        cursor.execute(sql, val)
        result = cursor.fetchall()
        if len(result) > 0:
            print("Kết quả tìm kiếm:")
            for row in result:
                print("Mã hàng hóa: ", row[0])
                print("Tên hàng hóa: ", row[1])
                print("Giá bán: ", row[2])
                print("Số lượng tồn kho: ", row[3])
                print("Số lượng đã bán: ", row[4])
        else:
            print("Không tìm thấy mặt hàng nào.")
    except mysql.connector.Error as error:
        print("Lỗi khi tìm kiếm mặt hàng: ", format(error))


def hien_thi_danh_sach_hang_hoa():
    try:
        sql = "SELECT * FROM HANGHOA"
        cursor.execute(sql)
        result = cursor.fetchall()
        if len(result) > 0:
            print("Danh sách trong kho:")
            for row in result:
                print("Mã hàng hóa: ", row[0])
                print("Tên hàng hóa: ", row[1])
                print("Giá bán: ", row[2])
                print("Số lượng tồn kho: ", row[3])
                print("Số lượng đã bán: ", row[4])
                print("=========================")
        else:
            print("Danh sách trong kho trống")
    except mysql.connector.Error as error:
        print("Hiển thị danh sách hàng hóa lỗi: ",format(error))
        

def tao_hoa_don(ma_hd ,ma_hh):
    try:
        sql = "SELECT MaHH, TenHH, GiaBan, SoLuongDaBan FROM HANGHOA WHERE MaHH = %s"
        val = (ma_hh,)
        cursor.execute(sql, val)
        result = cursor.fetchone()
        
        if result:
            MaHH, TenHH, GiaBan, SoLuongDaBan = result
            sql = "INSERT INTO CHITIETHOADON (MaHD, MaHH, TenHH, GiaBan, SoLuongDaBan, ThanhToan) VALUES (%s,%s, %s, %s,%s,%s)"
            ThanhToan = GiaBan * SoLuongDaBan
            val = (ma_hd , MaHH, TenHH, GiaBan, SoLuongDaBan, ThanhToan)
            cursor.execute(sql, val)
            mydb.commit()
            print("Tạo hóa đơn thanh toán thành công")
        else:
            print("Không tìm thấy mã hàng hóa", ma_hh)
    except mysql.connector.Error as error:
        print("Tạo Hóa Đơn lỗi: ",format(error))
    
def xoa_hoa_don(ma_hd):
    try:
        sql = "DELETE FROM CHITIETHOADON WHERE MaHD = %s "
        val = (ma_hd,)
        cursor.execute(sql,val)
        mydb.commit()
        if cursor.rowcount > 0:
            print("Hóa đơn này đã được xóa")
        else:
            print("Hóa đơn này không tồn tại")
    except mysql.connector.Error as error:
        print("Xóa hóa đơn bị lỗi: ", format(error))
        
