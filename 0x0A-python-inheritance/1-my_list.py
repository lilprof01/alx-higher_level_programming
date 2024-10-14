#!/usr/bin/python3
'''
this module contains a class MyList
'''


class MyList(list):
    '''
       class MyList which inherits from List
    '''

    pass

    def print_sorted(self):
        '''
          function prints list but sorted in ascending order
        '''
        print(sorted(self))
