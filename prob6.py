import numpy as np
from matplotlib import pyplot as plt
from numpy.linalg import eig

def main():
    #Define probabilities
    a = 1/6
    b = 19/120
    c = 7/40
    d = 1/120

    M = np.array([[d, d, d, d, d, d, c, c, c, c, c, c], 
                  [a, 0, 0, 0, 0, 0, 0, a, a, a, a, a], 
                  [a, a, 0, 0, 0, 0, 0, 0, a, a, a, a], 
                  [a, a, a, a, a, a, a, a, a, a, a, a], 
                  [a, a, a, a, 0, 0, 0, 0, 0, 0, a, a],
                  [b, b, b, b, b, 0, 0, 0, 0, 0, 0, b],
                  [a, a, a, a, a, a, 0, 0, 0, 0, 0, 0],
                  [0, a, a, a, a, a, a, 0, 0, 0, 0, 0],
                  [0, 0, a, a, a, a, a, a, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, a, a, a, a, a, a, 0, 0],
                  [0, 0, 0, 0, 0, b, b, b, b, b, b, 0]
                  ])

    eval, evec = eig(M)
    max_mag = 0
    index = -1
    for i in range(len(eval)):
        if abs(eval[i]) > max_mag:
            max_mag = eval[i]
            index = i
    
    mag_eig_sln = (abs(evec[:,index]))
    norm_mag_eig_sln = mag_eig_sln / sum(mag_eig_sln)
    print(mag_eig_sln)
    for a, b in enumerate(norm_mag_eig_sln):
        print('Space: ' + str(a + 1) + ': Probability: ' + str(b))



if __name__ == '__main__':
    main()