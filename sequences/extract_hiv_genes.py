from Bio import SeqIO
import sys

if len(sys.argv) < 2:
  print('USAGE: extract_hiv_genes.py sequence_file')
  exit(0)

seqs = list(SeqIO.parse(sys.argv[1],'fasta'))

gag = ''
pol = ''
env = ''

print(len(seqs[1].seq))

for i in xrange(len(seqs)):
  gag += '>' + seqs[i].id + '\n' + seqs[i].seq[:1479] + '\n'
  pol += '>' + seqs[i].id + '\n' + seqs[i].seq[1479:4479] + '\n'
  env += '>' + seqs[i].id + '\n' + seqs[i].seq[4479:] + '\n'
  
  
fName = sys.argv[1][:sys.argv[1].rfind('.')] 

gagName = fName + '_gag.fasta'
polName = fName + '_pol.fasta'
envName = fName + '_env.fasta'

#print(fName)

gagFile = open(gagName,'w')
gagFile.write(str(gag))
gagFile.close()

'''
polFile = open(polName,'w')
polFile.write(str(pol))
polFile.close()
'''

envFile = open(envName,'w')
envFile.write(str(env))
envFile.close()


