from PIL import Image
import os

'''将rgba图片的透明像素转成白色'''
def convert_transparent_pixels_to_white(image):
    try:
        # 获取图像的宽度和高度
        width, height = image.size

        # 遍历图像的每个像素
        for x in range(width):
            for y in range(height):
                # 获取当前像素的RGBA值
                r, g, b, a = image.getpixel((x, y))

                # 如果像素是完全透明的
                if a == 0:
                    # 将颜色值修改为白色（255, 255, 255）
                    image.putpixel((x, y), (255, 255, 255, 255))

        return image
    except Exception as e:
        print(f"处理图像失败：{e}")




def getPngObjectFromJpgOrPngPath(img_path):
    """
    读取指定文件路径的jpg或png，返回png对象
    :param img_path: 图片路径
    :return: PIL.Image对象，输出的处理后的PNG图片
    """
    try:
        # 将图片文件名中的点改成_

        # 获取文件名和扩展名
        file_name, file_ext = os.path.splitext(os.path.basename(img_path))


        # 如果文件名中包含点
        if "." in file_name:
            # 将点替换为下划线
            new_file_name = file_name.replace(".", "_")

            # 构造新的文件路径
            new_file_path = os.path.join(os.path.dirname(img_path), new_file_name + file_ext)

            # 重命名文件
            os.rename(img_path, new_file_path)

            # 更新img_path
            img_path = new_file_path

        # 读取图片文件
        pngObj = None
        if img_path.endswith(".jpg"): # 
            jpgObj = Image.open(img_path)
            pngObj = Image.new("RGBA", jpgObj.size)
            pngObj.paste(jpgObj)
        elif img_path.endswith(".png"): # 
            pngObj = Image.open(img_path).convert("RGBA")

        if pngObj is None:
            return None
        return pngObj.resize((800, 800))
    except Exception as e:
        print(f"拼接失败：{e}")
        return None


'''调整png对象的透明度'''
def adjust_transparency(png_image, alpha):
    try:
        # 获取透明度通道
        alpha_channel = png_image.split()[3]

        # 创建一个新的透明度通道，修改每个像素的透明度值
        adjusted_alpha_channel = alpha_channel.point(lambda p: p * alpha)

        # 将修改后的透明度通道与原图像的RGB通道合并
        adjusted_image = Image.merge("RGBA", png_image.split()[:3] + (adjusted_alpha_channel,))

        return adjusted_image
    except Exception as e:
        print(f"调整透明度失败：{e}")



'''给image加水印到指定位置，指定透明度'''
def add_watermark(image, watermark, position, opacity):
    try:
        # 将水印图像调整为与原图像相同的大小
        watermark = watermark.resize(image.size)

        # 创建一个与原图像相同的透明图层
        transparent_layer = Image.new("RGBA", image.size)

        # 在透明图层上粘贴水印图像
        transparent_layer.paste(watermark, position)

        # 将透明图层与原图像进行混合，调整水印的透明度
        blended_image = Image.blend(image, transparent_layer, opacity)

        return blended_image
    except Exception as e:
        print(f"添加水印失败：{e}")


'''调整水印watermark透明度opacity'''
def adjust_watermark_opacity(watermark, opacity):
    try:
        # 提取水印图像的透明度通道
        watermark = watermark.convert("RGBA")
        data = watermark.getdata()

        # 调整透明度通道的值
        new_data = []
        for item in data:
            r, g, b, a = item
            new_data.append((r, g, b, int(a * opacity)))

        # 创建调整后的水印图像
        adjusted_watermark = Image.new("RGBA", watermark.size)
        adjusted_watermark.putdata(new_data)

        return adjusted_watermark
    except Exception as e:
        print(f"调整水印透明度失败：{e}")

def changeTransparentPixelsToWhite(png_image):
    """
    将PNG图片中的透明像素更改为白色
    :param png_image: PIL.Image对象，输入的PNG图片
    :return: PIL.Image对象，输出的处理后的PNG图片
    """
    # 创建一个与输入图片大小相同的白色背景图像
    white_bg = Image.new("RGBA", png_image.size, (255, 255, 255, 255))

    # 将输入图片与白色背景图像合并
    combined_image = Image.alpha_composite(white_bg, png_image)

    return combined_image


def savePngObjectAsJpg(png_object, output_path):
    """
    将PNG图片保存为jpg文件
    :param png_object: PIL.Image对象，输入的PNG图片
    :param output_path: 保存路径
    """
    
    try:
        os.makedirs(os.path.dirname(output_path), exist_ok=True)

        # 将PNG对象转换为RGB模式，以便将其保存为JPG
        rgb_image = png_object.convert('RGB')
        # 保存JPG图片到指定的输出路径
        rgb_image.save(output_path, 'JPEG')
        print(output_path)

        file_name, file_ext = os.path.splitext(os.path.basename(output_path))
        if "." in file_name:
            raise Exception("文件名中不能用.  请用_代替.")

    except Exception as e:
        print(f"处理图像失败：{e}")


def combinePngObjects(combineImgInfo):
    """
    将PNG图片保存为jpg文件
    :param combineImgInfo 需要组合的多张图片的信息，包括PIL.Image对象, 缩放比例，放在800*800图片的位置
    :return: 组合后的PIL.Image对象的png对象
    """
    
    # 创建白色底图
    white_bg = Image.new("RGBA", (800, 800), (255, 255, 255, 255))

    # 往白色底图上贴图
    for eachInfo in combineImgInfo:
        size = eachInfo["size"]
        pos = eachInfo["pos"]
        pngItem = eachInfo["png"]
        

        # 创建透明底图
        new_png = Image.new("RGBA", (800, 800), (255, 255, 255, 0))
        new_png.paste(pngItem.resize(size), pos)
        white_bg = Image.alpha_composite(white_bg, new_png)

    return white_bg



def del_files_or_folder(dir_path):
    """
    # (不支持文件，文件夹不存在会报错)
    # os.walk会得到dir_path下各个后代文件夹和其中的文件的三元组列表，顺序自内而外排列，
    # 如 log下有111文件夹，111下有222文件夹：[('D:\\log\\111\\222', [], ['22.py']), ('D:\\log\\111', ['222'], ['11.py']), ('D:\\log', ['111'], ['00.py'])]
    """
    for root, dirs, files in os.walk(dir_path, topdown=False):
        # 第一步：删除文件
        for name in files:
            os.remove(os.path.join(root, name))  # 删除文件
        # 第二步：删除空文件夹
        for name in dirs:
            os.rmdir(os.path.join(root, name)) # 删除一个空目录