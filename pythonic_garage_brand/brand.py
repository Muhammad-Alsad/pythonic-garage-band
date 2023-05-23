class Musician:
    
    def __init__(self,name):
        """
        Initializes a Musician object with the given name.

        Args:
            name (str): The name of the musician.

        """
        self.name = name
    def __str__(self):
        """
        Returns a string representation of the Musician object.

        Returns:
            str: A formatted string containing the musician's name and the instrument they play.

        """
        return f'My name is {self.name} and I play {self.get_instrument()}'   
    def __repr__(self):
        """
        Returns a string representation of the Musician object.

        Returns:
            str: A formatted string containing the musician's role and name.

        """
        return f'{self.get_role()} instance. Name = {self.name}' 


class Band:
    instances=[]

    def __init__(self, name='Random',members =[]):
        """
        Initializes a Band object with the given name and members.

        Args:
            name (str, optional): The name of the band. Defaults to 'Random'.
            members (list, optional): A list of Musician objects representing the members of the band. Defaults to an empty list.

        """
        self.name = name
        self.members=members
        Band.instances.append(self)
    def play_solos(self):
        """
        Plays solos for each member of the band.

        Returns:
            list: A list of strings representing the solos played by each member.

        """
        list_Band=[]
        for member in self.members:
            list_Band.append(member.play_solo())
        return list_Band
    
    @classmethod 
    def to_list(cls):
        """
        Returns a list of all Band instances created.

        Returns:
            list: A list of Band instances.

        """
        return cls.instances 
        
    


class Guitarist(Musician):
     def __init__(self,name='Random'):
        """
        Initializes a Guitarist object with the given name.

        Args:
            name (str, optional): The name of the guitarist. Defaults to 'Random'.

        """
        self.name = name
     def get_instrument(self):
        """
        Returns the instrument played by the guitarist.

        Returns:
            str: The instrument played by the guitarist, which is 'guitar'.

        """
        return 'guitar' 
     def get_role(self):
        """
        Returns the role of the guitarist.

        Returns:
            str: The role of the guitarist, which is 'Guitarist'.

        """
        return  'Guitarist' 
     def play_solo(self):
        """
        Plays a solo on the guitar.

        Returns:
            str: A string representing a face-melting guitar solo.

        """
        return 'face melting guitar solo'
    
        


class Bassist(Musician):
     def __init__(self,name='Random'):
        """
        Initializes a Bassist object with the given name.

        Args:
            name (str, optional): The name of the bassist. Defaults to 'Random'.

        """
        self.name = name
     def get_instrument(self):
         """
        Returns the instrument played by the bassist.

        Returns:
            str: The instrument played by the bassist, which is 'bass'.

        """
         return 'bass'
     def get_role(self):
         """
        Returns the role of the bassist.

        Returns:
            str: The role of the bassist, which is 'Bassist'.

        """
         return  'Bassist' 
     def play_solo(self):
         """
        Plays a solo on the bass.

        Returns:
            str: A string representing the bass solo, which is 'bom bom buh bom'.

        """
         return 'bom bom buh bom'


class Drummer(Musician):
     def __init__(self,name='Random'):
        """
        Initializes a Drummer object with the given name.

        Args:
            name (str, optional): The name of the drummer. Defaults to 'Random'.

        """
        self.name = name
     def get_instrument(self):
        """
        Returns the instrument played by the drummer.

        Returns:
            str: The instrument played by the drummer, which is 'drums'.

        """
        return 'drums'
     def get_role(self):
        """
        Returns the role of the drummer.

        Returns:
            str: The role of the drummer, which is 'Drummer'.

        """
        return  'Drummer' 
     def play_solo(self):
        """
        Plays a drum solo.

        Returns:
            str: A string representing the drum solo, which is 'rattle boom crash'.

        """
        return 'rattle boom crash'


if __name__ == '__main__':
    pass
