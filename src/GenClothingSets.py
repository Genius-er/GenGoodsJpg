'''
此脚本的作用是将按标准制作的产品单图（上衣和有无背带裤），合并成产品套装图，并用参数控制否是加水印
    1、短袖上衣参考位置（135，18，665，782）
    2、无背带短裤（140，90，660，710）
    3、有背带短裤（270，65，530，735）
'''
import sys
import argparse
import os
import utils
from PIL import Image
import config
import re
import copy

"""本脚本的工作路径"""
WORK_PATH = "./resource/resourceForGenClothingSets"
OUTPUT_PATH = "./output/resourceForGenClothingSets"

SHORT_SLEEVE_SHIRTS_POS = [135, 18, 665, 782] # 短袖上衣的图片位置
STRAPLESS_SHORTS_POS = [140, 90, 660,710] # 无背带短裤的图片位置
BIB_SHORTS = [270, 65, 530, 735] # 有背带短裤的图片位置

# 是否加水印
AddWaterMark = True

# 统计数值
brandNum = 0 # 品牌数量
brandGoodsInfo = { # 记录每个品牌的数据

}

def genClothingSets():
    global brandNum
    print("====start=================================================")
    for Brand in os.listdir(WORK_PATH):
        if os.path.isdir(os.path.join(WORK_PATH, Brand)):
            print('================Start generating product maps for [{0}]=========================='.format(Brand))
            brandNum += 1
            genOneBrandClothingSets(Brand)
            print('================Finish generating product maps for [{0}]=========================='.format(Brand))

OneBrandAllPngObjInfo = {}
OneBrandAllShortsPngInfo = {}
OneBrandAllBibShortsPngInfo = {}
watermarkObj = Image.new("RGBA", (800, 800))
def genOneBrandClothingSets(Brand):
    global OneBrandAllShortsPngInfo, OneBrandAllBibShortsPngInfo, OneBrandAllPngObjInfo, watermarkObj
    BRAND_FILE_FOLDER_PATH = os.path.join(WORK_PATH, Brand) # 当前品牌的资源路径
    BRAND_OUTPUT_PATH = os.path.join(OUTPUT_PATH, Brand) # 当前品牌的工具输出资源路径


    # 清空环境
    OneBrandAllPngObjInfo = {}

    # 清空输出目录
    if os.path.exists(BRAND_OUTPUT_PATH):
        utils.del_files_or_folder(BRAND_OUTPUT_PATH)

    # 获取水印对象
    watermarkObj = utils.getPngObjectFromJpgOrPngPath(os.path.join(WORK_PATH, "watermark.png"))


    # 获取所有【无背带】短裤png对象到shorts_png_list
    shorts_file_list = [os.path.join(BRAND_FILE_FOLDER_PATH, "shorts", file) for file in os.listdir(os.path.join(BRAND_FILE_FOLDER_PATH, "shorts"))]
    shorts_png_list = []
    OneBrandAllShortsPngInfo = {}
    for file in shorts_file_list:
        # Process each file in the file_list
        oneShortsPngObj = utils.getPngObjectFromJpgOrPngPath(file)
        shorts_png_list.append(oneShortsPngObj)
        file_name, file_ext = os.path.splitext(os.path.basename(file))
        OneBrandAllShortsPngInfo[file_name] = oneShortsPngObj
        OneBrandAllPngObjInfo["Shorts_" + file_name] = oneShortsPngObj
        utils.savePngObjectAsJpg(utils.changeTransparentPixelsToWhite(oneShortsPngObj), os.path.join(OUTPUT_PATH, Brand, "Shorts", "Shorts_" + file_name + ".jpg"))
        utils.savePngObjectAsJpg(utils.changeTransparentPixelsToWhite(Image.alpha_composite(oneShortsPngObj, watermarkObj)), os.path.join(OUTPUT_PATH, Brand, "Shorts", "水印", "Shorts_" + file_name + ".jpg"))


    # 获取所有【有背带】短裤png对象到shorts_png_list
    bibShorts_file_list = [os.path.join(BRAND_FILE_FOLDER_PATH, "bibShorts", file) for file in os.listdir(os.path.join(BRAND_FILE_FOLDER_PATH, "bibShorts"))]
    bibShorts_png_list = []
    OneBrandAllBibShortsPngInfo = {}
    for file in bibShorts_file_list:
        oneShortsPngObj = utils.getPngObjectFromJpgOrPngPath(file)
        bibShorts_png_list.append(oneShortsPngObj)
        file_name, file_ext = os.path.splitext(os.path.basename(file))
        OneBrandAllBibShortsPngInfo[file_name] = oneShortsPngObj
        OneBrandAllPngObjInfo["BibShorts_" + file_name] = oneShortsPngObj
        utils.savePngObjectAsJpg(utils.changeTransparentPixelsToWhite(oneShortsPngObj), os.path.join(OUTPUT_PATH, Brand, "Shorts", "BibShorts_" + file_name + ".jpg"))
        utils.savePngObjectAsJpg(utils.changeTransparentPixelsToWhite(Image.alpha_composite(oneShortsPngObj, watermarkObj)), os.path.join(OUTPUT_PATH, Brand, "Shorts", "水印", "BibShorts_" + file_name + ".jpg"))




    # 遍历当前品牌的所有款式
    for eachShape in os.listdir(os.path.join(BRAND_FILE_FOLDER_PATH, "shirts")):
        if os.path.isdir(os.path.join(BRAND_FILE_FOLDER_PATH, "shirts", eachShape)):
            genOneBradOneShapSets(Brand, eachShape, shorts_png_list, bibShorts_png_list, watermarkObj)


    print("====end===================================================")
    

AllShapShirtsPngInfo = {}
ColorNumInOneShap = 0 # 一款产品中的颜色数量
def genOneBradOneShapSets(Brand, Shape, shorts_png_list, bibShorts_png_list, watermarkObj):
    global AllShapShirtsPngInfo, ColorNumInOneShap
    Shape_FILE_FOLDER_PATH = os.path.join(WORK_PATH, Brand, "shirts", Shape) # 当前品牌当前款的资源路径
    Shape_OUTPUT_PATH = os.path.join(OUTPUT_PATH, Brand, Shape) # 当前品牌的工具输出资源路径
     # 获取所有上衣正面png对象到shirts_png_list
    shirts_file_list = [file for file in os.listdir(Shape_FILE_FOLDER_PATH)]

    shirts_png_list = []  # 产品正面图
    AllShapShirtsPngInfo = {} # 保存上衣不同方向的图片，制作不同样式拼图
    for file in shirts_file_list:
        if file.replace(".png", "").find("_") == -1 or file.replace(".png", "").split("_")[1] == "0":
            shirts_png_list.append(utils.getPngObjectFromJpgOrPngPath(os.path.join(Shape_FILE_FOLDER_PATH, file)))

        file_name, file_ext = os.path.splitext(os.path.basename(file))
        AllShapShirtsPngInfo["Shirts_" + file_name] = utils.getPngObjectFromJpgOrPngPath(os.path.join(Shape_FILE_FOLDER_PATH, file))
        # OneBrandAllPngObjInfo["Shirts_" + Shape + file_name] = utils.getPngObjectFromJpgOrPngPath(os.path.join(Shape_FILE_FOLDER_PATH, file))
    
    ColorNumInOneShap = 0
    for i in range(len(config.GoodsJpgStyleConfig)):
        recursionGenJpgByRegular(Shape_OUTPUT_PATH, config.GoodsJpgStyleConfig, i, 0, [], None, 0)
    os.rename(Shape_OUTPUT_PATH, Shape_OUTPUT_PATH + f"({ColorNumInOneShap})")




ShapJpgNum = 0
def recursionGenJpgByRegular(outputPath, regularconfig, regularConfigIndex, regularIndex, matchParam, pngObj, ShapId):
    global OneBrandAllPngObjInfo, AllShapShirtsPngInfo, ShapJpgNum, watermarkObj, ColorNumInOneShap
    if regularConfigIndex >= len(regularconfig):
        return
    regularConfigItem = regularconfig[regularConfigIndex]
    if regularIndex >= len(regularConfigItem): # 超过了配置长度
        utils.savePngObjectAsJpg(pngObj, os.path.join(outputPath, "{0}_{1}_{2}.jpg".format(ShapId, ShapJpgNum, regularConfigIndex)))
        utils.savePngObjectAsJpg(utils.changeTransparentPixelsToWhite(Image.alpha_composite(pngObj, watermarkObj)), os.path.join(outputPath, "水印", "{0}_{1}_{2}.jpg".format(ShapId, ShapJpgNum, regularConfigIndex)))
        ShapJpgNum += 1
        if int(ShapId) > ColorNumInOneShap:
            ColorNumInOneShap = int(ShapId)
        return
    if regularIndex == 0 or pngObj == None: # 第一项
        ShapId = 0
        patternStr = regularConfigItem[regularIndex]["patternStr"]
        if patternStr.find("Shirts_") == 0:
            matchKeys = [] # 符合正则的所有key
            for key in AllShapShirtsPngInfo.keys():
                if re.match(patternStr, key):
                    matchKeys.append(key)
            for i in range(len(matchKeys)):
                eachKey = matchKeys[i]
                ShapId = re.match(patternStr, eachKey)[1]
                tmpMatchParam = copy.deepcopy(matchParam)
                tmpMatchParam.append(re.match(patternStr, eachKey))
                combineImgInfo = [{
                "size": regularConfigItem[regularIndex]["size"],
                "pos": regularConfigItem[regularIndex]["pos"],
                "png": AllShapShirtsPngInfo[eachKey]
                }]
                newPngObj = utils.combinePngObjects(combineImgInfo)
                # ShapId += 1
                ShapJpgNum = 1
                recursionGenJpgByRegular(outputPath, regularconfig, regularConfigIndex, regularIndex + 1, tmpMatchParam, newPngObj, ShapId)
        else:
            matchKeys = [] # 符合正则的所有key
            for key in OneBrandAllPngObjInfo.keys():
                if re.match(patternStr, key):
                    matchKeys.append(key)
                for i in range(len(matchKeys)):
                    eachKey = matchKeys[i]
                    tmpMatchParam = copy.deepcopy(matchParam)
                    tmpMatchParam.append(re.match(patternStr, key))
                    combineImgInfo = [{
                    "size": regularConfigItem[regularIndex]["size"],
                    "pos": regularConfigItem[regularIndex]["pos"],
                    "png": OneBrandAllPngObjInfo[eachKey]
                    }]
                    newPngObj = utils.combinePngObjects(combineImgInfo)
                    # ShapId += 1
                    ShapId = re.match(patternStr, eachKey)[1]
                    ShapJpgNum = 1
                    recursionGenJpgByRegular(outputPath, regularconfig, regularConfigIndex, regularIndex + 1, tmpMatchParam, newPngObj, ShapId)

    else: # 第二项开始
        patternStr = regularConfigItem[regularIndex]["patternStr"]
        if "regularParams" in regularConfigItem[regularIndex]:
            params = []
            for each in regularConfigItem[regularIndex]["regularParams"]:
                params.append(matchParam[each[0]][each[1]])
            patternStr = patternStr.format(*params)
        if patternStr.find("Shirts_") == 0:
            matchKeys = [] # 符合正则的所有key
            for key in AllShapShirtsPngInfo.keys():
                if re.match(patternStr, key):
                    matchKeys.append(key)
            for i in range(len(matchKeys)):
                eachKey = matchKeys[i]
                tmpMatchParam = copy.deepcopy(matchParam)
                tmpMatchParam.append(re.match(patternStr, key))
                combineImgInfo = [{
                    "size": (800, 800),
                    "pos": (0, 0),
                    "png": pngObj
                    },
                    {
                    "size": regularConfigItem[regularIndex]["size"],
                    "pos": regularConfigItem[regularIndex]["pos"],
                    "png": AllShapShirtsPngInfo[eachKey]
                }]
                newPngObj = utils.combinePngObjects(combineImgInfo)
                # ShapId += 1
                recursionGenJpgByRegular(outputPath, regularconfig, regularConfigIndex, regularIndex + 1, tmpMatchParam, newPngObj, ShapId)
        else:
            matchKeys = [] # 符合正则的所有key
            for key in OneBrandAllPngObjInfo.keys():
                if re.match(patternStr, key):
                    matchKeys.append(key)
            for i in range(len(matchKeys)):
                eachKey = matchKeys[i]
                tmpMatchParam = copy.deepcopy(matchParam)
                tmpMatchParam.append(re.match(patternStr, key))
                combineImgInfo = [{
                "size": (800, 800),
                "pos": (0, 0),
                "png": pngObj
                },{
                "size": regularConfigItem[regularIndex]["size"],
                "pos": regularConfigItem[regularIndex]["pos"],
                "png": OneBrandAllPngObjInfo[eachKey]
                }]
                newPngObj = utils.combinePngObjects(combineImgInfo)
                # ShapId += 1
                recursionGenJpgByRegular(outputPath, regularconfig, regularConfigIndex, regularIndex + 1, tmpMatchParam, newPngObj, ShapId)




def run(args):
    # global AddWaterMark
    # filefolderPath = args.filefolderPath
    # AddWaterMark = args.filefolderPath
    genClothingSets()
    

def main():
    parser = argparse.ArgumentParser()
    # parser.add_argument("--AddWaterMark", action="store_true", help="组合工具所需文件格式文件夹路")
    args = parser.parse_args()
    run(args)


main()
