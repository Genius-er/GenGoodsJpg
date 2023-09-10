# TODO: genConfig需要思考出一个通用性，可读性，程序操作方便性都高的数据格式
SummerSetsConfig = {
    "configName": "SummerSets", # 每个款输出的路径为[brandName]\[configName]
    "configInfo": {
        "a": { 
            "desc": "短袖上衣正面图，图片文件名为n_0.jpg，n为shirts的数量",
            "CompositeElements": [
                # 合成部分
                {
                    "desc": "从对应品牌中筛选出短袖上衣",
                    "type": "shirts", # 对应 SingleGoodsPngObj 中的一个类型或者shirts文件夹名，output中用用shirts的子文件夹名进行分文件夹
                    "fileNamePattern": r'(\d+)_0\.png',
                    "zOrder": 0, # 合图时候的顺序，数字越小越在下面，反之则越在上面，默认是和key一样
                    "scale": 1.0,
                    "pos": [0, 0], # 这个一定要整数
                }
            ],
            "outputJpgFileName": "{0}_0", 
        },
        "b": { 
            "desc": "短袖上衣后背面无背带短裤",
            "CompositeElements": [
                # 合成部分
                {
                    "desc": "从对应品牌中筛选出短袖上衣",
                    "type": "shirts", # 对应 SingleGoodsPngObj 中的一个类型或者shirts文件夹名，output中用用shirts的子文件夹名进行分文件夹
                    "fileNamePattern": r'(\d+)_0\.png',
                    "zOrder": 1, # 合图时候的顺序，数字越小越在下面，反之则越在上面，默认是和key一样
                    "scale": 0.975,
                    "pos": [-115, 68],
                },
                {
                    "desc": "从对应品牌中筛选出短裤背面",
                    "type": "shorts", # 对应 SingleGoodsPngObj 中的一个类型或者shirts文件夹名，output中用用shirts的子文件夹名进行分文件夹
                    "fileNamePattern": r'(\d+)_1\.png',
                    "zOrder": 0, # 合图时候的顺序，数字越小越在下面，反之则越在上面，默认是和key一样
                    "scale": 0.53,
                    "pos": [435, 47],
                },
            ],
            "outputJpgFileName": "{0}_{1}", 
        },
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


# 春秋款
SpringAutumnSetsConfig = {
    "configName": "SpringAutumnAndWinterSets", # 每个款输出的路径为[brandName]\[configName]
    "configInfo": {
        "a": { 
            "desc": "单长袖上衣正面",
            "CompositeElements": [
                # 合成部分
                {
                    "desc": "从对应品牌中筛选出长袖上衣",
                    "type": "longShirts",
                    "fileNamePattern": r'(\d+)_0\.png',
                    "zOrder": 0,
                    "scale": 1.0,
                    "pos": [0, 0],
                }
            ],
            "outputJpgFileName": "{0}_0", 
        },
        "b": { 
            "desc": "长袖上衣和背面无背带长裤",
            "CompositeElements": [
                # 合成部分
                {
                    "desc": "从对应品牌中筛选出长袖上衣",
                    "type": "longShirts", # 对应 SingleGoodsPngObj 中的一个类型或者shirts文件夹名，output中用用shirts的子文件夹名进行分文件夹
                    "fileNamePattern": r'(\d+)_0\.png',
                    "zOrder": 1, # 合图时候的顺序，数字越小越在下面，反之则越在上面，默认是和key一样
                    "scale": 0.918,
                    "pos": [-77, 33],
                },
                {
                    "desc": "从对应品牌中筛选出无背带长裤背面",
                    "type": "pants", # 对应 SingleGoodsPngObj 中的一个类型或者shirts文件夹名，output中用用shirts的子文件夹名进行分文件夹
                    "fileNamePattern": r'(\d+)_1\.png',
                    "zOrder": 0, # 合图时候的顺序，数字越小越在下面，反之则越在上面，默认是和key一样
                    "scale": 0.806,
                    "pos": [342, 40],
                },
            ],
            "outputJpgFileName": "{0}_{1}", 
        },
        "c": { 
            "desc": "长袖袖上衣和背带长裤背面",
            "CompositeElements": [
                # 合成部分
                {
                    "desc": "从对应品牌中筛选出长袖袖上衣",
                    "type": "longShirts",
                    "fileNamePattern": r'(\d+)_0\.png',
                    "zOrder": 1,
                    "scale": 0.918,
                    "pos": [-77, 33],
                },
                {
                    "desc": "从对应品牌中筛选出长背带裤裤背面",
                    "type": "bibPants",
                    "fileNamePattern": r'(\d+)_1\.png',
                    "zOrder": 0,
                    "scale": 0.869,
                    "pos": [317, 52],
                },
            ],
            "outputJpgFileName": "{0}_{1}", 
        }
    }
}


# 冬款
WinterSetsConfig = {
    "configName": "SpringAutumnAndWinterSets", # 每个款输出的路径为[brandName]\[configName]
    "configInfo": {
        "a": { 
            "desc": "单长袖上衣正面",
            "CompositeElements": [
                # 合成部分
                {
                    "desc": "从对应品牌中筛选出长袖上衣",
                    "type": "longShirts",
                    "fileNamePattern": r'(\d+)_0\.png',
                    "zOrder": 0,
                    "scale": 1.0,
                    "pos": [0, 0],
                },
                {
                    "desc": "抓绒左上挂件",
                    "type": "commonPng",
                    "fileNamePattern": r'WinterLeftTop1\.png',
                    "zOrder": 0,
                    "scale": 0.732,
                    "pos": [-214, 397],
                }
            ],
            "outputJpgFileName": "winter/{0}_0", 
        },
        "b": { 
            "desc": "长袖上衣和背面无背带长裤",
            "CompositeElements": [
                # 合成部分
                {
                    "desc": "从对应品牌中筛选出长袖上衣",
                    "type": "longShirts", # 对应 SingleGoodsPngObj 中的一个类型或者shirts文件夹名，output中用用shirts的子文件夹名进行分文件夹
                    "fileNamePattern": r'(\d+)_0\.png',
                    "zOrder": 1, # 合图时候的顺序，数字越小越在下面，反之则越在上面，默认是和key一样
                    "scale": 0.918,
                    "pos": [-77, 33],
                },
                {
                    "desc": "从对应品牌中筛选出无背带长裤背面",
                    "type": "pants", # 对应 SingleGoodsPngObj 中的一个类型或者shirts文件夹名，output中用用shirts的子文件夹名进行分文件夹
                    "fileNamePattern": r'(\d+)_1\.png',
                    "zOrder": 0, # 合图时候的顺序，数字越小越在下面，反之则越在上面，默认是和key一样
                    "scale": 0.806,
                    "pos": [342, 40],
                },
                {
                    "desc": "抓绒左上挂件",
                    "type": "commonPng",
                    "fileNamePattern": r'WinterLeftTop1\.png',
                    "zOrder": 0,
                    "scale": 0.732,
                    "pos": [-214, 397],
                }
            ],
            "outputJpgFileName": "winter/{0}_{1}", 
        },
        "c": { 
            "desc": "长袖袖上衣和背带长裤背面",
            "CompositeElements": [
                # 合成部分
                {
                    "desc": "从对应品牌中筛选出长袖袖上衣",
                    "type": "longShirts",
                    "fileNamePattern": r'(\d+)_0\.png',
                    "zOrder": 1,
                    "scale": 0.918,
                    "pos": [-77, 33],
                },
                {
                    "desc": "从对应品牌中筛选出长背带裤裤背面",
                    "type": "bibPants",
                    "fileNamePattern": r'(\d+)_1\.png',
                    "zOrder": 0,
                    "scale": 0.869,
                    "pos": [317, 52],
                },
                {
                    "desc": "抓绒左上挂件",
                    "type": "commonPng",
                    "fileNamePattern": r'WinterLeftTop1\.png',
                    "zOrder": 0,
                    "scale": 0.732,
                    "pos": [-214, 397],
                }
            ],
            "outputJpgFileName": "winter/{0}_{1}", 
        }
    }
}
