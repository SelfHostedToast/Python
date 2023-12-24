print('''
           88 88                                   
           88 ""                                   
           88                                      
,adPPYYba, 88 88  ,adPPYba, 8b,dPPYba,  ,adPPYba,  
""     `Y8 88 88 a8P_____88 88P'   `"8a I8[    ""  
,adPPPPP88 88 88 8PP""""""" 88       88  `"Y8ba,   
88,    ,88 88 88 "8b,   ,aa 88       88 aa    ]8I  
`"8bbdP"Y8 88 88  `"Ybbd8"' 88       88 `"YbbdP"'  
''')
print("Welcome to Aliens!\n")
print("Your mission is to escape the UFO. Alive...\n ") 

# Written by Dominick Smith

first_door = input("You wake up from a deep slumber and realize you aren't home, nor alone...\nYou get up off the table and see a door on the right and on the left.\nWhich door will you take? right or left?\n ").lower()
if first_door == "left":
  print("You carefully open the door using the biometric eye scanner, luckily no alarms sound.\n")

  print('''
                            GfLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLCCLfC          
                           GfL1L8888888888888888888888888888888888888888888888888888 0fttt          
                        8CfL0 fC                                                   8LfC Gt          
                      8CfL8   tC                                                 0LfC   Ct          
                    8LfC8     tC                                               0ffG     Gt          
                  0LfC        tC                                             GffG       Gt          
                0ffG          tC                                           Gff0         Gt          
              GffG            tC                                         GfL0           Gt          
            GfL0              tC                                       CfL8             Gt          
          0ffG8888888888888888fC8888888888888888888888888888888888888GtL8               Gt          
          GG880000000000000000fC800000000000000000000000000000000000GC8                 Gt          
          G8                  tC                                    0G                  Gt          
          G0                  tC                                    0G                  Gt          
          G0                  tC                                    0G                  Gt          
          G0                  tC                                    0G                  Gt          
          G0                  tC                                    0G                  Gt          
          G0                  tC                                    0G                  Gt          
          G0                  tC                                    0G                  Gt          
          G0                  tC                                    0G                  Gt          
          G0                  tC              0                     0G                  Gt          
          G0                  tC             000                    0G                  Gt          
          G0                  tC              0                     0G                  Gt          
          G0                  tC                                    0G                  Gt          
          G0                  tC                                    0G                  Gt          
          G0                  tC                                    0G                  Gt          
          G0                  tC                                    0G                  Gt          
          G0                  tC                                    0G                  Gt          
          G0                  tC                                    0G                  Ct          
          G0                  fC                                    8G                  Gt          
          G0                 81fCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCGtt          
          G0               8LfC0000000000000000000000000000000000000GG0000000000000080Ctt0          
          G0             8LfC8                                      0G              0fL0            
          G0           0LfG                                         0G            Gff0              
          G0         0ffG                                           0G          CfL0                
          G0       GffG                                             0G       8CfL8                  
          G0     Gff0                                               0G     8CtL8                    
          G0   GfL0                                                 0G   8LfC8                      
          G8 CfL8                                                   0G 0LfC                         
          GCtL0  8888888888888888888888888888888888888888888888888880CLfG                           
          0G080000000000000000000000000000000000000000000000000000000GG
        ''')

  second_door = input("You are now in a control room with a mysterious glowing box with a levatating item in it you can't quite make out.\nDo you reach into the box to grab the mysterious floating item? Yes or No?\n ").lower()

  if second_door == "no":
    print("You leave the floating item in place and afterwards you notice a room just ahead with another control panel.\nYou take a close look and realize the control panel has three '(3)' colored buttons, Red, Blue, and Green.\n")
    button_choice = input("Which button will you press? Red, Green or Yellow?\n ").lower()

    if button_choice == "red":
      print('''The room incinrates leaving you to pass out from the thick smoke.\n
    ,.   (   .      )        .      "
   ("     )  )'     ,'        )  . (`     '`
 .; )  ' (( (" )    ;(,     ((  (  ;)  "  )"
 _"., ,._'_.,)_(..,( . )_  _' )_') (. _..( '..
                ''')
      print('''GAME OVER \n
                                                                                                                                
  ,ad8888ba,        db        88b           d88 88888888888      ,ad8888ba,  8b           d8 88888888888 88888888ba   
 d8"'    `"8b      d88b       888b         d888 88              d8"'    `"8b `8b         d8' 88          88      "8b  
d8'               d8'`8b      88`8b       d8'88 88             d8'        `8b `8b       d8'  88          88      ,8P  
88               d8'  `8b     88 `8b     d8' 88 88aaaaa        88          88  `8b     d8'   88aaaaa     88aaaaaa8P'  
88      88888   d8YaaaaY8b    88  `8b   d8'  88 88"""""        88          88   `8b   d8'    88"""""     88""""88'    
Y8,        88  d8""""""""8b   88   `8b d8'   88 88             Y8,        ,8P    `8b d8'     88          88    `8b    
 Y8a.    .a88 d8'        `8b  88    `888'    88 88              Y8a.    .a8P      `888'      88          88     `8b   
  `"Y88888P" d8'          `8b 88     `8'     88 88888888888      `"Y8888Y"'        `8'       88888888888 88      `8b  
                                                                                                                      
          ''')
    elif button_choice == "green":
      print("The floor becomes a green colored sticky slime, alarms blare and you are greeted by aliens..\nTHEY AREN'T HAPPY\n GAME OVER! ")
      print('''
                 
            .-""""-.       .-""""-.
           /        \     /        |
          /_        _\   /_        _|
         // \      / || // \      / ||
         |\__\    /__/| |\__\    /__/|
          \    ||    /   \    ||    /
           \        /     \        /
            \  __  /       \  __  /
    .-""""-. '.__.'.-""""-. '.__.'.-""""-.
   /        \ |  |/        \ |  |/        |
  /_        _\|  /_        _\|  /_        _|
 // \      / || // \      / || // \      / ||
 |\__\    /__/| |\__\    /__/| |\__\    /__/|
  \    ||    /   \    ||    /   \    ||    /
   \        /     \        /     \        /
    \  __  /       \  __  /       \  __  /
     '.__.'         '.__.'         '.__.'
      |  |           |  |           |  |
      |  |           |  |           |  |
            
  ,ad8888ba,        db        88b           d88 88888888888      ,ad8888ba,  8b           d8 88888888888 88888888ba   
 d8"'    `"8b      d88b       888b         d888 88              d8"'    `"8b `8b         d8' 88          88      "8b  
d8'               d8'`8b      88`8b       d8'88 88             d8'        `8b `8b       d8'  88          88      ,8P  
88               d8'  `8b     88 `8b     d8' 88 88aaaaa        88          88  `8b     d8'   88aaaaa     88aaaaaa8P'  
88      88888   d8YaaaaY8b    88  `8b   d8'  88 88"""""        88          88   `8b   d8'    88"""""     88""""88'    
Y8,        88  d8""""""""8b   88   `8b d8'   88 88             Y8,        ,8P    `8b d8'     88          88    `8b    
 Y8a.    .a88 d8'        `8b  88    `888'    88 88              Y8a.    .a8P      `888'      88          88     `8b   
  `"Y88888P" d8'          `8b 88     `8'     88 88888888888      `"Y8888Y"'        `8'       88888888888 88      `8b 
            ''')
    elif button_choice == "yellow":
      print("You hit the yellow button shattering the floating cube from earlier. A trapdoor opens beneath you and you fall into the atmosphere.\nYou wake up realizing it was all a nightmare...\n YOU WIN!")
      print('''
8b        d8 ,ad8888ba,   88        88    I8,        8        ,8I 88 888b      88  
 Y8,    ,8P d8"'    `"8b  88        88    `8b       d8b       d8' 88 8888b     88  
  Y8,  ,8P d8'        `8b 88        88     "8,     ,8"8,     ,8"  88 88 `8b    88  
   "8aa8"  88          88 88        88      Y8     8P Y8     8P   88 88  `8b   88  
    `88'   88          88 88        88      `8b   d8' `8b   d8'   88 88   `8b  88  
     88    Y8,        ,8P 88        88       `8a a8'   `8a a8'    88 88    `8b 88  
     88     Y8a.    .a8P  Y8a.    .a8P        `8a8'     `8a8'     88 88     `8888  
     88      `"Y8888Y"'    `"Y8888Y"'          `8'       `8'      88 88      `888  
            ''')
    else:
      ("GAME OVER!")
  elif second_door == "yes":
    print('''You stick your hand into the mysterious cube instantly clamping your wrist down, and sounding an alarm! THEY KNOW YOU ARE HERE...\n
         
            .-""""-.       .-""""-.
           /        \     /        |
          /_        _\   /_        _|
         // \      / || // \      / ||
         |\__\    /__/| |\__\    /__/|
          \    ||    /   \    ||    /
           \        /     \        /
            \  __  /       \  __  /
    .-""""-. '.__.'.-""""-. '.__.'.-""""-.
   /        \ |  |/        \ |  |/        |
  /_        _\|  /_        _\|  /_        _|
 // \      / || // \      / || // \      / ||
 |\__\    /__/| |\__\    /__/| |\__\    /__/|
  \    ||    /   \    ||    /   \    ||    /
   \        /     \        /     \        /
    \  __  /       \  __  /       \  __  /
     '.__.'         '.__.'         '.__.'
      |  |           |  |           |  |
      |  |           |  |           |  |
         
   ,ad8888ba,        db        88b           d88 88888888888      ,ad8888ba,  8b           d8 88888888888 88888888ba   
 d8"'    `"8b      d88b       888b         d888 88              d8"'    `"8b `8b         d8' 88          88      "8b  
d8'               d8'`8b      88`8b       d8'88 88             d8'        `8b `8b       d8'  88          88      ,8P  
88               d8'  `8b     88 `8b     d8' 88 88aaaaa        88          88  `8b     d8'   88aaaaa     88aaaaaa8P'  
88      88888   d8YaaaaY8b    88  `8b   d8'  88 88"""""        88          88   `8b   d8'    88"""""     88""""88'    
Y8,        88  d8""""""""8b   88   `8b d8'   88 88             Y8,        ,8P    `8b d8'     88          88    `8b    
 Y8a.    .a88 d8'        `8b  88    `888'    88 88              Y8a.    .a8P      `888'      88          88     `8b   
  `"Y88888P" d8'          `8b 88     `8'     88 88888888888      `"Y8888Y"'        `8'       88888888888 88      `8b  
         ''')
  else:
    print('''
  ,ad8888ba,        db        88b           d88 88888888888      ,ad8888ba,  8b           d8 88888888888 88888888ba   
 d8"'    `"8b      d88b       888b         d888 88              d8"'    `"8b `8b         d8' 88          88      "8b  
d8'               d8'`8b      88`8b       d8'88 88             d8'        `8b `8b       d8'  88          88      ,8P  
88               d8'  `8b     88 `8b     d8' 88 88aaaaa        88          88  `8b     d8'   88aaaaa     88aaaaaa8P'  
88      88888   d8YaaaaY8b    88  `8b   d8'  88 88"""""        88          88   `8b   d8'    88"""""     88""""88'    
Y8,        88  d8""""""""8b   88   `8b d8'   88 88             Y8,        ,8P    `8b d8'     88          88    `8b    
 Y8a.    .a88 d8'        `8b  88    `888'    88 88              Y8a.    .a8P      `888'      88          88     `8b   
  `"Y88888P" d8'          `8b 88     `8'     88 88888888888      `"Y8888Y"'        `8'       88888888888 88      `8b  
          ''')
else:
  print('''
          You open the door to two aliens who immidiately look into your soul causing you to faint instantly. GAME OVER!\n
            .-""""-.        .-""""-.
           /        \      /        |
          /_        _\    /_        _|
         // \      / ||  // \      / \|
         |\__\    /__/|  |\__\    /__/|
          \    ||    /    \    ||    /
           \        /      \        /
            \  __  /        \  __  /
             '.__.'          '.__.'
              |  |            |  |
              |  |            |  |
          ''')
  print('''
                                                                                                                                
  ,ad8888ba,        db        88b           d88 88888888888      ,ad8888ba,  8b           d8 88888888888 88888888ba   
 d8"'    `"8b      d88b       888b         d888 88              d8"'    `"8b `8b         d8' 88          88      "8b  
d8'               d8'`8b      88`8b       d8'88 88             d8'        `8b `8b       d8'  88          88      ,8P  
88               d8'  `8b     88 `8b     d8' 88 88aaaaa        88          88  `8b     d8'   88aaaaa     88aaaaaa8P'  
88      88888   d8YaaaaY8b    88  `8b   d8'  88 88"""""        88          88   `8b   d8'    88"""""     88""""88'    
Y8,        88  d8""""""""8b   88   `8b d8'   88 88             Y8,        ,8P    `8b d8'     88          88    `8b    
 Y8a.    .a88 d8'        `8b  88    `888'    88 88              Y8a.    .a8P      `888'      88          88     `8b   
  `"Y88888P" d8'          `8b 88     `8'     88 88888888888      `"Y8888Y"'        `8'       88888888888 88      `8b  
                                                                                                                      
          ''')