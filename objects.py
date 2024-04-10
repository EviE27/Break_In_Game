#########################################################
#module: odjects
#########################################################
"""This module contains items that the charactor can pick up and use
along with key and passcode used to get through to other rooms.
"""
#########################################################
""" make action for explor and pick up"""
#list of object if the palyer explors the room and then thye can select 
odjects = {"side_door" : {"paper" : ["There is a code on the paper 7863"],
                ## window explor to look inside that would call the discription
                          "window" : ["""You look through the window but it is too 
                          dirty to see anything."""], 
                         },
         "celler_entrance" : {"celler door" : ["""you try to open the door but it is 
                                                locked """],
                             },
         
          
          }