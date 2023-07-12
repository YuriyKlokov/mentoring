class My_set:

    def __init__(self, *args):
        self.data_set = []
        self.add(*args)
        self.index_for_iter = 0
    
    def _check_homo(self, *args):
        homo_type = None
        lst = []
        for i in args:
            if homo_type != None and homo_type != type(i):
                print('NO HOMO!!!')
                return None
            self.homo_type = type(i)
            lst.append(i)
        return lst 
    
    def _duplicates_deleted(self, lst_for_perp):
        result = [] 
        lst_for_perp.sort()
        result.append(lst_for_perp[0])
        for i in range(1, len(lst_for_perp)):
            if lst_for_perp[i - 1] != lst_for_perp[i]:
                result.append(lst_for_perp[i])
        return result

    def add(self, *args):
        united = self.data_set + self._duplicates_deleted(lst_for_perp=self._check_homo(*args))
        self.data_set = self._duplicates_deleted(lst_for_perp=united)

    def __add__(self, elements_for_add):
        e = My_set(*self.data_set, *elements_for_add.data_set)
        return e

    def __sub__(self, elements_for_add):
        t = My_set(*[i for i in self.data_set if i not in elements_for_add.data_set])
        return t
    
    def __str__(self):
        return f'{self.data_set}'
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index_for_iter >= len(self.data_set):
            self.index_for_iter  = 0
            raise StopIteration 
        item = self.data_set[self.index_for_iter]
        self.index_for_iter += 1
        return item 