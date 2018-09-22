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
from parseParameters import parseParameters
from main import Fuzzy_Chi
""" 
 * <p>It reads the configuration file (data-set files and parameters) and launch the algorithm</p>
 *
 * @author Written by Alberto Fern谩ndez (University of Granada) 14/10/2007
 * @version 1.0
 * @since JDK1.5
"""
class Main :

    __parameters=parseParameters();

    # Default Constructor
def __init__(self):
    """
        * It launches the algorithm
        * @param confFile String it is the filename of the configuration file.
  """
def execute(configfile):
       parameters = parseParameters();
       parameters.parseConfigurationFile(configfile);
       method = Fuzzy_Chi(parameters);
       method.execute();

""" 
        * Main Program
        * @param args It contains the name of the configuration file<br/>
        * Format:
        * algorithm = ;algorithm name>
        * inputData = "&lt;training file&gt;" "&lt;validation file&gt;" "&lt;test file&gt;"
        * utputData = "&lt;training file&gt;" "&lt;test file&gt;"
        * 
        * seed = value (if used)
        * &lt;Parameter1&gt; = &lt;value1&gt;
        * &lt;Parameter2&gt; = &lt;value2&gt;
   """
def main(args):
       program = Main();
       print("Executing Algorithm.");
       program.execute(args[0]);







