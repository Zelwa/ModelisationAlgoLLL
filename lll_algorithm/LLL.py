import math
from fractions import Fraction
from decimal import *

import numpy as np
from numpy.compat import long

from ModelisationCFG import ModelisationCFG

from parserData import parser, parser2


class LLL:
    def __init__(self,basis,param,base_log):
        self.basis = basis
        self.orthogonalize_basis = self.basis.copy()
        self.gram_schmidt()
        self.param =param
        self.mat= np.eye(len(self.basis[0]),len(self.basis[0])).astype('object')
        self.mat = self.mat.astype('object')
        self.alpha = [0]*(len(self.orthogonalize_basis)-1)
        self.ci_list = [0]*(len(self.orthogonalize_basis)-1)
        self.base_log = base_log
        self.listCiConstruction()
        self.modelisation = ModelisationCFG(self.ci_list)

    def dot(self,u,v) -> long:
        return  sum(map(lambda x: Fraction(x[0].numerator * x[1].numerator,x[0].denominator * x[1].denominator), zip(u,v)))

    def m(self,u,v):
        numerateur = self.dot(u, v)
        denominateur = self.dot(u, u)
        return numerateur / denominateur

    def projection(self,u,v) -> long:
        scale = self.m(u,v)
        return list(map(lambda x: scale * x,u))


    def gram_schmidt(self):
        size = self.basis.shape[1]
        self.orthogonalize_basis[0] = self.basis[0]
        for i in range(1, size):
            self.orthogonalize_basis[i] = self.basis[i]
            for j in range(0, i):
                self.orthogonalize_basis[i]  -= self.projection(self.orthogonalize_basis[j],self.basis[i])


    def matrix(self,i,j):
            m = self.dot(self.basis[i], self.orthogonalize_basis[j])
            y = self.dot(self.orthogonalize_basis[j],self.orthogonalize_basis[j])
            mat= m / y
            return mat


    def listCiConstruction(self):
        for i in range(len(self.orthogonalize_basis)-1):
            ri_numerator = self.dot(self.orthogonalize_basis[i+1],self.orthogonalize_basis[i+1])
            ri_denomanitor = self.dot(self.orthogonalize_basis[i],self.orthogonalize_basis[i])
            ri = (ri_denomanitor/ri_numerator)
            self.ci_list[ i ] = 0
            if(ri>0):
                self.ci_list[i] = math.log(ri,self.base_log)
            else:
                self.ci_list[i] = 0


    def constructionAlpha(self,index):
            self.alpha = -(1/2)*(math.log((self.base_log**(-2*self.ci_list[index]))+self.matrix(index+1,index)**2,self.base_log))

    def lll_algorithm(self):
        n = len(self.basis[ 0 ])
        self.gram_schmidt()
        k = 1
        while k <= n-1:
            for j in range(k - 1, -1, -1):
                if abs(self.matrix(k,j)) > 1 / 2:
                    self.basis[ k ] = self.basis[ k ] - round(self.matrix(k,j)) * self.basis[ j ]
                    self.gram_schmidt()
                    self.matrix(k,j)

            if self.dot(self.orthogonalize_basis[ k ], self.orthogonalize_basis[ k ]) >= (
                    Fraction(self.param) - self.matrix(k, k-1) ** 2) * self.dot(self.orthogonalize_basis[ k - 1 ],
                                                                         self.orthogonalize_basis[ k - 1 ]):
                k = k + 1
            else:
                self.listCiConstruction()
                self.constructionAlpha(k-1)
                self.modelisation.setCiList(self.ci_list)
                self.modelisation.update(k-1,self.alpha,True)
                print("list_ci : " , self.ci_list)
                self.basis[ [ k, k - 1 ] ] = self.basis[ [ k - 1, k ] ]
                self.gram_schmidt()
                print(k)
                k = max(k - 1, 1)
        self.listCiConstruction()
        self.modelisation.setCiList(self.ci_list)
        self.modelisation.update(k - 1, self.alpha, False)



def main():
    basis = parser("../exemples/ajtai.txt")
    #v1 = [ Fraction(1), Fraction(1), Fraction(1) ]
    #v2 = [ Fraction(-1), Fraction(0), Fraction(2) ]
    #v3 = [ Fraction(3), Fraction(5), Fraction(6) ]
    #basis = np.array([v1,v2,v3])
    print("Base avant reduction :\n ", basis)
    algo = LLL(basis, 0.75, 2/math.sqrt(3))
    algo.lll_algorithm()
    print("Base apres reduction :\n ", algo.basis)
    algo.modelisation.application.mainloop()




if __name__ == "__main__":
    main()


