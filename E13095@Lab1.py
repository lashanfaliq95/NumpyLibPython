
import matplotlib.pyplot as plt
## TODO calculate local minima
import numpy as np
import csv
class Num:
	def __init__(self,matrix):
		self.matrix=matrix
		self.rowLen=matrix.shape[0]
		self.colLen=matrix.shape[1]
	def columnMean(self):
		mean_Mat= []
		for i in range(0,self.colLen):
			mean_Mat.append(np.mean(self.matrix[:,i:i+1]))
		return mean_Mat
	def newValue(self,meanMat):#getting the new matrix after substracting the mean of each column and squaring
		new_Mat=np.copy(self.matrix)
		for i in range(0,self.colLen):
			for j in range(0,self.rowLen):
				new_Mat[j][i]=(self.matrix[j][i]-meanMat[i])*(self.matrix[j][i]-meanMat[i])
		return new_Mat
	def finalMat(self,newMat):
		final_Mat=[]
		for i in range(0,self.colLen):
			num = np.sum(newMat[:,i:i+1])#getting the column matrix
			num = num/(self.rowLen-1) #getting the matrix after dividing by n-1 and getting the square root
			num = np.sqrt(num)
			final_Mat.append(num)
		return final_Mat


	
reader = csv.reader(open("labExercise01.csv","rb"),delimiter=",")
x = list(reader)
finalMatrix = np.array(x).astype("float")
 
num=Num(finalMatrix);
print num.finalMat(num.newValue(num.columnMean()))


reader = csv.reader(open("bonusExercise.csv","rb"),delimiter=",")
y= list(reader)
graph= np.array(y).astype("float")
#assuming the first column contains y indexes and sexond colmn contains x indexes
array=graph[:,:1]


for i in range(0,len(graph)):
	if i==0 or i==len(graph)-1:
		continue
	else:
		if array[i-1]<array[i] and array[i+1]>array[i]:
			local_minima=array[i]


print local_minima



