from app import App
from service_one_int import ServiceOneInt
from service_two_int import ServiceTwoInt
from service_one_string import ServiceOneString
from service_two_string import ServiceTwoString

if __name__ == "__main__":
    app = App("Main")
    app.run(ServiceOneInt(), ServiceTwoString())

    # todo: implement service factory