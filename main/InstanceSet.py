'''
    This class contains a complete set of instances. Its public methods are:
    numInstances
    Returns the number of instances of the Instance Set.
    getInstance
    Returns a concrete instance contained in the Instance Set.
    getInstances
    Returns an array with all the instances of the Instance Set.
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

 * <p>
 * <b> InstanceSet </b>
 * </p>
 *
 * The instance set class mantains a pool of instances read from the keel
 * formated data file. It provides a set of methods that permit to get
 * each instance, get the whole set of instances, get the number of instances,
 * etc.
 *
 * @author Albert Orriols Puig
 * @version keel0.1
 * @see Instance
 * @see Attributes
'''

from FormatErrorKeeper import FormatErrorKeeper;
from main import InstanceParser;
from main import Attribute;
from main import Attributes;
from InstanceAttributes import InstanceAttributes;
from main import Instance;
from main import ErrorInfo;


class InstanceSet:
    '''
   /////////////////////////////////////////////////////////////////////////////
   //////////////// ATTRIBUTES OF THE INSTANCESET CLASS ////////////////////////
   /////////////////////////////////////////////////////////////////////////////

   '''


# Attribute where all the instances of the DB are stored.

    instanceSet = [];

    # String where the header of the file is stored.

    header = "";

    # String where only the attributes definition header is stored
    attHeader = "";
    '''
     * Object that collects all the errors happened while reading the test and
     * train datasets.
    '''
    errorLogger = FormatErrorKeeper();

    # This object contains the attributes definitions

    attributes = InstanceAttributes();
    '''
     * It indicates if the attributes has not be stored as non-static, permiting
     * the load of different datasets
    '''
    storeAttributesAsNonStatic = None;

    # It indicates that the output attribute has been infered as the last one

    outputInfered = None;
    '''
    /////////////////////////////////////////////////////////////////////////////
    ///////////////// METHODS OF THE INSTANCESET CLASS //////////////////////////
    /////////////////////////////////////////////////////////////////////////////
    '''

    # It instances a new instance of InstanceSet

    def __init__(self,storeAttributesAsNonStatic=False, ins=None):

        if(ins!=None):
            self.instanceSet = ins.instanSet.copy();

            self.header = str(ins.header);
            self.attHeader = str(ins.attHeader);
            self.attributes = str(ins.attributes);
            self.storeAttributesAsNonStatic = ins.storeAttributesAsNonStatic;
        else:
            self.storeAttributesAsNonStatic = storeAttributesAsNonStatic;
            self.attributes = None;
    # end InstanceSet
    '''
    def InstanceSet(self, nonStaticAttributes):
        self.storeAttributesAsNonStatic = nonStaticAttributes;
        # if ( storeAttributesAsNonStatic ) Attributes.clearAll();
        attributes = None;
    '''
    '''
    def InstanceSet(self, ins):
        self.instanceSet = ins.instanSet.copy();
    
        self.header = str(ins.header);
        self.attHeader = str(ins.attHeader);
        self.attributes = str(ins.attributes);
        self.storeAttributesAsNonStatic = ins.storeAttributesAsNonStatic;
     '''
    # end InstanceSet
    '''
     * InstanceSet
     *
     * This constructor permit define if the attribute's definition need to be
     * stored as non-static (nonStaticAttributes = true). Otherwise, if 
     * nonStaticAttributes = false, using this constructor is equivalent to use
     * the constructor by default.
    '''
    '''
       * Creates a new InstanceSet with the header and Instances from the passed object
       * It performs a deep (new allocated) copy.
       * @param is Original InstanceSe
    '''

    '''
     * setAttributesAsNonStatic
     *
     * It stores the static-defined attributes in the class Attributes as
     * non static in the object attributes. After this it does not remove the
     * static-definition of the Attributes; this is in that way to permit to 
     * call this functions for differents datasets from the same problem, such
     * as, a train dataset and the correspondent test dataset.
     */
     '''


    def setAttributesAsNonStatic():
        attributes = InstanceAttributes();
        attributes.copyStaticAttributes();

        storeAttributesAsNonStatic = True;


    # end setAttributesAsNonStatic
    '''
    /**
     * getAttributeDefinitions
     *
     * It does return the definition of the attibutes contained in the dataset.
     * 
     * @return InstanceAttributes contains the attribute's definitions.
    '''


    def getAttributeDefinitions():
        return attributes;


    # end InstanceAttributes

    '''
     * This method reads all the information in a DB and load it to memory.
     * @param fileName is the database file name. 
     * @param isTrain is a flag that indicate if the database is for a train or for a test.
     * @throws DatasetException if there is any semantical error in the input file.
     * @throws HeaderFormatException if there is any lexical or sintactical error in the 
     * header of the input file
    '''


    def readSet(fileName, isTrain):
        try:
            line = "";
            print("Opening the file: " + fileName + ".");
            # Parsing the header of the DB.
            errorLogger = FormatErrorKeeper();
            # Declaring an instance parser
            parser = InstanceParser(fileName, isTrain);
            # Reading information in the header, i.e., @relation, @attribute, @inputs and @outputs
            parseHeader(parser, isTrain);
            print(" The number of output attributes is: " + Attributes.getOutputNumAttributes());
            # The attributes statistics are init if we are in train mode.
            if (isTrain and Attributes.getOutputNumAttributes() == 1):
                Attributes.initStatistics();
            # A temporal vector is used to store the instances read.
            # print( "\n\n  > Reading the data ");
            print("Reading the data");
            tempSet = [[0] * 1000] * 10000;
            line = parser.getLine();
            while (line != None):
                # System.out.println ("    > Data line: " + line );
                newInstance = Instance(line, isTrain, tempSet.size());
                tempSet.append(newInstance);

                # The vector of instances is converted to an array of instances.
                sizeInstance = tempSet.size();
                print("    > Number of instances read: " + tempSet.size());
                instanceSet = Instance[sizeInstance];
                for i in range(0, sizeInstance):
                    instanceSet[i] = Instance(tempSet[i]);

                print("After converting all instances");
                # System.out.println("The error logger has any error: "+errorLogger.getNumErrors());
                if (errorLogger.getNumErrors() > 0):
                    print("There has been " + errorLogger.getAllErrors().size() + "errors in the Dataset format.");
                    for k in range(0, errorLogger.getNumErrors()):
                        errorLogger.getError(k).print();
        except Exception:
            print("There has been " + errorLogger.getAllErrors().size() + " errors in the Dataset format",
                  errorLogger.getAllErrors());
            print(
                "\n  > Finishing the statistics: (isTrain)" + isTrain + ", (# out attributes)" + Attributes.getOutputNumAttributes());
        # If being on a train dataset, the statistics are finished
        if (isTrain and Attributes.getOutputNumAttributes() == 1):
            Attributes.finishStatistics();
        # close the stream
        parser.close();

        print("  >> File LOADED CORRECTLY!!");


    # end of InstanceSet constructor.


    '''
     * It reads the information in the header of the file. 
     * It reads relation's name, attributes' names, and inputs and outputs.
     *
     * @param parser is the parser of the data set
     * @param isTrain is a boolean indicating if this is a train set (and so
     * parameters information must be read) or a test set (parameters information 
     * has not to be read).
    '''


    def parseHeader(parser, isTrain):
        # 1. Declaration of variables
        inputAttrNames = [];
        outputAttrNames = [];

        inputsDef = False;
        outputsDef = False;

        line = "";
        aux = "";
        header = "";

        attCount = 0;
        lineCount = 0;

        attHeader = None;

        line = parser.getLine().trim();
        while (line.equalsIgnoreCase("@data") == False):
            line = line.trim();
            # System.out.println ("  > Line read: " + line +"." );
            lineCount += 1;
            if (line.toLowerCase().indexOf("@relation") != -1):
                if (isTrain):
                    Attributes.setRelationName(line.replaceAll("@relation", ""));

            if (line.toLowerCase().indexOf("@attribute") != -1):
                if (isTrain):
                    insertAttribute(line);
                attCount += 1;

            if (line.toLowerCase().indexOf("@inputs") != -1):
                attHeader = header;
                inputsDef = True;

                aux = line.substring(8);

                if (isTrain == True):
                    insertInputOutput(aux, lineCount, inputAttrNames, "inputs", isTrain);

            if (line.toLowerCase().indexOf("@outputs") != -1):
                if (attHeader == None):
                    attHeader = header;
                outputsDef = True;
                # System.out.println ( " >>> Defining the output !!!");

                aux = line.substring(8);
                if (isTrain == True):
                    insertInputOutput(aux, lineCount, outputAttrNames, "outputs", isTrain);

                print(" >> Size of the output is: " + outputAttrNames.size());

            header += line + "\n";

        if (attHeader == None):
            attHeader = header;

        processInputsAndOutputs(isTrain, inputsDef, outputsDef, outputAttrNames, inputAttrNames);


    # end headerParse

    def insertAttribute(line):
        indexL = 0,
        indexR = 0;
        type = "";

        # Treating string and declaring a string tokenizer
        line.replace("{", " {");
        # line.replace ("["," [");

        # System.out.println ("  > Processing line: "+  line );
        st = line.split(" [{\t");

        # Disregarding the first token. It is @attribute
        st.nextToken();

        at = Attribute();
        at.setName(st.nextToken().trim());
        # System.out.println ( "   > Attribute name: "+ at.getName() );

        # Next action depends on the type of attribute: continuous or nominal
        if (st.hasMoreTokens() == False):  # Parsing a nominal attribute with no definition of values
            # System.out.println ("    > Parsing nominal attribute without values ");
            at.setType(Attribute.NOMINAL);

        elif (line.indexOf("{") != -1):  # Parsing a nominal attribute
            # System.out.println ("    > Parsing nominal attribute with values: "+line );
            at.setType(Attribute.NOMINAL);
            at.setFixedBounds(True);

            indexL = line.indexOf("{");
            indexR = line.indexOf("}");

            # System.out.println ( "      > The Nominal values are: " + line.substring( indexL+1, indexR) );
            lineSub = line.substring(indexL + 1, indexR);
            st2 = lineSub.split(",");

            while (st2.hasMoreTokens()):
                at.addNominalValue(st2.nextToken().trim());


        else:  # Parsing an integer or real
            type = st.nextToken().trim();

            # System.out.println ("    > Parsing "+ type + " attributes");
            if (type.equalsIgnoreCase("integer")): at.setType(Attribute.INTEGER);
            if (type.equalsIgnoreCase("real")):   at.setType(Attribute.REAL);

            indexL = line.indexOf("[");
            indexR = line.indexOf("]");

            if (indexL != -1 and indexR != - 1):
                # System.out.println ( "      > The real values are: " + line.substring( indexL+1, indexR) );
                lineSub = line.substring(indexL + 1, indexR);
                st2 = lineSub(",");

                min = float(st2.nextToken().trim());
                max = float(st2.nextToken().trim());

                at.setBounds(min, max);

                Attributes.addAttribute(at);


    # end insertAttribute


    def insertInputOutput(line, lineCount, collection, type, isTrain):
        attName = "";

        print(" >> processing: " + line);

        # Declaring StringTokenizer
        st = line.split(",");

        while (st.hasMoreTokens()):
            attName = st.nextToken().trim();

            if (Attributes.getAttribute(attName) == None):
                # If this attribute has not been declared, generate error
                er = ErrorInfo(ErrorInfo.InputTestAttributeNotDefined, 0, lineCount, 0, 0, isTrain,
                               ("The attribute " + attName + " defined in @" + type +
                                " in test, it has not been defined in @inputs in its train dataset. It will be ignored"));
                InstanceSet.errorLogger.setError(er);

            else:
                print("   > " + type + " attribute considered: " + attName + ".");
                collection.add(attName);


    # end insertInputOutput


    def processInputsAndOutputs(isTrain, inputsDef, outputsDef, outputAttrNames, inputAttrNames):
        # Afteer parsing the header, the inputs and the outputs are prepared.
        print(" >> Processing inputs and outputs");
        outputInfered = False;
        if (isTrain == True):
            if (inputsDef == False and outputsDef == False):
                outputAttrNames.add(Attributes.getAttribute(Attributes.getNumAttributes() - 1).getName());
                inputAttrNames = Attributes.getAttributesExcept(outputAttrNames);
                outputInfered = True;
            elif (inputsDef == False and outputsDef == True):
                inputAttrNames = Attributes.getAttributesExcept(outputAttrNames);
            elif (inputsDef == True and outputsDef == False):
                outputAttrNames = Attributes.getAttributesExcept(inputAttrNames);
                outputInfered = True;

            Attributes.setOutputInputAttributes(inputAttrNames, outputAttrNames);


    # end of processInputsAndOutputs

    '''
     * Test if the output attribute has been infered.
     * @return True if the output attribute has been infered. False if not.
     '''


    def isOutputInfered():
        return outputInfered;


    '''
     * It returns the number of instances.
     * @return an int with the number of instances.
    '''


    def getNumInstances(self):
        if (self.instanceSet != None):
            return len(self.instanceSet);
        else:
            return 0;
        # end numInstances


    '''
     * Gets the instance located at the cursor position.
     * @return the instance located at the cursor position.
    '''


    def getInstance(self, whichInstance):
        if (whichInstance < 0 or whichInstance >= self.instanceSet.length):
            return None
        return instanceSet[whichInstance];


    # end getInstance


    '''
     * It returns all the instances of the class.
     * @return Instance[] with all the instances of the class.
     */
      public Instance[] getInstances() {
        return instanceSet;
      }//end getInstances
    '''
    '''
     * Returns the value of an integer or a real input attribute of an instance
     * in the instanceSet.
     * @param whichInst is the position of the instance.
     * @param whichAttr is the position of the input attribute.
     * @return a String with the numeric value.
     * @throws ArrayIndexOutOfBoundsException If the index is out of the instance
     * set size.
    '''


    def getInputNumericValue(self, whichInst, whichAttr):
        if (whichInst < 0 or whichInst >= len(self.instanceSet)):
            raise IndexError(
                "You are trying to access to " + whichInst + " instance and there are only " + instanceSet.length + ".");
        return instanceSet[whichInst].getInputRealValues(whichAttr);


    # end getInputNumericValue


    '''
     * Returns the value of an integer or a real output attribute of an instance
     * in the instanceSet.
     * @param whichInst is the position of the instance.
     * @param whichAttr is the position of the output attribute.
     * @return a String with the numeric value.
     * @throws ArrayIndexOutOfBoundsException If the index is out of the instance
     * set size.
    '''


    def getOutputNumericValue(whichInst, whichAttr):
        if (whichInst < 0 or whichInst >= instanceSet.length):
            print(ArrayIndexOutOfBoundsException(
                "You are trying to access to " + whichInst + " instance and there are only " + instanceSet.length + "."));
        return instanceSet[whichInst].getOutputRealValues(whichAttr);
        # end getOutputNumericValue


    '''
     * Returns the value of a nominal input attribute of an instance in the 
     * instanceSet.
     * @param whichInst is the position of the instance.
     * @param whichAttr is the position of the input attribute.
     * @return a String with the nominal value.
     * @throws ArrayIndexOutOfBoundsException If the index is out of the instance
     * set size.
    '''


    def getInputNominalValue(whichInst, whichAttr):
        if (whichInst < 0 or whichInst >= instanceSet.length):
            print(ArrayIndexOutOfBoundsException(
                "You are trying to access to " + whichInst + " instance and there are only " + instanceSet.length + "."))
        # end getInputNominalValue


    '''
     * Returns the value of a nominal output attribute of an instance in the 
     * instanceSet.
     * @param whichInst is the position of the instance.
     * @param whichAttr is the position of the output attribute.
     * @return a String with the nominal value.
     * @throws ArrayIndexOutOfBoundsException If the index is out of the instance
     * set size.
    '''


    def getOutputNominalValue(whichInst, whichAttr):
        if (whichInst < 0 or whichInst >= instanceSet.length):
            print("You are trying to access to " + whichInst + " instance and there are only " + instanceSet.length + ".");
        return instanceSet[whichInst].getOutputNominalValues(whichAttr);
        # end getOutputNumericValue


    '''
     * It does remove the instance i from the instanceSet.
     * @param instNum is the instance removed from the instanceSet.
    '''


    def removeInstance(self, instNum):
        if (instNum < 0 or instNum >= instanceSet.length):
            return;
        aux = Instance[len(self.instanceSet) - 1];
        add = 0;
        for i in range(0, instanceSet.length):
            if (instNum == i):
                add = 1;
            else:
                aux[i - add] = instanceSet[i];

        # Copying the auxiliar to the instanceSet variable
        instanceSet = aux;
        aux = None;  # avoiding memory leaks (not necessary in this case)


    # end removeInstance


    '''
     * It does remove an attribute. To remove an attribute, the train and the
     * test sets have to be passed to mantain the coherence of the system. 
     * Otherwise, only the attribute of the train set would be removed, leaving
     * inconsistent the instances of the test set, because of having one extra
     * attribute inexistent anymore.
     *
     * @param tSet is the test set. 
     * @param inputAtt is a boolean that is true when the attribute that is 
     * wanted to be removed is an input attribute.
     * @param whichAtt is a integer that indicate the position of the attriubte
     * to be deleted.
     * @return a boolean indicating if the attribute has been deleted
    '''


    def removeAttribute(self, tSet, inputAtt, whichAtt):
        attToDel = None;
        # Getting a reference to the attribute to del
        if (inputAtt == True):
            if (storeAttributesAsNonStatic and attributes != None):
                attToDel = attributes.getInputAttribute(whichAtt);
            else:
                attToDel = Attributes.getInputAttribute(whichAtt);

        else:
            if (storeAttributesAsNonStatic and attributes != None):
                attToDel = attributes.getOutputAttribute(whichAtt);
            else:
                attToDel = Attributes.getOutputAttribute(whichAtt);

        if (storeAttributesAsNonStatic == True and attributes != None):
            print("Removing the attribute");
        if (attributes.removeAttribute(inputAtt, whichAtt) == False or (
                tSet != None and tSet.attributes.removeAttribute(inputAtt, whichAtt)) == False):
            return False;
        else:
            if (Attributes.removeAttribute(inputAtt, whichAtt) == False):
                return False;
        for i in range(0, instanceSet.length):
            if (storeAttributesAsNonStatic and attributes != None):
                instanceSet[i].removeAttribute(attributes, attToDel, inputAtt, whichAtt);
            else:
                instanceSet[i].removeAttribute(attToDel, inputAtt, whichAtt);

        if (tSet != None):
            for i in range(0, tSet.instanceSet.length):

                if (storeAttributesAsNonStatic == True and attributes != None):
                    tSet.instanceSet[i].removeAttribute(attributes, attToDel, inputAtt, whichAtt);
            else:
                tSet.instanceSet[i].removeAttribute(attToDel, inputAtt, whichAtt);
            return True;


    # end removeAttribute

    '''
     * It returns the header.
     * @return a String with the header of the file.
    '''


    def getHeader(self):
        return self.header;


    # end getHeader

    def setHeader(copia):
        header = str(copia);


    # end getHeader

    def getAttHeader(self):
        return self.attHeader;


    # end getHeader


    def setAttHeader(copia):
        attHeader = str(copia);


    # end getHeader


    '''
     * It does return a new header (not necessary the same header as the 
     * input file one). It only includes the valid attributes, those ones
     * defined in @inputs and @outputs (or taken as that role following the
     * keel format specification).
     * @return a String with the new header
    '''


    def getNewHeader(self):
        line = "";
        attrs = [];

        # Getting the relation name and the attributes
        if (self.storeAttributesAsNonStatic == True and attributes != None):
            line = "@relation " + attributes.getRelationName() + "\n";
            attrs = attributes.getInputAttributes();
        else:
            line = "@relation " + Attributes.getRelationName() + "\n";
            attrs = Attributes.getInputAttributes();

        for i in range(0, attrs.length):
            line += attrs[i].toString() + "\n";
            # Gettin all the outputs attributes
        if (storeAttributesAsNonStatic and attributes != None):
            attrs = attributes.getOutputAttributes();
            line += attrs[0].toString() + "\n";
            # Getting @inputs and @outputs
            line += attributes.getInputHeader() + "\n";
            line += attributes.getOutputHeader() + "\n";

        else:
            attrs = Attributes.getOutputAttributes();
            line += attrs[0].toString() + "\n";

        # Getting @inputs and @outputs
        line += Attributes.getInputHeader() + "\n";
        line += Attributes.getOutputHeader() + "\n";

        return line;


    # end getNewHeader


    '''
     * It does return the original header definiton but
     * without @input and @output in there
    '''


    def getOriginalHeaderWithoutInOut():
        line = "";
        attrs = [];

        # Getting the relation name and the attributes
        if (storeAttributesAsNonStatic and attributes != None):
            line = "@relation " + attributes.getRelationName() + "\n";
            attrs = attributes.getAttributes();

        else:
            line = "@relation " + Attributes.getRelationName() + "\n";
            attrs = Attributes.getAttributes();

        for i in range(0, attrs.length):
            line = line + attrs[i].toString() + "\n";
        return line;
        # end getOriginalHeaderWithoutInOut;


    '''
     * It prints the dataset to the specified PrintWriter
     * @param out is the PrintWriter where to print
    '''


    def print(out):
        for i in range(0, instanceSet.length):
            out.println("> Instance " + i + ":");
        if (storeAttributesAsNonStatic == True and attributes != None):
            instanceSet[i].print(attributes, out);
        else:
            instanceSet[i].print(out);


    # end print

    '''
     * It prints the dataset to the specified PrintWriter.
     * The order of the attributes is the same as in the 
     * original file
     * @param out is the PrintWriter where to print
     * @param printInOut indicates if the @inputs (1), @outputs(2), 
     * both of them (3) or any (0) has to be printed
    '''


    def printAsOriginal(out, int):
        # Printing the header as the original one
        out.println(header);

        if (storeAttributesAsNonStatic and attributes != None):
            if (printInOut == 1 or printInOut == 3):
                out.println(attributes.getInputHeader());

        if (printInOut == 2 or printInOut == 3):

            out.println(attributes.getOutputHeader());

        else:
            if (printInOut == 1 or printInOut == 3):
                out.println(Attributes.getInputHeader());
            if (printInOut == 2 or printInOut == 3):
                out.println(Attributes.getOutputHeader());

        out.print("@data");
        for i in range(0, instanceSet.length):
            out.println();
            if (storeAttributesAsNonStatic and attributes != None):
                instanceSet[i].printAsOriginal(attributes, out);
        else:
            instanceSet[i].printAsOriginal(out);


    # end printAsOriginal


    def print():
        print("------------- ATTRIBUTES --------------");
        if (storeAttributesAsNonStatic and attributes != None):
            attributes.print();

        else:
            Attributes.print();

        print("-------------- INSTANCES --------------");
        for i in range(0, instanceSet.length):
            print("\n> Instance " + i + ":");

            if (storeAttributesAsNonStatic and attributes != None):
                instanceSet[i].print(attributes);
        else:
            instanceSet[i].print();


    # end print


    # Remove all instances from this InstanceSet

    def clearInstances():
        instanceSet = None;


    '''
       * It adds the passed instance at the end of the present InstanceSet
       * @param inst the instance to be added
    '''


    def addInstance(self, inst):
        i = 0;
        nVector = [];
        if (self.instanceSet != None):
            nVector = Instance[self.instanceSet.length + 1];
            for i in range(0, self.instanceSet.length):
                nVector[i] = self.instanceSet[i];

        else:
            nVector = Instance[1];

            nVector[i] = inst;
            instanceSet = nVector;

    '''
       * Clear the non-Static attributes. The static class Attributes is not modified.
    '''


    def clearNonStaticAttributes(self):
        self.attributes = None;


    '''
       * Appends the given attribute to the non-static list of the current InstanceSet
       * @param at The Attribute to be Appended
    '''


    def addAttribute(self, att):
        if (self.attributes == None):
            attributes = InstanceAttributes();
        attributes.addAttribute(att);

    # end of InstanceSet Class.
