
"""
工具所使用的所有原始png都按800*800制作（并为原始图的制作，制作对应的参考线PSD），
拼图过程都以800*800白底图的左下角为基准，原单品图只进行缩放和平移后以左下角在白底图左下角的相对位置作为位置
"""
import utils

AllTypeObjClass = {

}

# 定义一个带参数的类装饰器工厂函数
def genSingleGoodsClassDec(type, mainArea):
    class ClassDecorator:
        def __init__(self, cls):
            self.cls = cls  # 要装饰的类
            self.type = type
            self.mainArea = mainArea
            AllTypeObjClass[type] = cls

        def __call__(self, *args, **kwargs):
            instance = self.cls(*args, **kwargs)
            instance.type = self.type
            instance.mainArea = self.mainArea
            return instance
    return ClassDecorator

# # 使用类装饰器工厂函数来创建装饰器，并传递参数
# @bindSingleGoodsInfo = 

# # 应用装饰器到类上，并传递参数
# @bindSingleGoodsInfo
    


class PngDisplayObject():
    """
    显示对象
    """


    def __init__(self, filePath, config):
        """初始化方法，用于创建类的实例。

        Args:
            scaleX (int): X方向的缩放比例。
        self."""
        # 默认值
        self.scaleX = None
        self.scaleY = None
        self.x = 0
        self.y = 0
        self.width = 800
        self.height = 800
        self._anchorOffsetX = 0
        self._anchorOffsetY = 800
        self._percentAnchorOffsetX = None
        self._percentAnchorOffsetY = None
        self._mainArea = [0, 0, 0, 0] # 图片中主体所在位置左上角右下角坐标，即制定的参考线PSD位置
        self._type = ""
        self.displayPng = None
        self.index = -1
        self.zOrder = 0

        # 根据config修改值
        self.displayPng = utils.getPngObjectFromJpgOrPngPath(filePath)

        if self.displayPng != None:
            # 设置新的DPI值
            new_dpi = 300

            # 计算调整因子
            current_dpi = self.displayPng.info.get("dpi", (72, 72))  # 如果图像没有DPI信息，默认为(72, 72)
            dpi_scale_factor = new_dpi / current_dpi[0]  # 假设水平和垂直DPI相同

            # 调整图像大小，以匹配新的DPI值
            new_width = int(self.displayPng.width * dpi_scale_factor)
            new_height = int(self.displayPng.height * dpi_scale_factor)
            resized_image = self.displayPng.resize((new_width, new_height))

            # 更新DPI信息
            resized_image.info["dpi"] = (new_dpi, new_dpi)
            self.displayPng = resized_image
        if "zOrder" in config:
            self.zOrder = config["zOrder"]
        if "scale" in config:
            self.scaleX = config["scale"]
            self.scaleY = config["scale"]
        if "index" in config:
            self.index = config["index"]
        if "width" in config:
            self.index = config["width"]
        if "height" in config:
            self.index = config["height"]
        if "pos" in config:
            self.x = config["pos"][0]
            self.y = config["pos"][1]




    def _setAnchorOffsetX(self, value):
        """
        设置锚点X
        """
        if self._anchorOffsetX == value:
            return
        "如果value不是数字则将_anchorOffsetX置为0"
        if not isinstance(value, (int, float, complex)):
            self._anchorOffsetX = 0
        self._anchorOffsetX = value


    def _setAnchorOffsetY(self, value):
        """
        设置锚点Y
        """
        if self._anchorOffsetY == value:
            return
        "如果value不是数字则将_anchorOffsetY置为0"
        if not isinstance(value, (int, float, complex)):
            self._anchorOffsetY = 0
        self._anchorOffsetY = value

    def _getAnchorOffsetX(self):
        """
        获取锚点X
        """
        # 如果百分比锚点为None或者不是数字则直接返回_anchorOffsetX，反之则将百分比锚点乘以宽度返回
        if self._percentAnchorOffsetX is None or not isinstance(self._percentAnchorOffsetX, (int, float, complex)):
            return self._anchorOffsetX
        return self._percentAnchorOffsetX * self.width * 0.01

    def _getAnchorOffsetY(self):
        """
        获取锚点Y
        """
        return self._anchorOffsetY

    anchorOffsetX = property(_getAnchorOffsetX, _setAnchorOffsetX)
    anchorOffsetY = property(_getAnchorOffsetY, _setAnchorOffsetY)

bindCommonPng = genSingleGoodsClassDec("commonPng", [0, 0, 0, 0])
@bindCommonPng
class CommonPng(PngDisplayObject):
    def __init__(self, filePath, config):
        super().__init__(filePath, config)
        self._mainArea = [135, 18, 665, 782]


bindShirts = genSingleGoodsClassDec("shirts", [0, 0, 0, 0])
@bindShirts
class Shirts(PngDisplayObject):
    def __init__(self, filePath, config):
        super().__init__(filePath, config)
        self._mainArea = [135, 18, 665, 782]

bindLongShirts = genSingleGoodsClassDec("longShirts", [0, 0, 0, 0])
@bindLongShirts
class LongShirts(PngDisplayObject):
    def __init__(self, filePath, config):
        super().__init__(filePath, config)

bindShorts = genSingleGoodsClassDec("shorts", [0, 0, 0, 0])
@bindShorts
class Shorts(PngDisplayObject):
    def __init__(self, filePath, config):
        super().__init__(filePath, config)

bindBibShorts = genSingleGoodsClassDec("bibShorts", [0, 0, 0, 0])
@bindBibShorts
class BibShorts(PngDisplayObject):
    def __init__(self, filePath, config):
        super().__init__(filePath, config)

bindPants = genSingleGoodsClassDec("pants", [0, 0, 0, 0])
@bindPants
class Pants(PngDisplayObject):
    def __init__(self, filePath, config):
        super().__init__(filePath, config)

bindBibPants = genSingleGoodsClassDec("bibPants", [0, 0, 0, 0])
@bindBibPants
class BibPants(PngDisplayObject):
    def __init__(self, filePath, config):
        super().__init__(filePath, config)

bindVest = genSingleGoodsClassDec("vest", [0, 0, 0, 0])
@bindVest
class Vest(PngDisplayObject):
    def __init__(self, filePath, config):
        super().__init__(filePath, config)

bindLogo = genSingleGoodsClassDec("logo", [0, 0, 0, 0])
@bindLogo
class Logo(PngDisplayObject):
    def __init__(self, filePath, config):
        super().__init__(filePath, config)







# def main():
#     # parser = argparse.ArgumentParser()
#     # # parser.add_argument("--AddWaterMark", action="store_true", help="组合工具所需文件格式文件夹路")
#     # args = parser.parse_args()
#     # run(args)
#     test = PngDisplayObject("11")
#     test.anchorOffsetX = 100
#     print(test.anchorOffsetX)
#     print(test.anchorOffsetY)


# main()

    

    
    
