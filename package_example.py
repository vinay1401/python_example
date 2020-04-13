# 3 ways to import packages or module

# 1
import ecomerce.calculate

# 2
from ecomerce.calculate import calculate_shipping, calculate_tax

# 3
from ecomerce import calculate

ecomerce.calculate.calculate_shipping()
calculate_tax()

calculate.calculate_total()