# -*- coding: utf-8
#
# 全局变量声明
# author: Emirio
# date: 2021.07.14

import os

############################# 文件区 #############################
CURRENT_DIR = os.path.dirname(__file__) + "/"   # 当前脚本所在目录
FILE_NAME = "数据定标.xlsx"                       # 要导出的文件名
ABS_FILE_NAME = CURRENT_DIR + FILE_NAME         # 要导出的文件绝对路径
SHEET_NAME = "数据定标"                           # Sheet页名称

############################# 表头区 #############################
# 读取表格文件后只筛选如下几个字段的数据信息，避免读取无用数据浪费时间
FILTERED_TABLE_HEADER = ['单据类型', '区域', '字段名', '使用', '取值范围', '默认值', '约束', '安全级别', '参考标准类型']
BILL_TYPE_FLAG = "单据类型"
AREA_FLAG = "区域"
FIELD_NAME_FLAG = "字段名"
USAGE_FLAG = "使用"
VALUE_RANGE = "取值范围"
DEFAULT_VALUE = "默认值"
CONTRAINT_VALUE = "约束"
SECURITY_LEVEL = "安全级别"
REFERENCE_STANDARD = "参考标准类型"

############################# 数据区 #############################
# 存储各列对应的值
EDIT_DATE_LIST = []                 # 盘点日期
CODE_NUMBER_LIST = []               # 资产编号
ITEM_NAME_LIST = []                 # 数据项中文名称
ITEM_CODE_LIST = []                 # 数据项代码
ITEM_MEANING_LIST = []              # 数据项业务含义
AREA_NAME_LIST = []                 # 区域
DEPT_NAME_LIST = []                 # 归口管理部门
DATA_MANAGER_LIST = []              # 数据管家
MAINTAINANCE_METHOD_LIST = []       # 维护方式
CREATE_SOURCE_LIST = []             # 可信数据源
DISTRIBUTE_SOURCE_LIST = []         # 数据分布
DATA_TYPE_LIST = []                 # 数据类型
DATA_FORMAT_LIST = []               # 数据格式
VALUE_RANGE_LIST =[]                # 取值范围
FIELD_CONSTRAINT_LIST = []          # 字段约束
DEFAULT_VALUE_LIST = []             # 字段默认值
IS_INNERBOUND_LIST = []             # 是否入仓
THEME_AREA_LIST = []                # 主题域
SECURITY_LEVEL_LIST = []            # 安全级别
REFERENCE_STANDARD_LIST = []        # 参考标准

############################## 默认值 #############################
# 常用默认值
SERIAL_NO = "序号"                   # 序号
EDIT_DATE = ""                      # 盘点日期
AREA_NAME = ""                      # 区域
ITEM_MEANING = ""                   # 数据项业务含义
DEPT_NAME = "研发部"                 # 归口管理部门
DATA_MANAGER = "张小小"              # 数据管家
MAINTAINANCE_METHOD = "系统维护"     # 维护方式
DATA_TYPE = ""                      # 数据类型
DATA_FORMAT = ""                    # 数据格式
IS_INNERBOUND = "否"                # 是否入仓
THEME_AREA = ""                     # 主题域
CREATE_VALUE = "创建（C）"           # 可信数据源获取对象为创建（C）
HIDDEN_VALUE = "业务隐藏字段"         # 不统计业务隐藏字段区域

LEVEL_TWO = "LEVEL1"                # 默认安全级别为L2
MADE_BY_YQJR = "测试参考"             # 默认参考标准为我司实践

############################# 表格区 #############################
# 初始化pandas的DATAFRAME对象所用到的表格对象
DATA_TABLE = {
              "盘点日期": EDIT_DATE_LIST,
              "资产编号": CODE_NUMBER_LIST,
              "数据项中文名称": ITEM_NAME_LIST,
              "数据项代码": ITEM_CODE_LIST,
              "数据项业务含义": ITEM_MEANING_LIST,
              "区域": AREA_NAME_LIST,
              "归口管理部门": DEPT_NAME_LIST,
              "数据管家": DATA_MANAGER_LIST,
              "维护方式": MAINTAINANCE_METHOD,
              "可信数据源": CREATE_SOURCE_LIST,
              "数据分布": DISTRIBUTE_SOURCE_LIST,
              "数据类型": DATA_TYPE_LIST,
              "数据格式": DATA_FORMAT_LIST,
              "取值范围": DEFAULT_VALUE_LIST,
              "字段约束": FIELD_CONSTRAINT_LIST,
              "字段默认值": DEFAULT_VALUE_LIST,
              "是否入仓": IS_INNERBOUND_LIST,
              "主题域": THEME_AREA_LIST,
              "安全级别": SECURITY_LEVEL_LIST,
              "参考标准": REFERENCE_STANDARD_LIST
            }
