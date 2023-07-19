
import sys

#(Concatenation of Strings) *Common variables and String Assignments*
#
#This comment is relevant to repeated sections of code and thus will
#be reffering to this section for relevant justification going forward
#
#The method used for the string implementation which contains the relevant text-based narrative
#enables a more structured layout of the code blocks and strings which contain as indicated the
#narrative which is printed to the user when needed.
#Modifications are made more accessible and streamlined as an individual inspecting the code
#directly will not need to piece together the puzzle, for the most part, to determine what part
#of the narrative is meant to be printed were.
#Naming schemes for each string name have been chosen based on what stage and branch the string
#will be operating on, for example, the “forest_story_start” identifies which of the two starting
#storylines it is, and the start section is changed based on the stage and or branch is has gone
#off to.
#In various sections there are implementations of the variable referred to as “player_name”, again
#having this performed in the current method allows the method allows the overall readability to
#improve.
#When a change is required, the steps taken to swap out a variable or change a section of the story
#is vastly simplified.
#Although having the strings written out literally for each print is possible it will cause messy
#code and likely result in poor expandability etc if anything needs to be changed.)



def main():

    #The below code block greets the player and asks them to input their chosen name which is then
    #assigned to the appropriate variable.
    #As this section isn’t repeated and doesn’t require any conditions or comparisons to progress a
    #sys print statement is all that is needed to display the greeting and variable after it is stripped
    #from the inputted line.
    #
    #Having a greeting message is used as a formality when launching of this nature,, it also allows
    #an individual to troubleshoot and determine what stage of the program cycle they are at as upon
    #a storylines completion the function "main" will return itself leaving an indicator that it has
    #restarted in a sense. 
    sys.stdout.write("\nWelcome to the choose your own adventure program.\n")
    sys.stdout.write("======================================================\n")
    sys.stdout.write("Enter your name to begin: \n")

    #A variable name has been chosen based on a scenario where either an individual is unclear of if this
    #is a username or if it’s the player’s name that will be used in the story going forward.
    #The data stored within the variable is stripped from the line input by the player previously which is
    #then assigned to the variable in question.As the program directly requires a custom name that can be
    #decided upon by a user this method is a better alternative than doing that task later down the line
    #which could cause the code to become messy and confusing to someone who is needing to keep track of
    #the steps taken. 
    #
    #Having this variable stored at the very start enables anyone to change the code below without affecting
    #the variable either on purpose or by accident. 
    player_name = sys.stdin.readline().strip()
    sys.stdout.write("\nLets start " +player_name+"\n")
   
    main_story_start= "\nYou awaken in a large field of grass, the only thing\n"
    main_story_start+= "you have is some ragged clothes and footwear. In the\n"
    main_story_start+= "distance to your left is is a lone house upon a hill\n"
    main_story_start+= "which you think would only take roughly an hour to get\n"
    main_story_start+= "at a walking pace. To the right, you can see some smoke\n"
    main_story_start+= "rising out from a forest, perhaps a village or something\n"
    main_story_start+= "less civilized.\n"
    main_story_start+= "\nDo you go left or right? \n"
    
    #(*Refer to code block comment for this repeated sections Identified as "Concatenation of Strings"*)
    house_story_start= "\nYou set off to the house on the hill knowing it will\n"
    house_story_start+= "take you some time to get there but it seems the better\n"
    house_story_start+= "option.\n"
    house_story_start+= "\n[An Hour Passes by]\n\n"
    house_story_start+= "Cresting the hill to the house you can make out the faint\n"
    house_story_start+= "voices of two people, as you draw closer it appears to be\n"
    house_story_start+= "the small farmhouse likely being a temporary stay on a large\n"
    house_story_start+= "farm. Outside the farmhouse are twohorses, saddled and ready\n"
    house_story_start+= "for a ride, whoever’s inside must\’ve arrived only moments ago.\n"
    house_story_start+= "Getting closer still, you can make out two silhouettes from the\n"
    house_story_start+= "windows, two farmhands likely working this area of the farm.\n"
    house_story_start+= "Perhaps you could knock on the door and ask the farm hounds\n"
    house_story_start+= "what’s going on, or maybe still steal a horse and cover some\n"
    house_story_start+= "more ground.\n"
    house_story_start+= "\n\n"
    house_story_start+= "Steal a horse to cover more ground and perhaps reach somewhere faster [one]"
    house_story_start+= "\nor\n"
    house_story_start+= "Approach the house and attempt to get some help [two]\n"
    
    #(*Refer to code block comment for this repeated sections Identified as "Concatenation of Strings"*)
    house_story_branch_1= "\nYou steal the horse riding off into the sunset, you have\n"
    house_story_branch_1+= "no idea what youyou hope to find nor where to go but staying\n"
    house_story_branch_1+= "here isn’t an option anymore.\n"
    
    #(*Refer to code block comment for this repeated sections Identified as "Concatenation of Strings"*)
    house_story_branch_2= "\nApproaching the door calming careful not to startle everyone\n"
    house_story_branch_2+= "inside, you knock three times and wait… One of the farmhands\n"
    house_story_branch_2+= "opens the door cautiously. He looks you up and down\n"
    house_story_branch_2+= "before asking your name \""+player_name+"\" you answer.\n"
    house_story_branch_2+= "He asks how and why you came here; you\’re not sure telling\n"
    house_story_branch_2+= "him you seem to have lost most of your memory, he says there\n"
    house_story_branch_2+= "isn\’t anyone close by who could help. You talk for a while\n"
    house_story_branch_2+= "going back and forth eventually he asks if interested\n"
    house_story_branch_2+= "inhelping out on the farm. This seems like the best\n"
    house_story_branch_2+= "option. You spend the rest of yourdays as a farmhand\n"
    house_story_branch_2+= "without a recollection of who you were before, but it doesn’t\n"
    house_story_branch_2+= "matter now.\n"
    
    #(*Refer to code block comment for this repeated sections Identified as "Concatenation of Strings"*)
    forest_story_start= "\nYou make your way towards the forest aiming to reach the source\n"
    forest_story_start+= "of the smoke. Approaching where the grass fields and forest meet you\n"
    forest_story_start+= "begin to see a slew of tall trees and berry bushes;\n"
    forest_story_start+= "the forest barely lets any light in and as such is quite dark.\n"
    forest_story_start+= "Although you\’d rather not enter it\'s too late to be changing\n"
    forest_story_start+= "your mind. Making your way inand keeping an eye on the smoke\n"
    forest_story_start+= "at all times to avoid getting lost you push through the spiked\n"
    forest_story_start+= "berry bushes, fallen trees and startled wildlife.\n"
    forest_story_start+= "\n\n[Roughly 30 minutes pass by as you make a path towards the smoke]\n\n"
    forest_story_start+= "Just barely been able to make out the smoke through the trees you\n"
    forest_story_start+= "stumble upon a small clearing of berry bushes, they look to be\n"
    forest_story_start+= "blackberries and blueberries. You\’ve been travelling for some time\n"
    forest_story_start+= "through difficult terrain and need to eat something. This is going\n"
    forest_story_start+= "to be the best edible thing you\’re going to find no doubt for some time.\n"
    
    #(*Refer to code block comment for this repeated sections Identified as "Concatenation of Strings"*)
    forest_story_start_town_arrival= "\nAfter that, you arrive at the clearing where there\n"
    forest_story_start_town_arrival+= "appears to be an isolated village. As you approach the\n"
    forest_story_start_town_arrival+= "leader of the town comes up to you and asks your name\n"
    forest_story_start_town_arrival+= "along with how many of the berries did you have. You don\’t\n"
    forest_story_start_town_arrival+= "don\’t know how she knows this but seeing as she already knows\n"
    forest_story_start_town_arrival+= "that you tell her.\n"
    
    #(*Refer to code block comment for this repeated sections Identified as "Concatenation of Strings"*)
    forest_story_branch_blue_berries_less= "\nThe town\'s leader thanks you for your restraint\n"
    forest_story_branch_blue_berries_less+= "in the berry clearing and offers to help you if\n"
    forest_story_branch_blue_berries_less+= "you can answer his maths related question... You agree.\n"
    
    #(*Refer to code block comment for this repeated sections Identified as "Concatenation of Strings"*)
    forest_story_branch_blue_berries_exceed= "\nUpon hearing this the town leader begins to\n"
    forest_story_branch_blue_berries_exceed+= "get angry at you, you\’ve eaten way too many\n"
    forest_story_branch_blue_berries_exceed+= "berries for them to help you on your journey.\n"
    forest_story_branch_blue_berries_exceed+= "You\'re thrown into their town prison charged\n"
    forest_story_branch_blue_berries_exceed+= "with excessive berry consumption.\n"
    
    #(*Refer to code block comment for this repeated sections Identified as "Concatenation of Strings"*)
    forest_story_branch_black_berries_less= "\nThe town\'s leader thanks you for your restraint\n"
    forest_story_branch_black_berries_less+= "in the berry clearing and offers to help you if you\n"
    forest_story_branch_black_berries_less+= "can answer his maths related question... You agree.\n"
    
    #(*Refer to code block comment for this repeated sections Identified as "Concatenation of Strings"*)
    forest_story_branch_black_berries_exceed= "\nUpon hearing this the town leader begins to get\n"
    forest_story_branch_black_berries_exceed+= "angry at you, you\’ve eaten way too many berries\n"
    forest_story_branch_black_berries_exceed+= "for them to help you on your journey. You're thrown\n"
    forest_story_branch_black_berries_exceed+= "into their town prison charged with excessive berry consumption.\n"
    
    #(*Refer to code block comment for this repeated sections Identified as "Concatenation of Strings"*)
    forest_story_branch_maths_input_correct= "Looks like you've earned our help " +player_name+",\n"
    forest_story_branch_maths_input_correct+= "our town wizards got just the thing for you. The town\n"
    forest_story_branch_maths_input_correct+= "leader leads you to a small hut were a the wizard resides\n"
    forest_story_branch_maths_input_correct+= ", you enter... Inside is a old-man with grey hair and pale\n"
    forest_story_branch_maths_input_correct+= "skin, he looks up and says \"sit down""I\ive been.\n"
    forest_story_branch_maths_input_correct+= "expecting you You ask how, he explains that he can see\n"
    forest_story_branch_maths_input_correct+= "into the past and future, he leans forward and says \"do you\n"
    forest_story_branch_maths_input_correct+= "want to know your real name? Your not sure what he means, you\n"
    forest_story_branch_maths_input_correct+= "say your names clearly " +player_name+" he shakes his head your\n"
    forest_story_branch_maths_input_correct+= "quite mistaken... your real name is\n"
    
    #(*Refer to code block comment for this repeated sections Identified as "Concatenation of Strings"*)
    forest_story_all_berries_exact= "\nThe town leader looks surprised, you’ve managed to eat just\n"
    forest_story_all_berries_exact+= "the right amount of the sacred berries. The people of the\n"
    forest_story_all_berries_exact+= "village begin to worship you as a messiah.\n"
    
    #The variable in question contains a floating-point number which when necessary is used in a comparison
    #operation with another variable which will be assigned the players input.
    #As this variable is used in two separate branches the name identifier doesn’t need to be overly complicated
    #as “correct_maths_awnser” is self-explanatory.
    #Although having the value 2.5 only be referenced in the relevant comparison operation is possible the current
    #method means it can be changed without the underlying language of the operation and conditions also needing to
    #be modified. 
    #Its position in the code overall means it is both visible before the if statements and while loops allowing a
    #variable to be changed outside of the statement and strings. 
    correct_maths_awnser = 2.5


    sys.stdout.write(main_story_start)
    
    #Stores the stripped line string data and assigns it to the variable associated with the main choice or
    #response.
    #The below conditions need to use in the comparison operations to display and progress down the relevant
    #branch and thus for this reason the variable is positioned above those and is given the name
    #“main_choice_response” over an alternative such as the first choice.
    #
    #If the naming scheme was developed around something like “the first choice” etc it would be too unspecific
    #and less descriptive than the current one as there are multiple cases where the first choice could be interpreted
    #as the first choice in terms of several choices to pick from rather than the main choice which references the main
    #storyline at the beginning.  
    main_choice_response = sys.stdin.readline().strip()
    
    #Allows a scenario where the player inputs an invalid response to the print statement, the while loop will repeatedly
    #indicate that their input wasn’t valid and needs to be either “one” or “two”.
    #Once that condition is met then the loop will terminate and progress onwards to the below if/elif statements.
    #The print statements along with the readlines cannot feasibly exist outside of this code block given the
    #requirements and constraints for this program, the closest alternative would be to contain these in a series
    #of functions and return them when needed, however as stated this isn’t possible in this instance.
    #If neither the main choice variable is neither value of “left” and the main choice variable is also neither the
    #value of “right” then the print statement will be used to notify the player that the response is invalid.
    #The if statement below the while-loop is only met if the main choice variable has the value assigned to it of
    #“left” when this is the case a print statement will display the player the “house_story_start” string.
    #Towards the end of this string similar to the other storylines or branches is a line containing text that will
    #prompt them again for a response which is then stripped and assigned to the house storyline first decision
    #response variable.
    #
    #*Refer to comment with the relevant justification for the mentioned variables*
    #
    #Another while loop is used to act in a scenario where an input entered by the player isn’t valid to the needs
    #of the program.
    #*This acts the same way as the previous while loop for the “main_choice_response” invalid input*
    #
    #Whether they enter a valid input or not the variable is then used in two comparison operations to determine which
    #of the print statements will be outputted to the player.
    #Upon the print statements final line, the return to function “main” will be carried out essentially restarting the
    #program again allowing the player to go down a separate path. 
    while (main_choice_response != "left" and main_choice_response != "right"):
        sys.stdout.write("\nEnter either left or right: \n")
        main_choice_response = sys.stdin.readline().strip()
        
    #When the variable storing the input from the user meets the condition of been equal to the string of
    #“left” a print statement outputs the start of the house storyline string which on the final line contains
    #a prompt for the user to input either one or two when they need to progress.
    #. Placement of this condition has been chosen based on the constraints of the program and overall practice
    #of if, elif, and else conditions, a while-loop isn’t needed as the return to the function “main” performs
    #this operation and for the remaining parts of the “house storyline” to be carried out it needs to be indented
    #in this fashion for the below conditions to be successful.
    #Alternatively having this particular condition and following nested conditions swap places with the similar
    #“right” main choice branch is reasonable and will not affect the program, whoever left is associated as the
    #first option in English and thus has been placed before the “right” main choice conditions and storyline. 
    if (main_choice_response == "left"):
        sys.stdout.write(house_story_start)
        house_storyline_first_decision_response = sys.stdin.readline().strip()
        
        #When the player inputs something that isn’t a valid response to the print statement of the house
        #storyline string, a while loop has been implemented to prevent them from progressing down the sub
        #house storyline.
        #When the variable “house_storyline_first_decision_response” isn’t equal to “one” and also isn’t
        #equal to “two” the player will be put into this loop until they enter a valid input to go forward.
        #This is indented as it is contained within the previous if statement and storyline.
        while (house_storyline_first_decision_response != "one" and house_storyline_first_decision_response
               != "two"):
            sys.stdout.write("\nInvalid Input: please enter one or two")
            house_storyline_first_decision_response = sys.stdin.readline().strip()
            
        #The condition is satisfied when the variables data is equal to the string of “one”.
        #The relevant variable data has already been assigned and checked for valid inputs to prevent a dead
        #end on this if condition.
        #Alternative naming of the variables and strings has already been considered and justified thus the
        #relevant condition has been simplified to a degree that reasonable and still fits within the constraints
        #of the program's design. 
        if (house_storyline_first_decision_response == "one"):
            sys.stdout.write(house_story_branch_1)
            
        #Elif condition operates similarly by checking the previous if condition.
        #*Justification has been documented in the previous comment minor changes include
        #the desired data contained within the “house_storyline_first_decision_respose” variable* 
        elif (house_storyline_first_decision_response == "two"):
            sys.stdout.write(house_story_branch_2)
            
            
    #When the users’ inputs have been checked by the initial while loop the below elif condition is run to check
    #for the variables data value, when the comparison operation determines that the variables stored string are
    #equal to “right” a print statement is performed.
    #Contained within the print statement is the reference to the “forest_story_start” single continues string which
    #contains the relevant text for the forest storyline.
    #Subsequently, upon that print statement completion another print statement containing a custom written string
    #asking the player to choose between two options.
    #After the player enters their input the line is stripped and assigned to the “eat_berries_response” variable
    #which is needed later on for intended conditions.
    #
    #The placement of this initial condition for the right storyline remains the same as the left, although it is
    #reasonable to swap its position as long as the indentation remains the same for the below conditions the program
    #will operate normally.
    #Whoever, the strings containing the relevant storylines have been ordered so that the “house storyline appears”
    #first underneath the “main storyline” string followed by the “forest storyline” string, thus having them be organized
    #and structured similarly increases readability. 
    elif (main_choice_response == "right"):
        sys.stdout.write(forest_story_start)
        sys.stdout.write("\nDo you want to eat the [one] blue berries or [two] black berries?: \n")

        #The following variable “eat_berries_response” is assigned its data from a readline strip which is used in
        #the below comparison operations to determine which relevant strings need to be printed to progress the story.
        #Specifically, this variable is used to determine if the player chooses to eat the blueberries or blackberries.
        #The naming scheme makes no mention of the berry type as other variables will need to identify that later on in
        #the program.
        #Although the data stored within the variable could be an integer equivalent of the current strings the storyline
        #already requires integer-based variables relating to berries which would confuse their purpose. 
        eat_berries_response = sys.stdin.readline().strip()
        
        #When a player inputs an invalid input that will fail to meet the below if conditions and comparisons a while loop
        #has been created to combat this scenario.
        #The variable containing the stripped line string from the player's input is compared to the below if conditions.
        #When it is neither equal to “one” and or “two” the user will be prompted to redo the input to progress.
        #
        #Placement justifications similar to previous conditions, given the overall structure, organization, naming schemes,
        #and constraints of the program in question the while loops location to progress forwards after a successful input
        #means that I need to be above the relevant if statements and conditions.
        while (eat_berries_response != "one" and eat_berries_response != "two"):
            sys.stdout.write("\nInvalid Input\n")
            sys.stdout.write("\nEnter either one or two(As a word not a number): \n")
            eat_berries_response = sys.stdin.readline().strip()
            
        if eat_berries_response == "one":
            sys.stdout.write("\nHow many blue berries do you eat?: \n")

            #When the user has viewed the outputted print statement containing the string of text indicator they
            #need to input a choice a variable is assigned whatever they input with it then been converted to an
            #integer value.
            #Naming scheme refers to relevant berry path they with the amount indicating that number value will be assigned to it.
            blue_berries_amount = int(sys.stdin.readline().strip())

            #Check’s value of the data assigned to the “blueberries amount” variable, if it’s negative the while-loop
            #keeps the user from progressing until they enter zero or more. 
            while(blue_berries_amount<0):
                sys.stdout.write("\nInvalid Input, You cannot enter a negative number: \n")

                #Will conver the readline value inputted by player to a interger.
                #Method to further avoid invalid inputs etc. 
                blue_berries_amount = int(sys.stdin.readline().strip())
                sys.stdout.write(forest_story_start_town_arrival)

            #If the value of the data stored within "blue_berries_amount is more than 20 then the relevant storyline
            #will be printed.
            #This is done through the below condition and comparision operation. 
            if (blue_berries_amount>20):
                    sys.stdout.write(forest_story_branch_blue_berries_exceed)
                    sys.stdout.write("*Hint: Next time try and not have "+ str(blue_berries_amount) +" blue berries.\n\n")
                    
            #When value of variable is less than 20 then the relevant storyline is carried out.       
            elif (blue_berries_amount<20):
                    sys.stdout.write(forest_story_branch_blue_berries_less)
                    sys.stdout.write("\nOk, say we divide 5 by 2... What do we get?: \n")

                    #Variable is assigned stripped readline value which is converted to a float.
                    #The name refers to the relevant storyline and branch including its nature
                    #which is to verify the maths the player has done.  
                    forest_story_blue_berries_verify_maths = float(sys.stdin.readline().strip())

                    #If statement and condition comparing values of both variables, if the maths
                    #question isn’t correct then relevant storyline is displayed with the print statement. 
                    if (forest_story_blue_berries_verify_maths != correct_maths_awnser):
                        sys.stdout.write("That awnser isn't correct, looks like your gonna need to go somewhere else " +player_name+ ".\n")
                        
                    #When a variable string is equal to the other variables string the relevant storyline is displayed.
                    #In all cases relating to this condition and variable, there is no way to handle unexpected inputs
                    #from the player as per the constraints of the program. 
                    elif (forest_story_blue_berries_verify_maths == correct_maths_awnser):
                        sys.stdout.write(forest_story_branch_maths_input_correct)
                        
            #The below condition will carry out if the player inputs the exact integer number of 20.
            #The arrangement and position purpose is to allow a scenario where a player happens to
            #enter exactly 20 in response to the prompt with the subsequent line been stripped and
            #assigned to a variable. 
            else:
                sys.stdout.write(forest_story_all_berries_exact)
                
        #Below code block and indented conditions remain similar to previous with minor changes to the
        #variable naming schemes and string variables that are printed to the player.
        #Decisions made here remain the same, as the storyline essentially plays out in the same way with
        #the only changes being to the nature of the “berry variables” the player chose.
        #
        #While loop is created to handle invalid inputs which end only when the player inputs a valid input.
        #If statements operate to channel the storyline down a certain path displaying the approach variable
        #when needed.
        #
        #Alternatives that might be considered is a list implementation of sorts with the code block remaining
        #the same with the variable called upon been the only thing that changes, however considering the
        #restrictions and overall simplicity of the current method the implementation with the constraints in
        #mind seems to be the best option. 
        elif (eat_berries_response == "two"):
            sys.stdout.write("\nHow many black berries do you eat?: \n")
            black_berries_amount = int(sys.stdin.readline().strip())
            
            while (black_berries_amount<0):
                sys.stdout.write("\nInvalid Input, You cannot enter a negative number: \n")
                black_berries_amount = int(sys.stdin.readline().strip())
                sys.stdout.write(forest_story_start_town_arrival)
                
            if (black_berries_amount>20):
                    sys.stdout.write(forest_story_branch_black_berries_exceed)
                    sys.stdout.write("*Hint: Next time try and not have "+ str(black_berries_amount) +" black berries.\n\n")
                    
            elif (black_berries_amount<20):
                    sys.stdout.write(forest_story_branch_black_berries_less)
                    sys.stdout.write("\nOk, say we divide 5 by 2... What do we get?: \n")
                    forest_story_black_berries_verfiy_maths= float(sys.stdin.readline().strip())
                    
                    if (forest_story_black_berries_verfiy_maths != correct_maths_awnser):
                        sys.stdout.write("That awnser isn't correct, looks like your gonna need to go somewhere else " +player_name+ ".\n")
                        
                    elif (forest_story_black_berries_verfiy_maths == correct_maths_awnser):
                        sys.stdout.write(forest_story_branch_maths_input_correct)
                        
            else:
                sys.stdout.write(forest_story_all_berries_exact)

    sys.stdout.write("\n====THE==END====\n")

    #Returns everything contained in the function "main".             
    return main()
main()
