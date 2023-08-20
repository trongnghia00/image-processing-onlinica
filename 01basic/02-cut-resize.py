from PIL import Image

# Mở ảnh từ tệp tin
image = Image.open("my_image.jpg")

# Kích thước của khu vực cắt (left, upper, right, lower)
box = (150, 100, 850, 600)  # Ví dụ: cắt một hình vuông từ góc (100, 100) đến (400, 400)

# Cắt ảnh
cropped_image = image.crop(box)

# Hiển thị ảnh cắt
cropped_image.show()

# Kích thước mới (width, height)
new_size = (800, 600)  # Ví dụ: thay đổi kích thước thành 800x600 pixels

# Thay đổi kích thước ảnh
resized_image = cropped_image.resize(new_size)

# Hiển thị ảnh sau khi thay đổi kích thước
resized_image.show()

# Đóng ảnh sau khi hoàn thành
image.close()
cropped_image.close()
resized_image.close()