# Automation_Project

## AUTOMATION WITH PYTHON

this project is made to be used with the assistance of a launcher, or can be compiled later on the line.

as for now, the project only consist of launchers, web access module, and web search module.

__________________
### LAUNCHER
launcher is made to start the modules.

The idea here is to add the launcher directory into path environment variable,
and then we can just press Windows + R or open Run and type the name, for example wap, or even use codes, like 00, as long as it isn't used by the system like dxdiag, cmd, etc.

__Launcher list__

WAP is for web access point or web access module.

WSAP is for web search access point or web search module.

WSAP2 is for the branched version of web search module.

__________________
### WEB ACCESS
web access takes keyword inputs and match it with the available dictionary of key, lists, and names.

the dictionaries is imported from Data.json

web access Data.json is contains of defaultname and dictionaries.

__Data.json__

defaultname is the default url name in case the keyword doesn't match anything inside the dictionaries.

dictionary list = keywordlist, codelist, and namelist.


_______________
### WEB SEARCH
web search on the other hand, takes parameters, 

if 1 parameter was given, it will save the parameter as urlparameter and then it would ask for what to search.

if 2 was given instead, it would split the input into 2 variable(urlparameter, and search) with seperator from json file.

web search Data.json contains defaultindex, seperator, urlinfo.

__Data.json__

default index is the default searching url if the given urlparameter is invalid

seperator is an array composed of seperators that will be used at the spliting function, keep in mind the split function limit parameter is set to 1 splitting.

urlinfo is a list containing all the url informations. there are the names, url, letter1, and letter2.

  letter1 and letter2 are kinda odd, because using a dictionary is better for changing symbols or spaces. 
  
  i'll think about remaking this later, but for now i don't think i will.
_______________________

thanks for reading this piece of readme, and im very grateful for any support or help given! :)
