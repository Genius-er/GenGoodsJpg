import re
import os
import SingleGoodsPngObj
from itertools import product
from PIL import Image
import utils

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
        basicSourcePath = f"./resource/GoodsSinglePng/{brandName}"
        basicOutputPath = f"./output/{brandName}/{genConfig['configName']}"
        outputPath = ""

        # 判断如果 basicSourcePath 不存在则直接return
        if not os.path.exists(basicSourcePath):
            print(f"{basicSourcePath} 不存在，无法生成")
            return


        for jpgStyle, styleConfig in genConfig["configInfo"].items():
            genJpgObjList = [] # 双层list，list里面每一项要组合
            oupputFileNameFormat = styleConfig["outputJpgFileName"]
            if  styleConfig["CompositeElements"][0]["type"] in ["shirts", "longShirts"]:
                # 要便利每个shirt下面的款式
                sourcePath = f'{basicSourcePath}/{styleConfig["CompositeElements"][0]["type"]}'
                # 便利sourcePath路径下的所有子文件，拿到子文件夹名
                for item in os.listdir(sourcePath):
                    if os.path.isdir(f"{sourcePath}/{item}"):
                        styleNum = item # 对应品牌中的款式序号
                        print(f"styleNum:{styleNum}")
                        sourcePath = f'{basicSourcePath}/{styleConfig["CompositeElements"][0]["type"]}/{styleNum}'
                        outputPath = f"{basicOutputPath}/{styleNum}"

                        for itemConfig in styleConfig["CompositeElements"]:
                            if itemConfig["type"] in ["shirts", "longShirts"]:
                                genJpgObjList.append(self.getSubJpgObjList(sourcePath, itemConfig))
                            else:
                                genJpgObjList.append(self.getSubJpgObjList(os.path.join(os.path.dirname(os.path.dirname(sourcePath)), f'{itemConfig["type"]}'), itemConfig))
            else:
                sourcePath = f'{basicSourcePath}/{styleConfig["CompositeElements"][0]["type"]}'
                outputPath = f'{basicOutputPath}/{styleConfig["CompositeElements"][0]["type"]}'
                for itemConfig in styleConfig["CompositeElements"]:
                    if itemConfig["type"] in ["shirts", "longShirts"]:
                        raise ValueError("shirts and longShirts can't be used in this function")
                    else:
                        genJpgObjList.append(self.getSubJpgObjList(sourcePath, itemConfig))

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
                utils.savePngObjectAsJpg(conbineJpgObj, os.path.join(outputPath, oupputFileName))
            print(f"combinations:{combinations}")

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

            pos = (combineImgItem.x, 800 - combineImgItem.y - size[1]) # xy的锚点是左下角，要映射成左上角的位置
    
            

            # 创建透明底图
            new_png = Image.new("RGBA", (800, 800), (255, 255, 255, 0))
            new_png.paste(combineImgItem.displayPng.resize(size), pos)
            white_bg = Image.alpha_composite(white_bg, new_png)

        return white_bg

                        
                        
                            

    def getSubJpgObjList(self, sourcePath, CompositeElementsItem):
        print(f"sourcePath:{sourcePath}")
        # print(f"outputPath:{outputPath}")
        print(f"CompositeElementsItem:{CompositeElementsItem}")
        result = []
        for item in os.listdir(sourcePath):
            if os.path.isfile(f"{sourcePath}/{item}"):
                if re.match(CompositeElementsItem["fileNamePattern"], item):
                    print(f"item:{item}")
                    CompositeElementsItem["index"] = len(result)
                    result.append(self.getJpgObj(CompositeElementsItem, f"{sourcePath}/{item}"))
        # if CompositeElementsItem["type"] in ["shirts", "longShirts"]:
        #     # 找到 sourcePath中与fileNamePattern匹配上的文件
        # else:


        return result
    
    def genJpgByObjList(self, objList, outputPath):
        for item in objList:
            item.genJpg(outputPath)


    def getJpgObj(self, config, filePath):
        return SingleGoodsPngObj.AllTypeObjClass[config["type"]](filePath, config)

    





# TODO: genConfig需要思考出一个通用性，可读性，程序操作方便性都高的数据格式
SummerSetsConfig = {
    "configName": "SummerSets", # 每个款输出的路径为[brandName]\[configName]
    "configInfo": {
        # "a": { 
        #     "desc": "短袖上衣正面图，图片文件名为n_0.jpg，n为shirts的数量",
        #     "CompositeElements": [
        #         # 合成部分
        #         {
        #             "desc": "从对应品牌中筛选出短袖上衣",
        #             "type": "shirts", # 对应 SingleGoodsPngObj 中的一个类型或者shirts文件夹名，output中用用shirts的子文件夹名进行分文件夹
        #             "fileNamePattern": r'(\d+)_0\.png',
        #             "zOrder": 0, # 合图时候的顺序，数字越小越在下面，反之则越在上面，默认是和key一样
        #             "scale": 1.0,
        #             "pos": [0, 0],
        #         }
        #     ],
        #     "outputJpgFileName": "{0}_0", 
        # },
        # "b": { 
        #     "desc": "短袖上衣后背面无背带短裤",
        #     "CompositeElements": [
        #         # 合成部分
        #         {
        #             "desc": "从对应品牌中筛选出短袖上衣",
        #             "type": "shirts", # 对应 SingleGoodsPngObj 中的一个类型或者shirts文件夹名，output中用用shirts的子文件夹名进行分文件夹
        #             "fileNamePattern": r'(\d+)_0\.png',
        #             "zOrder": 1, # 合图时候的顺序，数字越小越在下面，反之则越在上面，默认是和key一样
        #             "scale": 0.975,
        #             "pos": [-115, 68],
        #         },
        #         {
        #             "desc": "从对应品牌中筛选出短裤背面",
        #             "type": "shorts", # 对应 SingleGoodsPngObj 中的一个类型或者shirts文件夹名，output中用用shirts的子文件夹名进行分文件夹
        #             "fileNamePattern": r'(\d+)_1\.png',
        #             "zOrder": 0, # 合图时候的顺序，数字越小越在下面，反之则越在上面，默认是和key一样
        #             "scale": 0.53,
        #             "pos": [435, 47],
        #         },
        #     ],
        #     "outputJpgFileName": "{0}_{1}", 
        # },
        "c": { 
            "desc": "短袖上衣后背面背带短裤",
            "CompositeElements": [
                # 合成部分
                {
                    "desc": "从对应品牌中筛选出短袖上衣",
                    "type": "shirts",
                    "fileNamePattern": r'(\d+)_0\.png',
                    "zOrder": 1,
                    "scale": 1.0,
                    "pos": [-128, 0],
                },
                {
                    "desc": "从对应品牌中筛选出短裤背面",
                    "type": "bibShorts",
                    "fileNamePattern": r'(\d+)_1\.png',
                    "zOrder": 0,
                    "scale": 0.185,
                    "pos": [345, 0],
                },
            ],
            "outputJpgFileName": "{0}_{1}", 
        }

    }
}


def main():
    # parser = argparse.ArgumentParser()
    # # parser.add_argument("--AddWaterMark", action="store_true", help="组合工具所需文件格式文件夹路")
    # args = parser.parse_args()
    # run(args)
    genClothingJpgManager = GenClothingJpgManager()
    genClothingJpgManager.genOneBrandClothingSetJpg("ExampleBrand", SummerSetsConfig)
    # from itertools import product

    # my_lists = [[1, 2, 3, 4], ["a", "c", "d"], ["一", "二", "三"]]

    # combinations = list(product(*my_lists))

    # for combination in combinations:
    #     print(combination)
    #     print(list(combination))

    # print("Finish")


main()