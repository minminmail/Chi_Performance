
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

import Fuzzy_Chi
from Fuzzy import Fuzzy


 # * <p>This class contains the structure of a Fuzzy Rule</p>
 # *
 # * @author Written by Alberto Fern谩ndez (University of Granada) 29/10/2007
 # * @version 1.0
 # * @since JDK1.5

class Rule:

  antecedent=None
  clas=None
  weight=None
  compatibilityType=None

  def __init__(self):
    print("__init__ of Rule")

  #Default constructor

     # * Constructor with parameters
     # * @param n_variables int
     # * @param compatibilityType int

  def setTwoParameters( self,n_variables,  compatibilityType):
    print("In rule calss , setTwoParameters method, the n_variables = "+str(n_variables))
    self.antecedent = [Fuzzy() for x in range(n_variables)]
    self.compatibilityType = compatibilityType

     # * It assigns the class of the rule
     # * @param clas int

  def setClass(self, clas):
    self.clas = clas

   # * It assigns the rule weight to the rule
   # * @param train myDataset the training set
   # * @param ruleWeight int the type of rule weight

  def assingConsequent(self,train, ruleWeight) :
    if ruleWeight == Fuzzy_Chi.Fuzzy_Chi.CF:
      self.consequent_CF(train)

    elif ruleWeight == Fuzzy_Chi.Fuzzy_Chi.PCF_II:
      self.consequent_PCF2(train)

    elif ruleWeight == Fuzzy_Chi.Fuzzy_Chi.PCF_IV:
      self.consequent_PCF4(train)

    elif ruleWeight == Fuzzy_Chi.Fuzzy_Chi.NO_RW:
      self.weight = 1.0

   # * It computes the compatibility of the rule with an input example
   # * @param example double[] The input example
   # * @return double the degree of compatibility

  def compatibility(self,example):
    if (self.compatibilityType == Fuzzy_Chi.Fuzzy_Chi.MINIMUM):
      #print("self.compatibilityType == Fuzzy_Chi.Fuzzy_Chi.MINIMUM")
      return self.minimumCompatibility(example)

    else :
      #print("self.compatibilityType != Fuzzy_Chi.Fuzzy_Chi.MINIMUM"+", self.compatibilityType = "+ str(self.compatibilityType))
      return self.productCompatibility(example)


   # * Operator T-min
   # * @param example double[] The input example
   # * @return double the computation the the minimum T-norm

  def minimumCompatibility(self,example):
    minimum=None
    membershipDegree=None
    minimum = 1.0
    for i in range(0, len(self.antecedent)):
      print("example["+str(i)+"] = "+example[i])
      membershipDegree = self.antecedent[i].setX(example[i])
      print("membershipDegree in minimumCompatibility = " + str(membershipDegree))
      minimum = min(membershipDegree, minimum)

    return minimum

   # * Operator T-product
   # * @param example double[] The input example
   # * @return double the computation the the product T-norm

  def productCompatibility(self, example):

    product = 1.0
    antecedent_number=len(self.antecedent)
    #print("antecedent_number = " + str(antecedent_number))
    for i in range( 0, antecedent_number):
      #print("example[i="+ str(i)+"]"+":"+ str(example[i]))
      membershipDegree = self.antecedent[i].setX(example[i])
      #print("membershipDegree in productCompatibility  = " +str(membershipDegree))
      product = product * membershipDegree
    #print("product: "+ str(product))
    return product


   # * Classic Certainty Factor weight
   # * @param train myDataset training dataset

  def consequent_CF( self,train):
    train_Class_Number = train.getnClasses()
    classes_sum = [0.0 for x in range(train_Class_Number)]
    for i in range( 0,train.getnClasses()):
       classes_sum[i] = 0.0

    total = 0.0
    comp = None
    #Computation of the sum by classes */
    for i in range( 0,train.size()):
      comp = self.compatibility(train.getExample(i))
      classes_sum[train.getOutputAsIntegerWithPos(i)] = classes_sum[train.getOutputAsIntegerWithPos(i)]+ comp
      total =total+ comp

    print("classes_sum[self.clas]  = " + str(classes_sum[self.clas] ) +"total" +str(total))
    self.weight = classes_sum[self.clas] / total

   # * Penalized Certainty Factor weight II (by Ishibuchi)
   # * @param train myDataset training dataset

  def consequent_PCF2(self,train) :
    classes_sum = float[train.getnClasses()]
    for i in range (0, train.getnClasses()):
       classes_sum[i] = 0.0

    total = 0.0
    comp = None
  # Computation of the sum by classes */
    for i in range (0,  train.size()):
      comp = self.compatibility(train.getExample(i))
      classes_sum[train.getOutputAsIntegerWithPos(i)] = classes_sum[train.getOutputAsIntegerWithPos(i)]+comp
      total = total+comp

    sum = (total - classes_sum[self.clas]) / (train.getnClasses() - 1.0)
    self.weight = (classes_sum[self.clas] - sum) / total

   # * Penalized Certainty Factor weight IV (by Ishibuchi)
   # * @param train myDataset training dataset

  def consequent_PCF4( self,train) :
    classes_sum =  [0.0 for x in range(train.getnClasses())]
    for  i in range( 0, train.getnClasses()):
      classes_sum[i] = 0.0

    total = 0.0
    comp= None

    train_size=train.size()
    print("train_size: " + str(train_size))
    # Computation of the sum by classes */
    for i in range( 0, train_size):
      comp = self.compatibility(train.getExample(i))
      print("comp = " + str(comp))
      classes_sum[train.getOutputAsIntegerWithPos(i)] = classes_sum[train.getOutputAsIntegerWithPos(i)]+ comp
      total = total+ comp

    print("self.clas ="+ str(self.clas)+"classes_sum[self.clas] :" + str(classes_sum[self.clas]))
    sum = total - classes_sum[self.clas]
    self.weight = (classes_sum[self.clas] - sum) / total

   # * This function detects if one rule is already included in the Rule Set
   # * @param r Rule Rule to compare
   # * @return boolean true if the rule already exists, else false

  def comparison(self,rule) :
    contador = 0
    for j in range (0, len(self.antecedent)):
      if (self.antecedent[j].label == rule.antecedent[j].label) :
        contador= contador + 1

    if (contador == len(rule.antecedent)):
      if (self.clas != rule.clas) : #Comparison of the rule weights
        if (self.weight < rule.weight) :
          #Rule Update
          self.clas = rule.clas
          self.weight = rule.weight

      return True
    else:
      return False







