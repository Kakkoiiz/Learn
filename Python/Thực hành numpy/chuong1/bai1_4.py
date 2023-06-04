import numpy as np

# Đọc dữ liệu từ tệp asean_data.csv
data = np.genfromtxt("py\Thực hành numpy\Asean_data.csv", delimiter=',', dtype=[('Country', 'U20'), ('Population', float), ('Area', int), ('GDP', int)], skip_header=1)

# Tìm nước có dân số nhiều nhất và ít nhất
most_populous_country = data['Country'][np.argmax(data['Population'])]
least_populous_country = data['Country'][np.argmin(data['Population'])]

print('Nuớc có dân số nhiều nhất là: ', most_populous_country)
print('Nước có dân số ít nhất là: ',least_populous_country)
# Tìm nước có diện tích lớn nhất và nhỏ nhất

largest_area_country = data['Country'][np.argmax(data['Area'])]
smallest_area_country = data['Country'][np.argmin(data['Area'])]

print('Nước có diện tích lớn nhất là: ', largest_area_country)
print('Nước có diện thích nhỏ nhất là: ',smallest_area_country)

# Tính mật độ dân số 

population_density = (data['Population']*1000000) / data['Area']
# Tinh GDP bình quân đầu người

gdp = data['GDP'] / data['Population']

# Lưu thông tin 
Asean_result = np.column_stack((population_density,gdp))
np.savetxt("py\Thực hành numpy\Asean_result.csv", X = Asean_result, delimiter="|", fmt="%.f", encoding="utf-8")