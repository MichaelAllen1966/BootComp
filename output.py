# -*- coding: utf-8 -*-
"""
Created on Sun Jul 30 11:51:07 2017

@author: tm3y13
"""

import csv

def write_results_matrix(matrix, n_scenarios):
    """
    Converts scenario comparison results to matrix format.
    Includes "-" for comparisons that are N/A
    """
     
    headers = scenario_headers(n_scenarios)
    row_headers = scenario_row_headers(n_scenarios)
     
    output_list = []
    
    headers.insert(0, '')
    output_list.append(headers) 
    for scenario, row in zip(row_headers, matrix):
        output_list.append([scenario, *row])

           
    with open('results_matrix.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(output_list)
        
    
def results_to_matrix(results):
    """
    Converts scenario comparison results to matrix format.
    Includes "-" for comparisons that are N/A
    """

    matrix = [['-' for i in range(len(results))] for j in results]
   
        
    #loop through results and add to matrix
    for i in range(len(results)):
        k = 0
        for j in range(len(results[i])):
            matrix[i][i+j] = results[i][k]
            k+= 1
    
    return matrix


def print_results_matrix(matrix, n_scenarios):
    """
    Screen print of comparison results in matrix form.  Not nice
    for large comparisons. 
    """
    
    headers = scenario_headers(n_scenarios)
    row_headers = scenario_row_headers(n_scenarios)
    
    row_format ="{:>10}" * (len(headers)+1)
    print(row_format.format("", *headers))
    for scenario, row in zip(row_headers, matrix):
        print(row_format.format(scenario, *row))
        
      
        
                
            
def scenario_headers(n_scenarios):
    """
    Returns a list representing headers in a results matrix
    """
    return ["S{0}".format(i) for i in range(2, n_scenarios+1)]
    


def scenario_row_headers(n_scenarios):
    """
    Returns a list representing headers in a results matrix
    """
    return ["S{0}".format(i) for i in range(1, n_scenarios)]



    

    