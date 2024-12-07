import csv
import random

wordfile = "words.csv"
userfile = "users.csv"

master_pwd = "1234"

game1 = "Word Guess"
game2 = "Word Match"
game3 = "Letter Hunt"

subject1 = "math"
subject2 = "science"
subject3 = "history"
subject4 = "art"
subject5 = "computer science"

easy = "easy"
normal = "normal"
hard = "hard"

max_level = 3
number_of_difficulty = 3
max_total_level_for_each_subject = max_level * number_of_difficulty
number_of_subjects = 5
max_total_level_for_each_game = max_total_level_for_each_subject * number_of_subjects
number_of_games = 3
max_total_level = max_total_level_for_each_game * number_of_games

def write_userlist(users):
    with open(userfile, "w", newline="") as users_csv:
        write_csv = csv.writer(users_csv)   #Writing header to csv
        write_csv.writerow(["username","password","game 1 subject 1 difficulty 1","g1s2d1","g1s3d1","g1s4d1","g1s5d1","g1s1d2","g1s2d2","g1s3d2","g1s4d2","g1s5d2","g1s1d3","g1s2d3","g1s3d3","g1s4d3","g1s5d3",
                                                  "g2s1d1","g2s2d1","g2s3d1","g2s4d1","g2s5d1","g2s1d2","g2s2d2","g2s3d2","g2s4d2","g2s5d2","g2s1d3","g2s2d3","g2s3d3","g2s4d3","g2s5d3",
                                                  "g3s1d1","g3s2d1","g3s3d1","g3s4d1","g3s5d1","g3s1d2","g3s2d2","g3s3d2","g3s4d2","g3s5d2","g3s1d3","g3s2d3","g3s3d3","g3s4d3","g3s5d3",
                                                  "Total Score","Total progress",
                                                  game1,game2,game3,
                                                  subject1,subject2,subject3,subject4,subject5,
                                                  easy,normal,hard
                            ])
        for user in users:   #It writes each data of each user  in the user dictionarry to a CSV file
            write_csv.writerow([user,users[user]["pwd"],users[user]["progress"][game1][subject1][easy],users[user]["progress"][game1][subject1][normal],users[user]["progress"][game1][subject1][hard],
                                                        users[user]["progress"][game1][subject2][easy],users[user]["progress"][game1][subject2][normal],users[user]["progress"][game1][subject2][hard],
                                                        users[user]["progress"][game1][subject3][easy],users[user]["progress"][game1][subject3][normal],users[user]["progress"][game1][subject3][hard],
                                                        users[user]["progress"][game1][subject4][easy],users[user]["progress"][game1][subject4][normal],users[user]["progress"][game1][subject4][hard],
                                                        users[user]["progress"][game1][subject5][easy],users[user]["progress"][game1][subject5][normal],users[user]["progress"][game1][subject5][hard],

                                                        users[user]["progress"][game2][subject1][easy],users[user]["progress"][game2][subject1][normal],users[user]["progress"][game2][subject1][hard],
                                                        users[user]["progress"][game2][subject2][easy],users[user]["progress"][game2][subject2][normal],users[user]["progress"][game2][subject2][hard],
                                                        users[user]["progress"][game2][subject3][easy],users[user]["progress"][game2][subject3][normal],users[user]["progress"][game2][subject3][hard],
                                                        users[user]["progress"][game2][subject4][easy],users[user]["progress"][game2][subject4][normal],users[user]["progress"][game2][subject4][hard],
                                                        users[user]["progress"][game2][subject5][easy],users[user]["progress"][game2][subject5][normal],users[user]["progress"][game2][subject5][hard],

                                                        users[user]["progress"][game3][subject1][easy],users[user]["progress"][game3][subject1][normal],users[user]["progress"][game3][subject1][hard],
                                                        users[user]["progress"][game3][subject2][easy],users[user]["progress"][game3][subject2][normal],users[user]["progress"][game3][subject2][hard],
                                                        users[user]["progress"][game3][subject3][easy],users[user]["progress"][game3][subject3][normal],users[user]["progress"][game3][subject3][hard],
                                                        users[user]["progress"][game3][subject4][easy],users[user]["progress"][game3][subject4][normal],users[user]["progress"][game3][subject4][hard],
                                                        users[user]["progress"][game3][subject5][easy],users[user]["progress"][game3][subject5][normal],users[user]["progress"][game3][subject5][hard],

                                                        users[user]["score"]["Total Score"],
                                                        users[user]["score"]["Total progress %"],
                                                        users[user]["score"][game1],users[user]["score"][game2],users[user]["score"][game3],
                                                        users[user]["score"][subject1],users[user]["score"][subject2],users[user]["score"][subject3],users[user]["score"][subject4],users[user]["score"][subject5],
                                                        users[user]["score"][easy],users[user]["score"][normal],users[user]["score"][hard],
                                ])
                                                        
def read_userlist():
    users = {}
    with open(userfile, "r", newline="") as users_csv:
        read_csv = csv.reader(users_csv)
        next(read_csv)
        for row in read_csv:  #Each line in the CSV represents a user. Imports the data from each row into the user's dictionarry
            users[row[0]] = {"pwd":row[1],
                             "progress":{game1:{subject1:{easy:int(row[2]),normal:int(row[3]),hard:int(row[4])},
                                                subject2:{easy:int(row[5]),normal:int(row[6]),hard:int(row[7])},
                                                subject3:{easy:int(row[8]),normal:int(row[9]),hard:int(row[10])},
                                                subject4:{easy:int(row[11]),normal:int(row[12]),hard:int(row[13])},
                                                subject5:{easy:int(row[14]),normal:int(row[15]),hard:int(row[16])}},
                                         game2:{subject1:{easy:int(row[17]),normal:int(row[18]),hard:int(row[19])},
                                                subject2:{easy:int(row[20]),normal:int(row[21]),hard:int(row[22])},
                                                subject3:{easy:int(row[23]),normal:int(row[24]),hard:int(row[25])},
                                                subject4:{easy:int(row[26]),normal:int(row[27]),hard:int(row[28])},
                                                subject5:{easy:int(row[29]),normal:int(row[30]),hard:int(row[31])}},
                                         game3:{subject1:{easy:int(row[32]),normal:int(row[33]),hard:int(row[34])},
                                                subject2:{easy:int(row[35]),normal:int(row[36]),hard:int(row[37])},
                                                subject3:{easy:int(row[38]),normal:int(row[39]),hard:int(row[40])},
                                                subject4:{easy:int(row[41]),normal:int(row[42]),hard:int(row[43])},
                                                subject5:{easy:int(row[44]),normal:int(row[45]),hard:int(row[46])}}
                                         },
                             "score":{"Total Score":int(row[47]),
                                              "Total progress %":float(row[48]),
                                              game1:int(row[49]),game2:int(row[50]),game3:int(row[51]),
                                              subject1:int(row[52]),subject2:int(row[53]),subject3:int(row[54]),subject4:int(row[55]),subject5:int(row[56]),
                                              easy:int(row[57]),normal:int(row[58]),hard:int(row[59])                                              
                                              }
                            }
        return(users)

def read_dictionary():
    global worddict
    worddict = {}
    with open(wordfile, "r", newline="") as words_csv:
        read_csv = csv.reader(words_csv)
        next(read_csv)
        for row in read_csv:
            subject = row[0]   #I have made temporary assignments for ease of understanding
            difficulty = row[1]
            level = row[2]
            word = row[3]
            definition = row[4]
            if subject not in worddict:  #If there is no dictionary on that subject, create a new dictionary
                worddict[subject] = {}
            if difficulty not in worddict[subject]:   #If there is no dictionary on this difficulty in the subject, create a new dictionary
                worddict[subject][difficulty] = {}
            if level not in worddict[subject][difficulty]:   #If there is no dictionary on this level in this difficulty in the subject, create a new dictionary
                worddict[subject][difficulty][level] = {}
            worddict[subject][difficulty][level][word] = definition   #Place the word and definition in correct subject-difficulty-level dictionary

def login(users):
    username = input("Username:")
    while username not in users:    #Confirms the existence of the User
        print("Not existing username. Try another username or press enter to go menu.")
        username = input("Username:")
        if username == "":  #If the user cannot remember their username, they can press enter and go back.
            enter = False
            return(username,enter)
    password = input("Password:")
    while password != users[username]["pwd"]:
        print("Incorrect password. Try another password or press enter to go menu.")
        password = input("Password:")
        if password == "":  #If the user cannot remember their password, they can press enter and go back.
            enter = False
            return(username,enter)        
    print(f"Login successful. \nWelcome {username}!")
    enter = True
    return(username,enter)

def register(users):
    username = input("Username:")
    while username in users:  #Prevents username duplication
        print("Username already exists. Try another username or press enter to go menu.")
        username = input("Username:")
        if username == "":
            enter = False
            return(username,users,enter)      
    password = input("Password:")
    while password == "":
        print("You need to choose a password!")
        password = input("Password:")
    check_password = input("Re-enter password:")  
    while password != check_password:  #Double checking for password
        print("Passwords do not match. Type again.")
        password = input("Password:")
        check_password = input("Re-enter password:")
    #Creating new user's username, password and other dictionaries used for progress in Users dictionarry
    users[username] = {"pwd":password,"progress":{
                                                game1:{
                                                    subject1:{easy:1,normal:1,hard:1},
                                                    subject2:{easy:1,normal:1,hard:1},
                                                    subject3:{easy:1,normal:1,hard:1},
                                                    subject4:{easy:1,normal:1,hard:1},
                                                    subject5:{easy:1,normal:1,hard:1}},
                                                game2:{
                                                    subject1:{easy:1,normal:1,hard:1},
                                                    subject2:{easy:1,normal:1,hard:1},
                                                    subject3:{easy:1,normal:1,hard:1},
                                                    subject4:{easy:1,normal:1,hard:1},
                                                    subject5:{easy:1,normal:1,hard:1}},
                                                game3:{
                                                    subject1:{easy:1,normal:1,hard:1},
                                                    subject2:{easy:1,normal:1,hard:1},
                                                    subject3:{easy:1,normal:1,hard:1},
                                                    subject4:{easy:1,normal:1,hard:1},
                                                    subject5:{easy:1,normal:1,hard:1}}
                                            },
                                        "score":{   
                                            "Total Score":0,
                                            "Total progress %":0,
                                            game1:0,game2:0,game3:0,
                                            subject1:0,subject2:0,subject3:0,subject4:0,subject5:0,
                                            easy:0,normal:0,hard:0                                              
                                              }
                       }
    print(f"User succesfully created. \nWelcome {username}!")
    write_userlist(users)
    enter = True
    return(username,users,enter)

def forgot_password(users):
    print("Talk with your tutor.")
    while True:
        tutor_login = input("Press enter to go menu or if you are a tutor, type master password(****Master password:1234****):")
        #I wrote the master passcode here so that you can check the function. Otherwise it will not be written in the original version.
        if tutor_login == "":
            return
        else:
            if tutor_login == master_pwd:
                print("")
                while True:
                    print("1-Show all username and passwords")   #Password recovery option with teacher login
                    print("2-Enter username")
                    print("3-Return menu")
                    choice = input("Choice:")
                    print("")
                    if choice == "1":
                        for user,details in users.items():
                            print(f"{user} : {details["pwd"]}")
                    elif choice == "2":
                        username = input("Username:")
                        if username in users:
                            print(f"{username}'s password: {users[username]["pwd"]}")
                        else:
                            print("Username not exists.")                       
                    elif choice == "3":
                        return
                    else:
                        print("Invalid choice.")
                    print("")
            else:
                print("Wrong password.")

def calculate_score(users,username):  #User score calculation with for loop in user data
    users[username]["score"]["Total Score"] = sum(values-1 for game in users[username]["progress"].values() for subject in game.values() for values in subject.values())
    users[username]["score"]["Total progress %"] = round(((sum(values-1 for game in users[username]["progress"].values() for subject in game.values() for values in subject.values()))/175*100),1)
    users[username]["score"][game1] =  sum(values-1 for subject in users[username]["progress"][game1].values() for values in subject.values())  #Collects all of game1 scores.
    users[username]["score"][game2] =  sum(values-1 for subject in users[username]["progress"][game2].values() for values in subject.values())
    users[username]["score"][game3] =  sum(values-1 for subject in users[username]["progress"][game3].values() for values in subject.values())
    users[username]["score"][subject1] = sum(values-1 for game in users[username]["progress"].values() for values in game[subject1].values()) #Collects subject 1 scores in each game
    users[username]["score"][subject2] = sum(values-1 for game in users[username]["progress"].values() for values in game[subject2].values())
    users[username]["score"][subject3] = sum(values-1 for game in users[username]["progress"].values() for values in game[subject3].values())
    users[username]["score"][subject4] = sum(values-1 for game in users[username]["progress"].values() for values in game[subject4].values())
    users[username]["score"][subject5] = sum(values-1 for game in users[username]["progress"].values() for values in game[subject5].values())
    users[username]["score"][easy] = sum(subject[easy]-1 for game in users[username]["progress"].values() for subject in game.values())  #Collects easy difficulty scores for each game and subject
    users[username]["score"][normal] = sum(subject[normal]-1 for game in users[username]["progress"].values() for subject in game.values())
    users[username]["score"][hard] = sum(subject[hard]-1 for game in users[username]["progress"].values() for subject in game.values())
    #The reason for writing "values-1" in all of them is to store the level in user data. 
    #However, what we need here are not the level user on, the levels made before. That's why they all have "-1".
    #All calculations are saved in the users dictionary

def choose_difficulty(users,username,game_choice,subject_choice):
    print("")
    print(f"1-Easy - Progress: {users[username]["progress"][game_choice][subject_choice][easy]-1}/{max_level}")
    print(f"2-Normal - Progress: {users[username]["progress"][game_choice][subject_choice][normal]-1}/{max_level}")
    print(f"3-Hard - Progress: {users[username]["progress"][game_choice][subject_choice][hard]-1}/{max_level}")
    print(f"4-Go back")
    while True:
        difficulty_choice = input("Choice:")
        if difficulty_choice == "1":
            difficulty_choice = easy
        elif difficulty_choice == "2":
            difficulty_choice = normal
        elif difficulty_choice == "3":
            difficulty_choice = hard
        elif difficulty_choice == "4":
            return(difficulty_choice)
        else:
            print("Invalid option.")
            continue
        if users[username]["progress"][game_choice][subject_choice][difficulty_choice]-1 == max_level:
            print("You already completed this difficulty. Please choose another difficulty or go back.")
            continue
        break
    return(difficulty_choice)

def choose_subject(users,username,game_choice):
    if sum(values-1 for subject in users[username]["progress"][game_choice].values() for values in subject.values()) == max_total_level_for_each_game:
        print("You already completed this game. Please choose another game or exit.")
        subject_choice = "6"
        return(subject_choice)
    print("")
    print(f"1-{subject1} - Progress: {sum(difficulty-1 for difficulty in users[username]["progress"][game_choice][subject1].values())}/{max_total_level_for_each_subject}")
    print(f"2-{subject2} - Progress: {sum(difficulty-1 for difficulty in users[username]["progress"][game_choice][subject2].values())}/{max_total_level_for_each_subject}")
    print(f"3-{subject3} - Progress: {sum(difficulty-1 for difficulty in users[username]["progress"][game_choice][subject3].values())}/{max_total_level_for_each_subject}")
    print(f"4-{subject4} - Progress: {sum(difficulty-1 for difficulty in users[username]["progress"][game_choice][subject4].values())}/{max_total_level_for_each_subject}")
    print(f"5-{subject5} - Progress: {sum(difficulty-1 for difficulty in users[username]["progress"][game_choice][subject5].values())}/{max_total_level_for_each_subject}")
    print(f"6-Go back")
    subject_choice = input("Choice:")

    while True:
        if subject_choice == "1":
            subject_choice = subject1
        elif subject_choice == "2":
            subject_choice = subject2
        elif subject_choice == "3":
            subject_choice = subject3
        elif subject_choice == "4":
            subject_choice = subject4
        elif subject_choice == "5":
            subject_choice = subject5
        elif subject_choice == "6":
            return(subject_choice)           
        else:
            subject_choice = input("Invalid choice. Type again:")
            continue
        if sum(difficulty-1 for difficulty in users[username]["progress"][game_choice][subject_choice].values()) == max_total_level_for_each_subject:
                print("You completed this subject already. Choose another one or press 6 to go back.")  
                subject_choice = input("Choice:")
        else:
            return(subject_choice)
    
def game1_word_guess(word,definition):      #The game functions are short because I have done common operations with the help of functions.
    print(f"\nDefinition: {definition}")    #I gave only "word", "definition" variables to these 3 game functions and made them return True or False with "answer" variable.
    print("Guess the word")
    attempt = 0
    while True:
        guess = input("Word:")
        if guess.lower() == word.lower():
            print("\nCorrect!")
            answer = True
            return(answer)
        else:
            print("\nWrong. Guess again.")
            attempt += 1
        if attempt == 2:                        #On 2 incorrect attempts I gave the first letter of the word as a clue
            print(f"First letter: {word[0]}")
        elif attempt == 4:
            print(word[0], end=" ")             #In 4 incorrect attempts I gave the first letter and length of the word as a clue
            for letter in range(len(word)-1):
                print('_', end=' ')
            print(" ")
        elif attempt == 6:                      #6 incorrect attempts, the right of error expires and has to start all over again
            print(f"\nWord was: {word}")        #All these 3 numbers can be changed to make the game easier or harder.
            answer = False
            return(answer)
def game2_word_match(word,definition):    #Gives the user 5 words and 1 definition and asks for the word belonging to the given definition
    print(f"Definition: {definition}")
    print("Guess the word")
    attempt = 0
    while True:
        guess = input("Word:")
        if guess.lower() == word.lower():
            print("\nCorrect!")
            answer = True
            return(answer)
        else:
            attempt += 1
            if attempt == 2:                    #2 incorrect attempts, the right of error expires and has to start all over again
                print(f"\nWord was: {word}")
                answer = False
                return(answer)
            print("\nWrong. Guess again.")

def game3_letter_hunt(word,definition):   #It gives the user the length of the word and ask a letter guess
    word = word.lower()
    wrong_attempt = 0
    letters = []
    wrong_letters = []
    print(f"\nDefinition: {definition}\n")
    print("Word:", end=" ")
    for i in word:
            if i == " ":
                print(" ", end=" ")
            else:
                print("_", end=" ")
    while True:
        answer = True
        letter = input("\nGuess letter:").lower()
        while letter == "":
            letter = input("\nInvalid letter.\nGuess letter:")
        if letter in letters:
            print(f"You already type {letter}")
            continue
        else:
            letters.append(letter)
        if letter == word:
            return(answer)
        if letter not in word:
            wrong_letters.append(letter)
            wrong_attempt += 1
            answer = False
            if wrong_attempt > 7:      #7 incorrect attempts, the right of error expires and has to start all over again
                print(f"Word was: {word}")
                return(answer)
        print(f"\nRemaining attempt: {8-wrong_attempt}")
        print("Non-existent letters: ", end=' ')
        print(*wrong_letters)
        for i in word:
            if i in letters or i == " ":
                print(i, end=' ')
            else:
                print('_', end=' ')
                answer = False
        if answer == True:
            print("\nCorrect!")
            print(f"Word is {word}\n")
            break
    return(answer)

def game_menu(users,username,game_choice): #I made a common game_menu function for 3 games because I needed to select the subject and difficulty before each game. 
    #Also, according to this data, I learnt the progress of the related level from user data and accessed the word-definition pair related to that level from word dictionary.
    return_selection = "Choose subject"
    while return_selection == "Choose subject":
        subject_choice = choose_subject(users,username,game_choice)
        if subject_choice == "6":
            return()
        return_selection = "Choose difficulty"
        while return_selection == "Choose difficulty":
            difficulty_choice = choose_difficulty(users,username,game_choice,subject_choice)
            if difficulty_choice == "4":
                return_selection = "Choose subject"
                continue
            return_selection = "1"
            while return_selection == "1":
                level = users[username]["progress"][game_choice][subject_choice][difficulty_choice]  
                #It takes the level of the relevant difficulty level of the relevant subject of the relevant game of the relevant user stored in the user data and assigns it to the "level" variable.
                #Because we will use it to get the words of the related level from the "worddict" dictionary.
                print("")
                print(f"Game: {game_choice}")
                print(f"Subject: {subject_choice}")
                print(f"Difficulty: {difficulty_choice}")
                print(f"Level: {level}")           
                question = 1
                for word,definition in worddict[subject_choice][difficulty_choice][str(level)].items():
                    if game_choice == game1:
                        answer = game1_word_guess(word,definition)
                    elif game_choice == game2:
                        word_list = list(worddict[subject_choice][difficulty_choice][str(level)].keys())
                        random.shuffle(word_list)
                        print("\nWords: " + " - ".join(word_list))
                        answer = game2_word_match(word,definition)
                    elif game_choice == game3:
                        answer = game3_letter_hunt(word,definition)
                    if answer == False:
                        print("")
                        print("You didn't pass the level.")
                        print("1-Start over on the same level.")          #Although it is difficult to control nested functions and while loops,
                        print("2-Return to the difficulty selection.")    #I offered the user the opportunity to return to whichever menu he wants.
                        print("3-Return to the subject selection.")
                        print("4-Return to the main menu.")
                        return_selection = input("Choice:")    
                        while return_selection not in ["1","2","3","4"]:
                            print("Invalid choice.Try again.")
                            return_selection = input("Choice:")
                        if return_selection == "1":
                            break
                        elif return_selection == "2":
                            return_selection = "Choose difficulty"
                            break
                        elif return_selection == "3":
                            return_selection = "Choose subject"
                            break
                        elif return_selection == "4":
                            return_selection = "Main menu"
                            return
                    if question < 5:
                        if answer == True:
                            answer = False
                            question += 1
                            print("\n1-New word")
                            print("2-Go back (Your progress will not be recorded because you have not completed 5 words at this level.)")
                            new_question = input("Choice:")
                            while new_question not in ["1","2"]:
                                new_question = input("Invalid choice.Type again.Choice:")
                            if new_question == "2":
                                return_selection = "Choose difficulty"
                                break
                if answer == True:   #After exiting the previous for loop, the level is complete.
                    #At this stage, the aim is to save the progress in the user data and send the user to the next menu.
                    users[username]["progress"][game_choice][subject_choice][difficulty_choice] += 1   #Increases the level in the recording by one level.
                    calculate_score(users,username)
                    write_userlist(users)
                    if sum(values-1 for game in users[username]["progress"].values() for subject in game.values() for values in subject.values()) == max_total_level:
                        #If the sum of all levels in the user data is equal to the max level, it means that the user has completed all games.
                        print("")
                        print("!!!!!!YOU FINISHED THE GAME!!!!!!")
                        print("")
                        break
                    elif sum(values-1 for subject in users[username]["progress"][game1].values() for values in subject.values()) == max_total_level_for_each_game:
                        #If the sum of this game levels in the user data equals the maximum level, the user has completed this game.
                        print(f"Congratulations! You have completed {game_choice}.")
                        break
                    elif sum(difficulty-1 for difficulty in users[username]["progress"][game_choice][subject_choice].values()) == max_total_level_for_each_subject:
                        #If the sum of this subjects all difficulty levels in the user data equals the maximum level, the user has completed this subject.
                        print(f"Congratulations! You have completed {subject_choice}")
                        return_selection = "Choose subject"   #In the previous function, this variable will be used to return to the subject selection.
                        break
                    elif users[username]["progress"][game_choice][subject_choice][difficulty_choice] == 4:
                        #When the level kept in the user data passes level 3 and becomes 4, that difficulty is completed. 
                        print(f"You have completed {subject_choice} - {difficulty_choice} difficulty.")
                        return_selection = "Choose difficulty"  #In the previous function, this variable will be used to return to the difficulty selection.
                        break
                    else: #If the above statements are not fulfilled, it means that there is still more level left in this difficulty level.
                        print("")
                        print(f"You have completed {level}. level.")
                        print("1-Start next level.")
                        print("2-Return to the difficulty selection.")   #Thanks to the layered use of both function and while loops, it is possible to return to the desired part at any stage.
                        print("3-Return to the subject selection.")
                        print("4-Return to the main menu.")
                        return_selection = input("Choice:")
                        while return_selection not in ["1","2","3","4"]:
                            print("Invalid choice.Try again.")
                            return_selection = input("Choice:")
                        if return_selection == "1":
                            continue
                        elif return_selection == "2":
                            return_selection = "Choose difficulty"
                            break
                        elif return_selection == "3":
                            return_selection = "Choose subject"
                            break
                        elif return_selection == "4":
                            return_selection = "Main menu"
                            return
                        
def progress(users,username):  #Show progress function
    print("\nTotal correctly recognised words: ", sum(values-1 for game in users[username]["progress"].values() for subject in game.values() for values in subject.values())*5,"/875",sep="")
    print(f"Your Total Score: {users[username]["score"]["Total Score"]}")
    print(f"Your Total Progress: %{users[username]["score"]["Total progress %"]}")
    total_user_ranking = sorted(users.items(), key=lambda user: user[1]["score"]["Total Score"], reverse=True)  #Function that ranks all users by "Total Score"
    for i, (user, data) in enumerate(total_user_ranking, 1):  #I numbered everyone according to the order in the ranked score list
            if user == username:                              #I learnt to use the enumerate function as I mentioned in Reference
                print(f"You're ranked {i} out of everyone.")
    while True:
        print("")
        print("Progress:")
        print("1-Your detailed progress")
        print("2-All list")
        print("3-All detailed")
        print("4-Go back")
        choice = input("Choice:")
        while choice not in ["1","2","3","4"]:
            choice = input("Invalid. Try again. Choice:")
        if choice == "1":        
            print("-----")
            print(f"Your {game1} score: {users[username]["score"][game1]}")
            print(f"Your {game2} score: {users[username]["score"][game2]}")
            print(f"Your {game3} score: {users[username]["score"][game3]}")
            print("---")
            print(f"Your {subject1} score: {users[username]["score"][subject1]}")
            print(f"Your {subject2} score: {users[username]["score"][subject2]}")
            print(f"Your {subject3} score: {users[username]["score"][subject3]}")
            print(f"Your {subject4} score: {users[username]["score"][subject4]}")
            print(f"Your {subject5} score: {users[username]["score"][subject5]}")
            print("---")
            print(f"Your {easy} score: {users[username]["score"][easy]}")
            print(f"Your {normal} score: {users[username]["score"][normal]}")
            print(f"Your {hard} score: {users[username]["score"][hard]}")
            print("-----")
        elif choice == "2":
            print("\nAll users scores:")
            for i, (user, data) in enumerate(total_user_ranking, 1):
                print(f"{i}. {user}: {data["score"]["Total Score"]}")
        elif choice == "3":  #Detailed game, subject and difficulty level based score lists
            print("")
            print("1-Ranking by games")
            print("2-Ranking by subjects")
            print("3-Ranking by difficulties")
            print("4-Go back")
            detailed_choice = input("Choice:")
            while detailed_choice not in ["1","2","3","4"]:
                detailed_choice = input("Invalid. Try again. Choice:")
            if detailed_choice == "1":  #It shows users according to the scores of the selected game.
                print("")
                print(f"1-{game1}")
                print(f"2-{game2}")
                print(f"3-{game3}")
                print("4-Go back")
                choice = input("Choice:")
                while choice not in ["1","2","3","4"]:
                    choice = input("Invalid. Try again. Choice:")
                if choice == "1":
                    game = game1
                elif choice == "2":
                    game = game2
                elif choice == "3":
                    game = game3   
                game_ranking = sorted(users.items(), key=lambda user: user[1]["score"][game], reverse=True)
                print(f"\n{game.capitalize()} ranking of all players:")
                for i, (user, data) in enumerate(game_ranking, 1):
                    print(f"{i}. {user}: {data["score"][game]}")      
                else:
                    continue
            elif detailed_choice == "2":  #It shows users according to the scores of the selected subject.
                print("")
                print(f"1-{subject1}")
                print(f"2-{subject2}")
                print(f"3-{subject3}")
                print(f"4-{subject4}")
                print(f"5-{subject5}")
                print("6-Go back")
                choice = input("Choice:")
                while choice not in ["1","2","3","4","5","6"]:
                    choice = input("Invalid. Try again. Choice:")
                if choice == "1":
                    subject = subject1
                elif choice == "2":
                    subject = subject2
                elif choice == "3":
                    subject = subject3
                elif choice == "4":
                    subject = subject4
                elif choice == "5":
                    subject = subject5
                else:
                    continue
                subject_ranking = sorted(users.items(), key=lambda user: user[1]["score"][subject], reverse=True)
                print(f"\n{subject.capitalize()} ranking of all players:")
                for i, (user, data) in enumerate(subject_ranking, 1):
                    print(f"{i}. {user}: {data["score"][subject]}")  
            elif detailed_choice == "3":  #It shows users according to the scores of the selected difficulty
                print("")
                print(f"1-{easy}")
                print(f"2-{normal}")
                print(f"3-{hard}")
                print("4-Go back")
                choice = input("Choice:")
                while choice not in ["1","2","3","4"]:
                    choice = input("Invalid. Try again. Choice:")
                if choice == "1":
                    difficulty = easy
                elif choice == "2":
                    difficulty = normal
                elif choice == "3":
                    difficulty = hard  
                difficulty_ranking = sorted(users.items(), key=lambda user: user[1]["score"][difficulty], reverse=True)
                print(f"\n{difficulty.capitalize()} ranking of all players:")
                for i, (user, data) in enumerate(difficulty_ranking, 1):
                    print(f"{i}. {user}: {data["score"][difficulty]}")      
                else:
                    continue
            else:
                continue
        else:
            break

def change_password(users,username):
    password = input("New password:")
    check_password = input("Re-enter new password:")
    while password != check_password:
        print("Passwords do not match. Type again.")
        password = input("Password:")
        check_password = input("Re-enter password:")
    users[username]["pwd"] = password
    write_userlist(users)
    print("Password succesfully changed.")
    return(users)
       
def user_menu(users,username):  #Main menu after the user logs in
    while True:
        print("")
        print(f"1-{game1} - Progress: {sum(values-1 for subject in users[username]["progress"][game1].values() for values in subject.values())}/{max_total_level_for_each_game}")
        print(f"2-{game2} - Progress: {sum(values-1 for subject in users[username]["progress"][game2].values() for values in subject.values())}/{max_total_level_for_each_game}")
        print(f"3-{game3} - Progress: {sum(values-1 for subject in users[username]["progress"][game3].values() for values in subject.values())}/{max_total_level_for_each_game}")
        print(f"4-Show progress")
        print(f"5-Change password")
        print(f"6-Log out")
        game_choice = input("Choice:")
        if game_choice == "1":
            game_choice = game1    #I linked the game_choice variable to game to simplify the code
            game_menu(users,username,game_choice)
        elif game_choice == "2":
            game_choice = game2
            game_menu(users,username,game_choice)
        elif game_choice == "3":
            game_choice = game3
            game_menu(users,username,game_choice)
        elif game_choice == "4":
            progress(users,username)
        elif game_choice == "5":
            change_password(users,username)
        elif game_choice == "6":
            return(users)
        elif game_choice not in ["1","2","3","4","5","6"]:
            print("Invalid choice.")

def main():
    while True:
        users = read_userlist()
        read_dictionary()
        print("")
        print("1-Login")
        print("2-New user")
        print("3-Forgot password")
        print("4-Exit")
        choice = input("Choice:")
        enter = False
        if choice == "1":
            username,enter = login(users)
        elif choice == "2":
            username,users,enter = register(users)
        elif choice == "3":
            forgot_password(users)
        elif choice == "4":
            exit()
        else:
            print("Invalid choice.\n")
        if enter == True:
            user_menu(users,username)
            calculate_score(users,username)
            write_userlist(users)

main()
