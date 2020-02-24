# Generate GFF files, for Awk exercise

library(Homo.sapiens)
library(rtracklayer)
library(dplyr)

genome = genes(TxDb.Hsapiens.UCSC.hg19.knownGene) %>% subset(seqnames %in% c("chr22", "chr8", "chr21"))
#genome = genes(TxDb.Hsapiens.UCSC.hg19.knownGene) %>% subset(seqnames %in% c("chr22", "chr21"))
genome$symbol = AnnotationDbi::select(org.Hs.eg.db, key=genome$gene_id, keytype='ENTREZID', columns='SYMBOL')$SYMBOL
genome$exerc1 = ifelse(start(chr8)>5000000 & end(chr8) < 10000000, T, F)

export(genome, "exercises/genes/human_genome_subset.gff", "gff3")
