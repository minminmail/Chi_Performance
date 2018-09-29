#
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
#  * Parser.java
#  *
#  * Created on 24 de enero de 2005, 10:43
#  */

# /**
#  * <p>
#  * <b> InstanceParser </b>
#  * </p>
#  * This class is a parser for the instances. It reads an instance (a line
#  * from the data file) and returns it. It also mantain some information as
#  * the relation name.
#  *
#  * @author  Albert Orriols Puig
#  * @version keel0.1
#  *
#  */

class InstanceParser:

   # /////////////////////////////////////////////////////////////////////////////
   # ////////////////// ATTRIBUTES OF THE PARSER CLASS ///////////////////////////
   # /////////////////////////////////////////////////////////////////////////////
   #
   # /**
   #  * A Buffered Reader to the DB input file.
   #  */
   #   private BufferedReader br;
   #
   # /**
   #  * A flag indicating if the DB is a train or a test DB. The difference between
   #  * them is that a test DB doesn't modify any parameter definition.
   #  */

    __isTrain = None;
    # It counts the attribute number.
    __attributeCount = 0;
    # String where de file header is stored
    __header = "";
    # String where the relation name is stored
    __relation = "";
    # Counter of the line
    lineCounter = 0;

    # /////////////////////////////////////////////////////////////////////////////
    # /////////////////// METHODS OF THE PARSER CLASS /////////////////////////////
    # /////////////////////////////////////////////////////////////////////////////
    # /**
    #  * It does create a new instance of ParserARFF.
    #  * @param fileName is the file name of the DB file.
    #  * @param _isTrain is a flag that indicates if the DB is for a train.
    #  */
    #

    def __init__(self,fileName, _isTrain):
        try:
            file = open(fileName, "r");
            br = file.read();
            lineCounter = 0;
        except Exception as error:
            print("The exceptoin is " + format(error))
            exit(1);

        self.__isTrain = _isTrain;
        self.__attributeCount = 0

    # end of Parser constructor

    #  * It returns all the header read in parseHeader.
    #  * @return a string with the header information.

    def getHeader(self):
        return self.__header

    # end getHeader

    #  * It returns the relation name
    #  * @return a string with the relation name.

    def getRelation(self):
        return self.__relation

    # end getRelation
    #

    #  * It returns an instance
    #  * @return an string with the instance.

    def getInstance(self):
        return self.getLine();

    # end getInstance
     # * It returns the number of attributes
     # * @return an integer with the number of attributes.
    def getAttributeNum(self):
        return self.__attributeCount

     # * This method reads one valid line of the file. So, it ingores the comments,
     # * and empty lines.
     # * @return a string with the new line read.

    def getLine(self):
        st = None;
        while True:
            try:
                st = self.br.readLine();
                self.lineCounter += 1;
            except Exception as error:
                print("Exception is " + format(error));
                exit(1);

            if (st != None and (st.startsWith("%") or st.equals(""))):
                break;
        return st;

    # end getLine

    # This method closes the buffered reader used to parse the instances

    def close(self):
        try:
            self.br.close();
        except IOError as ioError:
            print("Error: the instance parser could not be closed. Exiting now." + format(ioError));
            exit(-1);

    # end of Parser class
