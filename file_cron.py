import os, shutil, logging, time
from logging.handlers import RotatingFileHandler

dst = "D:\\test"
src = "C:\\Users\\visha\\Desktop\\dev-1\\prototype2\\upload"

#Create and configure logger
logname = "copyfile.log"
logging.basicConfig(
            handlers=[RotatingFileHandler(logname, maxBytes=5000000, backupCount=2)],
            format='%(asctime)s, %(msecs)d :: %(name)s :: %(levelname)s :: %(message)s',
            datefmt='%H:%M:%S',
            level=logging.DEBUG)

#Creating an object
logger=logging.getLogger()

def copyfile():
    start = time.time()
    logger.debug("************************************")
    logger.info("inside copyfile")
    try:
        folder_names = os.listdir(src)
        for folder_name in folder_names:
            if folder_name in os.listdir(dst):
                logger.info(f"already present {folder_name}")
                sub_folder_names = os.listdir(os.path.join(src, folder_name))
                for sub_folder_name in sub_folder_names:
                    if sub_folder_name in os.listdir(os.path.join(dst, folder_name)):
                        logger.info(f"already present {sub_folder_name}")
                        file_names = os.listdir(os.path.join(src, folder_name, sub_folder_name))
                        for file_name in file_names:
                            if file_name not in os.listdir(os.path.join(dst, folder_name, sub_folder_name)):
                                shutil.copy2(os.path.join(src, folder_name, sub_folder_name, file_name), 
                                os.path.join(dst, folder_name, sub_folder_name, file_name))
                                logger.info(f"copied {file_name}")
                    else:
                        shutil.copytree(os.path.join(src, folder_name, sub_folder_name), os.path.join(dst, folder_name, sub_folder_name))
                        logger.info(f"copied {sub_folder_name}")
            else:
                shutil.copytree(os.path.join(src, folder_name), os.path.join(dst, folder_name))
                logger.info(f"copied {folder_name}")
    except Exception as e:
        logger.error(e)
    finally:
        end = time.time()
        logger.info("exiting copyfile")
        logger.info(f"Runtime of the program is {end - start}")
        logger.debug("************************************")


if __name__ == '__main__':
    copyfile()