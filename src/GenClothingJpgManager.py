import re
import os
import SingleGoodsPngObj
from itertools import product
from PIL import Image
import utils
import config
import sys

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
                if not os.path.exists(outputPath):
                    continue
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
                        self.combineJpgObjList(
                            genJpgObjList,
                            outputPath,
                            oupputFileNameFormat,
                            jpgStyle,
                            sameIndexGroups=styleConfig.get("sameIndexGroups"),
                            distinctIndexGroups=styleConfig.get("distinctIndexGroups")
                        )
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
                self.combineJpgObjList(
                    genJpgObjList,
                    outputPath,
                    oupputFileNameFormat,
                    jpgStyle,
                    sameIndexGroups=styleConfig.get("sameIndexGroups"),
                    distinctIndexGroups=styleConfig.get("distinctIndexGroups")
                )



    def combineJpgObjList(self, genJpgObjList, outputPath, oupputFileNameFormat, jpgStyle, sameIndexGroups=None, distinctIndexGroups=None):
        # 进行组合
        filtered_combinations = []
        for combo in product(*genJpgObjList):
            is_valid = True
            if sameIndexGroups:
                for group in sameIndexGroups:
                    keys = []
                    for idx in group:
                        obj = combo[idx]
                        keys.append(getattr(obj, "matchKey", None))
                    if None in keys or len(set(keys)) != 1:
                        is_valid = False
                        break
            if is_valid and distinctIndexGroups:
                for group in distinctIndexGroups:
                    keys = []
                    for idx in group:
                        obj = combo[idx]
                        keys.append(getattr(obj, "matchKey", None))
                    # 组内全部不同；出现 None 或有重复则判为无效组合
                    if None in keys or len(set(keys)) != len(keys):
                        is_valid = False
                        break
            if is_valid:
                filtered_combinations.append(list(combo))

        for combination_idx, combination in enumerate(filtered_combinations, start=1):
            print(combination)
            print([item.index for item in list(combination)])
            combination.sort(key=lambda x: x.zOrder)
            conbineJpgObj = self.combinePngObjects(combination)
            oupputFileName = oupputFileNameFormat
            for i in range(len(combination)):
                # 如果字符串中有f"{{{i}}}"，则将其替换成combination[i].index
                if oupputFileName.find(f"{{{i}}}") != -1:
                    oupputFileName = oupputFileName.replace(f"{{{i}}}", f"{combination[i].index + 1}")
            oupputFileName = f"{oupputFileName}_{jpgStyle}_{combination_idx}.jpg"
            print(os.path.join(outputPath, oupputFileName))

            # utils.savePngObjectAsJpg(conbineJpgObj, os.path.join(outputPath, oupputFileName))
            self.saveGoodsJpg(conbineJpgObj, os.path.join(outputPath, oupputFileName))

        print(f"combinations:{filtered_combinations}")

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
        if not os.path.exists(sourcePath):
            return result
        for item in os.listdir(sourcePath):
            if os.path.isfile(f"{sourcePath}/{item}"):
                if re.match(CompositeElementsItem["fileNamePattern"], item):
                    print(f"item:{item}")
                    CompositeElementsItem["index"] = len(result)
                    m = re.match(r"(\d+)_", item)
                    if m:
                        CompositeElementsItem["matchKey"] = int(m.group(1))
                    else:
                        CompositeElementsItem.pop("matchKey", None)
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

def _get_runtime_root():
    """返回运行时根目录（保证打包后和源码运行时路径一致）"""
    if getattr(sys, 'frozen', False):
        return os.path.dirname(sys.executable)
    # 当前文件位于 src 目录下，项目根目录为其上一级
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def _select_brands(base_dir: str):
    """交互式选择品牌目录，返回选择的品牌列表"""
    brands = [d for d in os.listdir(base_dir) if os.path.isdir(os.path.join(base_dir, d))]
    if not brands:
        print("未在资源目录中发现任何品牌子目录。")
        return []

    print("可选品牌如下：")
    for i, b in enumerate(brands, start=1):
        print(f"[{i}] {b}")

    while True:
        choice = input("请输入要生成的品牌序号（支持多个，用逗号分隔；输入 all 选择全部）：").strip()
        if choice.lower() in ("all", "*"):
            return brands
        # 支持逗号、空格分隔
        tokens = [t for t in re.split(r"[\s,]+", choice) if t]
        indices = []
        valid = True
        for t in tokens:
            if not t.isdigit():
                valid = False
                break
            idx = int(t)
            if idx < 1 or idx > len(brands):
                valid = False
                break
            indices.append(idx)
        if valid and indices:
            # 去重并保持升序
            indices = sorted(set(indices))
            return [brands[i - 1] for i in indices]
        print("输入无效，请重新输入。")


def interactive_main():
    """交互式入口：选择品牌并生成对应图片"""
    project_root = _get_runtime_root()
    # 确保相对路径（./resource、./output）相对于项目根目录
    os.chdir(project_root)

    base_dir = os.path.join(project_root, "resource", "GoodsSinglePng")
    if not os.path.isdir(base_dir):
        print(f"{base_dir} 不存在，无法遍历品牌目录")
        return

    selected_brands = _select_brands(base_dir)
    if not selected_brands:
        return

    for brand in selected_brands:
        print(f"开始生成品牌：{brand}")
        genJpgForBrand(brand)


if __name__ == "__main__":
    interactive_main()
