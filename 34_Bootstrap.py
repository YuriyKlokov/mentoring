
import numpy as np
from scipy.stats import expon, norm

class Boostrap():
    def __init__(self, data_set):
        self.data_set = data_set
        self.data_set_len = len(data_set)
        self.bootstrap_distirbution = []

    def bootstrap_statistic(self, function, rng):
        self.teta_f = function(self.data_set)
        for i in range(rng):
            self.bootstrap_distirbution.append(function(np.random.choice(self.data_set, size=self.data_set_len, replace=True)))
            
class Bootstrap_percentile(Boostrap):
    
    def _get_bootstrap_sats_persentiles(self):
        bootstrap_destribution_po025 = np.percentile(a=self.bootstrap_distirbution, q=100*0.025)
        bootstrap_destribution_po975 = np.percentile(a=self.bootstrap_distirbution, q=100*0.975)
        return bootstrap_destribution_po025, bootstrap_destribution_po975
    
    def get_conf_interval(self):
        l_border, r_border = self._get_bootstrap_sats_persentiles() 
        return l_border, r_border 
    
class Boostrap_pivotal(Bootstrap_percentile):
    
    def get_conf_interval(self):
        bootstrap_destribution_po025, bootstrap_destribution_po975  = self._get_bootstrap_sats_persentiles() 
        l_border = 2 * self.teta_f - bootstrap_destribution_po975
        r_border = 2 * self.teta_f - bootstrap_destribution_po025
        return l_border, r_border
        
class Boostrap_normal(Boostrap):
    def get_conf_interval(self):
        se = np.var(self.bootstrap_distirbution)**0.5
        l_border = self.teta_f- norm.ppf(0.975) * se
        r_border = self.teta_f + norm.ppf(0.975) * se
        return l_border, r_border 


np.random.seed(40)
a = norm(loc=2 , scale=2).rvs(200)
b = Boostrap_pivotal(a)
b.bootstrap_statistic(function=np.mean, rng=10000)
print(b.get_conf_interval())



np.random.seed(40)

q = Boostrap_percentile(a)
q.bootstrap_statistic(function=np.mean, rng=10000)
print(q.get_conf_interval())


np.random.seed(40)
w = Boostrap_normal(a)
w.bootstrap_statistic(function=np.mean, rng=10000)
print(w.get_conf_interval())


f = 0
num_of_try = 1000
true_mean = 2
for i in range(num_of_try):
    a = norm(loc=true_mean , scale=2).rvs(200)
    b = Boostrap_pivotal(a)
    b.bootstrap_statistic(function=np.mean, rng=10000)
    l_border, r_border = b.get_conf_interval()
    if l_border < true_mean < r_border:
        f += 1
print(f/num_of_try - 1)

