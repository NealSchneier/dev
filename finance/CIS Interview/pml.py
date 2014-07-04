from bs4 import BeautifulSoup
import sys
import re

#This function replaces the leading indention from the HTML. 
#It is assumed that each tab is 4 spaces and that there are never more then two tabs in a line.
def replace4Spaces(pml_tag):
	#take advantage of regelar expressions to handle indentions
	pml_tag = re.sub(r'        ', "\t", pml_tag)
	pml_tag = re.sub(r'    ', "", pml_tag)
	return pml_tag

#args=1 - input file
#args=2 - output file
def main(args, debug=False):


	#open file and make easily workable.
	with open(args[1], 'rb') as f:
		soup = BeautifulSoup(f)
	code = ''
	#for each pml tag in the HTML go through this loop
	for index, pml_tag in enumerate(soup.find_all('pml')):
		#get the children of the PML tag ie so you just work with the code
		for child in pml_tag.children:
			
			code = code + str(child)
		
		code = replace4Spaces(code)
		#execute the python code and if there is output display it as part of the HTML
		out = {}
		exec(str(code)) in out
		#replaces the pml tag with the output from the executed python code
		pml_tag.replaceWith( str(out['pml']) )
		
	#output the data to either the file specified or the default file name
	output = "output.py"
	if len(args) > 2:
		output = args[2]
	with open(output, 'wb') as fp:
		#outputs the HTML in a pretty format
		fp.write(soup.prettify(formatter=None))

#the main function called when executing this script.
if __name__ == '__main__':
	main(sys.argv)