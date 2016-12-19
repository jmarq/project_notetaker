import process_config
from subprocess import call
import sys

def  main_wrapper(filename,vim=False,read_mode=False):
  pairs = process_config.parseConfigFile(filename)
  prompt_text = ""
  prompt_text += "Choose a Project:\n"

  # the below code is sloppy and must be refactored in the near future
  # this is the main user interaction area, care must be taken with error handling ;)
  for i in range(len(pairs)):
      prompt_text+=str(i)+") "+pairs[i][1]+"\n"
  selection = input(prompt_text)
  if int(selection)not in range(len(pairs)):
      print ("naw")
  else:
      pair = pairs[int(selection)]
      if vim:
          call(["vim",pair[0]])
      elif read_mode:
          call(['more',pair[0]])
      else:
        note = raw_input("\n vvv enter note for %s:\n" % pair[0])
        print "note: %s" % note
      


if __name__ == "__main__":
    conf_filename=sys.argv[1]
    vim = False
    read_mode = False
    if "-v" in sys.argv:
        vim = True
    elif "-r" in sys.argv:
        read_mode = True
    main_wrapper(conf_filename, vim=vim,read_mode=read_mode)


        
