"""
This program walks through a directory tree and deletes 
files larger than a given threshold size.
For safety i have it printing and the delete commented out.
"""
import os, send2trash

def delete():
	threshold = int(input('I Would Like to Delete Files Larger than ___ Bytes: '))
	directory = input('Enter the Directory You Would Like to Clean: ')
	absDir = os.path.abspath(directory)
	safeDelete = True
	os.chdir(absDir)

	for foldername, subfolders, filenames in os.walk(absDir):
		for filename in filenames:
			currentFile = os.path.join(foldername, filename)
			if filename.startswith('.'):
				continue
			elif os.path.getsize(currentFile) > threshold:
				if safeDelete:
					print(f'{currentFile} Size: {os.path.getsize(currentFile)} Deleted')
					send2trash.send2trash(currentFile)
				else:
					os.unlink(currentFile)			

	print('Done.')

def main():
	delete()

if __name__ == '__main__':
	main()