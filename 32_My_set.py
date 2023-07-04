class My_set:
    data_set = []

    def __init__(self, *args):
        self.add(*args)

    def _check_and_prepare(self, *args):
        homo_type = None
        lst = []
        result = []
        for i in args:
            if homo_type != None and homo_type != type(i):
                print('NO HOMO!!!')
                return None
            homo_type = type(i)
            lst.append(i)
        lst.sort()
        result.append(lst[0])
        for i in range(1, len(lst)):
            if lst[i - 1] != lst[i]:
                result.append(lst[i])
        return result

    def add(self, *args):
        self.data_set = self.data_set + self._check_and_prepare(*args)

    def __add__(self, elements_for_add):
        return self.data_set + self._check_and_prepare(*elements_for_add.data_set)

    def __sub__(self, elements_for_add):
        return [i for i in self.data_set if i not in elements_for_add.data_set]