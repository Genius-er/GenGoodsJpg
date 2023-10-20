import re
import os
import SingleGoodsPngObj
from itertools import product
from PIL import Image
import utils
import config

class GenClothingJpgManager():
    def __init__(self):
        print("init")

    


    def genOneBrandClothingSetJpg(self, brandName: str, genConfig: dict):
        """生成单个品牌单个产品指定生成配置生成产品图
        Args:
            brandName (str): 产品名，对应resource/GoodesSinglePng里的子文件夹名;
            genConfig (dict): 决定用哪些图和哪些图组合生成哪些图的配置文件;
        """
        print(f"========开始生成，品牌{brandName}, 使用的生成配置为{genConfig}========")
        projectSourcePath = "./resource"
        basicSourcePath = f"./resource/GoodsSinglePng/{brandName}"
        basicOutputPath = f"./output/{brandName}/{genConfig['configName']}"
        outputPath = ""

        # 判断如果 basicSourcePath 不存在则直接return
        if not os.path.exists(basicSourcePath):
            print(f"{basicSourcePath} 不存在，无法生成")
            return


        for jpgStyle, styleConfig in genConfig["configInfo"].items():
            oupputFileNameFormat = styleConfig["outputJpgFileName"]
            if  styleConfig["CompositeElements"][0]["type"] in ["shirts", "longShirts", "vest"]:
                # 要便利每个shirt下面的款式
                sourcePath = f'{basicSourcePath}/{styleConfig["CompositeElements"][0]["type"]}'
                # 便利sourcePath路径下的所有子文件，拿到子文件夹名
                for item in os.listdir(sourcePath):
                    stylePath = f"{sourcePath}/{item}"
                    if os.path.isdir(f"{sourcePath}/{item}"):
                        genJpgObjList = [] # 双层list，list里面每一项要组合 
                        styleNum = item # 对应品牌中的款式序号
                        print(f"styleNum:{styleNum}")
                        styleSourcePath = f'{basicSourcePath}/{styleConfig["CompositeElements"][0]["type"]}/{styleNum}'
                        allColorNum = []
                        for item in os.listdir(stylePath):
                            if os.path.isfile(f"{stylePath}/{item}"):
                                if re.match(r'(\d+)_(\d+)\.png', item):
                                    colorNum = int(item.split("_")[0])
                                    if colorNum not in allColorNum:
                                        allColorNum.append(colorNum)
                        colorNumOfOneStyle = len(allColorNum) # 一款产品中的颜色数量
                        outputPath = f'{basicOutputPath}/{styleNum}({colorNumOfOneStyle})'

                        for itemConfig in styleConfig["CompositeElements"]:
                            if itemConfig["type"] in ["shirts", "longShirts", "vest"]:
                                genJpgObjList.append(self.getSubJpgObjList(styleSourcePath, itemConfig))
                            elif itemConfig["type"] in ["commonPng"]: # 各品牌通用图片需要往品牌外一层找图片
                                genJpgObjList.append(self.getSubJpgObjList(os.path.join(projectSourcePath, "commonPng"), itemConfig))
                            else:
                                genJpgObjList.append(self.getSubJpgObjList(os.path.join(os.path.dirname(os.path.dirname(styleSourcePath)), f'{itemConfig["type"]}'), itemConfig))
                        self.combineJpgObjList(genJpgObjList, outputPath, oupputFileNameFormat, jpgStyle)
            else:
                genJpgObjList = [] # 双层list，list里面每一项要组合 
                sourcePath = f'{basicSourcePath}/{styleConfig["CompositeElements"][0]["type"]}'
                outputPath = f'{basicOutputPath}/{styleConfig["CompositeElements"][0]["type"]}'
                for itemConfig in styleConfig["CompositeElements"]:
                    if itemConfig["type"] in ["shirts", "longShirts", "vest"]:
                        raise ValueError("shirts and longShirts can't be used in this function")
                    elif itemConfig["type"] in ["commonPng"]: # 各品牌通用图片需要往品牌外一层找图片
                        genJpgObjList.append(self.getSubJpgObjList(os.path.join(projectSourcePath, "commonPng"), itemConfig))
                    else:
                        genJpgObjList.append(self.getSubJpgObjList(sourcePath, itemConfig))
                self.combineJpgObjList(genJpgObjList, outputPath, oupputFileNameFormat, jpgStyle)



    def combineJpgObjList(self, genJpgObjList, outputPath, oupputFileNameFormat, jpgStyle):
        # 进行组合
        combinations = list(product(*genJpgObjList))
        for combination in combinations:
            print(combination)
            combination = list(combination)
            print([item.index for item in list(combination)])
            a = list(combination).sort(key=lambda x: x.zOrder)
            conbineJpgObj = self.combinePngObjects(sorted(combination, key=lambda x: x.zOrder))
            oupputFileName = oupputFileNameFormat
            for i in range(len(combination)):
                # 如果字符串中有f"{{{i}}}"，则将其替换成combination[i].index
                if oupputFileName.find(f"{{{i}}}") != -1:
                    oupputFileName = oupputFileName.replace(f"{{{i}}}", f"{combination[i].index + 1}")
            oupputFileName = f"{oupputFileName}_{jpgStyle}.jpg"
            print(os.path.join(outputPath, oupputFileName))

            # utils.savePngObjectAsJpg(conbineJpgObj, os.path.join(outputPath, oupputFileName))
            self.saveGoodsJpg(conbineJpgObj, os.path.join(outputPath, oupputFileName))

        print(f"combinations:{combinations}")

    def saveGoodsJpg(self, jpgObj, path):
        utils.savePngObjectAsJpg(jpgObj, path)
        utils.savePngObjectAsJpg(self.addWarterMark(jpgObj), os.path.join(os.path.dirname(path), "watermark", os.path.basename(path)))


    def addWarterMark(self, pngObj, watermarkSourceName = "watermark1.png"):
        watermark = utils.getPngObjectFromJpgOrPngPath(os.path.join("./resource/commonPng", watermarkSourceName))
        if watermark is None:
            return pngObj
        return self.combineImageObj(pngObj, watermark.resize((800, 800)), (0, 0))
        

    def combinePngObjects(self, combineImgInfo):
        """
        将PNG图片保存为jpg文件
        :param combineImgInfo 需要组合的多张图片的信息，包括PIL.Image对象, 缩放比例，放在800*800图片的位置
        :return: 组合后的PIL.Image对象的png对象
        """
        # 创建白色底图
        white_bg = Image.new("RGBA", (800, 800), (255, 255, 255, 255))

        # 往白色底图上贴图
        for combineImgItem in combineImgInfo:
            size = (combineImgItem.width, combineImgItem.height)
            # 有scale优先使用scale
            if combineImgItem.scaleX is not None and combineImgItem.scaleY is not None:
                size = (int(combineImgItem.scaleX * combineImgItem.displayPng.width), int(combineImgItem.scaleY * combineImgItem.displayPng.height))

            pos = (int(combineImgItem.x - size[1]/2), int(combineImgItem.y - size[1]/2)) # xy的锚点是左下角，要映射成左上角的位置
    
            

            # 创建透明底图
            white_bg = self.combineImageObj(white_bg, combineImgItem.displayPng.resize(size), pos)

        return white_bg
    
    def combineImageObj(self, baseImg, newImg2, pos):
        new_png = Image.new("RGBA", (800, 800), (255, 255, 255, 0))
        new_png.paste(newImg2, pos)
        return Image.alpha_composite(baseImg, new_png)

                        
                        
                            

    def getSubJpgObjList(self, sourcePath, CompositeElementsItem):
        print(f"sourcePath:{sourcePath}")
        print(f"CompositeElementsItem:{CompositeElementsItem}")
        result = []
        for item in os.listdir(sourcePath):
            if os.path.isfile(f"{sourcePath}/{item}"):
                if re.match(CompositeElementsItem["fileNamePattern"], item):
                    print(f"item:{item}")
                    CompositeElementsItem["index"] = len(result)
                    result.append(self.getJpgObj(CompositeElementsItem, f"{sourcePath}/{item}"))
        return result
    
    def genJpgByObjList(self, objList, outputPath):
        for item in objList:
            item.genJpg(outputPath)


    def getJpgObj(self, config, filePath):
        return SingleGoodsPngObj.AllTypeObjClass[config["type"]](filePath, config)



def genJpgForBrand(brand):
    genClothingJpgManager = GenClothingJpgManager()
    # genClothingJpgManager.genOneBrandClothingSetJpg(brand, config.SummerSetsConfig)
    genClothingJpgManager.genOneBrandClothingSetJpg(brand, config.SpringAutumnSetsConfig)
    genClothingJpgManager.genOneBrandClothingSetJpg(brand, config.WinterSetsConfig)



def main():

    genJpgForBrand("etxeondo")


main()