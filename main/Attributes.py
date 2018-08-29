'''



Attributes is an static class which stores the definitions of the attributes represented in the data set. It contains an array of Attribute objects, and two additional arrays storing references about the input and output attributes. The order of the attributes stored is the same order than it was found in the input data file.

Its public methods are:

getInputAttributes
Returns an array containing all the input Attributes.
getOutputAttributes
Returns an array containing all the output Attributes.
getInputAttribute
Returns a single input attribute.
getOutputAttribute
Returns a single output attribute.
getAttribute
Returns a single attribute, defined neither as input nor as output attribute.
getNumInputAttributes
Returns the number of input attributes.
getNumOutputAttributes
Returns the number of output attributes.
getNumAttributes
Returns the number attributes, including input, output and undefined ones.
'''
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

/*
 * Attribute.java
 *
 */
 '''

'''

/**
 * <p>
 * <b> Attribute </b>
 * </p>
 * It contains an attribute representation. The class attributes are enough to 
 * descrive completly an attribute: name, type, possible values, minimums and 
 * maximums, etc. It offers a collection of functions to get all this information.
 *
 * @author Albert Orriols Puig
 * @version keel0.1
 */
 '''
class Attribute:
 '''
/////////////////////////////////////////////////////////////////////////////
//////////////// CONSTANTS OF THE ATTRIBUTE CLASS ///////////////////////////
/////////////////////////////////////////////////////////////////////////////

/**
 * Label for NOMINAL values.
 */
 '''
 NOMINAL = 0;

'''
/**
 * Label for INTEGER values.
 */
 '''
INTEGER = 1;
'''
/**
 * Label for REAL VALUES
 */
'''
REAL = 2;

'''
/**
 * Label to identify INPUT attributes
 */
 
'''
INPUT = 1;

'''
/**
 * Label to identify OUTPUT attributes
 */
 
 '''
OUTPUT = 2;

'''
/**
 * Label to identify attributes that hasn't been defined neither as input or output
 */
 '''
DIR_NOT_DEF = -1;

'''
/////////////////////////////////////////////////////////////////////////////
/////////////// ATTRIBUTES OF THE ATTRIBUTE CLASS ///////////////////////////
/////////////////////////////////////////////////////////////////////////////

/**
 * It indicates if the attribute  is an input (0), an output (1) or has not been
 * defined neither as input or output (-1)
 */
 '''
__dirAttribute=0;

'''
/**
 * It keeps the type of the attribute. It can be one of the following values:
 * [Attribute.Nominal, Attribute.Integer, Attribute.Real]
 */
'''
__type=0;

'''
/**
 * It stores the name of the attribute.
 */
'''
__name="";
'''
/**
 * Vector where all the values that can take this nominal attribute are going
 * to be stored.
 */
'''
__nominalValues=[];

'''
/**
 * Minimum value that can take a real attribute.
 */
 '''
__minNum=0.0;

'''
/**
 * Maximum value that can take a real attribute.
 */
 '''
__maxNum=0.0;

'''
/**
 * Flag that indicates if it's the first time that an operation is made
 * with the current attribute.
 */
 '''
__firstTime=None;

'''
/**
 * It indicates if the bounds of the attribute has been fixed in its definition.
 */
 
  '''
__fixedBounds=None;
'''
/**
 * It counts the number of values that can take a nominal attribute
 */
'''
__countValues=0;

'''
/**
 * It informs that a nominal value not compresed in train list values has been
 * read in test
 */
 '''
__newValuesInTest=None;

'''
/**
 * It keeps the new values in test
 */
'''
__newValuesList=[];

'''
/**
 * It keeps the frequency of each class value
 */
 
 '''
__classFrequencies=[];
'''
/**
 * It stores the most used value in a nominal attribute
 */
 
  '''
__mostUsedValue=[];
'''
/**
 * It stores the integer/real mean for this attribute
 */
 
 '''
__meanValue=[];

'''
/**
 * It keeps the number of updates per class
 */

'''
__numStatUpdates=[] ;

'''
/**
 * It says if statistics has to be made
 */
'''
__makeStatistics=None;
'''
/////////////////////////////////////////////////////////////////////////////
///////////////// METHODS OF THE ATTRIBUTE CLASS ////////////////////////////
/////////////////////////////////////////////////////////////////////////////

/**
 * Attribute Constructor. It instances a new Attribute instance.
 */
 '''
def __init__() :
   type = -1;
   countValues=0;
   dirAttribute = DIR_NOT_DEF;
   makeStatistics = False;
   #end Attribute

'''
/**
 * It sets the attribute type.
     * @param _type given attribute type
 */
'''
def setType(self,_type):
    if(type!=-1):
        print("Type already fixed !!");
        exit(1);

    type=_type;
    firstTime=True;

    #If type is nominal, a new vector has to be created to store the list of
    #values that it can take.
    if(type==self.NOMINAL) :
        nominalValues=[];
        newValuesList = [];

    #In all cases, the fixedBounds flag is set to false.
    fixedBounds=False;
  #end setType

'''
/**
 * It does return the type of the attribute
 * @return an int that contains the type of the attribute.
 */
 '''
def getType():
    return type;
  #end getType

'''
/**
 * It sets the attribute name
 * @param _name is the name to be set.
 */
 '''
def setName(_name):
    name = _name;
  #end setName

'''
/**
 * It gets the attribute name
 * @return a String with the attribute name.
 */
 '''
def getName(self):
   return self.name;
  #end setName

'''

/**
 * It sets the bound of the integer or real attribute.
 * @param _min is the minimum value that the attribute can take.
 * @param _max is the maximum value that the attribute can take.
 */
 
 '''
def setBounds( _minNum, _maxNum):
    if(type != REAL and type != INTEGER) :
        return;
    fixedBounds=True;
    minNum=_minNum;
    maxNum=_maxNum;
  #end setBounds

'''
/**
 * It returns the variable fixedBounds.
 * @return a boolean that indicates if the bounds are fixed.
 */
 '''
def getFixedBounds(self):
    return self.fixedBounds;
  #end getFixedBounds


'''
/**
 * It sets the fixedBounds value
 * @param fBounds is the value that has to be fixed to fixedBounds.
 */
'''
def setFixedBounds( fBounds):
      fixedBounds = fBounds;
  #end setFixedBounds

'''
/**
 * It does enlarge the attribute bounds
 * @param value is the value read from the BD file
 */
 '''
def enlargeBounds(self, value) :
    if(type!=REAL and type!=INTEGER) :
        return;

    if(self.firstTime) :
        #If it's the first attribute update and the bounds are not fixed in its
        #specification, the min and max values are initialized.
        if(self.fixedBounds==False) :
            minNum=value;
            maxNum=value;

        firstTime=False;


    #valueMeans[instanceClass]+=value;
        self.countValues+=1;

    if(self.fixedBounds) :
        return;


    if(value<minNum)  :
        minNum=value;
    if(value>maxNum)   :
        maxNum=value;
  #end enlargeBounds

'''
/**
 * It update an integer or real value read for an attribute in the test
 * set if it doesn't match with the bounds defined in the train set. In
 * this case, it replaces the value read for the nearliest bound (the
 * minimum or the maximim bound respectively)
 * @param value is the value read from the test file.
 * @return a double with the rectified value.
 */
 '''
def rectifyValueInBounds (self, value):
    if (value < self.minNum) :
        return self.minNum;
    if (value > self.maxNum) :
        return self.maxNum;
    return value;
  #end rectifyValueInBounds

'''
/**
 * It does check if the value passed as an argument is bounded by
 * the [min, max] interval.
     * @param val value to check.
 * @return a boolean that indicates if the value is bounded.
 */
 '''
def isInBounds(self,val):
      return (val>=self.minNum and val<=self.maxNum);
  #end isInBounds

'''
/**
 * It returns if the value passed is in the list of nominal values
 * @param val is the value to be checked.
 * @return a boolean indicating if the value is a possible nominal.
 */
 '''
def isNominalValue(self,val):
      return self.nominalValues.contains(val);
  #end isNominalValue

'''

/**
 * It returns the minimum possible value in a integer or real attribute
 * @return a double with the minimum value
 */
'''
def getMinAttribute(self) :
    return self.minNum;
  #end minAttribute

'''

/**
 * It returns the maximum possible value in a integer or real attribute
 * @return a double with the maximum value
 */
 '''
def getMaxAttribute(self):
    return self.maxNum;
  #end maxAttribute

'''
/**
 * This method add a new value to the list of possible values in a nominal
 * attribute.
 * @param value is the new value to be added.
'''
def addNominalValue(self, value) :
    if(type!=self.NOMINAL):
        return;
    if (value not in self.nominalValues):
        self.nominalValues.addElement(str(value));

  #end addNominalValue


'''
/**
 * It does return the value most frequent for the class
 * @param whichClass is the class which is wanted to know the most
 *        frequent value.
 * @return a String with the most used value.
 */
 
 '''
def getMostFrequentValue( self,whichClass):
      if (self.makeStatistics==False or type != self.NOMINAL or self.mostUsedValue == None):
          return None;
      if (whichClass <0 or whichClass >= self.mostUsedValue.length):
          return None;
      return self.mostUsedValue[whichClass];
  #end getMostFrequentValue


'''
/**
 * Does return the mean value for that attribute.
 * @param whichClass is the integer value for the class
 * @return a double with the mean value.
 */
'''
def getMeanValue(self,whichClass):
      if (self.makeStatistics==False or (type != REAL and type!=INTEGER) or self.meanValue == None):
        return 0;
      if(whichClass<0 or whichClass >= self.meanValue.length) :
          return 0;

      return self.meanValue[whichClass];
  #end getMeanValue
'''
/**
 * It does initializes the variables to make statistics
 * @param classNumber is the number of classes.
 */
'''
def initStatistics(self,classNumber):
    makeStatistics = True;
    if (type == self.NOMINAL):
        classFrequencies = int [classNumber];
        numStatUpdates = int[classNumber];
        for i in range(0, classNumber):
            numStatUpdates[i] = 0;
            classFrequencies[i] = int[self.nominalValues.size()];
            for j in range(0, self.nominalValues.size()):
                classFrequencies[i][j] = 0;


    else:
        meanValue = float [classNumber];
        numStatUpdates = int[classNumber];
        for i in range(0,classNumber):
         meanValue[i] = 0;
         numStatUpdates[i] = 0;


#end initStatistics

'''
/**
 * It does finish the statistics process.
 */
 '''
def finishStatistics(self):
     if (self.makeStatistics==False) :
         return;
     if (type == self.NOMINAL):
        mostUsedValue = str[len(self.classFrequencies)];
        for i in range(0,len(mostUsedValue)):
            maxNum = self.classFrequencies[i][0];
            pos = 0;
            for j in range(1,len(self.classFrequencies[i])):
                if (self.classFrequencies[i][j] > maxNum):
                    maxNum = self.classFrequencies[i][j];
                    pos = j;


            mostUsedValue[i] = str(self.nominalValues.elementAt(pos));


     else:
          for  i in range(0, len(self.meanValue)):
              self.meanValue[i] /= float(self.numStatUpdates[i]);


  #end finishStatistics
'''

/**
 * It does increment the frequency that a value of a class has been used.
 * It's called when a new value is read.
 * @param whichClass is the class which frequency has to be increased
 * @param value is the nominal value which frequency has to be increased.
 */
 '''
def increaseClassFrequency( self,whichClass,  value):
     if (self.makeStatistics and self.classFrequencies != None and self.classFrequencies[whichClass] != None and self.classFrequencies[whichClass] != None):
         self.classFrequencies[whichClass] [convertNominalValue(value)]+=1;
         self.numStatUpdates[whichClass]+=1;

  #end increaseClassFrequency

'''
/**
 * It adds the new value to the mean values vector
 * @param whichClass is the class where to add the new value
 * @param value is the value to be added.
 */
 '''
def addInMeanValue( self,whichClass,  value):
      if (self.makeStatistics==True):
          self.numStatUpdates [whichClass]+=1;
          self.meanValue[whichClass] += value;

  #en addInMeanValue

'''
/**
 * Adds a new value for a nominal that has been read in the test file.
 * @param value is the new value to be added.
 * @return a boolean indicating if value didn't exist in the list.
 */
 '''
def addTestNominalValue( self,value):
    if (type != self.NOMINAL) :
        return False;

    if (value not in (self.nominalValues)):
        self.nominalValues.append(str(value));
        self.newValuesList.append(str(value));
        self.newValuesInTest = True;
        return True;

    return False;
  #end addTestNominalValue


'''
/**
 * It returns a vector with all new nominal values read in test.
 * @return a Vector with all new nominal values.
 */
 '''
def getNewValuesInTest(self):
      return self.newValuesList;
  #end newValuesList

'''
/**
 * It returns true if in test have appeared new values.
 * @return a boolean indicating if new values have been read in test.
 */
 '''
def areNewNominalValuesInTest(self):
      return self.newValuesInTest;
  #return areNewValuesInTest

'''
/**
 * It returns the number of different values that can take a nominal attribute.
 * @return an int with the number of different values that can take a nominal
 *         attribute.
 */
 '''
def getNumNominalValues(self) :
    if(type!=self.NOMINAL) :
         return -1;
    return self.nominalValues.size();
  #end getNumNominalValues


'''
 * Returns all the possible nominal values
 * @return a Vector with the possible values that the nominal can take
'''
def getNominalValuesList(self):
      return self.nominalValues;
  #end getNominalValuesList


'''
/**
 * It returns de ith value of that nominal attribute
 * @param pos indicate which attribute value is wanted.
 * @return a string with the value.
 */
 '''
def getNominalValue(self, pos) :
    if(type!=self.NOMINAL) :
        return None;
    return str(self.nominalValues.elementAt(pos));
  #end getNominalValue


'''
/**
 * It converts a nominal value to a integer
 * @param value is the value that is wanted to be converted
 * @return an int with the converted value.
 */
 '''
def convertNominalValue(self,value) :
    return self.nominalValues.indexOf(value);
  #end convertNominalValue

'''

/**
 * It compares two attributes.
 * @param attr is the second attribute of the comparation.
 * @return a boolean that indicates if the attributes are equal.
 */
 '''
def equals(self, attr) :
    if((self.name==attr.name)==False):
       return False;
    if(attr.type!=type) :
        return False;
    if(type==self.NOMINAL) :
            if((self.nominalValues==(attr.nominalValues))==False):
                    return False;

    return True;
   #end equals

'''
/**
 * It sets if the attribute is an input or an output attribute
 * @param _dirAtt is the direction (input/output) of the attribute.
 */
 '''
def setDirectionAttribute( _dirAtt):
      dirAttribute = _dirAtt;
  #end setInputAttribute

'''
/**
 * It returns if the attribute is an input attribute
 * @return a int that indicates if it's an input or output attribute
 */
 '''
def getDirectionAttribute(self):
      return self.dirAttribute;
  #end getDirectionAttribute
'''
/**
 * It does normalize a value.
 * @param val is the value to be normalized.
 * @return a double with the normalized value.
 */
 '''
def normalizeValue (self,val):
      if (type == self.NOMINAL)  :
          return val;

      if (type == self.INTEGER):
          return val-min;
      if (type == self.REAL) :
          return (val-self.minNum)/(self.maxNum-self.minNum);
      return val;
  #end normalizeValue

'''
/**
 * It returns a String with the attribute information in keel format
 * @return an String with the attribute information.
 */
 '''
def toString(self):
    typeNames = {"","integer","real"};
    aux = "@attribute " + self.name;

    if (type =="NOMINAL"):
          aux=toStringNOMINAL(aux);
    elif (type == "INTEGER"):
        aux=toStringINTEGER(aux);
    elif(type=="REAL")   :
        aux = toStringREAL(aux);

  #end toString

def toStringNOMINAL(self,aux):
    aux += "{";
    ending = ",";
    for i in range(0, self.nominalValues.size()):
        if (i == self.nominalValues.size() - 1):
            ending = "";
        aux += str(self.nominalValues.elementAt(i)) + ending;
        return aux;

def toStringINTEGER(self, aux):
        aux += "{";
        ending = ",";
        aux += " integer[" + str(int(self.minNum));
        aux += "," + str(int(self.maxNum)) + "]";
        return aux;

def toStringREAL(self, aux):
        aux += " real[" + str(float(self.minNum));
        aux += "," + str(float(self.maxNum)) + "]";
        return aux;
'''
/**
 * This method prints the attribute information.
 */
 '''
def printInfo(self):
      typesConv = {"Nominal","Integer","Real"};
      print("    > Name: "+self.name+".");
      print("    > Type: "+type );
      print("    > Type: "+typesConv[type]+".");
      print ("    > Input/Output: ");
      switcher={

          "INPUT":print("INPUT"),
          "OUTPUT":print("OUTPUT"),
      }
      return switcher.get(self.dirAttribute,"NOT DEFINED")


      print(" > Range: ");

      switcher2={
          "NOMINAL": printNOMINAL(self),
          "INTEGER": print("["+int(self.minNum)+","+int(self.maxNum)+"]")
      }
      return switcher2.get(self.dirAttribute,"NOT DEFINED")



      switcher3 = {
          "NOMINAL": printTypeNOMINAL(self),
          "INTEGER": print("["+int(self.minNum)+","+int(self.maxNum)+"]")
      }
      return switcher3.get(type, print("["+self.minNum+","+self.maxNum+"]"))


      if (type == self.NOMINAL):
          if (mostUsedValue != None):
              print("\n    > Most used value: ");
              for i in range(0, mostUsedValue.length):
                  print("       > class "+i+":"+mostUsedValue[i]);
                  print("  ("+classFrequencies[i][convertNominalValue(mostUsedValue[i])]+")." );
      else :
         if (meanValue != None):
          print("\n    > Mean used value: ");
          for i in range(0,len(self.meanValue)):
            print("   > class "+i+": "+self.meanValue[i]);

      printInfo(self);
  #end print

def printNOMINAL(self):
    print("{");
    for i in range(0, self.nominalValues.size()):
        print((str)(self.nominalValues.elementAt(i)) + "  ");
        print("}");

def printTypeNOMINAL(self):
    print("{");
    for i in range(0, self.nominalValues.size()):
     print(str(self.nominalValues.elementAt(i)) + "  ");

   #end of class Attribute



