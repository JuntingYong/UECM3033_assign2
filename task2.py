# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 18:57:15 2016

@author: yong
"""

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import scipy as sp

#define a function called svd 
def svd(n):
    

    # first, make new matrix sigma for red, green and blue respectively 
    Sig_red_new=Sr.copy()
    Sig_green_new=Sg.copy()
    Sig_blue_new=Sb.copy()
    
    # then, make the first n element as nonzero
    Sig_red_new[n:800]=np.zeros_like(Sr[n:800])
    Sig_green_new[n:800]=np.zeros_like(Sg[n:800])
    Sig_blue_new[n:800]=np.zeros_like(Sb[n:800])

    # create diagonal matrix to perform dot multiplication by changing the 
    # dimension of sigma from (800,1) to (800,1000)to (800,1000)
    Sig_red_new = sp.linalg.diagsvd(Sig_red_new,800,1000)
    Sig_green_new = sp.linalg.diagsvd(Sig_green_new,800,1000)
    Sig_blue_new = sp.linalg.diagsvd(Sig_blue_new,800,1000)

    # now we can perform dot multiplication to create lower resolution matrix 
    new_red = np.dot(np.dot(Ur,Sig_red_new), Vr)
    new_green = np.dot(np.dot(Ug, Sig_green_new), Vg)
    new_blue = np.dot(np.dot(Ub, Sig_blue_new), Vb) 
    
    # to construct new resolution matrix
    img[:,:,0]= new_red
    img[:,:,1]= new_green
    img[:,:,2]= new_blue

    #plot the image 
    fig2 = plt.figure(n)
    ax1 = fig2.add_subplot(2,2,1)
    ax2 = fig2.add_subplot(2,2,2)
    ax3 = fig2.add_subplot(2,2,3)
    ax4 = fig2.add_subplot(2,2,4)
    ax1.imshow(img)
    ax2.imshow(r, cmap = 'Reds')
    ax3.imshow(g, cmap = 'Greens')
    ax4.imshow(b, cmap = 'Blues')
    plt.show()


#the original image
#read image
img=mpimg.imread('temple.jpg')
# generate rgb array
[r,g,b] = [img[:,:,i] for i in range(3)]
print("Original image")
fig = plt.figure(1)
ax1 = fig.add_subplot(2,2,1)
ax2 = fig.add_subplot(2,2,2)
ax3 = fig.add_subplot(2,2,3)
ax4 = fig.add_subplot(2,2,4)
ax1.imshow(img)
ax2.imshow(r, cmap = 'Reds')
ax3.imshow(g, cmap = 'Greens')
ax4.imshow(b, cmap = 'Blues')
plt.show()


Ur, Sr, Vr = sp.linalg.svd(r) #to find U, sigma and V for red matrix
Ug, Sg, Vg = sp.linalg.svd(g) #to find U, sigma and V for green matrix
Ub, Sb, Vb = sp.linalg.svd(b) #to find U, sigma and V for blue matrix

#to find the none zero elements in sigma of each red, green and blue matrices
red_nonzero=np.count_nonzero(Sr)
green_nonzero=np.count_nonzero(Sg)
blue_nonzero=np.count_nonzero(Sb)
print("The number of non zero elements in original Sigma of red, green, blue matrices are",red_nonzero,"," ,blue_nonzero,"and" ,green_nonzero, "respectively.")


#lower resolution with n=30
print("When n = 30， lower resolution")
svd(30)

#better resolution with n=200
print("When n = 200, better resolution")
svd(200)