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
'''
from main import Fuzzy_Chi
from main import Fuzzy

'''
 * <p>This class contains the structure of a Fuzzy Rule</p>
 *
 * @author Written by Alberto Fern谩ndez (University of Granada) 29/10/2007
 * @version 1.0
 * @since JDK1.5
'''

def __init__():

  antecedent=[];
  clas=0;
  weight=0.0;
  compatibilityType=0;


  #Default constructor

'''
   * Constructor with parameters
   * @param n_variables int
   * @param compatibilityType int
'''
def __init__( self,n_variables,  compatibilityType):
    antecedent = Fuzzy[n_variables];
    self.compatibilityType = compatibilityType;

'''
   * It assigns the class of the rule
   * @param clas int
'''
def setClass(self, clas):
    self.clas = clas;

'''
 * It assigns the rule weight to the rule
 * @param train myDataset the training set
 * @param ruleWeight int the type of rule weight
'''
def assingConsequent( train, ruleWeight) :
  if (ruleWeight == Fuzzy_Chi.CF) :
    consequent_CF(train);

  elif (ruleWeight == Fuzzy_Chi.PCF_II):
    consequent_PCF2(train);

  elif (ruleWeight == Fuzzy_Chi.PCF_IV):
    consequent_PCF4(train);

  elif (ruleWeight == Fuzzy_Chi.NO_RW) :
    weight = 1.0;

'''
 * It computes the compatibility of the rule with an input example
 * @param example double[] The input example
 * @return double the degree of compatibility
'''
def compatibility(self,example):
  if (self.compatibilityType == Fuzzy_Chi.MINIMUM):
    return minimumCompatibility(example);

  else :
    return productCompatibility(example);

'''
 * Operator T-min
 * @param example double[] The input example
 * @return double the computation the the minimum T-norm
'''
def minimumCompatibility(self,example):
  minimum=0.0,
  membershipDegree=0.0;
  minimum = 1.0;
  for i in range(0, self.antecedent.length):
    membershipDegree = self.antecedent[i].Fuzzify(example[i]);
    minimum = min(membershipDegree, minimum);

  return (minimum);

'''
 * Operator T-product
 * @param example double[] The input example
 * @return double the computation the the product T-norm
'''
def productCompatibility(self, example):
  product=0.0,
  membershipDegree=0.0;
  product = 1.0;
  for i in range( 0, self.antecedent.length):
    membershipDegree = self.antecedent[i].Fuzzify(example[i]);
    product = product * membershipDegree;

  return (product);

'''
 * Classic Certainty Factor weight
 * @param train myDataset training dataset
'''
def consequent_CF( self,train):
  classes_sum = float [train.getnClasses()];
  for i in range( 0,train.getnClasses()):
     classes_sum[i] = 0.0;

  total = 0.0;
  comp = 0.0;
  #Computation of the sum by classes */
  for i in range( 0,train.size()):
    comp = self.compatibility(train.getExample(i));
    classes_sum[train.getOutputAsInteger(i)] += comp;
    total += comp;

  weight = classes_sum[self.clas] / total;


'''
 * Penalized Certainty Factor weight II (by Ishibuchi)
 * @param train myDataset training dataset
'''
def consequent_PCF2(self,train) :
  classes_sum = float [train.getnClasses()];
  for i in range (0, train.getnClasses()):
     classes_sum[i] = 0.0;


  total = 0.0;
  comp = 0.0;
# Computation of the sum by classes */
  for i in range (0,  train.size()):
    comp = self.compatibility(train.getExample(i));
    classes_sum[train.getOutputAsInteger(i)] += comp;
    total += comp;

    sum = (total - classes_sum[self.clas]) / (train.getnClasses() - 1.0);
    weight = (classes_sum[self.clas] - sum) / total;


'''
 * Penalized Certainty Factor weight IV (by Ishibuchi)
 * @param train myDataset training dataset
'''
def consequent_PCF4( self,train) :
  classes_sum = float [train.getnClasses()];
  for  i in range( 0, train.getnClasses()):
    classes_sum[i] = 0.0;

  total = 0.0;
  comp=0.0;
  # Computation of the sum by classes */
  for i in range( 0, train.size()):
    comp = self.compatibility(train.getExample(i));
    classes_sum[train.getOutputAsInteger(i)] += comp;
    total += comp;

  sum = total - classes_sum[self.clas];
  weight = (classes_sum[self.clas] - sum) / total;


'''
 * This function detects if one rule is already included in the Rule Set
 * @param r Rule Rule to compare
 * @return boolean true if the rule already exists, else false
'''
def comparison(self,rule) :
  contador = 0;
  for j in range (0, self.antecedent.length):
    if (self.antecedent[j].label == rule.antecedent[j].label) :
      contador+=1;

  if (contador == rule.antecedent.length):
    if (self.clas != rule.clas) : #Comparison of the rule weights
      if (self.weight < rule.weight) :
        #Rule Update
        self.clas = rule.clas;
        self.weight = rule.weight;

    return True;

  return False;







