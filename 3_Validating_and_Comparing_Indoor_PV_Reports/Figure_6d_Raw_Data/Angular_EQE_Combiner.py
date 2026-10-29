# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 08:58:59 2026

@author: austi
"""

# from numpy import loadtxt
from os import getcwd, listdir, path
from pandas import DataFrame, read_csv

Current_Working_Directory = getcwd()


Files = listdir( Current_Working_Directory )
Files = [ File for File in Files if ".txt" in File ]

# Extract EQEs and Add to Dictionary

Output = {}

for j, File in enumerate( Files ):

    # Determine Angle: All files have form 'Name_<Angle>Deg.txt'

    Label = File.split( '_' )
    Label = Label[ 1 ]    
    Label = Label.replace( '.txt', '' )    

    # Write Path
    
    Path = path.join( 
        
        Current_Working_Directory,
        
        File )
    
    Data = read_csv( Path )
    
    # Add Wavelengths for First File (Assumes wavelength same in all files)

    if j == 0:
        
        Output[ "Wavelength/nm" ] = list( Data[ 'Wavelength [nm]' ] )
        
    # Add EQEs
    
    for Column in list( Data.columns ):
        
        if "EQE" in Column:

            Output[ Label ] = list( Data[ Column ] )


Device_Type = Files[ 0 ].split( '_' )[ 0 ]

DataFrame( Output ).to_excel( 
    
    Device_Type + '_Angle_Dep_EQE.xlsx',
    
    index = False )
