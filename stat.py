from math import sqrt


"""
    to do :
        story telling
        non quantitative values (aka qualitative value "make categorie?")
        mode
        see more on data repr (charts)
        distribution
        /!\ quartile/nth ile interpolation !
"""

# next steps : see more about distributions and use of graphs
tst = [9,5,1,3,7,11,11,17,23,18,19,19]


def get_sqrt(x):
    return sqrt(x)

class Serie:
    # for now, only for quantitative group
    def __init__(self,lst=None):
        if lst == None:
            self.lst = []
        else :
            self.lst = lst
        
        ### DESCRIPTIVE STATS ### 
        self.lgt = len(self.lst)
        self.maxi = self.get_max()
        self.mini = self.get_min()
        self.sum= self.get_sum()
        self.avg = self.get_avg()
        self.sorted = self.sorting()
        
        self.range = self.maxi - self.mini
        self.med = self.get_med()
        #mode
        
        self.variance = self.get_variance()
        self.summed_var = self.summed_variance()
        self.pop_var = self.get_population_variance()
        self.smp_var = self.get_sample_variance()
        self.standard_dev_smp = get_sqrt(self.smp_var)
        self.standard_dev_pop = get_sqrt(self.pop_var)
        self.Q1 = self.get_Q1()
        self.Q3 = self.get_Q3()
        self.interquart = self.Q3 - self.Q1
        
        self.dict_mode = self.get_dict_mode()
        self.mode = self.get_mode()
        
        self.props = {"lgt":self.lgt,"maxi":self.maxi,"mini":self.mini,"sum":self.sum,"avg":self.avg,"Q1":self.Q1,"Q3":self.Q3,"ecart interquartile":self.interquart,
                    "range":self.range,"med":self.med,"summed_var":self.summed_var,"sample variance":self.smp_var,
                    "sample standard deviation":self.standard_dev_smp,"population variance":self.pop_var,"population standard deviation":self.standard_dev_pop,
                    "mode":self.mode}
        

    def __str__(self):
        my_str = f"lst : {self.lst}\nsorted {self.sorted}:\n"
        for k,v in self.props.items():
            my_str+= f"\t{k} : {v}\n"
        my_str+= f"variance : {self.variance}"
        my_str+= f"frequence dict : {self.dict_mode}"
        return my_str
    
    def sorting(self):
        """
        res = [] 
        flag = True
        first = True
        lst = self.lst
        tmp = self.maxi
        while flag == True:
            first = False
            for i in lst:
                if i < tmp:
                    tmp = i
                    flag = False
                res.append(tmp)         
                lst = lst[i:]
            print(res)
        """
        res = []
        lst = self.lst.copy()
        while len(res) < self.lgt:
            tmp_min = self.get_min(lst)
            idx = None
            for i,v in enumerate(lst):
                if v == tmp_min:
                    idx = i
            res.append(tmp_min)
            #lst.pop(idx)
            del lst[idx]
        return res
            
    def get_max(self) :
        maxi = 0
        
        for i in self.lst :
            if i  > maxi :
                maxi = i
        return maxi
    
    def get_min(self,lst=None):
        if lst == None:
            lst = self.lst

        mini = self.maxi
        for i in lst :
            if i < mini:
                mini = i
                
        return mini
    
    def get_sum(self):
        summed = 0
        for i in self.lst:
            summed += i
        return summed
    
    def get_avg(self):
        return self.sum/self.lgt
    
    
    def get_med(self):
        # 7 valeur : je prend la 4eme
        # 6 valeur : le prend la 3 et la 4 et je fais la moyenne
        #print(self.lgt/2)
        rounded_mid_value = self.lgt//2
        #print("mid_value ",rounded_mid_value,"lgt",self.lgt)  
        if self.lgt % 2 == 0:
            #print("in if")
            first = self.sorted[int(rounded_mid_value)-1]
            second = self.sorted[int(rounded_mid_value)]
            #print(first,second)
            res = (first + second) / 2
        else :
        #if self.lgt % 2 == 1:
            #print("in else")
            res = self.sorted[int(rounded_mid_value)]
        return res
            
    
    def get_variance(self):
        
        res = []
        for i in self.sorted:
            res.append((i - self.avg)**2)
        return res
    

    def summed_variance(self):
        # could refactor by using sum and another list than self.lst !
        res = 0
        for i in self.variance:
            res += i
        return res
    
    def get_sample_variance(self):
        res = self.summed_var/(self.lgt-1)
        return res
        
    def get_population_variance(self):
        res = self.summed_var/self.lgt
        return res
    
    def get_Q1(self):
        #lst = self.sorted.copy()
        
        #print(self.med)
        #lst = lst[:self.med]
        
        x = 0.25 * self.lgt
        #print(f"Q1 est la{x}eme valeur donc {int(x)} pour les liste en python lst[0]=> 1ere valeur")
        res = self.sorted[int(x)]
        #print("lst: ",lst)
        #print(res)
        #idx_q1 = (self.lgt+3 )/ 4
        #print(idx_q1)
        return res
    def get_Q3(self):
        x = 0.75 * self.lgt
        #print(f"Q3 est la{x}eme valeur")
        res = self.sorted[int(x)]
        return res
    
    def get_nile(self,x,n=1):
        # n eme xile 
        y = n/x * self.lgt
        res = self.sorted[int(y)]
        return res
    
    def get_dict_mode(self):
        res = {}
        for i in self.lst:
            if i not in res.keys():
                res[i] = 1
            else:
                res[i] += 1
        #print(res)
        return res
    
    def get_mode(self):
        maxi = 0
        maxi_k = None
        lst = []
        res = {}
        for k,v in self.dict_mode.items():
            if v > maxi :
                maxi = v
                maxi_k = k
                
        for k,v in self.dict_mode.items():
            if v == maxi:
                lst.append(k)
            
        print("k,v",maxi_k,maxi)
        res[maxi] = lst
        #return maxi_k,maxi
        print(res)
        return res
        
        
s1 = Serie(tst)
#print(s1.lst)
#print(s1.sorted)

print(s1)