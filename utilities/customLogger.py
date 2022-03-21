import logging

# class LogGen:
#     @staticmethod
#     def loggen():
#         logger = logging.getLogger()
#         fhandler = logging.FileHandler(filename='mylog.log', mode='a')
#         formatter = logging.Formatter('% (asctime)s: % (levelname)s: % (message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
#         fhandler.setFormatter(formatter)
#         logger.addHandler(fhandler)
#         logger.setLevel(logging.INFO)
#         return logger
# Bottom code didn't generate log file

class LogGen:
    @staticmethod
    def loggen():
        # logging.basicConfig(filename=".\\Logs\\automation.log",
        #                     format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        logging.basicConfig(filename=".\\Logs\\automation.log", format='%(asctime)s: %(levelname)s: %(message)s',
                            datefmt='%m/%d/%y %I:%M:%S %p', force=True)
        logger=logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger




