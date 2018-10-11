'''
This file is part of KEEL-software, the Data Mining tool for regression,
    classification, clustering, pattern mining and so on.
Copyright (C) 2004-2010,F. Herrera (herrera@decsai.ugr.es)
L.S谩nchez(luciano @ uniovi.es)
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
GNU General Public License for more details. You should have received a copy of the GNU General Public License
along with this program.  If not, see http://www.gnu.org/licenses/
'''


  # This class contains the representation of a Fuzzy Data Base</p>
  #
  # @author Written by Alberto Fern谩ndez (University of Granada) 28/10/2007
  # @author Modified by Alberto Fern谩ndez (University of Granada) 12/11/2008
  # @version 1.1
  # @since JDK1.5


from Fuzzy import Fuzzy
class DataBase :

    n_variables = 0
    n_labels = 0
    dataBase = []
    names = []
     # Default constructor
    def __init__(self):
        self.n_variables = 0
        self.n_labels = 0

          # Constructor with parameters. It performs a homegeneous partition of the input space for
          # a given number of fuzzy labels.
          # @param n_variables int Number of input variables of the problem
          # @param n_labels int Number of fuzzy labels
          # @param rangos double[][] Range of each variable (minimum and maximum values)
          # @param names String[] Labels for the input attributes

    def setMultipleParameters(self, n_variables, n_labels, rangos, names):
            self.n_variables = int(n_variables)
            self.n_labels = int(n_labels)
            print("self.n_variables: "+ str(self.n_variables)+" self.n_labels : "+str(self.n_labels))
            dataBase = [[Fuzzy() for x in range( self.n_variables)] for y in range (self.n_labels)]
            self.names = names

            marca=0.0

            for  i in range(0,self.n_variables):
                print("i= " + str(i))
                marca = (rangos[i][1] - rangos[i][0]) / ( int(n_labels) - 1)
                if (marca == 0) : #there are no ranges (an unique valor)
                    print("Marca =0 in DataBase init method...")

                    for etq in range(0,self.n_labels):
                        print("etq= " + str(etq))
                        dataBase[i][etq] =  Fuzzy()
                        dataBase[i][etq].x0 = rangos[i][1] - 0.00000000000001
                        dataBase[i][etq].x1 = rangos[i][1]
                        dataBase[i][etq].x3 = rangos[i][1] + 0.00000000000001
                        dataBase[i][etq].y = 1
                        dataBase[i][etq].name = "L_" + str(etq)
                        dataBase[i][etq].label = etq

                else:
                    print("Marca !=0 in DataBase init method...")
                    for etq in range(0, n_labels):
                        dataBase[i][etq] =  Fuzzy()
                        dataBase[i][etq].x0 = rangos[i][0] + marca * (etq - 1)
                        dataBase[i][etq].x1 = rangos[i][0] + marca * etq
                        dataBase[i][etq].x3 = rangos[i][0] + marca * (etq + 1)
                        dataBase[i][etq].y = 1
                        dataBase[i][etq].name = ("L_" + etq)
                        dataBase[i][etq].label = etq


    # '''
    #      * @return int the number of input variables
    # '''
    def numVariables(self):
     return self.n_variables

     # '''
     #     * @return int the number of fuzzy labels
     # '''
    def numLabels(self):
        return self.n_labels

    # '''
    #      * It computes the membership degree for a input value
    #      * @param i int the input variable id
    #      * @param j int the fuzzy label id
    #      * @param X double the input value
    #      * @return double the membership degree
    #      */
    # '''
    def  membershipFunction(self,i, j, X):
            return self.dataBase[i][j].Fuzzify(X)

    # '''
    #      * It makes a copy of a fuzzy label
    #      * @param i int the input variable id
    #      * @param j int the fuzzy label id
    #      * @return Fuzzy a copy of a fuzzy label
    # '''
    def clone(self,i, j) :
            return self.dataBase[i][j].clone()

    # '''
    #      * It prints the Data Base into an string
    #      * @return String the data base
    # '''
    def printString(self) :
            cadena = (
                    "@Using Triangular Membership Functions as antecedent fuzzy sets\n")
            cadena += "@Number of Labels per variable: " + str(self.n_labels) + "\n"
            for i in range(0,self.n_variables):

                cadena += "\n" + self.names[i] + ":\n"
                for j in range( 0,self.n_labels):
                    cadena += " L_" + str(int(j + 1)) + ": (" + self.dataBase[i][j].x0 +  "," + self.dataBase[i][j].x1 + "," + self.dataBase[i][j].x3 + ")\n"

            return cadena

    # '''
    #      * It writes the Data Base into an output file
    #      * @param filename String the name of the output file
    # '''
    def writeFile(filename):

            file=open(filename, "w")
            outputString = printString()
            file.write(outputString)
            file.close()