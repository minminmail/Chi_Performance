# '''
#  * <p>It contains the methods to read a Classification/Regression Dataset</p>
#  *
#  * @author Written by Alberto Fern谩ndez (University of Granada) 15/10/2007
#  * @author Modified by Alberto Fern谩ndez (University of Granada) 12/11/2008
#  * @version 1.1
#  * @since JDK1.5
# '''
from InstanceSet import InstanceSet
from main import Attributes
import math
import sys
class MyDataSet:
    # Number to represent type of variable real or double.
    REAL = 0;
    #*Number to represent type of variable integer.*
    INTEGER = 1;
    #*Number to represent type of variable nominal.*
    NOMINAL = 2;

    __X=[]; # examples array
    __missing = []; # possible missing values
    __outputInteger = []; #  output of the data - set as integer values private
    __outputReal = []; # output of the data - set as double values
    __output = [];# output of the data - set as string values
    __emax=[]; #  max value of an attribute private
    __emin=[]; #  min value of an attribute

    __nData=0; #  Number of examples
    __nVars=0; #  Numer of variables
    __nInputs=0; #  Number of inputs
    __nClasses=0; #  Number of outputs

    __instanceSet=InstanceSet(); #  The whole instance set
    __stdev=[],
    __average=[]; #  standard deviation and average of each attribute
    __instancesCl=[];
    #  *Init a new set of instances

    def __init__(self):
        self.__instanceSet = InstanceSet();

    # '''
    #    * Outputs an array of examples with their corresponding attribute values.
    #    * @return double[][] an array of examples with their corresponding attribute values
    #  '''
    def getX(self):
        return self.X;
    # '''
    #    * Output a specific example
    #    * @param pos int position (id) of the example in the data-set
    #    * @return double[] the attributes of the given example
    # '''
    def getExample(self,pos):
         return self.X[pos];

    '''
       * Returns the output of the data-set as integer values
       * @return int[] an array of integer values corresponding to the output values of the dataset
    '''
    def getOutputAsInteger(self):
        size=self.outputInteger.length,
        output = int[size];
        for i in range( 0, size):
             output[i] = self.outputInteger[i];
        return output;

    # '''
    #    * Returns the output of the data-set as real values
    #    * @return double[] an array of real values corresponding to the output values of the dataset
    # '''
    def getOutputAsReal(self):
        output = float[self.outputReal.length];
        for i in range( 0,self.outputReal.length):
          output[i] = self.outputInteger[i];
        return output;
    # '''
    #    * Returns the output of the data-set as nominal values
    #    * @return String[] an array of nomianl values corresponding to the output values of the dataset
    #
    # '''
    def getOutputAsString(self):
        output = str[self.output.length];
        for  i in range ( 0, self.output.length):
          output[i] = self.output[i];

        return output;
    #
    # '''
    #    * It returns the output value of the example "pos"
    #    * @param pos int the position (id) of the example
    #    * @return String a string containing the output value
    #
    # '''
    def getOutputAsString(self,pos):
        return self.output[pos];

    # '''
    #    * It returns the output value of the example "pos"
    #    * @param pos int the position (id) of the example
    #    * @return int an integer containing the output value

    def getOutputAsInteger(self,pos):
     return self.outputInteger[pos];

    # '''
    #    * It returns the output value of the example "pos"
    #    * @param pos int the position (id) of the example
    #    * @return double a real containing the output value
    # '''
    def getOutputAsReal(self,pos):
     return self.outputReal[pos];

     # '''
     # *It returns an array with the maximum values of the attributes
     # * @ return double[] an array with the maximum values of the attributes
     #
     # '''
    def getemax(self):
     return self.emax;
     #
     # '''
     # *It returns an array with the minimum values of the attributes
     # * @ return double[] an array with the minimum values of the attributes
     # '''
    def getemin(self):
     return self.emin;


    # '''
    # *It returns the maximum value of the given attribute
    # *
    # * @ param variable the index of the attribute
    # * @ return the maximum value of the given attribute
    # '''
    def getMax(self, variable):
     return self.emax[self.variable];


    # '''
    # *It returns the minimum value of the given attribute
    #
    # * @ param variable the index of the attribute
    # * @ return the minimum value of the given attribute
    # * /
    #
    # '''
    def getMin(self,variable):
     return self.emin[variable];

    # '''
    # *It gets the size of the data - set
    # * @ return int the number of examples in the data - set
    # '''
    def getnData(self):

     return self.nData;

    # '''
    # *It gets the number of variables of the data - set(including the output)
    # * @ return int the number of variables of the data - set(including the output)
    # '''
    def getnVars(self):
     return self.__nVars;

    # '''
    #    * It gets the number of input attributes of the data-set
    #    * @return int the number of input attributes of the data-set
    # '''
    def getnInputs(self):
     return self.__nInputs;

    #  '''
    #    * It gets the number of output attributes of the data-set (for example number of classes in classification)
    #    * @return int the number of different output values of the data-set
    # '''
    def getnClasses(self):
        return self.__nClasses;

    #
    # '''
    #  * This function checks if the attribute value is missing
    #  * @param i int Example id
    #  * @param j int Variable id
    #  * @return boolean True is the value is missing, else it returns false
    # '''
    def isMissing(self, i, j):
      return self.missing[i][j];


    # '''
    #  * It reads the whole input data-set and it stores each example and its associated output value in
    #  * local arrays to ease their use.
    #  * @param datasetFile String name of the file containing the dataset
    #  * @param train boolean It must have the value "true" if we are reading the training data-set
    #  * @throws IOException If there ocurs any problem with the reading of the data-set
    # '''
    def readClassificationSet( self,datasetFile,train) :
     try :
          # Load in memory a dataset that contains a classification problem
          print("Inside readClassificationSet, datasetFile :"+ str(datasetFile))
          print("train is :" + str(train))
          print("object instanceSet is :"+ str(self.__instanceSet))
          if(self.__instanceSet is None):
              print("self.__instanceSet is Null")
          else :
              print("self.__instanceSet is not None")
              self.__instanceSet.readSet(datasetFile, train)
     #      nData = self.__instanceSet.getNumInstances();
     #      nInputs = Attributes.getInputNumAttributes();
     #      nVars = nInputs + Attributes.getOutputNumAttributes();
     #
     #      # outputIntegerheck that there is only one output variable
     #      if (Attributes.getOutputNumAttributes() > 1) :
     #        print("This algorithm can not process MIMO datasets");
     #        print("All outputs but the first one will be removed");
     #        exit(1);
     #      noOutputs = False;
     #      if (Attributes.getOutputNumAttributes() < 1) :
     #        print("This algorithm can not process datasets without outputs");
     #        print("Zero-valued output generated");
     #        noOutputs = True;
     #        exit(1);
     #
     #      #Initialice and fill our own tables
     #      self.X = [nData][nInputs];
     #      missing = [nData][nInputs];
     #      outputInteger = [nData];
     #      outputReal = [nData];
     #      output =[nData];
     #
     #       # Maximum and minimum of inputs
     #      self.emax =[nInputs];
     #      self.emin = [nInputs];
     #      for n in range( 0,nInputs):
     #         self.emax[n] = Attributes.getAttribute(n).getMaxAttribute();
     #         self.emin[n] = Attributes.getAttribute(n).getMinAttribute();
     #        # All values are casted into double/integer
     #      nClasses = 0;
     #      for i in range( 0, nData) :
     #            inst = self.IS.getInstance(i);
     #            for j in range( 0, nInputs):
     #                  self.X[i][j] = self.IS.getInputNumericValue(i, j); #inst.getInputRealValues(j);
     #                  missing[i][j] = inst.getInputMissingValues(j);
     #                  if (missing[i][j]==True):
     #                    self.X[i][j] = self.emin[j] - 1;
     #
     #            if (noOutputs==True):
     #                     outputInteger[i] = 0;
     #                     output[i] = "";
     #            else:
     #                    outputInteger[i] = self.IS.getOutputNumericValue(i, 0);
     #                    output[i] = self.IS.getOutputNominalValue(i, 0);
     #
     #            if(outputInteger[i] > nClasses):
     #                    nClasses = outputInteger[i];
     #
     #      nClasses+=1;
     #      print('Number of classes=' + nClasses);
     except Exception as error:
           print("DBG: Exception in readSet, in readClassificationSet");
     #
     # self.computeStatistics();
     # self.computeInstancesPerClass();

     # """
     #   * It reads the whole input data-set and it stores each example and its associated output value in
     #   * local arrays to ease their use.
     #   * @param datasetFile String name of the file containing the dataset
     #   * @param train boolean It must have the value "true" if we are reading the training data-set
     #   * @throws IOException If there ocurs any problem with the reading of the data-set
     # """
    def readRegressionSet(self,datasetFile, train) :

        try :
          #Load in memory a dataset that contains a regression problem
          self.IS.readSet(datasetFile, train);
          nData = self.IS.getNumInstances();
          nInputs = Attributes.getInputNumAttributes();
          nVars = nInputs + Attributes.getOutputNumAttributes();

          #outputIntegerheck that there is only one output variable
          if (Attributes.getOutputNumAttributes() > 1):
            print("This algorithm can not process MIMO datasets");
            print("All outputs but the first one will be removed");
            exit(1);

          noOutputs = False;
          if (Attributes.getOutputNumAttributes() < 1):
            print("This algorithm can not process datasets without outputs");
            print("Zero-valued output generated");
            noOutputs = True;
            exit(1);
          # Initialice and fill our own tables
          self.X =[self.Data][nInputs];
          self.missing [nData][nInputs];
          outputInteger = int[self.nData];

          # Maximum and minimum of inputs
          emax = [nInputs];
          emin = [nInputs];
          for i in range( 0,nInputs):
             emax[i] = Attributes.getAttribute(i).getMaxAttribute();
             emin[i] = Attributes.getAttribute(i).getMinAttribute();

            # All values are casted into double / integer
          nClasses = 0;

          for i in range (0,self.nData):
                inst = self.IS.getInstance(i);
                for j in range( 0, nInputs):
                  self.X[i][j] = self.IS.getInputNumericValue(i, j); #inst.getInputRealValues(j);
                  self.missing[i][j] = inst.getInputMissingValues(j);
                  if (self.missing[i][j]):
                    self.X[i][j] = emin[j] - 1;

                if (noOutputs):
                  self.outputReal[i] = outputInteger[i] = 0;

                else :
                  self.outputReal[i] = self.IS.getOutputNumericValue(i, 0);
                  self.outputInteger[i] = self.outputReal[i];
        except OSError  as error:
         print("OS error: {0}".format(error))
        except:
         print("DBG: Exception in readSet:", sys.exc_info()[0])

        self.computeStatistics();
    #
    # '''
    # *It copies the header of the dataset
    # * @ return String A string containing all the data - set information
    # '''
    def copyHeader():

        p = "";
        p = "@relation " + Attributes.getRelationName() + "\n";
        p += Attributes.getInputAttributesHeader();
        p += Attributes.getOutputAttributesHeader();
        p += Attributes.getInputHeader() + "\n";
        p += Attributes.getOutputHeader() + "\n";
        p += "@data\n";
        return p;

    # '''
    #    * It transform the input space into the [0,1] range
    # '''
    def normalize(self):
        atts = self.getnInputs();
        maxs= [atts];
        for j in range( 0,atts):
          maxs[j] = 1.0 / (self.emax[j] - self.emin[j]);

        for i in range(0,self.getnData()):
          for j in range(0,atts):
            if (self.isMissing(i, j)==False):#this process ignores missing values
              self.X[i][j] = (self.X[i][j] - self.emin[j]) * maxs[j];

    # '''
    #    * It checks if the data-set has any real value
    #    * @return boolean True if it has some real values, else false.
    # '''
    def hasNumericalAttributes():
        return (Attributes.hasIntegerAttributes() or Attributes.hasRealAttributes());

    # '''
    #    * It checks if the data-set has any missing value
    #    * @return boolean True if it has some missing values, else false.
    # '''
    def hasMissingAttributes(self):
        return (self.sizeWithoutMissing() < self.getnData());


    # '''
    #    * It return the size of the data-set without having account the missing values
    #    * @return int the size of the data-set without having account the missing values
    # '''

    def sizeWithoutMissing(self):

        tam = 0;
        for i in range( 0, self.nData):

            for j in range(1 ,self.nInputs):
               # changed the isMissing condition inside if
                  if (self.isMissing(i, j)==True) and (j == self.nInputs) :
                     tam+=1;

        return tam;
    # '''
    #    * It returns the number of examples
    #    *
    #    * @return the number of examples
    # '''
    def size(self):
        return self.nData;

    # '''
    #    * It computes the average and standard deviation of the input attributes
    # '''
    def  computeStatistics(self):
        stdev = float(self.getnVars()); # original was double ,changed into float in python
        average = float(self.getnVars());

        for i in range ( 0,self.getnInputs()):
          average[i] = 0;
          for j in range (0, self.getnData()):
            if (self.isMissing(j, i)==False):
              average[i] += self.X[j][i];


          average[i] /= self.getnData();

        average[len(average) - 1] = 0;
        for j in range( 0, self.outputReal.length):
          average[average.length - 1] += self.outputReal[j];

        average[average.length - 1] /= self.outputReal.length;

        for i in range( 0, self.getnInputs()):
          sum = 0;
          for j in range (0, self.getnData()):
            if (self.isMissing(j, i)==False):
              sum += (self.X[j][i] - average[i]) * (self.X[j][i] - average[i]);

          sum /= self.getnData();
          stdev[i] = math.sqrt(sum);

        sum = 0;
        for j in range(0, self.outputReal.length):
          sum += (self.outputReal[j] - average[average.length - 1]) *(self.outputReal[j] - average[average.length - 1]);

        sum /= self.outputReal.length;
        stdev[stdev.length - 1] = math.sqrt(sum);
    # '''
    #    * It return the standard deviation of an specific attribute
    #    * @param position int attribute id (position of the attribute)
    #    * @return double the standard deviation  of the attribute
    # '''
    def stdDev(self,position):
        return self.stdev[position];

    # '''
    #    * It return the average of an specific attribute
    #    * @param position int attribute id (position of the attribute)
    #    * @return double the average of the attribute
    # '''

    def average( position):
        return average[position];

    # '''
    #     *It computes the number of examples per class
    # '''

    def computeInstancesPerClass(self):
        instancesCl =  int[self.nClasses];
        for i in range( 0,self.getnData()):
         instancesCl[self.outputInteger[i]]+=1;


    # '''
    #     *It returns the number of examples for a given class
    #     * @ param clas int the class label id
    #     * @ return int the number of examples
    #     for the class
    #     * /
    #  '''
    def numberInstances(self,clas):
        return self.instancesCl[clas];

      #   '''
      # /**
      #  * It returns the number of labels for a nominal attribute
      #  * @param attribute int the attribute position in the data-set
      #  * @return int the number of labels for the attribute
      #  */
      #
      #     '''
    def numberValues(self,attribute):
        return Attributes.getInputAttribute(attribute).getNumNominalValues();

    # '''
    #    * It returns the class label (string) given a class id (int)
    #    * @param intValue int the class id
    #    * @return String the corrresponding class label
    #
    # '''
    # '''
    #    * It returns the class label (string) given a class id (int)
    #    * @param intValue int the class id
    #    * @return String the corrresponding class label
    # '''
    def getOutputValue( intValue) :
        return Attributes.getOutputAttribute(0).getNominalValue(intValue);

    # '''
    #  * It returns the type of the variable
    #  * @param variable int the variable id
    #  * @return int a code for the type of the variable (INTEGER, REAL or NOMINAL)
    # '''

    def getType( self,variable) :
        if (Attributes.getAttribute(variable).getType() == Attributes.getAttribute(0).INTEGER):
          return self.INTEGER;

        if (Attributes.getAttribute(variable).getType() == Attributes.getAttribute(0).REAL):
          return self.REAL;

        if (Attributes.getAttribute(variable).getType() == Attributes.getAttribute(0).NOMINAL):
          return self.NOMINAL;

        return 0;


    # '''
    #  * It returns the discourse universe for the input and output variables
    #  * @return double[][] The minimum [0] and maximum [1] range of each variable
    # '''
    def getRanges(self):
      rangos =  float[self.getnVars()][2];
      for i in range( 0, self.getnInputs()):
        if (Attributes.getInputAttribute(i).getNumNominalValues() > 0):
          rangos[i][0] = 0;
          rangos[i][1] = Attributes.getInputAttribute(i).getNumNominalValues() -1;

        else:
          rangos[i][0] = Attributes.getInputAttribute(i).getMinAttribute();
          rangos[i][1] = Attributes.getInputAttribute(i).getMaxAttribute();


      rangos[self.getnVars() -1][0] = Attributes.getOutputAttribute(0).getMinAttribute();
      rangos[self.getnVars() -1][1] = Attributes.getOutputAttribute(0).getMaxAttribute();
      return rangos;

    # '''
    #    * It returns the attribute labels for the input features
    #    * @return String[] the attribute labels for the input features
    # '''
    def getNames(self):
       nombres = ["" for x in range(self.nInputs)];
       for i in range ( 0, self.nInputs):
          nombres[i] = Attributes.getInputAttribute(i).getName();
       return nombres;
    #
    # '''
    #    * It returns the class labels
    #    * @return String[] the class labels
    # '''
    def getClasses(self):
        clases = ["" for x in range(self.nClasses)]

        for i in range( 0, self.nClasses):
          clases[i] = Attributes.getOutputAttribute(0).getNominalValue(i);
        return clases;

