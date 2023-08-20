from PIL import Image

# Mở ảnh từ tệp tin
image = Image.open("my_image.jpg")

# Hiển thị ảnh trong cửa sổ đồ họa
image.show()

# Đóng ảnh sau khi hoàn thành
image.close()