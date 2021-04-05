<?php

# Checks if both are PDF


# Checks if file contents are different
file_get_contents($f1) === file_get_contents($f2)

# Checks if MD5 hashes are the same
md5_file($f1) == md5_file($f2)

# It should be added as a general warning for all hash functions to always use 
# the triple equals === for comparison.

?>