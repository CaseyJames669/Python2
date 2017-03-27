# file: FileUtilities.py
# Authors: Michael H. Goldwasser
#          David Letscher
#
# This example is discussed in Chapter 8 of the book
# Object-Oriented Programming in Python
#
"""A couple utility functions for opening files."""

def openFileReadRobust():
  """Repeatedly prompt user for filename until successfully opening with read access.

  Precondition:   none
  Postcondition:  Return the newly open file object.
  """
  source = None
  while not source:                  # still no successfully opened file
    filename = input('What is the filename? ')
    try:
      source = open(filename)
    except IOError:
      print ('Sorry. Unable to open file', filename)
  return source

def openFileWriteRobust(defaultName):
  """Repeatedly prompt user for filename until successfully opening with write access.

  Precondition:   defaultName is a string.  It is a suggested filename. This will be 
                  offered within the prompt and used when the return key is pressed
                  without specifying another name.
  Postcondition:  Return a newly open file object with write access.

  
  """
  writable = None
  while not writable:                # still no successfully opened file
    prompt = 'What should the output be named [%s]? '% defaultName
    filename = input(prompt)
    if not filename:                 # user gave blank response
      filename = defaultName         # try the suggested default
    try:
      writable = open(filename, 'w')
    except IOError:
      print ('Sorry. Unable to write to file', filename)
  return writable
