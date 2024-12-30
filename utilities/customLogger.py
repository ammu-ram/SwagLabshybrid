import logging

class logGeneration():
    @staticmethod
    def logGeneration():
        logging.basicConfig(filename="/Logs/automation.log",levelname=logging.INFO,format="%(asctime)s %(levelname)s %(message)s")
        logger=logging.getLogger()
        return logger