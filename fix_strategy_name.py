#!/bin/bash


find services/resources/views -type f -name '*.py' -exec sed -i 's/from base\.controller import BaseController//g' {} +

#find services/resources/views -type f -exec sed -i 's/Context/BaseController/g' {} +
#find services/campaigns/views -type f -exec sed -i 's/Context/BaseController/g' {} +

#find services/resources/controller -type f -exec sed -i 's/services\.base\_controller/base\.controller/g' {} +
#find services/campaigns/controller -type f -exec sed -i 's/services\.base\_controller/base\.controller/g' {} +

#find services/resources/views -type f -exec sed -i 's/services\.base\_controller/base\.controller/g' {} +
#find services/campaigns/views -type f -exec sed -i 's/services\.base\_controller/base\.controller/g' {} +
