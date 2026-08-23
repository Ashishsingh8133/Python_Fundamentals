import logging
logging.basicConfig(
    filename='ashish.log',
    filemode='w',
    format='%(asctime)s-%(name)s-%(levelname)s-%(message)s',
    datefmt='%y:%m:%d %H:%M:%S',
    level=logging.DEBUG

)