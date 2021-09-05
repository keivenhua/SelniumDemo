import logging


# 指定日志输出格式
format = "[%(asctime)s - %(levelname)s - %(name)s] \n %(message)s"
datefmts = "%Y-%m-%d %H:%M:%S %P"
logging.basicConfig(filename="./test.log",level=logging.DEBUG,format=format)


logging.debug("%s 登录，消费%s元","kevin","666")
try:
    xxx
except:
    logging.debug("fail",exc_info=True)
# logging.info("info错误信息")
# logging.warning("warning错误信息")
# logging.error("error错误信息")
# logging.critical("critical错误信息")
# logging.log(logging.DEBUG,"错误信息")



