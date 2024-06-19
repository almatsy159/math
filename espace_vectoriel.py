


class E_Vect:
    def __init__(self,a=None,b=None,c=None):

        self.elements={}

    def loi_ext(self,opcode="*",b=None):
        res=None
        # b doit etre commutatif
        if type(self) != type(b):
            exec(f"{res}={self}{opcode}{b}")
        return res


    def loi_interne(self,opcode="+",b=None):
        res = None
        if type(self) == type(b):
            exec(f"{res}={self}{opcode}{b}")
        return res

    def __plus__(self):
