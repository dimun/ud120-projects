#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    cleaned_data = []

    ### your code goes here
    data = [(ages[i],net_worths[i],pow(net_worths[i]-predictions[i],2)) for i in range(len(ages))]
    data = sorted(data,key=lambda x:x[2])
    cleaned_data = data[:int(len(predictions)*0.9)]
    return cleaned_data

