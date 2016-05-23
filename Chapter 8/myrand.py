class MyRand(object):

    def set(self, p1, p2, x0, modulus):
        self.__p1 = p1
        self.__p2 = p2
        self.__x = x0
        self.__modulus = modulus

    def next(self):
        self.__x = (self.__p1 * self.__x + self.__p2) % self.__modulus
        return self.__x

    def reset(self):
        self.__p1 = 2
        self.__p2 = 2
        self.__x = 2
        self.__modulus = 2
