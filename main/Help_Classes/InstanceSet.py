'''
    This class contains a complete set of instances. Its public methods are:
    numInstances
    Returns the number of instances of the Instance Set.
    getInstance
    Returns a concrete instance contained in the Instance Set.
    getInstances
    Returns an array with all the instances of the Instance Set.
'''
    # /***********************************************************************
    #
	# This file is part of KEEL-software, the Data Mining tool for regression,
	# classification, clustering, pattern mining and so on.
    #
	# Copyright (C) 2004-2010
	#
	# F. Herrera (herrera@decsai.ugr.es)
    # L. S谩nchez (luciano@uniovi.es)
    # J. Alcal谩-Fdez (jalcala@decsai.ugr.es)
    # S. Garc铆a (sglopez@ujaen.es)
    # A. Fern谩ndez (alberto.fernandez@ujaen.es)
    # J. Luengo (julianlm@decsai.ugr.es)
    #
	# This program is free software: you can redistribute it and/or modify
	# it under the terms of the GNU General Public License as published by
	# the Free Software Foundation, either version 3 of the License, or
	# (at your option) any later version.
    #
	# This program is distributed in the hope that it will be useful,
	# but WITHOUT ANY WARRANTY; without even the implied warranty of
	# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
	# GNU General Public License for more details.
    #
	# You should have received a copy of the GNU General Public License
	# along with this program.  If not, see http://www.gnu.org/licenses/
  
# **********************************************************************/

#  * <p>
#  * <b> InstanceSet </b>
#  * </p>
#  *
#  * The instance set class mantains a pool of instances read from the keel
#  * formated data file. It provides a set of methods that permit to get
#  * each instance, get the whole set of instances, get the number of instances,
#  * etc.
#  *
#  * @author Albert Orriols Puig
#  * @version keel0.1
#  * @see Instance
#  * @see Attributes
#
from Help_Classes.FormatErrorKeeper import FormatErrorKeeper
from Help_Classes.InstanceParser import InstanceParser
from Help_Classes.Attribute import Attribute
from Help_Classes.Attributes import Attributes
from Help_Classes.InstanceAttributes import InstanceAttributes
from Help_Classes.Instance import Instance
from Help_Classes.ErrorInfo import ErrorInfo
from pathlib import Path

class InstanceSet:

   # /////////////////////////////////////////////////////////////////////////////
   # //////////////// ATTRIBUTES OF THE INSTANCESET CLASS ////////////////////////
   # /////////////////////////////////////////////////////////////////////////////

   # Attribute where all the instances of the DB are stored.

    instanceSet = [];

    # String where the header of the file is stored.

    header = "";

    # String where only the attributes definition header is stored
    attHeader = "";
    # '''
    #  * Object that collects all the errors happened while reading the test and
    #  * train datasets.
    # '''
    errorLogger = FormatErrorKeeper();

    # This object contains the attributes definitions

    attributes = InstanceAttributes();
    # '''
    #  * It indicates if the attributes has not be stored as non-static, permiting
    #  * the load of different datasets
    # '''
    storeAttributesAsNonStatic = None;

    # It indicates that the output attribute has been infered as the last one

    outputInfered = None;

    # /////////////////////////////////////////////////////////////////////////////
    # ///////////////// METHODS OF THE INSTANCESET CLASS //////////////////////////
    # /////////////////////////////////////////////////////////////////////////////

    # It instances a new instance of InstanceSet
    data_folder = Path("simpleTest/datasets/iris/")
    file_to_open= None

    def __init__(self,storeAttributesAsNonStatic=False, ins=None):

        print("In __init__ method in InstanceSet.")

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

    def InstanceSetWithNonSAtrr(self, nonStaticAttributes):
        self.storeAttributesAsNonStatic = nonStaticAttributes;
        # if ( storeAttributesAsNonStatic ) Attributes.clearAll();
        attributes = None;

    def InstanceSetWithIns(self, ins):
        self.instanceSet = ins.instanSet.copy();
    
        self.header = str(ins.header);
        self.attHeader = str(ins.attHeader);
        self.attributes = str(ins.attributes);
        self.storeAttributesAsNonStatic = ins.storeAttributesAsNonStatic;

    # end InstanceSet
    
     # * InstanceSet
     # *
     # * This constructor permit define if the attribute's definition need to be
     # * stored as non-static (nonStaticAttributes = true). Otherwise, if 
     # * nonStaticAttributes = false, using this constructor is equivalent to use
     # * the constructor by default.

     # * Creates a new InstanceSet with the header and Instances from the passed object
     # * It performs a deep (new allocated) copy.
     # * @param is Original InstanceSe

     # * setAttributesAsNonStatic
     # *
     # * It stores the static-defined attributes in the class Attributes as
     # * non static in the object attributes. After this it does not remove the
     # * static-definition of the Attributes; this is in that way to permit to 
     # * call this functions for differents datasets from the same problem, such
     # * as, a train dataset and the correspondent test dataset.
     # */
    
    def setAttributesAsNonStatic(self):
        attributes = InstanceAttributes();
        attributes.copyStaticAttributes();

        storeAttributesAsNonStatic = True;

    # end setAttributesAsNonStatic
    
    # /**
    #  * getAttributeDefinitions
    #  *
    #  * It does return the definition of the attibutes contained in the dataset.
    #  * 
    #  * @return InstanceAttributes contains the attribute's definitions.

    def getAttributeDefinitions(self):
        return self.attributes

    # end InstanceAttributes

     # * This method reads all the information in a DB and load it to memory.
     # * @param fileName is the database file name.
     # * @param isTrain is a flag that indicate if the database is for a train or for a test.
     # * @throws DatasetException if there is any semantical error in the input file.
     # * @throws HeaderFormatException if there is any lexical or sintactical error in the
     # * header of the input file

    def readSet(self,fileName, isTrain):
        print("Before try in readSet of InstanceSet, fileName is :" + str(fileName) + ".")
        print("Opening the file in readSet of InstanceSet: " + str(fileName) + ".")
        for file in fileName:
            try:
                # Parsing the header of the DB.
                errorLogger = FormatErrorKeeper()
                self.file_to_open=self.data_folder/file
                    # Declaring an instance parser
                print("In readSet,file_to_open is:"+ str(self.file_to_open))
                parser = InstanceParser(self.file_to_open, isTrain);
                    # Reading information in the header, i.e., @relation, @attribute, @inputs and @outputs
                print("In readSet finished read file " + str(self.file_to_open))
                self.parseHeader(parser, isTrain);
                print(" The number of output attributes is: " + Attributes.getOutputNumAttributes());
                    # The attributes statistics are init if we are in train mode.
                if (isTrain and Attributes.getOutputNumAttributes() == 1):
                    Attributes.initStatistics();
                    # A temporal vector is used to store the instances read.
                    # print( "\n\n  > Reading the data ");
                    print("Reading the data");
                    tempSet = [[0] * 1000] * 10000;
                    lines = parser.getLines();
                    while (lines != None):
                        print( "Data line: " + lines)
                    newInstance = Instance(lines, isTrain, len(tempSet));
                    tempSet.append(newInstance);

                        # The vector of instances is converted to an array of instances.
                    sizeInstance = len(tempSet)
                    print(" Number of instances read: " + str(sizeInstance));
                    instanceSet = Instance[sizeInstance];
                    for i in range(0, sizeInstance):
                        instanceSet[i] = Instance(tempSet[i]);

                        print("After converting all instances");
                         # System.out.println("The error logger has any error: "+errorLogger.getNumErrors());
                        if errorLogger.getNumErrors() > 0:
                            print("There has been " + errorLogger.getAllErrors().size() + "errors in the Dataset format.");
                            for k in range(0, errorLogger.getNumErrors()):
                                errorLogger.getError(k).print();
            except Exception as e :
                print("Unexpected error in readSet of InstanceSet class :" + str(e))

             #print("There has been " + errorLogger.getAllErrors().size() + " errors in the Dataset format",
        #           errorLogger.getAllErrors());
        #     print(
        #         "\n  > Finishing the statistics: (isTrain)" + isTrain + ", (# out attributes)" + Attributes.getOutputNumAttributes());
        # # If being on a train dataset, the statistics are finished
        # if (isTrain and Attributes.getOutputNumAttributes() == 1):
        #     Attributes.finishStatistics();
        # # close the stream
        # parser.close();
        #
        # print("  >> File LOADED CORRECTLY!!");

        # end of InstanceSet constructor.

         # * It reads the information in the header of the file.
         # * It reads relation's name, attributes' names, and inputs and outputs.
         # *
         # * @param parser is the parser of the data set
         # * @param isTrain is a boolean indicating if this is a train set (and so
         # * parameters information must be read) or a test set (parameters information
         # * has not to be read).

    def parseHeader(self,parser, isTrain):
        # 1. Declaration of variables
        inputAttrNames = [];
        outputAttrNames = [];

        inputsDef = False;
        outputsDef = False;

        aux = ""
        header = ""

        attCount = 0
        lineCount = 0

        attHeader = None

        print("Begin to call the InstanceParser.getLines(),parser.getLines(), in InstanceSet.")
        lines = parser.getLines()

        for line in lines:
            line = str(line).strip().lower()
            print("In parseHeader method of InstanceSet, the line is:" + line)
            if (line=="@data".lower()):
                break
            else:
                print("  Line read: " + line +"." )
                lineCount += 1;
                if ("@relation" in line):
                    if (isTrain):
                        relationName = str(line.replace("@relation", "")).strip()
                        print("set Relation name :" + str(relationName))
                        Attributes.setRelationName(self,relationName)

                elif ("@attribute" in line):
                    if (isTrain):
                        print("insert Attribute name :")
                        self.insertAttribute(line);
                        attCount += 1;

                elif ("@inputs" in line):
                        attHeader = header;
                        inputsDef = True;

                        aux = line.substring(8);

                        if (isTrain):
                            self.insertInputOutput(aux, lineCount, inputAttrNames, "inputs", isTrain);

                elif (str(line).lower().indexOf("@outputs") != -1):
                    if (attHeader == None):
                        attHeader = header
                        outputsDef = True
                        print( "Defining the output !!!");

                        aux = line.substring(8);
                        if (isTrain):
                            self.insertInputOutput(aux, lineCount, outputAttrNames, "outputs", isTrain);

                        print("Size of the output is: " + outputAttrNames.size());

                header += line + "\n";

        if (attHeader == None):
            attHeader = header;

        self.processInputsAndOutputs(isTrain, inputsDef, outputsDef, outputAttrNames, inputAttrNames);

    # end headerParse

    def insertAttribute(self,line):
        print("Insert attribute begin :")
        indexL = 0,
        indexR = 0;
        type = "";

        # Treating string and declaring a string tokenizer
        if "{" in line:
            token_str = "{"
            token_str_right="}"
        elif "[" in line:
            token_str = "["
            token_str_right = "]"
        token_withT= "\t" + token_str

        line=line.replace (token_str,token_withT);
        print("line with token_double:" + token_withT + "line:" + line)
        # System.out.println ("  > Processing line: "+  line );
        #st = line.split(" [{\t");
        st = line.split("\t")

        print("st after split is :" + str(st))
        # Disregarding the first token. It is @attribute
        st[0] = st[0].replace("@attribute","").strip()
        print("str[0] is:" + st[0])
        at = Attribute()
        at.setName(st[0])
        # System.out.println ( "   > Attribute name: "+ at.getName() );

        # Next action depends on the type of attribute: continuous or nominal
        if (len(st)==1):  # Parsing a nominal attribute with no definition of values
            # System.out.println ("    > Parsing nominal attribute without values ");
            at.setType(Attribute.NOMINAL)

        elif (token_str in line):  # Parsing a nominal attribute
            # System.out.println ("    > Parsing nominal attribute with values: "+line );
            at.setType(Attribute.NOMINAL)
            at.setFixedBounds(True)

            indexL = line.index(token_str)
            indexR = line.index(token_str_right)

            print( "The Nominal values are: " + line[indexL, indexR]);
            lineSub = line[indexL, indexR]
            print("The lineSub : " + lineSub)
            st2 = lineSub.split(",")

            while (st2.hasMoreTokens()):
                at.addNominalValue(st2.nextToken().strip())


        else:  # Parsing an integer or real
            type = st.nextToken().strip()

            # System.out.println ("    > Parsing "+ type + " attributes");
            if (type.lower() == "integer"):
                at.setType(Attribute.INTEGER);
            if (type.lower() == "real"):
                at.setType(Attribute.REAL);

            indexL = line.indexOf("[");
            indexR = line.indexOf("]");

            if (indexL is not -1 and indexR is not - 1):
                # System.out.println ( "      > The real values are: " + line.substring( indexL+1, indexR) );
                lineSub = line.substring(indexL + 1, indexR)
                st2 = lineSub(",")

                min = float(st2.nextToken().strip())
                max = float(st2.nextToken().strip())

                at.setBounds(min, max)
                print("Before add attribute : at"+str(at))
                Attributes.addAttribute(at)


    # end insertAttribute


    def insertInputOutput(line, lineCount, collection, type, isTrain):
        attName = "";

        print(" processing: " + line);

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


    def processInputsAndOutputs(self,isTrain, inputsDef, outputsDef, outputAttrNames, inputAttrNames):
        # Afteer parsing the header, the inputs and the outputs are prepared.
        print("Processing inputs and outputs");
        self.outputInfered = False;
        if (isTrain == True):
            print("isTrain == True")
            if (inputsDef == False and outputsDef == False):
                print("inputsDef == False and outputsDef == False")
                posHere = Attributes.getNumAttributes(self) - 1
                outputAttrNames.append(Attributes.getAttribute(self,posHere).getName());
                inputAttrNames = Attributes.getAttributesExcept(outputAttrNames);
                self.outputInfered = True;
            elif (inputsDef == False and outputsDef == True):
                print("inputsDef == False and outputsDef == True")
                inputAttrNames = Attributes.getAttributesExcept(outputAttrNames);
            elif (inputsDef == True and outputsDef == False):
                print("inputsDef == True and outputsDef == False")
                outputAttrNames = Attributes.getAttributesExcept(inputAttrNames);
                self.outputInfered = True;
            print("setOutputInputAttributes begin: ")
            Attributes.setOutputInputAttributes(inputAttrNames, outputAttrNames);


    # end of processInputsAndOutputs

    # '''
    #  * Test if the output attribute has been infered.
    #  * @return True if the output attribute has been infered. False if not.
    #  '''


    def isOutputInfered(self):
        return self.outputInfered;


    # '''
    #  * It returns the number of instances.
    #  * @return an int with the number of instances.
    # '''


    def getNumInstances(self):
        if (self.instanceSet != None):
            return len(self.instanceSet);
        else:
            return 0;
        # end numInstances


    # '''
    #  * Gets the instance located at the cursor position.
    #  * @return the instance located at the cursor position.
    # '''


    def getInstance(self, whichInstance):
        if (whichInstance < 0 or whichInstance >= self.instanceSet.length):
            return None
        return self.instanceSet[whichInstance];


    # end getInstance



        #  * It returns all the instances of the class.
        #  * @return Instance[] with all the instances of the class.

    def getInstances(self):
        return self.instanceSet;

    # //end getInstances
    # '''
    # '''
    #  * Returns the value of an integer or a real input attribute of an instance
    #  * in the instanceSet.
    #  * @param whichInst is the position of the instance.
    #  * @param whichAttr is the position of the input attribute.
    #  * @return a String with the numeric value.
    #  * @throws ArrayIndexOutOfBoundsException If the index is out of the instance
    #  * set size.
    # '''


    def getInputNumericValue(self, whichInst, whichAttr):
        if (whichInst < 0 or whichInst >= len(self.instanceSet)):
            raise IndexError(
                "You are trying to access to " + whichInst + " instance and there are only " + self.instanceSet.length + ".");
        return self.instanceSet[whichInst].getInputRealValues(whichAttr);


    # end getInputNumericValue


    # '''
    #  * Returns the value of an integer or a real output attribute of an instance
    #  * in the instanceSet.
    #  * @param whichInst is the position of the instance.
    #  * @param whichAttr is the position of the output attribute.
    #  * @return a String with the numeric value.
    #  * @throws ArrayIndexOutOfBoundsException If the index is out of the instance
    #  * set size.
    # '''


    def getOutputNumericValue(self,whichInst, whichAttr):
        if (whichInst < 0 or whichInst >= self.instanceSet.length):
            print(self.ArrayIndexOutOfBoundsException("You are trying to access to " + whichInst + " instance and there are only " + self.instanceSet.length + "."));
        return self.instanceSet[whichInst].getOutputRealValues(whichAttr);
        # end getOutputNumericValue

    #
    # '''
    #  * Returns the value of a nominal input attribute of an instance in the
    #  * instanceSet.
    #  * @param whichInst is the position of the instance.
    #  * @param whichAttr is the position of the input attribute.
    #  * @return a String with the nominal value.
    #  * @throws ArrayIndexOutOfBoundsException If the index is out of the instance
    #  * set size.
    # '''


    def getInputNominalValue(self,whichInst, whichAttr):
        if (whichInst < 0 or whichInst >= self.instanceSet.length):
            print(self.ArrayIndexOutOfBoundsException("You are trying to access to " + whichInst + " instance and there are only " + self.instanceSet.length + "."))
        # end getInputNominalValue

    #
    # '''
    #  * Returns the value of a nominal output attribute of an instance in the
    #  * instanceSet.
    #  * @param whichInst is the position of the instance.
    #  * @param whichAttr is the position of the output attribute.
    #  * @return a String with the nominal value.
    #  * @throws ArrayIndexOutOfBoundsException If the index is out of the instance
    #  * set size.
    # '''


    def getOutputNominalValue(self,whichInst, whichAttr):
        if (whichInst < 0 or whichInst >= self.instanceSet.length):
            print("You are trying to access to " + whichInst + " instance and there are only " + self.instanceSet.length + ".");
        return self.instanceSet[whichInst].getOutputNominalValues(whichAttr);
        # end getOutputNumericValue


    # '''
    #  * It does remove the instance i from the instanceSet.
    #  * @param instNum is the instance removed from the instanceSet.
    # '''


    def removeInstance(self, instNum):
        if (instNum < 0 or instNum >= self.instanceSet.length):
            return;
        aux = Instance[len(self.instanceSet) - 1];
        add = 0;
        for i in range(0, self.instanceSet.length):
            if (instNum == i):
                add = 1;
            else:
                aux[i - add] = self.instanceSet[i];

        # Copying the auxiliar to the instanceSet variable
        instanceSet = aux;
        aux = None;  # avoiding memory leaks (not necessary in this case)


    # end removeInstance


    # '''
    #  * It does remove an attribute. To remove an attribute, the train and the
    #  * test sets have to be passed to mantain the coherence of the system.
    #  * Otherwise, only the attribute of the train set would be removed, leaving
    #  * inconsistent the instances of the test set, because of having one extra
    #  * attribute inexistent anymore.
    #  *
    #  * @param tSet is the test set.
    #  * @param inputAtt is a boolean that is true when the attribute that is
    #  * wanted to be removed is an input attribute.
    #  * @param whichAtt is a integer that indicate the position of the attriubte
    #  * to be deleted.
    #  * @return a boolean indicating if the attribute has been deleted
    # '''


    def removeAttribute(self, tSet, inputAtt, whichAtt):
        attToDel = None;
        # Getting a reference to the attribute to del
        if (inputAtt == True):
            if (self.storeAttributesAsNonStatic and self.attributes != None):
                attToDel = self.attributes.getInputAttribute(whichAtt);
            else:
                attToDel = Attributes.getInputAttribute(whichAtt);

        else:
            if (self.storeAttributesAsNonStatic and self.attributes != None):
                attToDel = self.attributes.getOutputAttribute(whichAtt);
            else:
                attToDel = Attributes.getOutputAttribute(whichAtt);

        if (self.storeAttributesAsNonStatic == True and self.attributes != None):
            print("Removing the attribute");
        if (self.attributes.removeAttribute(inputAtt, whichAtt) == False or (
                tSet != None and tSet.attributes.removeAttribute(inputAtt, whichAtt)) == False):
            return False;
        else:
            if (Attributes.removeAttribute(inputAtt, whichAtt) == False):
                return False;
        for i in range(0, self.instanceSet.length):
            if (self.storeAttributesAsNonStatic and self.attributes != None):
                self.instanceSet[i].removeAttribute(self.attributes, attToDel, inputAtt, whichAtt);
            else:
                self.instanceSet[i].removeAttribute(attToDel, inputAtt, whichAtt);

        if (tSet != None):
            for i in range(0, tSet.instanceSet.length):

                if (self.storeAttributesAsNonStatic == True and self.attributes != None):
                    tSet.instanceSet[i].removeAttribute(self.attributes, attToDel, inputAtt, whichAtt);
            else:
                tSet.instanceSet[i].removeAttribute(attToDel, inputAtt, whichAtt);
            return True;


    # end removeAttribute

    # '''
    #  * It returns the header.
    #  * @return a String with the header of the file.
    # '''


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


    # '''
    #  * It does return a new header (not necessary the same header as the
    #  * input file one). It only includes the valid attributes, those ones
    #  * defined in @inputs and @outputs (or taken as that role following the
    #  * keel format specification).
    #  * @return a String with the new header
    # '''


    def getNewHeader(self):
        line = "";
        attrs = [];

        # Getting the relation name and the attributes
        if (self.storeAttributesAsNonStatic == True and self.attributes != None):
            line = "@relation " + self.attributes.getRelationName() + "\n";
            attrs = self.attributes.getInputAttributes();
        else:
            line = "@relation " + Attributes.getRelationName() + "\n";
            attrs = Attributes.getInputAttributes();

        for i in range(0, attrs.length):
            line += attrs[i].toString() + "\n";
            # Gettin all the outputs attributes
        if (self.storeAttributesAsNonStatic and self.attributes != None):
            attrs = self.attributes.getOutputAttributes();
            line += attrs[0].toString() + "\n";
            # Getting @inputs and @outputs
            line += self.attributes.getInputHeader() + "\n";
            line += self.attributes.getOutputHeader() + "\n";

        else:
            attrs = Attributes.getOutputAttributes();
            line += attrs[0].toString() + "\n";

        # Getting @inputs and @outputs
        line += Attributes.getInputHeader() + "\n";
        line += Attributes.getOutputHeader() + "\n";

        return line;


    # end getNewHeader


    # '''
    #  * It does return the original header definiton but
    #  * without @input and @output in there
    # '''


    def getOriginalHeaderWithoutInOut(self):
        line = "";
        attrs = [];

        # Getting the relation name and the attributes
        if (self.storeAttributesAsNonStatic and self.attributes != None):
            line = "@relation " + self.attributes.getRelationName() + "\n";
            attrs = self.attributes.getAttributes();

        else:
            line = "@relation " + Attributes.getRelationName() + "\n";
            attrs = Attributes.getAttributes();

        for i in range(0, attrs.length):
            line = line + attrs[i].toString() + "\n";
        return line;
        # end getOriginalHeaderWithoutInOut;


    # '''
    #  * It prints the dataset to the specified PrintWriter
    #  * @param out is the PrintWriter where to print
    # '''


    def print(self,out):
        for i in range(0, self.instanceSet.length):
            out.println("> Instance " + i + ":");
        if (self.storeAttributesAsNonStatic == True and self.attributes != None):
            self.instanceSet[i].print(self.attributes, out);
        else:
            self.instanceSet[i].print(out);


    # end print
    #
    # '''
    #  * It prints the dataset to the specified PrintWriter.
    #  * The order of the attributes is the same as in the
    #  * original file
    #  * @param out is the PrintWriter where to print
    #  * @param printInOut indicates if the @inputs (1), @outputs(2),
    #  * both of them (3) or any (0) has to be printed
    # '''


    def printAsOriginal(self,out, int):
        # Printing the header as the original one
        out.println(self.header);

        if (self.storeAttributesAsNonStatic and self.attributes != None):
            if (self.printInOut == 1 or self.printInOut == 3):
                out.println(self.attributes.getInputHeader());

        if (self.printInOut == 2 or self.printInOut == 3):

            out.println(self.attributes.getOutputHeader());

        else:
            if (self.printInOut == 1 or self.printInOut == 3):
                out.println(Attributes.getInputHeader());
            if (self.printInOut == 2 or self.printInOut == 3):
                out.println(Attributes.getOutputHeader());

        out.print("@data");
        for i in range(0, self.instanceSet.length):
            out.println();
            if (self.storeAttributesAsNonStatic and self.attributes != None):
                self.instanceSet[i].printAsOriginal(self.attributes, out);
        else:
            self.instanceSet[i].printAsOriginal(out);


    # end printAsOriginal


    def printHere(self):
        print("------------- ATTRIBUTES --------------");
        if (self.storeAttributesAsNonStatic and self.attributes != None):
            self.attributes.print();

        else:
            Attributes.print();

        print("-------------- INSTANCES --------------");
        for i in range(0, self.instanceSet.length):
            print("\n> Instance " + i + ":");

            if (self.storeAttributesAsNonStatic and self.attributes != None):
                self.instanceSet[i].print(self.attributes);
        else:
            self.instanceSet[i].print();


    # end print


    # Remove all instances from this InstanceSet

    def clearInstances(self):
        instanceSet = None;


    # '''
    #    * It adds the passed instance at the end of the present InstanceSet
    #    * @param inst the instance to be added
    # '''


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

    # '''
    #    * Clear the non-Static attributes. The static class Attributes is not modified.
    # '''


    def clearNonStaticAttributes(self):
        self.attributes = None;


    # '''
    #    * Appends the given attribute to the non-static list of the current InstanceSet
    #    * @param at The Attribute to be Appended
    # '''


    def addAttribute(self, att):
        if (self.attributes == None):
            attributes = InstanceAttributes();
        attributes.addAttribute(att);

    # end of InstanceSet Class.
