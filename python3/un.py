try:
    file = open("example_file.txt")

    try:
        def make_upcase(line):
        
        	return line.strip().upper()
        
        upcase_lines = map(make_upcase, file.readlines())

        for el in upcase_lines:

        	print(el)
                
    finally:
                # Arg, this is ugly.
                # We will figure out how to fix this later.
                file.close()
except IOError:
            # should never happen
    self.fail()