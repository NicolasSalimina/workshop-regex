##
## EPITECH PROJECT, 2022
## regex
## File description:
## ex01
##

from ast import Str
import re

txt = "=#kskt8&d*L8kajbc1zjcEg+4rj82m^fSiqp@ql!%si *!rnv#nelb%$%3vk_R*!rnv#nelb%$%3vk_E^vz@zz5t3p*n_il0vGp9nn+29#8s%y4o*ulE!8x4X C'E!lfmtyt@zk9ad5iaxrs@ST G5is*_-@4y_9vwpt=tocxENI!lfmtyt@zk9ad5iaxrs@AL"
regex = re.findall('[A-Z ]',txt)
str = ''.join(regex)

print(str)