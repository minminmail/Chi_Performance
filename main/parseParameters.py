'''
 /***********************************************************************

	This file is part of KEEL-software, the Data Mining tool for regression,
	classification, clustering, pattern mining and so on.

	Copyright (C) 2004-2010

	F. Herrera (herrera@decsai.ugr.es)
    L. S谩nchez (luciano@uniovi.es)
    J. Alcal谩-Fdez (jalcala@decsai.ugr.es)
    S. Garc铆a (sglopez@ujaen.es)
    A. Fern谩ndez (alberto.fernandez@ujaen.es)
    J. Luengo (julianlm@decsai.ugr.es)

	This program is free software: you can redistribute it and/or modify
	it under the terms of the GNU General Public License as published by
	the Free Software Foundation, either version 3 of the License, or
	(at your option) any later version.

	This program is distributed in the hope that it will be useful,
	but WITHOUT ANY WARRANTY; without even the implied warranty of
	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
	GNU General Public License for more details.

	You should have received a copy of the GNU General Public License
	along with this program.  If not, see http://www.gnu.org/licenses/

**********************************************************************/
'''

'''
 * <p>It reads the configuration file (data-set files and parameters)</p>
 *
 * @author Written by Alberto Fern谩ndez (University of Granada) 15/10/2007
 * @version 1.0
 * @since JDK1.5
'''
import logging
class parseParameters :

 __algorithmName="";
 __trainingFile="";
 __validationFile="";
 __testFile="";
 __inputFiles=[];
 __outputTrFile="";
 __outputTstFile="";
 __outputFiles=[];
 __parameters=[];

'''
     * Default constructor
'''
def parseParameters() :
    inputFiles = [];
    outputFiles = [];
    parameters =  [];

'''
     * It obtains all the necesary information from the configuration file.<br/>
     * First of all it reads the name of the input data-sets, training, validation and test.<br/>
     * Then it reads the name of the output files, where the training (validation) and test outputs will be stored<br/>
     * Finally it read the parameters of the algorithm, such as the random seed.<br/>
     *
     * @param fileName Name of the configuration file
     *
'''
def parseConfigurationFile(self, fileName):

        logging.info("fileName in parseParameters = " + fileName);
        logging.info("before open file" );
        file = open(fileName,"r"); #file is an string containing the whole file
        fileString = file.read();
        line =  fileString.split("\n\r");
        readName(line); #We read the algorithm name
        readInputFiles(line); #We read all the input files
        readOutputFiles(line); #We read all the output files
        readAllParameters(line); #We read all the possible parameters

'''
     * It reads the name of the algorithm from the configuration file
     * @param line StringTokenizer It is the line containing the algorithm name.
'''
def readName( line):

        data=line.nextToken().split(" = \" ");
        algorithmName=str(data.nextToken());

        while(data.hasMoreTokens()):
            algorithmName += " "+data.nextToken(); #We read the algorithm name

'''
     * We read the input data-set files and all the possible input files
     * @param line StringTokenizer It is the line containing the input files.
'''
def readInputFiles( self,line):
        new_line = line.nextToken(); #We read the input data line
        data = new_line.split(" = \" ");
        data.nextToken(); #inputFile
        trainingFile = data.nextToken();
        validationFile = data.nextToken();
        testFile = data.nextToken();
        while(data.hasMoreTokens()):
            self.inputFiles.add(data.nextToken());

'''
     * We read the output files for training and test and all the possible remaining output files
     * @param line StringTokenizer It is the line containing the output files.
'''
def readOutputFiles(self,line):
        new_line = line.nextToken(); #We read the input data line
        data = new_line.split(" = \" ");
        data.nextToken();#inputFile
        outputTrFile = data.nextToken();
        outputTstFile = data.nextToken();
        while(data.hasMoreTokens()):
            self.add(data.nextToken());

'''
     * We read all the possible parameters of the algorithm
     * @param line StringTokenizer It contains all the parameters.
'''
def readAllParameters(self,line):
        new_line="";
        cadena="";
        data="";
        while (line.hasMoreTokens()) :# While there is more parameters...
            new_line = line.nextToken();
            data = new_line.split(" = ");
            cadena = "";
            while (data.hasMoreTokens()):
                cadena = data.nextToken(); #parameter name

            self.parameters.add(cadena); #parameter value

        #If the algorithm is non-deterministic the first parameter is the Random SEED

'''
 * It returns the training input file
 *
 * @return the training input file
'''
def getTrainingInputFile(self):
    return self.trainingFile;


'''
 * It returns the test input file
 *
 * @return the test input file
'''
def  getTestInputFile(self):
    return self.testFile;

'''
 * It returns the validation input file
 *
 * @return the validation input file
'''
def getValidationInputFile(self):
    return self.validationFile;


'''
 * It returns the training output file
 *
 * @return the training output file
'''
def getTrainingOutputFile(self):
    return self.outputTrFile;


'''
 * It returns the test output file
 *
 * @return the test output file
'''
def getTestOutputFile(self):
    return self.outputTstFile;

'''
 * It returns the algorithm name
 *
 * @return the algorithm name
'''

def getAlgorithmName(self):
    return self.algorithmName;

'''
 * It returns the name of the parameters
 *
 * @return the name of the parameters
'''
def getParameters(self):
    param = self.parameters.toArray();
    return param;


'''
 * It returns the name of the parameter specified
 *
 * @param pos the index of the parameter
 * @return the name of the parameter specified
'''
def getParameter(self,pos):
    return str(self.parameters.get(pos));

'''
 * It returns the input files
 *
 * @return the input files
'''

def getInputFiles(self):
    return str (self.inputFiles.toArray());


'''
 * It returns the input file of the specified index
 *
 * @param pos index of the file
 * @return the input file of the specified index
'''
def  getInputFile(self, pos):
    return str(self.inputFiles.get(pos));

'''
 * It returns the output files
 *
 * @return the output files
'''
def getOutputFiles(self):
    return str(self.outputFiles.toArray());


'''
 * It returns the output file of the specified index
 *
 * @param pos index of the file
 * @return the output file of the specified index
'''
def getOutputFile(self, pos):
    return str(self.outputFiles.get(pos));


