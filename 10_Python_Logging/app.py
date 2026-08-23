import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s-%(name)s-%(levelname)s-%(message)s',
    datefmt='%Y-%M-%D %H:%M:%S',
    handlers=[
        logging.FileHandler("app1.log"),
        logging.StreamHandler()
    ]
)

logger=logging.getLogger("Arithmeticapp")

def add(a,b):
    result=a+b
    logging.debug(f"Addition {a} + {b} = {result}")
    return result

def substraction(a,b):
    result=a-b
    logging.debug(f"substraction {a}-{b} = {result}")
    return result

def multiply(a,b):
    result=a*b
    logging.debug(f"multiplication  {a} * {b}= {result}")
    return result

def division(a,b):
    try:
        result=a/b
        logger.debug(f"Division {a} /{b}= {result}")
        return result
    except ZeroDivisionError:
        logging.error("here is zero division error")
        


add(12,13)
substraction(10,5)
multiply(10,20)
division(10,5)