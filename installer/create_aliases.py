# Script to create a file with aliases for all the patterns
import os, sys

alias_filename = './fabric_patterns_aliases'
patterns = os.listdir('../patterns')

fabric_prefix = "fabric --pattern {}\n"
fabric_copy_prefix = "fabric --copy --pattern {}\n"

f=open(alias_filename,"w")

for pattern in patterns:
	alias1 = fabric_prefix.format(pattern)
	alias2 = fabric_copy_prefix.format(pattern)

	f.writelines(alias1)
	f.writelines(alias2)

f.close()