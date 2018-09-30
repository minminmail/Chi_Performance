
#  /***********************************************************************
#
# 	This file is part of KEEL-software, the Data Mining tool for regression,
# 	classification, clustering, pattern mining and so on.
#
# 	Copyright (C) 2004-2010
#
# 	F. Herrera (herrera@decsai.ugr.es)
#     L. S谩nchez (luciano@uniovi.es)
#     J. Alcal谩-Fdez (jalcala@decsai.ugr.es)
#     S. Garc铆a (sglopez@ujaen.es)
#     A. Fern谩ndez (alberto.fernandez@ujaen.es)
#     J. Luengo (julianlm@decsai.ugr.es)
#
# 	This program is free software: you can redistribute it and/or modify
# 	it under the terms of the GNU General Public License as published by
# 	the Free Software Foundation, either version 3 of the License, or
# 	(at your option) any later version.
#
# 	This program is distributed in the hope that it will be useful,
# 	but WITHOUT ANY WARRANTY; without even the implied warranty of
# 	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# 	GNU General Public License for more details.
#
# 	You should have received a copy of the GNU General Public License
# 	along with this program.  If not, see http://www.gnu.org/licenses/
#
# **********************************************************************/



#  * <p>It reads the configuration file (data-set files and parameters)</p>
#  *
#  * @author Written by Alberto Fern谩ndez (University of Granada) 15/10/2007
#  * @Modified by Rui Min 28/09/2018
#  * @version 1.0
#  * @since Python 3

import logging
import re
from pathlib import Path
class ParseParameters :

     __algorithmName=""

     __inputFiles=[]
     __inputTraFiles=[]
     __inputTstFiles=[]

     __outputTraFiles=[]
     __outputTstFiles=[]
     __outputFiles=[]

     __parameters={}

    # * Default constructor

     def __init__(self):
        inputFiles = [];
        outputFiles = [];
        parameters =  {};


         # * It obtains all the necesary information from the configuration file.<br/>
         # * First of all it reads the name of the input data-sets, training, validation and test.<br/>
         # * Then it reads the name of the output files, where the training (validation) and test outputs will be stored<br/>
         # * Finally it read the parameters of the algorithm, such as the random seed.<br/>
         # *
         # * @param fileName Name of the configuration file
         # *

     def parseConfigurationFile(self,fileName):

            logging.info("fileName in parseParameters = " + fileName);
            logging.info("before open file" );
            print(fileName);
            file = open(fileName,"r");
            #file is an string containing the whole file
            fileString = file.read();
            line =  fileString.splitlines();
            lineNumber=0;
            for lineNumber in range (0,len(line)):
                print("In line " + str(lineNumber) + ", the str is:begin ***   " + line[lineNumber] + "   ***end")
                if lineNumber==0:
                    self.readName(line[lineNumber])
                elif lineNumber==1:
                    self.readInputFiles(line[lineNumber])#We read all the input files
                elif lineNumber == 2:
                    self.readOutputFiles(line[lineNumber])#We read all the output files
                else: # read parameters and save into map
                    self.readAllParameters(line[lineNumber])  # We read all the possible parameters
            for key ,value in self.__parameters.items():
                print("key :"+ key + "value :" + value)


     # """
     #     * It reads the name of the algorithm from the configuration file
     #     * @param line StringTokenizer It is the line containing the algorithm name.
     # """
     def readName(self,line):
            print("In side the readName method the parameter pass is :" + str(line))
            name = line.rpartition("=")[2];
            name=name.strip()
            print("In side the readName method after split =, we get:" + str(name))
            self.__algorithmName = name
     # """
     #     * We read the input data-set files and all the possible input files
     #     * @param line StringTokenizer It is the line containing the input files.
     # """
     def readInputFiles( self,line):
            print("Inside the readInputFiles mehtod, we get parameter is:" + str(line))
            firstParts=line.split()
            for lineNumber in range(0,len(firstParts)):
                wholeName=firstParts[lineNumber]
                print("Inside readInputFiles, line "+ str(lineNumber) + ",wholeName: "+ str(wholeName))
                fileNameWithStr=wholeName.rpartition('/')[2]
                print("Inside readInputFiles, line " + str(fileNameWithStr) + ",fileNameWithStr: " + str(fileNameWithStr))
                fileName=fileNameWithStr[:-1]
                print("Inside readInputFiles, line " + str(lineNumber) + ",fielName: " + str(fileName))
                if (fileName[-3:]=='dat'):
                    self.__inputFiles.append(fileName)
                    print("Inside readInputFiles, line " + str(lineNumber) + ",added fileName: " + str(fileName))
                    fileNameWithoutSuffix = fileName.rpartition('.')[0]
                    typeInputFile =fileNameWithoutSuffix[-3:]
                    #check  input file's  type :trainning or test
                    if typeInputFile=='tra':
                        self.__inputTraFiles.append(fileName)
                    elif typeInputFile=='tst':
                        self.__inputTstFiles.append(fileName)

            print("The Input files number is :" + str(len(self.__inputFiles)))
            for inputFile in self.__inputFiles:
                print("input file is :" + inputFile)
            print("The Input training files number is :" + str(len(self.__inputTraFiles)))
            for inputTraFile in self.__inputTraFiles:
                print("input tra file is :" + inputTraFile)
            print("The Input test files number is :" + str(len(self.__inputTstFiles)))
            for inputTstFile in self.__inputTstFiles:
                print("input tst file is :" + inputTstFile)
     # """
     #     * We read the output files for training and test and all the possible remaining output files
     #     * @param line StringTokenizer It is the line containing the output files.
     # """
     def readOutputFiles(self,line):
             print("Inside the readInputFiles mehtod, we get parameter is:" + str(line))
             firstParts = line.split();
             for lineNumber in range(0, len(firstParts)):
                 wholeName = firstParts[lineNumber]
                 print("Inside readOutputFiles, line " + str(lineNumber) + ",wholeName: " + str(wholeName))
                 fileNameWithStr = wholeName.rpartition('/')[2]
                 print("Inside readOutputFiles, line " + str(fileNameWithStr) + ",fileNameWithStr: " + str(fileNameWithStr))
                 fileName = fileNameWithStr[:-1]
                 print("Inside readOutputFiles, line " + str(lineNumber) + ",fielName: " + str(fileName))
                 if(fileName[-3:] == 'txt'):
                     self.__outputFiles.append(fileName)
                     print("Inside readOutputFiles, line " + str(lineNumber) + ",added txt fileName: " + str(fileName))
                 elif(fileName[-3:] == 'tra'):
                     self.__outputTraFiles.append(fileName)
                     print("Inside readOutputFiles, line " + str(lineNumber) + ",added tra fileName: " + str(fileName))
                 elif(fileName[-3:] == 'tst'):
                     self.__outputTstFiles.append(fileName)
                     print("Inside readOutputFiles, line " + str(lineNumber) + ",added tst fileName: " + str(fileName))
             print("The Output txt files number is :" + str(len(self.__inputFiles)))
             print("The Output tra files number is :" + str(len(self.__inputFiles)))
             print("The Output tst files number is :" + str(len(self.__inputFiles)))

     # """
     #     * We read all the possible parameters of the algorithm
     #     * @param line StringTokenizer It contains all the parameters.
     # """
     def readAllParameters(self,line):

             key = line.rpartition("=")[0]
             value = line.rpartition("=")[2]
             # remove the space in key and value of parameters and save into dictionary
             self.__parameters[key.strip()] = value.strip()
            #If the algorithm is non-deterministic the first parameter is the Random SEED

     # """
     # * It returns the algorithm name
     # *
     # * @return the algorithm name
     # """

     def getAlgorithmName(self):
        return self.algorithmName;

     # """
     # * It returns the name of the parameters
     # *
     # * @return the name of the parameters
     # """
     def getParameters(self):
        param = self.___parameters
        return param;


     # """
     # * It returns the name of the parameter specified
     # *
     # * @param key the index of the parameter
     # * @return the value of the parameter specified
     # """
     def getParameter(self,key):
        return str(self.__parameters.keys().index(key));

     # """
     # * It returns the input files
     # *
     # * @return the input files
     # """

     def getInputFiles(self):
        return str (self.__inputFiles)

     # """
     # * It returns the input training files
     # *
     # * @return the input training files
     # """

     def getInputTrainingFiles(self):
        return self.__inputTraFiles

     # """
     #  * It returns the input test files
     #  *
     #  * @return the input test files
     #  """

     def getInputTestFiles(self):
         return self.__inputTstFiles

     # """
     # * It returns the input file of the specified index
     # *
     # * @param pos index of the file
     # * @return the input file of the specified index
     # """
     def  getInputFile(self, pos):
        return self.inputFiles[pos]

     # """
     # * It returns the output files
     # *
     # * @return the output files
     # """
     def getOutputFiles(self):
        return self.__outputFiles


     # """
     # * It returns the output file of the specified index
     # *
     # * @param pos index of the file
     # * @return the output file of the specified index
     # """
     def getOutputFile(self, pos):
        return self.outputFiles[pos]


