class Phone:
    __current_voltage = .1

    def __keep_single_core(self):
        print("CPU single core.")

    def call(self):
        if self.__current_voltage >= 1:
            self.__keep_single_core()
        else:
            print("Cannot call")

p = Phone()
p.call()

# 在类中提供仅供内部使用的属性和方法
# 不对外开放（类对象无法使用） - 手机用户无法修改电压等属性 - 拍照时 - 程序自动检测