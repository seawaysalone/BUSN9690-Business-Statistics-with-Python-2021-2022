# -*- coding: utf-8 -*-
"""
Created on Sat Dec 11 16:59:16 2021

@author: ADMIN

Q2
"""
import pandas as pd

employee = pd.DataFrame({'empno': ['00010', '00020', '00030', '00110', '00120', '00130'],
                        'lastname': ['HASS', 'THOMPSON', 'KWAN', 'LUCCHESSI', 'OCONNELL', 'QUINTANA'],
                         'workdept': ['A00', 'B01', 'CO1', 'A00', 'A00', 'C01']})

department = pd.DataFrame({'deptno': ['A00', 'B01', 'C01', 'D01'],
                          'deptname': ['Spiffy COMPUTER SERVICE DIV.', ' PLANNING', 'INFORMATION CENTER', 'DEVELOPMENT CENTER'],
                           'mgrno': ['000010', '000020', '000030', '']})

project = pd.DataFrame({'projno': ['AD3100', 'IF1000', 'IF2000', 'MA2100', 'PL2100'],
                        'projname': ['ADMIN SERVICES', 'QUERY SERVICES', 'USER EDUCATION', 'WELD LINE AUTOMATION', 'WELD LINE PLANNING'],
                        'deptno': ['D01', 'C01', 'E01', 'D01', 'B01'], 'respemp': ['000010', '000030', '000030', '000010', '000020']})

"""
Write one statement in Python to perform a left join on Table project and Table department according to deptno;
"""

leftjoin = pd.merge(project, department, on='deptno', how='left')

"""
Write one statement in Python to perform a right join on Table project and Table department according to deptno
"""

rightjoin = pd.merge(project,department,on='deptno',how='right')


"""
Write one statement in Python to perform an inner join on Table project and Table department according to deptno
"""

innerJoin=pd.merge(project, department,on="deptno")

"""
innerJoin=pd.merge(project, department,on="deptno")
"""
fullJoin=pd.merge(project, department,on="deptno", how='outer')
