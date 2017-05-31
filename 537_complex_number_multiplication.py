class Solution(object):
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        #(a+bi)(c+di) = (ac + adi + bci - bd) = ac-bd + (ad + bc)i
        #parse numbers
        real_1, complex_1 = self.parse_complex_number(a)
        real_2, complex_2 = self.parse_complex_number(b)

        real_part = real_1*real_2 - complex_1*complex_2
        complex_part = real_1*complex_2 + real_2*complex_1
        return "{}+{}i".format(real_part, complex_part)

    def parse_complex_number(self, num):
        plus = num.find("+")
        imag = num.find("i")
        return int(num[:plus]), int(num[plus+1:imag])
