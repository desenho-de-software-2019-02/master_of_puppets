#!/bin/bash


find services/resources/controller -type f -exec sed -i 's/BaseController/Strategy/g' {} +
find services/campaigns/controller -type f -exec sed -i 's/BaseController/Strategy/g' {} +

find services/resources/views -type f -exec sed -i 's/Context/BaseController/g' {} +
find services/campaigns/views -type f -exec sed -i 's/Context/BaseController/g' {} +
