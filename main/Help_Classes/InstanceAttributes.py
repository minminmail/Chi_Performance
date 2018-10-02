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
 * InstanceAttributes.java
 *
 * Created on 20 de junio de 2004, 10:06
 */
 '''
'''

/**
 * <p>
 * <b> InstanceAttributes </b>
 * </p>
 *
 * This class contains the information of all the attributes in the dataset.
 * It stores the same information in Attributes, but it is not defined as static.
 *
 * @author Albert Orriols Puig
 * @see Attribute
 * @version keel0.1
 */
'''

from main.Help_Classes import Attribute, Attributes


class InstanceAttributes :

 '''
/////////////////////////////////////////////////////////////////////////////
/////////////// ATTRIBUTES OF THE ATTRIBUTES CLASS //////////////////////////
/////////////////////////////////////////////////////////////////////////////

/**
 * It contains all the attributes definitions.
 */

 '''
__attributes=[];


# It contains a reference to all input attributes.

__inputAttr=[];


 # It contains a reference to all output attributes.

__outputAttr=[];


# It contains a reference to all undefined attributes.

__undefinedAttr=[];


 #A flag indicating if the vector contains any nominal attribute.

hasNominal=None;


 # A flag indicating if the vector contains any integer attribute.

__hasInteger=None;


 # A flag indicating if the vector contains any real attribute.

__hasReal=None;


 # A vector containing the types of each attribute.

  #private static int []type;


 # String that keeps the relation name

__relationName="";

'''

/////////////////////////////////////////////////////////////////////////////
///////////////// METHODS OF THE ATTRIBUTES CLASS ///////////////////////////
/////////////////////////////////////////////////////////////////////////////


/**
 * InstanceAttributes
 *
 * Class constructor. It reserve memory to allocate the attributes
 */
 '''
def __init__():
      attributes = [];
      inputAttr  = [];
      outputAttr = [];
      undefinedAttr = [];
      hasNominal=False;
      hasInteger=False;
      hasReal=False;
      relationName= "";
  #end clearAll

def __init__(self,ia):
    self.attributes = ia.attributes;
    self.inputAttr = ia.inputAttr;
    self.outputAttr = ia.outputAttr;
    self.undefinedAttr = ia.undefinedAttr;
    self.hasInteger = ia.hasInteger;
    self.hasNominal = ia.hasNominal;
    self.hasReal = ia.hasReal;
    self.relationName = str(ia.relationName);

'''
/**
 * copyStaticAttributes
 *
 * It copies the attributes definition statically stored in Attributes class
 */
'''
def copyStaticAttributes (self) :
  i=0;
  attributes = [];
  inputAttr  = [];
  outputAttr = [];
  undefinedAttr = [];

  for i in range (0, Attributes.attributes.size()) :
    self.attributes.add (Attributes.attributes.elementAt(i));
  for  i in range (0, Attributes.inputAttr.size()):
    self.inputAttr.add (Attributes.inputAttr.elementAt(i));

  for i in range(0, Attributes.outputAttr.size()):
       outputAttr.add (Attributes.outputAttr.elementAt(i));
  for i in range (0, Attributes.undefinedAttr.size()):
      undefinedAttr.add (Attributes.undefinedAttr.elementAt(i));


  hasNominal	= Attributes.hasNominal;
  hasInteger	= Attributes.hasInteger;
  hasReal		= Attributes.hasReal;
  relationName = Attributes.relationName;

#end copyStaticAttributes
'''
/**
 * This method adds an attribute definition.
 * @param attr is the new attribute to be added.
 */
'''
def addAttribute(self, attr) :
    attributes.addElement(attr);
    if(attr.getDirectionAttribute()== Attribute.INPUT):
        self.inputAttr.add(attr);
    if(attr.getDirectionAttribute()== Attribute.OUTPUT):
        self.outputAttr.add(attr);
    if(attr.getDirectionAttribute()== Attribute.DIR_NOT_DEF):
        self.undefinedAttr.add(attr);
    if(attr.getType()== Attribute.NOMINAL):
        hasNominal=True;
    if(attr.getType()== Attribute.INTEGER):
        hasInteger=True;
    if(attr.getType()== Attribute.REAL):
        hasReal=True;
  #end addAttribute



 #The function returns if there is any nominal attribute

def hasNominalAttributes() :
    return hasNominal;
  #end hasNominalAttributes

'''
/**
 * The function returns if there is any integer attribute.
 */
'''
def hasIntegerAttributes() :
    return hasInteger;
#end hasIntegerAttributes



 # The function returns if there is any real attribute.

def hasRealAttributes() :
    return hasReal;
  #end hasRealAttributes

'''
/**
 * It returns the attribute requested.
 * @param _name is the name of the attribute.
 */
'''
def getAttribute( self,_name) :
    i=0;
    for i in range (0,self.__attributes.size()):
        if ( Attribute(self.__attributes.elementAt(i)).getName().equals(_name)):
         break;

    if (i == self.__attributes.size()):
        return None;
    return Attribute(attributes.elementAt(i));
  #end getAttribute



 #It does return an array with all attributes

def  getAttributes(self):
    if (self.__attributes.size() == 0) :
        return None;
    attr = Attribute[self.__attributes.size()];
    for i in range (0, attr.length):
      attr[i] = Attribute(self.__attributes.elementAt(i))
  #end getAttribute



'''
 * It returns the input attribute being int the position passed as an argument.
 * @param pos is the position of the attribute wanted.
'''
def getInputAttribute( self,pos) :
    if (pos<0 or pos >= self.inputAttr.size()) :
        return None;
    return Attribute(self.inputAttr.elementAt(pos));
  #end getInputAttribute



 # It does return all the input attributes

def getInputAttributes(self):
    if (self.inputAttr.size() == 0):
        return None;
    attr = Attribute[self.inputAttr.size()];
    for i in range (0,len(attr)):
       attr[i] = Attribute(self.inputAttr.elementAt(i));
       return attr;
#end getInputAttribute
'''

/**
 * It does return an String with the @inputs in keel format.
 * @return an string with the @inputs definition  .
 */
'''
def getInputHeader(self):
    aux = "@inputs ";
    ending = ",";
    for i in range (0, self.inputAttr.size()):
      if (i == self.inputAttr.size() - 1):
          ending = "";
          aux += (Attribute(self.inputAttr.elementAt(i))).getName() + ending;

    return aux;
  #end getInputHeader
'''
/**
 * It does return a String with all the input attributes definition in keel
 * format. The order of the attributes is the order of lecture.
 * @return a String with the input attributes definition.
 */
 '''
def getInputAttributesHeader():
    aux = "";
    for i in range (0, _inputAttr.size()):
        #Writting the name and type of the attribute
        aux += Attribute(_inputAttr.elementAt(i)).toString() + "\n";

    return aux;
  #end getInputAttributesHeader

'''
/**
 * It does return all the output attributes.
 */
 '''
def getOutputAttributes():
    if (_outputAttr.size() == 0) :
        return None;
    attr = Attribute[_outputAttr.size()];
    for i in range (0,attr.length):
        attr[i] = Attribute(_outputAttr.elementAt(i));

    return attr;
#end outputAttributes

'''
/**
 * It returns the output attribute being int the position passed as an argument.
 * @param pos is the position of the attribute wanted.
 */
 '''
def getOutputAttribute(self,pos) :
    if (pos<0 or pos >= self._outputAttr.size()) :
        return None;
    return Attribute(self._outputAttr.elementAt(pos));
  #end getOutputAttribute
'''

/**
 * It does return an String with the @outputs in keel format.
 * @return an string with the @outputs definition  .
 */
 '''
def getOutputHeader(self):
    aux = "@outputs ";
    ending = ",";
    for i in range (0, outputAttr.size()):
      if (i == self.outputAttr.size() - 1) :

          ending = "";
          aux += (Attribute(self.outputAttr.elementAt(i)).getName()) + ending;

    return aux;
  #end getOutputHeader

'''
/**
 * It does return a String with all the output attributes definition in keel
 * format. The order of the attributes is the order of lecture.
 * @return a String with the output attributes definition.
 */
 '''
def getOutputAttributesHeader(self):
    aux = "";
    for i in range (0, self._outputAttr.size()):
        #Writting the name and type of the attribute
        aux += str(Attribute(self._outputAttr.elementAt(i))) + "\n";

    return aux;
#end getOutputAttributesHeader

'''

/**
 * It returns the undefined attribute being int the position passed as an argument.
 * @param pos is the position of the attribute wanted.
 */
 '''
def getUndefinedAttribute(self,pos) :
   if (pos<0 or pos >= self.undefinedAttr.size()) :
       return None;
   return Attribute(self.undefinedAttr.elementAt(pos));
  #end getUndefinedAttribute

'''
/**
 * It does return all the undefined attributes
 */
 '''
def getUndefinedAttributes(self):
    if (self.undefinedAttr.size() == 0): return None;
    attr = Attribute[self.undefinedAttr.size()];
    for i in range(0,attr.length):
        attr[i] = Attribute(self.undefinedAttr.elementAt(i));

    return attr;
    #end getUndefinedAttributes

'''
/**
 * It does return a String with all the undefined attributes definition
 * in keel format. The order of the attributes is the order of lecture.
 * @return a String with the input attributes definition.
 */
 '''
def getUndefinedAttributesHeader(self):
    aux = "";
    for i in range (0, self.undefinedAttr.size()):
        #Writting the name and type of the attribute
        aux += Attribute(self.undefinedAttr.elementAt(i)).toString() + "\n";

    return aux;
  #end getUndefinedAttributesHeader

'''
/**
 * It returns the attribute being int the position passed as an argument.
 * @param pos is the position of the attribute wanted.
 */
'''
def getAttribute(pos) :
    return Attribute(attributes.elementAt(pos));
#end getAttribute

'''

/**
 * It return the total number of attributes in the API
 * @return an int with the number of attributes
 */
 '''
def getNumAttributes() :
    return attributes.size();
#end getNumAttributes


'''
/**
 * It return the  number of input attributes in the API
 * @return an int with the number of attributes
 */
 '''
def getInputNumAttributes(self) :
    return self.inputAttr.size();
#end getInputNumAttributes
'''
/**
 * It return the number of output attributes in the API
 * @return an int with the number of attributes
 */
 '''
def getOutputNumAttributes(self) :
    return self.outputAttr.size();
#end getOutputNumAttributes
'''
/**
 * It return the number of undefined attributes in the API
 * @return an int with the number of attributes
 */
 '''
def getUndefinedNumAttributes(self):
    return self.undefinedAttr.size();
#end getUndefinedNumAttributes

'''
/**
 * It returns all the attribute names in the dataset except these ones
 * that are already in the vector v.
 * @param v is a vector with the exceptions
 * @return a Vector with the rest of attribute names.
 */
 '''
def getAttributesExcept(v):
    restAt =[];
    for  i in range(0, attributes.size()):
        attName = Attribute(attributes.get(i)).getName();
        if (v.contains(attName)==False):  restAt.add(attName);

    return restAt;
    #end getAttributesExcept

'''
/**
 * It organizes the whole number of attributes to input, output, and
 * "no-direction" attributes.
 * @param inAttNames  is a vector with the names of all input  attributes.
 * @param outAttNames is a vector with the names of all output attributes.
 */
'''
def setOutputInputAttributes(self,inAttNames,outAttNames):
    i=0;
    attName='';
    att= Attribute();

    for i in range (0, attributes.size()):
        att = Attribute(attributes.get(i));
        attName = att.getName();
        if (inAttNames.contains(attName)):
            att.setDirectionAttribute(Attribute.INPUT);
            self._inputAttr.add(attributes.get(i));
        elif (outAttNames.contains(attName)):
            att.setDirectionAttribute(Attribute.OUTPUT);
            self.outputAttr.add(attributes.get(i));
        else:
            self.undefinedAttr.add(attributes.get(i));



    #Finally, making some statistics
    hasNominal = False;
    hasInteger = False;
    hasReal    = False;

    for  index in range (0,2):
        if(index == 0):
            iterations=self._inputAttr.size() ;
        else:
            iterations=self._outputAttr.size();

        for i in range (0,iterations):

            if(index == 0):
               att = Attribute(self._inputAttr.elementAt(i)) ;
            else:
               att= Attribute(self._outputAttr.elementAt(i));
            if ( att.getType()== Attribute.NOMINAL):

                hasNominal = True;

            elif(att.getType() == Attribute.INTEGER):
                 hasInteger = True;

            elif(att.getType() == Attribute.REAL):
                    hasReal = True;

 #end setOutputInputAttributes
'''
/**
 * This method checks if all the input names vector corresponds with
 * all the attributes in input vector. If not, it returns a false. It
 * is used in a test to check that the definition of input attributes
 * is the same as the definition made in train.
 * @param outputNames is a vector with all input attribute names.
 */
'''
def areAllDefinedAsInputs(self,inputNames):
    if (inputNames.size() != self._inputAttr.size()):
        return False;

    for i in range(0, self._inputAttr.size()):
        if ( inputNames.contains((Attribute(self.inputAttr.elementAt(i))).getName())==False) :
            return False;

    return True;
  #end areAllDefinedAsInputs
'''
/**
 * This method checks if all the output names vector corresponds with
 * all the attributes in output vector. If not, it returns a false. It
 * is used in a test to check that the definition of output attributes
 * is the same as the definition made in train.
 * @param outputNames is a vector with all output attribute names.
 */
 '''
def areAllDefinedAsOutputs( self,outputNames):
    if (outputNames.size() != self._outputAttr.size()):
        return False;

    for i in range(0, self._outputAttr.size()):
        if ( outputNames.contains((Attribute(self._outputAttr.elementAt(i))).getName())):
            return False;

    return True;
  #end areAllDefinedAsOutputs
'''

/**
 * It sets the relation name.
 * @param rel is the name to be set to the relationName
 */
 '''
def setRelationName( rel):
    relationName = rel;
#end setRelationName
'''
/**
 * It gets the relation name.
 * @return an String with the realtion name.
 */
 
 '''
def getRelationName(self):
    return self._relationName;
#end relationName
'''
/**
 * It does remove an attribute. Removing an attribute only implies, in terms
 * of Attribute static class, to take it out from the input/output attributes
 * list, but it will never be removed from the attributes general list. So
 * it will be placed as a NON-SPECIFIED attribute, as it wasn't declared in
 * neither @inputs and @outputs definition.
 * @param inputAtt is a boolean that indicates if the attribute to be removed
 * is an input attribute
 * @param whichAtt is an integer that indicates the position of the attribute
 * to be removed.
 * @return a boolean that will be false if the attribute hasn't been found.
 */
 '''
def removeAttribute( self,inputAtt,  whichAtt):
    atToDel=None;
    if ( inputAtt and (whichAtt >=  self._inputAttr.size() or whichAtt < 0)) :
        return False;
    if (self.__inputAtt and (whichAtt >= self.__outputAttr.size() or whichAtt < 0)):
        return False;

    if (inputAtt):
        #inputAttribute
        atToDel =  Attribute(self.__inputAttr.elementAt(whichAtt));
        atToDel.setDirectionAttribute(Attribute.DIR_NOT_DEF);
        self.__inputAttr.removeElementAt(whichAtt);

    else: #output attribute
        atToDel = Attribute(self.__outputAttr.elementAt(whichAtt));
        atToDel.setDirectionAttribute(Attribute.DIR_NOT_DEF);
        self.__outputAttr.removeElementAt(whichAtt);

    #We get the position where it has to go in the undefined attributes vector.
    self.__undefPosition = self.searchUndefPosition(atToDel);
    self.__undefinedAttr.insertElementAt(atToDel, self.__undefPosition);

    hasNominal = False;
    hasInteger = False;
    hasReal    = False;
    for index in (0,2):
        if(index == 0):
            iterations = self.__inputAttr.size() ;
        else:
            iterations=self.__outputAttr.size();
        for  i in range(0,self.__iterations):
            if(index == 0):
                att = Attribute(inputAttr.elementAt(i)) ;
        else:
            att = Attribute(self.__outputAttr.elementAt(i));
        attTypeHere=att.getType();
        if ( attTypeHere== Attribute.NOMINAL):

            hasNominal = True;

        elif(attTypeHere == Attribute.INTEGER):
            hasInteger = True;

        elif(attTypeHere == Attribute.REAL):
            hasReal = True;


    return True;
#end removeAttribute
'''

/**
 * It does search the relative position of the input/output attribute
 * 'whichAtt' in the list of indefined attributes.
 * @param attToDel is an Attribute reference to the attribute that has to
 * be deleted.
 * @return an int with the relative position.
 */
 '''
def searchUndefPosition( self,attToDel):
    undefCount=0,
    count = 0;

    att_aux = Attribute(self.__attributes.elementAt(count));
    while (attToDel != att_aux):
        if (att_aux.getDirectionAttribute() == Attribute.DIR_NOT_DEF):
            undefCount+=1;

        count+=1;
        att_aux = Attribute(self.__attributes.elementAt(count));

    return undefCount;
#end searchUndefPosition
'''
/**
 * It does initializes the statistics to make the statistics. It only
 * works for classifier Datasets (only one output).
 */
'''
def initStatistics(self):
    if (self.__outputAttr.size() != 1):
        return;

    classNumber = Attribute(self.__outputAttr.elementAt(0)).getNumNominalValues();
    #If the output attribute has not been defined as a nominal or it has not
    #any value in the nominal list, the initalization is aborted.
    if (classNumber<=0) :
        return;

    for i in range(0,inputAttr.size()):
        Attribute(self.__inputAttr.elementAt(i)).initStatistics(classNumber);

  #end initStatistics

'''
/**
 * It does finish the statistics
 */
 '''
def finishStatistics(self):
    if (self.__outputAttr.size() != 1):
        return;

    for i in range(0, self.__inputAttr.size()):
        Attribute(self.__inputAttr.elementAt(i)).finishStatistics();

  #//end finishStatistics
'''
/**
 * It does print the attributes information
 */
 '''
def printInsAttr(self):
    println("@relation = "+self.__relationName);
    println("Number of attributes: "+self.__attributes.size());

    for i in range(0, self.__attributes.size()):
        att = Attribute(self.__attributes.elementAt(i));
        if (att.getDirectionAttribute() == Attribute.INPUT):
            println("  > INPUT ATTRIBUTE:     ");
        elif (att.getDirectionAttribute() == Attribute.OUTPUT):
            println("  > OUTPUT ATTRIBUTE:    ");
        else:
            println("  > UNDEFINED ATTRIBUTE: ");

        att.print();

#end print
#end of Attributes class



