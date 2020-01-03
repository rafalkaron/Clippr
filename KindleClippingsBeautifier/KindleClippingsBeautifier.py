# coding: utf-8
__version__ = "0.2"
__author__ = "Rafał Karoń <rafalkaron@gmail.com.com>"

"""
    Kindle Clippings Beautifier (Codename: Unchanging Zit)
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Beautify your Kindle clippings by exporting them to a desired format.
    
    Upcoming features:
    - Automatically detect the "My Clippoings.txt" file @ connected Kindle
    - Send converted files to an email
    - Convert to Markdown
    - Convert to PDF by using DITA-OT
    - Convert to HTML5 by using DITA-OT
    - CLI
    - GUI
    - EXE
    - Enumerate output files
"""
#Modules
import os
import datetime

#Global Variables
_timestamp = datetime.datetime.now()
_timestamp_formatted = str(_timestamp.strftime("%d_%m_%y-%H-%M-%S"))

#Functions
def intro():
    print("Beautify your Kindle clippings by exporting them to a Markdown file.")

def main_menu():
    _query = input("Enter one of the following:\n[md] to convert your Kindle clippings to Markdown\n")
    if _query == "md" or _query == "MD" or _query == "[md]" or _query == "[MD]":
        kindle_to_md()
    else:
        print("Try answering the following question again.")
        main_menu()

def kindle_to_md():
    global _kindle_to_md_called
    _kindle_to_md_called = True                                                                                                                 #Checks if the function was run for the summary
    _clippings_location = input("Enter a full path to the \"Kindle Clippings.txt\" file: ")                                                     #Asks for the input txt file
    _clippings_file = open(_clippings_location, "rt", encoding="utf-8")                                                                         #Opens the input txt file
    
    out_folder()                                                                                                                                #Calls a function that creates an out folder
    _out_md = open(str(_out_folder) + "/" + "My Clippings" +str(_timestamp.strftime("%d_%m_%y-%H-%M-%S")) + ".md", "w+t", encoding="utf-8")     #Creates the output md file
    _out_md.write("#My Kindle Clippings\n_Generated on " + str(_timestamp.strftime("%x")) + " at " + str(_timestamp.strftime("%X")) + "_\n\n")  #Adds title to the file
    _out_md.write(_clippings_file.read())                                                                                                       #Copies the input txt file contents into the output md file
    

    _clippings_file.close                                                                                                                       #Closes the file
    _out_md.close                                                                                                                               #Closes the file
_kindle_to_md_called = False                                                                                                                    #Needed for summary

def out_folder():
    global _out_folder
    _out_folder = ("out")
    if not os.path.exists(_out_folder):
        os.mkdir(_out_folder)

def src_folder():
    global _src_folder
    _src_folder = ("src")
    if not os.path.exists(_src_folder):
        os.mkdir(_src_folder)

def summary():
    if _kindle_to_md_called == True:
        print("Your Kindle clippings were converted to Markdown.")

#Invocations
intro()
main_menu()
summary()
exit()