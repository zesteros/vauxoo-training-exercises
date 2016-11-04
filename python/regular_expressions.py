"""the string "python" coincides with the expression
regular "python" using the match function"""
import re
if re.match("python", "python"):
	print "cierto"
"""If we wanted to to check if the string "python", "python"
"Python" or anything else that ends in "ython" we could
use the wildcard character, the point '.'"""
if re.match(".ython", "python"):
	print "true"
elif re.match(".ython", "jython"):
	print "true"
"""To check if the string consists of 3 characters followed by a
point, for example, could use the following"""
if re.match("...\.", "abc."):
	print "true"
"""If we need an expression that will only be true for the chain
nas "python", "jython" and "cython" and no other, could use
the character '|' alternative writing to express the full three subpatterns"""
if re.match("python|jython|cython", "python"):
	print "true"


