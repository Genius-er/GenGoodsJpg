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
                    "pos": [400,400], # 这个一定要整数
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
                    "pos": [275, 342],
                },
                {
                    "desc": "从对应品牌中筛选出短裤背面",
                    "type": "shorts", # 对应 SingleGoodsPngObj 中的一个类型或者shirts文件夹名，output中用用shirts的子文件夹名进行分文件夹
                    "fileNamePattern": r'(\d+)_1\.png',
                    "zOrder": 0, # 合图时候的顺序，数字越小越在下面，反之则越在上面，默认是和key一样
                    "scale": 0.53,
                    "pos": [650, 548],
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
                    "pos": [280, 400],
                },
                {
                    "desc": "从对应品牌中筛选出短裤背面",
                    "type": "bibShorts",
                    "fileNamePattern": r'(\d+)_1\.png',
                    "zOrder": 0,
                    "scale": 0.185,
                    "pos": [658, 501],
                },
            ],
            "outputJpgFileName": "{0}_{1}", 
        },
        "d": { 
            "desc": "背带短裤背面",
            "CompositeElements": [
                {
                    "desc": "从对应品牌中筛选出短裤背面",
                    "type": "bibShorts",
                    "fileNamePattern": r'(\d+)_1\.png',
                    "zOrder": 0,
                    "scale": 1,
                    "pos": [400, 400],
                },
            ],
            "outputJpgFileName": "{0}_1", 
        },
        "e": { 
            "desc": "无背带短裤背面",
            "CompositeElements": [
                {
                    "desc": "无背带短裤背面",
                    "type": "shorts",
                    "fileNamePattern": r'(\d+)_1\.png',
                    "zOrder": 0,
                    "scale": 1,
                    "pos": [400, 400],
                },
            ],
            "outputJpgFileName": "{0}_1", 
        },

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
                    "pos": [400, 400],
                }
            ],
            "outputJpgFileName": "{0}_0", 
        },
        "a1": { 
            "desc": "无背带长裤",
            "CompositeElements": [
                # 合成部分
                {
                    "desc": "无背带长裤",
                    "type": "pants",
                    "fileNamePattern": r'(\d+)_1\.png',
                    "zOrder": 0,
                    "scale": 1.0,
                    "pos": [400, 400],
                }
            ],
            "outputJpgFileName": "{0}_0", 
        },
        "a2": { 
            "desc": "背带长裤",
            "CompositeElements": [
                # 合成部分
                {
                    "desc": "无背带长裤",
                    "type": "bibPants",
                    "fileNamePattern": r'(\d+)_1\.png',
                    "zOrder": 0,
                    "scale": 1.0,
                    "pos": [400, 400],
                }
            ],
            "outputJpgFileName": "{0}_0", 
        },
        "a3": { 
            "desc": "长袖上衣正反面",
            "CompositeElements": [
                # 合成部分
                {
                    "desc": "从对应品牌中筛选出长袖上衣背面",
                    "type": "longShirts",
                    "fileNamePattern": r'(\d+)_1\.png',
                    "zOrder": 0,
                    "scale": 0.78,
                    "pos": [530, 300],
                },
                {
                    "desc": "从对应品牌中筛选出长袖上衣正面",
                    "type": "longShirts",
                    "fileNamePattern": r'(\d+)_0\.png',
                    "zOrder": 1,
                    "scale": 0.82,
                    "pos": [270, 500],
                }
            ],
            "sameIndexGroups": [[0, 1]],
            "outputJpgFileName": "长袖上衣正反面", 
        },
        "a4": { 
            "desc": "长袖上衣正反面加无背带裤子背面",
            "CompositeElements": [
                # 合成部分
                {
                    "desc": "从对应品牌中筛选出长袖上衣背面",
                    "type": "longShirts",
                    "fileNamePattern": r'(\d+)_1\.png',
                    "zOrder": 0,
                    "scale": 0.78,
                    "pos": [530, 300],
                },
                {
                    "desc": "从对应品牌中筛选出长袖上衣正面",
                    "type": "longShirts",
                    "fileNamePattern": r'(\d+)_0\.png',
                    "zOrder": 1,
                    "scale": 0.82,
                    "pos": [270, 500],
                },
                {
                    "desc": "从对应品牌中筛选出无背带长裤背面",
                    "type": "pants", # 对应 SingleGoodsPngObj 中的一个类型或者shirts文件夹名，output中用用shirts的子文件夹名进行分文件夹
                    "fileNamePattern": r'(\d+)_1\.png',
                    "zOrder": 0, # 合图时候的顺序，数字越小越在下面，反之则越在上面，默认是和key一样
                    "scale": 0.6,
                    "pos": [639, 566],
                }
            ],
            "sameIndexGroups": [[0, 1]],
            "outputJpgFileName": "长袖上衣正反面加无背带裤子背面", 
        },
        "a5": { 
            "desc": "长袖上衣正反面加有背带裤子背面",
            "CompositeElements": [
                # 合成部分
                {
                    "desc": "从对应品牌中筛选出长袖上衣背面",
                    "type": "longShirts",
                    "fileNamePattern": r'(\d+)_1\.png',
                    "zOrder": 0,
                    "scale": 0.78,
                    "pos": [530, 300],
                },
                {
                    "desc": "从对应品牌中筛选出长袖上衣正面",
                    "type": "longShirts",
                    "fileNamePattern": r'(\d+)_0\.png',
                    "zOrder": 1,
                    "scale": 0.82,
                    "pos": [270, 500],
                },
                {
                    "desc": "从对应品牌中筛选出背带长裤背面",
                    "type": "bibPants", # 对应 SingleGoodsPngObj 中的一个类型或者shirts文件夹名，output中用用shirts的子文件夹名进行分文件夹
                    "fileNamePattern": r'(\d+)_1\.png',
                    "zOrder": 0, # 合图时候的顺序，数字越小越在下面，反之则越在上面，默认是和key一样
                    "scale": 0.6,
                    "pos": [631, 540],
                }
            ],
            "sameIndexGroups": [[0, 1]],
            "outputJpgFileName": "长袖上衣正反面加有背带裤子背面", 
        },
        "a6": { 
            "desc": "长袖正反面加背带裤子背面",
            "CompositeElements": [
                # 合成部分
                {
                    "desc": "从对应品牌中筛选出长袖上衣背面",
                    "type": "longShirts",
                    "fileNamePattern": r'(\d+)_1\.png',
                    "zOrder": 0,
                    "scale": 0.82,
                    "pos": [457, 304],
                },
                {
                    "desc": "从对应品牌中筛选出长袖上衣正面",
                    "type": "longShirts",
                    "fileNamePattern": r'(\d+)_0\.png',
                    "zOrder": 1,
                    "scale": 0.82,
                    "pos": [246, 476],
                },
                {
                    "desc": "从对应品牌中筛选出背带长裤背面",
                    "type": "bibPants", # 对应 SingleGoodsPngObj 中的一个类型或者shirts文件夹名，output中用用shirts的子文件夹名进行分文件夹
                    "fileNamePattern": r'(\d+)_1\.png',
                    "zOrder": 0, # 合图时候的顺序，数字越小越在下面，反之则越在上面，默认是和key一样
                    "scale": 0.67,
                    "pos": [672, 546],
                }
            ],
            "sameIndexGroups": [[0, 1]],
            "outputJpgFileName": "长袖正反面加背带裤子背面", 
        },
        "a7": { 
            "desc": "两件长袖正面加背带裤背面",
            "CompositeElements": [
                # 合成部分
                {
                    "desc": "从对应品牌中筛选出长袖上衣正面",
                    "type": "longShirts",
                    "fileNamePattern": r'(\d+)_0\.png',
                    "zOrder": 1,
                    "scale": 0.768,
                    "pos": [422, 314],
                },
                {
                    "desc": "从对应品牌中筛选出长袖上衣正面",
                    "type": "longShirts", # 对应 SingleGoodsPngObj 中的一个类型或者shirts文件夹名，output中用用shirts的子文件夹名进行分文件夹
                    "fileNamePattern": r'(\d+)_0\.png',
                    "zOrder": 2, # 合图时候的顺序，数字越小越在下面，反之则越在上面，默认是和key一样
                    "scale": 0.768,
                    "pos": [225, 505],
                },
                {
                    "desc": "从对应品牌中筛选出背带长裤背面",
                    "type": "bibPants", # 对应 SingleGoodsPngObj 中的一个类型或者shirts文件夹名，output中用用shirts的子文件夹名进行分文件夹
                    "fileNamePattern": r'(\d+)_1\.png',
                    "zOrder": 0, # 合图时候的顺序，数字越小越在下面，反之则越在上面，默认是和key一样
                    "scale": 1.02,
                    "pos": [655, 375],
                }
            ],
            "distinctIndexGroups": [[0, 1]],
            "outputJpgFileName": "两件长袖正面加背带裤背面", 
        },
        "a8": { 
            "desc": "两件长袖正面加无背带裤背面",
            "CompositeElements": [
                # 合成部分
                {
                    "desc": "从对应品牌中筛选出长袖上衣正面",
                    "type": "longShirts",
                    "fileNamePattern": r'(\d+)_0\.png',
                    "zOrder": 1,
                    "scale": 0.768,
                    "pos": [422, 314],
                },
                {
                    "desc": "从对应品牌中筛选出长袖上衣正面",
                    "type": "longShirts", # 对应 SingleGoodsPngObj 中的一个类型或者shirts文件夹名，output中用用shirts的子文件夹名进行分文件夹
                    "fileNamePattern": r'(\d+)_0\.png',
                    "zOrder": 2, # 合图时候的顺序，数字越小越在下面，反之则越在上面，默认是和key一样
                    "scale": 0.768,
                    "pos": [225, 505],
                },
                {
                    "desc": "从对应品牌中筛选出无背带长裤背面",
                    "type": "pants", # 对应 SingleGoodsPngObj 中的一个类型或者shirts文件夹名，output中用用shirts的子文件夹名进行分文件夹
                    "fileNamePattern": r'(\d+)_1\.png',
                    "zOrder": 0, # 合图时候的顺序，数字越小越在下面，反之则越在上面，默认是和key一样
                    "scale": 0.88,
                    "pos": [667, 429],
                }
            ],
            "distinctIndexGroups": [[0, 1]],
            "outputJpgFileName": "两件长袖正面加无背带裤背面", 
        },
        "a9": { 
            "desc": "三件长袖正面无背带裤背面两款有背带裤背面",
            "CompositeElements": [
                {
                    "desc": "从对应品牌中筛选出长袖上衣正面",
                    "type": "longShirts",
                    "fileNamePattern": r'(\d+)_0\.png',
                    "zOrder": 0,
                    "scale": 0.733,
                    "pos": [216, 285],
                },
                {
                    "desc": "从对应品牌中筛选出长袖上衣正面",
                    "type": "longShirts",
                    "fileNamePattern": r'(\d+)_0\.png',
                    "zOrder": 1,
                    "scale": 0.733,
                    "pos": [419, 388],
                },
                {
                    "desc": "从对应品牌中筛选出长袖上衣正面",
                    "type": "longShirts",
                    "fileNamePattern": r'(\d+)_0\.png',
                    "zOrder": 2,
                    "scale": 0.733,
                    "pos": [594, 539],
                },
                {
                    "desc": "从对应品牌中筛选出无背带长裤背面",
                    "type": "pants", # 对应 SingleGoodsPngObj 中的一个类型或者shirts文件夹名，output中用用shirts的子文件夹名进行分文件夹
                    "fileNamePattern": r'(\d+)_1\.png',
                    "zOrder": 3, # 合图时候的顺序，数字越小越在下面，反之则越在上面，默认是和key一样
                    "scale": 0.53,
                    "pos": [96, 597],
                },
                {
                    "desc": "从对应品牌中筛选出背带长裤背面",
                    "type": "bibPants", # 对应 SingleGoodsPngObj 中的一个类型或者shirts文件夹名，output中用用shirts的子文件夹名进行分文件夹
                    "fileNamePattern": r'(\d+)_1\.png',
                    "zOrder": 4, # 合图时候的顺序，数字越小越在下面，反之则越在上面，默认是和key一样
                    "scale": 0.588,
                    "pos": [229, 566],
                },
                {
                    "desc": "从对应品牌中筛选出背带长裤背面",
                    "type": "bibPants", # 对应 SingleGoodsPngObj 中的一个类型或者shirts文件夹名，output中用用shirts的子文件夹名进行分文件夹
                    "fileNamePattern": r'(\d+)_1\.png',
                    "zOrder": 5, # 合图时候的顺序，数字越小越在下面，反之则越在上面，默认是和key一样
                    "scale": 0.588,
                    "pos": [355, 566],
                }
            ],
            "distinctIndexGroups": [[0, 1, 2], [4, 5]],
            "outputJpgFileName": "三件长袖正面无背带裤背面两款有背带裤背面", 
        },
        "a10": { 
            "desc": "四件长袖正面两款有背带裤背面",
            "CompositeElements": [
                {
                    "desc": "从对应品牌中筛选出长袖上衣正面",
                    "type": "longShirts",
                    "fileNamePattern": r'(\d+)_0\.png',
                    "zOrder": 0,
                    "scale": 0.685,
                    "pos": [590, 263],
                },
                {
                    "desc": "从对应品牌中筛选出长袖上衣正面",
                    "type": "longShirts",
                    "fileNamePattern": r'(\d+)_0\.png',
                    "zOrder": 1,
                    "scale": 0.685,
                    "pos": [476, 352],
                },
                {
                    "desc": "从对应品牌中筛选出长袖上衣正面",
                    "type": "longShirts",
                    "fileNamePattern": r'(\d+)_0\.png',
                    "zOrder": 2,
                    "scale": 0.685,
                    "pos": [359, 451],
                },
                {
                    "desc": "从对应品牌中筛选出长袖上衣正面",
                    "type": "longShirts",
                    "fileNamePattern": r'(\d+)_0\.png',
                    "zOrder": 2,
                    "scale": 0.685,
                    "pos": [221, 549],
                },
                {
                    "desc": "从对应品牌中筛选出背带长裤背面",
                    "type": "bibPants", # 对应 SingleGoodsPngObj 中的一个类型或者shirts文件夹名，output中用用shirts的子文件夹名进行分文件夹
                    "fileNamePattern": r'(\d+)_1\.png',
                    "zOrder": 4, # 合图时候的顺序，数字越小越在下面，反之则越在上面，默认是和key一样
                    "scale": 0.623,
                    "pos": [697, 553],
                },
                {
                    "desc": "从对应品牌中筛选出背带长裤背面",
                    "type": "bibPants", # 对应 SingleGoodsPngObj 中的一个类型或者shirts文件夹名，output中用用shirts的子文件夹名进行分文件夹
                    "fileNamePattern": r'(\d+)_1\.png',
                    "zOrder": 5, # 合图时候的顺序，数字越小越在下面，反之则越在上面，默认是和key一样
                    "scale": 0.623,
                    "pos": [550, 554],
                }
            ],
            "distinctIndexGroups": [[0, 1, 2, 3], [4, 5]],
            "outputJpgFileName": "四件长袖正面两款有背带裤背面", 
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
                    "pos": [290, 399],
                },
                {
                    "desc": "从对应品牌中筛选出无背带长裤背面",
                    "type": "pants", # 对应 SingleGoodsPngObj 中的一个类型或者shirts文件夹名，output中用用shirts的子文件夹名进行分文件夹
                    "fileNamePattern": r'(\d+)_1\.png',
                    "zOrder": 0, # 合图时候的顺序，数字越小越在下面，反之则越在上面，默认是和key一样
                    "scale": 0.806,
                    "pos": [664, 437],
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
                    "pos": [290, 399],
                },
                {
                    "desc": "从对应品牌中筛选出长背带裤裤背面",
                    "type": "bibPants",
                    "fileNamePattern": r'(\d+)_1\.png',
                    "zOrder": 0,
                    "scale": 0.869,
                    "pos": [664, 400],
                },
            ],
            "outputJpgFileName": "{0}_{1}", 
        },
        "d": { 
            "desc": "单款7颜色以上的主图",
            "CompositeElements": [
                # 合成部分
                {
                    "desc": "从对应品牌中筛选出长袖袖上衣",
                    "type": "longShirts",
                    "fileNamePattern": r'1_0\.png',
                    "zOrder": 0,
                    "scale": 0.6,
                    "pos": [638, 258],
                },
                {
                    "desc": "从对应品牌中筛选出长袖袖上衣",
                    "type": "longShirts",
                    "fileNamePattern": r'2_0\.png',
                    "zOrder": 0,
                    "scale": 0.6,
                    "pos": [563, 303],
                },{
                    "desc": "从对应品牌中筛选出长袖袖上衣",
                    "type": "longShirts",
                    "fileNamePattern": r'3_0\.png',
                    "zOrder": 0,
                    "scale": 0.6,
                    "pos": [496, 347],
                },
                {
                    "desc": "从对应品牌中筛选出长袖袖上衣",
                    "type": "longShirts",
                    "fileNamePattern": r'4_0\.png',
                    "zOrder": 0,
                    "scale": 0.6,
                    "pos": [424, 390],
                },{
                    "desc": "从对应品牌中筛选出长袖袖上衣",
                    "type": "longShirts",
                    "fileNamePattern": r'5_0\.png',
                    "zOrder": 0,
                    "scale": 0.6,
                    "pos": [352, 444],
                },{
                    "desc": "从对应品牌中筛选出长袖袖上衣",
                    "type": "longShirts",
                    "fileNamePattern": r'6_0\.png',
                    "zOrder": 0,
                    "scale": 0.6,
                    "pos": [248, 496],
                },{
                    "desc": "从对应品牌中筛选出长袖袖上衣",
                    "type": "longShirts",
                    "fileNamePattern": r'7_0\.png',
                    "zOrder": 0,
                    "scale": 0.6,
                    "pos": [176, 559],
                },
                {
                    "desc": "从对应品牌中筛选出长背带裤裤背面",
                    "type": "bibPants",
                    "fileNamePattern": r'1_1\.png',
                    "zOrder": 0,
                    "scale": 0.326,
                    "pos": [234, 134],
                },
                {
                    "desc": "从对应品牌中筛选出长背带裤裤背面",
                    "type": "bibPants",
                    "fileNamePattern": r'2_1\.png',
                    "zOrder": 0,
                    "scale": 0.326,
                    "pos": [140, 134],
                },
                {
                    "desc": "从对应品牌中筛选出长背带裤裤背面",
                    "type": "pants",
                    "fileNamePattern": r'1_1\.png',
                    "zOrder": 0,
                    "scale": 0.265,
                    "pos": [683, 678],
                }
            ],
            "outputJpgFileName": "main", 
        },
        "e": { 
            "desc": "单款3颜色以上的主图",
            "CompositeElements": [
                # 合成部分
                {
                    "desc": "从对应品牌中筛选出长袖袖上衣",
                    "type": "longShirts",
                    "fileNamePattern": r'3_0\.png',
                    "zOrder": 0,
                    "scale": 0.8,
                    "pos": [550, 309],
                },
                {
                    "desc": "从对应品牌中筛选出长袖袖上衣",
                    "type": "longShirts",
                    "fileNamePattern": r'2_0\.png',
                    "zOrder": 0,
                    "scale": 0.8,
                    "pos": [399, 388],
                },{
                    "desc": "从对应品牌中筛选出长袖袖上衣",
                    "type": "longShirts",
                    "fileNamePattern": r'1_0\.png',
                    "zOrder": 0,
                    "scale": 0.8,
                    "pos": [229, 467],
                }
            ],
            "outputJpgFileName": "main", 
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
                    "pos": [400, 400],
                },
                {
                    "desc": "抓绒左上挂件",
                    "type": "commonPng",
                    "fileNamePattern": r'WinterLeftTop1\.png',
                    "zOrder": 0,
                    "scale": 0.732,
                    "pos": [78, 110],
                }
            ],
            "outputJpgFileName": "winter/{0}_0", 
        },
        "a1": { 
            "desc": "无背带长裤",
            "CompositeElements": [
                # 合成部分
                {
                    "desc": "无背带长裤",
                    "type": "pants",
                    "fileNamePattern": r'(\d+)_1\.png',
                    "zOrder": 0,
                    "scale": 1.0,
                    "pos": [400, 400],
                },
                {
                    "desc": "抓绒左上挂件",
                    "type": "commonPng",
                    "fileNamePattern": r'WinterLeftTop1\.png',
                    "zOrder": 0,
                    "scale": 0.732,
                    "pos": [78, 110],
                }
            ],
            "outputJpgFileName": "winter/{0}_0", 
        },
        "a2": { 
            "desc": "背带长裤",
            "CompositeElements": [
                # 合成部分
                {
                    "desc": "无背带长裤",
                    "type": "bibPants",
                    "fileNamePattern": r'(\d+)_1\.png',
                    "zOrder": 0,
                    "scale": 1.0,
                    "pos": [400, 400],
                },
                {
                    "desc": "抓绒左上挂件",
                    "type": "commonPng",
                    "fileNamePattern": r'WinterLeftTop1\.png',
                    "zOrder": 0,
                    "scale": 0.732,
                    "pos": [78, 110],
                }
            ],
            "outputJpgFileName": "winter/{0}_0", 
        },
        "a3": { 
            "desc": "长袖上衣正反面",
            "CompositeElements": [
                # 合成部分
                {
                    "desc": "从对应品牌中筛选出长袖上衣背面",
                    "type": "longShirts",
                    "fileNamePattern": r'(\d+)_1\.png',
                    "zOrder": 0,
                    "scale": 0.78,
                    "pos": [530, 300],
                },
                {
                    "desc": "从对应品牌中筛选出长袖上衣正面",
                    "type": "longShirts",
                    "fileNamePattern": r'(\d+)_0\.png',
                    "zOrder": 1,
                    "scale": 0.82,
                    "pos": [270, 500],
                },
                {
                    "desc": "抓绒左上挂件",
                    "type": "commonPng",
                    "fileNamePattern": r'WinterLeftTop1\.png',
                    "zOrder": 0,
                    "scale": 0.732,
                    "pos": [78, 110],
                }
            ],
            "sameIndexGroups": [[0, 1]],
            "outputJpgFileName": "winter/长袖上衣正反面", 
        },
        "a4": { 
            "desc": "长袖上衣正反面加无背带裤子背面",
            "CompositeElements": [
                # 合成部分
                {
                    "desc": "从对应品牌中筛选出长袖上衣背面",
                    "type": "longShirts",
                    "fileNamePattern": r'(\d+)_1\.png',
                    "zOrder": 0,
                    "scale": 0.78,
                    "pos": [530, 300],
                },
                {
                    "desc": "从对应品牌中筛选出长袖上衣正面",
                    "type": "longShirts",
                    "fileNamePattern": r'(\d+)_0\.png',
                    "zOrder": 1,
                    "scale": 0.82,
                    "pos": [270, 500],
                },
                {
                    "desc": "从对应品牌中筛选出无背带长裤背面",
                    "type": "pants", # 对应 SingleGoodsPngObj 中的一个类型或者shirts文件夹名，output中用用shirts的子文件夹名进行分文件夹
                    "fileNamePattern": r'(\d+)_1\.png',
                    "zOrder": 0, # 合图时候的顺序，数字越小越在下面，反之则越在上面，默认是和key一样
                    "scale": 0.6,
                    "pos": [639, 566],
                },
                {
                    "desc": "抓绒左上挂件",
                    "type": "commonPng",
                    "fileNamePattern": r'WinterLeftTop1\.png',
                    "zOrder": 0,
                    "scale": 0.732,
                    "pos": [78, 110],
                }
            ],
            "sameIndexGroups": [[0, 1]],
            "outputJpgFileName": "winter/长袖上衣正反面加无背带裤子背面", 
        },
        "a5": { 
            "desc": "长袖上衣正反面加有背带裤子背面",
            "CompositeElements": [
                # 合成部分
                {
                    "desc": "从对应品牌中筛选出长袖上衣背面",
                    "type": "longShirts",
                    "fileNamePattern": r'(\d+)_1\.png',
                    "zOrder": 0,
                    "scale": 0.78,
                    "pos": [530, 300],
                },
                {
                    "desc": "从对应品牌中筛选出长袖上衣正面",
                    "type": "longShirts",
                    "fileNamePattern": r'(\d+)_0\.png',
                    "zOrder": 1,
                    "scale": 0.82,
                    "pos": [270, 500],
                },
                {
                    "desc": "从对应品牌中筛选出背带长裤背面",
                    "type": "bibPants", # 对应 SingleGoodsPngObj 中的一个类型或者shirts文件夹名，output中用用shirts的子文件夹名进行分文件夹
                    "fileNamePattern": r'(\d+)_1\.png',
                    "zOrder": 0, # 合图时候的顺序，数字越小越在下面，反之则越在上面，默认是和key一样
                    "scale": 0.6,
                    "pos": [631, 540],
                },
                {
                    "desc": "抓绒左上挂件",
                    "type": "commonPng",
                    "fileNamePattern": r'WinterLeftTop1\.png',
                    "zOrder": 0,
                    "scale": 0.732,
                    "pos": [78, 110],
                }
            ],
            "sameIndexGroups": [[0, 1]],
            "outputJpgFileName": "winter/长袖上衣正反面加有背带裤子背面", 
        },
        "a6": { 
            "desc": "长袖正反面加背带裤子背面",
            "CompositeElements": [
                # 合成部分
                {
                    "desc": "从对应品牌中筛选出长袖上衣背面",
                    "type": "longShirts",
                    "fileNamePattern": r'(\d+)_1\.png',
                    "zOrder": 0,
                    "scale": 0.82,
                    "pos": [457, 304],
                },
                {
                    "desc": "从对应品牌中筛选出长袖上衣正面",
                    "type": "longShirts",
                    "fileNamePattern": r'(\d+)_0\.png',
                    "zOrder": 1,
                    "scale": 0.82,
                    "pos": [246, 476],
                },
                {
                    "desc": "从对应品牌中筛选出背带长裤背面",
                    "type": "bibPants", # 对应 SingleGoodsPngObj 中的一个类型或者shirts文件夹名，output中用用shirts的子文件夹名进行分文件夹
                    "fileNamePattern": r'(\d+)_1\.png',
                    "zOrder": 0, # 合图时候的顺序，数字越小越在下面，反之则越在上面，默认是和key一样
                    "scale": 0.67,
                    "pos": [672, 546],
                },
                {
                    "desc": "抓绒左上挂件",
                    "type": "commonPng",
                    "fileNamePattern": r'WinterLeftTop1\.png',
                    "zOrder": 0,
                    "scale": 0.732,
                    "pos": [78, 110],
                }
            ],
            "sameIndexGroups": [[0, 1]],
            "outputJpgFileName": "winter/长袖正反面加背带裤子背面", 
        },
        "a7": { 
            "desc": "两件长袖正面加背带裤背面",
            "CompositeElements": [
                # 合成部分
                {
                    "desc": "从对应品牌中筛选出长袖上衣正面",
                    "type": "longShirts",
                    "fileNamePattern": r'(\d+)_0\.png',
                    "zOrder": 1,
                    "scale": 0.768,
                    "pos": [422, 314],
                },
                {
                    "desc": "从对应品牌中筛选出长袖上衣正面",
                    "type": "longShirts", # 对应 SingleGoodsPngObj 中的一个类型或者shirts文件夹名，output中用用shirts的子文件夹名进行分文件夹
                    "fileNamePattern": r'(\d+)_0\.png',
                    "zOrder": 2, # 合图时候的顺序，数字越小越在下面，反之则越在上面，默认是和key一样
                    "scale": 0.768,
                    "pos": [225, 505],
                },
                {
                    "desc": "从对应品牌中筛选出背带长裤背面",
                    "type": "bibPants", # 对应 SingleGoodsPngObj 中的一个类型或者shirts文件夹名，output中用用shirts的子文件夹名进行分文件夹
                    "fileNamePattern": r'(\d+)_1\.png',
                    "zOrder": 0, # 合图时候的顺序，数字越小越在下面，反之则越在上面，默认是和key一样
                    "scale": 1.02,
                    "pos": [655, 375],
                },
                {
                    "desc": "抓绒左上挂件",
                    "type": "commonPng",
                    "fileNamePattern": r'WinterLeftTop1\.png',
                    "zOrder": 3,
                    "scale": 0.732,
                    "pos": [78, 110],
                }
            ],
            "distinctIndexGroups": [[0, 1]],
            "outputJpgFileName": "winter/两件长袖正面加背带裤背面", 
        },
        "a8": { 
            "desc": "两件长袖正面加无背带裤背面",
            "CompositeElements": [
                # 合成部分
                {
                    "desc": "从对应品牌中筛选出长袖上衣正面",
                    "type": "longShirts",
                    "fileNamePattern": r'(\d+)_0\.png',
                    "zOrder": 1,
                    "scale": 0.768,
                    "pos": [422, 314],
                },
                {
                    "desc": "从对应品牌中筛选出长袖上衣正面",
                    "type": "longShirts", # 对应 SingleGoodsPngObj 中的一个类型或者shirts文件夹名，output中用用shirts的子文件夹名进行分文件夹
                    "fileNamePattern": r'(\d+)_0\.png',
                    "zOrder": 2, # 合图时候的顺序，数字越小越在下面，反之则越在上面，默认是和key一样
                    "scale": 0.768,
                    "pos": [225, 505],
                },
                {
                    "desc": "从对应品牌中筛选出无背带长裤背面",
                    "type": "pants", # 对应 SingleGoodsPngObj 中的一个类型或者shirts文件夹名，output中用用shirts的子文件夹名进行分文件夹
                    "fileNamePattern": r'(\d+)_1\.png',
                    "zOrder": 0, # 合图时候的顺序，数字越小越在下面，反之则越在上面，默认是和key一样
                    "scale": 0.88,
                    "pos": [667, 429],
                },
                {
                    "desc": "抓绒左上挂件",
                    "type": "commonPng",
                    "fileNamePattern": r'WinterLeftTop1\.png',
                    "zOrder": 3,
                    "scale": 0.732,
                    "pos": [78, 110],
                }
            ],
            "distinctIndexGroups": [[0, 1]],
            "outputJpgFileName": "winter/两件长袖正面加无背带裤背面", 
        },
        "a9": { 
            "desc": "三件长袖正面无背带裤背面两款有背带裤背面",
            "CompositeElements": [
                {
                    "desc": "从对应品牌中筛选出长袖上衣正面",
                    "type": "longShirts",
                    "fileNamePattern": r'(\d+)_0\.png',
                    "zOrder": 0,
                    "scale": 0.733,
                    "pos": [216, 285],
                },
                {
                    "desc": "从对应品牌中筛选出长袖上衣正面",
                    "type": "longShirts",
                    "fileNamePattern": r'(\d+)_0\.png',
                    "zOrder": 1,
                    "scale": 0.733,
                    "pos": [419, 388],
                },
                {
                    "desc": "从对应品牌中筛选出长袖上衣正面",
                    "type": "longShirts",
                    "fileNamePattern": r'(\d+)_0\.png',
                    "zOrder": 2,
                    "scale": 0.733,
                    "pos": [594, 539],
                },
                {
                    "desc": "从对应品牌中筛选出无背带长裤背面",
                    "type": "pants", # 对应 SingleGoodsPngObj 中的一个类型或者shirts文件夹名，output中用用shirts的子文件夹名进行分文件夹
                    "fileNamePattern": r'(\d+)_1\.png',
                    "zOrder": 3, # 合图时候的顺序，数字越小越在下面，反之则越在上面，默认是和key一样
                    "scale": 0.53,
                    "pos": [96, 597],
                },
                {
                    "desc": "从对应品牌中筛选出背带长裤背面",
                    "type": "bibPants", # 对应 SingleGoodsPngObj 中的一个类型或者shirts文件夹名，output中用用shirts的子文件夹名进行分文件夹
                    "fileNamePattern": r'(\d+)_1\.png',
                    "zOrder": 4, # 合图时候的顺序，数字越小越在下面，反之则越在上面，默认是和key一样
                    "scale": 0.588,
                    "pos": [229, 566],
                },
                {
                    "desc": "从对应品牌中筛选出背带长裤背面",
                    "type": "bibPants", # 对应 SingleGoodsPngObj 中的一个类型或者shirts文件夹名，output中用用shirts的子文件夹名进行分文件夹
                    "fileNamePattern": r'(\d+)_1\.png',
                    "zOrder": 5, # 合图时候的顺序，数字越小越在下面，反之则越在上面，默认是和key一样
                    "scale": 0.588,
                    "pos": [355, 566],
                },
                {
                    "desc": "抓绒左上挂件",
                    "type": "commonPng",
                    "fileNamePattern": r'WinterLeftTop1\.png',
                    "zOrder": 6,
                    "scale": 0.732,
                    "pos": [78, 110],
                }
            ],
            "distinctIndexGroups": [[0, 1, 2], [4, 5]],
            "outputJpgFileName": "winter/三件长袖正面无背带裤背面两款有背带裤背面", 
        },
        "a10": { 
            "desc": "四件长袖正面两款有背带裤背面",
            "CompositeElements": [
                {
                    "desc": "从对应品牌中筛选出长袖上衣正面",
                    "type": "longShirts",
                    "fileNamePattern": r'(\d+)_0\.png',
                    "zOrder": 0,
                    "scale": 0.685,
                    "pos": [590, 263],
                },
                {
                    "desc": "从对应品牌中筛选出长袖上衣正面",
                    "type": "longShirts",
                    "fileNamePattern": r'(\d+)_0\.png',
                    "zOrder": 1,
                    "scale": 0.685,
                    "pos": [476, 352],
                },
                {
                    "desc": "从对应品牌中筛选出长袖上衣正面",
                    "type": "longShirts",
                    "fileNamePattern": r'(\d+)_0\.png',
                    "zOrder": 2,
                    "scale": 0.685,
                    "pos": [359, 451],
                },
                {
                    "desc": "从对应品牌中筛选出长袖上衣正面",
                    "type": "longShirts",
                    "fileNamePattern": r'(\d+)_0\.png',
                    "zOrder": 2,
                    "scale": 0.685,
                    "pos": [221, 549],
                },
                {
                    "desc": "从对应品牌中筛选出背带长裤背面",
                    "type": "bibPants", # 对应 SingleGoodsPngObj 中的一个类型或者shirts文件夹名，output中用用shirts的子文件夹名进行分文件夹
                    "fileNamePattern": r'(\d+)_1\.png',
                    "zOrder": 4, # 合图时候的顺序，数字越小越在下面，反之则越在上面，默认是和key一样
                    "scale": 0.623,
                    "pos": [697, 553],
                },
                {
                    "desc": "从对应品牌中筛选出背带长裤背面",
                    "type": "bibPants", # 对应 SingleGoodsPngObj 中的一个类型或者shirts文件夹名，output中用用shirts的子文件夹名进行分文件夹
                    "fileNamePattern": r'(\d+)_1\.png',
                    "zOrder": 5, # 合图时候的顺序，数字越小越在下面，反之则越在上面，默认是和key一样
                    "scale": 0.623,
                    "pos": [550, 554],
                },
                {
                    "desc": "抓绒左上挂件",
                    "type": "commonPng",
                    "fileNamePattern": r'WinterLeftTop1\.png',
                    "zOrder": 6,
                    "scale": 0.732,
                    "pos": [78, 110],
                }
            ],
            "distinctIndexGroups": [[0, 1, 2, 3], [4, 5]],
            "outputJpgFileName": "winter/四件长袖正面两款有背带裤背面", 
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
                    "pos": [290, 399],
                },
                {
                    "desc": "从对应品牌中筛选出无背带长裤背面",
                    "type": "pants", # 对应 SingleGoodsPngObj 中的一个类型或者shirts文件夹名，output中用用shirts的子文件夹名进行分文件夹
                    "fileNamePattern": r'(\d+)_1\.png',
                    "zOrder": 0, # 合图时候的顺序，数字越小越在下面，反之则越在上面，默认是和key一样
                    "scale": 0.806,
                    "pos": [664, 437],
                },
                {
                    "desc": "抓绒左上挂件",
                    "type": "commonPng",
                    "fileNamePattern": r'WinterLeftTop1\.png',
                    "zOrder": 0,
                    "scale": 0.732,
                    "pos": [78, 110],
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
                    "pos": [290, 399],
                },
                {
                    "desc": "从对应品牌中筛选出长背带裤裤背面",
                    "type": "bibPants",
                    "fileNamePattern": r'(\d+)_1\.png',
                    "zOrder": 0,
                    "scale": 0.869,
                    "pos": [664, 400],
                },
                {
                    "desc": "抓绒左上挂件",
                    "type": "commonPng",
                    "fileNamePattern": r'WinterLeftTop1\.png',
                    "zOrder": 0,
                    "scale": 0.732,
                    "pos": [78, 110],
                }
            ],
            "outputJpgFileName": "winter/{0}_{1}", 
        },
        "d": { 
            "desc": "单款7颜色以上的主图",
            "CompositeElements": [
                # 合成部分
                {
                    "desc": "从对应品牌中筛选出长袖袖上衣",
                    "type": "longShirts",
                    "fileNamePattern": r'1_0\.png',
                    "zOrder": 0,
                    "scale": 0.6,
                    "pos": [638, 258],
                },
                {
                    "desc": "从对应品牌中筛选出长袖袖上衣",
                    "type": "longShirts",
                    "fileNamePattern": r'2_0\.png',
                    "zOrder": 0,
                    "scale": 0.6,
                    "pos": [563, 303],
                },{
                    "desc": "从对应品牌中筛选出长袖袖上衣",
                    "type": "longShirts",
                    "fileNamePattern": r'3_0\.png',
                    "zOrder": 0,
                    "scale": 0.6,
                    "pos": [496, 347],
                },
                {
                    "desc": "从对应品牌中筛选出长袖袖上衣",
                    "type": "longShirts",
                    "fileNamePattern": r'4_0\.png',
                    "zOrder": 0,
                    "scale": 0.6,
                    "pos": [424, 390],
                },{
                    "desc": "从对应品牌中筛选出长袖袖上衣",
                    "type": "longShirts",
                    "fileNamePattern": r'5_0\.png',
                    "zOrder": 0,
                    "scale": 0.6,
                    "pos": [352, 444],
                },{
                    "desc": "从对应品牌中筛选出长袖袖上衣",
                    "type": "longShirts",
                    "fileNamePattern": r'6_0\.png',
                    "zOrder": 0,
                    "scale": 0.6,
                    "pos": [248, 496],
                },{
                    "desc": "从对应品牌中筛选出长袖袖上衣",
                    "type": "longShirts",
                    "fileNamePattern": r'7_0\.png',
                    "zOrder": 0,
                    "scale": 0.6,
                    "pos": [176, 559],
                },
                {
                    "desc": "从对应品牌中筛选出长背带裤裤背面",
                    "type": "bibPants",
                    "fileNamePattern": r'1_1\.png',
                    "zOrder": 0,
                    "scale": 0.326,
                    "pos": [234, 134],
                },
                {
                    "desc": "从对应品牌中筛选出长背带裤裤背面",
                    "type": "bibPants",
                    "fileNamePattern": r'2_1\.png',
                    "zOrder": 0,
                    "scale": 0.326,
                    "pos": [140, 134],
                },
                {
                    "desc": "从对应品牌中筛选出长背带裤裤背面",
                    "type": "pants",
                    "fileNamePattern": r'1_1\.png',
                    "zOrder": 0,
                    "scale": 0.265,
                    "pos": [683, 678],
                },
                {
                    "desc": "抓绒左上挂件",
                    "type": "commonPng",
                    "fileNamePattern": r'WinterLeftTop1\.png',
                    "zOrder": 0,
                    "scale": 0.5,
                    "pos": [60, 90],
                }
            ],
            "outputJpgFileName": "winter/main", 
        },
        "e": { 
            "desc": "单款3颜色以上的主图",
            "CompositeElements": [
                # 合成部分
                {
                    "desc": "从对应品牌中筛选出长袖袖上衣",
                    "type": "longShirts",
                    "fileNamePattern": r'3_0\.png',
                    "zOrder": 0,
                    "scale": 0.8,
                    "pos": [550, 309],
                },
                {
                    "desc": "从对应品牌中筛选出长袖袖上衣",
                    "type": "longShirts",
                    "fileNamePattern": r'2_0\.png',
                    "zOrder": 0,
                    "scale": 0.8,
                    "pos": [399, 388],
                },{
                    "desc": "从对应品牌中筛选出长袖袖上衣",
                    "type": "longShirts",
                    "fileNamePattern": r'1_0\.png',
                    "zOrder": 0,
                    "scale": 0.8,
                    "pos": [229, 467],
                },
                {
                    "desc": "抓绒左上挂件",
                    "type": "commonPng",
                    "fileNamePattern": r'WinterLeftTop1\.png',
                    "zOrder": 0,
                    "scale": 0.732,
                    "pos": [78, 110],
                }
            ],
            "outputJpgFileName": "winter/main", 
        }
    }
}


def trans(scale, xy):
    return [int(800*scale/2+xy[0]), int(800 - xy[1] - 800*scale/2)]


trans(1, [0, 0])
trans(1, [0, 0])
