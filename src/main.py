import utils
from PIL import Image









def concatenate_images(image1_path, image2_path, output_path, watermark_path, position):
    try:
        # 定义要提取的范围和粘贴的位置
        crop_box1 = (140, 0, 670, 800)  # (left, upper, right, lower)
        paste_position1 = (0, 0)  # (x, y)
        crop_box2 = (280, 0, 550, 800)  # (left, upper, right, lower)
        paste_position2 = (530, 0)  # (x, y)

        image1 = utils.getPngObjectFromJpgOrPngPath(image1_path)
        image2 = utils.getPngObjectFromJpgOrPngPath(image2_path)
        watermark = utils.getPngObjectFromJpgOrPngPath(watermark_path)


        # 提取指定范围的子图像
        cropped_image1 = image1.crop(crop_box1)
        cropped_image2 = image2.crop(crop_box2)

        # # 确保两个图像具有相同的尺寸
        # if image1.size != image2.size:
        #     raise ValueError("两个图像的尺寸不匹配。")

        # 创建一个新的图像，尺寸是两个图像宽度的总和，高度等于其中一个图像的高度
        # new_width = image1.width + image2.width
        # new_height = image1.height
        new_image = Image.new("RGBA", (800, 800))

        # 将第一个图像粘贴到新图像的左侧
        new_image.paste(cropped_image1, paste_position1)

        # 将第二个图像粘贴到新图像的右侧
        new_image.paste(cropped_image2, paste_position2)

        # 调整水印图像的大小，使其与拼接后的图像大小相同
        watermark = watermark.resize(new_image.size)
        watermark = utils.adjust_transparency(watermark, 1)

        # 将拼接后的图像覆盖在水印图像上
        new_image_with_watermark = Image.alpha_composite(new_image, watermark.convert("RGBA"))

        # 保存带有水印的拼接图像
        new_image_with_watermark.save(output_path)
        print("拼接成功！")
    except Exception as e:
        print(f"拼接失败：{e}")

# 使用示例
image1_path = ".\\resource\\etxeondo_1_1.jpg"  # 第一个PNG图像的路径
image2_path = ".\\resource\\etxeondo_2_-1.jpg"  # 第二个PNG图像的路径
output_path = ".\\output\\concatenated.png"  # 拼接后的图像的输出路径
watermark_path = ".\\resource\\etxeondo_watermark.png"  # 水印图像的路径
position = (100, 100)  # 水印的位置，以拼接图像的左上角为参考点


# concatenate_images(image1_path, image2_path, output_path, watermark_path, position)



watermark = utils.getPngObjectFromJpgOrPngPath(".\\resource\\watermark.png")
watermark = watermark.resize((800,800))
adjusted_watermark = utils.adjust_watermark_opacity(watermark, 0.1)
for i in range(1,21):
    print(i)
    new_image = Image.new("RGBA", (800, 800))
    img1 = utils.getPngObjectFromJpgOrPngPath(".\\resource\\{}.jpg".format(i))
    img1 = img1.resize((800, 800))

    # result = add_watermark(img1, adjusted_watermark, position, 0.1)
    # new_image.paste(img1, (0,0))
    new_image = Image.alpha_composite(new_image, adjusted_watermark.convert("RGBA"))
    new_image = utils.convert_transparent_pixels_to_white(new_image)
    # new_image.save(".\\output\\{}.png".format(i))
    new_image = new_image.convert("RGB")
    new_image.save(".\\output\\{}.jpg".format(i), "JPEG", quality=95)