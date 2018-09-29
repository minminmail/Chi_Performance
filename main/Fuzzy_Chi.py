"""
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
"""
from DataBase import DataBase
from MyDataSet import MyDataSet
from main import RuleBase

'''
 * <p>It contains the implementation of the Chi algorithm</p>
 *
 * @author Written by Alberto Fern谩ndez (University of Granada) 02/11/2007
 * @version 1.0
 * @since JDK1.5
'''
class Fuzzy_Chi :

      train=MyDataSet()
      val=MyDataSet()
      test=MyDataSet()
      outputTr=""
      outputTst=""
      fileDB=""
      fileRB=""
      nClasses=0
      nLabels=0
      combinationType=0
      inferenceType=0
      ruleWeight=0
      dataBase=DataBase()
      ruleBase=DataBase()

       # Configuration flags.

      MINIMUM = 0;
        # Configuration flags.

      PRODUCT = 1;
         #  Configuration flags.

      CF = 0;
        # Configuration flags.

      PCF_IV = 1;
         #  Configuration flags.

      MCF = 2;
         # Configuration flags.

      NO_RW = 3;
         # Configuration flags.

      PCF_II = 3;
         #  Configuration flags.
      WINNING_RULE = 0;
         #  Configuration flags.

      ADDITIVE_COMBINATION = 1;
       #We may declare here the algorithm's parameters

      somethingWrong = False; #to check if everything is correct.

     #  Default constructor

      """
           * It reads the data from the input files (training, validation and test) and parse all the parameters
           * from the parameters array.
           * @param parameters parseParameters It contains the input files, output files and parameters
      """
      def __init__(self,parameters):

            self.train = MyDataSet()
            self.val = MyDataSet()
            self.test = MyDataSet()
            try:
              print("Reading the training set: ")
              inputTrainingFiles= parameters.getInputTrainingFiles()
              for file in inputTrainingFiles:
                  print("File Name is :" + file);
              self.train.readClassificationSet(inputTrainingFiles, True)
            #   print("Reading the validation set: ")
            #                      # did not see any parameters.getValidationInputFile()
            #   #val.readClassificationSet(parameters.getValidationInputFile(), False);
            #   print("Reading the test set: ")
            #   for file in parameters.getInputTestFiles():
            #       print("File Name is :" + file);
            #
            #   self.test.readClassificationSet(parameters.getInputTestFiles(), False);
            except IOError as ioError :
                print ("I/O error: "+ str(ioError))
            except Exception as e:
                print("Unexpected error:" + str(e));
            # somethingWrong = True;
            #
            #     #We may check if there are some numerical attributes, because our algorithm may not handle them:
            #     #somethingWrong = somethingWrong || train.hasNumericalAttributes();
            # somethingWrong = somethingWrong or train.hasMissingAttributes();
            #
            # outputTr = parameters.getTrainingOutputFile();
            # outputTst = parameters.getTestOutputFile();
            #
            # fileDB = parameters.getOutputFile(0);
            # fileRB = parameters.getOutputFile(1);
            #
            #     #Now we parse the parameters
            # nLabels = int(parameters.getParameter(0));
            # aux = str(parameters.getParameter(1)).lower(); #Computation of the compatibility degree
            # combinationType = self.PRODUCT;
            # if (aux == "minimum"):
            #     combinationType = self.MINIMUM;
            #
            # aux = str(parameters.getParameter(2)).lower();
            # self.ruleWeight = self.PCF_IV;
            #
            # if (aux == "Certainty_Factor".lower()):
            #       self.ruleWeight = self.CF;
            #
            # elif (aux=="Average_Penalized_Certainty_Factor".lower()):
            #       self.ruleWeight = self.PCF_II;
            #
            # elif (aux=="No_Weights".lower()):
            #   self.ruleWeight = self.NO_RW;
            # aux = str(parameters.getParameter(3)).lower();
            # self.inferenceType = self.WINNING_RULE;
            # if(aux ==("Additive_Combination").lower()) :
            #     self.inferenceType = self.ADDITIVE_COMBINATION;

                #It launches the algorithm
      def execute(self) :
            if (self.somethingWrong==True) : #We do not execute the program
              print("An error was found, the data-set have missing values");
              print("Please remove those values before the execution");
              print("Aborting the program");
              #We should not use the statement: System.exit(-1);

            else :
              #We do here the algorithm's operations

              nClasses = self.train.getnClasses();

              dataBase = DataBase(self.train.getnInputs(), self.nLabels,
                                      self.train.getRanges(),self.train.getNames());
              ruleBase = RuleBase(dataBase, self.inferenceType, self.combinationType,self.ruleWeight, self.train.getNames(), self.train.getClasses());

              print("Data Base:\n"+dataBase.printString());
              ruleBase.Generation(self.train);

              dataBase.writeFile(self.fileDB);
              ruleBase.writeFile(self.fileRB);

              #Finally we should fill the training and test output files
              accTra = doOutput(self.val, self.outputTr);
              accTst = doOutput(self.test, self.outputTst);

              print("Accuracy obtained in training: "+accTra);
              print("Accuracy obtained in test: "+accTst);
              print("Algorithm Finished");

      """
         * It generates the output file from a given dataset and stores it in a file
         * @param dataset myDataset input dataset
         * @param filename String the name of the file
         *
         * @return The classification accuracy
      """
      def doOutput(self,dataset, filename) :
          output = "";
          hits = 0;
          output = dataset.copyHeader(); #we insert the header in the output file
          #We write the output for each example
          for i in range( 0, dataset.getnData()):
            #for classification:
            classOut = self.classificationOutput(dataset.getExample(i));
            output += dataset.getOutputAsString(i) + " " + classOut + "\n";
            if (dataset.getOutputAsString(i).equalsIgnoreCase(classOut)):
              hits+=1;

          file = open(filename,"w");
          file.write(output);
          file.close();
          return (1.0*hits/dataset.size());

      """
           * It returns the algorithm classification output given an input example
           * @param example double[] The input example
           * @return String the output generated by the algorithm
       """
      def classificationOutput(self,example):
            output = "?";
            '''
              Here we should include the algorithm directives to generate the
              classification output from the input example
           '''
            classOut = self.ruleBase.FRM(example);
            if (classOut >= 0):
              output = self.train.getOutputValue(classOut);

            return output;







