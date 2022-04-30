import pandas as pd
import random

class ChoreCalendar:
    __dishchart = pd.DataFrame({'morning':[None,None,None,None,None,None,None],
                                'evening':[None,None,None,None,None,None,None]},
                                index=['monday','tuesday',
                                'wednesday','thursday',
                                'friday','saturday','sunday'])

    __chorechart = pd.DataFrame(columns=['chore', 'assignee','complete'])
    __roomates = None

    '''
    This constructor will create a house with a list of roomates and chores 
    Both lists MUST be the same length
    '''
    def __init__(self, roomates, chores):
        if(len(roomates) == len(chores)):
            self.__chorechart['chore'] = chores
            self.__chorechart['assignee'] = roomates
            self.__chorechart['complete'] = False
            self.__dishchart['morning'] = [(i,False) for i in roomates[:7]]
            self.__dishchart['evening'] = [(i,False) for i in roomates[-7:]]
            self.__roomates = roomates
        else:
            print('Error: Names and Chores lists lengths must be the same')

    '''
    This Method gets the roomate that is responsible for dishes on a given day and shift
    '''
    def GetDishAsignee(self, shift, day):
        day = day.lower
        shift = shift.lower
        days = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
        if shift != 'morning' or shift != 'afternoon':
            print('Please enter shift as either \'morning\' or \'afternoon\'')
            return -1
        if day not in days:
            print('Please enter a valid day ex. \'monday\'')
            return -1
        return self.__dishchart[day,shift][0]

    '''
    This method marks a given dish shift as complete based on the day and shift
    '''
    def CompleteDishShift(self, shift, day):
        day = day.lower()
        shift = shift.lower()
        days = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
        shifts = ['morning','afternoon']
        if shift not in shifts:
            print('Please enter shift as either \'morning\' or \'afternoon\'')
            return -1
        if day not in days:
            print('Please enter a valid day ex. \'monday\'')
            return -1
        if self.__dishchart.at[day,shift][1] != True:
            self.__dishchart.at[day,shift] = (self.__dishchart.loc[day,shift][0], True)
            return True
        else: 
            print('This was already completed')
            return -1
    
    '''
    This Method gets the person responsible for a chore at a given index
    '''
    def GetChoreAsignee(self,index):
        return self.__chorechart.iloc[index,1]

    '''
    This method completes a chore
    '''
    def CompleteChore(self,index):
        if self.__chorechart['complete'][index] != True:
            self.__chorechart['complete'][index] = True
            return True
        else: 
            print('This was already completed')
            return -1
    
    '''
    This method shuffles the chores and dish shifts around in a somewhat even way.
    This also resets the complete indicators
    '''
    def Shuffle(self):
        random.shuffle(self.__roomates)
        self.__chorechart['assignee'] = self.__roomates
        self.__chorechart['complete'] = False
        self.__dishchart['morning'] = [(i,False) for i in self.__roomates[:7]]
        self.__dishchart['evening'] = [(i,False) for i in self.__roomates[-7:]]

    '''
    This method prints the chore chart
    '''
    def printChores(self):
        print(self.__chorechart.head(len(self.__chorechart)))
    
    '''
    This method prints the dish chart
    '''
    def printDishes(self):
        print(self.__dishchart.head(len(self.__dishchart)))
    


h = ChoreCalendar(['Evan','Henry','Lexie','Ollie','Sarah','Monet','Ethan','Jonny'], ['a','b','c','d','e','f','g','h'])
h.printChores()
h.printDishes()
h.Shuffle()
print('---------')
h.printChores()
h.printDishes()
h.Shuffle()
print('---------')
h.printChores()
h.printDishes()
h.Shuffle()
print('---------')
h.printChores()
h.printDishes()
h.Shuffle()
print('---------')

