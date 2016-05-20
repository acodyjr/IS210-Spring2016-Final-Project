#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Bar|$plit - Paying only your share of the tab."""

import decimal as dec


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
        >>>*****Welcome to Bar|$plit*****
        >>>How many people are paying the tab? 3
        >>>On a scale of 1-5, how would you rate your service? 4
        >>>Based on your rating, a 15% tip is proper. Continue? (y/n) y
        >>>Will you be splitting the bill evenly? (y/n) y
        >>>What is the total amount due? $37.59

        ***********************************

        Total with tip is: $  43.23

        Total amount due per person: $  14.41

        Start over? (y/n)

        >>>How many people are paying the tab? 1
        >>>On a scale of 1-5, how would you rate your service? 5
        >>>Based on your rating, a 20% tip is proper. Continue? (y/n) y
        >>>What is the total amount due? $25.43

        ***********************************

        Total with tip is: $  30.52

        Total amount due per person: $  30.52

        Start over? (y/n)
    """
    totalwithtip = dec.Decimal(totalbill *
                               (1 + dec.Decimal(servicerating) / 100))
    totaleach = dec.Decimal(totalwithtip)/groupsize
    print '\n', LINEDIV, ('\n\nTotal with tip is: $ '), round(totalwithtip, 2)
    print ('\nTotal amount due per person: $ '), round(totaleach, 2)
    restart()


def costcalculator(groupsize, servicerating):
    """A function to get individual costs and output cost responsibilities.

    Args:
        groupsize (int): Number of people paying bill.
        servicerating (dec): Percentage tip based on service.

    Returns:
        dict: Dictionary key/vals printed showing amounts due per person.

    Examples:
        >>>*****Welcome to Bar|$plit*****
        >>>How many people are paying the tab? 2
        >>>On a scale of 1-5, how would you rate your service? 5
        >>>Based on your rating, a 20% tip is proper. Continue? (y/n) y
        >>>Will you be splitting the bill evenly? (y/n) n

        >>>Who is dining member 1? Foo
        >>>How many items did Foo have? 1
        >>>What is the cost of item 1 for Foo? $8.59

        >>>Who is dining member 2? Bar
        >>>How many items did Bar have? 2
        >>>What is the cost of item 1 for Bar? $9.95
        >>>What is the cost of item 2 for Bar? $12.35

        ***********************************

        Foo owes $ 10.31

        Bar owes $ 26.76

        Start over? (y/n)
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
        print '\n', names, 'owes $', round(amount, 2)
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

startup()
