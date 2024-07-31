class Wool:
    """
    The Wool class represents a wool object.

    Attributes:
    - title: The title of the wool dialog.
    - speaker: The speaker of the wool dialog.
    - position: The position of the wool dialog.
    - color: The color of the wool dialog.
    - variable_name: The name of the variable.
    - value: The value of the variable.
    - specificity: The specificity of the wool object.
    - frequency: The frequency of the wool object.
    - attainability: The attainability of the wool object.
    """
    def __init__(self):
        self.title = ""
        self.speaker = "Coach"
        self.position = (-416,112)
        self.color = "cyan"
        self.variable_name = ""
        self.value = ""
        self.specificity = ""
        self.frequency = ""
        self.attainability = ""

    def structure(self) -> str:
        """
        Prints the structure of the Wool object.

        @return: The structure of the Wool object as a string.
        """
        struc = "title: " + self.title + "\nspeaker: " + self.speaker + "\nposition: " + \
                str(self.position[0]) + "," + str(self.position[1]) + "\ncolor: " + self.color
        struc += "\n---\n"
        return struc

    def makeset(self, variable_name, value) -> str:
        """
        Prints the set statement for the variable.

        @param variable_name: The name of the variable.
        @param value: The value of the variable.

        @return: The set statement for the variable as a string.
        """
        self.variable_name = variable_name
        self.value = value
        return "<<set $"+self.variable_name+" = \""+self.value+"\">>"

    def dialog(self, message, reply, title="End") -> str:
        """
        Prints the dialog message and its replies.

        @param message: The dialog message.
        @param reply: The replies to the dialog message.
        @param title: The title of the dialog message. Default value is "End".

        @return: The dialog message and its replies as a string.
        """
        self.title = title
        self.structure()
        struc = self.structure()
        struc += message
        struc += "\n"
        for i in reply:
            struc += self.reply(i[0],i[1])
            struc += "\n"
        struc += "==="  + "\n"
        return struc

    def reply(self, message, next):
        """
        Returns the reply string with message and next node.

        @param message: The message to be replied.
        @param next: The next node to be linked.
        @return: The reply string with message and next node as a string.
        """
        reply = "[[" + message + "|" + next + "]]"
        return reply

