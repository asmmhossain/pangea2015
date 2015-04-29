args <- commandArgs(trailingOnly=T)

if(length(args) < 1)
{
  stop('Tree file name not provided')
}

tName <- paste(args[1],'.rtt.newick',sep='')
#dateName <- paste(args[1],'.date',sep='')

#print(tName)
#print(rttName)

library('ape')
library('adephylo')

t <- read.tree(tName)

dis <- distRoot(t)

#print(names(t))

dates <- numeric(length(t$tip.label))

#write(length(dates),file=dateName,append=T)


for(i in 1:length(dates))
{
  dates[i]<-as.numeric(strsplit(t$tip.label[i],'_')[[1]][3])
  
  #str <- paste(t$tip.label[i],dates[i],sep='\t')
  #write(str,file=dateName,append=T)
}

lm(dis~dates)
