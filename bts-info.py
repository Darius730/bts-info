class BTS:
    name = "bangtan sonyeondan"
    birth = 2013
    def description(self):
        desc_str = "His name is %s and born in %d" % (self.name, self.birth)
        return desc_str
        
        RM = BTS()
        RM.name = "Kim Namjoon"
        RM.birth = 1994

        Jin = BTS()
        Jin.name = "Kim Seokjin"
        Jin.birth = 1992

        Suga = BTS()
        Suga.name = "Min Yoongi"
        Suga.birth = 1993

        JHope = BTS()
        JHope.name = "Jung Hoseok"
        JHope.birth = 1994

        Jimin = BTS()
        Jimin.name = "Park Jimin"
        Jimin.birth = 1995

        V = BTS()
        V.name = "Kim Taehyung"
        V.birth = 1995

        Jungkook = BTS()
        Jungkook.name = "Jeon Jungkook"
        Jungkook.birth = 1997
        
        print(RM.description)
        print(Jin.description)
        print(Suga.description)
        print(JHope.description)
        print(Jimin.description)
        print(V.description)
        print(Jungkook.description)
