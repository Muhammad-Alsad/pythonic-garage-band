class Musician:
    def __init__(self,name):
        self.name = name
    def __str__(self):
        return f'My name is {self.name} and I play {self.get_instrument()}'   
    def __repr__(self):
        return f'{self.get_role()} instance. Name = {self.name}' 


class Band:
    instances=[]

    def __init__(self, name='Random',members =[]):
        self.name = name
        self.members=members
        Band.instances.append(self)
    def play_solos(self):
        list_Band=[]
        for member in self.members:
            list_Band.append(member.play_solo())
        return list_Band
    
    @classmethod 
    def to_list(cls):
        return cls.instances 
        
    


class Guitarist(Musician):
     def __init__(self,name='Random'):
         self.name = name
     def get_instrument(self):
         return 'guitar' 
     def get_role(self):
         return  'Guitarist' 
     def play_solo(self):
         return 'face melting guitar solo'
    
        


class Bassist(Musician):
     def __init__(self,name='Random'):
         self.name = name
     def get_instrument(self):
         return 'bass'
     def get_role(self):
         return  'Bassist' 
     def play_solo(self):
         return 'bom bom buh bom'


class Drummer(Musician):
     def __init__(self,name='Random'):
         self.name = name
     def get_instrument(self):
         return 'drums'
     def get_role(self):
         return  'Drummer' 
     def play_solo(self):
         return 'rattle boom crash'


if __name__ == '__main__':
    pass
