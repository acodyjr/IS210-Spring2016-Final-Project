#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Bar|$plit - Paying only your share of the tab."""

import decimal as dec
import os


WELCOME = '*****Welcome to Bar|$plit*****\n'
TOTAL_PROMPT = 'What is the total amount due? $'
GROUP_PROMPT = 'How many people are paying the tab? '
SPLIT_PROMPT = 'Will you be splitting the bill evenly? (y/n) '
TIP_PROMPT = 'On a scale of 1-5, how would you rate your service? '
TIP_CONFIRM = 'Based on your rating, a {0}% tip is proper. Continue? (y/n) '
TIP_QUERY = 'What percentage tip would you like to use? '
SUGGESTED_TIP = {int(1): dec.Decimal(0.00),
                 int(2): dec.Decimal(5.00),
                 int(3): dec.Decimal(10.00),
                 int(4): dec.Decimal(15.00),
                 int(5): dec.Decimal(20.00)}
LINEDIV = '*' * 35
FNAME_RAW = '\nWho is dining member {0}? '
ITEMS_RAW = 'How many items did {0} have? '
BILL_ITEMS = 'What is the cost of item {0} for {1}? $'

def startup():
    """Function to acquire initial data input to process.

    Args:
        none

    Returns:
        none
    """
    print WELCOME
    groupsize = int(raw_input(GROUP_PROMPT))
    servicerating = int(raw_input(TIP_PROMPT))
    servicerating = SUGGESTED_TIP[servicerating]
    tipconfirm = raw_input(TIP_CONFIRM.format(servicerating))
    if tipconfirm != 'y':
        servicerating = dec.Decimal(raw_input(TIP_QUERY))
    if groupsize > 1:
        splitbill = raw_input(SPLIT_PROMPT)
        if splitbill is 'y':
            totalbill = dec.Decimal(raw_input(TOTAL_PROMPT))
            billsplitter(totalbill, groupsize, servicerating)
        elif splitbill is 'n':
            costcalculator(groupsize, servicerating)
    elif groupsize == 1:
        totalbill = dec.Decimal(raw_input(TOTAL_PROMPT))
        billsplitter(totalbill, groupsize, servicerating)
            
def billsplitter(totalbill, groupsize, servicerating):
    """Function to perform an even split on a tab.

    Args:
        totalbill (dec): Total amount due on tab.
        groupsize (int): Number of people splitting the bill.
        servicerating (dec): Percentage tip based on service.

    Returns:
        dec: Amount each person contributes to cover full amount.

    Examples:
        >>>

        >>>
    """
    totalwithtip = dec.Decimal(totalbill *
                               (1 + dec.Decimal(servicerating) / 100))
    totaleach = dec.Decimal(totalwithtip)/groupsize
    print '\n', LINEDIV, ('\n\nThe total with tip is: $ '), dec.Decimal(totalwithtip)
    print ('\nTotal amount due per person: $ '), dec.Decimal(totaleach)
    restart()


def costcalculator(groupsize, servicerating):
    """A function to get individual costs and output cost responsibilities.

    Args:
        groupsize (int): Number of people paying bill.
        servicerating (dec): Percentage tip based on service.

    Returns:
        dict: Dictionary key/vals printed showing amounts due per person.
        
    Examples:
        >>>

        >>>
    """
    counter, billitems, billcounter, billtotal, nametotal = 0, 0, 0, 0, 0
    fnames = {}
    while counter < groupsize:
        fname = raw_input(FNAME_RAW.format(counter+1))
        billitems = int(raw_input(ITEMS_RAW.format(fname)))
        while billcounter < billitems:
            billtotal = dec.Decimal(
                         raw_input(BILL_ITEMS.format(billcounter + 1, fname)))
            nametotal += billtotal
            billcounter += 1
        nametotal += nametotal * (servicerating/100)
        fnames[fname] = nametotal
        billitems, billcounter, billtotal, nametotal = 0, 0, 0, 0
        counter += 1
    print '\n', LINEDIV
    for names, amount in fnames.iteritems():
        print '\n', names, 'owes $', amount
    restart()

def restart():
    """A function to restart the calculator if desired after output.

    Args:
        none

    Returns:
        none:
    """
    if raw_input('\nStart over? (y/n) ') is 'y':
        startup()
    else:
        print 'Thank you for using Bar|$plit!'
    
startup()  ## Initiate program.
