class Convert_Base:
    def __init__(self):
        self.dig_ls = "0123456789abcdefghijklmnopqrstuvwxyz"

    def to(self, dec, base):
        if dec == 0:
            return '00'
        num = ""
        while dec != 0:
            dig = dec % base
            dec = dec // base

            dig = self.dig_ls[dig]

            num = dig + num

        return num

    def back(self, num, base):
        j = 0
        dec = 0
        for i in range(len(num)):
            j = j - 1
            d = self.dig_ls.index(num[j]) * pow(base, i)
            dec = dec + d
        return dec
