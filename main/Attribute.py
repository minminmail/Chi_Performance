'''
*********************************************************************

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

*********************************************************************

Attribute.java

* <b> Attribute </b>

* It contains an attribute representation. The class attributes are enough to
* descrive completly an attribute: name, type, possible values, minimums and
* maximums, etc. It offers a collection of functions to get all this information.
*
* @author Albert Orriols Puig
* @version keel0.1
'''
class Attribute:

 '''
/////////////////////////////////////////////////////////////////////////////
//////////////// CONSTANTS OF THE ATTRIBUTE CLASS ///////////////////////////
/////////////////////////////////////////////////////////////////////////////


 * Label for NOMINAL values.
'''

 NOMINAL = 0;

 # * Label for INTEGER values.

 INTEGER = 1;
 # * Label for REAL VALUES


 REAL = 2;


 #  Label to identify INPUT attributes


 INPUT = 1;

 # Label to identify OUTPUT attributes


 OUTPUT = 2;


 #  Label to identify attributes that hasn't been defined neither as input or output


 DIR_NOT_DEF = -1;

 # '''
 # /////////////////////////////////////////////////////////////////////////////
 # /////////////// ATTRIBUTES OF THE ATTRIBUTE CLASS ///////////////////////////
 # /////////////////////////////////////////////////////////////////////////////
 #
 #
 #  * It indicates if the attribute  is an input (0), an output (1) or has not been
 #  * defined neither as input or output (-1)
 # '''

 _dirAttribute=0;

 # '''
 #  * It keeps the type of the attribute. It can be one of the following values:
 #  * [Attribute.Nominal, Attribute.Integer, Attribute.Real]
 # '''

 _type=0;

 #It stores the name of the attribute.


 _name='';
 # '''
 #  * Vector where all the values that can take this nominal attribute are going
 #  * to be stored.
 #  '''

 _nominalValues=[];
 # '''
 #  * Minimum value that can take a real attribute.
 #  '''

 _min=0.0;
 # '''
 #  * Maximum value that can take a real attribute.
 #  '''

 _max=0.0;
 # '''
 #  * Flag that indicates if it's the first time that an operation is made
 #  * with the current attribute.
 #  '''

 _firstTime=None;
 # '''
 #  * It indicates if the bounds of the attribute has been fixed in its definition.
 #  '''

 _fixedBounds=None;
 # '''
 #  * It counts the number of values that can take a nominal attribute
 #  '''

 _countValues=0;

 # '''
 #  * It informs that a nominal value not compresed in train list values has been
 #  * read in test
 #  '''

 _newValuesInTest=None;
 # '''
 #  * It keeps the new values in test
 #  '''

 _newValuesList=[];
 # '''
 #  It keeps the frequency of each class value
 # '''

 #
 # '''
 # # Creates a list containing 5 lists, each of 8 items, all set to 0
 # w, h = 8, 5;
 # Matrix = [[0 for x in range(w)] for y in range(h)]
 # '''
 w=0;
 h=0;
 _classFrequencies = [[0 for x in range(w)] for y in range(h)]

 # '''
 #  * It stores the most used value in a nominal attribute
 #  '''


 # '''
 # strs = ["" for x in range(size)]
 # '''
 _mostUsedValue=["" for x in range(0)];
 # '''
 #  * It stores the integer/real mean for this attribute
 #  '''

 _meanValue=[];
 # '''
 #  * It keeps the number of updates per class
 #  '''

 _numStatUpdates=[];

 # '''
 #  * It says if statistics has to be made
 #  '''

 _makeStatistics=None;
 # '''
 # /////////////////////////////////////////////////////////////////////////////
 # ///////////////// METHODS OF THE ATTRIBUTE CLASS ////////////////////////////
 # /////////////////////////////////////////////////////////////////////////////
 #
 #
 #  * Attribute Constructor. It instances a new Attribute instance.
 #  '''

 def _init_(self):
     _type=-1;
     countValues=0;
     _dirAttribute = DIR_NOT_DEF;
     makeStatistics = False;

 #//end Attribute

 # '''
 #  * It sets the attribute type.
 #      * @param _type given attribute type
 #  '''

 def setType(type) :
  if(type!=-1) :
   print("Type already fixed !!")
   exit(1);

  type=_type;
  _firstTime=True;
 # '''
 #     //If type is nominal, a new vector has to be created to store the list of
 #     //values that it can take.
 # '''
 if(type==NOMINAL) :
  nominalValues=[];
  newValuesList = [];


  #//In all cases, the fixedBounds flag is set to false.
  fixedBounds=False;
  #end setType

 # '''
 #  * It does return the type of the attribute
 #  * @return an int that contains the type of the attribute.
 #  '''

 def getType() :
  return _type;
 #//end getType

 # '''
 #  * It sets the attribute name
 #  * @param _name is the name to be set.
 #  '''

 def setName(name) :
  name = _name;
 #end setName

 #
 # '''
 #  * It gets the attribute name
 #  * @return a String with the attribute name.
 #  '''

 def getName() :
  return name;
 #end setName


 # '''
 #  * It sets the bound of the integer or real attribute.
 #  * @param _min is the minimum value that the attribute can take.
 #  * @param _max is the maximum value that the attribute can take.
 #  '''

 def setBounds(_min,_max) :
  if(_type != REAL and _type != INTEGER):
   return;
  fixedBounds=True;
  min=_min;
  max=_max;
 #end setBounds

 # '''
 #  * It returns the variable fixedBounds.
 #  * @return a boolean that indicates if the bounds are fixed.
 #  '''

 def getFixedBounds():
  return fixedBounds;
 #end getFixedBounds

 #
 # '''
 #  * It sets the fixedBounds value
 #  * @param fBounds is the value that has to be fixed to fixedBounds.
 #  '''

 def setFixedBounds( fBounds):
  fixedBounds = fBounds;
 #end setFixedBounds

 # '''
 #  * It does enlarge the attribute bounds
 #  * @param value is the value read from the BD file
 #  '''

 def enlargeBounds( value) :
  if(_type!=REAL and _type!=INTEGER) :
   return;

  if(_firstTime==True) :
   #//If it's the first attribute update and the bounds are not fixed in its
   #//specification, the min and max values are initialized.
   if(_fixedBounds==False) :
    min=value;
    max=value;

   _firstTime=False;


  #//valueMeans[instanceClass]+=value;
  countValues+=1;

  if(_fixedBounds):
   return;
  if(value<_min):
   _min=value;
  if(value>_max) :
   _max=value;
 #end enlargeBounds

 # '''
 #  * It update an integer or real value read for an attribute in the test
 #  * set if it doesn't match with the bounds defined in the train set. In
 #  * this case, it replaces the value read for the nearliest bound (the
 #  * minimum or the maximim bound respectively)
 #  * @param value is the value read from the test file.
 #  * @return a double with the rectified value.
 #  '''

 def rectifyValueInBounds ( value):
  if (value < min) :
   return min;
  if (value > max):
   return max;
  return value;
 #end rectifyValueInBounds

 # '''
 #  * It does check if the value passed as an argument is bounded by
 #  * the [min, max] interval.
 #      * @param val value to check.
 #  * @return a boolean that indicates if the value is bounded.
 #  '''

 def isInBounds( val):
  return (val>=_min and val<=_max);
 #end isInBounds

 # '''
 #  * It returns if the value passed is in the list of nominal values
 #  * @param val is the value to be checked.
 #  * @return a boolean indicating if the value is a possible nominal.
 #  '''

 def isNominalValue( val):
  return nominalValues.contains(val);
 #end isNominalValue

 #
 # '''
 #  * It returns the minimum possible value in a integer or real attribute
 #  * @return a double with the minimum value
 #  '''

 def getMinAttribute() :
  return min;
 #end minAttribute

 #
 # '''
 #  * It returns the maximum possible value in a integer or real attribute
 #  * @return a double with the maximum value
 #  '''
 def getMaxAttribute() :
  return max;
 #end maxAttribute


 # '''
 #  * This method add a new value to the list of possible values in a nominal
 #  * attribute.
 #  * @param value is the new value to be added.
 #  '''
 def addNominalValue( value) :
  if(_type!=NOMINAL) :
   return;
  if (nominalValues.contains(value)==False):
   nominalValues.addElement(str(value));

 #end addNominalValue


 #
 # '''
 #  * It does return the value most frequent for the class
 #  * @param whichClass is the class which is wanted to know the most
 #  *        frequent value.
 #  * @return a String with the most used value.
 #  '''
 def getMostFrequentValue( whichClass):
  if (_makeStatistics==False or _type != NOMINAL or _mostUsedValue == None):
   return None;
  if (whichClass <0 or whichClass >= _mostUsedValue.length) :
   return None;
  return _mostUsedValue[whichClass];
 #end getMostFrequentValue


 #
 # '''
 #  * Does return the mean value for that attribute.
 #  * @param whichClass is the integer value for the class
 #  * @return a double with the mean value.
 #  '''
 def getMeanValue( whichClass):
  if (_makeStatistics==False or (_type != REAL and _type!=INTEGER) or _meanValue == None):
   return 0;
  if(whichClass<0 or whichClass >= _meanValue.length):
   return 0;
  return _meanValue[whichClass];
 #end getMeanValue

 # '''
 #  * It does initializes the variables to make statistics
 #  * @param classNumber is the number of classes.
 #  '''
 def initStatistics( classNumber):
  makeStatistics = True;
  if (_type == NOMINAL):
   #w, h = 8, 5;
   #Matrix = [[0 for x in range(w)] for y in range(h)]
   w,h=classNumber,0;
   classFrequencies = [[0 for x in range(w)] for y in range(h)] ;
   numStatUpdates = int[classNumber];
   for i in range(0, classNumber):
    numStatUpdates[i] = 0;
    classFrequencies[i] = int[nominalValues.size()];
    for j in range(0,nominalValues.size()):
     classFrequencies[i][j] = 0;


  else:
   meanValue = float [classNumber];
   numStatUpdates = int[classNumber];
   for i in range (0,classNumber):
    meanValue[i] = 0;
    numStatUpdates[i] = 0;


 #end initStatistics


 # '''
 #  * It does finish the statistics process.
 #  '''
 def finishStatistics():
  if (_makeStatistics==False):
   return;
  if (_type == NOMINAL):
   mostUsedValue = str [_classFrequencies.length];
   for i in range(0,mostUsedValue.length):
    max = _classFrequencies[i][0];
    pos = 0;
    for j in range(1,_classFrequencies[i].length):
     if (_classFrequencies[i][j] > max):
      max = _classFrequencies[i][j];
      pos = j;

    mostUsedValue[i] = str(nominalValues.elementAt(pos));

  else:
   for i in range(0,_meanValue.length):
    _meanValue[i] /= float(_numStatUpdates[i]);


 #end finishStatistics


 # '''
 #  * It does increment the frequency that a value of a class has been used.
 #  * It's called when a new value is read.
 #  * @param whichClass is the class which frequency has to be increased
 #  * @param value is the nominal value which frequency has to be increased.
 #  '''
 def increaseClassFrequency( whichClass,  value):
  if (_makeStatistics and _classFrequencies != None and _classFrequencies[whichClass] != None and _classFrequencies[whichClass] != None):
   _classFrequencies[whichClass] [convertNominalValue(value)]+=1;
   _numStatUpdates[whichClass]+=1;

 #end increaseClassFrequency


 # '''
 #  * It adds the new value to the mean values vector
 #  * @param whichClass is the class where to add the new value
 #  * @param value is the value to be added.
 #  '''
 def addInMeanValue( whichClass,  value):
  if (_makeStatistics):
   _numStatUpdates [whichClass]+=1;
   _meanValue[whichClass] += value;

 #en addInMeanValue

 #
 # '''
 #  * Adds a new value for a nominal that has been read in the test file.
 #  * @param value is the new value to be added.
 #  * @return a boolean indicating if value didn't exist in the list.
 #  '''
 def addTestNominalValue( value):
  if (_type != NOMINAL) :
   return False;

  if (_nominalValues.contains(value)==False):
   nominalValues.addElement(str(value));
   newValuesList.addElement(str(value));
   newValuesInTest = True;
   return True;

  return False;
   #end addTestNominalValue



 # '''
 #  * It returns a vector with all new nominal values read in test.
 #  * @return a Vector with all new nominal values.
 #  '''
 def  getNewValuesInTest():
  return newValuesList;
 #end newValuesList

 #
 # '''
 #  * It returns true if in test have appeared new values.
 #  * @return a boolean indicating if new values have been read in test.
 #  '''
 def areNewNominalValuesInTest():
  return newValuesInTest;
 #return areNewValuesInTest


 # '''
 #  * It returns the number of different values that can take a nominal attribute.
 #  * @return an int with the number of different values that can take a nominal
 #  *         attribute.
 #  '''
 def getNumNominalValues() :
  if(_type!=NOMINAL):
   return -1;
  return nominalValues.size();
 #end getNumNominalValues

 #
 # '''
 #  * Returns all the possible nominal values
 #  * @return a Vector with the possible values that the nominal can take
 #  '''
 def getNominalValuesList():
  return nominalValues;
 #end getNominalValuesList


 #
 # '''
 #  * It returns de ith value of that nominal attribute
 #  * @param pos indicate which attribute value is wanted.
 #  * @return a string with the value.
 #  '''
 def getNominalValue( pos) :
  if(_type!=NOMINAL):
   return None;
  return str(nominalValues.elementAt(pos));
 #end getNominalValue



 # '''
 #  * It converts a nominal value to a integer
 #  * @param value is the value that is wanted to be converted
 #  * @return an int with the converted value.
 #  '''
 def convertNominalValue( value) :
  return nominalValues.indexOf(value);
 #end convertNominalValue


 #
 # '''
 #  * It compares two attributes.
 #  * @param attr is the second attribute of the comparation.
 #  * @return a boolean that indicates if the attributes are equal.
 #  '''
 def equals( attr) :
  if(_name.equals(attr.name)==False):
   return False;
  if(attr.type!=_type) :
   return False;
  if(_type==NOMINAL) :
   if(nominalValues.equals(attr.nominalValues)==False):
    return False;

    return True;
   #end equals
 #
 #
 # '''
 #  * It sets if the attribute is an input or an output attribute
 #  * @param _dirAtt is the direction (input/output) of the attribute.
 #  '''
 def setDirectionAttribute( _dirAtt):
  _dirAttribute = _dirAtt;
 #end setInputAttribute

 #
 # '''
 #  * It returns if the attribute is an input attribute
 #  * @return a int that indicates if it's an input or output attribute
 #  '''
 def getDirectionAttribute():
  return _dirAttribute;
 #end getDirectionAttribute


 # '''
 #  * It does normalize a value.
 #  * @param val is the value to be normalized.
 #  * @return a double with the normalized value.
 #  '''
 def normalizeValue (val):
  if (_type == NOMINAL):  return val;
  if (_type == INTEGER) : return val-min;
  if (_type == REAL) :    return (val-min)/(max-min);
  return val;
 #end normalizeValue


 # '''
 #  * It returns a String with the attribute information in keel format
 #  * @return an String with the attribute information.
 #  '''
 def toString():
  typeNames = {"","integer","real"};
  aux = "@attribute " + name;
  if(_type==NOMINAL):

    aux += "{";
    ending = ",";
    for  i in range (0,_nominalValues.size()):
     if (i == nominalValues.size() - 1): ending = "";
     aux += str(nominalValues.elementAt(i)) + ending;

    aux +='}';
    #//System.out.println("Caso NOMINAL, aux->"+aux);
    #//System.out.println("name->" + name);
  elif(_type==INTEGER):

      aux += " integer["+(int(_min)).toString();
      aux += ","+ (int(_max)).toString()+"]";

  elif(_type== REAL):
      aux += " real["+float( _min).toString();
      aux += ","+ float(_max).toString()+"]";


      return aux;
 #end toString
 #
 # '''
 #  * This method prints the attribute information.
 #  '''
 def print():
  typesConv = {"Nominal","Integer","Real"};
  print(" Name: "+_name+".");
  print(" Type: "+_type );
  print(" Type: "+typesConv[type]+".");
  print(" Input/Output: ");
  if (_dirAttribute==INPUT):

    print("INPUT");

  elif(_dirAttribute== OUTPUT):
     print("OUTPUT");
  else:

     print("NOT DEFINED");

  print(" Range: ");
  if (_type==NOMINAL):

     print("{");
     for i in range(0, nominalValues.size()):
      print (str(nominalValues.elementAt(i))+"  ");

      print("}");
  elif(_type==INTEGER):

     print("["+int(_min)+","+int(_max)+"]");

  else:
     print("["+__min+","+__max+"]");

  if (_type == NOMINAL):
    if (_mostUsedValue != None):
     print("\n    > Most used value: ");
     for  i in range(0, _mostUsedValue.length):
      print("       > class "+i+":"+_mostUsedValue[i]);
      print("  ("+_classFrequencies[i][convertNominalValue(_mostUsedValue[i])]+")." );

  else :
    if (_meanValue != None):
     print("\n    > Mean used value: ");
     for i in range (0,_meanValue):
      print("       > class "+i+": "+_meanValue[i]);

  print();
  #end print
   #end of class Attribute



