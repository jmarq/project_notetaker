import process_config

def  main_wrapper():
  pairs = process_config.parseConfigFile("possible_conf_file.conf")
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
      print pairs[int(selection)][0]


if __name__ == "__main__":
    main_wrapper()


        
