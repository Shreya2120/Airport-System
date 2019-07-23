#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 28 18:56:38 2018

@author: driftking9987
"""
import string
import random
from collections import defaultdict

#t = input("Enter a number: ")
#print("shreya"+t)
#File to contain data

path = '/Users/driftking9987/Documents/Python Scripts/data_airline.txt'
path_flight = '/Users/driftking9987/Documents/Python Scripts/flight_detail.txt'
path_passenger = '/Users/driftking9987/Documents/Python Scripts/passenger_detail.txt'
flight_startOptions = []
flight_endOptions = []
listOfFlight = []

def userInput():
    chosen_option = input("Please enter 1 for Security Personnel, 2 for Flight Staff, 3 for Passengers: ")
#    print(PNRGenerator())
    writePNRData()
    return chosen_option

def readPNRInfo():
    PNRData = open(path,'r')
    return PNRData

def writePNRData():
    new_pnr = open(path,'a')
    a = PNRGenerator() #the PNR which has been generated 
    print(a) #to see the PNR which has been generated (should be commented out later)
    new_pnr.write('\n'+a)
    
def PNRGenerator(size=6, chars=string.ascii_uppercase + string.digits):
    new_pnr = ''.join(random.choice(chars) for _ in range(size))
    old_pnr = readPNRInfo().readlines()
    print(old_pnr)
    #Below function is to check if the generated pnr is a repeat one
    for x in old_pnr:
        if new_pnr not in x:
            return new_pnr
        else:
            PNRGenerator()
            
def createPassengerList():
    temp_p = open(path_passenger, 'a')
    name = input("Enter name : ")
    fStart= input("Enter boarding point : ")
    fStop= input("Enter destination point : ")
    a,b,c = createFlightDetail_single(fStart,fStop)
    temp_p.write('\n'+name + "|" + PNRGenerator()+"|"+a+"->"+b+"|"+c)
    print(a+b+c)

def printSortedDetail(flightNumber):
    new_list = []
    existing_passenger = open(path_passenger, 'r')
    one_passenger = existing_passenger.readlines()
    for x in one_passenger:
#        print(x)
        t = x.split(' ')
#        print(t)
        if t[3].replace(' ','').replace('\n','') == flightNumber:
            new_list.append(x)
            
    print(new_list)
    print(sorted(new_list, key = lambda x: x.split()[0]))

    
def loadFlightDetails():
    existing_flights = open(path_flight, 'r')
    one_flight = existing_flights.readlines()
    for x in one_flight:
#        print (x)
        t = x.split('|')
        flight_start = t[1]
        flight_end = t[3]
        flight_startOptions.append(flight_start)
        flight_endOptions.append(flight_end)
        flighDet = flight_start+flight_end
        listOfFlight.append(flighDet.replace(' ',''))
        print(flighDet.replace(' ',''))
    createFlightDetail('F','C')
    print(sorted(list(set(listOfFlight))))
    return sorted(list(set(flight_startOptions))),sorted(list(set(flight_endOptions))) #returns the starting points and ending points
def createFlightDetail_single(start,end):
    existing_flights = open(path_flight, 'r')
    one_flight = existing_flights.readlines()
    for x in one_flight:
        t = x.split('|')
        if t[3].replace(' ','') == end:
            if (t[1].replace(' ','')) == start:
                print ("Flight for you is : "+t[1] +" ->" +t[3]+" and flight number is :"+t[4])
                return t[1],t[3],t[4]
                
def createFlightDetail_multiple(start,end):
    existing_flights = open(path_flight, 'r')
    one_flight = existing_flights.readlines()
    for x in one_flight:
        t = x.split('|')
        if t[3].replace(' ','') == end:
            if (t[1].replace(' ','')) == start:
                print ("Flight for you is : "+t[1] +" ->" +t[3]+" and flight number is :"+t[4])
            
printSortedDetail('1')
#createPassengerList()
#userInput()

#loadFlightDetails()
