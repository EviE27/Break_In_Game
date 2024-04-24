#########################################################
#module: odjects
#########################################################
"""This module contains items that the charactor can pick up and use
along with key and passcode used to get through to other rooms.
"""
#########################################################
""" make action for explor and pick up"""
#list of object if the palyer explors the room and then thye can select 
odject = { 
            "paper" : {"discription" : "There is a code on the paper 7863",
                       "location": [1, 0],
                       "code" : "7863",
                      },
            "window" : {"discription" :"""You look through the window but it is too 
                          dirty to see anything.""", 
                        "location" : [1, 0] and [2, 0 ] and [3, 0],
                         },
          "celler door" : {"discription" : """ The door is locked... but it has a
          cobination lock""",
                           "location" : [0, 1] and [0, 2],
                           "requierment" : ["code"]
                             },
         "wood crates" :{ "discription" : " The crates are filled with...Jelly beans", 
                         "location" : [2, 1] and [3, 1],
                         "jelly_beans" : "Jelly beans",
                        },
         "key" : {"discription" : "This key looks like the one for the breaker box",
                  "location" : [4, 1]
                        },
          "case" : {"discription" :""" on the table there is a case has PLANS writen on 
it, but it looks like their are lazer sorounding the case. """,
                    
                   " location" : [1, 2] and [2, 2] and [3, 2],
                   },
                     "breaker box": {"discription" : """it looks like the breaker box 
controls the power to the lazers """,           
                     " location" : [1, 2] and [2, 2],
                     "requierment" : ["key"]
                    } 
                    },
           
          
          