from pyscf import gto, scf
hf_scanner = scf.RHF(gto.Mole().set(verbose=0)).as_scanner()
a = hf_scanner(gto.M(atom='H 0 0 0; F 0 0 1.1'))
