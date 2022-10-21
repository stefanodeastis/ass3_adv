#!/usr/bin/env python3
# Copyright (C) 2022 s.deastis@studenti.unipi.it
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""Tranining for the CMEPDA course, 2022/23.
"""
import argparse
import time
import string
import numpy as np
import matplotlib.pyplot as plt


class VoltageData:
    def __init__(self,times,voltages,errors=None):
        times=np.array(times)
        voltages=np.array(voltages)
        self._data=np.column_stack([times,voltages])

    @classmethod
    def from_file(cls, file_path):
        """ Alternate constructor from a data file, exploiting load_txt()"""
        t, v,errors = np.loadtxt(file_path, unpack=True)
        return cls(t, v)

    def __len__(self):
        '''
        '''
        return len(self._data)
'''
    def __iter__(self):
        """Return the values row by row.
        We use a generator expression here. The syntax is very readible!"""
        for i in range(len(self)):
            yield self._data[i, :]
            #yield ritorna il generatore
'''

class Animal:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
        '''
    def __iter__(self):
        a=np.array([self.x,self.y,self.z])
        for i in a:
            yield i
            '''
    def __iter__(self):
        yield self.x
    def __next__(self):
        a=np.array([self.x,self.y,self.z])
        if self.x <3:
            x=self.x
            self.x +=1
            return a[0]
        else:
            raise StopIteration
if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Print some book statistics')
    parser.add_argument('infile', type=str, help='name of the file .txt containing the data sample')
    args = parser.parse_args()

    t,V,errors=np.loadtxt(args.infile, unpack=True)
    data=VoltageData(t,V)
    #data=VoltageData.from_file(args.infile)

    print(data._data[:,0]) #stampa i tempi (1 le ampiezze)
    print(len(data))
    for i in data._data:
        print(i)
    prova=Animal((1.,2.,3.),5,6)
    for i in prova:
        print (i)







#with open(file, 'r',encoding='utf-8') as data:
