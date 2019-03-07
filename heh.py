from pyscf import gto, scf
heh = open('heh.dat','w')
for i in range(1000):

    e = scf.RHF(gto.M(atom='He 0 0 0; H 0 0 {}'.format(str(3.6*i/1000)),basis='sto-3g', charge=1, verbose=0, unit='bohr')).kernel()
    print >>heh, str(3.5*i/1000), str(e)
