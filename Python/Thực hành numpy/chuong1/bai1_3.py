import numpy as np

# Đọc dữ liệu

oop_data = np.genfromtxt("py\Thực hành numpy\oop_data.csv" ,delimiter=",")
    
# Hiển thị kiểu dữ liệu, kích thước, số chiều, số phần tử

print("Kích thước dữ liệu của biến: ", type(oop_data))
print("Kích thước của biến: ", oop_data.shape)
print("Số chiều của biến: ",oop_data.ndim)
print("Số Phần tử của biến:", oop_data.size)

# Tìm thời gian nhanh nhất, chậm nhất, trung bình 

min_times = np.min(oop_data, axis=0)
max_times = np.max(oop_data, axis=0)
mean_times = np.mean(oop_data, axis= 0)

# in ra thông tin
for i in range(1,5):
    print("Bài", str(i)+":")
    print("Thời gian làm bài nhanh nhất: ", min_times[i])
    print("Thời gian làm bài chậm nhất: ", max_times[i])
    print("Thời gian làm bài trung bình: ", mean_times[i])
    
# Thời gian làm bài trung bình làm tất cả
mean_times_all = np.mean(oop_data)

print("Thời gian hoàn thành tất cả bài tập là: ", mean_times_all)

# lưu thông tin 
oop_result = np.vstack((min_times, max_times, mean_times))
np.savetxt("py\Thực hành numpy\oop_result.csv", X=oop_result, delimiter=",",header="Thời gian nhanh nhất, chậm, trung bình:",fmt="%.2f", encoding="utf-8")