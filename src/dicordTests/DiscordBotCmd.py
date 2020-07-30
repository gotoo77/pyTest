from datetime import date
from datetime import datetime


# Function to convert list into string
def list_to_string(f_list):
    # initialize an empty string
    convert_to_str = ""
    # traverse in the string
    for list_elem in f_list:
        convert_to_str += list_elem + ","
    # return string
    return convert_to_str


"""
DiscordBotCmd :cette classe encapsule les commandes du bot Discord
"""


class DiscordBotCmd:
    """
    init for this class
    """
    def __init__(self):
        self.list_of_commands = []  # creates a new empty list for each command
        self.list_of_commands.append("!time")
        self.list_of_commands.append("!hi")
        self.list_of_commands.append("!list")
        self.list_of_commands.append("!hangman")
    """ 
    say list of commands
    """
    def list(self):
        str1 = "list_of_commands is : "
        # using list comprehension
        cmdLst_str = list_to_string(self.list_of_commands)
        resp = " ".join((str1, cmdLst_str))
        # resp = "known commands are : " + str(self.cmds).strip('[]')
        return resp

    """ 
    what is the date today ? :D
    """
    def time(self):
        now = datetime.now()  # current date and time
        year = now.strftime("%Y")
        # print("year:", year)
        month = now.strftime("%m")
        # print("month:", month)
        day = now.strftime("%d")
        # print("day:", day)
        time = now.strftime("%H:%M:%S")
        # print("time:", time)
        date_time = now.strftime("%d/%m/%Y, %H:%M:%S")
        # print("date and time:", date_time)
        return date_time
