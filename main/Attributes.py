
# /***********************************************************************
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

# /*
#  * Attributes.java
#  *
#  * Created on 20 de junio de 2004, 10:06
#  */
from Attribute import Attribute

# /**
 # * <p>
 # * <b> Attributes </b>
 # * </p>
 # *
 # * This class is a static class that, basically, contains a Vector of defined
 # * attributes in the train file. Although it keeps all the attributes, it divides
 # * them in two groups, the input attributes and the output attributes. It could
 # * be that, depending on the @inputs and @outputs defined in the train file, some
 # * of the attributes are not valid, so, their values are not loaded to the API
 # * dataset. Even in this case, the non-careful attributes information is mantained
 # * in this static class.
 # *
 # * @author Albert Orriols Puig
 # * @see Attribute
 # * @version keel0.1
 # */

class Attributes:
#
# /////////////////////////////////////////////////////////////////////////////
# /////////////// ATTRIBUTES OF THE ATTRIBUTES CLASS //////////////////////////
# /////////////////////////////////////////////////////////////////////////////
#
# /**
#  * It contains all the attributes definitions.
#  */
  attributes = []

# /**
#  * It contains a reference to all input attributes.
#  */
  inputAttr  = []

# /**
#  * It contains a reference to all output attributes.
#  */
  outputAttr = []

# /**
#  * It contains a reference to all undefined attributes.
#  */
  undefinedAttr = []

# /**
#  * A flag indicating if the vector contains any nominal attribute.
#  */
  hasNominal = False
#
# /**
#  * A flag indicating if the vector contains any integer attribute.
#  */
  hasInteger = False

# /**
#  * A flag indicating if the vector contains any real attribute.
#  */
  hasReal = False

# /**
#  * It indicates if there are missing values
#  */
  hasMissing = False

# /**
#  * A vector containing the types of each attribute.
#  */
  #private static int []type;

# /**
#  * String that keeps the relation name
#  */
  relationName = ""

# /////////////////////////////////////////////////////////////////////////////
# ///////////////// METHODS OF THE ATTRIBUTES CLASS ///////////////////////////
# /////////////////////////////////////////////////////////////////////////////

# /**
#  * clearAll
#  * This method clears all the static members of the class.
#  * It is used when another dataset is wanted to be loaded
#  */
  def clearAll(self):
      self.attributes = []
      self.inputAttr  = []
      self.outputAttr = []
      self.undefinedAttr = []
      self.hasNominal = False
      self.hasInteger = False
      self.hasReal = False
      self.hasMissing = False
      self.relationName = None
   #end clearAll

# /**
#  * This method adds an attribute definition.
#  * @param attr is the new attribute to be added.
#  */
  def addAttribute(self, attr):
    self.attributes.addElement(attr)
    if(attr.getType()==Attribute.NOMINAL):
        hasNominal= True
    if(attr.getType()==Attribute.INTEGER) :
        hasInteger= True
    if(attr.getType()==Attribute.REAL):
        hasReal = True
   #end addAttribute


# /**
#  * The function returns if there is any nominal attribute
#      * @return True if there is any nominal attribute, False otherwise.
#  */
  def  hasNominalAttributes(self):
    return self.hasNominal
   #end hasNominalAttributes


# /**
#  * The function returns if there is any integer attribute.
#      * @return True if there is any integer attribute, False otherwise.
#  */
  def hasIntegerAttributes(self):
    return self.hasInteger;
   #end hasIntegerAttributes

# /**
#  * The function returns if there is any real attribute.
#      * @returnTrue if there is any real attribute, False otherwise.
#  */
  def  hasRealAttributes(self):
    return self.hasReal
   #end hasRealAttributes

# /**
#  * The function returns if there is any missing value
#      * @return if there is any missing value, False otherwise.
#  */
  def hasMissingValues(self):
    return self.hasMissing

    #end hasMissingValues

# /**
#  * It returns the attribute requested.
#  * @param _name is the name of the attribute.
#      * @return the attribute requested.
#  */
  def getAttribute(self,_name):
    for i in range (0,len(self.attributes)):
        attribute = self.attributes.elementAt(i)
        if  (self.attribute).getName()==_name:
            break;

    if (i == self.attributes.size()) :
        return None;
    return attribute
   #end getAttribute


# /**
#  * It does return an array with all attributes
#      * @return an array with all attributes
#  */
  def  getAttributes(self):
    if (len(self.attributes) == 0):
        return None
    attr = self.attributes
    for i in range(0, len(attr)):
      attr[i] = self.attributes.elementAt(i)

    return attr;
   #end getAttribute

# /**
#  * It returns the input attribute being int the position passed as an argument.
#  * @param pos is the position of the attribute wanted.
#      * @return the input attribute being int the position passed as an argument.
#  */
  def getInputAttribute(self, pos):
    if pos<0 or pos >= len(self.inputAttr):
        return None;
    return self.inputAttr.elementAt(pos);
   #end getInputAttribute

# /**
#  * It does return all the input attributes
#      * @return all the input attributes
#  */
  def getInputAttributes(self):
    if (self.inputAttr.size() == 0) :
        return None;
    attr = self.inputAttr;
    for i in range (0, attr.length):
      attr[i] = self.inputAttr.elementAt(i);

    return attr;
   #end getInputAttribute

# /**
#  * It does return an String with the @inputs in keel format.
#  * @return an string with the @inputs definition  .
#  */
  def getInputHeader(self):
    aux = "@inputs ";
    ending = ",";
    for i in range(0, self.inputAttr.size()):
      if (i == self.inputAttr.size() - 1):
          ending = "";
      attribute=self.inputAttr.elementAt(i)
      aux += (attribute).getName() + ending;
    return aux;
  #end getInputHeader

# /**
#  * It does return a String with all the input attributes definition in keel
#  * format. The order of the attributes is the order of lecture.
#  * @return a String with the input attributes definition.
#  */
  def getInputAttributesHeader(self):
    aux = "";
    for i in range (0, self.inputAttr.size()):
        #Writting the name and type of the attribute
        aux += (self.inputAttr.elementAt(i)).toString()+"\n";

    return aux;
  #end getInputAttributesHeader

#
# /**
#  * It does return all the output attributes.
#      * @return all the output attributes.
#  */
  def getOutputAttributes(self):
    if (self.outputAttr.size() == 0):
        return None;
    attr = Attribute[self.outputAttr.size()]
    for i in range (0,attr.length):
      attr[i] = self.outputAttr.elementAt(i)

    return attr;
  #end outputAttributes
# /*
#  * It returns the output attribute being int the position passed as an argument.
#  * @param pos is the position of the attribute wanted.
#      * @return the output attribute being int the position passed as an argument.
#  */
  def getOutputAttribute(self,pos):
    if pos<0 or pos >= len(self.outputAttr):
        return None;
    return self.outputAttr.elementAt(pos);
  #end getOutputAttribute

# /**
#  * It does return an String with the @outputs in keel format.
#  * @return an string with the @outputs definition  .
#  */
  def getOutputHeader(self):
    aux = "@outputs ";
    ending = ",";
    for i in range (0, len(self.outputAttr)):
      if (i == len(self.outputAttr) - 1):
          ending = "";
      aux += (self.outputAttr.elementAt(i)).getName() + ending;

    return aux;
  #end getOutputHeader

# /**
#  * It does return a String with all the output attributes definition in keel
#  * format. The order of the attributes is the order of lecture.
#  * @return a String with the output attributes definition.
#  */
  def  getOutputAttributesHeader(self):
    aux = "";
    for i in range (0, len(self.outputAttr)):
        #Writting the name and type of the attribute
        aux += (self.outputAttr.elementAt(i)).toString()+"\n";

    return aux;
  #end getOutputAttributesHeader


# /**
#  * It returns the undefined attribute being int the position passed as an argument.
#  * @param pos is the position of the attribute wanted.
#      * @return the undefined attribute being int the position passed as an argument.
#  *
#  */
  def  getUndefinedAttribute( self,pos):
   if (pos<0 or pos >= len(self.undefinedAttr)):
       return None;
   return self.undefinedAttr.elementAt(pos);
  #end getUndefinedAttribute

# /**
#  * It does return all the undefined attributes
#      * @return all the undefined attributes
#  */
  def  getUndefinedAttributes(self):
    if (self.undefinedAttr.size() == 0):
        return None;
    attr = self.undefinedAttr;
    for i in range(0,attr.length):
      attr[i] = self.undefinedAttr.elementAt(i);

    return attr;
  #end getUndefinedAttributes

# /**
#  * It does return a String with all the undefined attributes definition
#  * in keel format. The order of the attributes is the order of lecture.
#  * @return a String with the input attributes definition.
#  */
  def getUndefinedAttributesHeader(self):
    aux = "";
    for i in range (0, undefinedAttr.size()):
        #Writting the name and type of the attribute
        aux += (self.undefinedAttr.elementAt(i)).toString()+"\n";

    return aux;
  #end getUndefinedAttributesHeader

# /**
#  * It returns the attribute being int the position passed as an argument.
#  * @param pos is the position of the attribute wanted.
#      * @return the attribute being int the position passed as an argument.
#  *

  def getAttribute(self, pos):
   return self.attributes.elementAt(pos);
  #end getAttribute

# /**
#  * It return the total number of attributes in the API
#  * @return an int with the number of attributes
#  */
  def getNumAttributes(self):
    return len(self.attributes)
  #end getNumAttributes


# /**
#  * It return the  number of input attributes in the API
#  * @return an int with the number of attributes
#  */
  def getInputNumAttributes(self):
    return len(self.inputAttr)
  #end getInputNumAttributes

# /**
#  * It return the number of output attributes in the API
#  * @return an int with the number of attributes
#  */
  def getOutputNumAttributes(self):
    return len(self.outputAttr)
  #end getOutputNumAttributes

# /**
#  * It return the number of undefined attributes in the API
#  * @return an int with the number of attributes
#  */
  def getUndefinedNumAttributes(self):
    return self.undefinedAttr.size();
  #end getUndefinedNumAttributes

# /**
#  * It returns all the attribute names in the dataset except these ones
#  * that are already in the vector v.
#  * @param v is a vector with the exceptions
#  * @return a Vector with the rest of attribute names.
#  */
  def getAttributesExcept(self,vector):
      restAt = []
      for i in (0, len(self.attributes)):
          attName = self.attributes.get(i).getName();
          if (attName not in vector):
              restAt.add(attName);

      return restAt;
  #end getAttributesExcept


# /**
#  * It organizes the whole number of attributes to input, output, and
#  * "no-direction" attributes.
#  * @param inAttNames  is a vector with the names of all input  attributes.
#  * @param outAttNames is a vector with the names of all output attributes.
#  */
  def setOutputInputAttributes(self,inAttNames, outAttNames):

    attName=""
    att=None

    for i in range (0, len(self.attributes)):
        att = self.attributes.get(i);
        attName = att.getName();
        if (attName in inAttNames):
            att.setDirectionAttribute(Attribute.INPUT);
            self.inputAttr.append(self.attributes.get(i));
        elif outAttNames.contains(attName):
            att.setDirectionAttribute(Attribute.OUTPUT);
            self.outputAttr.append(self.attributes.get(i));
        else:
            self.undefinedAttr.append(self.attributes.get(i));

    #Finally, making some statistics
    hasNominal = False;
    hasInteger = False;
    hasReal    = False;

    for index in range (0 ,2):
        if (self.index == 0):
            iterations = len(self.inputAttr)
        else:
            iterations = len(self.outputAttr)

        for i in range (0,iterations):
            if (index== 0):
                att = self.inputAttr.elementAt(i)
            else:
                att = self.outputAttr.elementAt(i)

            type = att.getType()
            if type==Attribute.NOMINAL:
                hasNominal = True;
            elif type==Attribute.INTEGER:
                hasInteger = True;
            elif type == Attribute.REAL:
                hasReal = True;

  #end setOutputInputAttributes

# /**
#  * This method checks if all the input names vector corresponds with
#  * all the attributes in input vector. If not, it returns a false. It
#  * is used in a test to check that the definition of input attributes
#  * is the same as the definition made in train.
#  * @param outputNames is a vector with all input attribute names.
#  */
  def areAllDefinedAsInputs(self,inputNames):
    if len(inputNames) != len(self.inputAttr):
        return False
    for i in range (0 ,len(self.inputAttr)):
        name = self.inputAttr.elementAt(i).getName()
        if name not in inputNames:
            return False;

    return True;
  #end areAllDefinedAsInputs


# /**
#  * This method checks if all the output names vector corresponds with
#  * all the attributes in output vector. If not, it returns a false. It
#  * is used in a test to check that the definition of output attributes
#  * is the same as the definition made in train.
#  * @param outputNames is a vector with all output attribute names.
#      * @return True if all the output names vector corresponds with
#  * all the attributes in output vector.
#  */

  def areAllDefinedAsOutputs(self,outputNames):
    if len(outputNames) != len(self.outputAttr):
        return False;

    for i in range (0, len(self.outputAttr)):
        name = self.outputAttr.elementAt(i).getName()
        if ( name not in outputNames ):
            return False;

    return True;
  #end areAllDefinedAsOutputs


# /**
#  * It sets the relation name.
#  * @param rel is the name to be set to the relationName
#  */
  def setRelationName(self,rel):
      self.relationName = rel;
  #end setRelationName

# /**
#  * It gets the relation name.
#  * @return an String with the realtion name.
#  */
  def getRelationName(self):
      return self.relationName;
  #end relationName

# /**
#  * It does remove an attribute. Removing an attribute only implies, in terms
#  * of Attribute static class, to take it out from the input/output attributes
#  * list, but it will never be removed from the attributes general list. So
#  * it will be placed as a NON-SPECIFIED attribute, as it wasn't declared in
#  * neither @inputs and @outputs definition.
#  * @param inputAtt is a boolean that indicates if the attribute to be removed
#  * is an input attribute
#  * @param whichAtt is an integer that indicates the position of the attribute
#  * to be removed.
#  * @return a boolean that will be false if the attribute hasn't been found.
#  */
  def removeAttribute( self,inputAtt, whichAtt):
    atToDel = None
    if ( inputAtt and (whichAtt >=  len(self.inputAttr) or whichAtt < 0)):
        return False;
    if (not inputAtt and (whichAtt >= len(self.outputAttr) or whichAtt < 0)):
        return False;
    if (inputAtt):
        #inputAttribute
        atToDel =  self.inputAttr.elementAt(whichAtt);
        atToDel.setDirectionAttribute(Attribute.DIR_NOT_DEF);
        self.inputAttr.removeElementAt(whichAtt);

    else :# output attribute
        atToDel = self.outputAttr.elementAt(whichAtt);
        atToDel.setDirectionAttribute(Attribute.DIR_NOT_DEF);
        self.outputAttr.removeElementAt(whichAtt);

    #We get the position where it has to go in the undefined attributes vector.
    self.undefPosition = self.searchUndefPosition(atToDel)
    self.undefinedAttr.insertElementAt(atToDel, self.undefPosition)

    self.hasNominal = False;
    self.hasInteger = False;
    self.hasReal    = False;
    for index in range (0, 2):
        if index == 0:
            iterations = len(self.inputAttr)
        else:
            iterations = len(self.outputAttr)

        for i in range (0,iterations):
            if index == 0:
                att = self.inputAttr.elementAt(i)
            else:
                self.outputAttr.elementAt(i)
            if self.index == 0:
                att = self.inputAttr.elementAt(i)
            else:
                att = self.outputAttr.elementAt(i)

            type=att.getType()
            if type==Attribute.NOMINAL:
                hasNominal = True;
            elif type == Attribute.INTEGER:
                hasInteger = True;

            elif type ==  Attribute.REAL:
                hasReal = True;

    return True;
  #end removeAttribute

#
# /**
#  * It does search the relative position of the input/output attribute
#  * 'whichAtt' in the list of indefined attributes.
#  * @param attToDel is an Attribute reference to the attribute that has to
#  * be deleted.
#  * @return an int with the relative position.
#  */
  def searchUndefPosition( self,attToDel):
      undefCount=0
      count = 0

      att_aux = self.attributes.elementAt(count);
      while (attToDel != att_aux):
         if (att_aux.getDirectionAttribute() == Attribute.DIR_NOT_DEF):
             undefCount+=1

         count+=1
         att_aux = self.attributes.elementAt(count);

      return undefCount;
  #end searchUndefPosition
#
# /**
#  * It does initializes the statistics to make the statistics. It only
#  * works for classifier Datasets (only one output).
#  */

  def initStatistics(self):
    if (self.outputAttr.size() != 1):
        return;

    classNumber = self.outputAttr.elementAt(0).getNumNominalValues()
    #If the output attribute has not been defined as a nominal or it has not
    #any value in the nominal list, the initalization is aborted.
    if classNumber<=0:
        return;

    for i in range (0, len(self.inputAttr)):
        (self.inputAttr.elementAt(i)).initStatistics(classNumber);

    #end initStatistics


# /**
#  * It does finish the statistics
#  */
  def finishStatistics(self):
    if (self.outputAttr.size() != 1):
        return;

    for i in range (0,len(self.inputAttr)):
        (self.inputAttr.elementAt(i)).finishStatistics();

   #end finishStatistics

# /**
#  * It does print the attributes information
#  */
  def  printHere(self):
    print("@relation = "+ self.relationName)
    for i in range(0,self.attributes.size()):
        att = self.attributes.elementAt(i);
        if (att.getDirectionAttribute() == Attribute.INPUT):
            print("INPUT ATTRIBUTE:");
        elif (att.getDirectionAttribute() == Attribute.OUTPUT):
            print("OUTPUT ATTRIBUTE:");
        else:
            print("UNDEFINED ATTRIBUTE:");

        att.print();

   #end print


  #end of Attributes class





