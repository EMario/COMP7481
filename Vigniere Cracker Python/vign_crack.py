#!/usr/bin/env python

######################################
##
##	Mario Enriquez	A00909441
##
##	COMP 7481	Carly Orr
##
##	Vigenere Cracker
##
######################################

import os
import re

class WordRepeat:
	#Class to save the Repeated Words
	word = ""
	pos = 0
	rep = 0
	dist = []

	def __init__(self,word,pos,rep,dist):
		self.word = word
		self.pos = pos
		self.rep = rep
		self.dist = dist

	def getWord(self):
		return self.word

	def getPosition(self):
		return self.pos

	def getDistance(self):
		return self.dist
	
def table():
	#Vigenere table generator
	i = 0
	j= "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	while (i<26):
		array.append(j[i:] + j[:i])
		i+=1
	return array

def vigniere_enc(filename):
	#encrypts a vigenere file
	with open(filename,"r") as enc_file:
		lines = enc_file.readlines()
	enc_file.close()
	enc=open("/root/Documents/enc.txt","w")
	x = 0
	for i in lines:
		for j in i:
			res = ord(j)
			encrypt=0
			if(res>=65 and res<=90):
				res=res-65
				encrypt=1
			if(res>=97 and res<=122):
				res=res-97
				encrypt=1
			if(encrypt==1):			
				line = vign[res]
				c = line[keyword[x]] 
				x=x+1
				if(x==len(keyword)):
					x=0
				enc.write(c)
			else:
				enc.write(j)
	enc.close()

def vigniere_dec():
	#decrypts a vigenere file
	with open("/root/Documents/enc.txt","r") as dec_file:
		lines = dec_file.readlines()
	dec_file.close()
	dec=open("/root/Documents/dec.txt","w")
	x = 0
	for i in lines:
		for j in i:
			res = ord(j)
			decrypt=0
			if(res>=65 and res<=90):
				decrypt=1
			if(res>=97 and res<=122):
				res=res-32
				decrypt=1
			if(decrypt==1):			
				line = vign[keyword[x]]
				cont=0				
				while line[cont]!=chr(res):
					cont=cont+1
				c = chr(cont+65)
				x=x+1
				if(x==len(keyword)):
					x=0
				dec.write(c)
			else:
				dec.write(j)
	dec.close()

def dec(word,key):
	#reverse decoding to obtain keyword
	x=0
	y=""
	k=[]
	j=0
	c=""
	for i in key:
		k.append(ord(i))
		if(k[j]>=65 and k[j]<=90):
			k[j]=k[j]-65
		if(k[j]>=97 and k[j]<=122):
			k[j]=k[j]-97
		j=j+1
	for z in word:
		y = vign[k[x]]
		cont=0				
		while y[cont]!=z:
			cont=cont+1
		c = c + chr(cont+65)		
		x=x+1
		if(x==len(key)):
			x=0
	print "Key: ",c

def analyze(repeat,length,dec_word):
	#document analysis to get keyword
	with open("/root/Documents/enc.txt","r") as dec_file:
		lines = dec_file.readlines()
	dec_file.close()
	doc=''.join(lines)
	#''.join(x for x in doc if x.isalpha())
	newdoc=re.sub(r'\W+','',doc)
	print "Document: ",newdoc
	wordlist=[]
	checked=[]
	distance=[]
	for y in range(0,len(newdoc)-3):
		if not newdoc[y:y+3] in checked:
			for x in range(y+3,len(newdoc)-3):
				if (newdoc[y:y+3]==newdoc[x:x+3]):
					distance.append(x-y)
			if distance:
				wordlist.append(WordRepeat(newdoc[y:y+3],y,len(distance)+1,distance))
			distance=[]
			checked.append(newdoc[y:y+3])
	for i in wordlist:
		if(len(WordRepeat.getDistance(i))>int(repeat)):
			print "Sequence:",WordRepeat.getWord(i)
			print "Position of Document:",WordRepeat.getPosition(i)
			print "Repetitions found at:",WordRepeat.getDistance(i)
			factor(WordRepeat.getDistance(i),length)
			dec(WordRepeat.getWord(i),dec_word)

def factor(factorList,length):
	#factorList of the distances between first and each iteration of the word
	rep_list=[];
	for i in factorList:
		for j in range(2,int(length)):
			if i%j==0:
				if not j in rep_list:
					rep_list.append(j)
	print "Possible size:", rep_list

def key_gen(new_key):
	#Generates key
	keygen=[]
	key=new_key
	for x in key:
		keyword.append(ord(x))
	for i in keyword:
		if(i>=65 and i<=90):
			i=i-65
		if(i>=97 and i<=122):
			i=i-97
		keygen.append(i)
	return keygen

#main
array = []
keyword = []
vign = table()
print "Enter a document to encrypt and analyze:"
filename=raw_input()
print "Enter a key:"
key=raw_input()
print "Minumum number of repetitions:"
repeat=raw_input()
print "Maximum keyword length:"
length=raw_input()
print "Word to check (maximum 3 word):"
dec_word=raw_input()
keyword = key_gen(key)
vigniere_enc(filename)
#vigniere_dec()
analyze(repeat,length,dec_word)
