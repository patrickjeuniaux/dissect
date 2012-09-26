'''
Created on Jun 3, 2012

@author: thenghia.pham
'''
from weighting import Weighting
    
class PlogWeighting(Weighting):
    '''
    Positive Log Weighting
    '''
    _name = "plog"
    # TODO: implement Weighting
    #       remove constructor 

    def apply_weighting(self, matrix_, column_marginal = None):
        '''
        Performs positive log weighting.
        
        Args:
            matrix_ (Matrix): Input matrix
            column_marginal (array): column marginals of the core matrix if the matrix is a peripheral matrix
    
        Returns:
            Matrix: the matrix after applying plog
            
        '''
        matrix_ = matrix_.copy()
        matrix_.plog()
        return matrix_
        
    def get_name(self):
        return self.__name
    def __str__(self, *args, **kwargs):
        return self.__name
        