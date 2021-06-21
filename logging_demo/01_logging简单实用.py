# -\*- coding: UTF-8 -\*-
import logging


"""
filename:指定日志文件保存路径，日志就不会输出到控制台而是输出到指定文件
level：指定日志界别，只有大于或者等于当前设置的级别的日志信息才会输出
"""
format = "%(asctime)s - %(levelname)s - %(name)s - %(message)s"
datefmt = "%Y-%m-%d %H:%M:%S %p"
# 日志配置
logging.basicConfig(filename="./test1.log",level=logging.DEBUG,format=format,datefmt=datefmt)

# 直接调用
logging.debug("debug信息")
logging.info("info信息")
logging.warning("warning信息")
logging.error("error信息")
logging.critical("critical信息")
logging.log(logging.DEBUG,"------------错误信息-------------")
