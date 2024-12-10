class Serie:
    def __init__(self,name,lst=None):
        if lst == None:
            lst = []
        self.serie = lst
        self.len = len(self.serie)
        
    def get_moy(self):
        tmp = 0
        for i in self.serie:
            tmp += i
        return tmp/self.len
        
    
    def get_med(self):
        #for i in self.serie:
        #    if i == self.len//2 :
        #
        return self.serie[self.len//2]