import numpy as np
from scipy.stats import expon, norm

class Boostrap_pivotal():
    def __init__(self, data_set):
        self.data_set = data_set
        self.data_set_len = len(data_set)
        self.bootstrap_distirbution = []

    def bootstrap_statistic(self, function, rng):
        self.teta_f = function(self.data_set)
        for i in range(rng):
            self.bootstrap_distirbution.append(function(np.random.choice(self.data_set, size=self.data_set_len, replace=True)))

    def get_conf_interval(self):
        bootstrap_destribution_po025 = np.percentile(a=self.bootstrap_distirbution, q=100*0.025)
        bootstrap_destribution_po975 = np.percentile(a=self.bootstrap_distirbution, q=100*0.975)
        print(2 * self.teta_f - bootstrap_destribution_po975, 2 * self.teta_f - bootstrap_destribution_po025)

np.random.seed(40)
a = expon(scale=1.0).rvs(200)
b = Boostrap_pivotal(a)
b.bootstrap_statistic(function=np.mean, rng=10000)
b.get_conf_interval()


class Boostrap_percentile(Boostrap_pivotal):
    def get_conf_interval(self):
        bootstrap_destribution_po025 = np.percentile(a=self.bootstrap_distirbution, q=100*0.025)
        bootstrap_destribution_po975 = np.percentile(a=self.bootstrap_distirbution, q=100*0.975)
        print(bootstrap_destribution_po025, bootstrap_destribution_po975)
    
np.random.seed(40)

q = Boostrap_percentile(a)
q.bootstrap_statistic(function=np.mean, rng=10000)
q.get_conf_interval()


class Boostrap_normal(Boostrap_pivotal):
    def get_conf_interval(self):
        se = np.var(self.bootstrap_distirbution)**0.5
        print(self.teta_f - norm.ppf(0.975) * se, self.teta_f + norm.ppf(0.975) * se)
        
np.random.seed(40)
w = Boostrap_normal(a)
w.bootstrap_statistic(function=np.mean, rng=10000)
w.get_conf_interval()

