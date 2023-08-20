from PIL import Image

# Mở ảnh từ tệp tin
image = Image.open("my_image.jpg")

# Đảo ngược ảnh theo chiều ngang
# flipped_image = image.transpose(Image.FLIP_LEFT_RIGHT)
flipped_image = image.transpose(Image.FLIP_TOP_BOTTOM)

# Hiển thị ảnh đảo ngược
flipped_image.show()

# Đóng các ảnh
image.close()
flipped_image.close()