# Script to create a file with aliases for all the patterns
import os, sys

alias_filename = './fabric_patterns_aliases'
patterns = os.listdir('../patterns')

fabric_prefix = "alias {}='fabric --pattern {}'\n"
fabric_copy_prefix = "alias c_{}='fabric --copy --pattern {}'\n"

f=open(alias_filename,"w")

for pattern in patterns:
	alias1 = fabric_prefix.format(pattern,pattern)
	alias2 = fabric_copy_prefix.format(pattern,pattern)

	f.writelines(alias1)
	f.writelines(alias2)

f.close()