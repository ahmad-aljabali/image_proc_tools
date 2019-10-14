'''
Matrix formats

K (intrensic camera_matrix)= 
[fx   0   cx]
[0    fy  cy]
[0    0   1 ]

D (distortion coeffs)= [k1,k2,p1,p2,k2,...,kn]

R (rotation matrix)=
[nx  ox  ax]
[ny  oy  ay]
[nz  oz  az]

P (projection matrix)=
[f   0   cx'   T*f]
[0   f   cy   0  ]
[0   0   1    0  ]

Q (reprojection matrix)*=
[1   0   0      -cx       ]
[0   1   0      -cy       ]
[0   0   0       f        ]
[0   0   -1/T   (cx-cx')/T]

*: use princeple camera values typacly left
*: term Q44 can be replaced as a simplification with 0 by assuming cx=cx'

'''
import numpy as np

CAMERA_HEIGHT=
CAMERA_WIDTH=


f=
cx=
cx_prim=
cy=
T=   #T = P14/f

Q =np.array([
[1,   0,   0,      -cx       ],
[0,   1,   0,      -cy       ],
[0,   0,   0,       f        ],
[0,   0,   -1/T,   (cx-cx_prim)/T]])


# Left Camera
KL =

DL = 

RL = 

PL = 

# Right Camera
KR = 

DR = 

RR = 

PR = 
