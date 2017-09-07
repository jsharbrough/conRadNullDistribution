# -*- coding: utf-8 -*-
import sys
import random
def polSub(fasta,code='invertebrateMt'):
    geneticCodes = {'standard':{"TTT":"F",	"TTC":"F",	"TTA":"L",	"TTG":"L",	"TCT":"S",	"TCC":"S",	"TCA":"S",	"TCG":"S",	"TAT":"Y",	"TAC":"Y",	"TAA":"*",	"TAG":"*",	"TGT":"C",	"TGC":"C",	"TGA":"*",	"TGG":"W",	"CTT":"L",	"CTC":"L",	"CTA":"L",	"CTG":"L",	"CCT":"P",	"CCC":"P",	"CCA":"P",	"CCG":"P",	"CAT":"H",	"CAC":"H",	"CAA":"Q",	"CAG":"Q",	"CGT":"R",	"CGC":"R",	"CGA":"R",	"CGG":"R",	"ATT":"I",	"ATC":"I",	"ATA":"I",	"ATG":"M",	"ACT":"T",	"ACC":"T",	"ACA":"T",	"ACG":"T",	"AAT":"N",	"AAC":"N",	"AAA":"K",	"AAG":"K",	"AGT":"S",	"AGC":"S",	"AGA":"R",	"AGG":"R",	"GTT":"V",	"GTC":"V",	"GTA":"V",	"GTG":"V",	"GCT":"A",	"GCC":"A",	"GCA":"A",	"GCG":"A",	"GAT":"D",	"GAC":"D",	"GAA":"E",	"GAG":"E",	"GGT":"G",	"GGC":"G",	"GGA":"G",	"GGG":"G"},'invertebrateMt':{'CTT': 'L', 'TAG': '*', 'ACA': 'T', 'ACG': 'T', 'ATC': 'I', 'AAC': 'N', 'ATA': 'M', 'AGG': 'S', 'CCT': 'P', 'ACT': 'T', 'AGC': 'S', 'AAG': 'K', 'AGA': 'S', 'CAT': 'H', 'AAT': 'N', 'ATT': 'I', 'CTG': 'L', 'CTA': 'L', 'CTC': 'L', 'CAC': 'H', 'AAA': 'K', 'CCG': 'P', 'AGT': 'S', 'CCA': 'P', 'CAA': 'Q', 'CCC': 'P', 'TAT': 'Y', 'GGT': 'G', 'TGT': 'C', 'CGA': 'R', 'CAG': 'Q', 'TCT': 'S', 'GAT': 'D', 'CGG': 'R', 'TTT': 'F', 'TGC': 'C', 'GGG': 'G', 'TGA': 'W', 'GGA': 'G', 'TGG': 'W', 'GGC': 'G', 'TAC': 'Y', 'TTC': 'F', 'TCG': 'S', 'TTA': 'L', 'TTG': 'L', 'TCC': 'S', 'ACC': 'T', 'TAA': '*', 'GCA': 'A', 'GTA': 'V', 'GCC': 'A', 'GTC': 'V', 'GCG': 'A', 'GTG': 'V', 'GAG': 'E', 'GTT': 'V', 'GCT': 'A', 'GAC': 'D', 'CGT': 'R', 'GAA': 'E', 'TCA': 'S', 'ATG': 'M', 'CGC': 'R'},'vertebrateMt':{'CTT': 'L', 'TAG': '*', 'ACA': 'T', 'ACG': 'T', 'ATC': 'I', 'AAC': 'N', 'ATA': 'M', 'AGG': '*', 'CCT': 'P', 'ACT': 'T', 'AGC': 'S', 'AAG': 'K', 'AGA': '*', 'CAT': 'H', 'AAT': 'N', 'ATT': 'I', 'CTG': 'L', 'CTA': 'L', 'CTC': 'L', 'CAC': 'H', 'AAA': 'K', 'CCG': 'P', 'AGT': 'S', 'CCA': 'P', 'CAA': 'Q', 'CCC': 'P', 'TAT': 'Y', 'GGT': 'G', 'TGT': 'C', 'CGA': 'R', 'CAG': 'Q', 'TCT': 'S', 'GAT': 'D', 'CGG': 'R', 'TTT': 'F', 'TGC': 'C', 'GGG': 'G', 'TGA': 'W', 'GGA': 'G', 'TGG': 'W', 'GGC': 'G', 'TAC': 'Y', 'TTC': 'F', 'TCG': 'S', 'TTA': 'L', 'TTG': 'L', 'TCC': 'S', 'ACC': 'T', 'TAA': '*', 'GCA': 'A', 'GTA': 'V', 'GCC': 'A', 'GTC': 'V', 'GCG': 'A', 'GTG': 'V', 'GAG': 'E', 'GTT': 'V', 'GCT': 'A', 'GAC': 'D', 'CGT': 'R', 'GAA': 'E', 'TCA': 'S', 'ATG': 'M', 'CGC': 'R'}, 'yeastMt':{'CTT': 'T', 'TAG': '*', 'ACA': 'T', 'ACG': 'T', 'ATC': 'I', 'AAC': 'N', 'ATA': 'M', 'AGG': 'R', 'CCT': 'P', 'ACT': 'T', 'AGC': 'S', 'AAG': 'K', 'AGA': 'R', 'CAT': 'H', 'AAT': 'N', 'ATT': 'I', 'CTG': 'T', 'CTA': 'T', 'CTC': 'T', 'CAC': 'H', 'AAA': 'K', 'CCG': 'P', 'AGT': 'S', 'CCA': 'P', 'CAA': 'Q', 'CCC': 'P', 'TAT': 'Y', 'GGT': 'G', 'TGT': 'C', 'CGA': 'R', 'CAG': 'Q', 'TCT': 'S', 'GAT': 'D', 'CGG': 'R', 'TTT': 'F', 'TGC': 'C', 'GGG': 'G', 'TGA': 'W', 'GGA': 'G', 'TGG': 'W', 'GGC': 'G', 'TAC': 'Y', 'TTC': 'F', 'TCG': 'S', 'TTA': 'L', 'TTG': 'L', 'TCC': 'S', 'ACC': 'T', 'TAA': '*', 'GCA': 'A', 'GTA': 'V', 'GCC': 'A', 'GTC': 'V', 'GCG': 'A', 'GTG': 'V', 'GAG': 'E', 'GTT': 'V', 'GCT': 'A', 'GAC': 'D', 'CGT': 'R', 'GAA': 'E', 'TCA': 'S', 'ATG': 'M', 'CGC': 'R'}, 'coelenterateMt':{'CTT': 'L', 'TAG': '*', 'ACA': 'T', 'ACG': 'T', 'ATC': 'I', 'AAC': 'N', 'ATA': 'I', 'AGG': 'R', 'CCT': 'P', 'ACT': 'T', 'AGC': 'S', 'AAG': 'K', 'AGA': 'R', 'CAT': 'H', 'AAT': 'N', 'ATT': 'I', 'CTG': 'L', 'CTA': 'L', 'CTC': 'L', 'CAC': 'H', 'AAA': 'K', 'CCG': 'P', 'AGT': 'S', 'CCA': 'P', 'CAA': 'Q', 'CCC': 'P', 'TAT': 'Y', 'GGT': 'G', 'TGT': 'C', 'CGA': 'R', 'CAG': 'Q', 'TCT': 'S', 'GAT': 'D', 'CGG': 'R', 'TTT': 'F', 'TGC': 'C', 'GGG': 'G', 'TGA': 'W', 'GGA': 'G', 'TGG': 'W', 'GGC': 'G', 'TAC': 'Y', 'TTC': 'F', 'TCG': 'S', 'TTA': 'L', 'TTG': 'L', 'TCC': 'S', 'ACC': 'T', 'TAA': '*', 'GCA': 'A', 'GTA': 'V', 'GCC': 'A', 'GTC': 'V', 'GCG': 'A', 'GTG': 'V', 'GAG': 'E', 'GTT': 'V', 'GCT': 'A', 'GAC': 'D', 'CGT': 'R', 'GAA': 'E', 'TCA': 'S', 'ATG': 'M', 'CGC': 'R'},'ciliateNuc':{'CTT': 'L', 'TAG': 'Q', 'ACA': 'T', 'ACG': 'T', 'ATC': 'I', 'AAC': 'N', 'ATA': 'I', 'AGG': 'R', 'CCT': 'P', 'ACT': 'T', 'AGC': 'S', 'AAG': 'K', 'AGA': 'R', 'CAT': 'H', 'AAT': 'N', 'ATT': 'I', 'CTG': 'L', 'CTA': 'L', 'CTC': 'L', 'CAC': 'H', 'AAA': 'K', 'CCG': 'P', 'AGT': 'S', 'CCA': 'P', 'CAA': 'Q', 'CCC': 'P', 'TAT': 'Y', 'GGT': 'G', 'TGT': 'C', 'CGA': 'R', 'CAG': 'Q', 'TCT': 'S', 'GAT': 'D', 'CGG': 'R', 'TTT': 'F', 'TGC': 'C', 'GGG': 'G', 'TGA': '*', 'GGA': 'G', 'TGG': 'W', 'GGC': 'G', 'TAC': 'Y', 'TTC': 'F', 'TCG': 'S', 'TTA': 'L', 'TTG': 'L', 'TCC': 'S', 'ACC': 'T', 'TAA': 'Q', 'GCA': 'A', 'GTA': 'V', 'GCC': 'A', 'GTC': 'V', 'GCG': 'A', 'GTG': 'V', 'GAG': 'E', 'GTT': 'V', 'GCT': 'A', 'GAC': 'D', 'CGT': 'R', 'GAA': 'E', 'TCA': 'S', 'ATG': 'M', 'CGC': 'R'},'echinodermMt':{'CTT': 'L', 'TAG': '*', 'ACA': 'T', 'ACG': 'T', 'ATC': 'I', 'AAC': 'N', 'ATA': 'I', 'AGG': 'S', 'CCT': 'P', 'ACT': 'T', 'AGC': 'S', 'AAG': 'K', 'AGA': 'S', 'CAT': 'H', 'AAT': 'N', 'ATT': 'I', 'CTG': 'L', 'CTA': 'L', 'CTC': 'L', 'CAC': 'H', 'AAA': 'N', 'CCG': 'P', 'AGT': 'S', 'CCA': 'P', 'CAA': 'Q', 'CCC': 'P', 'TAT': 'Y', 'GGT': 'G', 'TGT': 'C', 'CGA': 'R', 'CAG': 'Q', 'TCT': 'S', 'GAT': 'D', 'CGG': 'R', 'TTT': 'F', 'TGC': 'C', 'GGG': 'G', 'TGA': 'W', 'GGA': 'G', 'TGG': 'W', 'GGC': 'G', 'TAC': 'Y', 'TTC': 'F', 'TCG': 'S', 'TTA': 'L', 'TTG': 'L', 'TCC': 'S', 'ACC': 'T', 'TAA': '*', 'GCA': 'A', 'GTA': 'V', 'GCC': 'A', 'GTC': 'V', 'GCG': 'A', 'GTG': 'V', 'GAG': 'E', 'GTT': 'V', 'GCT': 'A', 'GAC': 'D', 'CGT': 'R', 'GAA': 'E', 'TCA': 'S', 'ATG': 'M', 'CGC': 'R'}, 'euplotidNuc':{'CTT': 'L', 'TAG': '*', 'ACA': 'T', 'ACG': 'T', 'ATC': 'I', 'AAC': 'N', 'ATA': 'I', 'AGG': 'R', 'CCT': 'P', 'ACT': 'T', 'AGC': 'S', 'AAG': 'K', 'AGA': 'R', 'CAT': 'H', 'AAT': 'N', 'ATT': 'I', 'CTG': 'L', 'CTA': 'L', 'CTC': 'L', 'CAC': 'H', 'AAA': 'K', 'CCG': 'P', 'AGT': 'S', 'CCA': 'P', 'CAA': 'Q', 'CCC': 'P', 'TAT': 'Y', 'GGT': 'G', 'TGT': 'C', 'CGA': 'R', 'CAG': 'Q', 'TCT': 'S', 'GAT': 'D', 'CGG': 'R', 'TTT': 'F', 'TGC': 'C', 'GGG': 'G', 'TGA': 'C', 'GGA': 'G', 'TGG': 'W', 'GGC': 'G', 'TAC': 'Y', 'TTC': 'F', 'TCG': 'S', 'TTA': 'L', 'TTG': 'L', 'TCC': 'S', 'ACC': 'T', 'TAA': '*', 'GCA': 'A', 'GTA': 'V', 'GCC': 'A', 'GTC': 'V', 'GCG': 'A', 'GTG': 'V', 'GAG': 'E', 'GTT': 'V', 'GCT': 'A', 'GAC': 'D', 'CGT': 'R', 'GAA': 'E', 'TCA': 'S', 'ATG': 'M', 'CGC': 'R'}, 'bacterial':{'CTT': 'L', 'TAG': '*', 'ACA': 'T', 'ACG': 'T', 'ATC': 'I', 'AAC': 'N', 'ATA': 'I', 'AGG': 'R', 'CCT': 'P', 'ACT': 'T', 'AGC': 'S', 'AAG': 'K', 'AGA': 'R', 'CAT': 'H', 'AAT': 'N', 'ATT': 'I', 'CTG': 'L', 'CTA': 'L', 'CTC': 'L', 'CAC': 'H', 'AAA': 'K', 'CCG': 'P', 'AGT': 'S', 'CCA': 'P', 'CAA': 'Q', 'CCC': 'P', 'TAT': 'Y', 'GGT': 'G', 'TGT': 'C', 'CGA': 'R', 'CAG': 'Q', 'TCT': 'S', 'GAT': 'D', 'CGG': 'R', 'TTT': 'F', 'TGC': 'C', 'GGG': 'G', 'TGA': '*', 'GGA': 'G', 'TGG': 'W', 'GGC': 'G', 'TAC': 'Y', 'TTC': 'F', 'TCG': 'S', 'TTA': 'L', 'TTG': 'L', 'TCC': 'S', 'ACC': 'T', 'TAA': '*', 'GCA': 'A', 'GTA': 'V', 'GCC': 'A', 'GTC': 'V', 'GCG': 'A', 'GTG': 'V', 'GAG': 'E', 'GTT': 'V', 'GCT': 'A', 'GAC': 'D', 'CGT': 'R', 'GAA': 'E', 'TCA': 'S', 'ATG': 'M', 'CGC': 'R'},'yeastNuc':{'CTT': 'L', 'TAG': '*', 'ACA': 'T', 'ACG': 'T', 'ATC': 'I', 'AAC': 'N', 'ATA': 'I', 'AGG': 'R', 'CCT': 'P', 'ACT': 'T', 'AGC': 'S', 'AAG': 'K', 'AGA': 'R', 'CAT': 'H', 'AAT': 'N', 'ATT': 'I', 'CTG': 'S', 'CTA': 'L', 'CTC': 'L', 'CAC': 'H', 'AAA': 'K', 'CCG': 'P', 'AGT': 'S', 'CCA': 'P', 'CAA': 'Q', 'CCC': 'P', 'TAT': 'Y', 'GGT': 'G', 'TGT': 'C', 'CGA': 'R', 'CAG': 'Q', 'TCT': 'S', 'GAT': 'D', 'CGG': 'R', 'TTT': 'F', 'TGC': 'C', 'GGG': 'G', 'TGA': '*', 'GGA': 'G', 'TGG': 'W', 'GGC': 'G', 'TAC': 'Y', 'TTC': 'F', 'TCG': 'S', 'TTA': 'L', 'TTG': 'L', 'TCC': 'S', 'ACC': 'T', 'TAA': '*', 'GCA': 'A', 'GTA': 'V', 'GCC': 'A', 'GTC': 'V', 'GCG': 'A', 'GTG': 'V', 'GAG': 'E', 'GTT': 'V', 'GCT': 'A', 'GAC': 'D', 'CGT': 'R', 'GAA': 'E', 'TCA': 'S', 'ATG': 'M', 'CGC': 'R'}, 'ascidianMt':{'CTT': 'L', 'TAG': '*', 'ACA': 'T', 'ACG': 'T', 'ATC': 'I', 'AAC': 'N', 'ATA': 'M', 'AGG': 'G', 'CCT': 'P', 'ACT': 'T', 'AGC': 'S', 'AAG': 'K', 'AGA': 'G', 'CAT': 'H', 'AAT': 'N', 'ATT': 'I', 'CTG': 'L', 'CTA': 'L', 'CTC': 'L', 'CAC': 'H', 'AAA': 'K', 'CCG': 'P', 'AGT': 'S', 'CCA': 'P', 'CAA': 'Q', 'CCC': 'P', 'TAT': 'Y', 'GGT': 'G', 'TGT': 'C', 'CGA': 'R', 'CAG': 'Q', 'TCT': 'S', 'GAT': 'D', 'CGG': 'R', 'TTT': 'F', 'TGC': 'C', 'GGG': 'G', 'TGA': 'W', 'GGA': 'G', 'TGG': 'W', 'GGC': 'G', 'TAC': 'Y', 'TTC': 'F', 'TCG': 'S', 'TTA': 'L', 'TTG': 'L', 'TCC': 'S', 'ACC': 'T', 'TAA': '*', 'GCA': 'A', 'GTA': 'V', 'GCC': 'A', 'GTC': 'V', 'GCG': 'A', 'GTG': 'V', 'GAG': 'E', 'GTT': 'V', 'GCT': 'A', 'GAC': 'D', 'CGT': 'R', 'GAA': 'E', 'TCA': 'S', 'ATG': 'M', 'CGC': 'R'},'flatwormMt':{'CTT': 'L', 'TAG': '*', 'ACA': 'T', 'ACG': 'T', 'ATC': 'I', 'AAC': 'N', 'ATA': 'I', 'AGG': 'S', 'CCT': 'P', 'ACT': 'T', 'AGC': 'S', 'AAG': 'K', 'AGA': 'S', 'CAT': 'H', 'AAT': 'N', 'ATT': 'I', 'CTG': 'L', 'CTA': 'L', 'CTC': 'L', 'CAC': 'H', 'AAA': 'N', 'CCG': 'P', 'AGT': 'S', 'CCA': 'P', 'CAA': 'Q', 'CCC': 'P', 'TAT': 'Y', 'GGT': 'G', 'TGT': 'C', 'CGA': 'R', 'CAG': 'Q', 'TCT': 'S', 'GAT': 'D', 'CGG': 'R', 'TTT': 'F', 'TGC': 'C', 'GGG': 'G', 'TGA': 'W', 'GGA': 'G', 'TGG': 'W', 'GGC': 'G', 'TAC': 'Y', 'TTC': 'F', 'TCG': 'S', 'TTA': 'L', 'TTG': 'L', 'TCC': 'S', 'ACC': 'T', 'TAA': 'Y', 'GCA': 'A', 'GTA': 'V', 'GCC': 'A', 'GTC': 'V', 'GCG': 'A', 'GTG': 'V', 'GAG': 'E', 'GTT': 'V', 'GCT': 'A', 'GAC': 'D', 'CGT': 'R', 'GAA': 'E', 'TCA': 'S', 'ATG': 'M', 'CGC': 'R'},'chlorophyceanMt':{'CTT': 'L', 'TAG': 'L', 'ACA': 'T', 'ACG': 'T', 'ATC': 'I', 'AAC': 'N', 'ATA': 'I', 'AGG': 'R', 'CCT': 'P', 'ACT': 'T', 'AGC': 'S', 'AAG': 'K', 'AGA': 'R', 'CAT': 'H', 'AAT': 'N', 'ATT': 'I', 'CTG': 'L', 'CTA': 'L', 'CTC': 'L', 'CAC': 'H', 'AAA': 'K', 'CCG': 'P', 'AGT': 'S', 'CCA': 'P', 'CAA': 'Q', 'CCC': 'P', 'TAT': 'Y', 'GGT': 'G', 'TGT': 'C', 'CGA': 'R', 'CAG': 'Q', 'TCT': 'S', 'GAT': 'D', 'CGG': 'R', 'TTT': 'F', 'TGC': 'C', 'GGG': 'G', 'TGA': '*', 'GGA': 'G', 'TGG': 'W', 'GGC': 'G', 'TAC': 'Y', 'TTC': 'F', 'TCG': 'S', 'TTA': 'L', 'TTG': 'L', 'TCC': 'S', 'ACC': 'T', 'TAA': '*', 'GCA': 'A', 'GTA': 'V', 'GCC': 'A', 'GTC': 'V', 'GCG': 'A', 'GTG': 'V', 'GAG': 'E', 'GTT': 'V', 'GCT': 'A', 'GAC': 'D', 'CGT': 'R', 'GAA': 'E', 'TCA': 'S', 'ATG': 'M', 'CGC': 'R'},'trematodeMt':{'CTT': 'L', 'TAG': '*', 'ACA': 'T', 'ACG': 'T', 'ATC': 'I', 'AAC': 'N', 'ATA': 'M', 'AGG': 'S', 'CCT': 'P', 'ACT': 'T', 'AGC': 'S', 'AAG': 'K', 'AGA': 'S', 'CAT': 'H', 'AAT': 'N', 'ATT': 'I', 'CTG': 'L', 'CTA': 'L', 'CTC': 'L', 'CAC': 'H', 'AAA': 'N', 'CCG': 'P', 'AGT': 'S', 'CCA': 'P', 'CAA': 'Q', 'CCC': 'P', 'TAT': 'Y', 'GGT': 'G', 'TGT': 'C', 'CGA': 'R', 'CAG': 'Q', 'TCT': 'S', 'GAT': 'D', 'CGG': 'R', 'TTT': 'F', 'TGC': 'C', 'GGG': 'G', 'TGA': 'W', 'GGA': 'G', 'TGG': 'W', 'GGC': 'G', 'TAC': 'Y', 'TTC': 'F', 'TCG': 'S', 'TTA': 'L', 'TTG': 'L', 'TCC': 'S', 'ACC': 'T', 'TAA': '*', 'GCA': 'A', 'GTA': 'V', 'GCC': 'A', 'GTC': 'V', 'GCG': 'A', 'GTG': 'V', 'GAG': 'E', 'GTT': 'V', 'GCT': 'A', 'GAC': 'D', 'CGT': 'R', 'GAA': 'E', 'TCA': 'S', 'ATG': 'M', 'CGC': 'R'},'pterobranchiaMt':{'CTT': 'L', 'TAG': '*', 'ACA': 'T', 'ACG': 'T', 'ATC': 'I', 'AAC': 'N', 'ATA': 'I', 'AGG': 'K', 'CCT': 'P', 'ACT': 'T', 'AGC': 'S', 'AAG': 'K', 'AGA': 'S', 'CAT': 'H', 'AAT': 'N', 'ATT': 'I', 'CTG': 'L', 'CTA': 'L', 'CTC': 'L', 'CAC': 'H', 'AAA': 'K', 'CCG': 'P', 'AGT': 'S', 'CCA': 'P', 'CAA': 'Q', 'CCC': 'P', 'TAT': 'Y', 'GGT': 'G', 'TGT': 'C', 'CGA': 'R', 'CAG': 'Q', 'TCT': 'S', 'GAT': 'D', 'CGG': 'R', 'TTT': 'F', 'TGC': 'C', 'GGG': 'G', 'TGA': 'W', 'GGA': 'G', 'TGG': 'W', 'GGC': 'G', 'TAC': 'Y', 'TTC': 'F', 'TCG': 'S', 'TTA': 'L', 'TTG': 'L', 'TCC': 'S', 'ACC': 'T', 'TAA': '*', 'GCA': 'A', 'GTA': 'V', 'GCC': 'A', 'GTC': 'V', 'GCG': 'A', 'GTG': 'V', 'GAG': 'E', 'GTT': 'V', 'GCT': 'A', 'GAC': 'D', 'CGT': 'R', 'GAA': 'E', 'TCA': 'S', 'ATG': 'M', 'CGC': 'R'}}
    geneticCode = geneticCodes[code]
    startCodons = ['ATT','ATC','ATA','ATG','GTG'] #invertebrateMt code
    positionDict = {(0,1533):'COI',(1533,2217):'COII',(2217,2373):'ATP8',(2373,3066):'ATP6',(3066,4005):'ND1',(4005,4509):'ND6',(4509,5646):'CYTB',(5646,5940):'ND4L',(5940,7314):'ND4',(7314,9030):'ND5',(9030,9807):'COIII',(9807,10158):'ND3',(10158,11214):'ND2'} #{(start,stop):gene}
    seqDict, seqList, codonDict = buildCodonDict(fasta)
    popList = []
    sexList = []
    outList = [] 
    synSites = {">$Duluth":2591.52083333,	">$Heron2":2598,	">$McGregor":2599,	">$Waik36":2586.91666667,	">$WalesC":2584.91666667,	">$clone_1":2598,	">$AC51":2598.33333333,	">$Heron_mitochondrion":2599,	">$clone_7":2592.85416667,	">$Waik37":2586.58333333,	">$Gunn":2597.66666667,	">$DenmarkA":2593.125,	">$Waik372":2589.25,	">$Tarawera":2586.58333333,	">$Poerua_triploid":2597,	">$Kaniere_triploid":2586.58333333,	">$Waik_lane4_TCCTGAGC_trimmed_paired_contig_237":2593.79166667,	">$Brunner_2_4n":2593.60416674,	">$Brunner_6_3n":2592.9583334,	">$Grasmere_1_4n":2628.66666703,	">$Grasmere_6_3n":2599.62500001,	">$Poerua_72_4n":2605.47916675,	">$Rotoiti_1_4n":2594.35416672,	">$*Kaniere_1_2n":2598.33333333,	">$*Ianthe_lane1_TAAGGCGA_trimmed_paired_contig_309":2595,	">$*Yellow_Contig_56":2592.33333333,	">$*Alexsex":2592.33333333,	">$*AlexMap":2592.33333333,	">$*Lady":2598.66666667,	">$*Ianthe":2597,	">$*Rotoroa_1_2n":2598.58333338}
    C1Sites = {">$Duluth":6323.85416667,	">$Heron2":6320.33333333,	">$McGregor":6319,	">$Waik36":6330.25,	">$WalesC":6333.25,	">$clone_1":6319.66666667,	">$AC51":6318.66666667,	">$Heron_mitochondrion":6319.33333333,	">$clone_7":6322.52083333,	">$Waik37":6327.25,	">$Gunn":6324.33333333,	">$DenmarkA":6322.45833333,	">$Waik372":6330.58333333,	">$Tarawera":6329.25,	">$Poerua_triploid":6321.66666667,	">$Kaniere_triploid":6330.58333333,	">$Waik_lane4_TCCTGAGC_trimmed_paired_contig_237":6320.125,	">$Brunner_2_4n":6259.27083326,	">$Brunner_6_3n":6262.95833327,	">$Grasmere_1_4n":5990.99999963,	">$Grasmere_6_3n":6307.62499999,	">$Poerua_72_4n":6232.81249992,	">$Rotoiti_1_4n":6264.68749995,	">$*Kaniere_1_2n":6320.33333333,	">$*Ianthe_lane1_TAAGGCGA_trimmed_paired_contig_309":6321,	">$*Yellow_Contig_56":6326.33333333,	">$*Alexsex":6326.33333333,	">$*AlexMap":6326.33333333,	">$*Lady":6318,	">$*Ianthe":6321.33333333,	">$*Rotoroa_1_2n":6271.58333329}
    R1Sites = {">$Duluth":2298.625,	">$Heron2":2295.66666667,	">$McGregor":2296,	">$Waik36":2296.83333333,	">$WalesC":2295.83333333,	">$clone_1":2296.33333333,	">$AC51":2297,	">$Heron_mitochondrion":2295.66666667,	">$clone_7":2298.625,	">$Waik37":2300.16666667,	">$Gunn":2292,	">$DenmarkA":2298.41666667,	">$Waik372":2294.16666667,	">$Tarawera":2298.16666667,	">$Poerua_triploid":2295.33333333,	">$Kaniere_triploid":2296.83333333,	">$Waik_lane4_TCCTGAGC_trimmed_paired_contig_237":2300.08333333,	">$Brunner_2_4n":2361.125,	">$Brunner_6_3n":2358.08333333,	">$Grasmere_1_4n":2594.33333333,	">$Grasmere_6_3n":2306.75,	">$Poerua_72_4n":2375.70833333,	">$Rotoiti_1_4n":2354.95833333,	">$*Kaniere_1_2n":2295.33333333,	">$*Ianthe_lane1_TAAGGCGA_trimmed_paired_contig_309":2298,	">$*Yellow_Contig_56":2295.33333333,	">$*Alexsex":2295.33333333,	">$*AlexMap":2295.33333333,	">$*Lady":2297.33333333,	">$*Ianthe":2295.66666667,	">$*Rotoroa_1_2n":2343.83333333}
    C2Sites = {">$Duluth":5093.47916667,	">$Heron2":5090.33333333,	">$McGregor":5089.66666667,	">$Waik36":5100.75,	">$WalesC":5101.75,	">$clone_1":5091.33333333,	">$AC51":5089.33333333,	">$Heron_mitochondrion":5088.66666667,	">$clone_7":5092.14583333,	">$Waik37":5096.75,	">$Gunn":5090.33333333,	">$DenmarkA":5091.875,	">$Waik372":5097.41666667,	">$Tarawera":5097.08333333,	">$Poerua_triploid":5092,	">$Kaniere_triploid":5096.75,	">$Waik_lane4_TCCTGAGC_trimmed_paired_contig_237":5091.20833333,	">$Brunner_2_4n":5082.39583326,	">$Brunner_6_3n":5076.37499994,	">$Grasmere_1_4n":4999.33333297,	">$Grasmere_6_3n":5084.70833332,	">$Poerua_72_4n":5059.52083325,	">$Rotoiti_1_4n":5085.97916662,	">$*Kaniere_1_2n":5090,	">$*Ianthe_lane1_TAAGGCGA_trimmed_paired_contig_309":5095.33333333,	">$*Yellow_Contig_56":5097.33333333,	">$*Alexsex":5097.33333333,	">$*AlexMap":5097.33333333,	">$*Lady":5089,	">$*Ianthe":5093,	">$*Rotoroa_1_2n":5078.41666662}
    R2Sites = {">$Duluth":3529,	">$Heron2":3525.66666667,	">$McGregor":3525.33333333,	">$Waik36":3526.33333333,	">$WalesC":3527.33333333,	">$clone_1":3524.66666667,	">$AC51":3526.33333333,	">$Heron_mitochondrion":3526.33333333,	">$clone_7":3529,	">$Waik37":3530.66666667,	">$Gunn":3526,	">$DenmarkA":3529,	">$Waik372":3527.33333333,	">$Tarawera":3530.33333333,	">$Poerua_triploid":3525,	">$Kaniere_triploid":3530.66666667,	">$Waik_lane4_TCCTGAGC_trimmed_paired_contig_237":3529,	">$Brunner_2_4n":3538,	">$Brunner_6_3n":3544.66666667,	">$Grasmere_1_4n":3586,	">$Grasmere_6_3n":3529.66666667,	">$Poerua_72_4n":3549,	">$Rotoiti_1_4n":3533.66666667,	">$*Kaniere_1_2n":3525.66666667,	">$*Ianthe_lane1_TAAGGCGA_trimmed_paired_contig_309":3523.66666667,	">$*Yellow_Contig_56":3524.33333333,	">$*Alexsex":3524.33333333,	">$*AlexMap":3524.33333333,	">$*Lady":3526.33333333,	">$*Ianthe":3524,	">$*Rotoroa_1_2n":3537}
    C3Sites = {">$Duluth":2949.125,	">$Heron2":2945,	">$McGregor":2945,	">$Waik36":2947.16666667,	">$WalesC":2950.83333333,	">$clone_1":2944.66666667,	">$AC51":2945,	">$Heron_mitochondrion":2944.66666667,	">$clone_7":2949.79166667,	">$Waik37":2950.5,	">$Gunn":2944,	">$DenmarkA":2949.75,	">$Waik372":2952.83333333,	">$Tarawera":2950.5,	">$Poerua_triploid":2945.66666667,	">$Kaniere_triploid":2950.83333333,	">$Waik_lane4_TCCTGAGC_trimmed_paired_contig_237":2948.75,	">$Brunner_2_4n":2917.29166659,	">$Brunner_6_3n":2925.4166666,	">$Grasmere_1_4n":2832.33333297,	">$Grasmere_6_3n":2941.74999999,	">$Poerua_72_4n":2926.20833325,	">$Rotoiti_1_4n":2932.12499995,	">$*Kaniere_1_2n":2945.66666667,	">$*Ianthe_lane1_TAAGGCGA_trimmed_paired_contig_309":2945.33333333,	">$*Yellow_Contig_56":2946.66666667,	">$*Alexsex":2946.66666667,	">$*AlexMap":2946.66666667,	">$*Lady":2947.33333333,	">$*Ianthe":2945.33333333,	">$*Rotoroa_1_2n":2928.16666662}
    R3Sites = {">$Duluth":5673.35416667,	">$Heron2":5671,	">$McGregor":5670,	">$Waik36":5679.91666667,	">$WalesC":5678.25,	">$clone_1":5671.33333333,	">$AC51":5670.66666667,	">$Heron_mitochondrion":5670.33333333,	">$clone_7":5671.35416667,	">$Waik37":5676.91666667,	">$Gunn":5672.33333333,	">$DenmarkA":5671.125,	">$Waik372":5671.91666667,	">$Tarawera":5676.91666667,	">$Poerua_triploid":5671.33333333,	">$Kaniere_triploid":5676.58333333,	">$Waik_lane4_TCCTGAGC_trimmed_paired_contig_237":5671.45833333,	">$Brunner_2_4n":5703.10416667,	">$Brunner_6_3n":5695.625,	">$Grasmere_1_4n":5753,	">$Grasmere_6_3n":5672.625,	">$Poerua_72_4n":5682.3125,	">$Rotoiti_1_4n":5687.52083333,	">$*Kaniere_1_2n":5670,	">$*Ianthe_lane1_TAAGGCGA_trimmed_paired_contig_309":5673.66666667,	">$*Yellow_Contig_56":5675,	">$*Alexsex":5675,	">$*AlexMap":5675,	">$*Lady":5668,	">$*Ianthe":5671.66666667,	">$*Rotoroa_1_2n":5687.25}
    C4Sites = {">$Duluth":3422.02083333,	">$Heron2":3419.66666667,	">$McGregor":3420,	">$Waik36":3420.25,	">$WalesC":3423.25,	">$clone_1":3419.33333333,	">$AC51":3419,	">$Heron_mitochondrion":3419,	">$clone_7":3422.6875,	">$Waik37":3424.58333333,	">$Gunn":3420,	">$DenmarkA":3422.45833333,	">$Waik372":3428.25,	">$Tarawera":3424.91666667,	">$Poerua_triploid":3421,	">$Kaniere_triploid":3423.58333333,	">$Waik_lane4_TCCTGAGC_trimmed_paired_contig_237":3421.79166667,	">$Brunner_2_4n":3405.10416659,	">$Brunner_6_3n":3421.95833327,	">$Grasmere_1_4n":3382.99999963,	">$Grasmere_6_3n":3416.95833332,	">$Poerua_72_4n":3422.97916658,	">$Rotoiti_1_4n":3422.85416662,	">$*Kaniere_1_2n":3420.33333333,	">$*Ianthe_lane1_TAAGGCGA_trimmed_paired_contig_309":3420,	">$*Yellow_Contig_56":3420.66666667,	">$*Alexsex":3420.66666667,	">$*AlexMap":3420.66666667,	">$*Lady":3423,	">$*Ianthe":3419.33333333,	">$*Rotoroa_1_2n":3414.91666662}
    R4Sites = {">$Duluth":5200.45833333,	">$Heron2":5196.33333333,	">$McGregor":5195,	">$Waik36":5206.83333333,	">$WalesC":5205.83333333,	">$clone_1":5196.66666667,	">$AC51":5196.66666667,	">$Heron_mitochondrion":5196,	">$clone_7":5198.45833333,	">$Waik37":5202.83333333,	">$Gunn":5196.33333333,	">$DenmarkA":5198.41666667,	">$Waik372":5196.5,	">$Tarawera":5202.5,	">$Poerua_triploid":5196,	">$Kaniere_triploid":5203.83333333,	">$Waik_lane4_TCCTGAGC_trimmed_paired_contig_237":5198.41666667,	">$Brunner_2_4n":5215.29166667,	">$Brunner_6_3n":5199.08333333,	">$Grasmere_1_4n":5202.33333333,	">$Grasmere_6_3n":5197.41666667,	">$Poerua_72_4n":5185.54166667,	">$Rotoiti_1_4n":5196.79166667,	">$*Kaniere_1_2n":5195.33333333,	">$*Ianthe_lane1_TAAGGCGA_trimmed_paired_contig_309":5199,	">$*Yellow_Contig_56":5201,	">$*Alexsex":5201,	">$*AlexMap":5201,	">$*Lady":5192.33333333,	">$*Ianthe":5197.66666667,	">$*Rotoroa_1_2n":5200.5}
    C5Sites = {">$Duluth":4384.85416667,	">$Heron2":4382.33333333,	">$McGregor":4382,	">$Waik36":4383.58333333,	">$WalesC":4385.58333333,	">$clone_1":4382.33333333,	">$AC51":4382,	">$Heron_mitochondrion":4382.33333333,	">$clone_7":4385.1875,	">$Waik37":4385.58333333,	">$Gunn":4382.66666667,	">$DenmarkA":4385.125,	">$Waik372":4390.58333333,	">$Tarawera":4385.58333333,	">$Poerua_triploid":4383.33333333,	">$Kaniere_triploid":4386.25,	">$Waik_lane4_TCCTGAGC_trimmed_paired_contig_237":4383.79166667,	">$Brunner_2_4n":4338.9375,	">$Brunner_6_3n":4354.95833333,	">$Grasmere_1_4n":4238,	">$Grasmere_6_3n":4375.95833333,	">$Poerua_72_4n":4354.14583333,	">$Rotoiti_1_4n":4363.35416667,	">$*Kaniere_1_2n":4383.33333333,	">$*Ianthe_lane1_TAAGGCGA_trimmed_paired_contig_309":4384,	">$*Yellow_Contig_56":4381.66666667,	">$*Alexsex":4381.66666667,	">$*AlexMap":4381.66666667,	">$*Lady":4385.33333333,	">$*Ianthe":4384.66666667,	">$*Rotoroa_1_2n":4354.91666667}
    R5Sites = {">$Duluth":4237.625,	">$Heron2":4233.66666667,	">$McGregor":4233,	">$Waik36":4243.5,	">$WalesC":4243.5,	">$clone_1":4233.66666667,	">$AC51":4233.66666667,	">$Heron_mitochondrion":4232.66666667,	">$clone_7":4235.95833333,	">$Waik37":4241.83333333,	">$Gunn":4233.66666667,	">$DenmarkA":4235.75,	">$Waik372":4234.16666667,	">$Tarawera":4241.83333333,	">$Poerua_triploid":4233.66666667,	">$Kaniere_triploid":4241.16666667,	">$Waik_lane4_TCCTGAGC_trimmed_paired_contig_237":4236.41666667,	">$Brunner_2_4n":4281.45833326,	">$Brunner_6_3n":4266.08333327,	">$Grasmere_1_4n":4347.33333297,	">$Grasmere_6_3n":4238.41666665,	">$Poerua_72_4n":4254.37499992,	">$Rotoiti_1_4n":4256.29166662,	">$*Kaniere_1_2n":4232.33333333,	">$*Ianthe_lane1_TAAGGCGA_trimmed_paired_contig_309":4235,	">$*Yellow_Contig_56":4240,	">$*Alexsex":4240,	">$*AlexMap":4240,	">$*Lady":4230,	">$*Ianthe":4232.33333333,	">$*Rotoroa_1_2n":4260.49999996}
    C6Sites = {">$Duluth":4128.5625,	">$Heron2":4124.66666667,	">$McGregor":4124.33333333,	">$Waik36":4130.08333333,	">$WalesC":4129.75,	">$clone_1":4125.66666667,	">$AC51":4124.66666667,	">$Heron_mitochondrion":4125,	">$clone_7":4126.89583333,	">$Waik37":4123.41666667,	">$Gunn":4126.33333333,	">$DenmarkA":4127.04166667,	">$Waik372":4126.08333333,	">$Tarawera":4124.08333333,	">$Poerua_triploid":4126,	">$Kaniere_triploid":4125.75,	">$Waik_lane4_TCCTGAGC_trimmed_paired_contig_237":4126.04166667,	">$Brunner_2_4n":4078.47916674,	">$Brunner_6_3n":4075.2083334,	">$Grasmere_1_4n":3848.3333337,	">$Grasmere_6_3n":4112.54166668,	">$Poerua_72_4n":4050.43750008,	">$Rotoiti_1_4n":4084.39583338,	">$*Kaniere_1_2n":4126.33333333,	">$*Ianthe_lane1_TAAGGCGA_trimmed_paired_contig_309":4125,	">$*Yellow_Contig_56":4127.33333333,	">$*Alexsex":4127.33333333,	">$*AlexMap":4127.33333333,	">$*Lady":4121,	">$*Ianthe":4123.66666667,	">$*Rotoroa_1_2n":4085.08333338}
    R6Sites = {">$Duluth":4493.91666667,	">$Heron2":4491.33333333,	">$McGregor":4490.66666667,	">$Waik36":4497,	">$WalesC":4499.33333333,	">$clone_1":4490.33333333,	">$AC51":4491,	">$Heron_mitochondrion":4490,	">$clone_7":4494.25,	">$Waik37":4504,	">$Gunn":4490,	">$DenmarkA":4493.83333333,	">$Waik372":4498.66666667,	">$Tarawera":4503.33333333,	">$Poerua_triploid":4491,	">$Kaniere_triploid":4501.66666667,	">$Waik_lane4_TCCTGAGC_trimmed_paired_contig_237":4494.16666667,	">$Brunner_2_4n":4541.91666674,	">$Brunner_6_3n":4545.8333334,	">$Grasmere_1_4n":4737.00000037,	">$Grasmere_6_3n":4501.83333335,	">$Poerua_72_4n":4558.08333342,	">$Rotoiti_1_4n":4535.25000005,	">$*Kaniere_1_2n":4489.33333333,	">$*Ianthe_lane1_TAAGGCGA_trimmed_paired_contig_309":4494,	">$*Yellow_Contig_56":4494.33333333,	">$*Alexsex":4494.33333333,	">$*AlexMap":4494.33333333,	">$*Lady":4494.33333333,	">$*Ianthe":4493.33333333,	">$*Rotoroa_1_2n":4530.33333338}
    C7Sites = {">$Duluth":3873.77083333,	">$Heron2":3870.66666667,	">$McGregor":3870,	">$Waik36":3879.91666667,	">$WalesC":3880.58333333,	">$clone_1":3871.66666667,	">$AC51":3870.66666667,	">$Heron_mitochondrion":3870.33333333,	">$clone_7":3872.10416667,	">$Waik37":3874.25,	">$Gunn":3872.33333333,	">$DenmarkA":3871.625,	">$Waik372":3875.91666667,	">$Tarawera":3874.58333333,	">$Poerua_triploid":3872.66666667,	">$Kaniere_triploid":3875.91666667,	">$Waik_lane4_TCCTGAGC_trimmed_paired_contig_237":3870.29166667,	">$Brunner_2_4n":3832.85416667,	">$Brunner_6_3n":3825.79166667,	">$Grasmere_1_4n":3635.33333333,	">$Grasmere_6_3n":3860.45833333,	">$Poerua_72_4n":3801.89583333,	">$Rotoiti_1_4n":3832.9375,	">$*Kaniere_1_2n":3871.66666667,	">$*Ianthe_lane1_TAAGGCGA_trimmed_paired_contig_309":3873.66666667,	">$*Yellow_Contig_56":3877,	">$*Alexsex":3877,	">$*AlexMap":3877,	">$*Lady":3869,	">$*Ianthe":3872.33333333,	">$*Rotoroa_1_2n":3832.58333333}
    R7Sites = {">$Duluth":4748.70833333,	">$Heron2":4745.33333333,	">$McGregor":4745,	">$Waik36":4747.16666667,	">$WalesC":4748.5,	">$clone_1":4744.33333333,	">$AC51":4745,	">$Heron_mitochondrion":4744.66666667,	">$clone_7":4749.04166667,	">$Waik37":4753.16666667,	">$Gunn":4744,	">$DenmarkA":4749.25,	">$Waik372":4748.83333333,	">$Tarawera":4752.83333333,	">$Poerua_triploid":4744.33333333,	">$Kaniere_triploid":4751.5,	">$Waik_lane4_TCCTGAGC_trimmed_paired_contig_237":4749.91666667,	">$Brunner_2_4n":4787.54166659,	">$Brunner_6_3n":4795.24999994,	">$Grasmere_1_4n":4949.99999963,	">$Grasmere_6_3n":4753.91666665,	">$Poerua_72_4n":4806.62499992,	">$Rotoiti_1_4n":4786.70833328,	">$*Kaniere_1_2n":4744,	">$*Ianthe_lane1_TAAGGCGA_trimmed_paired_contig_309":4745.33333333,	">$*Yellow_Contig_56":4744.66666667,	">$*Alexsex":4744.66666667,	">$*AlexMap":4744.66666667,	">$*Lady":4746.33333333,	">$*Ianthe":4744.66666667,	">$*Rotoroa_1_2n":4782.83333329}
    meanCSites = {">$Duluth":4310.80952381,	">$Heron2":4307.57142857143,	">$McGregor":4307.14285714286,	">$Waik36":4313.14285714286,	">$WalesC":4314.99999999857,	">$clone_1":4307.80952381,	">$AC51":4307.04761904857,	">$Heron_mitochondrion":4307.04761904714,	">$clone_7":4310.19047619,	">$Waik37":4311.76190476143,	">$Gunn":4308.57142857,	">$DenmarkA":4310.04761904714,	">$Waik372":4314.52380952286,	">$Tarawera":4312.28571428429,	">$Poerua_triploid":4308.90476190571,	">$Kaniere_triploid":4312.80952380857,	">$Waik_lane4_TCCTGAGC_trimmed_paired_contig_237":4308.85714285857,	">$Brunner_2_4n":4273.47619044429,	">$Brunner_6_3n":4277.52380949714,	">$Grasmere_1_4n":4132.47619031857,	">$Grasmere_6_3n":4299.99999999429,	">$Poerua_72_4n":4263.99999996286,	">$Rotoiti_1_4n":4283.76190474143,	">$*Kaniere_1_2n":4308.23809523714,	">$*Ianthe_lane1_TAAGGCGA_trimmed_paired_contig_309":4309.19047619,	">$*Yellow_Contig_56":4311,	">$*Alexsex":4311,	">$*AlexMap":4311,	">$*Lady":4307.52380952286,	">$*Ianthe":4308.52380952286,	">$*Rotoroa_1_2n":4280.80952379}
    meanRSites = {">$Duluth":4311.66964285714,	">$Heron2":4308.42857142857,	">$McGregor":4307.85714285714,	">$Waik36":4313.94047619,	">$WalesC":4314.08333333143,	">$clone_1":4308.19047619,	">$AC51":4308.61904762,	">$Heron_mitochondrion":4307.95238095286,	">$clone_7":4310.95535714286,	">$Waik37":4315.65476190571,	">$Gunn":4307.76190476143,	">$DenmarkA":4310.82738095286,	">$Waik372":4310.22619047714,	">$Tarawera":4315.13095238,	">$Poerua_triploid":4308.09523809429,	">$Kaniere_triploid":4314.60714285714,	">$Waik_lane4_TCCTGAGC_trimmed_paired_contig_237":4311.35119047714,	">$Brunner_2_4n":4346.91964284714,	">$Brunner_6_3n":4343.51785713429,	">$Grasmere_1_4n":4452.85714280429,	">$Grasmere_6_3n":4314.37499999857,	">$Poerua_72_4n":4344.52083332286,	">$Rotoiti_1_4n":4335.88392856429,	">$*Kaniere_1_2n":4307.42857142714,	">$*Ianthe_lane1_TAAGGCGA_trimmed_paired_contig_309":4309.80952381,	">$*Yellow_Contig_56":4310.66666666571,	">$*Alexsex":4310.66666666571,	">$*AlexMap":4310.66666666571,	">$*Lady":4307.80952380714,	">$*Ianthe":4308.47619047714,	">$*Rotoroa_1_2n":4334.60714285143}
    D1 = {'mean':[],1:[],2:[],3:[],4:[],5:[],6:[],7:[]}#πC/πS
    D2 = {'mean':[],1:[],2:[],3:[],4:[],5:[],6:[],7:[]}#πR/πS
    D3 = {'mean':[],1:[],2:[],3:[],4:[],5:[],6:[],7:[]}#thetaC/thetaS
    D4 = {'mean':[],1:[],2:[],3:[],4:[],5:[],6:[],7:[]}#thetaR/thetaS
    D5 = {'piS':[]} #πS
    logfile = open('mt_nullDistribution_IantheAnalysis.log','w')
    for seq in seqList:
        if '$' in seq:
            popList.append(seq)
        else:
            outList.append(seq)
    seqNums = range(len(popList))
    currPCT = 0
    sexN = 6
    asexN = 16
    sexAn = aN(sexN)
    asexAn = aN(asexN)
    logfile.write('Calculating population genetic parameters:\n')
    logfile.close()
    while len(D1['mean']) < 10000:
        newPCT = int(round(100*len(D1['mean'])/10000.0))
        if newPCT > currPCT:
            logfile = open('mt_nullDistribution_πS.log','a')
            logfile.write('\t' + str(newPCT) + '% complete\n')
            logfile.close()
            currPCT = newPCT
        sexList = []
        asexList = []
        while len(sexList) < sexN:
            currNum = random.choice(seqNums)
            if popList[currNum] not in sexList:
                sexList.append(popList[currNum])
        while len(asexList) < asexN:
            currNum = random.choice(seqNums)
            if popList[currNum] not in asexList and popList[currNum] not in sexList:
                asexList.append(popList[currNum])
        sexSynSites = 0.0
        asexSynSites = 0.0
        sexC1Sites = 0.0
        sexC2Sites = 0.0
        sexC3Sites = 0.0
        sexC4Sites = 0.0
        sexC5Sites = 0.0
        sexC6Sites = 0.0
        sexC7Sites = 0.0
        sexMeanCSites = 0.0
        sexR1Sites = 0.0
        sexR2Sites = 0.0
        sexR3Sites = 0.0
        sexR4Sites = 0.0
        sexR5Sites = 0.0
        sexR6Sites = 0.0
        sexR7Sites = 0.0
        sexMeanRSites = 0.0
        asexC1Sites = 0.0
        asexC2Sites = 0.0
        asexC3Sites = 0.0
        asexC4Sites = 0.0
        asexC5Sites = 0.0
        asexC6Sites = 0.0
        asexC7Sites = 0.0
        asexMeanCSites = 0.0
        asexR1Sites = 0.0
        asexR2Sites = 0.0
        asexR3Sites = 0.0
        asexR4Sites = 0.0
        asexR5Sites = 0.0
        asexR6Sites = 0.0
        asexR7Sites = 0.0
        asexMeanRSites = 0.0
        for sexual in sexList:
            sexSynSites += synSites[sexual]
            sexC1Sites += C1Sites[sexual]
            sexC2Sites += C2Sites[sexual]
            sexC3Sites += C3Sites[sexual]
            sexC4Sites += C4Sites[sexual]
            sexC5Sites += C5Sites[sexual]
            sexC6Sites += C6Sites[sexual]
            sexC7Sites += C7Sites[sexual]
            sexMeanCSites += meanCSites[sexual] 
            sexR1Sites += R1Sites[sexual]
            sexR2Sites += R2Sites[sexual]
            sexR3Sites += R3Sites[sexual]
            sexR4Sites += R4Sites[sexual]
            sexR5Sites += R5Sites[sexual]
            sexR6Sites += R6Sites[sexual]
            sexR7Sites += R7Sites[sexual]
            sexMeanRSites += meanRSites[sexual]
        for asexual in asexList:
            asexSynSites += synSites[asexual]
            asexC1Sites += C1Sites[asexual]
            asexC2Sites += C2Sites[asexual]
            asexC3Sites += C3Sites[asexual]
            asexC4Sites += C4Sites[asexual]
            asexC5Sites += C5Sites[asexual]
            asexC6Sites += C6Sites[asexual]
            asexC7Sites += C7Sites[asexual]
            asexMeanCSites += meanCSites[asexual] 
            asexR1Sites += R1Sites[asexual]
            asexR2Sites += R2Sites[asexual]
            asexR3Sites += R3Sites[asexual]
            asexR4Sites += R4Sites[asexual]
            asexR5Sites += R5Sites[asexual]
            asexR6Sites += R6Sites[asexual]
            asexR7Sites += R7Sites[asexual]
            asexMeanRSites += meanRSites[asexual]
        asexSynSites /= len(asexList)
        asexC1Sites /= len(asexList)
        asexC2Sites /= len(asexList)
        asexC3Sites /= len(asexList)
        asexC4Sites /= len(asexList)
        asexC5Sites /= len(asexList)
        asexC6Sites /= len(asexList)
        asexC7Sites /= len(asexList)
        asexMeanCSites /= len(asexList)
        asexR1Sites /= len(asexList)
        asexR2Sites /= len(asexList)
        asexR3Sites /= len(asexList)
        asexR4Sites /= len(asexList)
        asexR5Sites /= len(asexList)
        asexR6Sites /= len(asexList)
        asexR7Sites /= len(asexList)
        asexMeanRSites /= len(asexList)
        sexSynSites /= len(sexList)
        sexC1Sites /= len(sexList)
        sexC2Sites /= len(sexList)
        sexC3Sites /= len(sexList)
        sexC4Sites /= len(sexList)
        sexC5Sites /= len(sexList)
        sexC6Sites /= len(sexList)
        sexC7Sites /= len(sexList)
        sexMeanCSites /= len(sexList)
        sexR1Sites /= len(sexList)
        sexR2Sites /= len(sexList)
        sexR3Sites /= len(sexList)
        sexR4Sites /= len(sexList)
        sexR5Sites /= len(sexList)
        sexR6Sites /= len(sexList)
        sexR7Sites /= len(sexList)
        sexMeanRSites /= len(sexList)
        refSeq = seqDict[sexList[0]]
        outSeq = seqDict[outList[0]]
        outCodons = codonDict[outList[0]]
        sex_sum2PQ_S = 0
        sex_sum2PQ_N = 0
        sex_sum2PQ_C1 = 0
        sex_sum2PQ_C2 = 0
        sex_sum2PQ_C3 = 0
        sex_sum2PQ_C4 = 0
        sex_sum2PQ_C5 = 0
        sex_sum2PQ_C6 = 0
        sex_sum2PQ_C7 = 0
        sex_sum2PQ_R1 = 0
        sex_sum2PQ_R2 = 0
        sex_sum2PQ_R3 = 0
        sex_sum2PQ_R4 = 0
        sex_sum2PQ_R5 = 0
        sex_sum2PQ_R6 = 0
        sex_sum2PQ_R7 = 0
        sex_sum2PQ_meanC = 0
        sex_sum2PQ_meanR = 0
        sex_synS = 0
        sex_nsynS = 0
        sex_con1S = 0
        sex_con2S = 0
        sex_con3S = 0
        sex_con4S = 0
        sex_con5S = 0
        sex_con6S = 0
        sex_con7S = 0
        sex_meanConS = 0
        sex_rad1S = 0
        sex_rad2S = 0
        sex_rad3S = 0
        sex_rad4S = 0
        sex_rad5S = 0
        sex_rad6S = 0
        sex_rad7S = 0
        sex_meanRadS = 0
        i = 0
        while i < len(codonDict[seqList[0]]):
            outCodon = outCodons[i]
            gene = False
            for locus in positionDict:
                start = locus[0]
                stop = locus[1]
                if i*3 >= start and i*3 <= stop:
                    gene = positionDict[locus]
            currAlleleDict = {}
            currAlleleList = []
            currAADict = {}
            for seq in sexList:
                currCodons = codonDict[seq]
                currCodon = currCodons[i]
                if currCodon not in currAlleleDict and 'N' not in currCodon and '-' not in currCodon:
                    currAlleleDict[currCodon] = 1
                    currAlleleList.append(currCodon)
                elif 'N' not in currCodon and '-' not in currCodon:
                    currValue = currAlleleDict[currCodon]
                    currValue += 1
                    currAlleleDict[currCodon] = currValue
            if len(currAlleleDict) > 1:
                totalIndividuals = 0
                site1 = []
                site2 = []
                site3 = []
                for codon in currAlleleList:
                    totalIndividuals += currAlleleDict[codon]
                    if codon[0] not in site1:
                        site1.append(codon[0])
                    if codon[1] not in site2:
                        site2.append(codon[1])
                    if codon[2] not in site3:
                        site3.append(codon[2])
                currFreqDict = {}
                totalChanges = (len(site1) - 1) + (len(site2) - 1) + (len(site3) - 1)
                variableSites = []
                if len(site1) > 1:
                    variableSites.append(i*3)
                if len(site2) > 1:
                    variableSites.append((i*3) + 1)
                if len(site3) > 1:
                    variableSites.append((i*3) + 1)
                aaList = []
                twoPQ = 2
                for codon in currAlleleDict:
                    freq = float(currAlleleDict[codon])/totalIndividuals
                    currFreqDict[codon] = freq
                    if i == 0 and codon in startCodons:
                        aa = 'M'
                    else:
                        aa = geneticCode[codon]
                    currAADict[codon] = aa
                    if aa not in aaList:
                        aaList.append(aa)
                if totalChanges == 1:
                    for codon in currAlleleDict:
                        freq = float(currAlleleDict[codon])/totalIndividuals
                        currFreqDict[codon] = freq
                        twoPQ *= freq
                    if len(aaList) == 1:
                        sex_synS += 1
                        sex_sum2PQ_S += twoPQ
                    else:
                        sex_nsynS += 1
                        sex_sum2PQ_N += twoPQ
                        mutType = CRI(aaList) #[1,2,3,4,5,6,7,cri]
                        if mutType[0] == 0:
                            sex_con1S += 1
                            sex_sum2PQ_C1 += twoPQ
                        else:
                            sex_rad1S += 1
                            sex_sum2PQ_R1 += twoPQ
                        if mutType[1] == 0:
                            sex_con2S += 1
                            sex_sum2PQ_C2 += twoPQ
                        else:
                            sex_rad2S += 1
                            sex_sum2PQ_R2 += twoPQ
                        if mutType[2] == 0:
                            sex_con3S += 1
                            sex_sum2PQ_C3 += twoPQ
                        else:
                            sex_rad3S += 1
                            sex_sum2PQ_R3 += twoPQ
                        if mutType[3] == 0:
                            sex_con4S += 1
                            sex_sum2PQ_C4 += twoPQ
                        else:
                            sex_rad4S += 1
                            sex_sum2PQ_R4 += twoPQ
                        if mutType[4] == 0:
                            sex_con5S += 1
                            sex_sum2PQ_C5 += twoPQ
                        else:
                            sex_rad5S += 1
                            sex_sum2PQ_R5 += twoPQ
                        if mutType[5] == 0:
                            sex_con6S += 1
                            sex_sum2PQ_C6 += twoPQ
                        else:
                            sex_rad6S += 1
                            sex_sum2PQ_R6 += twoPQ
                        if mutType[6] == 0:
                            sex_con7S += 1
                            sex_sum2PQ_C7 += twoPQ
                        else:
                            sex_rad7S += 1
                            sex_sum2PQ_R7 += twoPQ
                        if mutType[7] <= 0.5:
                            sex_meanConS += 1
                            sex_sum2PQ_meanC += twoPQ
                        else:
                            sex_meanRadS += 1
                            sex_sum2PQ_meanR += twoPQ
                elif totalChanges == 2:
                    if len(currAlleleDict) == 3:
                        ab = 0
                        ac = 0
                        bc = 0
                        codonA = currAlleleList[0]
                        codonB = currAlleleList[1]
                        codonC = currAlleleList[2]
                        if codonA[0] != codonB[0]:
                            ab += 1
                        if codonA[1] != codonB[1]:
                            ab += 1
                        if codonA[2] != codonB[2]:
                            ab += 1
                        if codonA[0] != codonC[0]:
                            ac += 1
                        if codonA[1] != codonC[1]:
                            ac += 1
                        if codonA[2] != codonC[2]:
                            ac += 1
                        if codonC[0] != codonB[0]:
                            bc += 1
                        if codonC[1] != codonB[1]:
                            bc += 1
                        if codonC[2] != codonB[2]:
                            bc += 1
                        if ab == ac and ac == bc:
                            if 'N' not in outCodon and '-' not in outCodon:
                                if outCodon == codonA:
                                    aaList1 = [currAADict[codonA],currAADict[codonB]]
                                    aaList2 = [currAADict[codonA],currAADict[codonC]]
                                    codonList1 = [codonA,codonB]
                                    codonList2 = [codonA,codonC]
                                    if aaList1[0] == aaList1[1]:
                                        if aaList2[0] == aaList2[1]:
                                            sex_synS += 2
                                            twoPQ = 4
                                            for allele in currFreqDict:
                                                twoPQ *= currFreqDict[allele]
                                            sex_sum2PQ_S += twoPQ
                                        else:
                                            twoPQ1 = 2*currFreqDict[codonList1[1]]*(1-currFreqDict[codonList1[1]]) #syn 
                                            twoPQ2 = 2*currFreqDict[codonList2[1]]*(1-currFreqDict[codonList2[1]]) #nsyn
                                            sex_sum2PQ_S += twoPQ1
                                            sex_sum2PQ_N += twoPQ2
                                            sex_synS += 1
                                            sex_nsynS += 1
                                            mutType = CRI(aaList2) #[1,2,3,4,5,6,7,cri]
                                            if mutType[0] == 0:
                                                sex_con1S += 1
                                                sex_sum2PQ_C1 += twoPQ2
                                            else:
                                                sex_rad1S += 1
                                                sex_sum2PQ_R1 += twoPQ2
                                            if mutType[1] == 0:
                                                sex_con2S += 1
                                                sex_sum2PQ_C2 += twoPQ2
                                            else:
                                                sex_rad2S += 1
                                                sex_sum2PQ_R2 += twoPQ2
                                            if mutType[2] == 0:
                                                sex_con3S += 1
                                                sex_sum2PQ_C3 += twoPQ2
                                            else:
                                                sex_rad3S += 1
                                                sex_sum2PQ_R3 += twoPQ2
                                            if mutType[3] == 0:
                                                sex_con4S += 1
                                                sex_sum2PQ_C4 += twoPQ2
                                            else:
                                                sex_rad4S += 1
                                                sex_sum2PQ_R4 += twoPQ2
                                            if mutType[4] == 0:
                                                sex_con5S += 1
                                                sex_sum2PQ_C5 += twoPQ2
                                            else:
                                                sex_rad5S += 1
                                                sex_sum2PQ_R5 += twoPQ2
                                            if mutType[5] == 0:
                                                sex_con6S += 1
                                                sex_sum2PQ_C6 += twoPQ2
                                            else:
                                                sex_rad6S += 1
                                                sex_sum2PQ_R6 += twoPQ2
                                            if mutType[6] == 0:
                                                sex_con7S += 1
                                                sex_sum2PQ_C7 += twoPQ2
                                            else:
                                                sex_rad7S += 1
                                                sex_sum2PQ_R7 += twoPQ2
                                            if mutType[7] <= 0.5:
                                                sex_meanConS += 1
                                                sex_sum2PQ_meanC += twoPQ2
                                            else:
                                                sex_meanRadS += 1
                                                sex_sum2PQ_meanR += twoPQ2
                                    elif aaList2[0] == aaList2[1]:
                                        sex_nsynS += 1
                                        sex_synS += 1
                                        twoPQ1 = 2*currFreqDict[codonList1[1]]*(1-currFreqDict[codonList1[1]]) #nsyn 
                                        twoPQ2 = 2*currFreqDict[codonList2[1]]*(1-currFreqDict[codonList2[1]]) #syn
                                        sex_sum2PQ_S += twoPQ2
                                        sex_sum2PQ_N += twoPQ1
                                        mutType = CRI(aaList1) #[1,2,3,4,5,6,7,cri]
                                        if mutType[0] == 0:
                                            sex_con1S += 1
                                            sex_sum2PQ_C1 += twoPQ1
                                        else:
                                            sex_rad1S += 1
                                            sex_sum2PQ_R1 += twoPQ1
                                        if mutType[1] == 0:
                                            sex_con2S += 1
                                            sex_sum2PQ_C2 += twoPQ1
                                        else:
                                            sex_rad2S += 1
                                            sex_sum2PQ_R2 += twoPQ1
                                        if mutType[2] == 0:
                                            sex_con3S += 1
                                            sex_sum2PQ_C3 += twoPQ1
                                        else:
                                            sex_rad3S += 1
                                            sex_sum2PQ_R3 += twoPQ1
                                        if mutType[3] == 0:
                                            sex_con4S += 1
                                            sex_sum2PQ_C4 += twoPQ1
                                        else:
                                            sex_rad4S += 1
                                            sex_sum2PQ_R4 += twoPQ1
                                        if mutType[4] == 0:
                                            sex_con5S += 1
                                            sex_sum2PQ_C5 += twoPQ1
                                        else:
                                            sex_rad5S += 1
                                            sex_sum2PQ_R5 += twoPQ1
                                        if mutType[5] == 0:
                                            sex_con6S += 1
                                            sex_sum2PQ_C6 += twoPQ1
                                        else:
                                            sex_rad6S += 1
                                            sex_sum2PQ_R6 += twoPQ1
                                        if mutType[6] == 0:
                                            sex_con7S += 1
                                            sex_sum2PQ_C7 += twoPQ1
                                        else:
                                            sex_rad7S += 1
                                            sex_sum2PQ_R7 += twoPQ1
                                        if mutType[7] <= 0.5:
                                            sex_meanConS += 1
                                            sex_sum2PQ_meanC += twoPQ1
                                        else:
                                            sex_meanRadS += 1
                                            sex_sum2PQ_meanR += twoPQ1
                                    else:
                                        sex_nsynS += 2
                                        twoPQ1 = 2*currFreqDict[codonList1[1]]*(1-currFreqDict[codonList1[1]]) #nsyn 
                                        twoPQ2 = 2*currFreqDict[codonList2[1]]*(1-currFreqDict[codonList2[1]]) #nsyn
                                        sex_sum2PQ_N += twoPQ1 + twoPQ2
                                        mutType = CRI(aaList1) #[1,2,3,4,5,6,7,cri]
                                        if mutType[0] == 0:
                                            sex_con1S += 1
                                            sex_sum2PQ_C1 += twoPQ1
                                        else:
                                            sex_rad1S += 1
                                            sex_sum2PQ_R1 += twoPQ1
                                        if mutType[1] == 0:
                                            sex_con2S += 1
                                            sex_sum2PQ_C2 += twoPQ1
                                        else:
                                            sex_rad2S += 1
                                            sex_sum2PQ_R2 += twoPQ1
                                        if mutType[2] == 0:
                                            sex_con3S += 1
                                            sex_sum2PQ_C3 += twoPQ1
                                        else:
                                            sex_rad3S += 1
                                            sex_sum2PQ_R3 += twoPQ1
                                        if mutType[3] == 0:
                                            sex_con4S += 1
                                            sex_sum2PQ_C4 += twoPQ1
                                        else:
                                            sex_rad4S += 1
                                            sex_sum2PQ_R4 += twoPQ1
                                        if mutType[4] == 0:
                                            sex_con5S += 1
                                            sex_sum2PQ_C5 += twoPQ1
                                        else:
                                            sex_rad5S += 1
                                            sex_sum2PQ_R5 += twoPQ1
                                        if mutType[5] == 0:
                                            sex_con6S += 1
                                            sex_sum2PQ_C6 += twoPQ1
                                        else:
                                            sex_rad6S += 1
                                            sex_sum2PQ_R6 += twoPQ1
                                        if mutType[6] == 0:
                                            sex_con7S += 1
                                            sex_sum2PQ_C7 += twoPQ1
                                        else:
                                            sex_rad7S += 1
                                            sex_sum2PQ_R7 += twoPQ1
                                        if mutType[7] <= 0.5:
                                            sex_meanConS += 1
                                            sex_sum2PQ_meanC += twoPQ1
                                        else:
                                            sex_meanRadS += 1
                                            sex_sum2PQ_meanR += twoPQ1
                                        mutType = CRI(aaList2) #[1,2,3,4,5,6,7,cri]
                                        if mutType[0] == 0:
                                            sex_con1S += 1
                                            sex_sum2PQ_C1 += twoPQ2
                                        else:
                                            sex_rad1S += 1
                                            sex_sum2PQ_R1 += twoPQ2
                                        if mutType[1] == 0:
                                            sex_con2S += 1
                                            sex_sum2PQ_C2 += twoPQ2
                                        else:
                                            sex_rad2S += 1
                                            sex_sum2PQ_R2 += twoPQ2
                                        if mutType[2] == 0:
                                            sex_con3S += 1
                                            sex_sum2PQ_C3 += twoPQ2
                                        else:
                                            sex_rad3S += 1
                                            sex_sum2PQ_R3 += twoPQ2
                                        if mutType[3] == 0:
                                            sex_con4S += 1
                                            sex_sum2PQ_C4 += twoPQ2
                                        else:
                                            sex_rad4S += 1
                                            sex_sum2PQ_R4 += twoPQ2
                                        if mutType[4] == 0:
                                            sex_con5S += 1
                                            sex_sum2PQ_C5 += twoPQ2
                                        else:
                                            sex_rad5S += 1
                                            sex_sum2PQ_R5 += twoPQ2
                                        if mutType[5] == 0:
                                            sex_con6S += 1
                                            sex_sum2PQ_C6 += twoPQ2
                                        else:
                                            sex_rad6S += 1
                                            sex_sum2PQ_R6 += twoPQ2
                                        if mutType[6] == 0:
                                            sex_con7S += 1
                                            sex_sum2PQ_C7 += twoPQ2
                                        else:
                                            sex_rad7S += 1
                                            sex_sum2PQ_R7 += twoPQ2
                                        if mutType[7] <= 0.5:
                                            sex_meanConS += 1
                                            sex_sum2PQ_meanC += twoPQ2
                                        else:
                                            sex_meanRadS += 1
                                            sex_sum2PQ_meanR += twoPQ2
                                elif outCodon == codonB:
                                    aaList1 = [currAADict[codonB],currAADict[codonA]]
                                    aaList2 = [currAADict[codonB],currAADict[codonC]]
                                    codonList1 = [codonB,codonA]
                                    codonList2 = [codonB,codonC]
                                    if aaList1[0] == aaList1[1]:
                                        if aaList2[0] == aaList2[1]:
                                            sex_synS += 2
                                            twoPQ = 4
                                            for allele in currFreqDict:
                                                twoPQ *= currFreqDict[allele]
                                            sex_sum2PQ_S += twoPQ
                                        else:
                                            twoPQ1 = 2*currFreqDict[codonList1[1]]*(1-currFreqDict[codonList1[1]]) #syn 
                                            twoPQ2 = 2*currFreqDict[codonList2[1]]*(1-currFreqDict[codonList2[1]]) #nsyn
                                            sex_sum2PQ_S += twoPQ1
                                            sex_sum2PQ_N += twoPQ2
                                            sex_synS += 1
                                            sex_nsynS += 1
                                            mutType = CRI(aaList2) #[1,2,3,4,5,6,7,cri]
                                            if mutType[0] == 0:
                                                sex_con1S += 1
                                                sex_sum2PQ_C1 += twoPQ2
                                            else:
                                                sex_rad1S += 1
                                                sex_sum2PQ_R1 += twoPQ2
                                            if mutType[1] == 0:
                                                sex_con2S += 1
                                                sex_sum2PQ_C2 += twoPQ2
                                            else:
                                                sex_rad2S += 1
                                                sex_sum2PQ_R2 += twoPQ2
                                            if mutType[2] == 0:
                                                sex_con3S += 1
                                                sex_sum2PQ_C3 += twoPQ2
                                            else:
                                                sex_rad3S += 1
                                                sex_sum2PQ_R3 += twoPQ2
                                            if mutType[3] == 0:
                                                sex_con4S += 1
                                                sex_sum2PQ_C4 += twoPQ2
                                            else:
                                                sex_rad4S += 1
                                                sex_sum2PQ_R4 += twoPQ2
                                            if mutType[4] == 0:
                                                sex_con5S += 1
                                                sex_sum2PQ_C5 += twoPQ2
                                            else:
                                                sex_rad5S += 1
                                                sex_sum2PQ_R5 += twoPQ2
                                            if mutType[5] == 0:
                                                sex_con6S += 1
                                                sex_sum2PQ_C6 += twoPQ2
                                            else:
                                                sex_rad6S += 1
                                                sex_sum2PQ_R6 += twoPQ2
                                            if mutType[6] == 0:
                                                sex_con7S += 1
                                                sex_sum2PQ_C7 += twoPQ2
                                            else:
                                                sex_rad7S += 1
                                                sex_sum2PQ_R7 += twoPQ2
                                            if mutType[7] <= 0.5:
                                                sex_meanConS += 1
                                                sex_sum2PQ_meanC += twoPQ2
                                            else:
                                                sex_meanRadS += 1
                                                sex_sum2PQ_meanR += twoPQ2
                                    elif aaList2[0] == aaList2[1]:
                                        sex_nsynS += 1
                                        sex_synS += 1
                                        twoPQ1 = 2*currFreqDict[codonList1[1]]*(1-currFreqDict[codonList1[1]]) #nsyn 
                                        twoPQ2 = 2*currFreqDict[codonList2[1]]*(1-currFreqDict[codonList2[1]]) #syn
                                        sex_sum2PQ_S += twoPQ2
                                        sex_sum2PQ_N += twoPQ1
                                        mutType = CRI(aaList1) #[1,2,3,4,5,6,7,cri]
                                        if mutType[0] == 0:
                                            sex_con1S += 1
                                            sex_sum2PQ_C1 += twoPQ1
                                        else:
                                            sex_rad1S += 1
                                            sex_sum2PQ_R1 += twoPQ1
                                        if mutType[1] == 0:
                                            sex_con2S += 1
                                            sex_sum2PQ_C2 += twoPQ1
                                        else:
                                            sex_rad2S += 1
                                            sex_sum2PQ_R2 += twoPQ1
                                        if mutType[2] == 0:
                                            sex_con3S += 1
                                            sex_sum2PQ_C3 += twoPQ1
                                        else:
                                            sex_rad3S += 1
                                            sex_sum2PQ_R3 += twoPQ1
                                        if mutType[3] == 0:
                                            sex_con4S += 1
                                            sex_sum2PQ_C4 += twoPQ1
                                        else:
                                            sex_rad4S += 1
                                            sex_sum2PQ_R4 += twoPQ1
                                        if mutType[4] == 0:
                                            sex_con5S += 1
                                            sex_sum2PQ_C5 += twoPQ1
                                        else:
                                            sex_rad5S += 1
                                            sex_sum2PQ_R5 += twoPQ1
                                        if mutType[5] == 0:
                                            sex_con6S += 1
                                            sex_sum2PQ_C6 += twoPQ1
                                        else:
                                            sex_rad6S += 1
                                            sex_sum2PQ_R6 += twoPQ1
                                        if mutType[6] == 0:
                                            sex_con7S += 1
                                            sex_sum2PQ_C7 += twoPQ1
                                        else:
                                            sex_rad7S += 1
                                            sex_sum2PQ_R7 += twoPQ1
                                        if mutType[7] <= 0.5:
                                            sex_meanConS += 1
                                            sex_sum2PQ_meanC += twoPQ1
                                        else:
                                            sex_meanRadS += 1
                                            sex_sum2PQ_meanR += twoPQ1
                                    else:
                                        sex_nsynS += 2
                                        twoPQ1 = 2*currFreqDict[codonList1[1]]*(1-currFreqDict[codonList1[1]]) #nsyn 
                                        twoPQ2 = 2*currFreqDict[codonList2[1]]*(1-currFreqDict[codonList2[1]]) #nsyn
                                        sex_sum2PQ_N += twoPQ1 + twoPQ2
                                        mutType = CRI(aaList1) #[1,2,3,4,5,6,7,cri]
                                        if mutType[0] == 0:
                                            sex_con1S += 1
                                            sex_sum2PQ_C1 += twoPQ1
                                        else:
                                            sex_rad1S += 1
                                            sex_sum2PQ_R1 += twoPQ1
                                        if mutType[1] == 0:
                                            sex_con2S += 1
                                            sex_sum2PQ_C2 += twoPQ1
                                        else:
                                            sex_rad2S += 1
                                            sex_sum2PQ_R2 += twoPQ1
                                        if mutType[2] == 0:
                                            sex_con3S += 1
                                            sex_sum2PQ_C3 += twoPQ1
                                        else:
                                            sex_rad3S += 1
                                            sex_sum2PQ_R3 += twoPQ1
                                        if mutType[3] == 0:
                                            sex_con4S += 1
                                            sex_sum2PQ_C4 += twoPQ1
                                        else:
                                            sex_rad4S += 1
                                            sex_sum2PQ_R4 += twoPQ1
                                        if mutType[4] == 0:
                                            sex_con5S += 1
                                            sex_sum2PQ_C5 += twoPQ1
                                        else:
                                            sex_rad5S += 1
                                            sex_sum2PQ_R5 += twoPQ1
                                        if mutType[5] == 0:
                                            sex_con6S += 1
                                            sex_sum2PQ_C6 += twoPQ1
                                        else:
                                            sex_rad6S += 1
                                            sex_sum2PQ_R6 += twoPQ1
                                        if mutType[6] == 0:
                                            sex_con7S += 1
                                            sex_sum2PQ_C7 += twoPQ1
                                        else:
                                            sex_rad7S += 1
                                            sex_sum2PQ_R7 += twoPQ1
                                        if mutType[7] <= 0.5:
                                            sex_meanConS += 1
                                            sex_sum2PQ_meanC += twoPQ1
                                        else:
                                            sex_meanRadS += 1
                                            sex_sum2PQ_meanR += twoPQ1
                                        mutType = CRI(aaList2) #[1,2,3,4,5,6,7,cri]
                                        if mutType[0] == 0:
                                            sex_con1S += 1
                                            sex_sum2PQ_C1 += twoPQ2
                                        else:
                                            sex_rad1S += 1
                                            sex_sum2PQ_R1 += twoPQ2
                                        if mutType[1] == 0:
                                            sex_con2S += 1
                                            sex_sum2PQ_C2 += twoPQ2
                                        else:
                                            sex_rad2S += 1
                                            sex_sum2PQ_R2 += twoPQ2
                                        if mutType[2] == 0:
                                            sex_con3S += 1
                                            sex_sum2PQ_C3 += twoPQ2
                                        else:
                                            sex_rad3S += 1
                                            sex_sum2PQ_R3 += twoPQ2
                                        if mutType[3] == 0:
                                            sex_con4S += 1
                                            sex_sum2PQ_C4 += twoPQ2
                                        else:
                                            sex_rad4S += 1
                                            sex_sum2PQ_R4 += twoPQ2
                                        if mutType[4] == 0:
                                            sex_con5S += 1
                                            sex_sum2PQ_C5 += twoPQ2
                                        else:
                                            sex_rad5S += 1
                                            sex_sum2PQ_R5 += twoPQ2
                                        if mutType[5] == 0:
                                            sex_con6S += 1
                                            sex_sum2PQ_C6 += twoPQ2
                                        else:
                                            sex_rad6S += 1
                                            sex_sum2PQ_R6 += twoPQ2
                                        if mutType[6] == 0:
                                            sex_con7S += 1
                                            sex_sum2PQ_C7 += twoPQ2
                                        else:
                                            sex_rad7S += 1
                                            sex_sum2PQ_R7 += twoPQ2
                                        if mutType[7] <= 0.5:
                                            sex_meanConS += 1
                                            sex_sum2PQ_meanC += twoPQ2
                                        else:
                                            sex_meanRadS += 1
                                            sex_sum2PQ_meanR += twoPQ2
                                elif outCodon == codonC:
                                    aaList1 = [currAADict[codonC],currAADict[codonA]]
                                    aaList2 = [currAADict[codonC],currAADict[codonB]]
                                    codonList1 = [codonA,codonB]
                                    codonList2 = [codonA,codonC]
                                    if aaList1[0] == aaList1[1]:
                                        if aaList2[0] == aaList2[1]:
                                            sex_synS += 2
                                            twoPQ = 4
                                            for allele in currFreqDict:
                                                twoPQ *= currFreqDict[allele]
                                            sex_sum2PQ_S += twoPQ
                                        else:
                                            twoPQ1 = 2*currFreqDict[codonList1[1]]*(1-currFreqDict[codonList1[1]]) #syn 
                                            twoPQ2 = 2*currFreqDict[codonList2[1]]*(1-currFreqDict[codonList2[1]]) #nsyn
                                            sex_sum2PQ_S += twoPQ1
                                            sex_sum2PQ_N += twoPQ2
                                            sex_synS += 1
                                            sex_nsynS += 1
                                            mutType = CRI(aaList2) #[1,2,3,4,5,6,7,cri]
                                            if mutType[0] == 0:
                                                sex_con1S += 1
                                                sex_sum2PQ_C1 += twoPQ2
                                            else:
                                                sex_rad1S += 1
                                                sex_sum2PQ_R1 += twoPQ2
                                            if mutType[1] == 0:
                                                sex_con2S += 1
                                                sex_sum2PQ_C2 += twoPQ2
                                            else:
                                                sex_rad2S += 1
                                                sex_sum2PQ_R2 += twoPQ2
                                            if mutType[2] == 0:
                                                sex_con3S += 1
                                                sex_sum2PQ_C3 += twoPQ2
                                            else:
                                                sex_rad3S += 1
                                                sex_sum2PQ_R3 += twoPQ2
                                            if mutType[3] == 0:
                                                sex_con4S += 1
                                                sex_sum2PQ_C4 += twoPQ2
                                            else:
                                                sex_rad4S += 1
                                                sex_sum2PQ_R4 += twoPQ2
                                            if mutType[4] == 0:
                                                sex_con5S += 1
                                                sex_sum2PQ_C5 += twoPQ2
                                            else:
                                                sex_rad5S += 1
                                                sex_sum2PQ_R5 += twoPQ2
                                            if mutType[5] == 0:
                                                sex_con6S += 1
                                                sex_sum2PQ_C6 += twoPQ2
                                            else:
                                                sex_rad6S += 1
                                                sex_sum2PQ_R6 += twoPQ2
                                            if mutType[6] == 0:
                                                sex_con7S += 1
                                                sex_sum2PQ_C7 += twoPQ2
                                            else:
                                                sex_rad7S += 1
                                                sex_sum2PQ_R7 += twoPQ2
                                            if mutType[7] <= 0.5:
                                                sex_meanConS += 1
                                                sex_sum2PQ_meanC += twoPQ2
                                            else:
                                                sex_meanRadS += 1
                                                sex_sum2PQ_meanR += twoPQ2
                                    elif aaList2[0] == aaList2[1]:
                                        sex_nsynS += 1
                                        sex_synS += 1
                                        twoPQ1 = 2*currFreqDict[codonList1[1]]*(1-currFreqDict[codonList1[1]]) #nsyn 
                                        twoPQ2 = 2*currFreqDict[codonList2[1]]*(1-currFreqDict[codonList2[1]]) #syn
                                        sex_sum2PQ_S += twoPQ2
                                        sex_sum2PQ_N += twoPQ1
                                        mutType = CRI(aaList1) #[1,2,3,4,5,6,7,cri]
                                        if mutType[0] == 0:
                                            sex_con1S += 1
                                            sex_sum2PQ_C1 += twoPQ1
                                        else:
                                            sex_rad1S += 1
                                            sex_sum2PQ_R1 += twoPQ1
                                        if mutType[1] == 0:
                                            sex_con2S += 1
                                            sex_sum2PQ_C2 += twoPQ1
                                        else:
                                            sex_rad2S += 1
                                            sex_sum2PQ_R2 += twoPQ1
                                        if mutType[2] == 0:
                                            sex_con3S += 1
                                            sex_sum2PQ_C3 += twoPQ1
                                        else:
                                            sex_rad3S += 1
                                            sex_sum2PQ_R3 += twoPQ1
                                        if mutType[3] == 0:
                                            sex_con4S += 1
                                            sex_sum2PQ_C4 += twoPQ1
                                        else:
                                            sex_rad4S += 1
                                            sex_sum2PQ_R4 += twoPQ1
                                        if mutType[4] == 0:
                                            sex_con5S += 1
                                            sex_sum2PQ_C5 += twoPQ1
                                        else:
                                            sex_rad5S += 1
                                            sex_sum2PQ_R5 += twoPQ1
                                        if mutType[5] == 0:
                                            sex_con6S += 1
                                            sex_sum2PQ_C6 += twoPQ1
                                        else:
                                            sex_rad6S += 1
                                            sex_sum2PQ_R6 += twoPQ1
                                        if mutType[6] == 0:
                                            sex_con7S += 1
                                            sex_sum2PQ_C7 += twoPQ1
                                        else:
                                            sex_rad7S += 1
                                            sex_sum2PQ_R7 += twoPQ1
                                        if mutType[7] <= 0.5:
                                            sex_meanConS += 1
                                            sex_sum2PQ_meanC += twoPQ1
                                        else:
                                            sex_meanRadS += 1
                                            sex_sum2PQ_meanR += twoPQ1
                                    else:
                                        sex_nsynS += 2
                                        twoPQ1 = 2*currFreqDict[codonList1[1]]*(1-currFreqDict[codonList1[1]]) #nsyn 
                                        twoPQ2 = 2*currFreqDict[codonList2[1]]*(1-currFreqDict[codonList2[1]]) #nsyn
                                        sex_sum2PQ_N += twoPQ1 + twoPQ2
                                        mutType = CRI(aaList1) #[1,2,3,4,5,6,7,cri]
                                        if mutType[0] == 0:
                                            sex_con1S += 1
                                            sex_sum2PQ_C1 += twoPQ1
                                        else:
                                            sex_rad1S += 1
                                            sex_sum2PQ_R1 += twoPQ1
                                        if mutType[1] == 0:
                                            sex_con2S += 1
                                            sex_sum2PQ_C2 += twoPQ1
                                        else:
                                            sex_rad2S += 1
                                            sex_sum2PQ_R2 += twoPQ1
                                        if mutType[2] == 0:
                                            sex_con3S += 1
                                            sex_sum2PQ_C3 += twoPQ1
                                        else:
                                            sex_rad3S += 1
                                            sex_sum2PQ_R3 += twoPQ1
                                        if mutType[3] == 0:
                                            sex_con4S += 1
                                            sex_sum2PQ_C4 += twoPQ1
                                        else:
                                            sex_rad4S += 1
                                            sex_sum2PQ_R4 += twoPQ1
                                        if mutType[4] == 0:
                                            sex_con5S += 1
                                            sex_sum2PQ_C5 += twoPQ1
                                        else:
                                            sex_rad5S += 1
                                            sex_sum2PQ_R5 += twoPQ1
                                        if mutType[5] == 0:
                                            sex_con6S += 1
                                            sex_sum2PQ_C6 += twoPQ1
                                        else:
                                            sex_rad6S += 1
                                            sex_sum2PQ_R6 += twoPQ1
                                        if mutType[6] == 0:
                                            sex_con7S += 1
                                            sex_sum2PQ_C7 += twoPQ1
                                        else:
                                            sex_rad7S += 1
                                            sex_sum2PQ_R7 += twoPQ1
                                        if mutType[7] <= 0.5:
                                            sex_meanConS += 1
                                            sex_sum2PQ_meanC += twoPQ1
                                        else:
                                            sex_meanRadS += 1
                                            sex_sum2PQ_meanR += twoPQ1
                                        mutType = CRI(aaList2) #[1,2,3,4,5,6,7,cri]
                                        if mutType[0] == 0:
                                            sex_con1S += 1
                                            sex_sum2PQ_C1 += twoPQ2
                                        else:
                                            sex_rad1S += 1
                                            sex_sum2PQ_R1 += twoPQ2
                                        if mutType[1] == 0:
                                            sex_con2S += 1
                                            sex_sum2PQ_C2 += twoPQ2
                                        else:
                                            sex_rad2S += 1
                                            sex_sum2PQ_R2 += twoPQ2
                                        if mutType[2] == 0:
                                            sex_con3S += 1
                                            sex_sum2PQ_C3 += twoPQ2
                                        else:
                                            sex_rad3S += 1
                                            sex_sum2PQ_R3 += twoPQ2
                                        if mutType[3] == 0:
                                            sex_con4S += 1
                                            sex_sum2PQ_C4 += twoPQ2
                                        else:
                                            sex_rad4S += 1
                                            sex_sum2PQ_R4 += twoPQ2
                                        if mutType[4] == 0:
                                            sex_con5S += 1
                                            sex_sum2PQ_C5 += twoPQ2
                                        else:
                                            sex_rad5S += 1
                                            sex_sum2PQ_R5 += twoPQ2
                                        if mutType[5] == 0:
                                            sex_con6S += 1
                                            sex_sum2PQ_C6 += twoPQ2
                                        else:
                                            sex_rad6S += 1
                                            sex_sum2PQ_R6 += twoPQ2
                                        if mutType[6] == 0:
                                            sex_con7S += 1
                                            sex_sum2PQ_C7 += twoPQ2
                                        else:
                                            sex_rad7S += 1
                                            sex_sum2PQ_R7 += twoPQ2
                                        if mutType[7] <= 0.5:
                                            sex_meanConS += 1
                                            sex_sum2PQ_meanC += twoPQ2
                                        else:
                                            sex_meanRadS += 1
                                            sex_sum2PQ_meanR += twoPQ2                            
                        else:
                            if ab > ac and ab > bc:
                                codonList1 = [codonC,codonB]
                                codonList2 = [codonC,codonA]
                            elif ac > ab and ac > bc:
                                codonList1 = [codonB,codonA]
                                codonList2 = [codonB,codonC]
                            elif bc > ab and bc > ac:
                                codonList1 = [codonA,codonB]
                                codonList2 = [codonA,codonC]
                            aaList1 = []
                            aaList2 = []
                            for comp in codonList1:
                                if i < 3:
                                    if comp in startCodons:
                                        aaList1.append('M')
                                    else:
                                        aaList1.append(geneticCode[comp])
                                else:
                                    aaList1.append(geneticCode[comp])
                            for comp in codonList2:
                                if i < 3:
                                    if comp in startCodons:
                                        aaList2.append('M')
                                    else:
                                        aaList2.append(geneticCode[comp])
                                else:
                                    aaList2.append(geneticCode[comp])
                            if aaList1[0] == aaList1[1]:
                                if aaList2[0] == aaList2[1]:
                                    sex_synS += 2
                                    twoPQ = 4
                                    for allele in currFreqDict:
                                        twoPQ *= currFreqDict[allele]
                                    sex_sum2PQ_S += twoPQ
                                else:
                                    twoPQ1 = 2*currFreqDict[codonList1[1]]*(1-currFreqDict[codonList1[1]]) #syn 
                                    twoPQ2 = 2*currFreqDict[codonList2[1]]*(1-currFreqDict[codonList2[1]]) #nsyn
                                    sex_sum2PQ_S += twoPQ1
                                    sex_sum2PQ_N += twoPQ2
                                    sex_synS += 1
                                    sex_nsynS += 1
                                    mutType = CRI(aaList2) #[1,2,3,4,5,6,7,cri]
                                    if mutType[0] == 0:
                                        sex_con1S += 1
                                        sex_sum2PQ_C1 += twoPQ2
                                    else:
                                        sex_rad1S += 1
                                        sex_sum2PQ_R1 += twoPQ2
                                    if mutType[1] == 0:
                                        sex_con2S += 1
                                        sex_sum2PQ_C2 += twoPQ2
                                    else:
                                        sex_rad2S += 1
                                        sex_sum2PQ_R2 += twoPQ2
                                    if mutType[2] == 0:
                                        sex_con3S += 1
                                        sex_sum2PQ_C3 += twoPQ2
                                    else:
                                        sex_rad3S += 1
                                        sex_sum2PQ_R3 += twoPQ2
                                    if mutType[3] == 0:
                                        sex_con4S += 1
                                        sex_sum2PQ_C4 += twoPQ2
                                    else:
                                        sex_rad4S += 1
                                        sex_sum2PQ_R4 += twoPQ2
                                    if mutType[4] == 0:
                                        sex_con5S += 1
                                        sex_sum2PQ_C5 += twoPQ2
                                    else:
                                        sex_rad5S += 1
                                        sex_sum2PQ_R5 += twoPQ2
                                    if mutType[5] == 0:
                                        sex_con6S += 1
                                        sex_sum2PQ_C6 += twoPQ2
                                    else:
                                        sex_rad6S += 1
                                        sex_sum2PQ_R6 += twoPQ2
                                    if mutType[6] == 0:
                                        sex_con7S += 1
                                        sex_sum2PQ_C7 += twoPQ2
                                    else:
                                        sex_rad7S += 1
                                        sex_sum2PQ_R7 += twoPQ2
                                    if mutType[7] <= 0.5:
                                        sex_meanConS += 1
                                        sex_sum2PQ_meanC += twoPQ2
                                    else:
                                        sex_meanRadS += 1
                                        sex_sum2PQ_meanR += twoPQ2
                            elif aaList2[0] == aaList2[1]:
                                sex_nsynS += 1
                                sex_synS += 1
                                twoPQ1 = 2*currFreqDict[codonList1[1]]*(1-currFreqDict[codonList1[1]]) #nsyn 
                                twoPQ2 = 2*currFreqDict[codonList2[1]]*(1-currFreqDict[codonList2[1]]) #syn
                                sex_sum2PQ_S += twoPQ2
                                sex_sum2PQ_N += twoPQ1
                                mutType = CRI(aaList1) #[1,2,3,4,5,6,7,cri]
                                if mutType[0] == 0:
                                    sex_con1S += 1
                                    sex_sum2PQ_C1 += twoPQ1
                                else:
                                    sex_rad1S += 1
                                    sex_sum2PQ_R1 += twoPQ1
                                if mutType[1] == 0:
                                    sex_con2S += 1
                                    sex_sum2PQ_C2 += twoPQ1
                                else:
                                    sex_rad2S += 1
                                    sex_sum2PQ_R2 += twoPQ1
                                if mutType[2] == 0:
                                    sex_con3S += 1
                                    sex_sum2PQ_C3 += twoPQ1
                                else:
                                    sex_rad3S += 1
                                    sex_sum2PQ_R3 += twoPQ1
                                if mutType[3] == 0:
                                    sex_con4S += 1
                                    sex_sum2PQ_C4 += twoPQ1
                                else:
                                    sex_rad4S += 1
                                    sex_sum2PQ_R4 += twoPQ1
                                if mutType[4] == 0:
                                    sex_con5S += 1
                                    sex_sum2PQ_C5 += twoPQ1
                                else:
                                    sex_rad5S += 1
                                    sex_sum2PQ_R5 += twoPQ1
                                if mutType[5] == 0:
                                    sex_con6S += 1
                                    sex_sum2PQ_C6 += twoPQ1
                                else:
                                    sex_rad6S += 1
                                    sex_sum2PQ_R6 += twoPQ1
                                if mutType[6] == 0:
                                    sex_con7S += 1
                                    sex_sum2PQ_C7 += twoPQ1
                                else:
                                    sex_rad7S += 1
                                    sex_sum2PQ_R7 += twoPQ1
                                if mutType[7] <= 0.5:
                                    sex_meanConS += 1
                                    sex_sum2PQ_meanC += twoPQ1
                                else:
                                    sex_meanRadS += 1
                                    sex_sum2PQ_meanR += twoPQ1
                            else:
                                sex_nsynS += 2
                                twoPQ1 = 2*currFreqDict[codonList1[1]]*(1-currFreqDict[codonList1[1]]) #nsyn 
                                twoPQ2 = 2*currFreqDict[codonList2[1]]*(1-currFreqDict[codonList2[1]]) #nsyn
                                sex_sum2PQ_N += twoPQ1 + twoPQ2
                                mutType = CRI(aaList1) #[1,2,3,4,5,6,7,cri]
                                if mutType[0] == 0:
                                    sex_con1S += 1
                                    sex_sum2PQ_C1 += twoPQ1
                                else:
                                    sex_rad1S += 1
                                    sex_sum2PQ_R1 += twoPQ1
                                if mutType[1] == 0:
                                    sex_con2S += 1
                                    sex_sum2PQ_C2 += twoPQ1
                                else:
                                    sex_rad2S += 1
                                    sex_sum2PQ_R2 += twoPQ1
                                if mutType[2] == 0:
                                    sex_con3S += 1
                                    sex_sum2PQ_C3 += twoPQ1
                                else:
                                    sex_rad3S += 1
                                    sex_sum2PQ_R3 += twoPQ1
                                if mutType[3] == 0:
                                    sex_con4S += 1
                                    sex_sum2PQ_C4 += twoPQ1
                                else:
                                    sex_rad4S += 1
                                    sex_sum2PQ_R4 += twoPQ1
                                if mutType[4] == 0:
                                    sex_con5S += 1
                                    sex_sum2PQ_C5 += twoPQ1
                                else:
                                    sex_rad5S += 1
                                    sex_sum2PQ_R5 += twoPQ1
                                if mutType[5] == 0:
                                    sex_con6S += 1
                                    sex_sum2PQ_C6 += twoPQ1
                                else:
                                    sex_rad6S += 1
                                    sex_sum2PQ_R6 += twoPQ1
                                if mutType[6] == 0:
                                    sex_con7S += 1
                                    sex_sum2PQ_C7 += twoPQ1
                                else:
                                    sex_rad7S += 1
                                    sex_sum2PQ_R7 += twoPQ1
                                if mutType[7] <= 0.5:
                                    sex_meanConS += 1
                                    sex_sum2PQ_meanC += twoPQ1
                                else:
                                    sex_meanRadS += 1
                                    sex_sum2PQ_meanR += twoPQ1
                                mutType = CRI(aaList2) #[1,2,3,4,5,6,7,cri]
                                if mutType[0] == 0:
                                    sex_con1S += 1
                                    sex_sum2PQ_C1 += twoPQ2
                                else:
                                    sex_rad1S += 1
                                    sex_sum2PQ_R1 += twoPQ2
                                if mutType[1] == 0:
                                    sex_con2S += 1
                                    sex_sum2PQ_C2 += twoPQ2
                                else:
                                    sex_rad2S += 1
                                    sex_sum2PQ_R2 += twoPQ2
                                if mutType[2] == 0:
                                    sex_con3S += 1
                                    sex_sum2PQ_C3 += twoPQ2
                                else:
                                    sex_rad3S += 1
                                    sex_sum2PQ_R3 += twoPQ2
                                if mutType[3] == 0:
                                    sex_con4S += 1
                                    sex_sum2PQ_C4 += twoPQ2
                                else:
                                    sex_rad4S += 1
                                    sex_sum2PQ_R4 += twoPQ2
                                if mutType[4] == 0:
                                    sex_con5S += 1
                                    sex_sum2PQ_C5 += twoPQ2
                                else:
                                    sex_rad5S += 1
                                    sex_sum2PQ_R5 += twoPQ2
                                if mutType[5] == 0:
                                    sex_con6S += 1
                                    sex_sum2PQ_C6 += twoPQ2
                                else:
                                    sex_rad6S += 1
                                    sex_sum2PQ_R6 += twoPQ2
                                if mutType[6] == 0:
                                    sex_con7S += 1
                                    sex_sum2PQ_C7 += twoPQ2
                                else:
                                    sex_rad7S += 1
                                    sex_sum2PQ_R7 += twoPQ2
                                if mutType[7] <= 0.5:
                                    sex_meanConS += 1
                                    sex_sum2PQ_meanC += twoPQ2
                                else:
                                    sex_meanRadS += 1
                                    sex_sum2PQ_meanR += twoPQ2
                    elif len(currAlleleDict) == 2:
                        currFreqDict = {}
                        twoPQ = 2
                        for codon in currAlleleDict:
                            freq = float(currAlleleDict[codon])/totalIndividuals
                            twoPQ *= freq
                            currFreqDict[codon] = freq
                        if len(aaList) == 1:
                            sex_synS += 2
                            sex_sum2PQ_S += (2*twoPQ) 
            i += 1
        asex_sum2PQ_S = 0
        asex_sum2PQ_N = 0
        asex_sum2PQ_C1 = 0
        asex_sum2PQ_C2 = 0
        asex_sum2PQ_C3 = 0
        asex_sum2PQ_C4 = 0
        asex_sum2PQ_C5 = 0
        asex_sum2PQ_C6 = 0
        asex_sum2PQ_C7 = 0
        asex_sum2PQ_R1 = 0
        asex_sum2PQ_R2 = 0
        asex_sum2PQ_R3 = 0
        asex_sum2PQ_R4 = 0
        asex_sum2PQ_R5 = 0
        asex_sum2PQ_R6 = 0
        asex_sum2PQ_R7 = 0
        asex_sum2PQ_meanC = 0
        asex_sum2PQ_meanR = 0
        asex_synS = 0
        asex_nsynS = 0
        asex_con1S = 0
        asex_con2S = 0
        asex_con3S = 0
        asex_con4S = 0
        asex_con5S = 0
        asex_con6S = 0
        asex_con7S = 0
        asex_meanConS = 0
        asex_rad1S = 0
        asex_rad2S = 0
        asex_rad3S = 0
        asex_rad4S = 0
        asex_rad5S = 0
        asex_rad6S = 0
        asex_rad7S = 0
        asex_meanRadS = 0
        i = 0
        while i < len(codonDict[seqList[0]]):
            outCodon = outCodons[i]
            gene = False
            for locus in positionDict:
                start = locus[0]
                stop = locus[1]
                if i*3 >= start and i*3 <= stop:
                    gene = positionDict[locus]
            currAlleleDict = {}
            currAlleleList = []
            currAADict = {}
            for seq in asexList:
                currCodons = codonDict[seq]
                currCodon = currCodons[i]
                if currCodon not in currAlleleDict and 'N' not in currCodon and '-' not in currCodon:
                    currAlleleDict[currCodon] = 1
                    currAlleleList.append(currCodon)
                elif 'N' not in currCodon and '-' not in currCodon:
                    currValue = currAlleleDict[currCodon]
                    currValue += 1
                    currAlleleDict[currCodon] = currValue
            if len(currAlleleDict) > 1:
                totalIndividuals = 0
                site1 = []
                site2 = []
                site3 = []
                for codon in currAlleleList:
                    totalIndividuals += currAlleleDict[codon]
                    if codon[0] not in site1:
                        site1.append(codon[0])
                    if codon[1] not in site2:
                        site2.append(codon[1])
                    if codon[2] not in site3:
                        site3.append(codon[2])
                currFreqDict = {}
                totalChanges = (len(site1) - 1) + (len(site2) - 1) + (len(site3) - 1)
                variableSites = []
                if len(site1) > 1:
                    variableSites.append(i*3)
                if len(site2) > 1:
                    variableSites.append((i*3) + 1)
                if len(site3) > 1:
                    variableSites.append((i*3) + 1)
                aaList = []
                twoPQ = 2
                for codon in currAlleleDict:
                    freq = float(currAlleleDict[codon])/totalIndividuals
                    currFreqDict[codon] = freq
                    if i == 0 and codon in startCodons:
                        aa = 'M'
                    else:
                        aa = geneticCode[codon]
                    currAADict[codon] = aa
                    if aa not in aaList:
                        aaList.append(aa)
                if totalChanges == 1:
                    for codon in currAlleleDict:
                        freq = float(currAlleleDict[codon])/totalIndividuals
                        currFreqDict[codon] = freq
                        twoPQ *= freq
                    if len(aaList) == 1:
                        asex_synS += 1
                        asex_sum2PQ_S += twoPQ
                    else:
                        asex_nsynS += 1
                        asex_sum2PQ_N += twoPQ
                        mutType = CRI(aaList) #[1,2,3,4,5,6,7,cri]
                        if mutType[0] == 0:
                            asex_con1S += 1
                            asex_sum2PQ_C1 += twoPQ
                        else:
                            asex_rad1S += 1
                            asex_sum2PQ_R1 += twoPQ
                        if mutType[1] == 0:
                            asex_con2S += 1
                            asex_sum2PQ_C2 += twoPQ
                        else:
                            asex_rad2S += 1
                            asex_sum2PQ_R2 += twoPQ
                        if mutType[2] == 0:
                            asex_con3S += 1
                            asex_sum2PQ_C3 += twoPQ
                        else:
                            asex_rad3S += 1
                            asex_sum2PQ_R3 += twoPQ
                        if mutType[3] == 0:
                            asex_con4S += 1
                            asex_sum2PQ_C4 += twoPQ
                        else:
                            asex_rad4S += 1
                            asex_sum2PQ_R4 += twoPQ
                        if mutType[4] == 0:
                            asex_con5S += 1
                            asex_sum2PQ_C5 += twoPQ
                        else:
                            asex_rad5S += 1
                            asex_sum2PQ_R5 += twoPQ
                        if mutType[5] == 0:
                            asex_con6S += 1
                            asex_sum2PQ_C6 += twoPQ
                        else:
                            asex_rad6S += 1
                            asex_sum2PQ_R6 += twoPQ
                        if mutType[6] == 0:
                            asex_con7S += 1
                            asex_sum2PQ_C7 += twoPQ
                        else:
                            asex_rad7S += 1
                            asex_sum2PQ_R7 += twoPQ
                        if mutType[7] <= 0.5:
                            asex_meanConS += 1
                            asex_sum2PQ_meanC += twoPQ
                        else:
                            asex_meanRadS += 1
                            asex_sum2PQ_meanR += twoPQ
                elif totalChanges == 2:
                    if len(currAlleleDict) == 3:
                        ab = 0
                        ac = 0
                        bc = 0
                        codonA = currAlleleList[0]
                        codonB = currAlleleList[1]
                        codonC = currAlleleList[2]
                        if codonA[0] != codonB[0]:
                            ab += 1
                        if codonA[1] != codonB[1]:
                            ab += 1
                        if codonA[2] != codonB[2]:
                            ab += 1
                        if codonA[0] != codonC[0]:
                            ac += 1
                        if codonA[1] != codonC[1]:
                            ac += 1
                        if codonA[2] != codonC[2]:
                            ac += 1
                        if codonC[0] != codonB[0]:
                            bc += 1
                        if codonC[1] != codonB[1]:
                            bc += 1
                        if codonC[2] != codonB[2]:
                            bc += 1
                        if ab == ac and ac == bc:
                            if 'N' not in outCodon and '-' not in outCodon:
                                if outCodon == codonA:
                                    aaList1 = [currAADict[codonA],currAADict[codonB]]
                                    aaList2 = [currAADict[codonA],currAADict[codonC]]
                                    codonList1 = [codonA,codonB]
                                    codonList2 = [codonA,codonC]
                                    if aaList1[0] == aaList1[1]:
                                        if aaList2[0] == aaList2[1]:
                                            asex_synS += 2
                                            twoPQ = 4
                                            for allele in currFreqDict:
                                                twoPQ *= currFreqDict[allele]
                                            asex_sum2PQ_S += twoPQ
                                        else:
                                            twoPQ1 = 2*currFreqDict[codonList1[1]]*(1-currFreqDict[codonList1[1]]) #syn 
                                            twoPQ2 = 2*currFreqDict[codonList2[1]]*(1-currFreqDict[codonList2[1]]) #nsyn
                                            asex_sum2PQ_S += twoPQ1
                                            asex_sum2PQ_N += twoPQ2
                                            asex_synS += 1
                                            asex_nsynS += 1
                                            mutType = CRI(aaList2) #[1,2,3,4,5,6,7,cri]
                                            if mutType[0] == 0:
                                                asex_con1S += 1
                                                asex_sum2PQ_C1 += twoPQ2
                                            else:
                                                asex_rad1S += 1
                                                asex_sum2PQ_R1 += twoPQ2
                                            if mutType[1] == 0:
                                                asex_con2S += 1
                                                asex_sum2PQ_C2 += twoPQ2
                                            else:
                                                asex_rad2S += 1
                                                asex_sum2PQ_R2 += twoPQ2
                                            if mutType[2] == 0:
                                                asex_con3S += 1
                                                asex_sum2PQ_C3 += twoPQ2
                                            else:
                                                asex_rad3S += 1
                                                asex_sum2PQ_R3 += twoPQ2
                                            if mutType[3] == 0:
                                                asex_con4S += 1
                                                asex_sum2PQ_C4 += twoPQ2
                                            else:
                                                asex_rad4S += 1
                                                asex_sum2PQ_R4 += twoPQ2
                                            if mutType[4] == 0:
                                                asex_con5S += 1
                                                asex_sum2PQ_C5 += twoPQ2
                                            else:
                                                asex_rad5S += 1
                                                asex_sum2PQ_R5 += twoPQ2
                                            if mutType[5] == 0:
                                                asex_con6S += 1
                                                asex_sum2PQ_C6 += twoPQ2
                                            else:
                                                asex_rad6S += 1
                                                asex_sum2PQ_R6 += twoPQ2
                                            if mutType[6] == 0:
                                                asex_con7S += 1
                                                asex_sum2PQ_C7 += twoPQ2
                                            else:
                                                asex_rad7S += 1
                                                asex_sum2PQ_R7 += twoPQ2
                                            if mutType[7] <= 0.5:
                                                asex_meanConS += 1
                                                asex_sum2PQ_meanC += twoPQ2
                                            else:
                                                asex_meanRadS += 1
                                                asex_sum2PQ_meanR += twoPQ2
                                    elif aaList2[0] == aaList2[1]:
                                        asex_nsynS += 1
                                        asex_synS += 1
                                        twoPQ1 = 2*currFreqDict[codonList1[1]]*(1-currFreqDict[codonList1[1]]) #nsyn 
                                        twoPQ2 = 2*currFreqDict[codonList2[1]]*(1-currFreqDict[codonList2[1]]) #syn
                                        asex_sum2PQ_S += twoPQ2
                                        asex_sum2PQ_N += twoPQ1
                                        mutType = CRI(aaList1) #[1,2,3,4,5,6,7,cri]
                                        if mutType[0] == 0:
                                            asex_con1S += 1
                                            asex_sum2PQ_C1 += twoPQ1
                                        else:
                                            asex_rad1S += 1
                                            asex_sum2PQ_R1 += twoPQ1
                                        if mutType[1] == 0:
                                            asex_con2S += 1
                                            asex_sum2PQ_C2 += twoPQ1
                                        else:
                                            asex_rad2S += 1
                                            asex_sum2PQ_R2 += twoPQ1
                                        if mutType[2] == 0:
                                            asex_con3S += 1
                                            asex_sum2PQ_C3 += twoPQ1
                                        else:
                                            asex_rad3S += 1
                                            asex_sum2PQ_R3 += twoPQ1
                                        if mutType[3] == 0:
                                            asex_con4S += 1
                                            asex_sum2PQ_C4 += twoPQ1
                                        else:
                                            asex_rad4S += 1
                                            asex_sum2PQ_R4 += twoPQ1
                                        if mutType[4] == 0:
                                            asex_con5S += 1
                                            asex_sum2PQ_C5 += twoPQ1
                                        else:
                                            asex_rad5S += 1
                                            asex_sum2PQ_R5 += twoPQ1
                                        if mutType[5] == 0:
                                            asex_con6S += 1
                                            asex_sum2PQ_C6 += twoPQ1
                                        else:
                                            asex_rad6S += 1
                                            asex_sum2PQ_R6 += twoPQ1
                                        if mutType[6] == 0:
                                            asex_con7S += 1
                                            asex_sum2PQ_C7 += twoPQ1
                                        else:
                                            asex_rad7S += 1
                                            asex_sum2PQ_R7 += twoPQ1
                                        if mutType[7] <= 0.5:
                                            asex_meanConS += 1
                                            asex_sum2PQ_meanC += twoPQ1
                                        else:
                                            asex_meanRadS += 1
                                            asex_sum2PQ_meanR += twoPQ1
                                    else:
                                        asex_nsynS += 2
                                        twoPQ1 = 2*currFreqDict[codonList1[1]]*(1-currFreqDict[codonList1[1]]) #nsyn 
                                        twoPQ2 = 2*currFreqDict[codonList2[1]]*(1-currFreqDict[codonList2[1]]) #nsyn
                                        asex_sum2PQ_N += twoPQ1 + twoPQ2
                                        mutType = CRI(aaList1) #[1,2,3,4,5,6,7,cri]
                                        if mutType[0] == 0:
                                            asex_con1S += 1
                                            asex_sum2PQ_C1 += twoPQ1
                                        else:
                                            asex_rad1S += 1
                                            asex_sum2PQ_R1 += twoPQ1
                                        if mutType[1] == 0:
                                            asex_con2S += 1
                                            asex_sum2PQ_C2 += twoPQ1
                                        else:
                                            asex_rad2S += 1
                                            asex_sum2PQ_R2 += twoPQ1
                                        if mutType[2] == 0:
                                            asex_con3S += 1
                                            asex_sum2PQ_C3 += twoPQ1
                                        else:
                                            asex_rad3S += 1
                                            asex_sum2PQ_R3 += twoPQ1
                                        if mutType[3] == 0:
                                            asex_con4S += 1
                                            asex_sum2PQ_C4 += twoPQ1
                                        else:
                                            asex_rad4S += 1
                                            asex_sum2PQ_R4 += twoPQ1
                                        if mutType[4] == 0:
                                            asex_con5S += 1
                                            asex_sum2PQ_C5 += twoPQ1
                                        else:
                                            asex_rad5S += 1
                                            asex_sum2PQ_R5 += twoPQ1
                                        if mutType[5] == 0:
                                            asex_con6S += 1
                                            asex_sum2PQ_C6 += twoPQ1
                                        else:
                                            asex_rad6S += 1
                                            asex_sum2PQ_R6 += twoPQ1
                                        if mutType[6] == 0:
                                            asex_con7S += 1
                                            asex_sum2PQ_C7 += twoPQ1
                                        else:
                                            asex_rad7S += 1
                                            asex_sum2PQ_R7 += twoPQ1
                                        if mutType[7] <= 0.5:
                                            asex_meanConS += 1
                                            asex_sum2PQ_meanC += twoPQ1
                                        else:
                                            asex_meanRadS += 1
                                            asex_sum2PQ_meanR += twoPQ1
                                        mutType = CRI(aaList2) #[1,2,3,4,5,6,7,cri]
                                        if mutType[0] == 0:
                                            asex_con1S += 1
                                            asex_sum2PQ_C1 += twoPQ2
                                        else:
                                            asex_rad1S += 1
                                            asex_sum2PQ_R1 += twoPQ2
                                        if mutType[1] == 0:
                                            asex_con2S += 1
                                            asex_sum2PQ_C2 += twoPQ2
                                        else:
                                            asex_rad2S += 1
                                            asex_sum2PQ_R2 += twoPQ2
                                        if mutType[2] == 0:
                                            asex_con3S += 1
                                            asex_sum2PQ_C3 += twoPQ2
                                        else:
                                            asex_rad3S += 1
                                            asex_sum2PQ_R3 += twoPQ2
                                        if mutType[3] == 0:
                                            asex_con4S += 1
                                            asex_sum2PQ_C4 += twoPQ2
                                        else:
                                            asex_rad4S += 1
                                            asex_sum2PQ_R4 += twoPQ2
                                        if mutType[4] == 0:
                                            asex_con5S += 1
                                            asex_sum2PQ_C5 += twoPQ2
                                        else:
                                            asex_rad5S += 1
                                            asex_sum2PQ_R5 += twoPQ2
                                        if mutType[5] == 0:
                                            asex_con6S += 1
                                            asex_sum2PQ_C6 += twoPQ2
                                        else:
                                            asex_rad6S += 1
                                            asex_sum2PQ_R6 += twoPQ2
                                        if mutType[6] == 0:
                                            asex_con7S += 1
                                            asex_sum2PQ_C7 += twoPQ2
                                        else:
                                            asex_rad7S += 1
                                            asex_sum2PQ_R7 += twoPQ2
                                        if mutType[7] <= 0.5:
                                            asex_meanConS += 1
                                            asex_sum2PQ_meanC += twoPQ2
                                        else:
                                            asex_meanRadS += 1
                                            asex_sum2PQ_meanR += twoPQ2
                                elif outCodon == codonB:
                                    aaList1 = [currAADict[codonB],currAADict[codonA]]
                                    aaList2 = [currAADict[codonB],currAADict[codonC]]
                                    codonList1 = [codonB,codonA]
                                    codonList2 = [codonB,codonC]
                                    if aaList1[0] == aaList1[1]:
                                        if aaList2[0] == aaList2[1]:
                                            asex_synS += 2
                                            twoPQ = 4
                                            for allele in currFreqDict:
                                                twoPQ *= currFreqDict[allele]
                                            asex_sum2PQ_S += twoPQ
                                        else:
                                            twoPQ1 = 2*currFreqDict[codonList1[1]]*(1-currFreqDict[codonList1[1]]) #syn 
                                            twoPQ2 = 2*currFreqDict[codonList2[1]]*(1-currFreqDict[codonList2[1]]) #nsyn
                                            asex_sum2PQ_S += twoPQ1
                                            asex_sum2PQ_N += twoPQ2
                                            asex_synS += 1
                                            asex_nsynS += 1
                                            mutType = CRI(aaList2) #[1,2,3,4,5,6,7,cri]
                                            if mutType[0] == 0:
                                                asex_con1S += 1
                                                asex_sum2PQ_C1 += twoPQ2
                                            else:
                                                asex_rad1S += 1
                                                asex_sum2PQ_R1 += twoPQ2
                                            if mutType[1] == 0:
                                                asex_con2S += 1
                                                asex_sum2PQ_C2 += twoPQ2
                                            else:
                                                asex_rad2S += 1
                                                asex_sum2PQ_R2 += twoPQ2
                                            if mutType[2] == 0:
                                                asex_con3S += 1
                                                asex_sum2PQ_C3 += twoPQ2
                                            else:
                                                asex_rad3S += 1
                                                asex_sum2PQ_R3 += twoPQ2
                                            if mutType[3] == 0:
                                                asex_con4S += 1
                                                asex_sum2PQ_C4 += twoPQ2
                                            else:
                                                asex_rad4S += 1
                                                asex_sum2PQ_R4 += twoPQ2
                                            if mutType[4] == 0:
                                                asex_con5S += 1
                                                asex_sum2PQ_C5 += twoPQ2
                                            else:
                                                asex_rad5S += 1
                                                asex_sum2PQ_R5 += twoPQ2
                                            if mutType[5] == 0:
                                                asex_con6S += 1
                                                asex_sum2PQ_C6 += twoPQ2
                                            else:
                                                asex_rad6S += 1
                                                asex_sum2PQ_R6 += twoPQ2
                                            if mutType[6] == 0:
                                                asex_con7S += 1
                                                asex_sum2PQ_C7 += twoPQ2
                                            else:
                                                asex_rad7S += 1
                                                asex_sum2PQ_R7 += twoPQ2
                                            if mutType[7] <= 0.5:
                                                asex_meanConS += 1
                                                asex_sum2PQ_meanC += twoPQ2
                                            else:
                                                asex_meanRadS += 1
                                                asex_sum2PQ_meanR += twoPQ2
                                    elif aaList2[0] == aaList2[1]:
                                        asex_nsynS += 1
                                        asex_synS += 1
                                        twoPQ1 = 2*currFreqDict[codonList1[1]]*(1-currFreqDict[codonList1[1]]) #nsyn 
                                        twoPQ2 = 2*currFreqDict[codonList2[1]]*(1-currFreqDict[codonList2[1]]) #syn
                                        asex_sum2PQ_S += twoPQ2
                                        asex_sum2PQ_N += twoPQ1
                                        mutType = CRI(aaList1) #[1,2,3,4,5,6,7,cri]
                                        if mutType[0] == 0:
                                            asex_con1S += 1
                                            asex_sum2PQ_C1 += twoPQ1
                                        else:
                                            asex_rad1S += 1
                                            asex_sum2PQ_R1 += twoPQ1
                                        if mutType[1] == 0:
                                            asex_con2S += 1
                                            asex_sum2PQ_C2 += twoPQ1
                                        else:
                                            asex_rad2S += 1
                                            asex_sum2PQ_R2 += twoPQ1
                                        if mutType[2] == 0:
                                            asex_con3S += 1
                                            asex_sum2PQ_C3 += twoPQ1
                                        else:
                                            asex_rad3S += 1
                                            asex_sum2PQ_R3 += twoPQ1
                                        if mutType[3] == 0:
                                            asex_con4S += 1
                                            asex_sum2PQ_C4 += twoPQ1
                                        else:
                                            asex_rad4S += 1
                                            asex_sum2PQ_R4 += twoPQ1
                                        if mutType[4] == 0:
                                            asex_con5S += 1
                                            asex_sum2PQ_C5 += twoPQ1
                                        else:
                                            asex_rad5S += 1
                                            asex_sum2PQ_R5 += twoPQ1
                                        if mutType[5] == 0:
                                            asex_con6S += 1
                                            asex_sum2PQ_C6 += twoPQ1
                                        else:
                                            asex_rad6S += 1
                                            asex_sum2PQ_R6 += twoPQ1
                                        if mutType[6] == 0:
                                            asex_con7S += 1
                                            asex_sum2PQ_C7 += twoPQ1
                                        else:
                                            asex_rad7S += 1
                                            asex_sum2PQ_R7 += twoPQ1
                                        if mutType[7] <= 0.5:
                                            asex_meanConS += 1
                                            asex_sum2PQ_meanC += twoPQ1
                                        else:
                                            asex_meanRadS += 1
                                            asex_sum2PQ_meanR += twoPQ1
                                    else:
                                        asex_nsynS += 2
                                        twoPQ1 = 2*currFreqDict[codonList1[1]]*(1-currFreqDict[codonList1[1]]) #nsyn 
                                        twoPQ2 = 2*currFreqDict[codonList2[1]]*(1-currFreqDict[codonList2[1]]) #nsyn
                                        asex_sum2PQ_N += twoPQ1 + twoPQ2
                                        mutType = CRI(aaList1) #[1,2,3,4,5,6,7,cri]
                                        if mutType[0] == 0:
                                            asex_con1S += 1
                                            asex_sum2PQ_C1 += twoPQ1
                                        else:
                                            asex_rad1S += 1
                                            asex_sum2PQ_R1 += twoPQ1
                                        if mutType[1] == 0:
                                            asex_con2S += 1
                                            asex_sum2PQ_C2 += twoPQ1
                                        else:
                                            asex_rad2S += 1
                                            asex_sum2PQ_R2 += twoPQ1
                                        if mutType[2] == 0:
                                            asex_con3S += 1
                                            asex_sum2PQ_C3 += twoPQ1
                                        else:
                                            asex_rad3S += 1
                                            asex_sum2PQ_R3 += twoPQ1
                                        if mutType[3] == 0:
                                            asex_con4S += 1
                                            asex_sum2PQ_C4 += twoPQ1
                                        else:
                                            asex_rad4S += 1
                                            asex_sum2PQ_R4 += twoPQ1
                                        if mutType[4] == 0:
                                            asex_con5S += 1
                                            asex_sum2PQ_C5 += twoPQ1
                                        else:
                                            asex_rad5S += 1
                                            asex_sum2PQ_R5 += twoPQ1
                                        if mutType[5] == 0:
                                            asex_con6S += 1
                                            asex_sum2PQ_C6 += twoPQ1
                                        else:
                                            asex_rad6S += 1
                                            asex_sum2PQ_R6 += twoPQ1
                                        if mutType[6] == 0:
                                            asex_con7S += 1
                                            asex_sum2PQ_C7 += twoPQ1
                                        else:
                                            asex_rad7S += 1
                                            asex_sum2PQ_R7 += twoPQ1
                                        if mutType[7] <= 0.5:
                                            asex_meanConS += 1
                                            asex_sum2PQ_meanC += twoPQ1
                                        else:
                                            asex_meanRadS += 1
                                            asex_sum2PQ_meanR += twoPQ1
                                        mutType = CRI(aaList2) #[1,2,3,4,5,6,7,cri]
                                        if mutType[0] == 0:
                                            asex_con1S += 1
                                            asex_sum2PQ_C1 += twoPQ2
                                        else:
                                            asex_rad1S += 1
                                            asex_sum2PQ_R1 += twoPQ2
                                        if mutType[1] == 0:
                                            asex_con2S += 1
                                            asex_sum2PQ_C2 += twoPQ2
                                        else:
                                            asex_rad2S += 1
                                            asex_sum2PQ_R2 += twoPQ2
                                        if mutType[2] == 0:
                                            asex_con3S += 1
                                            asex_sum2PQ_C3 += twoPQ2
                                        else:
                                            asex_rad3S += 1
                                            asex_sum2PQ_R3 += twoPQ2
                                        if mutType[3] == 0:
                                            asex_con4S += 1
                                            asex_sum2PQ_C4 += twoPQ2
                                        else:
                                            asex_rad4S += 1
                                            asex_sum2PQ_R4 += twoPQ2
                                        if mutType[4] == 0:
                                            asex_con5S += 1
                                            asex_sum2PQ_C5 += twoPQ2
                                        else:
                                            asex_rad5S += 1
                                            asex_sum2PQ_R5 += twoPQ2
                                        if mutType[5] == 0:
                                            asex_con6S += 1
                                            asex_sum2PQ_C6 += twoPQ2
                                        else:
                                            asex_rad6S += 1
                                            asex_sum2PQ_R6 += twoPQ2
                                        if mutType[6] == 0:
                                            asex_con7S += 1
                                            asex_sum2PQ_C7 += twoPQ2
                                        else:
                                            asex_rad7S += 1
                                            asex_sum2PQ_R7 += twoPQ2
                                        if mutType[7] <= 0.5:
                                            asex_meanConS += 1
                                            asex_sum2PQ_meanC += twoPQ2
                                        else:
                                            asex_meanRadS += 1
                                            asex_sum2PQ_meanR += twoPQ2
                                elif outCodon == codonC:
                                    aaList1 = [currAADict[codonC],currAADict[codonA]]
                                    aaList2 = [currAADict[codonC],currAADict[codonB]]
                                    codonList1 = [codonA,codonB]
                                    codonList2 = [codonA,codonC]
                                    if aaList1[0] == aaList1[1]:
                                        if aaList2[0] == aaList2[1]:
                                            asex_synS += 2
                                            twoPQ = 4
                                            for allele in currFreqDict:
                                                twoPQ *= currFreqDict[allele]
                                            asex_sum2PQ_S += twoPQ
                                        else:
                                            twoPQ1 = 2*currFreqDict[codonList1[1]]*(1-currFreqDict[codonList1[1]]) #syn 
                                            twoPQ2 = 2*currFreqDict[codonList2[1]]*(1-currFreqDict[codonList2[1]]) #nsyn
                                            asex_sum2PQ_S += twoPQ1
                                            asex_sum2PQ_N += twoPQ2
                                            asex_synS += 1
                                            asex_nsynS += 1
                                            mutType = CRI(aaList2) #[1,2,3,4,5,6,7,cri]
                                            if mutType[0] == 0:
                                                asex_con1S += 1
                                                asex_sum2PQ_C1 += twoPQ2
                                            else:
                                                asex_rad1S += 1
                                                asex_sum2PQ_R1 += twoPQ2
                                            if mutType[1] == 0:
                                                asex_con2S += 1
                                                asex_sum2PQ_C2 += twoPQ2
                                            else:
                                                asex_rad2S += 1
                                                asex_sum2PQ_R2 += twoPQ2
                                            if mutType[2] == 0:
                                                asex_con3S += 1
                                                asex_sum2PQ_C3 += twoPQ2
                                            else:
                                                asex_rad3S += 1
                                                asex_sum2PQ_R3 += twoPQ2
                                            if mutType[3] == 0:
                                                asex_con4S += 1
                                                asex_sum2PQ_C4 += twoPQ2
                                            else:
                                                asex_rad4S += 1
                                                asex_sum2PQ_R4 += twoPQ2
                                            if mutType[4] == 0:
                                                asex_con5S += 1
                                                asex_sum2PQ_C5 += twoPQ2
                                            else:
                                                asex_rad5S += 1
                                                asex_sum2PQ_R5 += twoPQ2
                                            if mutType[5] == 0:
                                                asex_con6S += 1
                                                asex_sum2PQ_C6 += twoPQ2
                                            else:
                                                asex_rad6S += 1
                                                asex_sum2PQ_R6 += twoPQ2
                                            if mutType[6] == 0:
                                                asex_con7S += 1
                                                asex_sum2PQ_C7 += twoPQ2
                                            else:
                                                asex_rad7S += 1
                                                asex_sum2PQ_R7 += twoPQ2
                                            if mutType[7] <= 0.5:
                                                asex_meanConS += 1
                                                asex_sum2PQ_meanC += twoPQ2
                                            else:
                                                asex_meanRadS += 1
                                                asex_sum2PQ_meanR += twoPQ2
                                    elif aaList2[0] == aaList2[1]:
                                        asex_nsynS += 1
                                        asex_synS += 1
                                        twoPQ1 = 2*currFreqDict[codonList1[1]]*(1-currFreqDict[codonList1[1]]) #nsyn 
                                        twoPQ2 = 2*currFreqDict[codonList2[1]]*(1-currFreqDict[codonList2[1]]) #syn
                                        asex_sum2PQ_S += twoPQ2
                                        asex_sum2PQ_N += twoPQ1
                                        mutType = CRI(aaList1) #[1,2,3,4,5,6,7,cri]
                                        if mutType[0] == 0:
                                            asex_con1S += 1
                                            asex_sum2PQ_C1 += twoPQ1
                                        else:
                                            asex_rad1S += 1
                                            asex_sum2PQ_R1 += twoPQ1
                                        if mutType[1] == 0:
                                            asex_con2S += 1
                                            asex_sum2PQ_C2 += twoPQ1
                                        else:
                                            asex_rad2S += 1
                                            asex_sum2PQ_R2 += twoPQ1
                                        if mutType[2] == 0:
                                            asex_con3S += 1
                                            asex_sum2PQ_C3 += twoPQ1
                                        else:
                                            asex_rad3S += 1
                                            asex_sum2PQ_R3 += twoPQ1
                                        if mutType[3] == 0:
                                            asex_con4S += 1
                                            asex_sum2PQ_C4 += twoPQ1
                                        else:
                                            asex_rad4S += 1
                                            asex_sum2PQ_R4 += twoPQ1
                                        if mutType[4] == 0:
                                            asex_con5S += 1
                                            asex_sum2PQ_C5 += twoPQ1
                                        else:
                                            asex_rad5S += 1
                                            asex_sum2PQ_R5 += twoPQ1
                                        if mutType[5] == 0:
                                            asex_con6S += 1
                                            asex_sum2PQ_C6 += twoPQ1
                                        else:
                                            asex_rad6S += 1
                                            asex_sum2PQ_R6 += twoPQ1
                                        if mutType[6] == 0:
                                            asex_con7S += 1
                                            asex_sum2PQ_C7 += twoPQ1
                                        else:
                                            asex_rad7S += 1
                                            asex_sum2PQ_R7 += twoPQ1
                                        if mutType[7] <= 0.5:
                                            asex_meanConS += 1
                                            asex_sum2PQ_meanC += twoPQ1
                                        else:
                                            asex_meanRadS += 1
                                            asex_sum2PQ_meanR += twoPQ1
                                    else:
                                        asex_nsynS += 2
                                        twoPQ1 = 2*currFreqDict[codonList1[1]]*(1-currFreqDict[codonList1[1]]) #nsyn 
                                        twoPQ2 = 2*currFreqDict[codonList2[1]]*(1-currFreqDict[codonList2[1]]) #nsyn
                                        asex_sum2PQ_N += twoPQ1 + twoPQ2
                                        mutType = CRI(aaList1) #[1,2,3,4,5,6,7,cri]
                                        if mutType[0] == 0:
                                            asex_con1S += 1
                                            asex_sum2PQ_C1 += twoPQ1
                                        else:
                                            asex_rad1S += 1
                                            asex_sum2PQ_R1 += twoPQ1
                                        if mutType[1] == 0:
                                            asex_con2S += 1
                                            asex_sum2PQ_C2 += twoPQ1
                                        else:
                                            asex_rad2S += 1
                                            asex_sum2PQ_R2 += twoPQ1
                                        if mutType[2] == 0:
                                            asex_con3S += 1
                                            asex_sum2PQ_C3 += twoPQ1
                                        else:
                                            asex_rad3S += 1
                                            asex_sum2PQ_R3 += twoPQ1
                                        if mutType[3] == 0:
                                            asex_con4S += 1
                                            asex_sum2PQ_C4 += twoPQ1
                                        else:
                                            asex_rad4S += 1
                                            asex_sum2PQ_R4 += twoPQ1
                                        if mutType[4] == 0:
                                            asex_con5S += 1
                                            asex_sum2PQ_C5 += twoPQ1
                                        else:
                                            asex_rad5S += 1
                                            asex_sum2PQ_R5 += twoPQ1
                                        if mutType[5] == 0:
                                            asex_con6S += 1
                                            asex_sum2PQ_C6 += twoPQ1
                                        else:
                                            asex_rad6S += 1
                                            asex_sum2PQ_R6 += twoPQ1
                                        if mutType[6] == 0:
                                            asex_con7S += 1
                                            asex_sum2PQ_C7 += twoPQ1
                                        else:
                                            asex_rad7S += 1
                                            asex_sum2PQ_R7 += twoPQ1
                                        if mutType[7] <= 0.5:
                                            asex_meanConS += 1
                                            asex_sum2PQ_meanC += twoPQ1
                                        else:
                                            asex_meanRadS += 1
                                            asex_sum2PQ_meanR += twoPQ1
                                        mutType = CRI(aaList2) #[1,2,3,4,5,6,7,cri]
                                        if mutType[0] == 0:
                                            asex_con1S += 1
                                            asex_sum2PQ_C1 += twoPQ2
                                        else:
                                            asex_rad1S += 1
                                            asex_sum2PQ_R1 += twoPQ2
                                        if mutType[1] == 0:
                                            asex_con2S += 1
                                            asex_sum2PQ_C2 += twoPQ2
                                        else:
                                            asex_rad2S += 1
                                            asex_sum2PQ_R2 += twoPQ2
                                        if mutType[2] == 0:
                                            asex_con3S += 1
                                            asex_sum2PQ_C3 += twoPQ2
                                        else:
                                            asex_rad3S += 1
                                            asex_sum2PQ_R3 += twoPQ2
                                        if mutType[3] == 0:
                                            asex_con4S += 1
                                            asex_sum2PQ_C4 += twoPQ2
                                        else:
                                            asex_rad4S += 1
                                            asex_sum2PQ_R4 += twoPQ2
                                        if mutType[4] == 0:
                                            asex_con5S += 1
                                            asex_sum2PQ_C5 += twoPQ2
                                        else:
                                            asex_rad5S += 1
                                            asex_sum2PQ_R5 += twoPQ2
                                        if mutType[5] == 0:
                                            asex_con6S += 1
                                            asex_sum2PQ_C6 += twoPQ2
                                        else:
                                            asex_rad6S += 1
                                            asex_sum2PQ_R6 += twoPQ2
                                        if mutType[6] == 0:
                                            asex_con7S += 1
                                            asex_sum2PQ_C7 += twoPQ2
                                        else:
                                            asex_rad7S += 1
                                            asex_sum2PQ_R7 += twoPQ2
                                        if mutType[7] <= 0.5:
                                            asex_meanConS += 1
                                            asex_sum2PQ_meanC += twoPQ2
                                        else:
                                            asex_meanRadS += 1
                                            asex_sum2PQ_meanR += twoPQ2
                        else:
                            if ab > ac and ab > bc:
                                codonList1 = [codonC,codonB]
                                codonList2 = [codonC,codonA]
                            elif ac > ab and ac > bc:
                                codonList1 = [codonB,codonA]
                                codonList2 = [codonB,codonC]
                            elif bc > ab and bc > ac:
                                codonList1 = [codonA,codonB]
                                codonList2 = [codonA,codonC]
                            aaList1 = []
                            aaList2 = []
                            for comp in codonList1:
                                if i < 3:
                                    if comp in startCodons:
                                        aaList1.append('M')
                                    else:
                                        aaList1.append(geneticCode[comp])
                                else:
                                    aaList1.append(geneticCode[comp])
                            for comp in codonList2:
                                if i < 3:
                                    if comp in startCodons:
                                        aaList2.append('M')
                                    else:
                                        aaList2.append(geneticCode[comp])
                                else:
                                    aaList2.append(geneticCode[comp])
                            if aaList1[0] == aaList1[1]:
                                if aaList2[0] == aaList2[1]:
                                    asex_synS += 2
                                    twoPQ = 4
                                    for allele in currFreqDict:
                                        twoPQ *= currFreqDict[allele]
                                    asex_sum2PQ_S += twoPQ
                                else:
                                    twoPQ1 = 2*currFreqDict[codonList1[1]]*(1-currFreqDict[codonList1[1]]) #syn 
                                    twoPQ2 = 2*currFreqDict[codonList2[1]]*(1-currFreqDict[codonList2[1]]) #nsyn
                                    asex_sum2PQ_S += twoPQ1
                                    asex_sum2PQ_N += twoPQ2
                                    asex_synS += 1
                                    asex_nsynS += 1
                                    mutType = CRI(aaList2) #[1,2,3,4,5,6,7,cri]
                                    if mutType[0] == 0:
                                        asex_con1S += 1
                                        asex_sum2PQ_C1 += twoPQ2
                                    else:
                                        asex_rad1S += 1
                                        asex_sum2PQ_R1 += twoPQ2
                                    if mutType[1] == 0:
                                        asex_con2S += 1
                                        asex_sum2PQ_C2 += twoPQ2
                                    else:
                                        asex_rad2S += 1
                                        asex_sum2PQ_R2 += twoPQ2
                                    if mutType[2] == 0:
                                        asex_con3S += 1
                                        asex_sum2PQ_C3 += twoPQ2
                                    else:
                                        asex_rad3S += 1
                                        asex_sum2PQ_R3 += twoPQ2
                                    if mutType[3] == 0:
                                        asex_con4S += 1
                                        asex_sum2PQ_C4 += twoPQ2
                                    else:
                                        asex_rad4S += 1
                                        asex_sum2PQ_R4 += twoPQ2
                                    if mutType[4] == 0:
                                        asex_con5S += 1
                                        asex_sum2PQ_C5 += twoPQ2
                                    else:
                                        asex_rad5S += 1
                                        asex_sum2PQ_R5 += twoPQ2
                                    if mutType[5] == 0:
                                        asex_con6S += 1
                                        asex_sum2PQ_C6 += twoPQ2
                                    else:
                                        asex_rad6S += 1
                                        asex_sum2PQ_R6 += twoPQ2
                                    if mutType[6] == 0:
                                        asex_con7S += 1
                                        asex_sum2PQ_C7 += twoPQ2
                                    else:
                                        asex_rad7S += 1
                                        asex_sum2PQ_R7 += twoPQ2
                                    if mutType[7] <= 0.5:
                                        asex_meanConS += 1
                                        asex_sum2PQ_meanC += twoPQ2
                                    else:
                                        asex_meanRadS += 1
                                        asex_sum2PQ_meanR += twoPQ2
                            elif aaList2[0] == aaList2[1]:
                                asex_nsynS += 1
                                asex_synS += 1
                                twoPQ1 = 2*currFreqDict[codonList1[1]]*(1-currFreqDict[codonList1[1]]) #nsyn 
                                twoPQ2 = 2*currFreqDict[codonList2[1]]*(1-currFreqDict[codonList2[1]]) #syn
                                asex_sum2PQ_S += twoPQ2
                                asex_sum2PQ_N += twoPQ1
                                mutType = CRI(aaList1) #[1,2,3,4,5,6,7,cri]
                                if mutType[0] == 0:
                                    asex_con1S += 1
                                    asex_sum2PQ_C1 += twoPQ1
                                else:
                                    asex_rad1S += 1
                                    asex_sum2PQ_R1 += twoPQ1
                                if mutType[1] == 0:
                                    asex_con2S += 1
                                    asex_sum2PQ_C2 += twoPQ1
                                else:
                                    asex_rad2S += 1
                                    asex_sum2PQ_R2 += twoPQ1
                                if mutType[2] == 0:
                                    asex_con3S += 1
                                    asex_sum2PQ_C3 += twoPQ1
                                else:
                                    asex_rad3S += 1
                                    asex_sum2PQ_R3 += twoPQ1
                                if mutType[3] == 0:
                                    asex_con4S += 1
                                    asex_sum2PQ_C4 += twoPQ1
                                else:
                                    asex_rad4S += 1
                                    asex_sum2PQ_R4 += twoPQ1
                                if mutType[4] == 0:
                                    asex_con5S += 1
                                    asex_sum2PQ_C5 += twoPQ1
                                else:
                                    asex_rad5S += 1
                                    asex_sum2PQ_R5 += twoPQ1
                                if mutType[5] == 0:
                                    asex_con6S += 1
                                    asex_sum2PQ_C6 += twoPQ1
                                else:
                                    asex_rad6S += 1
                                    asex_sum2PQ_R6 += twoPQ1
                                if mutType[6] == 0:
                                    asex_con7S += 1
                                    asex_sum2PQ_C7 += twoPQ1
                                else:
                                    asex_rad7S += 1
                                    asex_sum2PQ_R7 += twoPQ1
                                if mutType[7] <= 0.5:
                                    asex_meanConS += 1
                                    asex_sum2PQ_meanC += twoPQ1
                                else:
                                    asex_meanRadS += 1
                                    asex_sum2PQ_meanR += twoPQ1
                            else:
                                asex_nsynS += 2
                                twoPQ1 = 2*currFreqDict[codonList1[1]]*(1-currFreqDict[codonList1[1]]) #nsyn 
                                twoPQ2 = 2*currFreqDict[codonList2[1]]*(1-currFreqDict[codonList2[1]]) #nsyn
                                asex_sum2PQ_N += twoPQ1 + twoPQ2
                                mutType = CRI(aaList1) #[1,2,3,4,5,6,7,cri]
                                if mutType[0] == 0:
                                    asex_con1S += 1
                                    asex_sum2PQ_C1 += twoPQ1
                                else:
                                    asex_rad1S += 1
                                    asex_sum2PQ_R1 += twoPQ1
                                if mutType[1] == 0:
                                    asex_con2S += 1
                                    asex_sum2PQ_C2 += twoPQ1
                                else:
                                    asex_rad2S += 1
                                    asex_sum2PQ_R2 += twoPQ1
                                if mutType[2] == 0:
                                    asex_con3S += 1
                                    asex_sum2PQ_C3 += twoPQ1
                                else:
                                    asex_rad3S += 1
                                    asex_sum2PQ_R3 += twoPQ1
                                if mutType[3] == 0:
                                    asex_con4S += 1
                                    asex_sum2PQ_C4 += twoPQ1
                                else:
                                    asex_rad4S += 1
                                    asex_sum2PQ_R4 += twoPQ1
                                if mutType[4] == 0:
                                    asex_con5S += 1
                                    asex_sum2PQ_C5 += twoPQ1
                                else:
                                    asex_rad5S += 1
                                    asex_sum2PQ_R5 += twoPQ1
                                if mutType[5] == 0:
                                    asex_con6S += 1
                                    asex_sum2PQ_C6 += twoPQ1
                                else:
                                    asex_rad6S += 1
                                    asex_sum2PQ_R6 += twoPQ1
                                if mutType[6] == 0:
                                    asex_con7S += 1
                                    asex_sum2PQ_C7 += twoPQ1
                                else:
                                    asex_rad7S += 1
                                    asex_sum2PQ_R7 += twoPQ1
                                if mutType[7] <= 0.5:
                                    asex_meanConS += 1
                                    asex_sum2PQ_meanC += twoPQ1
                                else:
                                    asex_meanRadS += 1
                                    asex_sum2PQ_meanR += twoPQ1
                                mutType = CRI(aaList2) #[1,2,3,4,5,6,7,cri]
                                if mutType[0] == 0:
                                    asex_con1S += 1
                                    asex_sum2PQ_C1 += twoPQ2
                                else:
                                    asex_rad1S += 1
                                    asex_sum2PQ_R1 += twoPQ2
                                if mutType[1] == 0:
                                    asex_con2S += 1
                                    asex_sum2PQ_C2 += twoPQ2
                                else:
                                    asex_rad2S += 1
                                    asex_sum2PQ_R2 += twoPQ2
                                if mutType[2] == 0:
                                    asex_con3S += 1
                                    asex_sum2PQ_C3 += twoPQ2
                                else:
                                    asex_rad3S += 1
                                    asex_sum2PQ_R3 += twoPQ2
                                if mutType[3] == 0:
                                    asex_con4S += 1
                                    asex_sum2PQ_C4 += twoPQ2
                                else:
                                    asex_rad4S += 1
                                    asex_sum2PQ_R4 += twoPQ2
                                if mutType[4] == 0:
                                    asex_con5S += 1
                                    asex_sum2PQ_C5 += twoPQ2
                                else:
                                    asex_rad5S += 1
                                    asex_sum2PQ_R5 += twoPQ2
                                if mutType[5] == 0:
                                    asex_con6S += 1
                                    asex_sum2PQ_C6 += twoPQ2
                                else:
                                    asex_rad6S += 1
                                    asex_sum2PQ_R6 += twoPQ2
                                if mutType[6] == 0:
                                    asex_con7S += 1
                                    asex_sum2PQ_C7 += twoPQ2
                                else:
                                    asex_rad7S += 1
                                    asex_sum2PQ_R7 += twoPQ2
                                if mutType[7] <= 0.5:
                                    asex_meanConS += 1
                                    asex_sum2PQ_meanC += twoPQ2
                                else:
                                    asex_meanRadS += 1
                                    asex_sum2PQ_meanR += twoPQ2
                    elif len(currAlleleDict) == 2:
                        currFreqDict = {}
                        twoPQ = 2
                        for codon in currAlleleDict:
                            freq = float(currAlleleDict[codon])/totalIndividuals
                            twoPQ *= freq
                            currFreqDict[codon] = freq
                        if len(aaList) == 1:
                            asex_synS += 2
                            asex_sum2PQ_S += (2*twoPQ)
            i += 1
        sexPiS = (len(sexList)/(len(sexList)-1))*(sex_sum2PQ_S/sexSynSites)
        sexPiC1_PiS = ((len(sexList)/(len(sexList)-1))*(sex_sum2PQ_C1/sexC1Sites))/sexPiS
        sexPiC2_PiS = ((len(sexList)/(len(sexList)-1))*(sex_sum2PQ_C2/sexC2Sites))/sexPiS
        sexPiC3_PiS = ((len(sexList)/(len(sexList)-1))*(sex_sum2PQ_C3/sexC3Sites))/sexPiS
        sexPiC4_PiS = ((len(sexList)/(len(sexList)-1))*(sex_sum2PQ_C4/sexC4Sites))/sexPiS
        sexPiC5_PiS = ((len(sexList)/(len(sexList)-1))*(sex_sum2PQ_C5/sexC5Sites))/sexPiS
        sexPiC6_PiS = ((len(sexList)/(len(sexList)-1))*(sex_sum2PQ_C6/sexC6Sites))/sexPiS
        sexPiC7_PiS = ((len(sexList)/(len(sexList)-1))*(sex_sum2PQ_C7/sexC7Sites))/sexPiS
        sexPiCMean_PiS = ((len(sexList)/(len(sexList)-1))*(sex_sum2PQ_meanC/sexMeanCSites))/sexPiS
        sexPiR1_PiS = ((len(sexList)/(len(sexList)-1))*(sex_sum2PQ_R1/sexR1Sites))/sexPiS
        sexPiR2_PiS = ((len(sexList)/(len(sexList)-1))*(sex_sum2PQ_R1/sexR1Sites))/sexPiS
        sexPiR3_PiS = ((len(sexList)/(len(sexList)-1))*(sex_sum2PQ_R1/sexR1Sites))/sexPiS
        sexPiR4_PiS = ((len(sexList)/(len(sexList)-1))*(sex_sum2PQ_R1/sexR1Sites))/sexPiS
        sexPiR5_PiS = ((len(sexList)/(len(sexList)-1))*(sex_sum2PQ_R1/sexR1Sites))/sexPiS
        sexPiR6_PiS = ((len(sexList)/(len(sexList)-1))*(sex_sum2PQ_R1/sexR1Sites))/sexPiS
        sexPiR7_PiS = ((len(sexList)/(len(sexList)-1))*(sex_sum2PQ_R1/sexR1Sites))/sexPiS
        sexPiRMean_PiS = ((len(sexList)/(len(sexList)-1))*(sex_sum2PQ_meanR/sexMeanRSites))/sexPiS
        asexPiS = (len(asexList)/(len(asexList)-1))*(asex_sum2PQ_S/asexSynSites)
        asexPiC1_PiS = ((len(asexList)/(len(asexList)-1))*(asex_sum2PQ_C1/asexC1Sites))/asexPiS
        asexPiC2_PiS = ((len(asexList)/(len(asexList)-1))*(asex_sum2PQ_C2/asexC2Sites))/asexPiS
        asexPiC3_PiS = ((len(asexList)/(len(asexList)-1))*(asex_sum2PQ_C3/asexC3Sites))/asexPiS
        asexPiC4_PiS = ((len(asexList)/(len(asexList)-1))*(asex_sum2PQ_C4/asexC4Sites))/asexPiS
        asexPiC5_PiS = ((len(asexList)/(len(asexList)-1))*(asex_sum2PQ_C5/asexC5Sites))/asexPiS
        asexPiC6_PiS = ((len(asexList)/(len(asexList)-1))*(asex_sum2PQ_C6/asexC6Sites))/asexPiS
        asexPiC7_PiS = ((len(asexList)/(len(asexList)-1))*(asex_sum2PQ_C7/asexC7Sites))/asexPiS
        asexPiCMean_PiS = ((len(asexList)/(len(asexList)-1))*(asex_sum2PQ_meanC/asexMeanCSites))/asexPiS
        asexPiR1_PiS = ((len(asexList)/(len(asexList)-1))*(asex_sum2PQ_R1/asexR1Sites))/asexPiS
        asexPiR2_PiS = ((len(asexList)/(len(asexList)-1))*(asex_sum2PQ_R1/asexR1Sites))/asexPiS
        asexPiR3_PiS = ((len(asexList)/(len(asexList)-1))*(asex_sum2PQ_R1/asexR1Sites))/asexPiS
        asexPiR4_PiS = ((len(asexList)/(len(asexList)-1))*(asex_sum2PQ_R1/asexR1Sites))/asexPiS
        asexPiR5_PiS = ((len(asexList)/(len(asexList)-1))*(asex_sum2PQ_R1/asexR1Sites))/asexPiS
        asexPiR6_PiS = ((len(asexList)/(len(asexList)-1))*(asex_sum2PQ_R1/asexR1Sites))/asexPiS
        asexPiR7_PiS = ((len(asexList)/(len(asexList)-1))*(asex_sum2PQ_R1/asexR1Sites))/asexPiS
        asexPiRMean_PiS = ((len(asexList)/(len(asexList)-1))*(asex_sum2PQ_meanR/asexMeanRSites))/asexPiS
        sexThetaS = sex_synS/(sexAn*sexSynSites)
        sexThetaC1_ThetaS = (sex_con1S/(sexAn*sexC1Sites))/sexThetaS
        sexThetaC2_ThetaS = (sex_con2S/(sexAn*sexC2Sites))/sexThetaS
        sexThetaC3_ThetaS = (sex_con3S/(sexAn*sexC3Sites))/sexThetaS
        sexThetaC4_ThetaS = (sex_con4S/(sexAn*sexC4Sites))/sexThetaS
        sexThetaC5_ThetaS = (sex_con5S/(sexAn*sexC5Sites))/sexThetaS
        sexThetaC6_ThetaS = (sex_con6S/(sexAn*sexC6Sites))/sexThetaS
        sexThetaC7_ThetaS = (sex_con7S/(sexAn*sexC7Sites))/sexThetaS
        sexThetaCMean_ThetaS = (sex_meanConS/(sexAn*sexMeanCSites))/sexThetaS
        sexThetaR1_ThetaS = (sex_rad1S/(sexAn*sexR1Sites))/sexThetaS
        sexThetaR2_ThetaS = (sex_rad2S/(sexAn*sexR2Sites))/sexThetaS
        sexThetaR3_ThetaS = (sex_rad3S/(sexAn*sexR3Sites))/sexThetaS
        sexThetaR4_ThetaS = (sex_rad4S/(sexAn*sexR4Sites))/sexThetaS
        sexThetaR5_ThetaS = (sex_rad5S/(sexAn*sexR5Sites))/sexThetaS
        sexThetaR6_ThetaS = (sex_rad6S/(sexAn*sexR6Sites))/sexThetaS
        sexThetaR7_ThetaS = (sex_rad7S/(sexAn*sexR7Sites))/sexThetaS
        sexThetaRMean_ThetaS = (sex_meanRadS/(sexAn*sexMeanRSites))/sexThetaS
        asexThetaS = asex_synS/(asexAn*asexSynSites)
        asexThetaC1_ThetaS = (asex_con1S/(asexAn*asexC1Sites))/asexThetaS
        asexThetaC2_ThetaS = (asex_con2S/(asexAn*asexC2Sites))/asexThetaS
        asexThetaC3_ThetaS = (asex_con3S/(asexAn*asexC3Sites))/asexThetaS
        asexThetaC4_ThetaS = (asex_con4S/(asexAn*asexC4Sites))/asexThetaS
        asexThetaC5_ThetaS = (asex_con5S/(asexAn*asexC5Sites))/asexThetaS
        asexThetaC6_ThetaS = (asex_con6S/(asexAn*asexC6Sites))/asexThetaS
        asexThetaC7_ThetaS = (asex_con7S/(asexAn*asexC7Sites))/asexThetaS
        asexThetaCMean_ThetaS = (asex_meanConS/(asexAn*asexMeanCSites))/asexThetaS
        asexThetaR1_ThetaS = (asex_rad1S/(asexAn*asexR1Sites))/asexThetaS
        asexThetaR2_ThetaS = (asex_rad2S/(asexAn*asexR2Sites))/asexThetaS
        asexThetaR3_ThetaS = (asex_rad3S/(asexAn*asexR3Sites))/asexThetaS
        asexThetaR4_ThetaS = (asex_rad4S/(asexAn*asexR4Sites))/asexThetaS
        asexThetaR5_ThetaS = (asex_rad5S/(asexAn*asexR5Sites))/asexThetaS
        asexThetaR6_ThetaS = (asex_rad6S/(asexAn*asexR6Sites))/asexThetaS
        asexThetaR7_ThetaS = (asex_rad7S/(asexAn*asexR7Sites))/asexThetaS
        asexThetaRMean_ThetaS = (asex_meanRadS/(asexAn*asexMeanRSites))/asexThetaS
        D1_1 = asexPiC1_PiS - sexPiC1_PiS #π conservative
        D1_2 = asexPiC2_PiS - sexPiC2_PiS #π conservative
        D1_3 = asexPiC3_PiS - sexPiC3_PiS #π conservative
        D1_4 = asexPiC4_PiS - sexPiC4_PiS #π conservative
        D1_5 = asexPiC5_PiS - sexPiC5_PiS #π conservative
        D1_6 = asexPiC6_PiS - sexPiC6_PiS #π conservative
        D1_7 = asexPiC7_PiS - sexPiC7_PiS #π conservative
        D1_Mean = asexPiCMean_PiS - sexPiCMean_PiS #π conservative
        D2_1 = asexPiR1_PiS - sexPiR1_PiS #π radical
        D2_2 = asexPiR2_PiS - sexPiR2_PiS #π radical
        D2_3 = asexPiR3_PiS - sexPiR3_PiS #π radical
        D2_4 = asexPiR4_PiS - sexPiR4_PiS #π radical
        D2_5 = asexPiR5_PiS - sexPiR5_PiS #π radical
        D2_6 = asexPiR6_PiS - sexPiR6_PiS #π radical
        D2_7 = asexPiR7_PiS - sexPiR7_PiS #π radical
        D2_Mean = asexPiRMean_PiS - sexPiRMean_PiS #π radical
        D3_1 = asexThetaC1_ThetaS - sexThetaC1_ThetaS #theta conservative
        D3_2 = asexThetaC2_ThetaS - sexThetaC2_ThetaS #theta conservative
        D3_3 = asexThetaC3_ThetaS - sexThetaC3_ThetaS #theta conservative
        D3_4 = asexThetaC4_ThetaS - sexThetaC4_ThetaS #theta conservative
        D3_5 = asexThetaC5_ThetaS - sexThetaC5_ThetaS #theta conservative
        D3_6 = asexThetaC6_ThetaS - sexThetaC6_ThetaS #theta conservative
        D3_7 = asexThetaC7_ThetaS - sexThetaC7_ThetaS #theta conservative
        D3_Mean = asexThetaCMean_ThetaS - sexThetaCMean_ThetaS #theta conservative
        D4_1 = asexThetaR1_ThetaS - sexThetaR1_ThetaS #theta radical
        D4_2 = asexThetaR2_ThetaS - sexThetaR2_ThetaS #theta radical
        D4_3 = asexThetaR3_ThetaS - sexThetaR3_ThetaS #theta radical
        D4_4 = asexThetaR4_ThetaS - sexThetaR4_ThetaS #theta radical
        D4_5 = asexThetaR5_ThetaS - sexThetaR5_ThetaS #theta radical
        D4_6 = asexThetaR6_ThetaS - sexThetaR6_ThetaS #theta radical
        D4_7 = asexThetaR7_ThetaS - sexThetaR7_ThetaS #theta radical
        D4_Mean = asexThetaRMean_ThetaS - sexThetaRMean_ThetaS #theta radical
        currD1_1 = D1[1]
        currD1_2 = D1[2]
        currD1_3 = D1[3]
        currD1_4 = D1[4]
        currD1_5 = D1[5]
        currD1_6 = D1[6]
        currD1_7 = D1[7]
        currD1_Mean = D1['mean']
        currD2_1 = D1[1]
        currD2_2 = D2[2]
        currD2_3 = D2[3]
        currD2_4 = D2[4]
        currD2_5 = D2[5]
        currD2_6 = D2[6]
        currD2_7 = D2[7]
        currD2_Mean = D2['mean']
        currD3_1 = D3[1]
        currD3_2 = D3[2]
        currD3_3 = D3[3]
        currD3_4 = D3[4]
        currD3_5 = D3[5]
        currD3_6 = D3[6]
        currD3_7 = D3[7]
        currD3_Mean = D3['mean']
        currD4_1 = D4[1]
        currD4_2 = D4[2]
        currD4_3 = D4[3]
        currD4_4 = D4[4]
        currD4_5 = D4[5]
        currD4_6 = D4[6]
        currD4_7 = D4[7]
        currD4_Mean = D4['mean']
        currD1_1.append(D1_1)
        currD1_2.append(D1_2)
        currD1_3.append(D1_3)
        currD1_4.append(D1_4)
        currD1_5.append(D1_5)
        currD1_6.append(D1_6)
        currD1_7.append(D1_7)
        currD1_Mean.append(D1_Mean)
        currD2_1.append(D2_1)
        currD2_2.append(D2_2)
        currD2_3.append(D2_3)
        currD2_4.append(D2_4)
        currD2_5.append(D2_5)
        currD2_6.append(D2_6)
        currD2_7.append(D2_7)
        currD2_Mean.append(D2_Mean)
        currD3_1.append(D3_1)
        currD3_2.append(D3_2)
        currD3_3.append(D3_3)
        currD3_4.append(D3_4)
        currD3_5.append(D3_5)
        currD3_6.append(D3_6)
        currD3_7.append(D3_7)
        currD3_Mean.append(D3_Mean)
        currD4_1.append(D4_1)
        currD4_2.append(D4_2)
        currD4_3.append(D4_3)
        currD4_4.append(D4_4)
        currD4_5.append(D4_5)
        currD4_6.append(D4_6)
        currD4_7.append(D4_7)
        currD4_Mean.append(D4_Mean)
        D1[1] = currD1_1
        D1[2] = currD1_2
        D1[3] = currD1_3
        D1[4] = currD1_4
        D1[5] = currD1_5
        D1[6] = currD1_6
        D1[7] = currD1_7
        D1['mean'] = currD1_Mean
        D2[1] = currD2_1
        D2[2] = currD2_2
        D2[3] = currD2_3
        D2[4] = currD2_4
        D2[5] = currD2_5
        D2[6] = currD2_6
        D2[7] = currD2_7
        D2['mean'] = currD2_Mean
        D3[1] = currD3_1
        D3[2] = currD3_2
        D3[3] = currD3_3
        D3[4] = currD3_4
        D3[5] = currD3_5
        D3[6] = currD3_6
        D3[7] = currD3_7
        D3['mean'] = currD3_Mean
        D4[1] = currD4_1
        D4[2] = currD4_2
        D4[3] = currD4_3
        D4[4] = currD4_4
        D4[5] = currD4_5
        D4[6] = currD4_6
        D4[7] = currD4_7
        D4['mean'] = currD4_Mean
    logfile = open('mt_nullDistribution_IantheAnalysis.log','a')
    logfile.write('Finished calculating population genetic parameters\nSorting Population Genetic Parameters\n')
    logfile.close()
    sortedD1_1 = sorted(D1[1])
    logfile = open('mt_nullDistribution_IantheAnalysis.log','a')
    logfile.write('\t' + str(round(100*(1.0/32))) + '% complete\n')
    logfile.close()
    sortedD1_2 = sorted(D1[2])
    logfile = open('mt_nullDistribution_IantheAnalysis.log','a')
    logfile.write('\t' + str(round(100*(2.0/32))) + '% complete\n')
    logfile.close()
    sortedD1_3 = sorted(D1[3])
    logfile = open('mt_nullDistribution_IantheAnalysis.log','a')
    logfile.write('\t' + str(round(100*(3.0/32))) + '% complete\n')
    logfile.close()
    sortedD1_4 = sorted(D1[4])
    logfile = open('mt_nullDistribution_IantheAnalysis.log','a')
    logfile.write('\t' + str(round(100*(4.0/32))) + '% complete\n')
    logfile.close()
    sortedD1_5 = sorted(D1[5])
    logfile = open('mt_nullDistribution_IantheAnalysis.log','a')
    logfile.write('\t' + str(round(100*(5.0/32))) + '% complete\n')
    logfile.close()
    sortedD1_6 = sorted(D1[6])
    logfile = open('mt_nullDistribution_IantheAnalysis.log','a')
    logfile.write('\t' + str(round(100*(6.0/32))) + '% complete\n')
    logfile.close()
    sortedD1_7 = sorted(D1[7])
    logfile = open('mt_nullDistribution_IantheAnalysis.log','a')
    logfile.write('\t' + str(round(100*(7.0/32))) + '% complete\n')
    logfile.close()
    sortedD1_Mean = sorted(D1['mean'])
    logfile = open('mt_nullDistribution_IantheAnalysis.log','a')
    logfile.write('\t' + str(round(100*(8.0/32))) + '% complete\n')
    logfile.close()
    sortedD2_1 = sorted(D2[1])
    logfile = open('mt_nullDistribution_IantheAnalysis.log','a')
    logfile.write('\t' + str(round(100*(9.0/32))) + '% complete\n')
    logfile.close()
    sortedD2_2 = sorted(D2[2])
    logfile = open('mt_nullDistribution_IantheAnalysis.log','a')
    logfile.write('\t' + str(round(100*(10.0/32))) + '% complete\n')
    logfile.close()
    sortedD2_3 = sorted(D2[3])
    logfile = open('mt_nullDistribution_IantheAnalysis.log','a')
    logfile.write('\t' + str(round(100*(11.0/32))) + '% complete\n')
    logfile.close()
    sortedD2_4 = sorted(D2[4])
    logfile = open('mt_nullDistribution_IantheAnalysis.log','a')
    logfile.write('\t' + str(round(100*(12.0/32))) + '% complete\n')
    logfile.close()
    sortedD2_5 = sorted(D2[5])
    logfile = open('mt_nullDistribution_IantheAnalysis.log','a')
    logfile.write('\t' + str(round(100*(13.0/32))) + '% complete\n')
    logfile.close()
    sortedD2_6 = sorted(D2[6])
    logfile = open('mt_nullDistribution_IantheAnalysis.log','a')
    logfile.write('\t' + str(round(100*(14.0/32))) + '% complete\n')
    logfile.close()
    sortedD2_7 = sorted(D2[7])
    logfile = open('mt_nullDistribution_IantheAnalysis.log','a')
    logfile.write('\t' + str(round(100*(15.0/32))) + '% complete\n')
    logfile.close()
    sortedD2_Mean = sorted(D2['mean'])
    logfile = open('mt_nullDistribution_IantheAnalysis.log','a')
    logfile.write('\t' + str(round(100*(16.0/32))) + '% complete\n')
    logfile.close()
    sortedD3_1 = sorted(D3[1])
    logfile = open('mt_nullDistribution_IantheAnalysis.log','a')
    logfile.write('\t' + str(round(100*(17.0/32))) + '% complete\n')
    logfile.close()
    sortedD3_2 = sorted(D3[2])
    logfile = open('mt_nullDistribution_IantheAnalysis.log','a')
    logfile.write('\t' + str(round(100*(18.0/32))) + '% complete\n')
    logfile.close()
    sortedD3_3 = sorted(D3[3])
    logfile = open('mt_nullDistribution_IantheAnalysis.log','a')
    logfile.write('\t' + str(round(100*(19.0/32))) + '% complete\n')
    logfile.close()
    sortedD3_4 = sorted(D3[4])
    logfile = open('mt_nullDistribution_IantheAnalysis.log','a')
    logfile.write('\t' + str(round(100*(20.0/32))) + '% complete\n')
    logfile.close()
    sortedD3_5 = sorted(D3[5])
    logfile = open('mt_nullDistribution_IantheAnalysis.log','a')
    logfile.write('\t' + str(round(100*(21.0/32))) + '% complete\n')
    logfile.close()
    sortedD3_6 = sorted(D3[6])
    logfile = open('mt_nullDistribution_IantheAnalysis.log','a')
    logfile.write('\t' + str(round(100*(22.0/32))) + '% complete\n')
    logfile.close()
    sortedD3_7 = sorted(D3[7])
    logfile = open('mt_nullDistribution_IantheAnalysis.log','a')
    logfile.write('\t' + str(round(100*(23.0/32))) + '% complete\n')
    logfile.close()
    sortedD3_Mean = sorted(D3['mean'])
    logfile = open('mt_nullDistribution_IantheAnalysis.log','a')
    logfile.write('\t' + str(round(100*(24.0/32))) + '% complete\n')
    logfile.close()
    sortedD4_1 = sorted(D4[1])
    logfile = open('mt_nullDistribution_IantheAnalysis.log','a')
    logfile.write('\t' + str(round(100*(25.0/32))) + '% complete\n')
    logfile.close()
    sortedD4_2 = sorted(D4[2])
    logfile = open('mt_nullDistribution_IantheAnalysis.log','a')
    logfile.write('\t' + str(round(100*(26.0/32))) + '% complete\n')
    logfile.close()
    sortedD4_3 = sorted(D4[3])
    logfile = open('mt_nullDistribution_IantheAnalysis.log','a')
    logfile.write('\t' + str(round(100*(27.0/32))) + '% complete\n')
    logfile.close()
    sortedD4_4 = sorted(D4[4])
    logfile = open('mt_nullDistribution_IantheAnalysis.log','a')
    logfile.write('\t' + str(round(100*(28.0/32))) + '% complete\n')
    logfile.close()
    sortedD4_5 = sorted(D4[5])
    logfile = open('mt_nullDistribution_IantheAnalysis.log','a')
    logfile.write('\t' + str(round(100*(29.0/32))) + '% complete\n')
    logfile.close()
    sortedD4_6 = sorted(D4[6])
    logfile = open('mt_nullDistribution_IantheAnalysis.log','a')
    logfile.write('\t' + str(round(100*(30.0/32))) + '% complete\n')
    logfile.close()
    sortedD4_7 = sorted(D4[7])
    logfile = open('mt_nullDistribution_IantheAnalysis.log','a')
    logfile.write('\t' + str(round(100*(31.0/32))) + '% complete\n')
    logfile.close()
    sortedD4_Mean = sorted(D4['mean'])
    logfile = open('mt_nullDistribution_IantheAnalysis.log','a')
    logfile.write('Finished sorting population genetic parameters\nWriting output to standard out\n')
    i = 0
    sys.stdout.write('D1_mean\tD2_mean\tD3_mean\tD4_mean\tD1_1\tD1_2\tD1_3\tD1_4\tD1_5\tD1_6\tD1_7\tD2_1\tD2_2\tD2_3\tD2_4\tD2_5\tD2_6\tD2_7\tD3_1\tD3_2\tD3_3\tD3_4\tD3_5\tD3_6\tD3_7\tD4_1\tD4_2\tD4_3\tD4_4\tD4_5\tD4_6\tD4_7\n')
    logfile.close()
    while i < 10000:
        sys.stdout.write(str(sortedD1_Mean[i]) + '\t' + str(sortedD2_Mean[i]) + '\t' + str(sortedD3_Mean[i]) + '\t' + str(sortedD4_Mean[i]) + '\t' + str(sortedD1_1[i]) + '\t' + str(sortedD1_2[i]) + '\t' + str(sortedD1_3[i]) + '\t' + str(sortedD1_4[i]) + '\t' + str(sortedD1_5[i]) + '\t' + str(sortedD1_6[i]) + '\t' + str(sortedD1_7[i]) + '\t' + str(sortedD2_1[i]) + '\t' + str(sortedD2_2[i]) + '\t' + str(sortedD2_3[i]) + '\t' + str(sortedD2_4[i]) + '\t' + str(sortedD2_5[i]) + '\t' + str(sortedD2_6[i]) + '\t' + str(sortedD2_7[i]) + '\t' + str(sortedD3_1[i]) + '\t' + str(sortedD3_2[i]) + '\t' + str(sortedD3_3[i]) + '\t' + str(sortedD3_4[i]) + '\t' + str(sortedD3_5[i]) + '\t' + str(sortedD3_6[i]) + '\t' + str(sortedD3_7[i]) + '\t' + str(sortedD4_1[i]) + '\t' + str(sortedD4_2[i]) + '\t' + str(sortedD4_3[i]) + '\t' + str(sortedD4_4[i]) + '\t' + str(sortedD4_5[i]) + '\t' + str(sortedD4_6[i]) + '\t' + str(sortedD4_7[i]) + '\n')
        i += 1
    logfile.close()

def polSubSyn(fasta,code='invertebrateMt'):
    geneticCodes = {'standard':{"TTT":"F",	"TTC":"F",	"TTA":"L",	"TTG":"L",	"TCT":"S",	"TCC":"S",	"TCA":"S",	"TCG":"S",	"TAT":"Y",	"TAC":"Y",	"TAA":"*",	"TAG":"*",	"TGT":"C",	"TGC":"C",	"TGA":"*",	"TGG":"W",	"CTT":"L",	"CTC":"L",	"CTA":"L",	"CTG":"L",	"CCT":"P",	"CCC":"P",	"CCA":"P",	"CCG":"P",	"CAT":"H",	"CAC":"H",	"CAA":"Q",	"CAG":"Q",	"CGT":"R",	"CGC":"R",	"CGA":"R",	"CGG":"R",	"ATT":"I",	"ATC":"I",	"ATA":"I",	"ATG":"M",	"ACT":"T",	"ACC":"T",	"ACA":"T",	"ACG":"T",	"AAT":"N",	"AAC":"N",	"AAA":"K",	"AAG":"K",	"AGT":"S",	"AGC":"S",	"AGA":"R",	"AGG":"R",	"GTT":"V",	"GTC":"V",	"GTA":"V",	"GTG":"V",	"GCT":"A",	"GCC":"A",	"GCA":"A",	"GCG":"A",	"GAT":"D",	"GAC":"D",	"GAA":"E",	"GAG":"E",	"GGT":"G",	"GGC":"G",	"GGA":"G",	"GGG":"G"},'invertebrateMt':{'CTT': 'L', 'TAG': '*', 'ACA': 'T', 'ACG': 'T', 'ATC': 'I', 'AAC': 'N', 'ATA': 'M', 'AGG': 'S', 'CCT': 'P', 'ACT': 'T', 'AGC': 'S', 'AAG': 'K', 'AGA': 'S', 'CAT': 'H', 'AAT': 'N', 'ATT': 'I', 'CTG': 'L', 'CTA': 'L', 'CTC': 'L', 'CAC': 'H', 'AAA': 'K', 'CCG': 'P', 'AGT': 'S', 'CCA': 'P', 'CAA': 'Q', 'CCC': 'P', 'TAT': 'Y', 'GGT': 'G', 'TGT': 'C', 'CGA': 'R', 'CAG': 'Q', 'TCT': 'S', 'GAT': 'D', 'CGG': 'R', 'TTT': 'F', 'TGC': 'C', 'GGG': 'G', 'TGA': 'W', 'GGA': 'G', 'TGG': 'W', 'GGC': 'G', 'TAC': 'Y', 'TTC': 'F', 'TCG': 'S', 'TTA': 'L', 'TTG': 'L', 'TCC': 'S', 'ACC': 'T', 'TAA': '*', 'GCA': 'A', 'GTA': 'V', 'GCC': 'A', 'GTC': 'V', 'GCG': 'A', 'GTG': 'V', 'GAG': 'E', 'GTT': 'V', 'GCT': 'A', 'GAC': 'D', 'CGT': 'R', 'GAA': 'E', 'TCA': 'S', 'ATG': 'M', 'CGC': 'R'},'vertebrateMt':{'CTT': 'L', 'TAG': '*', 'ACA': 'T', 'ACG': 'T', 'ATC': 'I', 'AAC': 'N', 'ATA': 'M', 'AGG': '*', 'CCT': 'P', 'ACT': 'T', 'AGC': 'S', 'AAG': 'K', 'AGA': '*', 'CAT': 'H', 'AAT': 'N', 'ATT': 'I', 'CTG': 'L', 'CTA': 'L', 'CTC': 'L', 'CAC': 'H', 'AAA': 'K', 'CCG': 'P', 'AGT': 'S', 'CCA': 'P', 'CAA': 'Q', 'CCC': 'P', 'TAT': 'Y', 'GGT': 'G', 'TGT': 'C', 'CGA': 'R', 'CAG': 'Q', 'TCT': 'S', 'GAT': 'D', 'CGG': 'R', 'TTT': 'F', 'TGC': 'C', 'GGG': 'G', 'TGA': 'W', 'GGA': 'G', 'TGG': 'W', 'GGC': 'G', 'TAC': 'Y', 'TTC': 'F', 'TCG': 'S', 'TTA': 'L', 'TTG': 'L', 'TCC': 'S', 'ACC': 'T', 'TAA': '*', 'GCA': 'A', 'GTA': 'V', 'GCC': 'A', 'GTC': 'V', 'GCG': 'A', 'GTG': 'V', 'GAG': 'E', 'GTT': 'V', 'GCT': 'A', 'GAC': 'D', 'CGT': 'R', 'GAA': 'E', 'TCA': 'S', 'ATG': 'M', 'CGC': 'R'}, 'yeastMt':{'CTT': 'T', 'TAG': '*', 'ACA': 'T', 'ACG': 'T', 'ATC': 'I', 'AAC': 'N', 'ATA': 'M', 'AGG': 'R', 'CCT': 'P', 'ACT': 'T', 'AGC': 'S', 'AAG': 'K', 'AGA': 'R', 'CAT': 'H', 'AAT': 'N', 'ATT': 'I', 'CTG': 'T', 'CTA': 'T', 'CTC': 'T', 'CAC': 'H', 'AAA': 'K', 'CCG': 'P', 'AGT': 'S', 'CCA': 'P', 'CAA': 'Q', 'CCC': 'P', 'TAT': 'Y', 'GGT': 'G', 'TGT': 'C', 'CGA': 'R', 'CAG': 'Q', 'TCT': 'S', 'GAT': 'D', 'CGG': 'R', 'TTT': 'F', 'TGC': 'C', 'GGG': 'G', 'TGA': 'W', 'GGA': 'G', 'TGG': 'W', 'GGC': 'G', 'TAC': 'Y', 'TTC': 'F', 'TCG': 'S', 'TTA': 'L', 'TTG': 'L', 'TCC': 'S', 'ACC': 'T', 'TAA': '*', 'GCA': 'A', 'GTA': 'V', 'GCC': 'A', 'GTC': 'V', 'GCG': 'A', 'GTG': 'V', 'GAG': 'E', 'GTT': 'V', 'GCT': 'A', 'GAC': 'D', 'CGT': 'R', 'GAA': 'E', 'TCA': 'S', 'ATG': 'M', 'CGC': 'R'}, 'coelenterateMt':{'CTT': 'L', 'TAG': '*', 'ACA': 'T', 'ACG': 'T', 'ATC': 'I', 'AAC': 'N', 'ATA': 'I', 'AGG': 'R', 'CCT': 'P', 'ACT': 'T', 'AGC': 'S', 'AAG': 'K', 'AGA': 'R', 'CAT': 'H', 'AAT': 'N', 'ATT': 'I', 'CTG': 'L', 'CTA': 'L', 'CTC': 'L', 'CAC': 'H', 'AAA': 'K', 'CCG': 'P', 'AGT': 'S', 'CCA': 'P', 'CAA': 'Q', 'CCC': 'P', 'TAT': 'Y', 'GGT': 'G', 'TGT': 'C', 'CGA': 'R', 'CAG': 'Q', 'TCT': 'S', 'GAT': 'D', 'CGG': 'R', 'TTT': 'F', 'TGC': 'C', 'GGG': 'G', 'TGA': 'W', 'GGA': 'G', 'TGG': 'W', 'GGC': 'G', 'TAC': 'Y', 'TTC': 'F', 'TCG': 'S', 'TTA': 'L', 'TTG': 'L', 'TCC': 'S', 'ACC': 'T', 'TAA': '*', 'GCA': 'A', 'GTA': 'V', 'GCC': 'A', 'GTC': 'V', 'GCG': 'A', 'GTG': 'V', 'GAG': 'E', 'GTT': 'V', 'GCT': 'A', 'GAC': 'D', 'CGT': 'R', 'GAA': 'E', 'TCA': 'S', 'ATG': 'M', 'CGC': 'R'},'ciliateNuc':{'CTT': 'L', 'TAG': 'Q', 'ACA': 'T', 'ACG': 'T', 'ATC': 'I', 'AAC': 'N', 'ATA': 'I', 'AGG': 'R', 'CCT': 'P', 'ACT': 'T', 'AGC': 'S', 'AAG': 'K', 'AGA': 'R', 'CAT': 'H', 'AAT': 'N', 'ATT': 'I', 'CTG': 'L', 'CTA': 'L', 'CTC': 'L', 'CAC': 'H', 'AAA': 'K', 'CCG': 'P', 'AGT': 'S', 'CCA': 'P', 'CAA': 'Q', 'CCC': 'P', 'TAT': 'Y', 'GGT': 'G', 'TGT': 'C', 'CGA': 'R', 'CAG': 'Q', 'TCT': 'S', 'GAT': 'D', 'CGG': 'R', 'TTT': 'F', 'TGC': 'C', 'GGG': 'G', 'TGA': '*', 'GGA': 'G', 'TGG': 'W', 'GGC': 'G', 'TAC': 'Y', 'TTC': 'F', 'TCG': 'S', 'TTA': 'L', 'TTG': 'L', 'TCC': 'S', 'ACC': 'T', 'TAA': 'Q', 'GCA': 'A', 'GTA': 'V', 'GCC': 'A', 'GTC': 'V', 'GCG': 'A', 'GTG': 'V', 'GAG': 'E', 'GTT': 'V', 'GCT': 'A', 'GAC': 'D', 'CGT': 'R', 'GAA': 'E', 'TCA': 'S', 'ATG': 'M', 'CGC': 'R'},'echinodermMt':{'CTT': 'L', 'TAG': '*', 'ACA': 'T', 'ACG': 'T', 'ATC': 'I', 'AAC': 'N', 'ATA': 'I', 'AGG': 'S', 'CCT': 'P', 'ACT': 'T', 'AGC': 'S', 'AAG': 'K', 'AGA': 'S', 'CAT': 'H', 'AAT': 'N', 'ATT': 'I', 'CTG': 'L', 'CTA': 'L', 'CTC': 'L', 'CAC': 'H', 'AAA': 'N', 'CCG': 'P', 'AGT': 'S', 'CCA': 'P', 'CAA': 'Q', 'CCC': 'P', 'TAT': 'Y', 'GGT': 'G', 'TGT': 'C', 'CGA': 'R', 'CAG': 'Q', 'TCT': 'S', 'GAT': 'D', 'CGG': 'R', 'TTT': 'F', 'TGC': 'C', 'GGG': 'G', 'TGA': 'W', 'GGA': 'G', 'TGG': 'W', 'GGC': 'G', 'TAC': 'Y', 'TTC': 'F', 'TCG': 'S', 'TTA': 'L', 'TTG': 'L', 'TCC': 'S', 'ACC': 'T', 'TAA': '*', 'GCA': 'A', 'GTA': 'V', 'GCC': 'A', 'GTC': 'V', 'GCG': 'A', 'GTG': 'V', 'GAG': 'E', 'GTT': 'V', 'GCT': 'A', 'GAC': 'D', 'CGT': 'R', 'GAA': 'E', 'TCA': 'S', 'ATG': 'M', 'CGC': 'R'}, 'euplotidNuc':{'CTT': 'L', 'TAG': '*', 'ACA': 'T', 'ACG': 'T', 'ATC': 'I', 'AAC': 'N', 'ATA': 'I', 'AGG': 'R', 'CCT': 'P', 'ACT': 'T', 'AGC': 'S', 'AAG': 'K', 'AGA': 'R', 'CAT': 'H', 'AAT': 'N', 'ATT': 'I', 'CTG': 'L', 'CTA': 'L', 'CTC': 'L', 'CAC': 'H', 'AAA': 'K', 'CCG': 'P', 'AGT': 'S', 'CCA': 'P', 'CAA': 'Q', 'CCC': 'P', 'TAT': 'Y', 'GGT': 'G', 'TGT': 'C', 'CGA': 'R', 'CAG': 'Q', 'TCT': 'S', 'GAT': 'D', 'CGG': 'R', 'TTT': 'F', 'TGC': 'C', 'GGG': 'G', 'TGA': 'C', 'GGA': 'G', 'TGG': 'W', 'GGC': 'G', 'TAC': 'Y', 'TTC': 'F', 'TCG': 'S', 'TTA': 'L', 'TTG': 'L', 'TCC': 'S', 'ACC': 'T', 'TAA': '*', 'GCA': 'A', 'GTA': 'V', 'GCC': 'A', 'GTC': 'V', 'GCG': 'A', 'GTG': 'V', 'GAG': 'E', 'GTT': 'V', 'GCT': 'A', 'GAC': 'D', 'CGT': 'R', 'GAA': 'E', 'TCA': 'S', 'ATG': 'M', 'CGC': 'R'}, 'bacterial':{'CTT': 'L', 'TAG': '*', 'ACA': 'T', 'ACG': 'T', 'ATC': 'I', 'AAC': 'N', 'ATA': 'I', 'AGG': 'R', 'CCT': 'P', 'ACT': 'T', 'AGC': 'S', 'AAG': 'K', 'AGA': 'R', 'CAT': 'H', 'AAT': 'N', 'ATT': 'I', 'CTG': 'L', 'CTA': 'L', 'CTC': 'L', 'CAC': 'H', 'AAA': 'K', 'CCG': 'P', 'AGT': 'S', 'CCA': 'P', 'CAA': 'Q', 'CCC': 'P', 'TAT': 'Y', 'GGT': 'G', 'TGT': 'C', 'CGA': 'R', 'CAG': 'Q', 'TCT': 'S', 'GAT': 'D', 'CGG': 'R', 'TTT': 'F', 'TGC': 'C', 'GGG': 'G', 'TGA': '*', 'GGA': 'G', 'TGG': 'W', 'GGC': 'G', 'TAC': 'Y', 'TTC': 'F', 'TCG': 'S', 'TTA': 'L', 'TTG': 'L', 'TCC': 'S', 'ACC': 'T', 'TAA': '*', 'GCA': 'A', 'GTA': 'V', 'GCC': 'A', 'GTC': 'V', 'GCG': 'A', 'GTG': 'V', 'GAG': 'E', 'GTT': 'V', 'GCT': 'A', 'GAC': 'D', 'CGT': 'R', 'GAA': 'E', 'TCA': 'S', 'ATG': 'M', 'CGC': 'R'},'yeastNuc':{'CTT': 'L', 'TAG': '*', 'ACA': 'T', 'ACG': 'T', 'ATC': 'I', 'AAC': 'N', 'ATA': 'I', 'AGG': 'R', 'CCT': 'P', 'ACT': 'T', 'AGC': 'S', 'AAG': 'K', 'AGA': 'R', 'CAT': 'H', 'AAT': 'N', 'ATT': 'I', 'CTG': 'S', 'CTA': 'L', 'CTC': 'L', 'CAC': 'H', 'AAA': 'K', 'CCG': 'P', 'AGT': 'S', 'CCA': 'P', 'CAA': 'Q', 'CCC': 'P', 'TAT': 'Y', 'GGT': 'G', 'TGT': 'C', 'CGA': 'R', 'CAG': 'Q', 'TCT': 'S', 'GAT': 'D', 'CGG': 'R', 'TTT': 'F', 'TGC': 'C', 'GGG': 'G', 'TGA': '*', 'GGA': 'G', 'TGG': 'W', 'GGC': 'G', 'TAC': 'Y', 'TTC': 'F', 'TCG': 'S', 'TTA': 'L', 'TTG': 'L', 'TCC': 'S', 'ACC': 'T', 'TAA': '*', 'GCA': 'A', 'GTA': 'V', 'GCC': 'A', 'GTC': 'V', 'GCG': 'A', 'GTG': 'V', 'GAG': 'E', 'GTT': 'V', 'GCT': 'A', 'GAC': 'D', 'CGT': 'R', 'GAA': 'E', 'TCA': 'S', 'ATG': 'M', 'CGC': 'R'}, 'ascidianMt':{'CTT': 'L', 'TAG': '*', 'ACA': 'T', 'ACG': 'T', 'ATC': 'I', 'AAC': 'N', 'ATA': 'M', 'AGG': 'G', 'CCT': 'P', 'ACT': 'T', 'AGC': 'S', 'AAG': 'K', 'AGA': 'G', 'CAT': 'H', 'AAT': 'N', 'ATT': 'I', 'CTG': 'L', 'CTA': 'L', 'CTC': 'L', 'CAC': 'H', 'AAA': 'K', 'CCG': 'P', 'AGT': 'S', 'CCA': 'P', 'CAA': 'Q', 'CCC': 'P', 'TAT': 'Y', 'GGT': 'G', 'TGT': 'C', 'CGA': 'R', 'CAG': 'Q', 'TCT': 'S', 'GAT': 'D', 'CGG': 'R', 'TTT': 'F', 'TGC': 'C', 'GGG': 'G', 'TGA': 'W', 'GGA': 'G', 'TGG': 'W', 'GGC': 'G', 'TAC': 'Y', 'TTC': 'F', 'TCG': 'S', 'TTA': 'L', 'TTG': 'L', 'TCC': 'S', 'ACC': 'T', 'TAA': '*', 'GCA': 'A', 'GTA': 'V', 'GCC': 'A', 'GTC': 'V', 'GCG': 'A', 'GTG': 'V', 'GAG': 'E', 'GTT': 'V', 'GCT': 'A', 'GAC': 'D', 'CGT': 'R', 'GAA': 'E', 'TCA': 'S', 'ATG': 'M', 'CGC': 'R'},'flatwormMt':{'CTT': 'L', 'TAG': '*', 'ACA': 'T', 'ACG': 'T', 'ATC': 'I', 'AAC': 'N', 'ATA': 'I', 'AGG': 'S', 'CCT': 'P', 'ACT': 'T', 'AGC': 'S', 'AAG': 'K', 'AGA': 'S', 'CAT': 'H', 'AAT': 'N', 'ATT': 'I', 'CTG': 'L', 'CTA': 'L', 'CTC': 'L', 'CAC': 'H', 'AAA': 'N', 'CCG': 'P', 'AGT': 'S', 'CCA': 'P', 'CAA': 'Q', 'CCC': 'P', 'TAT': 'Y', 'GGT': 'G', 'TGT': 'C', 'CGA': 'R', 'CAG': 'Q', 'TCT': 'S', 'GAT': 'D', 'CGG': 'R', 'TTT': 'F', 'TGC': 'C', 'GGG': 'G', 'TGA': 'W', 'GGA': 'G', 'TGG': 'W', 'GGC': 'G', 'TAC': 'Y', 'TTC': 'F', 'TCG': 'S', 'TTA': 'L', 'TTG': 'L', 'TCC': 'S', 'ACC': 'T', 'TAA': 'Y', 'GCA': 'A', 'GTA': 'V', 'GCC': 'A', 'GTC': 'V', 'GCG': 'A', 'GTG': 'V', 'GAG': 'E', 'GTT': 'V', 'GCT': 'A', 'GAC': 'D', 'CGT': 'R', 'GAA': 'E', 'TCA': 'S', 'ATG': 'M', 'CGC': 'R'},'chlorophyceanMt':{'CTT': 'L', 'TAG': 'L', 'ACA': 'T', 'ACG': 'T', 'ATC': 'I', 'AAC': 'N', 'ATA': 'I', 'AGG': 'R', 'CCT': 'P', 'ACT': 'T', 'AGC': 'S', 'AAG': 'K', 'AGA': 'R', 'CAT': 'H', 'AAT': 'N', 'ATT': 'I', 'CTG': 'L', 'CTA': 'L', 'CTC': 'L', 'CAC': 'H', 'AAA': 'K', 'CCG': 'P', 'AGT': 'S', 'CCA': 'P', 'CAA': 'Q', 'CCC': 'P', 'TAT': 'Y', 'GGT': 'G', 'TGT': 'C', 'CGA': 'R', 'CAG': 'Q', 'TCT': 'S', 'GAT': 'D', 'CGG': 'R', 'TTT': 'F', 'TGC': 'C', 'GGG': 'G', 'TGA': '*', 'GGA': 'G', 'TGG': 'W', 'GGC': 'G', 'TAC': 'Y', 'TTC': 'F', 'TCG': 'S', 'TTA': 'L', 'TTG': 'L', 'TCC': 'S', 'ACC': 'T', 'TAA': '*', 'GCA': 'A', 'GTA': 'V', 'GCC': 'A', 'GTC': 'V', 'GCG': 'A', 'GTG': 'V', 'GAG': 'E', 'GTT': 'V', 'GCT': 'A', 'GAC': 'D', 'CGT': 'R', 'GAA': 'E', 'TCA': 'S', 'ATG': 'M', 'CGC': 'R'},'trematodeMt':{'CTT': 'L', 'TAG': '*', 'ACA': 'T', 'ACG': 'T', 'ATC': 'I', 'AAC': 'N', 'ATA': 'M', 'AGG': 'S', 'CCT': 'P', 'ACT': 'T', 'AGC': 'S', 'AAG': 'K', 'AGA': 'S', 'CAT': 'H', 'AAT': 'N', 'ATT': 'I', 'CTG': 'L', 'CTA': 'L', 'CTC': 'L', 'CAC': 'H', 'AAA': 'N', 'CCG': 'P', 'AGT': 'S', 'CCA': 'P', 'CAA': 'Q', 'CCC': 'P', 'TAT': 'Y', 'GGT': 'G', 'TGT': 'C', 'CGA': 'R', 'CAG': 'Q', 'TCT': 'S', 'GAT': 'D', 'CGG': 'R', 'TTT': 'F', 'TGC': 'C', 'GGG': 'G', 'TGA': 'W', 'GGA': 'G', 'TGG': 'W', 'GGC': 'G', 'TAC': 'Y', 'TTC': 'F', 'TCG': 'S', 'TTA': 'L', 'TTG': 'L', 'TCC': 'S', 'ACC': 'T', 'TAA': '*', 'GCA': 'A', 'GTA': 'V', 'GCC': 'A', 'GTC': 'V', 'GCG': 'A', 'GTG': 'V', 'GAG': 'E', 'GTT': 'V', 'GCT': 'A', 'GAC': 'D', 'CGT': 'R', 'GAA': 'E', 'TCA': 'S', 'ATG': 'M', 'CGC': 'R'},'pterobranchiaMt':{'CTT': 'L', 'TAG': '*', 'ACA': 'T', 'ACG': 'T', 'ATC': 'I', 'AAC': 'N', 'ATA': 'I', 'AGG': 'K', 'CCT': 'P', 'ACT': 'T', 'AGC': 'S', 'AAG': 'K', 'AGA': 'S', 'CAT': 'H', 'AAT': 'N', 'ATT': 'I', 'CTG': 'L', 'CTA': 'L', 'CTC': 'L', 'CAC': 'H', 'AAA': 'K', 'CCG': 'P', 'AGT': 'S', 'CCA': 'P', 'CAA': 'Q', 'CCC': 'P', 'TAT': 'Y', 'GGT': 'G', 'TGT': 'C', 'CGA': 'R', 'CAG': 'Q', 'TCT': 'S', 'GAT': 'D', 'CGG': 'R', 'TTT': 'F', 'TGC': 'C', 'GGG': 'G', 'TGA': 'W', 'GGA': 'G', 'TGG': 'W', 'GGC': 'G', 'TAC': 'Y', 'TTC': 'F', 'TCG': 'S', 'TTA': 'L', 'TTG': 'L', 'TCC': 'S', 'ACC': 'T', 'TAA': '*', 'GCA': 'A', 'GTA': 'V', 'GCC': 'A', 'GTC': 'V', 'GCG': 'A', 'GTG': 'V', 'GAG': 'E', 'GTT': 'V', 'GCT': 'A', 'GAC': 'D', 'CGT': 'R', 'GAA': 'E', 'TCA': 'S', 'ATG': 'M', 'CGC': 'R'}}
    geneticCode = geneticCodes[code]
    startCodons = ['ATT','ATC','ATA','ATG','GTG'] #invertebrateMt code
    positionDict = {(0,1533):'COI',(1533,2217):'COII',(2217,2373):'ATP8',(2373,3066):'ATP6',(3066,4005):'ND1',(4005,4509):'ND6',(4509,5646):'CYTB',(5646,5940):'ND4L',(5940,7314):'ND4',(7314,9030):'ND5',(9030,9807):'COIII',(9807,10158):'ND3',(10158,11214):'ND2'} #{(start,stop):gene}
    seqDict, seqList, codonDict = buildCodonDict(fasta)
    popList = []
    sexList = []
    outList = [] 
    synSites = {">$Duluth":2591.52083333,	">$Heron2":2598,	">$McGregor":2599,	">$Waik36":2586.91666667,	">$WalesC":2584.91666667,	">$clone_1":2598,	">$AC51":2598.33333333,	">$Heron_mitochondrion":2599,	">$clone_7":2592.85416667,	">$Waik37":2586.58333333,	">$Gunn":2597.66666667,	">$DenmarkA":2593.125,	">$Waik372":2589.25,	">$Tarawera":2586.58333333,	">$Poerua_triploid":2597,	">$Kaniere_triploid":2586.58333333,	">$Waik_lane4_TCCTGAGC_trimmed_paired_contig_237":2593.79166667,	">$Brunner_2_4n":2593.60416674,	">$Brunner_6_3n":2592.9583334,	">$Grasmere_1_4n":2628.66666703,	">$Grasmere_6_3n":2599.62500001,	">$Poerua_72_4n":2605.47916675,	">$Rotoiti_1_4n":2594.35416672,	">$Kaniere_1_2n":2598.33333333,	">$Ianthe_lane1_TAAGGCGA_trimmed_paired_contig_309":2595,	">$Yellow_Contig_56":2592.33333333,	">$Alexsex":2592.33333333,	">$AlexMap":2592.33333333,	">$Lady":2598.66666667,	">$Ianthe":2597,	">$Rotoroa_1_2n":2598.58333338}
    D1 = {'piS':[]} #πS
    D2 = {'thetaS':[]} #thetaS
    logfile = open('mt_nullDistribution_Synonymous.log','w')
    for seq in seqList:
        if '$' in seq:
            popList.append(seq)
        else:
            outList.append(seq)
    seqNums = range(len(popList))
    currPCT = 0
    sexN = 8
    asexN = 23
    sexAn = aN(sexN)
    asexAn = aN(asexN)
    logfile.write('Calculating population genetic parameters:\n')
    logfile.close()
    while len(D1['piS']) < 10000:
        newPCT = int(round(100*len(D1['piS'])/10000.0))
        if newPCT > currPCT:
            logfile = open('mt_nullDistribution_Synonymous.log','a')
            logfile.write('\t' + str(newPCT) + '% complete\n')
            logfile.close()
            currPCT = newPCT
        sexList = []
        asexList = []
        while len(sexList) < sexN:
            currNum = random.choice(seqNums)
            if popList[currNum] not in sexList:
                sexList.append(popList[currNum])
        while len(asexList) < asexN:
            currNum = random.choice(seqNums)
            if popList[currNum] not in asexList and popList[currNum] not in sexList:
                asexList.append(popList[currNum])
        sexSynSites = 0.0
        asexSynSites = 0.0
        for sexual in sexList:
            sexSynSites += synSites[sexual]
        for asexual in asexList:
            asexSynSites += synSites[asexual]
        asexSynSites /= len(asexList)
        sexSynSites /= len(sexList)
        refSeq = seqDict[sexList[0]]
        outSeq = seqDict[outList[0]]
        outCodons = codonDict[outList[0]]
        sex_sum2PQ_S = 0
        sex_synS = 0
        i = 0
        while i < len(codonDict[seqList[0]]):
            outCodon = outCodons[i]
            gene = False
            for locus in positionDict:
                start = locus[0]
                stop = locus[1]
                if i*3 >= start and i*3 <= stop:
                    gene = positionDict[locus]
            currAlleleDict = {}
            currAlleleList = []
            currAADict = {}
            for seq in sexList:
                currCodons = codonDict[seq]
                currCodon = currCodons[i]
                if currCodon not in currAlleleDict and 'N' not in currCodon and '-' not in currCodon:
                    currAlleleDict[currCodon] = 1
                    currAlleleList.append(currCodon)
                elif 'N' not in currCodon and '-' not in currCodon:
                    currValue = currAlleleDict[currCodon]
                    currValue += 1
                    currAlleleDict[currCodon] = currValue
            if len(currAlleleDict) > 1:
                totalIndividuals = 0
                site1 = []
                site2 = []
                site3 = []
                for codon in currAlleleList:
                    totalIndividuals += currAlleleDict[codon]
                    if codon[0] not in site1:
                        site1.append(codon[0])
                    if codon[1] not in site2:
                        site2.append(codon[1])
                    if codon[2] not in site3:
                        site3.append(codon[2])
                currFreqDict = {}
                totalChanges = (len(site1) - 1) + (len(site2) - 1) + (len(site3) - 1)
                variableSites = []
                if len(site1) > 1:
                    variableSites.append(i*3)
                if len(site2) > 1:
                    variableSites.append((i*3) + 1)
                if len(site3) > 1:
                    variableSites.append((i*3) + 1)
                aaList = []
                twoPQ = 2
                for codon in currAlleleDict:
                    freq = float(currAlleleDict[codon])/totalIndividuals
                    currFreqDict[codon] = freq
                    if i == 0 and codon in startCodons:
                        aa = 'M'
                    else:
                        aa = geneticCode[codon]
                    currAADict[codon] = aa
                    if aa not in aaList:
                        aaList.append(aa)
                if totalChanges == 1:
                    for codon in currAlleleDict:
                        freq = float(currAlleleDict[codon])/totalIndividuals
                        currFreqDict[codon] = freq
                        twoPQ *= freq
                    if len(aaList) == 1:
                        sex_synS += 1
                        sex_sum2PQ_S += twoPQ
                elif totalChanges == 2:
                    if len(currAlleleDict) == 3:
                        ab = 0
                        ac = 0
                        bc = 0
                        codonA = currAlleleList[0]
                        codonB = currAlleleList[1]
                        codonC = currAlleleList[2]
                        if codonA[0] != codonB[0]:
                            ab += 1
                        if codonA[1] != codonB[1]:
                            ab += 1
                        if codonA[2] != codonB[2]:
                            ab += 1
                        if codonA[0] != codonC[0]:
                            ac += 1
                        if codonA[1] != codonC[1]:
                            ac += 1
                        if codonA[2] != codonC[2]:
                            ac += 1
                        if codonC[0] != codonB[0]:
                            bc += 1
                        if codonC[1] != codonB[1]:
                            bc += 1
                        if codonC[2] != codonB[2]:
                            bc += 1
                        if ab == ac and ac == bc:
                            if 'N' not in outCodon and '-' not in outCodon:
                                if outCodon == codonA:
                                    aaList1 = [currAADict[codonA],currAADict[codonB]]
                                    aaList2 = [currAADict[codonA],currAADict[codonC]]
                                    codonList1 = [codonA,codonB]
                                    codonList2 = [codonA,codonC]
                                    if aaList1[0] == aaList1[1]:
                                        if aaList2[0] == aaList2[1]:
                                            sex_synS += 2
                                            twoPQ = 4
                                            for allele in currFreqDict:
                                                twoPQ *= currFreqDict[allele]
                                            sex_sum2PQ_S += twoPQ
                                        else:
                                            twoPQ1 = 2*currFreqDict[codonList1[1]]*(1-currFreqDict[codonList1[1]]) #syn 
                                            sex_sum2PQ_S += twoPQ1
                                            sex_synS += 1
                                    elif aaList2[0] == aaList2[1]:
                                        sex_synS += 1
                                        twoPQ2 = 2*currFreqDict[codonList2[1]]*(1-currFreqDict[codonList2[1]]) #syn
                                        sex_sum2PQ_S += twoPQ2
                                elif outCodon == codonB:
                                    aaList1 = [currAADict[codonB],currAADict[codonA]]
                                    aaList2 = [currAADict[codonB],currAADict[codonC]]
                                    codonList1 = [codonB,codonA]
                                    codonList2 = [codonB,codonC]
                                    if aaList1[0] == aaList1[1]:
                                        if aaList2[0] == aaList2[1]:
                                            sex_synS += 2
                                            twoPQ = 4
                                            for allele in currFreqDict:
                                                twoPQ *= currFreqDict[allele]
                                            sex_sum2PQ_S += twoPQ
                                        else:
                                            twoPQ1 = 2*currFreqDict[codonList1[1]]*(1-currFreqDict[codonList1[1]]) #syn 
                                            sex_sum2PQ_S += twoPQ1
                                            sex_synS += 1
                                    elif aaList2[0] == aaList2[1]:
                                        sex_synS += 1
                                        twoPQ2 = 2*currFreqDict[codonList2[1]]*(1-currFreqDict[codonList2[1]]) #syn
                                        sex_sum2PQ_S += twoPQ2
                                elif outCodon == codonC:
                                    aaList1 = [currAADict[codonC],currAADict[codonA]]
                                    aaList2 = [currAADict[codonC],currAADict[codonB]]
                                    codonList1 = [codonA,codonB]
                                    codonList2 = [codonA,codonC]
                                    if aaList1[0] == aaList1[1]:
                                        if aaList2[0] == aaList2[1]:
                                            sex_synS += 2
                                            twoPQ = 4
                                            for allele in currFreqDict:
                                                twoPQ *= currFreqDict[allele]
                                            sex_sum2PQ_S += twoPQ
                                        else:
                                            twoPQ1 = 2*currFreqDict[codonList1[1]]*(1-currFreqDict[codonList1[1]]) #syn 
                                            sex_sum2PQ_S += twoPQ1
                                            sex_synS += 1
                                    elif aaList2[0] == aaList2[1]:
                                        sex_synS += 1
                                        twoPQ2 = 2*currFreqDict[codonList2[1]]*(1-currFreqDict[codonList2[1]]) #syn
                                        sex_sum2PQ_S += twoPQ2                            
                        else:
                            if ab > ac and ab > bc:
                                codonList1 = [codonC,codonB]
                                codonList2 = [codonC,codonA]
                            elif ac > ab and ac > bc:
                                codonList1 = [codonB,codonA]
                                codonList2 = [codonB,codonC]
                            elif bc > ab and bc > ac:
                                codonList1 = [codonA,codonB]
                                codonList2 = [codonA,codonC]
                            aaList1 = []
                            aaList2 = []
                            for comp in codonList1:
                                if i < 3:
                                    if comp in startCodons:
                                        aaList1.append('M')
                                    else:
                                        aaList1.append(geneticCode[comp])
                                else:
                                    aaList1.append(geneticCode[comp])
                            for comp in codonList2:
                                if i < 3:
                                    if comp in startCodons:
                                        aaList2.append('M')
                                    else:
                                        aaList2.append(geneticCode[comp])
                                else:
                                    aaList2.append(geneticCode[comp])
                            if aaList1[0] == aaList1[1]:
                                if aaList2[0] == aaList2[1]:
                                    sex_synS += 2
                                    twoPQ = 4
                                    for allele in currFreqDict:
                                        twoPQ *= currFreqDict[allele]
                                    sex_sum2PQ_S += twoPQ
                                else:
                                    twoPQ1 = 2*currFreqDict[codonList1[1]]*(1-currFreqDict[codonList1[1]]) #syn 
                                    sex_sum2PQ_S += twoPQ1
                                    sex_synS += 1
                            elif aaList2[0] == aaList2[1]:
                                sex_synS += 1
                                twoPQ2 = 2*currFreqDict[codonList2[1]]*(1-currFreqDict[codonList2[1]]) #syn
                                sex_sum2PQ_S += twoPQ2
                    elif len(currAlleleDict) == 2:
                        currFreqDict = {}
                        twoPQ = 2
                        for codon in currAlleleDict:
                            freq = float(currAlleleDict[codon])/totalIndividuals
                            twoPQ *= freq
                            currFreqDict[codon] = freq
                        if len(aaList) == 1:
                            sex_synS += 2
                            sex_sum2PQ_S += (2*twoPQ) 
            i += 1
        asex_sum2PQ_S = 0 
        asex_synS = 0
        i = 0
        while i < len(codonDict[seqList[0]]):
            outCodon = outCodons[i]
            gene = False
            for locus in positionDict:
                start = locus[0]
                stop = locus[1]
                if i*3 >= start and i*3 <= stop:
                    gene = positionDict[locus]
            currAlleleDict = {}
            currAlleleList = []
            currAADict = {}
            for seq in asexList:
                currCodons = codonDict[seq]
                currCodon = currCodons[i]
                if currCodon not in currAlleleDict and 'N' not in currCodon and '-' not in currCodon:
                    currAlleleDict[currCodon] = 1
                    currAlleleList.append(currCodon)
                elif 'N' not in currCodon and '-' not in currCodon:
                    currValue = currAlleleDict[currCodon]
                    currValue += 1
                    currAlleleDict[currCodon] = currValue
            if len(currAlleleDict) > 1:
                totalIndividuals = 0
                site1 = []
                site2 = []
                site3 = []
                for codon in currAlleleList:
                    totalIndividuals += currAlleleDict[codon]
                    if codon[0] not in site1:
                        site1.append(codon[0])
                    if codon[1] not in site2:
                        site2.append(codon[1])
                    if codon[2] not in site3:
                        site3.append(codon[2])
                currFreqDict = {}
                totalChanges = (len(site1) - 1) + (len(site2) - 1) + (len(site3) - 1)
                variableSites = []
                if len(site1) > 1:
                    variableSites.append(i*3)
                if len(site2) > 1:
                    variableSites.append((i*3) + 1)
                if len(site3) > 1:
                    variableSites.append((i*3) + 1)
                aaList = []
                twoPQ = 2
                for codon in currAlleleDict:
                    freq = float(currAlleleDict[codon])/totalIndividuals
                    currFreqDict[codon] = freq
                    if i == 0 and codon in startCodons:
                        aa = 'M'
                    else:
                        aa = geneticCode[codon]
                    currAADict[codon] = aa
                    if aa not in aaList:
                        aaList.append(aa)
                if totalChanges == 1:
                    for codon in currAlleleDict:
                        freq = float(currAlleleDict[codon])/totalIndividuals
                        currFreqDict[codon] = freq
                        twoPQ *= freq
                    if len(aaList) == 1:
                        asex_synS += 1
                        asex_sum2PQ_S += twoPQ
                elif totalChanges == 2:
                    if len(currAlleleDict) == 3:
                        ab = 0
                        ac = 0
                        bc = 0
                        codonA = currAlleleList[0]
                        codonB = currAlleleList[1]
                        codonC = currAlleleList[2]
                        if codonA[0] != codonB[0]:
                            ab += 1
                        if codonA[1] != codonB[1]:
                            ab += 1
                        if codonA[2] != codonB[2]:
                            ab += 1
                        if codonA[0] != codonC[0]:
                            ac += 1
                        if codonA[1] != codonC[1]:
                            ac += 1
                        if codonA[2] != codonC[2]:
                            ac += 1
                        if codonC[0] != codonB[0]:
                            bc += 1
                        if codonC[1] != codonB[1]:
                            bc += 1
                        if codonC[2] != codonB[2]:
                            bc += 1
                        if ab == ac and ac == bc:
                            if 'N' not in outCodon and '-' not in outCodon:
                                if outCodon == codonA:
                                    aaList1 = [currAADict[codonA],currAADict[codonB]]
                                    aaList2 = [currAADict[codonA],currAADict[codonC]]
                                    codonList1 = [codonA,codonB]
                                    codonList2 = [codonA,codonC]
                                    if aaList1[0] == aaList1[1]:
                                        if aaList2[0] == aaList2[1]:
                                            asex_synS += 2
                                            twoPQ = 4
                                            for allele in currFreqDict:
                                                twoPQ *= currFreqDict[allele]
                                            asex_sum2PQ_S += twoPQ
                                        else:
                                            twoPQ1 = 2*currFreqDict[codonList1[1]]*(1-currFreqDict[codonList1[1]]) #syn 
                                            asex_sum2PQ_S += twoPQ1
                                            asex_synS += 1
                                    elif aaList2[0] == aaList2[1]:
                                        asex_synS += 1
                                        twoPQ2 = 2*currFreqDict[codonList2[1]]*(1-currFreqDict[codonList2[1]]) #syn
                                        asex_sum2PQ_S += twoPQ2
                                elif outCodon == codonB:
                                    aaList1 = [currAADict[codonB],currAADict[codonA]]
                                    aaList2 = [currAADict[codonB],currAADict[codonC]]
                                    codonList1 = [codonB,codonA]
                                    codonList2 = [codonB,codonC]
                                    if aaList1[0] == aaList1[1]:
                                        if aaList2[0] == aaList2[1]:
                                            asex_synS += 2
                                            twoPQ = 4
                                            for allele in currFreqDict:
                                                twoPQ *= currFreqDict[allele]
                                            asex_sum2PQ_S += twoPQ
                                        else:
                                            twoPQ1 = 2*currFreqDict[codonList1[1]]*(1-currFreqDict[codonList1[1]]) #syn 
                                            asex_sum2PQ_S += twoPQ1
                                            asex_synS += 1
                                    elif aaList2[0] == aaList2[1]:
                                        asex_synS += 1
                                        twoPQ2 = 2*currFreqDict[codonList2[1]]*(1-currFreqDict[codonList2[1]]) #syn
                                        asex_sum2PQ_S += twoPQ2
                                elif outCodon == codonC:
                                    aaList1 = [currAADict[codonC],currAADict[codonA]]
                                    aaList2 = [currAADict[codonC],currAADict[codonB]]
                                    codonList1 = [codonA,codonB]
                                    codonList2 = [codonA,codonC]
                                    if aaList1[0] == aaList1[1]:
                                        if aaList2[0] == aaList2[1]:
                                            asex_synS += 2
                                            twoPQ = 4
                                            for allele in currFreqDict:
                                                twoPQ *= currFreqDict[allele]
                                            asex_sum2PQ_S += twoPQ
                                        else:
                                            twoPQ1 = 2*currFreqDict[codonList1[1]]*(1-currFreqDict[codonList1[1]]) #syn 
                                            asex_sum2PQ_S += twoPQ1
                                            asex_synS += 1
                                    elif aaList2[0] == aaList2[1]:
                                        asex_synS += 1
                                        twoPQ2 = 2*currFreqDict[codonList2[1]]*(1-currFreqDict[codonList2[1]]) #syn
                                        asex_sum2PQ_S += twoPQ2
                        else:
                            if ab > ac and ab > bc:
                                codonList1 = [codonC,codonB]
                                codonList2 = [codonC,codonA]
                            elif ac > ab and ac > bc:
                                codonList1 = [codonB,codonA]
                                codonList2 = [codonB,codonC]
                            elif bc > ab and bc > ac:
                                codonList1 = [codonA,codonB]
                                codonList2 = [codonA,codonC]
                            aaList1 = []
                            aaList2 = []
                            for comp in codonList1:
                                if i < 3:
                                    if comp in startCodons:
                                        aaList1.append('M')
                                    else:
                                        aaList1.append(geneticCode[comp])
                                else:
                                    aaList1.append(geneticCode[comp])
                            for comp in codonList2:
                                if i < 3:
                                    if comp in startCodons:
                                        aaList2.append('M')
                                    else:
                                        aaList2.append(geneticCode[comp])
                                else:
                                    aaList2.append(geneticCode[comp])
                            if aaList1[0] == aaList1[1]:
                                if aaList2[0] == aaList2[1]:
                                    asex_synS += 2
                                    twoPQ = 4
                                    for allele in currFreqDict:
                                        twoPQ *= currFreqDict[allele]
                                    asex_sum2PQ_S += twoPQ
                                else:
                                    twoPQ1 = 2*currFreqDict[codonList1[1]]*(1-currFreqDict[codonList1[1]]) #syn 
                                    asex_sum2PQ_S += twoPQ1
                                    asex_synS += 1
                            elif aaList2[0] == aaList2[1]:
                                asex_synS += 1
                                twoPQ2 = 2*currFreqDict[codonList2[1]]*(1-currFreqDict[codonList2[1]]) #syn
                                asex_sum2PQ_S += twoPQ2
                    elif len(currAlleleDict) == 2:
                        currFreqDict = {}
                        twoPQ = 2
                        for codon in currAlleleDict:
                            freq = float(currAlleleDict[codon])/totalIndividuals
                            twoPQ *= freq
                            currFreqDict[codon] = freq
                        if len(aaList) == 1:
                            asex_synS += 2
                            asex_sum2PQ_S += (2*twoPQ)
            i += 1
        sexPiS = (len(sexList)/(len(sexList)-1))*(sex_sum2PQ_S/sexSynSites)
        asexPiS = (len(asexList)/(len(asexList)-1))*(asex_sum2PQ_S/asexSynSites)
        sexThetaS = sex_synS/(sexAn*sexSynSites)
        asexThetaS = asex_synS/(asexAn*asexSynSites)
        D1_syn = asexPiS - sexPiS #π synonymous
        D2_syn = asexThetaS - sexThetaS #theta synonymous
        currD1_syn = D1['piS']
        currD2_syn = D2['thetaS']
        currD1_syn.append(D1_syn)
        currD2_syn.append(D2_syn)
        D1['piS'] = currD1_syn
        D2['thetaS'] = currD1_syn
    logfile = open('mt_nullDistribution_Synonymous.log','a')
    logfile.write('Finished calculating population genetic parameters\nSorting Population Genetic Parameters\n')
    logfile.close()
    sortedD1_syn = sorted(D1['piS'])
    logfile = open('mt_nullDistribution_Synonymous.log','a')
    logfile.write('\t' + str(round(100*(1.0/2))) + '% complete\n')
    logfile.close()
    sortedD2_syn = sorted(D2['thetaS'])
    logfile = open('mt_nullDistribution_Synonymouss.log','a')
    logfile.write('\t' + str(round(100*(2.0/2))) + '% complete\n')
    logfile.close()
    logfile = open('mt_nullDistribution_Synonymous.log','a')
    logfile.write('Finished sorting population genetic parameters\nWriting output to standard out\n')
    i = 0
    sys.stdout.write('πS D\tthetaS D\n')
    logfile.close()
    while i < 10000:
        sys.stdout.write(str(sortedD1_syn[i]) + '\t' + str(sortedD2_syn[i]) + '\n')
        i += 1
    logfile.close()
    
def CRI(aaList):
    aaSchemeList = [1,2,3,4,5,6,7]
    aaSchemeDict = {1:{("R","H"):"C",("R","K"):"C",("R","D"):"R",("R","E"):"R",("R","A"):"R",("R","N"):"R",("R","C"):"R",("R","Q"):"R",("R","G"):"R",("R","I"):"R",("R","L"):"R",("R","M"):"R",("R","F"):"R",("R","P"):"R",("R","S"):"R",("R","T"):"R",("R","W"):"R",("R","Y"):"R",("R","V"):"R",("H","K"):"C",("H","D"):"R",("H","E"):"R",("H","A"):"R",("H","N"):"R",("H","C"):"R",("H","Q"):"R",("H","G"):"R",("H","I"):"R",("H","L"):"R",("H","M"):"R",("H","F"):"R",("H","P"):"R",("H","S"):"R",("H","T"):"R",("H","W"):"R",("H","Y"):"R",("H","V"):"R",("K","D"):"R",("K","E"):"R",("K","A"):"R",("K","N"):"R",("K","C"):"R",("K","Q"):"R",("K","G"):"R",("K","I"):"R",("K","L"):"R",("K","M"):"R",("K","F"):"R",("K","P"):"R",("K","S"):"R",("K","T"):"R",("K","W"):"R",("K","Y"):"R",("K","V"):"R",("D","E"):"C",("D","A"):"R",("D","N"):"R",("D","C"):"R",("D","Q"):"R",("D","G"):"R",("D","I"):"R",("D","L"):"R",("D","M"):"R",("D","F"):"R",("D","P"):"R",("D","S"):"R",("D","T"):"R",("D","W"):"R",("D","Y"):"R",("D","V"):"R",("E","A"):"R",("E","N"):"R",("E","C"):"R",("E","Q"):"R",("E","G"):"R",("E","I"):"R",("E","L"):"R",("E","M"):"R",("E","F"):"R",("E","P"):"R",("E","S"):"R",("E","T"):"R",("E","W"):"R",("E","Y"):"R",("E","V"):"R",("A","N"):"C",("A","C"):"C",("A","Q"):"C",("A","G"):"C",("A","I"):"C",("A","L"):"C",("A","M"):"C",("A","F"):"C",("A","P"):"C",("A","S"):"C",("A","T"):"C",("A","W"):"C",("A","Y"):"C",("A","V"):"C",("N","C"):"C",("N","Q"):"C",("N","G"):"C",("N","I"):"C",("N","L"):"C",("N","M"):"C",("N","F"):"C",("N","P"):"C",("N","S"):"C",("N","T"):"C",("N","W"):"C",("N","Y"):"C",("N","V"):"C",("C","Q"):"C",("C","G"):"C",("C","I"):"C",("C","L"):"C",("C","M"):"C",("C","F"):"C",("C","P"):"C",("C","S"):"C",("C","T"):"C",("C","W"):"C",("C","Y"):"C",("C","V"):"C",("Q","G"):"C",("Q","I"):"C",("Q","L"):"C",("Q","M"):"C",("Q","F"):"C",("Q","P"):"C",("Q","S"):"C",("Q","T"):"C",("Q","W"):"C",("Q","Y"):"C",("Q","V"):"C",("G","I"):"C",("G","L"):"C",("G","M"):"C",("G","F"):"C",("G","P"):"C",("G","S"):"C",("G","T"):"C",("G","W"):"C",("G","Y"):"C",("G","V"):"C",("I","L"):"C",("I","M"):"C",("I","F"):"C",("I","P"):"C",("I","S"):"C",("I","T"):"C",("I","W"):"C",("I","Y"):"C",("I","V"):"C",("L","M"):"C",("L","F"):"C",("L","P"):"C",("L","S"):"C",("L","T"):"C",("L","W"):"C",("L","Y"):"C",("L","V"):"C",("M","F"):"C",("M","P"):"C",("M","S"):"C",("M","T"):"C",("M","W"):"C",("M","Y"):"C",("M","V"):"C",("F","P"):"C",("F","S"):"C",("F","T"):"C",("F","W"):"C",("F","Y"):"C",("F","V"):"C",("P","S"):"C",("P","T"):"C",("P","W"):"C",("P","Y"):"C",("P","V"):"C",("S","T"):"C",("S","W"):"C",("S","Y"):"C",("S","V"):"C",("T","W"):"C",("T","Y"):"C",("T","V"):"C",("W","Y"):"C",("W","V"):"C",("Y","V"):"C",("H","R"):"C",("K","R"):"C",("D","R"):"R",("E","R"):"R",("A","R"):"R",("N","R"):"R",("C","R"):"R",("Q","R"):"R",("G","R"):"R",("I","R"):"R",("L","R"):"R",("M","R"):"R",("F","R"):"R",("P","R"):"R",("S","R"):"R",("T","R"):"R",("W","R"):"R",("Y","R"):"R",("V","R"):"R",("K","H"):"C",("D","H"):"R",("E","H"):"R",("A","H"):"R",("N","H"):"R",("C","H"):"R",("Q","H"):"R",("G","H"):"R",("I","H"):"R",("L","H"):"R",("M","H"):"R",("F","H"):"R",("P","H"):"R",("S","H"):"R",("T","H"):"R",("W","H"):"R",("Y","H"):"R",("V","H"):"R",("D","K"):"R",("E","K"):"R",("A","K"):"R",("N","K"):"R",("C","K"):"R",("Q","K"):"R",("G","K"):"R",("I","K"):"R",("L","K"):"R",("M","K"):"R",("F","K"):"R",("P","K"):"R",("S","K"):"R",("T","K"):"R",("W","K"):"R",("Y","K"):"R",("V","K"):"R",("E","D"):"C",("A","D"):"R",("N","D"):"R",("C","D"):"R",("Q","D"):"R",("G","D"):"R",("I","D"):"R",("L","D"):"R",("M","D"):"R",("F","D"):"R",("P","D"):"R",("S","D"):"R",("T","D"):"R",("W","D"):"R",("Y","D"):"R",("V","D"):"R",("A","E"):"R",("N","E"):"R",("C","E"):"R",("Q","E"):"R",("G","E"):"R",("I","E"):"R",("L","E"):"R",("M","E"):"R",("F","E"):"R",("P","E"):"R",("S","E"):"R",("T","E"):"R",("W","E"):"R",("Y","E"):"R",("V","E"):"R",("N","A"):"C",("C","A"):"C",("Q","A"):"C",("G","A"):"C",("I","A"):"C",("L","A"):"C",("M","A"):"C",("F","A"):"C",("P","A"):"C",("S","A"):"C",("T","A"):"C",("W","A"):"C",("Y","A"):"C",("V","A"):"C",("C","N"):"C",("Q","N"):"C",("G","N"):"C",("I","N"):"C",("L","N"):"C",("M","N"):"C",("F","N"):"C",("P","N"):"C",("S","N"):"C",("T","N"):"C",("W","N"):"C",("Y","N"):"C",("V","N"):"C",("Q","C"):"C",("G","C"):"C",("I","C"):"C",("L","C"):"C",("M","C"):"C",("F","C"):"C",("P","C"):"C",("S","C"):"C",("T","C"):"C",("W","C"):"C",("Y","C"):"C",("V","C"):"C",("G","Q"):"C",("I","Q"):"C",("L","Q"):"C",("M","Q"):"C",("F","Q"):"C",("P","Q"):"C",("S","Q"):"C",("T","Q"):"C",("W","Q"):"C",("Y","Q"):"C",("V","Q"):"C",("I","G"):"C",("L","G"):"C",("M","G"):"C",("F","G"):"C",("P","G"):"C",("S","G"):"C",("T","G"):"C",("W","G"):"C",("Y","G"):"C",("V","G"):"C",("L","I"):"C",("M","I"):"C",("F","I"):"C",("P","I"):"C",("S","I"):"C",("T","I"):"C",("W","I"):"C",("Y","I"):"C",("V","I"):"C",("M","L"):"C",("F","L"):"C",("P","L"):"C",("S","L"):"C",("T","L"):"C",("W","L"):"C",("Y","L"):"C",("V","L"):"C",("F","M"):"C",("P","M"):"C",("S","M"):"C",("T","M"):"C",("W","M"):"C",("Y","M"):"C",("V","M"):"C",("P","F"):"C",("S","F"):"C",("T","F"):"C",("W","F"):"C",("Y","F"):"C",("V","F"):"C",("S","P"):"C",("T","P"):"C",("W","P"):"C",("Y","P"):"C",("V","P"):"C",("T","S"):"C",("W","S"):"C",("Y","S"):"C",("V","S"):"C",("W","T"):"C",("Y","T"):"C",("V","T"):"C",("Y","W"):"C",("V","W"):"C",("V","Y"):"C",("R","*"):"R",("H","*"):"R",("K","*"):"R",("D","*"):"R",("E","*"):"R",("A","*"):"R",("N","*"):"R",("C","*"):"R",("Q","*"):"R",("G","*"):"R",("I","*"):"R",("L","*"):"R",("M","*"):"R",("F","*"):"R",("P","*"):"R",("S","*"):"R",("T","*"):"R",("W","*"):"R",("Y","*"):"R",("V","*"):"R",("*","R"):"R",("*","H"):"R",("*","K"):"R",("*","D"):"R",("*","E"):"R",("*","A"):"R",("*","N"):"R",("*","C"):"R",("*","Q"):"R",("*","G"):"R",("*","I"):"R",("*","L"):"R",("*","M"):"R",("*","F"):"R",("*","P"):"R",("*","S"):"R",("*","T"):"R",("*","W"):"R",("*","Y"):"R",("*","V"):"R"},2:{("R","H"):"C",("R","K"):"C",("R","D"):"C",("R","E"):"C",("R","A"):"R",("R","N"):"C",("R","C"):"C",("R","Q"):"C",("R","G"):"C",("R","I"):"R",("R","L"):"R",("R","M"):"R",("R","F"):"R",("R","P"):"R",("R","S"):"C",("R","T"):"C",("R","W"):"R",("R","Y"):"C",("R","V"):"R",("H","K"):"C",("H","D"):"C",("H","E"):"C",("H","A"):"R",("H","N"):"C",("H","C"):"C",("H","Q"):"C",("H","G"):"C",("H","I"):"R",("H","L"):"R",("H","M"):"R",("H","F"):"R",("H","P"):"R",("H","S"):"C",("H","T"):"C",("H","W"):"R",("H","Y"):"C",("H","V"):"R",("K","D"):"C",("K","E"):"C",("K","A"):"R",("K","N"):"C",("K","C"):"C",("K","Q"):"C",("K","G"):"C",("K","I"):"R",("K","L"):"R",("K","M"):"R",("K","F"):"R",("K","P"):"R",("K","S"):"C",("K","T"):"C",("K","W"):"R",("K","Y"):"C",("K","V"):"R",("D","E"):"C",("D","A"):"R",("D","N"):"C",("D","C"):"C",("D","Q"):"C",("D","G"):"C",("D","I"):"R",("D","L"):"R",("D","M"):"R",("D","F"):"R",("D","P"):"R",("D","S"):"C",("D","T"):"C",("D","W"):"R",("D","Y"):"C",("D","V"):"R",("E","A"):"R",("E","N"):"C",("E","C"):"C",("E","Q"):"C",("E","G"):"C",("E","I"):"R",("E","L"):"R",("E","M"):"R",("E","F"):"R",("E","P"):"R",("E","S"):"C",("E","T"):"C",("E","W"):"R",("E","Y"):"C",("E","V"):"R",("A","N"):"R",("A","C"):"R",("A","Q"):"R",("A","G"):"R",("A","I"):"C",("A","L"):"C",("A","M"):"C",("A","F"):"C",("A","P"):"C",("A","S"):"R",("A","T"):"R",("A","W"):"C",("A","Y"):"R",("A","V"):"C",("N","C"):"C",("N","Q"):"C",("N","G"):"C",("N","I"):"R",("N","L"):"R",("N","M"):"R",("N","F"):"R",("N","P"):"R",("N","S"):"C",("N","T"):"C",("N","W"):"R",("N","Y"):"C",("N","V"):"R",("C","Q"):"C",("C","G"):"C",("C","I"):"R",("C","L"):"R",("C","M"):"R",("C","F"):"R",("C","P"):"R",("C","S"):"C",("C","T"):"C",("C","W"):"R",("C","Y"):"C",("C","V"):"R",("Q","G"):"C",("Q","I"):"R",("Q","L"):"R",("Q","M"):"R",("Q","F"):"R",("Q","P"):"R",("Q","S"):"C",("Q","T"):"C",("Q","W"):"R",("Q","Y"):"C",("Q","V"):"R",("G","I"):"R",("G","L"):"R",("G","M"):"R",("G","F"):"R",("G","P"):"R",("G","S"):"C",("G","T"):"C",("G","W"):"R",("G","Y"):"C",("G","V"):"R",("I","L"):"C",("I","M"):"C",("I","F"):"C",("I","P"):"C",("I","S"):"R",("I","T"):"R",("I","W"):"C",("I","Y"):"R",("I","V"):"C",("L","M"):"C",("L","F"):"C",("L","P"):"C",("L","S"):"R",("L","T"):"R",("L","W"):"C",("L","Y"):"R",("L","V"):"C",("M","F"):"C",("M","P"):"C",("M","S"):"R",("M","T"):"R",("M","W"):"C",("M","Y"):"R",("M","V"):"C",("F","P"):"C",("F","S"):"R",("F","T"):"R",("F","W"):"C",("F","Y"):"R",("F","V"):"C",("P","S"):"R",("P","T"):"R",("P","W"):"C",("P","Y"):"R",("P","V"):"C",("S","T"):"C",("S","W"):"R",("S","Y"):"C",("S","V"):"R",("T","W"):"R",("T","Y"):"C",("T","V"):"R",("W","Y"):"R",("W","V"):"C",("Y","V"):"R",("H","R"):"C",("K","R"):"C",("D","R"):"C",("E","R"):"C",("A","R"):"R",("N","R"):"C",("C","R"):"C",("Q","R"):"C",("G","R"):"C",("I","R"):"R",("L","R"):"R",("M","R"):"R",("F","R"):"R",("P","R"):"R",("S","R"):"C",("T","R"):"C",("W","R"):"R",("Y","R"):"C",("V","R"):"R",("K","H"):"C",("D","H"):"C",("E","H"):"C",("A","H"):"R",("N","H"):"C",("C","H"):"C",("Q","H"):"C",("G","H"):"C",("I","H"):"R",("L","H"):"R",("M","H"):"R",("F","H"):"R",("P","H"):"R",("S","H"):"C",("T","H"):"C",("W","H"):"R",("Y","H"):"C",("V","H"):"R",("D","K"):"C",("E","K"):"C",("A","K"):"R",("N","K"):"C",("C","K"):"C",("Q","K"):"C",("G","K"):"C",("I","K"):"R",("L","K"):"R",("M","K"):"R",("F","K"):"R",("P","K"):"R",("S","K"):"C",("T","K"):"C",("W","K"):"R",("Y","K"):"C",("V","K"):"R",("E","D"):"C",("A","D"):"R",("N","D"):"C",("C","D"):"C",("Q","D"):"C",("G","D"):"C",("I","D"):"R",("L","D"):"R",("M","D"):"R",("F","D"):"R",("P","D"):"R",("S","D"):"C",("T","D"):"C",("W","D"):"R",("Y","D"):"C",("V","D"):"R",("A","E"):"R",("N","E"):"C",("C","E"):"C",("Q","E"):"C",("G","E"):"C",("I","E"):"R",("L","E"):"R",("M","E"):"R",("F","E"):"R",("P","E"):"R",("S","E"):"C",("T","E"):"C",("W","E"):"R",("Y","E"):"C",("V","E"):"R",("N","A"):"R",("C","A"):"R",("Q","A"):"R",("G","A"):"R",("I","A"):"C",("L","A"):"C",("M","A"):"C",("F","A"):"C",("P","A"):"C",("S","A"):"R",("T","A"):"R",("W","A"):"C",("Y","A"):"R",("V","A"):"C",("C","N"):"C",("Q","N"):"C",("G","N"):"C",("I","N"):"R",("L","N"):"R",("M","N"):"R",("F","N"):"R",("P","N"):"R",("S","N"):"C",("T","N"):"C",("W","N"):"R",("Y","N"):"C",("V","N"):"R",("Q","C"):"C",("G","C"):"C",("I","C"):"R",("L","C"):"R",("M","C"):"R",("F","C"):"R",("P","C"):"R",("S","C"):"C",("T","C"):"C",("W","C"):"R",("Y","C"):"C",("V","C"):"R",("G","Q"):"C",("I","Q"):"R",("L","Q"):"R",("M","Q"):"R",("F","Q"):"R",("P","Q"):"R",("S","Q"):"C",("T","Q"):"C",("W","Q"):"R",("Y","Q"):"C",("V","Q"):"R",("I","G"):"R",("L","G"):"R",("M","G"):"R",("F","G"):"R",("P","G"):"R",("S","G"):"C",("T","G"):"C",("W","G"):"R",("Y","G"):"C",("V","G"):"R",("L","I"):"C",("M","I"):"C",("F","I"):"C",("P","I"):"C",("S","I"):"R",("T","I"):"R",("W","I"):"C",("Y","I"):"R",("V","I"):"C",("M","L"):"C",("F","L"):"C",("P","L"):"C",("S","L"):"R",("T","L"):"R",("W","L"):"C",("Y","L"):"R",("V","L"):"C",("F","M"):"C",("P","M"):"C",("S","M"):"R",("T","M"):"R",("W","M"):"C",("Y","M"):"R",("V","M"):"C",("P","F"):"C",("S","F"):"R",("T","F"):"R",("W","F"):"C",("Y","F"):"R",("V","F"):"C",("S","P"):"R",("T","P"):"R",("W","P"):"C",("Y","P"):"R",("V","P"):"C",("T","S"):"C",("W","S"):"R",("Y","S"):"C",("V","S"):"R",("W","T"):"R",("Y","T"):"C",("V","T"):"R",("Y","W"):"R",("V","W"):"C",("V","Y"):"R",("R","*"):"R",("H","*"):"R",("K","*"):"R",("D","*"):"R",("E","*"):"R",("A","*"):"R",("N","*"):"R",("C","*"):"R",("Q","*"):"R",("G","*"):"R",("I","*"):"R",("L","*"):"R",("M","*"):"R",("F","*"):"R",("P","*"):"R",("S","*"):"R",("T","*"):"R",("W","*"):"R",("Y","*"):"R",("V","*"):"R",("*","R"):"R",("*","H"):"R",("*","K"):"R",("*","D"):"R",("*","E"):"R",("*","A"):"R",("*","N"):"R",("*","C"):"R",("*","Q"):"R",("*","G"):"R",("*","I"):"R",("*","L"):"R",("*","M"):"R",("*","F"):"R",("*","P"):"R",("*","S"):"R",("*","T"):"R",("*","W"):"R",("*","Y"):"R",("*","V"):"R"},3:{("R","H"):"C",("R","K"):"C",("R","D"):"R",("R","E"):"R",("R","A"):"R",("R","N"):"R",("R","C"):"R",("R","Q"):"R",("R","G"):"R",("R","I"):"R",("R","L"):"R",("R","M"):"R",("R","F"):"R",("R","P"):"R",("R","S"):"R",("R","T"):"R",("R","W"):"R",("R","Y"):"R",("R","V"):"R",("H","K"):"C",("H","D"):"R",("H","E"):"R",("H","A"):"R",("H","N"):"R",("H","C"):"R",("H","Q"):"R",("H","G"):"R",("H","I"):"R",("H","L"):"R",("H","M"):"R",("H","F"):"R",("H","P"):"R",("H","S"):"R",("H","T"):"R",("H","W"):"R",("H","Y"):"R",("H","V"):"R",("K","D"):"R",("K","E"):"R",("K","A"):"R",("K","N"):"R",("K","C"):"R",("K","Q"):"R",("K","G"):"R",("K","I"):"R",("K","L"):"R",("K","M"):"R",("K","F"):"R",("K","P"):"R",("K","S"):"R",("K","T"):"R",("K","W"):"R",("K","Y"):"R",("K","V"):"R",("D","E"):"C",("D","A"):"R",("D","N"):"C",("D","C"):"R",("D","Q"):"C",("D","G"):"R",("D","I"):"R",("D","L"):"R",("D","M"):"R",("D","F"):"R",("D","P"):"R",("D","S"):"R",("D","T"):"R",("D","W"):"R",("D","Y"):"R",("D","V"):"R",("E","A"):"R",("E","N"):"C",("E","C"):"R",("E","Q"):"C",("E","G"):"R",("E","I"):"R",("E","L"):"R",("E","M"):"R",("E","F"):"R",("E","P"):"R",("E","S"):"R",("E","T"):"R",("E","W"):"R",("E","Y"):"R",("E","V"):"R",("A","N"):"R",("A","C"):"R",("A","Q"):"R",("A","G"):"C",("A","I"):"R",("A","L"):"R",("A","M"):"R",("A","F"):"R",("A","P"):"C",("A","S"):"C",("A","T"):"C",("A","W"):"R",("A","Y"):"R",("A","V"):"R",("N","C"):"R",("N","Q"):"C",("N","G"):"R",("N","I"):"R",("N","L"):"R",("N","M"):"R",("N","F"):"R",("N","P"):"R",("N","S"):"R",("N","T"):"R",("N","W"):"R",("N","Y"):"R",("N","V"):"R",("C","Q"):"R",("C","G"):"R",("C","I"):"R",("C","L"):"R",("C","M"):"R",("C","F"):"R",("C","P"):"R",("C","S"):"R",("C","T"):"R",("C","W"):"R",("C","Y"):"R",("C","V"):"R",("Q","G"):"R",("Q","I"):"R",("Q","L"):"R",("Q","M"):"R",("Q","F"):"R",("Q","P"):"R",("Q","S"):"R",("Q","T"):"R",("Q","W"):"R",("Q","Y"):"R",("Q","V"):"R",("G","I"):"R",("G","L"):"R",("G","M"):"R",("G","F"):"R",("G","P"):"C",("G","S"):"C",("G","T"):"C",("G","W"):"R",("G","Y"):"R",("G","V"):"R",("I","L"):"C",("I","M"):"C",("I","F"):"R",("I","P"):"R",("I","S"):"R",("I","T"):"R",("I","W"):"R",("I","Y"):"R",("I","V"):"C",("L","M"):"C",("L","F"):"R",("L","P"):"R",("L","S"):"R",("L","T"):"R",("L","W"):"R",("L","Y"):"R",("L","V"):"C",("M","F"):"R",("M","P"):"R",("M","S"):"R",("M","T"):"R",("M","W"):"R",("M","Y"):"R",("M","V"):"C",("F","P"):"R",("F","S"):"C",("F","T"):"C",("F","W"):"R",("F","Y"):"R",("F","V"):"R",("P","S"):"C",("P","T"):"C",("P","W"):"R",("P","Y"):"R",("P","V"):"R",("S","T"):"C",("S","W"):"R",("S","Y"):"R",("S","V"):"R",("T","W"):"R",("T","Y"):"R",("T","V"):"R",("W","Y"):"C",("W","V"):"R",("Y","V"):"R",("H","R"):"C",("K","R"):"C",("D","R"):"R",("E","R"):"R",("A","R"):"R",("N","R"):"R",("C","R"):"R",("Q","R"):"R",("G","R"):"R",("I","R"):"R",("L","R"):"R",("M","R"):"R",("F","R"):"R",("P","R"):"R",("S","R"):"R",("T","R"):"R",("W","R"):"R",("Y","R"):"R",("V","R"):"R",("K","H"):"C",("D","H"):"R",("E","H"):"R",("A","H"):"R",("N","H"):"R",("C","H"):"R",("Q","H"):"R",("G","H"):"R",("I","H"):"R",("L","H"):"R",("M","H"):"R",("F","H"):"R",("P","H"):"R",("S","H"):"R",("T","H"):"R",("W","H"):"R",("Y","H"):"R",("V","H"):"R",("D","K"):"R",("E","K"):"R",("A","K"):"R",("N","K"):"R",("C","K"):"R",("Q","K"):"R",("G","K"):"R",("I","K"):"R",("L","K"):"R",("M","K"):"R",("F","K"):"R",("P","K"):"R",("S","K"):"R",("T","K"):"R",("W","K"):"R",("Y","K"):"R",("V","K"):"R",("E","D"):"C",("A","D"):"R",("N","D"):"C",("C","D"):"R",("Q","D"):"C",("G","D"):"R",("I","D"):"R",("L","D"):"R",("M","D"):"R",("F","D"):"R",("P","D"):"R",("S","D"):"R",("T","D"):"R",("W","D"):"R",("Y","D"):"R",("V","D"):"R",("A","E"):"R",("N","E"):"C",("C","E"):"R",("Q","E"):"C",("G","E"):"R",("I","E"):"R",("L","E"):"R",("M","E"):"R",("F","E"):"R",("P","E"):"R",("S","E"):"R",("T","E"):"R",("W","E"):"R",("Y","E"):"R",("V","E"):"R",("N","A"):"R",("C","A"):"R",("Q","A"):"R",("G","A"):"C",("I","A"):"R",("L","A"):"R",("M","A"):"R",("F","A"):"R",("P","A"):"C",("S","A"):"C",("T","A"):"C",("W","A"):"R",("Y","A"):"R",("V","A"):"R",("C","N"):"R",("Q","N"):"C",("G","N"):"R",("I","N"):"R",("L","N"):"R",("M","N"):"R",("F","N"):"R",("P","N"):"R",("S","N"):"R",("T","N"):"R",("W","N"):"R",("Y","N"):"R",("V","N"):"R",("Q","C"):"R",("G","C"):"R",("I","C"):"R",("L","C"):"R",("M","C"):"R",("F","C"):"R",("P","C"):"R",("S","C"):"R",("T","C"):"R",("W","C"):"R",("Y","C"):"R",("V","C"):"R",("G","Q"):"R",("I","Q"):"R",("L","Q"):"R",("M","Q"):"R",("F","Q"):"R",("P","Q"):"R",("S","Q"):"R",("T","Q"):"R",("W","Q"):"R",("Y","Q"):"R",("V","Q"):"R",("I","G"):"R",("L","G"):"R",("M","G"):"R",("F","G"):"R",("P","G"):"C",("S","G"):"C",("T","G"):"C",("W","G"):"R",("Y","G"):"R",("V","G"):"R",("L","I"):"C",("M","I"):"C",("F","I"):"R",("P","I"):"R",("S","I"):"R",("T","I"):"R",("W","I"):"R",("Y","I"):"R",("V","I"):"C",("M","L"):"C",("F","L"):"R",("P","L"):"R",("S","L"):"R",("T","L"):"R",("W","L"):"R",("Y","L"):"R",("V","L"):"C",("F","M"):"R",("P","M"):"R",("S","M"):"R",("T","M"):"R",("W","M"):"R",("Y","M"):"R",("V","M"):"C",("P","F"):"R",("S","F"):"C",("T","F"):"C",("W","F"):"R",("Y","F"):"R",("V","F"):"R",("S","P"):"C",("T","P"):"C",("W","P"):"R",("Y","P"):"R",("V","P"):"R",("T","S"):"C",("W","S"):"R",("Y","S"):"R",("V","S"):"R",("W","T"):"R",("Y","T"):"R",("V","T"):"R",("Y","W"):"C",("V","W"):"R",("V","Y"):"R",("R","*"):"R",("H","*"):"R",("K","*"):"R",("D","*"):"R",("E","*"):"R",("A","*"):"R",("N","*"):"R",("C","*"):"R",("Q","*"):"R",("G","*"):"R",("I","*"):"R",("L","*"):"R",("M","*"):"R",("F","*"):"R",("P","*"):"R",("S","*"):"R",("T","*"):"R",("W","*"):"R",("Y","*"):"R",("V","*"):"R",("*","R"):"R",("*","H"):"R",("*","K"):"R",("*","D"):"R",("*","E"):"R",("*","A"):"R",("*","N"):"R",("*","C"):"R",("*","Q"):"R",("*","G"):"R",("*","I"):"R",("*","L"):"R",("*","M"):"R",("*","F"):"R",("*","P"):"R",("*","S"):"R",("*","T"):"R",("*","W"):"R",("*","Y"):"R",("*","V"):"R"},4:{("R","H"):"C",("R","K"):"C",("R","D"):"R",("R","E"):"R",("R","A"):"R",("R","N"):"R",("R","C"):"R",("R","Q"):"C",("R","G"):"R",("R","I"):"R",("R","L"):"R",("R","M"):"R",("R","F"):"C",("R","P"):"R",("R","S"):"R",("R","T"):"R",("R","W"):"C",("R","Y"):"C",("R","V"):"R",("H","K"):"C",("H","D"):"R",("H","E"):"R",("H","A"):"R",("H","N"):"R",("H","C"):"R",("H","Q"):"C",("H","G"):"R",("H","I"):"R",("H","L"):"R",("H","M"):"R",("H","F"):"C",("H","P"):"R",("H","S"):"R",("H","T"):"R",("H","W"):"C",("H","Y"):"C",("H","V"):"R",("K","D"):"R",("K","E"):"R",("K","A"):"R",("K","N"):"R",("K","C"):"R",("K","Q"):"C",("K","G"):"R",("K","I"):"R",("K","L"):"R",("K","M"):"R",("K","F"):"C",("K","P"):"R",("K","S"):"R",("K","T"):"R",("K","W"):"C",("K","Y"):"C",("K","V"):"R",("D","E"):"C",("D","A"):"R",("D","N"):"R",("D","C"):"R",("D","Q"):"R",("D","G"):"R",("D","I"):"R",("D","L"):"R",("D","M"):"R",("D","F"):"R",("D","P"):"R",("D","S"):"R",("D","T"):"R",("D","W"):"R",("D","Y"):"R",("D","V"):"R",("E","A"):"R",("E","N"):"R",("E","C"):"R",("E","Q"):"R",("E","G"):"R",("E","I"):"R",("E","L"):"R",("E","M"):"R",("E","F"):"R",("E","P"):"R",("E","S"):"R",("E","T"):"R",("E","W"):"R",("E","Y"):"R",("E","V"):"R",("A","N"):"C",("A","C"):"C",("A","Q"):"R",("A","G"):"C",("A","I"):"R",("A","L"):"R",("A","M"):"R",("A","F"):"R",("A","P"):"C",("A","S"):"C",("A","T"):"C",("A","W"):"R",("A","Y"):"R",("A","V"):"R",("N","C"):"C",("N","Q"):"R",("N","G"):"C",("N","I"):"R",("N","L"):"R",("N","M"):"R",("N","F"):"R",("N","P"):"C",("N","S"):"C",("N","T"):"C",("N","W"):"R",("N","Y"):"R",("N","V"):"R",("C","Q"):"R",("C","G"):"C",("C","I"):"R",("C","L"):"R",("C","M"):"R",("C","F"):"R",("C","P"):"C",("C","S"):"C",("C","T"):"C",("C","W"):"R",("C","Y"):"R",("C","V"):"R",("Q","G"):"R",("Q","I"):"R",("Q","L"):"R",("Q","M"):"R",("Q","F"):"C",("Q","P"):"R",("Q","S"):"R",("Q","T"):"R",("Q","W"):"C",("Q","Y"):"C",("Q","V"):"R",("G","I"):"R",("G","L"):"R",("G","M"):"R",("G","F"):"R",("G","P"):"C",("G","S"):"C",("G","T"):"C",("G","W"):"R",("G","Y"):"R",("G","V"):"R",("I","L"):"C",("I","M"):"C",("I","F"):"R",("I","P"):"R",("I","S"):"R",("I","T"):"R",("I","W"):"R",("I","Y"):"R",("I","V"):"C",("L","M"):"C",("L","F"):"R",("L","P"):"R",("L","S"):"R",("L","T"):"R",("L","W"):"R",("L","Y"):"R",("L","V"):"C",("M","F"):"R",("M","P"):"R",("M","S"):"R",("M","T"):"R",("M","W"):"R",("M","Y"):"R",("M","V"):"C",("F","P"):"R",("F","S"):"R",("F","T"):"R",("F","W"):"C",("F","Y"):"C",("F","V"):"R",("P","S"):"C",("P","T"):"C",("P","W"):"R",("P","Y"):"R",("P","V"):"R",("S","T"):"C",("S","W"):"R",("S","Y"):"R",("S","V"):"R",("T","W"):"R",("T","Y"):"R",("T","V"):"R",("W","Y"):"C",("W","V"):"R",("Y","V"):"R",("H","R"):"C",("K","R"):"C",("D","R"):"R",("E","R"):"R",("A","R"):"R",("N","R"):"R",("C","R"):"R",("Q","R"):"C",("G","R"):"R",("I","R"):"R",("L","R"):"R",("M","R"):"R",("F","R"):"C",("P","R"):"R",("S","R"):"R",("T","R"):"R",("W","R"):"C",("Y","R"):"C",("V","R"):"R",("K","H"):"C",("D","H"):"R",("E","H"):"R",("A","H"):"R",("N","H"):"R",("C","H"):"R",("Q","H"):"C",("G","H"):"R",("I","H"):"R",("L","H"):"R",("M","H"):"R",("F","H"):"C",("P","H"):"R",("S","H"):"R",("T","H"):"R",("W","H"):"C",("Y","H"):"C",("V","H"):"R",("D","K"):"R",("E","K"):"R",("A","K"):"R",("N","K"):"R",("C","K"):"R",("Q","K"):"C",("G","K"):"R",("I","K"):"R",("L","K"):"R",("M","K"):"R",("F","K"):"C",("P","K"):"R",("S","K"):"R",("T","K"):"R",("W","K"):"C",("Y","K"):"C",("V","K"):"R",("E","D"):"C",("A","D"):"R",("N","D"):"R",("C","D"):"R",("Q","D"):"R",("G","D"):"R",("I","D"):"R",("L","D"):"R",("M","D"):"R",("F","D"):"R",("P","D"):"R",("S","D"):"R",("T","D"):"R",("W","D"):"R",("Y","D"):"R",("V","D"):"R",("A","E"):"R",("N","E"):"R",("C","E"):"R",("Q","E"):"R",("G","E"):"R",("I","E"):"R",("L","E"):"R",("M","E"):"R",("F","E"):"R",("P","E"):"R",("S","E"):"R",("T","E"):"R",("W","E"):"R",("Y","E"):"R",("V","E"):"R",("N","A"):"C",("C","A"):"C",("Q","A"):"R",("G","A"):"C",("I","A"):"R",("L","A"):"R",("M","A"):"R",("F","A"):"R",("P","A"):"C",("S","A"):"C",("T","A"):"C",("W","A"):"R",("Y","A"):"R",("V","A"):"R",("C","N"):"C",("Q","N"):"R",("G","N"):"C",("I","N"):"R",("L","N"):"R",("M","N"):"R",("F","N"):"R",("P","N"):"C",("S","N"):"C",("T","N"):"C",("W","N"):"R",("Y","N"):"R",("V","N"):"R",("Q","C"):"R",("G","C"):"C",("I","C"):"R",("L","C"):"R",("M","C"):"R",("F","C"):"R",("P","C"):"C",("S","C"):"C",("T","C"):"C",("W","C"):"R",("Y","C"):"R",("V","C"):"R",("G","Q"):"R",("I","Q"):"R",("L","Q"):"R",("M","Q"):"R",("F","Q"):"C",("P","Q"):"R",("S","Q"):"R",("T","Q"):"R",("W","Q"):"C",("Y","Q"):"C",("V","Q"):"R",("I","G"):"R",("L","G"):"R",("M","G"):"R",("F","G"):"R",("P","G"):"C",("S","G"):"C",("T","G"):"C",("W","G"):"R",("Y","G"):"R",("V","G"):"R",("L","I"):"C",("M","I"):"C",("F","I"):"R",("P","I"):"R",("S","I"):"R",("T","I"):"R",("W","I"):"R",("Y","I"):"R",("V","I"):"C",("M","L"):"C",("F","L"):"R",("P","L"):"R",("S","L"):"R",("T","L"):"R",("W","L"):"R",("Y","L"):"R",("V","L"):"C",("F","M"):"R",("P","M"):"R",("S","M"):"R",("T","M"):"R",("W","M"):"R",("Y","M"):"R",("V","M"):"C",("P","F"):"R",("S","F"):"R",("T","F"):"R",("W","F"):"C",("Y","F"):"C",("V","F"):"R",("S","P"):"C",("T","P"):"C",("W","P"):"R",("Y","P"):"R",("V","P"):"R",("T","S"):"C",("W","S"):"R",("Y","S"):"R",("V","S"):"R",("W","T"):"R",("Y","T"):"R",("V","T"):"R",("Y","W"):"C",("V","W"):"R",("V","Y"):"R",("R","*"):"R",("H","*"):"R",("K","*"):"R",("D","*"):"R",("E","*"):"R",("A","*"):"R",("N","*"):"R",("C","*"):"R",("Q","*"):"R",("G","*"):"R",("I","*"):"R",("L","*"):"R",("M","*"):"R",("F","*"):"R",("P","*"):"R",("S","*"):"R",("T","*"):"R",("W","*"):"R",("Y","*"):"R",("V","*"):"R",("*","R"):"R",("*","H"):"R",("*","K"):"R",("*","D"):"R",("*","E"):"R",("*","A"):"R",("*","N"):"R",("*","C"):"R",("*","Q"):"R",("*","G"):"R",("*","I"):"R",("*","L"):"R",("*","M"):"R",("*","F"):"R",("*","P"):"R",("*","S"):"R",("*","T"):"R",("*","W"):"R",("*","Y"):"R",("*","V"):"R"},5:{("R","H"):"C",("R","K"):"C",("R","D"):"R",("R","E"):"R",("R","A"):"R",("R","N"):"R",("R","C"):"R",("R","Q"):"R",("R","G"):"R",("R","I"):"R",("R","L"):"R",("R","M"):"R",("R","F"):"R",("R","P"):"R",("R","S"):"R",("R","T"):"R",("R","W"):"R",("R","Y"):"R",("R","V"):"R",("H","K"):"C",("H","D"):"R",("H","E"):"R",("H","A"):"R",("H","N"):"R",("H","C"):"R",("H","Q"):"R",("H","G"):"R",("H","I"):"R",("H","L"):"R",("H","M"):"R",("H","F"):"R",("H","P"):"R",("H","S"):"R",("H","T"):"R",("H","W"):"R",("H","Y"):"R",("H","V"):"R",("K","D"):"R",("K","E"):"R",("K","A"):"R",("K","N"):"R",("K","C"):"R",("K","Q"):"R",("K","G"):"R",("K","I"):"R",("K","L"):"R",("K","M"):"R",("K","F"):"R",("K","P"):"R",("K","S"):"R",("K","T"):"R",("K","W"):"R",("K","Y"):"R",("K","V"):"R",("D","E"):"C",("D","A"):"R",("D","N"):"R",("D","C"):"R",("D","Q"):"R",("D","G"):"R",("D","I"):"R",("D","L"):"R",("D","M"):"R",("D","F"):"R",("D","P"):"R",("D","S"):"R",("D","T"):"R",("D","W"):"R",("D","Y"):"R",("D","V"):"R",("E","A"):"R",("E","N"):"R",("E","C"):"R",("E","Q"):"R",("E","G"):"R",("E","I"):"R",("E","L"):"R",("E","M"):"R",("E","F"):"R",("E","P"):"R",("E","S"):"R",("E","T"):"R",("E","W"):"R",("E","Y"):"R",("E","V"):"R",("A","N"):"C",("A","C"):"C",("A","Q"):"C",("A","G"):"C",("A","I"):"C",("A","L"):"C",("A","M"):"C",("A","F"):"R",("A","P"):"C",("A","S"):"C",("A","T"):"C",("A","W"):"R",("A","Y"):"R",("A","V"):"C",("N","C"):"C",("N","Q"):"C",("N","G"):"C",("N","I"):"C",("N","L"):"C",("N","M"):"C",("N","F"):"R",("N","P"):"C",("N","S"):"C",("N","T"):"C",("N","W"):"R",("N","Y"):"R",("N","V"):"C",("C","Q"):"C",("C","G"):"C",("C","I"):"C",("C","L"):"C",("C","M"):"C",("C","F"):"R",("C","P"):"C",("C","S"):"C",("C","T"):"C",("C","W"):"R",("C","Y"):"R",("C","V"):"C",("Q","G"):"C",("Q","I"):"C",("Q","L"):"C",("Q","M"):"C",("Q","F"):"R",("Q","P"):"C",("Q","S"):"C",("Q","T"):"C",("Q","W"):"R",("Q","Y"):"R",("Q","V"):"C",("G","I"):"C",("G","L"):"C",("G","M"):"C",("G","F"):"R",("G","P"):"C",("G","S"):"C",("G","T"):"C",("G","W"):"R",("G","Y"):"R",("G","V"):"C",("I","L"):"C",("I","M"):"C",("I","F"):"R",("I","P"):"C",("I","S"):"C",("I","T"):"C",("I","W"):"R",("I","Y"):"R",("I","V"):"C",("L","M"):"C",("L","F"):"R",("L","P"):"C",("L","S"):"C",("L","T"):"C",("L","W"):"R",("L","Y"):"R",("L","V"):"C",("M","F"):"R",("M","P"):"C",("M","S"):"C",("M","T"):"C",("M","W"):"R",("M","Y"):"R",("M","V"):"C",("F","P"):"R",("F","S"):"R",("F","T"):"R",("F","W"):"C",("F","Y"):"C",("F","V"):"R",("P","S"):"C",("P","T"):"C",("P","W"):"R",("P","Y"):"R",("P","V"):"C",("S","T"):"C",("S","W"):"R",("S","Y"):"R",("S","V"):"R",("T","W"):"R",("T","Y"):"R",("T","V"):"C",("W","Y"):"C",("W","V"):"R",("Y","V"):"R",("H","R"):"C",("K","R"):"C",("D","R"):"R",("E","R"):"R",("A","R"):"R",("N","R"):"R",("C","R"):"R",("Q","R"):"R",("G","R"):"R",("I","R"):"R",("L","R"):"R",("M","R"):"R",("F","R"):"R",("P","R"):"R",("S","R"):"R",("T","R"):"R",("W","R"):"R",("Y","R"):"R",("V","R"):"R",("K","H"):"C",("D","H"):"R",("E","H"):"R",("A","H"):"R",("N","H"):"R",("C","H"):"R",("Q","H"):"R",("G","H"):"R",("I","H"):"R",("L","H"):"R",("M","H"):"R",("F","H"):"R",("P","H"):"R",("S","H"):"R",("T","H"):"R",("W","H"):"R",("Y","H"):"R",("V","H"):"R",("D","K"):"R",("E","K"):"R",("A","K"):"R",("N","K"):"R",("C","K"):"R",("Q","K"):"R",("G","K"):"R",("I","K"):"R",("L","K"):"R",("M","K"):"R",("F","K"):"R",("P","K"):"R",("S","K"):"R",("T","K"):"R",("W","K"):"R",("Y","K"):"R",("V","K"):"R",("E","D"):"C",("A","D"):"R",("N","D"):"R",("C","D"):"R",("Q","D"):"R",("G","D"):"R",("I","D"):"R",("L","D"):"R",("M","D"):"R",("F","D"):"R",("P","D"):"R",("S","D"):"R",("T","D"):"R",("W","D"):"R",("Y","D"):"R",("V","D"):"R",("A","E"):"R",("N","E"):"R",("C","E"):"R",("Q","E"):"R",("G","E"):"R",("I","E"):"R",("L","E"):"R",("M","E"):"R",("F","E"):"R",("P","E"):"R",("S","E"):"R",("T","E"):"R",("W","E"):"R",("Y","E"):"R",("V","E"):"R",("N","A"):"C",("C","A"):"C",("Q","A"):"C",("G","A"):"C",("I","A"):"C",("L","A"):"C",("M","A"):"C",("F","A"):"R",("P","A"):"C",("S","A"):"C",("T","A"):"C",("W","A"):"R",("Y","A"):"R",("V","A"):"C",("C","N"):"C",("Q","N"):"C",("G","N"):"C",("I","N"):"C",("L","N"):"C",("M","N"):"C",("F","N"):"R",("P","N"):"C",("S","N"):"C",("T","N"):"C",("W","N"):"R",("Y","N"):"R",("V","N"):"C",("Q","C"):"C",("G","C"):"C",("I","C"):"C",("L","C"):"C",("M","C"):"C",("F","C"):"R",("P","C"):"C",("S","C"):"C",("T","C"):"C",("W","C"):"R",("Y","C"):"R",("V","C"):"C",("G","Q"):"C",("I","Q"):"C",("L","Q"):"C",("M","Q"):"C",("F","Q"):"R",("P","Q"):"C",("S","Q"):"C",("T","Q"):"C",("W","Q"):"R",("Y","Q"):"R",("V","Q"):"C",("I","G"):"C",("L","G"):"C",("M","G"):"C",("F","G"):"R",("P","G"):"C",("S","G"):"C",("T","G"):"C",("W","G"):"R",("Y","G"):"R",("V","G"):"C",("L","I"):"C",("M","I"):"C",("F","I"):"R",("P","I"):"C",("S","I"):"C",("T","I"):"C",("W","I"):"R",("Y","I"):"R",("V","I"):"C",("M","L"):"C",("F","L"):"R",("P","L"):"C",("S","L"):"C",("T","L"):"C",("W","L"):"R",("Y","L"):"R",("V","L"):"C",("F","M"):"R",("P","M"):"C",("S","M"):"C",("T","M"):"C",("W","M"):"R",("Y","M"):"R",("V","M"):"C",("P","F"):"R",("S","F"):"R",("T","F"):"R",("W","F"):"C",("Y","F"):"C",("V","F"):"R",("S","P"):"C",("T","P"):"C",("W","P"):"R",("Y","P"):"R",("V","P"):"C",("T","S"):"C",("W","S"):"R",("Y","S"):"R",("V","S"):"R",("W","T"):"R",("Y","T"):"R",("V","T"):"C",("Y","W"):"C",("V","W"):"R",("V","Y"):"R",("R","*"):"R",("H","*"):"R",("K","*"):"R",("D","*"):"R",("E","*"):"R",("A","*"):"R",("N","*"):"R",("C","*"):"R",("Q","*"):"R",("G","*"):"R",("I","*"):"R",("L","*"):"R",("M","*"):"R",("F","*"):"R",("P","*"):"R",("S","*"):"R",("T","*"):"R",("W","*"):"R",("Y","*"):"R",("V","*"):"R",("*","R"):"R",("*","H"):"R",("*","K"):"R",("*","D"):"R",("*","E"):"R",("*","A"):"R",("*","N"):"R",("*","C"):"R",("*","Q"):"R",("*","G"):"R",("*","I"):"R",("*","L"):"R",("*","M"):"R",("*","F"):"R",("*","P"):"R",("*","S"):"R",("*","T"):"R",("*","W"):"R",("*","Y"):"R",("*","V"):"R"},6:{("R","H"):"C",("R","K"):"C",("R","D"):"R",("R","E"):"R",("R","A"):"R",("R","N"):"R",("R","C"):"R",("R","Q"):"R",("R","G"):"R",("R","I"):"R",("R","L"):"R",("R","M"):"R",("R","F"):"R",("R","P"):"R",("R","S"):"R",("R","T"):"R",("R","W"):"R",("R","Y"):"R",("R","V"):"R",("H","K"):"C",("H","D"):"R",("H","E"):"R",("H","A"):"R",("H","N"):"R",("H","C"):"R",("H","Q"):"R",("H","G"):"R",("H","I"):"R",("H","L"):"R",("H","M"):"R",("H","F"):"R",("H","P"):"R",("H","S"):"R",("H","T"):"R",("H","W"):"R",("H","Y"):"R",("H","V"):"R",("K","D"):"R",("K","E"):"R",("K","A"):"R",("K","N"):"R",("K","C"):"R",("K","Q"):"R",("K","G"):"R",("K","I"):"R",("K","L"):"R",("K","M"):"R",("K","F"):"R",("K","P"):"R",("K","S"):"R",("K","T"):"R",("K","W"):"R",("K","Y"):"R",("K","V"):"R",("D","E"):"C",("D","A"):"R",("D","N"):"R",("D","C"):"R",("D","Q"):"R",("D","G"):"R",("D","I"):"R",("D","L"):"R",("D","M"):"R",("D","F"):"R",("D","P"):"R",("D","S"):"R",("D","T"):"R",("D","W"):"R",("D","Y"):"R",("D","V"):"R",("E","A"):"R",("E","N"):"R",("E","C"):"R",("E","Q"):"R",("E","G"):"R",("E","I"):"R",("E","L"):"R",("E","M"):"R",("E","F"):"R",("E","P"):"R",("E","S"):"R",("E","T"):"R",("E","W"):"R",("E","Y"):"R",("E","V"):"R",("A","N"):"R",("A","C"):"R",("A","Q"):"R",("A","G"):"C",("A","I"):"C",("A","L"):"C",("A","M"):"C",("A","F"):"C",("A","P"):"C",("A","S"):"R",("A","T"):"R",("A","W"):"C",("A","Y"):"R",("A","V"):"C",("N","C"):"C",("N","Q"):"C",("N","G"):"R",("N","I"):"R",("N","L"):"R",("N","M"):"R",("N","F"):"R",("N","P"):"R",("N","S"):"C",("N","T"):"C",("N","W"):"R",("N","Y"):"C",("N","V"):"R",("C","Q"):"C",("C","G"):"R",("C","I"):"R",("C","L"):"R",("C","M"):"R",("C","F"):"R",("C","P"):"R",("C","S"):"C",("C","T"):"C",("C","W"):"R",("C","Y"):"C",("C","V"):"R",("Q","G"):"R",("Q","I"):"R",("Q","L"):"R",("Q","M"):"R",("Q","F"):"R",("Q","P"):"R",("Q","S"):"C",("Q","T"):"C",("Q","W"):"R",("Q","Y"):"C",("Q","V"):"R",("G","I"):"C",("G","L"):"C",("G","M"):"C",("G","F"):"C",("G","P"):"C",("G","S"):"R",("G","T"):"R",("G","W"):"C",("G","Y"):"R",("G","V"):"C",("I","L"):"C",("I","M"):"C",("I","F"):"C",("I","P"):"C",("I","S"):"R",("I","T"):"R",("I","W"):"C",("I","Y"):"R",("I","V"):"C",("L","M"):"C",("L","F"):"C",("L","P"):"C",("L","S"):"R",("L","T"):"R",("L","W"):"C",("L","Y"):"R",("L","V"):"C",("M","F"):"C",("M","P"):"C",("M","S"):"R",("M","T"):"R",("M","W"):"C",("M","Y"):"R",("M","V"):"C",("F","P"):"C",("F","S"):"R",("F","T"):"R",("F","W"):"C",("F","Y"):"R",("F","V"):"C",("P","S"):"R",("P","T"):"R",("P","W"):"C",("P","Y"):"R",("P","V"):"C",("S","T"):"C",("S","W"):"R",("S","Y"):"C",("S","V"):"R",("T","W"):"R",("T","Y"):"C",("T","V"):"R",("W","Y"):"R",("W","V"):"C",("Y","V"):"R",("H","R"):"C",("K","R"):"C",("D","R"):"R",("E","R"):"R",("A","R"):"R",("N","R"):"R",("C","R"):"R",("Q","R"):"R",("G","R"):"R",("I","R"):"R",("L","R"):"R",("M","R"):"R",("F","R"):"R",("P","R"):"R",("S","R"):"R",("T","R"):"R",("W","R"):"R",("Y","R"):"R",("V","R"):"R",("K","H"):"C",("D","H"):"R",("E","H"):"R",("A","H"):"R",("N","H"):"R",("C","H"):"R",("Q","H"):"R",("G","H"):"R",("I","H"):"R",("L","H"):"R",("M","H"):"R",("F","H"):"R",("P","H"):"R",("S","H"):"R",("T","H"):"R",("W","H"):"R",("Y","H"):"R",("V","H"):"R",("D","K"):"R",("E","K"):"R",("A","K"):"R",("N","K"):"R",("C","K"):"R",("Q","K"):"R",("G","K"):"R",("I","K"):"R",("L","K"):"R",("M","K"):"R",("F","K"):"R",("P","K"):"R",("S","K"):"R",("T","K"):"R",("W","K"):"R",("Y","K"):"R",("V","K"):"R",("E","D"):"C",("A","D"):"R",("N","D"):"R",("C","D"):"R",("Q","D"):"R",("G","D"):"R",("I","D"):"R",("L","D"):"R",("M","D"):"R",("F","D"):"R",("P","D"):"R",("S","D"):"R",("T","D"):"R",("W","D"):"R",("Y","D"):"R",("V","D"):"R",("A","E"):"R",("N","E"):"R",("C","E"):"R",("Q","E"):"R",("G","E"):"R",("I","E"):"R",("L","E"):"R",("M","E"):"R",("F","E"):"R",("P","E"):"R",("S","E"):"R",("T","E"):"R",("W","E"):"R",("Y","E"):"R",("V","E"):"R",("N","A"):"R",("C","A"):"R",("Q","A"):"R",("G","A"):"C",("I","A"):"C",("L","A"):"C",("M","A"):"C",("F","A"):"C",("P","A"):"C",("S","A"):"R",("T","A"):"R",("W","A"):"C",("Y","A"):"R",("V","A"):"C",("C","N"):"C",("Q","N"):"C",("G","N"):"R",("I","N"):"R",("L","N"):"R",("M","N"):"R",("F","N"):"R",("P","N"):"R",("S","N"):"C",("T","N"):"C",("W","N"):"R",("Y","N"):"C",("V","N"):"R",("Q","C"):"C",("G","C"):"R",("I","C"):"R",("L","C"):"R",("M","C"):"R",("F","C"):"R",("P","C"):"R",("S","C"):"C",("T","C"):"C",("W","C"):"R",("Y","C"):"C",("V","C"):"R",("G","Q"):"R",("I","Q"):"R",("L","Q"):"R",("M","Q"):"R",("F","Q"):"R",("P","Q"):"R",("S","Q"):"C",("T","Q"):"C",("W","Q"):"R",("Y","Q"):"C",("V","Q"):"R",("I","G"):"C",("L","G"):"C",("M","G"):"C",("F","G"):"C",("P","G"):"C",("S","G"):"R",("T","G"):"R",("W","G"):"C",("Y","G"):"R",("V","G"):"C",("L","I"):"C",("M","I"):"C",("F","I"):"C",("P","I"):"C",("S","I"):"R",("T","I"):"R",("W","I"):"C",("Y","I"):"R",("V","I"):"C",("M","L"):"C",("F","L"):"C",("P","L"):"C",("S","L"):"R",("T","L"):"R",("W","L"):"C",("Y","L"):"R",("V","L"):"C",("F","M"):"C",("P","M"):"C",("S","M"):"R",("T","M"):"R",("W","M"):"C",("Y","M"):"R",("V","M"):"C",("P","F"):"C",("S","F"):"R",("T","F"):"R",("W","F"):"C",("Y","F"):"R",("V","F"):"C",("S","P"):"R",("T","P"):"R",("W","P"):"C",("Y","P"):"R",("V","P"):"C",("T","S"):"C",("W","S"):"R",("Y","S"):"C",("V","S"):"R",("W","T"):"R",("Y","T"):"C",("V","T"):"R",("Y","W"):"R",("V","W"):"C",("V","Y"):"R",("R","*"):"R",("H","*"):"R",("K","*"):"R",("D","*"):"R",("E","*"):"R",("A","*"):"R",("N","*"):"R",("C","*"):"R",("Q","*"):"R",("G","*"):"R",("I","*"):"R",("L","*"):"R",("M","*"):"R",("F","*"):"R",("P","*"):"R",("S","*"):"R",("T","*"):"R",("W","*"):"R",("Y","*"):"R",("V","*"):"R",("*","R"):"R",("*","H"):"R",("*","K"):"R",("*","D"):"R",("*","E"):"R",("*","A"):"R",("*","N"):"R",("*","C"):"R",("*","Q"):"R",("*","G"):"R",("*","I"):"R",("*","L"):"R",("*","M"):"R",("*","F"):"R",("*","P"):"R",("*","S"):"R",("*","T"):"R",("*","W"):"R",("*","Y"):"R",("*","V"):"R"},7:{("R","H"):"C",("R","K"):"C",("R","D"):"R",("R","E"):"R",("R","A"):"R",("R","N"):"R",("R","C"):"R",("R","Q"):"R",("R","G"):"R",("R","I"):"R",("R","L"):"R",("R","M"):"R",("R","F"):"R",("R","P"):"R",("R","S"):"R",("R","T"):"R",("R","W"):"R",("R","Y"):"R",("R","V"):"R",("H","K"):"C",("H","D"):"R",("H","E"):"R",("H","A"):"R",("H","N"):"R",("H","C"):"R",("H","Q"):"R",("H","G"):"R",("H","I"):"R",("H","L"):"R",("H","M"):"R",("H","F"):"R",("H","P"):"R",("H","S"):"R",("H","T"):"R",("H","W"):"R",("H","Y"):"R",("H","V"):"R",("K","D"):"R",("K","E"):"R",("K","A"):"R",("K","N"):"R",("K","C"):"R",("K","Q"):"R",("K","G"):"R",("K","I"):"R",("K","L"):"R",("K","M"):"R",("K","F"):"R",("K","P"):"R",("K","S"):"R",("K","T"):"R",("K","W"):"R",("K","Y"):"R",("K","V"):"R",("D","E"):"C",("D","A"):"R",("D","N"):"R",("D","C"):"R",("D","Q"):"R",("D","G"):"R",("D","I"):"R",("D","L"):"R",("D","M"):"R",("D","F"):"R",("D","P"):"R",("D","S"):"R",("D","T"):"R",("D","W"):"R",("D","Y"):"R",("D","V"):"R",("E","A"):"R",("E","N"):"R",("E","C"):"R",("E","Q"):"R",("E","G"):"R",("E","I"):"R",("E","L"):"R",("E","M"):"R",("E","F"):"R",("E","P"):"R",("E","S"):"R",("E","T"):"R",("E","W"):"R",("E","Y"):"R",("E","V"):"R",("A","N"):"R",("A","C"):"R",("A","Q"):"R",("A","G"):"R",("A","I"):"C",("A","L"):"C",("A","M"):"C",("A","F"):"C",("A","P"):"C",("A","S"):"R",("A","T"):"R",("A","W"):"C",("A","Y"):"R",("A","V"):"C",("N","C"):"C",("N","Q"):"C",("N","G"):"C",("N","I"):"R",("N","L"):"R",("N","M"):"R",("N","F"):"R",("N","P"):"R",("N","S"):"C",("N","T"):"C",("N","W"):"R",("N","Y"):"C",("N","V"):"R",("C","Q"):"C",("C","G"):"C",("C","I"):"R",("C","L"):"R",("C","M"):"R",("C","F"):"R",("C","P"):"R",("C","S"):"C",("C","T"):"C",("C","W"):"R",("C","Y"):"C",("C","V"):"R",("Q","G"):"C",("Q","I"):"R",("Q","L"):"R",("Q","M"):"R",("Q","F"):"R",("Q","P"):"R",("Q","S"):"C",("Q","T"):"C",("Q","W"):"R",("Q","Y"):"C",("Q","V"):"R",("G","I"):"R",("G","L"):"R",("G","M"):"R",("G","F"):"R",("G","P"):"R",("G","S"):"C",("G","T"):"C",("G","W"):"R",("G","Y"):"C",("G","V"):"R",("I","L"):"C",("I","M"):"C",("I","F"):"C",("I","P"):"C",("I","S"):"R",("I","T"):"R",("I","W"):"C",("I","Y"):"R",("I","V"):"C",("L","M"):"C",("L","F"):"C",("L","P"):"C",("L","S"):"R",("L","T"):"R",("L","W"):"C",("L","Y"):"R",("L","V"):"C",("M","F"):"C",("M","P"):"C",("M","S"):"R",("M","T"):"R",("M","W"):"C",("M","Y"):"R",("M","V"):"C",("F","P"):"C",("F","S"):"R",("F","T"):"R",("F","W"):"C",("F","Y"):"R",("F","V"):"C",("P","S"):"R",("P","T"):"R",("P","W"):"C",("P","Y"):"R",("P","V"):"C",("S","T"):"C",("S","W"):"R",("S","Y"):"C",("S","V"):"R",("T","W"):"R",("T","Y"):"C",("T","V"):"R",("W","Y"):"R",("W","V"):"C",("Y","V"):"R",("H","R"):"C",("K","R"):"C",("D","R"):"R",("E","R"):"R",("A","R"):"R",("N","R"):"R",("C","R"):"R",("Q","R"):"R",("G","R"):"R",("I","R"):"R",("L","R"):"R",("M","R"):"R",("F","R"):"R",("P","R"):"R",("S","R"):"R",("T","R"):"R",("W","R"):"R",("Y","R"):"R",("V","R"):"R",("K","H"):"C",("D","H"):"R",("E","H"):"R",("A","H"):"R",("N","H"):"R",("C","H"):"R",("Q","H"):"R",("G","H"):"R",("I","H"):"R",("L","H"):"R",("M","H"):"R",("F","H"):"R",("P","H"):"R",("S","H"):"R",("T","H"):"R",("W","H"):"R",("Y","H"):"R",("V","H"):"R",("D","K"):"R",("E","K"):"R",("A","K"):"R",("N","K"):"R",("C","K"):"R",("Q","K"):"R",("G","K"):"R",("I","K"):"R",("L","K"):"R",("M","K"):"R",("F","K"):"R",("P","K"):"R",("S","K"):"R",("T","K"):"R",("W","K"):"R",("Y","K"):"R",("V","K"):"R",("E","D"):"C",("A","D"):"R",("N","D"):"R",("C","D"):"R",("Q","D"):"R",("G","D"):"R",("I","D"):"R",("L","D"):"R",("M","D"):"R",("F","D"):"R",("P","D"):"R",("S","D"):"R",("T","D"):"R",("W","D"):"R",("Y","D"):"R",("V","D"):"R",("A","E"):"R",("N","E"):"R",("C","E"):"R",("Q","E"):"R",("G","E"):"R",("I","E"):"R",("L","E"):"R",("M","E"):"R",("F","E"):"R",("P","E"):"R",("S","E"):"R",("T","E"):"R",("W","E"):"R",("Y","E"):"R",("V","E"):"R",("N","A"):"R",("C","A"):"R",("Q","A"):"R",("G","A"):"R",("I","A"):"C",("L","A"):"C",("M","A"):"C",("F","A"):"C",("P","A"):"C",("S","A"):"R",("T","A"):"R",("W","A"):"C",("Y","A"):"R",("V","A"):"C",("C","N"):"C",("Q","N"):"C",("G","N"):"C",("I","N"):"R",("L","N"):"R",("M","N"):"R",("F","N"):"R",("P","N"):"R",("S","N"):"C",("T","N"):"C",("W","N"):"R",("Y","N"):"C",("V","N"):"R",("Q","C"):"C",("G","C"):"C",("I","C"):"R",("L","C"):"R",("M","C"):"R",("F","C"):"R",("P","C"):"R",("S","C"):"C",("T","C"):"C",("W","C"):"R",("Y","C"):"C",("V","C"):"R",("G","Q"):"C",("I","Q"):"R",("L","Q"):"R",("M","Q"):"R",("F","Q"):"R",("P","Q"):"R",("S","Q"):"C",("T","Q"):"C",("W","Q"):"R",("Y","Q"):"C",("V","Q"):"R",("I","G"):"R",("L","G"):"R",("M","G"):"R",("F","G"):"R",("P","G"):"R",("S","G"):"C",("T","G"):"C",("W","G"):"R",("Y","G"):"C",("V","G"):"R",("L","I"):"C",("M","I"):"C",("F","I"):"C",("P","I"):"C",("S","I"):"R",("T","I"):"R",("W","I"):"C",("Y","I"):"R",("V","I"):"C",("M","L"):"C",("F","L"):"C",("P","L"):"C",("S","L"):"R",("T","L"):"R",("W","L"):"C",("Y","L"):"R",("V","L"):"C",("F","M"):"C",("P","M"):"C",("S","M"):"R",("T","M"):"R",("W","M"):"C",("Y","M"):"R",("V","M"):"C",("P","F"):"C",("S","F"):"R",("T","F"):"R",("W","F"):"C",("Y","F"):"R",("V","F"):"C",("S","P"):"R",("T","P"):"R",("W","P"):"C",("Y","P"):"R",("V","P"):"C",("T","S"):"C",("W","S"):"R",("Y","S"):"C",("V","S"):"R",("W","T"):"R",("Y","T"):"C",("V","T"):"R",("Y","W"):"R",("V","W"):"C",("V","Y"):"R",("R","*"):"R",("H","*"):"R",("K","*"):"R",("D","*"):"R",("E","*"):"R",("A","*"):"R",("N","*"):"R",("C","*"):"R",("Q","*"):"R",("G","*"):"R",("I","*"):"R",("L","*"):"R",("M","*"):"R",("F","*"):"R",("P","*"):"R",("S","*"):"R",("T","*"):"R",("W","*"):"R",("Y","*"):"R",("V","*"):"R",("*","R"):"R",("*","H"):"R",("*","K"):"R",("*","D"):"R",("*","E"):"R",("*","A"):"R",("*","N"):"R",("*","C"):"R",("*","Q"):"R",("*","G"):"R",("*","I"):"R",("*","L"):"R",("*","M"):"R",("*","F"):"R",("*","P"):"R",("*","S"):"R",("*","T"):"R",("*","W"):"R",("*","Y"):"R",("*","V"):"R"}}
    resultsList = []
    cri = 0
    for scheme in aaSchemeList:
        currScheme = aaSchemeDict[scheme]
        currValue = currScheme[(aaList[0],aaList[1])]
        if currValue == 'R':
            cri += 1
            resultsList.append(1)
        else:
            resultsList.append(0)
    cri = cri/7.0
    resultsList.append(cri)
    return resultsList
            
        
                
        
        
def buildCodonDict(fasta):
    code = 'invertebrateMt'
    geneticCodes = {'standard':{"TTT":"F",	"TTC":"F",	"TTA":"L",	"TTG":"L",	"TCT":"S",	"TCC":"S",	"TCA":"S",	"TCG":"S",	"TAT":"Y",	"TAC":"Y",	"TAA":"*",	"TAG":"*",	"TGT":"C",	"TGC":"C",	"TGA":"*",	"TGG":"W",	"CTT":"L",	"CTC":"L",	"CTA":"L",	"CTG":"L",	"CCT":"P",	"CCC":"P",	"CCA":"P",	"CCG":"P",	"CAT":"H",	"CAC":"H",	"CAA":"Q",	"CAG":"Q",	"CGT":"R",	"CGC":"R",	"CGA":"R",	"CGG":"R",	"ATT":"I",	"ATC":"I",	"ATA":"I",	"ATG":"M",	"ACT":"T",	"ACC":"T",	"ACA":"T",	"ACG":"T",	"AAT":"N",	"AAC":"N",	"AAA":"K",	"AAG":"K",	"AGT":"S",	"AGC":"S",	"AGA":"R",	"AGG":"R",	"GTT":"V",	"GTC":"V",	"GTA":"V",	"GTG":"V",	"GCT":"A",	"GCC":"A",	"GCA":"A",	"GCG":"A",	"GAT":"D",	"GAC":"D",	"GAA":"E",	"GAG":"E",	"GGT":"G",	"GGC":"G",	"GGA":"G",	"GGG":"G"},'invertebrateMt':{'CTT': 'L', 'TAG': '*', 'ACA': 'T', 'ACG': 'T', 'ATC': 'I', 'AAC': 'N', 'ATA': 'M', 'AGG': 'S', 'CCT': 'P', 'ACT': 'T', 'AGC': 'S', 'AAG': 'K', 'AGA': 'S', 'CAT': 'H', 'AAT': 'N', 'ATT': 'I', 'CTG': 'L', 'CTA': 'L', 'CTC': 'L', 'CAC': 'H', 'AAA': 'K', 'CCG': 'P', 'AGT': 'S', 'CCA': 'P', 'CAA': 'Q', 'CCC': 'P', 'TAT': 'Y', 'GGT': 'G', 'TGT': 'C', 'CGA': 'R', 'CAG': 'Q', 'TCT': 'S', 'GAT': 'D', 'CGG': 'R', 'TTT': 'F', 'TGC': 'C', 'GGG': 'G', 'TGA': 'W', 'GGA': 'G', 'TGG': 'W', 'GGC': 'G', 'TAC': 'Y', 'TTC': 'F', 'TCG': 'S', 'TTA': 'L', 'TTG': 'L', 'TCC': 'S', 'ACC': 'T', 'TAA': '*', 'GCA': 'A', 'GTA': 'V', 'GCC': 'A', 'GTC': 'V', 'GCG': 'A', 'GTG': 'V', 'GAG': 'E', 'GTT': 'V', 'GCT': 'A', 'GAC': 'D', 'CGT': 'R', 'GAA': 'E', 'TCA': 'S', 'ATG': 'M', 'CGC': 'R'},'vertebrateMt':{'CTT': 'L', 'TAG': '*', 'ACA': 'T', 'ACG': 'T', 'ATC': 'I', 'AAC': 'N', 'ATA': 'M', 'AGG': '*', 'CCT': 'P', 'ACT': 'T', 'AGC': 'S', 'AAG': 'K', 'AGA': '*', 'CAT': 'H', 'AAT': 'N', 'ATT': 'I', 'CTG': 'L', 'CTA': 'L', 'CTC': 'L', 'CAC': 'H', 'AAA': 'K', 'CCG': 'P', 'AGT': 'S', 'CCA': 'P', 'CAA': 'Q', 'CCC': 'P', 'TAT': 'Y', 'GGT': 'G', 'TGT': 'C', 'CGA': 'R', 'CAG': 'Q', 'TCT': 'S', 'GAT': 'D', 'CGG': 'R', 'TTT': 'F', 'TGC': 'C', 'GGG': 'G', 'TGA': 'W', 'GGA': 'G', 'TGG': 'W', 'GGC': 'G', 'TAC': 'Y', 'TTC': 'F', 'TCG': 'S', 'TTA': 'L', 'TTG': 'L', 'TCC': 'S', 'ACC': 'T', 'TAA': '*', 'GCA': 'A', 'GTA': 'V', 'GCC': 'A', 'GTC': 'V', 'GCG': 'A', 'GTG': 'V', 'GAG': 'E', 'GTT': 'V', 'GCT': 'A', 'GAC': 'D', 'CGT': 'R', 'GAA': 'E', 'TCA': 'S', 'ATG': 'M', 'CGC': 'R'}, 'yeastMt':{'CTT': 'T', 'TAG': '*', 'ACA': 'T', 'ACG': 'T', 'ATC': 'I', 'AAC': 'N', 'ATA': 'M', 'AGG': 'R', 'CCT': 'P', 'ACT': 'T', 'AGC': 'S', 'AAG': 'K', 'AGA': 'R', 'CAT': 'H', 'AAT': 'N', 'ATT': 'I', 'CTG': 'T', 'CTA': 'T', 'CTC': 'T', 'CAC': 'H', 'AAA': 'K', 'CCG': 'P', 'AGT': 'S', 'CCA': 'P', 'CAA': 'Q', 'CCC': 'P', 'TAT': 'Y', 'GGT': 'G', 'TGT': 'C', 'CGA': 'R', 'CAG': 'Q', 'TCT': 'S', 'GAT': 'D', 'CGG': 'R', 'TTT': 'F', 'TGC': 'C', 'GGG': 'G', 'TGA': 'W', 'GGA': 'G', 'TGG': 'W', 'GGC': 'G', 'TAC': 'Y', 'TTC': 'F', 'TCG': 'S', 'TTA': 'L', 'TTG': 'L', 'TCC': 'S', 'ACC': 'T', 'TAA': '*', 'GCA': 'A', 'GTA': 'V', 'GCC': 'A', 'GTC': 'V', 'GCG': 'A', 'GTG': 'V', 'GAG': 'E', 'GTT': 'V', 'GCT': 'A', 'GAC': 'D', 'CGT': 'R', 'GAA': 'E', 'TCA': 'S', 'ATG': 'M', 'CGC': 'R'}, 'coelenterateMt':{'CTT': 'L', 'TAG': '*', 'ACA': 'T', 'ACG': 'T', 'ATC': 'I', 'AAC': 'N', 'ATA': 'I', 'AGG': 'R', 'CCT': 'P', 'ACT': 'T', 'AGC': 'S', 'AAG': 'K', 'AGA': 'R', 'CAT': 'H', 'AAT': 'N', 'ATT': 'I', 'CTG': 'L', 'CTA': 'L', 'CTC': 'L', 'CAC': 'H', 'AAA': 'K', 'CCG': 'P', 'AGT': 'S', 'CCA': 'P', 'CAA': 'Q', 'CCC': 'P', 'TAT': 'Y', 'GGT': 'G', 'TGT': 'C', 'CGA': 'R', 'CAG': 'Q', 'TCT': 'S', 'GAT': 'D', 'CGG': 'R', 'TTT': 'F', 'TGC': 'C', 'GGG': 'G', 'TGA': 'W', 'GGA': 'G', 'TGG': 'W', 'GGC': 'G', 'TAC': 'Y', 'TTC': 'F', 'TCG': 'S', 'TTA': 'L', 'TTG': 'L', 'TCC': 'S', 'ACC': 'T', 'TAA': '*', 'GCA': 'A', 'GTA': 'V', 'GCC': 'A', 'GTC': 'V', 'GCG': 'A', 'GTG': 'V', 'GAG': 'E', 'GTT': 'V', 'GCT': 'A', 'GAC': 'D', 'CGT': 'R', 'GAA': 'E', 'TCA': 'S', 'ATG': 'M', 'CGC': 'R'},'ciliateNuc':{'CTT': 'L', 'TAG': 'Q', 'ACA': 'T', 'ACG': 'T', 'ATC': 'I', 'AAC': 'N', 'ATA': 'I', 'AGG': 'R', 'CCT': 'P', 'ACT': 'T', 'AGC': 'S', 'AAG': 'K', 'AGA': 'R', 'CAT': 'H', 'AAT': 'N', 'ATT': 'I', 'CTG': 'L', 'CTA': 'L', 'CTC': 'L', 'CAC': 'H', 'AAA': 'K', 'CCG': 'P', 'AGT': 'S', 'CCA': 'P', 'CAA': 'Q', 'CCC': 'P', 'TAT': 'Y', 'GGT': 'G', 'TGT': 'C', 'CGA': 'R', 'CAG': 'Q', 'TCT': 'S', 'GAT': 'D', 'CGG': 'R', 'TTT': 'F', 'TGC': 'C', 'GGG': 'G', 'TGA': '*', 'GGA': 'G', 'TGG': 'W', 'GGC': 'G', 'TAC': 'Y', 'TTC': 'F', 'TCG': 'S', 'TTA': 'L', 'TTG': 'L', 'TCC': 'S', 'ACC': 'T', 'TAA': 'Q', 'GCA': 'A', 'GTA': 'V', 'GCC': 'A', 'GTC': 'V', 'GCG': 'A', 'GTG': 'V', 'GAG': 'E', 'GTT': 'V', 'GCT': 'A', 'GAC': 'D', 'CGT': 'R', 'GAA': 'E', 'TCA': 'S', 'ATG': 'M', 'CGC': 'R'},'echinodermMt':{'CTT': 'L', 'TAG': '*', 'ACA': 'T', 'ACG': 'T', 'ATC': 'I', 'AAC': 'N', 'ATA': 'I', 'AGG': 'S', 'CCT': 'P', 'ACT': 'T', 'AGC': 'S', 'AAG': 'K', 'AGA': 'S', 'CAT': 'H', 'AAT': 'N', 'ATT': 'I', 'CTG': 'L', 'CTA': 'L', 'CTC': 'L', 'CAC': 'H', 'AAA': 'N', 'CCG': 'P', 'AGT': 'S', 'CCA': 'P', 'CAA': 'Q', 'CCC': 'P', 'TAT': 'Y', 'GGT': 'G', 'TGT': 'C', 'CGA': 'R', 'CAG': 'Q', 'TCT': 'S', 'GAT': 'D', 'CGG': 'R', 'TTT': 'F', 'TGC': 'C', 'GGG': 'G', 'TGA': 'W', 'GGA': 'G', 'TGG': 'W', 'GGC': 'G', 'TAC': 'Y', 'TTC': 'F', 'TCG': 'S', 'TTA': 'L', 'TTG': 'L', 'TCC': 'S', 'ACC': 'T', 'TAA': '*', 'GCA': 'A', 'GTA': 'V', 'GCC': 'A', 'GTC': 'V', 'GCG': 'A', 'GTG': 'V', 'GAG': 'E', 'GTT': 'V', 'GCT': 'A', 'GAC': 'D', 'CGT': 'R', 'GAA': 'E', 'TCA': 'S', 'ATG': 'M', 'CGC': 'R'}, 'euplotidNuc':{'CTT': 'L', 'TAG': '*', 'ACA': 'T', 'ACG': 'T', 'ATC': 'I', 'AAC': 'N', 'ATA': 'I', 'AGG': 'R', 'CCT': 'P', 'ACT': 'T', 'AGC': 'S', 'AAG': 'K', 'AGA': 'R', 'CAT': 'H', 'AAT': 'N', 'ATT': 'I', 'CTG': 'L', 'CTA': 'L', 'CTC': 'L', 'CAC': 'H', 'AAA': 'K', 'CCG': 'P', 'AGT': 'S', 'CCA': 'P', 'CAA': 'Q', 'CCC': 'P', 'TAT': 'Y', 'GGT': 'G', 'TGT': 'C', 'CGA': 'R', 'CAG': 'Q', 'TCT': 'S', 'GAT': 'D', 'CGG': 'R', 'TTT': 'F', 'TGC': 'C', 'GGG': 'G', 'TGA': 'C', 'GGA': 'G', 'TGG': 'W', 'GGC': 'G', 'TAC': 'Y', 'TTC': 'F', 'TCG': 'S', 'TTA': 'L', 'TTG': 'L', 'TCC': 'S', 'ACC': 'T', 'TAA': '*', 'GCA': 'A', 'GTA': 'V', 'GCC': 'A', 'GTC': 'V', 'GCG': 'A', 'GTG': 'V', 'GAG': 'E', 'GTT': 'V', 'GCT': 'A', 'GAC': 'D', 'CGT': 'R', 'GAA': 'E', 'TCA': 'S', 'ATG': 'M', 'CGC': 'R'}, 'bacterial':{'CTT': 'L', 'TAG': '*', 'ACA': 'T', 'ACG': 'T', 'ATC': 'I', 'AAC': 'N', 'ATA': 'I', 'AGG': 'R', 'CCT': 'P', 'ACT': 'T', 'AGC': 'S', 'AAG': 'K', 'AGA': 'R', 'CAT': 'H', 'AAT': 'N', 'ATT': 'I', 'CTG': 'L', 'CTA': 'L', 'CTC': 'L', 'CAC': 'H', 'AAA': 'K', 'CCG': 'P', 'AGT': 'S', 'CCA': 'P', 'CAA': 'Q', 'CCC': 'P', 'TAT': 'Y', 'GGT': 'G', 'TGT': 'C', 'CGA': 'R', 'CAG': 'Q', 'TCT': 'S', 'GAT': 'D', 'CGG': 'R', 'TTT': 'F', 'TGC': 'C', 'GGG': 'G', 'TGA': '*', 'GGA': 'G', 'TGG': 'W', 'GGC': 'G', 'TAC': 'Y', 'TTC': 'F', 'TCG': 'S', 'TTA': 'L', 'TTG': 'L', 'TCC': 'S', 'ACC': 'T', 'TAA': '*', 'GCA': 'A', 'GTA': 'V', 'GCC': 'A', 'GTC': 'V', 'GCG': 'A', 'GTG': 'V', 'GAG': 'E', 'GTT': 'V', 'GCT': 'A', 'GAC': 'D', 'CGT': 'R', 'GAA': 'E', 'TCA': 'S', 'ATG': 'M', 'CGC': 'R'},'yeastNuc':{'CTT': 'L', 'TAG': '*', 'ACA': 'T', 'ACG': 'T', 'ATC': 'I', 'AAC': 'N', 'ATA': 'I', 'AGG': 'R', 'CCT': 'P', 'ACT': 'T', 'AGC': 'S', 'AAG': 'K', 'AGA': 'R', 'CAT': 'H', 'AAT': 'N', 'ATT': 'I', 'CTG': 'S', 'CTA': 'L', 'CTC': 'L', 'CAC': 'H', 'AAA': 'K', 'CCG': 'P', 'AGT': 'S', 'CCA': 'P', 'CAA': 'Q', 'CCC': 'P', 'TAT': 'Y', 'GGT': 'G', 'TGT': 'C', 'CGA': 'R', 'CAG': 'Q', 'TCT': 'S', 'GAT': 'D', 'CGG': 'R', 'TTT': 'F', 'TGC': 'C', 'GGG': 'G', 'TGA': '*', 'GGA': 'G', 'TGG': 'W', 'GGC': 'G', 'TAC': 'Y', 'TTC': 'F', 'TCG': 'S', 'TTA': 'L', 'TTG': 'L', 'TCC': 'S', 'ACC': 'T', 'TAA': '*', 'GCA': 'A', 'GTA': 'V', 'GCC': 'A', 'GTC': 'V', 'GCG': 'A', 'GTG': 'V', 'GAG': 'E', 'GTT': 'V', 'GCT': 'A', 'GAC': 'D', 'CGT': 'R', 'GAA': 'E', 'TCA': 'S', 'ATG': 'M', 'CGC': 'R'}, 'ascidianMt':{'CTT': 'L', 'TAG': '*', 'ACA': 'T', 'ACG': 'T', 'ATC': 'I', 'AAC': 'N', 'ATA': 'M', 'AGG': 'G', 'CCT': 'P', 'ACT': 'T', 'AGC': 'S', 'AAG': 'K', 'AGA': 'G', 'CAT': 'H', 'AAT': 'N', 'ATT': 'I', 'CTG': 'L', 'CTA': 'L', 'CTC': 'L', 'CAC': 'H', 'AAA': 'K', 'CCG': 'P', 'AGT': 'S', 'CCA': 'P', 'CAA': 'Q', 'CCC': 'P', 'TAT': 'Y', 'GGT': 'G', 'TGT': 'C', 'CGA': 'R', 'CAG': 'Q', 'TCT': 'S', 'GAT': 'D', 'CGG': 'R', 'TTT': 'F', 'TGC': 'C', 'GGG': 'G', 'TGA': 'W', 'GGA': 'G', 'TGG': 'W', 'GGC': 'G', 'TAC': 'Y', 'TTC': 'F', 'TCG': 'S', 'TTA': 'L', 'TTG': 'L', 'TCC': 'S', 'ACC': 'T', 'TAA': '*', 'GCA': 'A', 'GTA': 'V', 'GCC': 'A', 'GTC': 'V', 'GCG': 'A', 'GTG': 'V', 'GAG': 'E', 'GTT': 'V', 'GCT': 'A', 'GAC': 'D', 'CGT': 'R', 'GAA': 'E', 'TCA': 'S', 'ATG': 'M', 'CGC': 'R'},'flatwormMt':{'CTT': 'L', 'TAG': '*', 'ACA': 'T', 'ACG': 'T', 'ATC': 'I', 'AAC': 'N', 'ATA': 'I', 'AGG': 'S', 'CCT': 'P', 'ACT': 'T', 'AGC': 'S', 'AAG': 'K', 'AGA': 'S', 'CAT': 'H', 'AAT': 'N', 'ATT': 'I', 'CTG': 'L', 'CTA': 'L', 'CTC': 'L', 'CAC': 'H', 'AAA': 'N', 'CCG': 'P', 'AGT': 'S', 'CCA': 'P', 'CAA': 'Q', 'CCC': 'P', 'TAT': 'Y', 'GGT': 'G', 'TGT': 'C', 'CGA': 'R', 'CAG': 'Q', 'TCT': 'S', 'GAT': 'D', 'CGG': 'R', 'TTT': 'F', 'TGC': 'C', 'GGG': 'G', 'TGA': 'W', 'GGA': 'G', 'TGG': 'W', 'GGC': 'G', 'TAC': 'Y', 'TTC': 'F', 'TCG': 'S', 'TTA': 'L', 'TTG': 'L', 'TCC': 'S', 'ACC': 'T', 'TAA': 'Y', 'GCA': 'A', 'GTA': 'V', 'GCC': 'A', 'GTC': 'V', 'GCG': 'A', 'GTG': 'V', 'GAG': 'E', 'GTT': 'V', 'GCT': 'A', 'GAC': 'D', 'CGT': 'R', 'GAA': 'E', 'TCA': 'S', 'ATG': 'M', 'CGC': 'R'},'chlorophyceanMt':{'CTT': 'L', 'TAG': 'L', 'ACA': 'T', 'ACG': 'T', 'ATC': 'I', 'AAC': 'N', 'ATA': 'I', 'AGG': 'R', 'CCT': 'P', 'ACT': 'T', 'AGC': 'S', 'AAG': 'K', 'AGA': 'R', 'CAT': 'H', 'AAT': 'N', 'ATT': 'I', 'CTG': 'L', 'CTA': 'L', 'CTC': 'L', 'CAC': 'H', 'AAA': 'K', 'CCG': 'P', 'AGT': 'S', 'CCA': 'P', 'CAA': 'Q', 'CCC': 'P', 'TAT': 'Y', 'GGT': 'G', 'TGT': 'C', 'CGA': 'R', 'CAG': 'Q', 'TCT': 'S', 'GAT': 'D', 'CGG': 'R', 'TTT': 'F', 'TGC': 'C', 'GGG': 'G', 'TGA': '*', 'GGA': 'G', 'TGG': 'W', 'GGC': 'G', 'TAC': 'Y', 'TTC': 'F', 'TCG': 'S', 'TTA': 'L', 'TTG': 'L', 'TCC': 'S', 'ACC': 'T', 'TAA': '*', 'GCA': 'A', 'GTA': 'V', 'GCC': 'A', 'GTC': 'V', 'GCG': 'A', 'GTG': 'V', 'GAG': 'E', 'GTT': 'V', 'GCT': 'A', 'GAC': 'D', 'CGT': 'R', 'GAA': 'E', 'TCA': 'S', 'ATG': 'M', 'CGC': 'R'},'trematodeMt':{'CTT': 'L', 'TAG': '*', 'ACA': 'T', 'ACG': 'T', 'ATC': 'I', 'AAC': 'N', 'ATA': 'M', 'AGG': 'S', 'CCT': 'P', 'ACT': 'T', 'AGC': 'S', 'AAG': 'K', 'AGA': 'S', 'CAT': 'H', 'AAT': 'N', 'ATT': 'I', 'CTG': 'L', 'CTA': 'L', 'CTC': 'L', 'CAC': 'H', 'AAA': 'N', 'CCG': 'P', 'AGT': 'S', 'CCA': 'P', 'CAA': 'Q', 'CCC': 'P', 'TAT': 'Y', 'GGT': 'G', 'TGT': 'C', 'CGA': 'R', 'CAG': 'Q', 'TCT': 'S', 'GAT': 'D', 'CGG': 'R', 'TTT': 'F', 'TGC': 'C', 'GGG': 'G', 'TGA': 'W', 'GGA': 'G', 'TGG': 'W', 'GGC': 'G', 'TAC': 'Y', 'TTC': 'F', 'TCG': 'S', 'TTA': 'L', 'TTG': 'L', 'TCC': 'S', 'ACC': 'T', 'TAA': '*', 'GCA': 'A', 'GTA': 'V', 'GCC': 'A', 'GTC': 'V', 'GCG': 'A', 'GTG': 'V', 'GAG': 'E', 'GTT': 'V', 'GCT': 'A', 'GAC': 'D', 'CGT': 'R', 'GAA': 'E', 'TCA': 'S', 'ATG': 'M', 'CGC': 'R'},'pterobranchiaMt':{'CTT': 'L', 'TAG': '*', 'ACA': 'T', 'ACG': 'T', 'ATC': 'I', 'AAC': 'N', 'ATA': 'I', 'AGG': 'K', 'CCT': 'P', 'ACT': 'T', 'AGC': 'S', 'AAG': 'K', 'AGA': 'S', 'CAT': 'H', 'AAT': 'N', 'ATT': 'I', 'CTG': 'L', 'CTA': 'L', 'CTC': 'L', 'CAC': 'H', 'AAA': 'K', 'CCG': 'P', 'AGT': 'S', 'CCA': 'P', 'CAA': 'Q', 'CCC': 'P', 'TAT': 'Y', 'GGT': 'G', 'TGT': 'C', 'CGA': 'R', 'CAG': 'Q', 'TCT': 'S', 'GAT': 'D', 'CGG': 'R', 'TTT': 'F', 'TGC': 'C', 'GGG': 'G', 'TGA': 'W', 'GGA': 'G', 'TGG': 'W', 'GGC': 'G', 'TAC': 'Y', 'TTC': 'F', 'TCG': 'S', 'TTA': 'L', 'TTG': 'L', 'TCC': 'S', 'ACC': 'T', 'TAA': '*', 'GCA': 'A', 'GTA': 'V', 'GCC': 'A', 'GTC': 'V', 'GCG': 'A', 'GTG': 'V', 'GAG': 'E', 'GTT': 'V', 'GCT': 'A', 'GAC': 'D', 'CGT': 'R', 'GAA': 'E', 'TCA': 'S', 'ATG': 'M', 'CGC': 'R'}}
    geneticCode = geneticCodes[code]
    startCodons = ['ATT','ATC','ATA','ATG','GTG']
    seqDict,seqList = buildSeqDict(fasta)
    codonDict = {}
    AADict = {}
    for seq in seqList:
        nucleotideSeq = seqDict[seq]
        codonList = []
        i = 2
        while i < len(nucleotideSeq):
            currCodon = nucleotideSeq[i-2] + nucleotideSeq[i-1] + nucleotideSeq[i]
            codonList.append(currCodon)
            i += 3
        codonDict[seq] = codonList
        AAseq = ''
        codonNum = 1
        for codon in codonList:
            if codonNum == 1 and 'N' not in codon and '-' not in codon:
                if codon in startCodons:
                    aa = 'M'
                else:
                    aa = geneticCode[codon]
            elif 'N' not in codon and '-' not in codon:
                aa = geneticCode[codon]
            else:
                aa = 'X'
            AAseq += aa
            codonNum += 1
        if AAseq[-1] == '*':
            AAseq = AAseq[0:-1]
        AADict[seq] = AAseq
    return seqDict, seqList, codonDict

def buildSeqDict(fasta):
    infile = open(fasta,'r')
    scaffoldDict = {}
    scaffoldList = []
    seqName = ''
    currSeq = ''
    for line in infile:
        if line[0] == '>':
            if seqName != '':
                scaffoldDict[seqName] = currSeq
            seqName = line
            while seqName[-1] == '\n' or seqName[-1] == '\t' or seqName[-1] == '\r':
                seqName = seqName[0:-1]
            scaffoldList.append(seqName)
            currSeq = ''
        else:
            currSeq += line
            while currSeq[-1] == '\n' or currSeq[-1] == '\t' or currSeq[-1] == '\r':
                currSeq = currSeq[0:-1]
    scaffoldDict[seqName] = currSeq 
    return scaffoldDict, scaffoldList

def meanSites(fasta):
    asexList = ['>$Duluth','>$Heron2','>$McGregor','>$Waik36','>$WalesC','>$clone_1','>$AC51','>$Heron_mitochondrion','>$clone_7','>$Waik37','>$Gunn','>$DenmarkA','>$Waik372','>$Tarawera','>$Poerua_triploid','>$Kaniere_triploid','>$Waik_lane4_TCCTGAGC_trimmed_paired_contig_237','>$Brunner_2_4n','>$Brunner_6_3n','>$Grasmere_1_4n','>$Grasmere_6_3n','>$Poerua_72_4n','>$Rotoiti_1_4n']
    sexList = ['>$*Kaniere_1_2n','>$*Ianthe_lane1_TAAGGCGA_trimmed_paired_contig_309','>$*Yellow_Contig_56','>$*Alexsex','>$*AlexMap','>$*Lady','>$*Ianthe','>$*Rotoroa_1_2n']
    antipodarumList = ['>$Duluth','>$Heron2','>$McGregor','>$Waik36','>$WalesC','>$clone_1','>$AC51','>$Heron_mitochondrion','>$clone_7','>$Waik37','>$Gunn','>$DenmarkA','>$Waik372','>$Tarawera','>$Poerua_triploid','>$Kaniere_triploid','>$Waik_lane4_TCCTGAGC_trimmed_paired_contig_237','>$Brunner_2_4n','>$Brunner_6_3n','>$Grasmere_1_4n','>$Grasmere_6_3n','>$Poerua_72_4n','>$Rotoiti_1_4n','>$*Kaniere_1_2n','>$*Ianthe_lane1_TAAGGCGA_trimmed_paired_contig_309','>$*Yellow_Contig_56','>$*Alexsex','>$*AlexMap','>$*Lady','>$*Ianthe','>$*Rotoroa_1_2n']
    seqDict, seqList, codonDict = buildCodonDict(fasta)
    sexS = 0
    sexN = 0
    sexC1 = 0
    sexR1 = 0
    sexC2 = 0
    sexR2 = 0
    sexC3 = 0
    sexR3 = 0
    sexC4 = 0
    sexR4 = 0
    sexC5 = 0
    sexR5 = 0
    sexC6 = 0
    sexR6 = 0
    sexC7 = 0
    sexR7 = 0
    asexS = 0
    asexN = 0
    asexC1 = 0
    asexR1 = 0
    asexC2 = 0
    asexR2 = 0
    asexC3 = 0
    asexR3 = 0
    asexC4 = 0
    asexR4 = 0
    asexC5 = 0
    asexR5 = 0
    asexC6 = 0
    asexR6 = 0
    asexC7 = 0
    asexR7 = 0
    S = 0
    N = 0
    C1 = 0
    R1 = 0
    C2 = 0
    R2 = 0
    C3 = 0
    R3 = 0
    C4 = 0
    R4 = 0
    C5 = 0
    R5 = 0
    C6 = 0
    R6 = 0
    C7 = 0
    R7 = 0
    est = countSites(codonDict['>Potamopyrgus_estuarinus'])
    estS = est[0]
    estN = est[1]
    estC1 = est[2]
    estR1 = est[3]
    estC2 = est[4]
    estR2 = est[5]
    estC3 = est[6]
    estR3 = est[7]
    estC4 = est[8]
    estR4 = est[9]
    estC5 = est[10]
    estR5 = est[11]
    estC6 = est[12]
    estR6 = est[13]
    estC7 = est[14]
    estR7 =  est[15]
    outfile = open('sites.txt','w')
    for snail in antipodarumList:
        snailSites = countSites(codonDict[snail])
        S += snailSites[0]
        N += snailSites[1]
        R1 += snailSites[2]
        C1 += snailSites[3]
        R2 += snailSites[4]
        C2 += snailSites[5]
        R3 += snailSites[6]
        C3 += snailSites[7]
        R4 += snailSites[8]
        C4 += snailSites[9]
        R5 += snailSites[10]
        C5 += snailSites[11]
        R6 += snailSites[12]
        C6 += snailSites[13]
        R7 += snailSites[14]
        C7 += snailSites[15]
        if snail in sexList:
            sexS += snailSites[0]
            sexN += snailSites[1]
            sexR1 += snailSites[2]
            sexC1 += snailSites[3]
            sexR2 += snailSites[4]
            sexC2 += snailSites[5]
            sexR3 += snailSites[6]
            sexC3 += snailSites[7]
            sexR4 += snailSites[8]
            sexC4 += snailSites[9]
            sexR5 += snailSites[10]
            sexC5 += snailSites[11]
            sexR6 += snailSites[12]
            sexC6 += snailSites[13]
            sexR7 += snailSites[14]
            sexC7 += snailSites[15]
        elif snail in asexList:
            asexS += snailSites[0]
            asexN += snailSites[1]
            asexR1 += snailSites[2]
            asexC1 += snailSites[3]
            asexR2 += snailSites[4]
            asexC2 += snailSites[5]
            asexR3 += snailSites[6]
            asexC3 += snailSites[7]
            asexR4 += snailSites[8]
            asexC4 += snailSites[9]
            asexR5 += snailSites[10]
            asexC5 += snailSites[11]
            asexR6 += snailSites[12]
            asexC6 += snailSites[13]
            asexR7 += snailSites[14]
            asexC7 += snailSites[15]
    sexS /= len(sexList)
    sexN /= len(sexList)
    sexC1 /= len(sexList)
    sexR1 /= len(sexList)
    sexC2 /= len(sexList)
    sexR2 /= len(sexList)
    sexC3 /= len(sexList)
    sexR3 /= len(sexList)
    sexC4 /= len(sexList)
    sexR4 /= len(sexList)
    sexC5 /= len(sexList)
    sexR5 /= len(sexList)
    sexC6 /= len(sexList)
    sexR6 /= len(sexList)
    sexC7 /= len(sexList)
    sexR7 /= len(sexList)
    asexS /= len(asexList)
    asexN /= len(asexList)
    asexC1 /= len(asexList)
    asexR1 /= len(asexList)
    asexC2 /= len(asexList)
    asexR2 /= len(asexList)
    asexC3 /= len(asexList)
    asexR3 /= len(asexList)
    asexC4 /= len(asexList)
    asexR4 /= len(asexList)
    asexC5 /= len(asexList)
    asexR5 /= len(asexList)
    asexC6 /= len(asexList)
    asexR6 /= len(asexList)
    asexC7 /= len(asexList)
    asexR7 /= len(asexList)
    divS = (S + estS)/(len(antipodarumList) + 1)
    divN = (N + estN)/(len(antipodarumList) + 1)
    divC1 = (C1 + estC1)/(len(antipodarumList) + 1)
    divR1 = (R1 + estR1)/(len(antipodarumList) + 1)
    divC2 = (C2 + estC2)/(len(antipodarumList) + 1)
    divR2 = (R2 + estR2)/(len(antipodarumList) + 1)
    divC3 = (C3 + estC3)/(len(antipodarumList) + 1)
    divR3 = (R3 + estR3)/(len(antipodarumList) + 1)
    divC4 = (C4 + estC4)/(len(antipodarumList) + 1)
    divR4 = (R4 + estR4)/(len(antipodarumList) + 1)
    divC5 = (C5 + estC5)/(len(antipodarumList) + 1)
    divR5 = (R5 + estR5)/(len(antipodarumList) + 1)
    divC6 = (C6 + estC6)/(len(antipodarumList) + 1)
    divR6 = (R6 + estR6)/(len(antipodarumList) + 1)
    divC7 = (C7 + estC7)/(len(antipodarumList) + 1)
    divR7 = (R7 + estR7)/(len(antipodarumList) + 1)
    S /= len(antipodarumList)
    N /= len(antipodarumList)
    C1 /= len(antipodarumList)
    R1 /= len(antipodarumList)
    C2 /= len(antipodarumList)
    R2 /= len(antipodarumList)
    C3 /= len(antipodarumList)
    R3 /= len(antipodarumList)
    C4 /= len(antipodarumList)
    R4 /= len(antipodarumList)
    C5 /= len(antipodarumList)
    R5 /= len(antipodarumList)
    C6 /= len(antipodarumList)
    R6 /= len(antipodarumList)
    C7 /= len(antipodarumList)
    R7 /= len(antipodarumList)
    meanC = (C1 + C2 + C3 + C4 + C5 + C6 + C7)/7
    meanR = (R1 + R2 + R3 + R4 + R5 + R6 + R7)/7
    meanDivC = (divC1 + divC2 + divC3 + divC4 + divC5 + divC6 + divC7)/7
    meanDivR = (divR1 + divR2 + divR3 + divR4 + divR5 + divR6 + divR7)/7
    meanSexC = (sexC1 + sexC2 + sexC3 + sexC4 + sexC5 + sexC6 + sexC7)/7
    meanSexR = (sexR1 + sexR2 + sexR3 + sexR4 + sexR5 + sexR6 + sexR7)/7
    meanAsexC = (asexC1 + asexC2 + asexC3 + asexC4 + asexC5 + asexC6 + asexC7)/7
    meanAsexR = (asexR1 + asexR2 + asexR3 + asexR4 + asexR5 + asexR6 + asexR7)/7
    outfile.write('Group\tS\tN\tC1\tR1\tC2\tR2\tC3\tR3\tC4\tR4\tC5\tR5\tC6\tR6\tC7\tR7\tmeanC\tmeanR\nP.antipodarum-P.estuarinus\t' + str(divS) + '\t' + str(divN) + '\t' + str(divC1) + '\t' + str(divR1) + '\t' + str(divC2) + '\t' + str(divR2) + '\t' + str(divC3) + '\t' + str(divR3) + '\t' + str(divC4) + '\t' + str(divR4) + '\t' + str(divC5) + '\t' + str(divR5) + '\t' + str(divC6) + '\t' + str(divR6) + '\t' + str(divC7) + '\t' + str(divR7) + '\t' + str(meanDivC) + '\t' + str(meanDivR) + '\nP.antipodarum\t' + str(S) + '\t' + str(N) + '\t' + str(C1) + '\t' + str(R1) + '\t' + str(C2) + '\t' + str(R2) + '\t' + str(C3) + '\t' + str(R3) + '\t' + str(C4) + '\t' + str(R4) + '\t' + str(C5) + '\t' + str(R5) + '\t' + str(C6) + '\t' + str(R6) + '\t' + str(C7) + '\t' + str(R7) + '\t' + str(meanC) + '\t' + str(meanR) + '\nSex\t' + str(sexS) + '\t' + str(sexN) + '\t' + str(sexC1) + '\t' + str(sexR1) + '\t' + str(sexC2) + '\t' + str(sexR2) + '\t' + str(sexC3) + '\t' + str(sexR3) + '\t' + str(sexC4) + '\t' + str(sexR4) + '\t' + str(sexC5) + '\t' + str(sexR5) + '\t' + str(sexC6) + '\t' + str(sexR6) + '\t' + str(sexC7) + '\t' + str(sexR7) + '\t' + str(meanSexC) + '\t' + str(meanSexR) + '\nAsex\t' + str(asexS) + '\t' + str(asexN) + '\t' + str(asexC1) + '\t' + str(asexR1) + '\t' + str(asexC2) + '\t' + str(asexR2) + '\t' + str(asexC3) + '\t' + str(asexR3) + '\t' + str(asexC4) + '\t' + str(asexR4) + '\t' + str(asexC5) + '\t' + str(asexR5) + '\t' + str(asexC6) + '\t' + str(asexR6) + '\t' + str(asexC7) + '\t' + str(asexR7) + '\t' + str(meanAsexC) + '\t' + str(meanAsexR) + '\n')
    outfile.close()

def countSites(codonList):
    code = 'invertebrateMt'
    geneticCodes = {'standard':{"TTT":"F",	"TTC":"F",	"TTA":"L",	"TTG":"L",	"TCT":"S",	"TCC":"S",	"TCA":"S",	"TCG":"S",	"TAT":"Y",	"TAC":"Y",	"TAA":"*",	"TAG":"*",	"TGT":"C",	"TGC":"C",	"TGA":"*",	"TGG":"W",	"CTT":"L",	"CTC":"L",	"CTA":"L",	"CTG":"L",	"CCT":"P",	"CCC":"P",	"CCA":"P",	"CCG":"P",	"CAT":"H",	"CAC":"H",	"CAA":"Q",	"CAG":"Q",	"CGT":"R",	"CGC":"R",	"CGA":"R",	"CGG":"R",	"ATT":"I",	"ATC":"I",	"ATA":"I",	"ATG":"M",	"ACT":"T",	"ACC":"T",	"ACA":"T",	"ACG":"T",	"AAT":"N",	"AAC":"N",	"AAA":"K",	"AAG":"K",	"AGT":"S",	"AGC":"S",	"AGA":"R",	"AGG":"R",	"GTT":"V",	"GTC":"V",	"GTA":"V",	"GTG":"V",	"GCT":"A",	"GCC":"A",	"GCA":"A",	"GCG":"A",	"GAT":"D",	"GAC":"D",	"GAA":"E",	"GAG":"E",	"GGT":"G",	"GGC":"G",	"GGA":"G",	"GGG":"G"},'invertebrateMt':{'CTT': 'L', 'TAG': '*', 'ACA': 'T', 'ACG': 'T', 'ATC': 'I', 'AAC': 'N', 'ATA': 'M', 'AGG': 'S', 'CCT': 'P', 'ACT': 'T', 'AGC': 'S', 'AAG': 'K', 'AGA': 'S', 'CAT': 'H', 'AAT': 'N', 'ATT': 'I', 'CTG': 'L', 'CTA': 'L', 'CTC': 'L', 'CAC': 'H', 'AAA': 'K', 'CCG': 'P', 'AGT': 'S', 'CCA': 'P', 'CAA': 'Q', 'CCC': 'P', 'TAT': 'Y', 'GGT': 'G', 'TGT': 'C', 'CGA': 'R', 'CAG': 'Q', 'TCT': 'S', 'GAT': 'D', 'CGG': 'R', 'TTT': 'F', 'TGC': 'C', 'GGG': 'G', 'TGA': 'W', 'GGA': 'G', 'TGG': 'W', 'GGC': 'G', 'TAC': 'Y', 'TTC': 'F', 'TCG': 'S', 'TTA': 'L', 'TTG': 'L', 'TCC': 'S', 'ACC': 'T', 'TAA': '*', 'GCA': 'A', 'GTA': 'V', 'GCC': 'A', 'GTC': 'V', 'GCG': 'A', 'GTG': 'V', 'GAG': 'E', 'GTT': 'V', 'GCT': 'A', 'GAC': 'D', 'CGT': 'R', 'GAA': 'E', 'TCA': 'S', 'ATG': 'M', 'CGC': 'R'},'vertebrateMt':{'CTT': 'L', 'TAG': '*', 'ACA': 'T', 'ACG': 'T', 'ATC': 'I', 'AAC': 'N', 'ATA': 'M', 'AGG': '*', 'CCT': 'P', 'ACT': 'T', 'AGC': 'S', 'AAG': 'K', 'AGA': '*', 'CAT': 'H', 'AAT': 'N', 'ATT': 'I', 'CTG': 'L', 'CTA': 'L', 'CTC': 'L', 'CAC': 'H', 'AAA': 'K', 'CCG': 'P', 'AGT': 'S', 'CCA': 'P', 'CAA': 'Q', 'CCC': 'P', 'TAT': 'Y', 'GGT': 'G', 'TGT': 'C', 'CGA': 'R', 'CAG': 'Q', 'TCT': 'S', 'GAT': 'D', 'CGG': 'R', 'TTT': 'F', 'TGC': 'C', 'GGG': 'G', 'TGA': 'W', 'GGA': 'G', 'TGG': 'W', 'GGC': 'G', 'TAC': 'Y', 'TTC': 'F', 'TCG': 'S', 'TTA': 'L', 'TTG': 'L', 'TCC': 'S', 'ACC': 'T', 'TAA': '*', 'GCA': 'A', 'GTA': 'V', 'GCC': 'A', 'GTC': 'V', 'GCG': 'A', 'GTG': 'V', 'GAG': 'E', 'GTT': 'V', 'GCT': 'A', 'GAC': 'D', 'CGT': 'R', 'GAA': 'E', 'TCA': 'S', 'ATG': 'M', 'CGC': 'R'}, 'yeastMt':{'CTT': 'T', 'TAG': '*', 'ACA': 'T', 'ACG': 'T', 'ATC': 'I', 'AAC': 'N', 'ATA': 'M', 'AGG': 'R', 'CCT': 'P', 'ACT': 'T', 'AGC': 'S', 'AAG': 'K', 'AGA': 'R', 'CAT': 'H', 'AAT': 'N', 'ATT': 'I', 'CTG': 'T', 'CTA': 'T', 'CTC': 'T', 'CAC': 'H', 'AAA': 'K', 'CCG': 'P', 'AGT': 'S', 'CCA': 'P', 'CAA': 'Q', 'CCC': 'P', 'TAT': 'Y', 'GGT': 'G', 'TGT': 'C', 'CGA': 'R', 'CAG': 'Q', 'TCT': 'S', 'GAT': 'D', 'CGG': 'R', 'TTT': 'F', 'TGC': 'C', 'GGG': 'G', 'TGA': 'W', 'GGA': 'G', 'TGG': 'W', 'GGC': 'G', 'TAC': 'Y', 'TTC': 'F', 'TCG': 'S', 'TTA': 'L', 'TTG': 'L', 'TCC': 'S', 'ACC': 'T', 'TAA': '*', 'GCA': 'A', 'GTA': 'V', 'GCC': 'A', 'GTC': 'V', 'GCG': 'A', 'GTG': 'V', 'GAG': 'E', 'GTT': 'V', 'GCT': 'A', 'GAC': 'D', 'CGT': 'R', 'GAA': 'E', 'TCA': 'S', 'ATG': 'M', 'CGC': 'R'}, 'coelenterateMt':{'CTT': 'L', 'TAG': '*', 'ACA': 'T', 'ACG': 'T', 'ATC': 'I', 'AAC': 'N', 'ATA': 'I', 'AGG': 'R', 'CCT': 'P', 'ACT': 'T', 'AGC': 'S', 'AAG': 'K', 'AGA': 'R', 'CAT': 'H', 'AAT': 'N', 'ATT': 'I', 'CTG': 'L', 'CTA': 'L', 'CTC': 'L', 'CAC': 'H', 'AAA': 'K', 'CCG': 'P', 'AGT': 'S', 'CCA': 'P', 'CAA': 'Q', 'CCC': 'P', 'TAT': 'Y', 'GGT': 'G', 'TGT': 'C', 'CGA': 'R', 'CAG': 'Q', 'TCT': 'S', 'GAT': 'D', 'CGG': 'R', 'TTT': 'F', 'TGC': 'C', 'GGG': 'G', 'TGA': 'W', 'GGA': 'G', 'TGG': 'W', 'GGC': 'G', 'TAC': 'Y', 'TTC': 'F', 'TCG': 'S', 'TTA': 'L', 'TTG': 'L', 'TCC': 'S', 'ACC': 'T', 'TAA': '*', 'GCA': 'A', 'GTA': 'V', 'GCC': 'A', 'GTC': 'V', 'GCG': 'A', 'GTG': 'V', 'GAG': 'E', 'GTT': 'V', 'GCT': 'A', 'GAC': 'D', 'CGT': 'R', 'GAA': 'E', 'TCA': 'S', 'ATG': 'M', 'CGC': 'R'},'ciliateNuc':{'CTT': 'L', 'TAG': 'Q', 'ACA': 'T', 'ACG': 'T', 'ATC': 'I', 'AAC': 'N', 'ATA': 'I', 'AGG': 'R', 'CCT': 'P', 'ACT': 'T', 'AGC': 'S', 'AAG': 'K', 'AGA': 'R', 'CAT': 'H', 'AAT': 'N', 'ATT': 'I', 'CTG': 'L', 'CTA': 'L', 'CTC': 'L', 'CAC': 'H', 'AAA': 'K', 'CCG': 'P', 'AGT': 'S', 'CCA': 'P', 'CAA': 'Q', 'CCC': 'P', 'TAT': 'Y', 'GGT': 'G', 'TGT': 'C', 'CGA': 'R', 'CAG': 'Q', 'TCT': 'S', 'GAT': 'D', 'CGG': 'R', 'TTT': 'F', 'TGC': 'C', 'GGG': 'G', 'TGA': '*', 'GGA': 'G', 'TGG': 'W', 'GGC': 'G', 'TAC': 'Y', 'TTC': 'F', 'TCG': 'S', 'TTA': 'L', 'TTG': 'L', 'TCC': 'S', 'ACC': 'T', 'TAA': 'Q', 'GCA': 'A', 'GTA': 'V', 'GCC': 'A', 'GTC': 'V', 'GCG': 'A', 'GTG': 'V', 'GAG': 'E', 'GTT': 'V', 'GCT': 'A', 'GAC': 'D', 'CGT': 'R', 'GAA': 'E', 'TCA': 'S', 'ATG': 'M', 'CGC': 'R'},'echinodermMt':{'CTT': 'L', 'TAG': '*', 'ACA': 'T', 'ACG': 'T', 'ATC': 'I', 'AAC': 'N', 'ATA': 'I', 'AGG': 'S', 'CCT': 'P', 'ACT': 'T', 'AGC': 'S', 'AAG': 'K', 'AGA': 'S', 'CAT': 'H', 'AAT': 'N', 'ATT': 'I', 'CTG': 'L', 'CTA': 'L', 'CTC': 'L', 'CAC': 'H', 'AAA': 'N', 'CCG': 'P', 'AGT': 'S', 'CCA': 'P', 'CAA': 'Q', 'CCC': 'P', 'TAT': 'Y', 'GGT': 'G', 'TGT': 'C', 'CGA': 'R', 'CAG': 'Q', 'TCT': 'S', 'GAT': 'D', 'CGG': 'R', 'TTT': 'F', 'TGC': 'C', 'GGG': 'G', 'TGA': 'W', 'GGA': 'G', 'TGG': 'W', 'GGC': 'G', 'TAC': 'Y', 'TTC': 'F', 'TCG': 'S', 'TTA': 'L', 'TTG': 'L', 'TCC': 'S', 'ACC': 'T', 'TAA': '*', 'GCA': 'A', 'GTA': 'V', 'GCC': 'A', 'GTC': 'V', 'GCG': 'A', 'GTG': 'V', 'GAG': 'E', 'GTT': 'V', 'GCT': 'A', 'GAC': 'D', 'CGT': 'R', 'GAA': 'E', 'TCA': 'S', 'ATG': 'M', 'CGC': 'R'}, 'euplotidNuc':{'CTT': 'L', 'TAG': '*', 'ACA': 'T', 'ACG': 'T', 'ATC': 'I', 'AAC': 'N', 'ATA': 'I', 'AGG': 'R', 'CCT': 'P', 'ACT': 'T', 'AGC': 'S', 'AAG': 'K', 'AGA': 'R', 'CAT': 'H', 'AAT': 'N', 'ATT': 'I', 'CTG': 'L', 'CTA': 'L', 'CTC': 'L', 'CAC': 'H', 'AAA': 'K', 'CCG': 'P', 'AGT': 'S', 'CCA': 'P', 'CAA': 'Q', 'CCC': 'P', 'TAT': 'Y', 'GGT': 'G', 'TGT': 'C', 'CGA': 'R', 'CAG': 'Q', 'TCT': 'S', 'GAT': 'D', 'CGG': 'R', 'TTT': 'F', 'TGC': 'C', 'GGG': 'G', 'TGA': 'C', 'GGA': 'G', 'TGG': 'W', 'GGC': 'G', 'TAC': 'Y', 'TTC': 'F', 'TCG': 'S', 'TTA': 'L', 'TTG': 'L', 'TCC': 'S', 'ACC': 'T', 'TAA': '*', 'GCA': 'A', 'GTA': 'V', 'GCC': 'A', 'GTC': 'V', 'GCG': 'A', 'GTG': 'V', 'GAG': 'E', 'GTT': 'V', 'GCT': 'A', 'GAC': 'D', 'CGT': 'R', 'GAA': 'E', 'TCA': 'S', 'ATG': 'M', 'CGC': 'R'}, 'bacterial':{'CTT': 'L', 'TAG': '*', 'ACA': 'T', 'ACG': 'T', 'ATC': 'I', 'AAC': 'N', 'ATA': 'I', 'AGG': 'R', 'CCT': 'P', 'ACT': 'T', 'AGC': 'S', 'AAG': 'K', 'AGA': 'R', 'CAT': 'H', 'AAT': 'N', 'ATT': 'I', 'CTG': 'L', 'CTA': 'L', 'CTC': 'L', 'CAC': 'H', 'AAA': 'K', 'CCG': 'P', 'AGT': 'S', 'CCA': 'P', 'CAA': 'Q', 'CCC': 'P', 'TAT': 'Y', 'GGT': 'G', 'TGT': 'C', 'CGA': 'R', 'CAG': 'Q', 'TCT': 'S', 'GAT': 'D', 'CGG': 'R', 'TTT': 'F', 'TGC': 'C', 'GGG': 'G', 'TGA': '*', 'GGA': 'G', 'TGG': 'W', 'GGC': 'G', 'TAC': 'Y', 'TTC': 'F', 'TCG': 'S', 'TTA': 'L', 'TTG': 'L', 'TCC': 'S', 'ACC': 'T', 'TAA': '*', 'GCA': 'A', 'GTA': 'V', 'GCC': 'A', 'GTC': 'V', 'GCG': 'A', 'GTG': 'V', 'GAG': 'E', 'GTT': 'V', 'GCT': 'A', 'GAC': 'D', 'CGT': 'R', 'GAA': 'E', 'TCA': 'S', 'ATG': 'M', 'CGC': 'R'},'yeastNuc':{'CTT': 'L', 'TAG': '*', 'ACA': 'T', 'ACG': 'T', 'ATC': 'I', 'AAC': 'N', 'ATA': 'I', 'AGG': 'R', 'CCT': 'P', 'ACT': 'T', 'AGC': 'S', 'AAG': 'K', 'AGA': 'R', 'CAT': 'H', 'AAT': 'N', 'ATT': 'I', 'CTG': 'S', 'CTA': 'L', 'CTC': 'L', 'CAC': 'H', 'AAA': 'K', 'CCG': 'P', 'AGT': 'S', 'CCA': 'P', 'CAA': 'Q', 'CCC': 'P', 'TAT': 'Y', 'GGT': 'G', 'TGT': 'C', 'CGA': 'R', 'CAG': 'Q', 'TCT': 'S', 'GAT': 'D', 'CGG': 'R', 'TTT': 'F', 'TGC': 'C', 'GGG': 'G', 'TGA': '*', 'GGA': 'G', 'TGG': 'W', 'GGC': 'G', 'TAC': 'Y', 'TTC': 'F', 'TCG': 'S', 'TTA': 'L', 'TTG': 'L', 'TCC': 'S', 'ACC': 'T', 'TAA': '*', 'GCA': 'A', 'GTA': 'V', 'GCC': 'A', 'GTC': 'V', 'GCG': 'A', 'GTG': 'V', 'GAG': 'E', 'GTT': 'V', 'GCT': 'A', 'GAC': 'D', 'CGT': 'R', 'GAA': 'E', 'TCA': 'S', 'ATG': 'M', 'CGC': 'R'}, 'ascidianMt':{'CTT': 'L', 'TAG': '*', 'ACA': 'T', 'ACG': 'T', 'ATC': 'I', 'AAC': 'N', 'ATA': 'M', 'AGG': 'G', 'CCT': 'P', 'ACT': 'T', 'AGC': 'S', 'AAG': 'K', 'AGA': 'G', 'CAT': 'H', 'AAT': 'N', 'ATT': 'I', 'CTG': 'L', 'CTA': 'L', 'CTC': 'L', 'CAC': 'H', 'AAA': 'K', 'CCG': 'P', 'AGT': 'S', 'CCA': 'P', 'CAA': 'Q', 'CCC': 'P', 'TAT': 'Y', 'GGT': 'G', 'TGT': 'C', 'CGA': 'R', 'CAG': 'Q', 'TCT': 'S', 'GAT': 'D', 'CGG': 'R', 'TTT': 'F', 'TGC': 'C', 'GGG': 'G', 'TGA': 'W', 'GGA': 'G', 'TGG': 'W', 'GGC': 'G', 'TAC': 'Y', 'TTC': 'F', 'TCG': 'S', 'TTA': 'L', 'TTG': 'L', 'TCC': 'S', 'ACC': 'T', 'TAA': '*', 'GCA': 'A', 'GTA': 'V', 'GCC': 'A', 'GTC': 'V', 'GCG': 'A', 'GTG': 'V', 'GAG': 'E', 'GTT': 'V', 'GCT': 'A', 'GAC': 'D', 'CGT': 'R', 'GAA': 'E', 'TCA': 'S', 'ATG': 'M', 'CGC': 'R'},'flatwormMt':{'CTT': 'L', 'TAG': '*', 'ACA': 'T', 'ACG': 'T', 'ATC': 'I', 'AAC': 'N', 'ATA': 'I', 'AGG': 'S', 'CCT': 'P', 'ACT': 'T', 'AGC': 'S', 'AAG': 'K', 'AGA': 'S', 'CAT': 'H', 'AAT': 'N', 'ATT': 'I', 'CTG': 'L', 'CTA': 'L', 'CTC': 'L', 'CAC': 'H', 'AAA': 'N', 'CCG': 'P', 'AGT': 'S', 'CCA': 'P', 'CAA': 'Q', 'CCC': 'P', 'TAT': 'Y', 'GGT': 'G', 'TGT': 'C', 'CGA': 'R', 'CAG': 'Q', 'TCT': 'S', 'GAT': 'D', 'CGG': 'R', 'TTT': 'F', 'TGC': 'C', 'GGG': 'G', 'TGA': 'W', 'GGA': 'G', 'TGG': 'W', 'GGC': 'G', 'TAC': 'Y', 'TTC': 'F', 'TCG': 'S', 'TTA': 'L', 'TTG': 'L', 'TCC': 'S', 'ACC': 'T', 'TAA': 'Y', 'GCA': 'A', 'GTA': 'V', 'GCC': 'A', 'GTC': 'V', 'GCG': 'A', 'GTG': 'V', 'GAG': 'E', 'GTT': 'V', 'GCT': 'A', 'GAC': 'D', 'CGT': 'R', 'GAA': 'E', 'TCA': 'S', 'ATG': 'M', 'CGC': 'R'},'chlorophyceanMt':{'CTT': 'L', 'TAG': 'L', 'ACA': 'T', 'ACG': 'T', 'ATC': 'I', 'AAC': 'N', 'ATA': 'I', 'AGG': 'R', 'CCT': 'P', 'ACT': 'T', 'AGC': 'S', 'AAG': 'K', 'AGA': 'R', 'CAT': 'H', 'AAT': 'N', 'ATT': 'I', 'CTG': 'L', 'CTA': 'L', 'CTC': 'L', 'CAC': 'H', 'AAA': 'K', 'CCG': 'P', 'AGT': 'S', 'CCA': 'P', 'CAA': 'Q', 'CCC': 'P', 'TAT': 'Y', 'GGT': 'G', 'TGT': 'C', 'CGA': 'R', 'CAG': 'Q', 'TCT': 'S', 'GAT': 'D', 'CGG': 'R', 'TTT': 'F', 'TGC': 'C', 'GGG': 'G', 'TGA': '*', 'GGA': 'G', 'TGG': 'W', 'GGC': 'G', 'TAC': 'Y', 'TTC': 'F', 'TCG': 'S', 'TTA': 'L', 'TTG': 'L', 'TCC': 'S', 'ACC': 'T', 'TAA': '*', 'GCA': 'A', 'GTA': 'V', 'GCC': 'A', 'GTC': 'V', 'GCG': 'A', 'GTG': 'V', 'GAG': 'E', 'GTT': 'V', 'GCT': 'A', 'GAC': 'D', 'CGT': 'R', 'GAA': 'E', 'TCA': 'S', 'ATG': 'M', 'CGC': 'R'},'trematodeMt':{'CTT': 'L', 'TAG': '*', 'ACA': 'T', 'ACG': 'T', 'ATC': 'I', 'AAC': 'N', 'ATA': 'M', 'AGG': 'S', 'CCT': 'P', 'ACT': 'T', 'AGC': 'S', 'AAG': 'K', 'AGA': 'S', 'CAT': 'H', 'AAT': 'N', 'ATT': 'I', 'CTG': 'L', 'CTA': 'L', 'CTC': 'L', 'CAC': 'H', 'AAA': 'N', 'CCG': 'P', 'AGT': 'S', 'CCA': 'P', 'CAA': 'Q', 'CCC': 'P', 'TAT': 'Y', 'GGT': 'G', 'TGT': 'C', 'CGA': 'R', 'CAG': 'Q', 'TCT': 'S', 'GAT': 'D', 'CGG': 'R', 'TTT': 'F', 'TGC': 'C', 'GGG': 'G', 'TGA': 'W', 'GGA': 'G', 'TGG': 'W', 'GGC': 'G', 'TAC': 'Y', 'TTC': 'F', 'TCG': 'S', 'TTA': 'L', 'TTG': 'L', 'TCC': 'S', 'ACC': 'T', 'TAA': '*', 'GCA': 'A', 'GTA': 'V', 'GCC': 'A', 'GTC': 'V', 'GCG': 'A', 'GTG': 'V', 'GAG': 'E', 'GTT': 'V', 'GCT': 'A', 'GAC': 'D', 'CGT': 'R', 'GAA': 'E', 'TCA': 'S', 'ATG': 'M', 'CGC': 'R'},'pterobranchiaMt':{'CTT': 'L', 'TAG': '*', 'ACA': 'T', 'ACG': 'T', 'ATC': 'I', 'AAC': 'N', 'ATA': 'I', 'AGG': 'K', 'CCT': 'P', 'ACT': 'T', 'AGC': 'S', 'AAG': 'K', 'AGA': 'S', 'CAT': 'H', 'AAT': 'N', 'ATT': 'I', 'CTG': 'L', 'CTA': 'L', 'CTC': 'L', 'CAC': 'H', 'AAA': 'K', 'CCG': 'P', 'AGT': 'S', 'CCA': 'P', 'CAA': 'Q', 'CCC': 'P', 'TAT': 'Y', 'GGT': 'G', 'TGT': 'C', 'CGA': 'R', 'CAG': 'Q', 'TCT': 'S', 'GAT': 'D', 'CGG': 'R', 'TTT': 'F', 'TGC': 'C', 'GGG': 'G', 'TGA': 'W', 'GGA': 'G', 'TGG': 'W', 'GGC': 'G', 'TAC': 'Y', 'TTC': 'F', 'TCG': 'S', 'TTA': 'L', 'TTG': 'L', 'TCC': 'S', 'ACC': 'T', 'TAA': '*', 'GCA': 'A', 'GTA': 'V', 'GCC': 'A', 'GTC': 'V', 'GCG': 'A', 'GTG': 'V', 'GAG': 'E', 'GTT': 'V', 'GCT': 'A', 'GAC': 'D', 'CGT': 'R', 'GAA': 'E', 'TCA': 'S', 'ATG': 'M', 'CGC': 'R'}}
    geneticCode = geneticCodes[code]
    startCodons = ['ATT','ATC','ATA','ATG','GTG'] #invertebrateMt cod
    aaSchemeDict1 = {("R","H"):"C",("R","K"):"C",("R","D"):"R",("R","E"):"R",("R","A"):"R",("R","N"):"R",("R","C"):"R",("R","Q"):"R",("R","G"):"R",("R","I"):"R",("R","L"):"R",("R","M"):"R",("R","F"):"R",("R","P"):"R",("R","S"):"R",("R","T"):"R",("R","W"):"R",("R","Y"):"R",("R","V"):"R",("H","K"):"C",("H","D"):"R",("H","E"):"R",("H","A"):"R",("H","N"):"R",("H","C"):"R",("H","Q"):"R",("H","G"):"R",("H","I"):"R",("H","L"):"R",("H","M"):"R",("H","F"):"R",("H","P"):"R",("H","S"):"R",("H","T"):"R",("H","W"):"R",("H","Y"):"R",("H","V"):"R",("K","D"):"R",("K","E"):"R",("K","A"):"R",("K","N"):"R",("K","C"):"R",("K","Q"):"R",("K","G"):"R",("K","I"):"R",("K","L"):"R",("K","M"):"R",("K","F"):"R",("K","P"):"R",("K","S"):"R",("K","T"):"R",("K","W"):"R",("K","Y"):"R",("K","V"):"R",("D","E"):"C",("D","A"):"R",("D","N"):"R",("D","C"):"R",("D","Q"):"R",("D","G"):"R",("D","I"):"R",("D","L"):"R",("D","M"):"R",("D","F"):"R",("D","P"):"R",("D","S"):"R",("D","T"):"R",("D","W"):"R",("D","Y"):"R",("D","V"):"R",("E","A"):"R",("E","N"):"R",("E","C"):"R",("E","Q"):"R",("E","G"):"R",("E","I"):"R",("E","L"):"R",("E","M"):"R",("E","F"):"R",("E","P"):"R",("E","S"):"R",("E","T"):"R",("E","W"):"R",("E","Y"):"R",("E","V"):"R",("A","N"):"C",("A","C"):"C",("A","Q"):"C",("A","G"):"C",("A","I"):"C",("A","L"):"C",("A","M"):"C",("A","F"):"C",("A","P"):"C",("A","S"):"C",("A","T"):"C",("A","W"):"C",("A","Y"):"C",("A","V"):"C",("N","C"):"C",("N","Q"):"C",("N","G"):"C",("N","I"):"C",("N","L"):"C",("N","M"):"C",("N","F"):"C",("N","P"):"C",("N","S"):"C",("N","T"):"C",("N","W"):"C",("N","Y"):"C",("N","V"):"C",("C","Q"):"C",("C","G"):"C",("C","I"):"C",("C","L"):"C",("C","M"):"C",("C","F"):"C",("C","P"):"C",("C","S"):"C",("C","T"):"C",("C","W"):"C",("C","Y"):"C",("C","V"):"C",("Q","G"):"C",("Q","I"):"C",("Q","L"):"C",("Q","M"):"C",("Q","F"):"C",("Q","P"):"C",("Q","S"):"C",("Q","T"):"C",("Q","W"):"C",("Q","Y"):"C",("Q","V"):"C",("G","I"):"C",("G","L"):"C",("G","M"):"C",("G","F"):"C",("G","P"):"C",("G","S"):"C",("G","T"):"C",("G","W"):"C",("G","Y"):"C",("G","V"):"C",("I","L"):"C",("I","M"):"C",("I","F"):"C",("I","P"):"C",("I","S"):"C",("I","T"):"C",("I","W"):"C",("I","Y"):"C",("I","V"):"C",("L","M"):"C",("L","F"):"C",("L","P"):"C",("L","S"):"C",("L","T"):"C",("L","W"):"C",("L","Y"):"C",("L","V"):"C",("M","F"):"C",("M","P"):"C",("M","S"):"C",("M","T"):"C",("M","W"):"C",("M","Y"):"C",("M","V"):"C",("F","P"):"C",("F","S"):"C",("F","T"):"C",("F","W"):"C",("F","Y"):"C",("F","V"):"C",("P","S"):"C",("P","T"):"C",("P","W"):"C",("P","Y"):"C",("P","V"):"C",("S","T"):"C",("S","W"):"C",("S","Y"):"C",("S","V"):"C",("T","W"):"C",("T","Y"):"C",("T","V"):"C",("W","Y"):"C",("W","V"):"C",("Y","V"):"C",("H","R"):"C",("K","R"):"C",("D","R"):"R",("E","R"):"R",("A","R"):"R",("N","R"):"R",("C","R"):"R",("Q","R"):"R",("G","R"):"R",("I","R"):"R",("L","R"):"R",("M","R"):"R",("F","R"):"R",("P","R"):"R",("S","R"):"R",("T","R"):"R",("W","R"):"R",("Y","R"):"R",("V","R"):"R",("K","H"):"C",("D","H"):"R",("E","H"):"R",("A","H"):"R",("N","H"):"R",("C","H"):"R",("Q","H"):"R",("G","H"):"R",("I","H"):"R",("L","H"):"R",("M","H"):"R",("F","H"):"R",("P","H"):"R",("S","H"):"R",("T","H"):"R",("W","H"):"R",("Y","H"):"R",("V","H"):"R",("D","K"):"R",("E","K"):"R",("A","K"):"R",("N","K"):"R",("C","K"):"R",("Q","K"):"R",("G","K"):"R",("I","K"):"R",("L","K"):"R",("M","K"):"R",("F","K"):"R",("P","K"):"R",("S","K"):"R",("T","K"):"R",("W","K"):"R",("Y","K"):"R",("V","K"):"R",("E","D"):"C",("A","D"):"R",("N","D"):"R",("C","D"):"R",("Q","D"):"R",("G","D"):"R",("I","D"):"R",("L","D"):"R",("M","D"):"R",("F","D"):"R",("P","D"):"R",("S","D"):"R",("T","D"):"R",("W","D"):"R",("Y","D"):"R",("V","D"):"R",("A","E"):"R",("N","E"):"R",("C","E"):"R",("Q","E"):"R",("G","E"):"R",("I","E"):"R",("L","E"):"R",("M","E"):"R",("F","E"):"R",("P","E"):"R",("S","E"):"R",("T","E"):"R",("W","E"):"R",("Y","E"):"R",("V","E"):"R",("N","A"):"C",("C","A"):"C",("Q","A"):"C",("G","A"):"C",("I","A"):"C",("L","A"):"C",("M","A"):"C",("F","A"):"C",("P","A"):"C",("S","A"):"C",("T","A"):"C",("W","A"):"C",("Y","A"):"C",("V","A"):"C",("C","N"):"C",("Q","N"):"C",("G","N"):"C",("I","N"):"C",("L","N"):"C",("M","N"):"C",("F","N"):"C",("P","N"):"C",("S","N"):"C",("T","N"):"C",("W","N"):"C",("Y","N"):"C",("V","N"):"C",("Q","C"):"C",("G","C"):"C",("I","C"):"C",("L","C"):"C",("M","C"):"C",("F","C"):"C",("P","C"):"C",("S","C"):"C",("T","C"):"C",("W","C"):"C",("Y","C"):"C",("V","C"):"C",("G","Q"):"C",("I","Q"):"C",("L","Q"):"C",("M","Q"):"C",("F","Q"):"C",("P","Q"):"C",("S","Q"):"C",("T","Q"):"C",("W","Q"):"C",("Y","Q"):"C",("V","Q"):"C",("I","G"):"C",("L","G"):"C",("M","G"):"C",("F","G"):"C",("P","G"):"C",("S","G"):"C",("T","G"):"C",("W","G"):"C",("Y","G"):"C",("V","G"):"C",("L","I"):"C",("M","I"):"C",("F","I"):"C",("P","I"):"C",("S","I"):"C",("T","I"):"C",("W","I"):"C",("Y","I"):"C",("V","I"):"C",("M","L"):"C",("F","L"):"C",("P","L"):"C",("S","L"):"C",("T","L"):"C",("W","L"):"C",("Y","L"):"C",("V","L"):"C",("F","M"):"C",("P","M"):"C",("S","M"):"C",("T","M"):"C",("W","M"):"C",("Y","M"):"C",("V","M"):"C",("P","F"):"C",("S","F"):"C",("T","F"):"C",("W","F"):"C",("Y","F"):"C",("V","F"):"C",("S","P"):"C",("T","P"):"C",("W","P"):"C",("Y","P"):"C",("V","P"):"C",("T","S"):"C",("W","S"):"C",("Y","S"):"C",("V","S"):"C",("W","T"):"C",("Y","T"):"C",("V","T"):"C",("Y","W"):"C",("V","W"):"C",("V","Y"):"C",("R","*"):"R",("H","*"):"R",("K","*"):"R",("D","*"):"R",("E","*"):"R",("A","*"):"R",("N","*"):"R",("C","*"):"R",("Q","*"):"R",("G","*"):"R",("I","*"):"R",("L","*"):"R",("M","*"):"R",("F","*"):"R",("P","*"):"R",("S","*"):"R",("T","*"):"R",("W","*"):"R",("Y","*"):"R",("V","*"):"R",("*","R"):"R",("*","H"):"R",("*","K"):"R",("*","D"):"R",("*","E"):"R",("*","A"):"R",("*","N"):"R",("*","C"):"R",("*","Q"):"R",("*","G"):"R",("*","I"):"R",("*","L"):"R",("*","M"):"R",("*","F"):"R",("*","P"):"R",("*","S"):"R",("*","T"):"R",("*","W"):"R",("*","Y"):"R",("*","V"):"R"}
    aaSchemeDict2 = {("R","H"):"C",("R","K"):"C",("R","D"):"C",("R","E"):"C",("R","A"):"R",("R","N"):"C",("R","C"):"C",("R","Q"):"C",("R","G"):"C",("R","I"):"R",("R","L"):"R",("R","M"):"R",("R","F"):"R",("R","P"):"R",("R","S"):"C",("R","T"):"C",("R","W"):"R",("R","Y"):"C",("R","V"):"R",("H","K"):"C",("H","D"):"C",("H","E"):"C",("H","A"):"R",("H","N"):"C",("H","C"):"C",("H","Q"):"C",("H","G"):"C",("H","I"):"R",("H","L"):"R",("H","M"):"R",("H","F"):"R",("H","P"):"R",("H","S"):"C",("H","T"):"C",("H","W"):"R",("H","Y"):"C",("H","V"):"R",("K","D"):"C",("K","E"):"C",("K","A"):"R",("K","N"):"C",("K","C"):"C",("K","Q"):"C",("K","G"):"C",("K","I"):"R",("K","L"):"R",("K","M"):"R",("K","F"):"R",("K","P"):"R",("K","S"):"C",("K","T"):"C",("K","W"):"R",("K","Y"):"C",("K","V"):"R",("D","E"):"C",("D","A"):"R",("D","N"):"C",("D","C"):"C",("D","Q"):"C",("D","G"):"C",("D","I"):"R",("D","L"):"R",("D","M"):"R",("D","F"):"R",("D","P"):"R",("D","S"):"C",("D","T"):"C",("D","W"):"R",("D","Y"):"C",("D","V"):"R",("E","A"):"R",("E","N"):"C",("E","C"):"C",("E","Q"):"C",("E","G"):"C",("E","I"):"R",("E","L"):"R",("E","M"):"R",("E","F"):"R",("E","P"):"R",("E","S"):"C",("E","T"):"C",("E","W"):"R",("E","Y"):"C",("E","V"):"R",("A","N"):"R",("A","C"):"R",("A","Q"):"R",("A","G"):"R",("A","I"):"C",("A","L"):"C",("A","M"):"C",("A","F"):"C",("A","P"):"C",("A","S"):"R",("A","T"):"R",("A","W"):"C",("A","Y"):"R",("A","V"):"C",("N","C"):"C",("N","Q"):"C",("N","G"):"C",("N","I"):"R",("N","L"):"R",("N","M"):"R",("N","F"):"R",("N","P"):"R",("N","S"):"C",("N","T"):"C",("N","W"):"R",("N","Y"):"C",("N","V"):"R",("C","Q"):"C",("C","G"):"C",("C","I"):"R",("C","L"):"R",("C","M"):"R",("C","F"):"R",("C","P"):"R",("C","S"):"C",("C","T"):"C",("C","W"):"R",("C","Y"):"C",("C","V"):"R",("Q","G"):"C",("Q","I"):"R",("Q","L"):"R",("Q","M"):"R",("Q","F"):"R",("Q","P"):"R",("Q","S"):"C",("Q","T"):"C",("Q","W"):"R",("Q","Y"):"C",("Q","V"):"R",("G","I"):"R",("G","L"):"R",("G","M"):"R",("G","F"):"R",("G","P"):"R",("G","S"):"C",("G","T"):"C",("G","W"):"R",("G","Y"):"C",("G","V"):"R",("I","L"):"C",("I","M"):"C",("I","F"):"C",("I","P"):"C",("I","S"):"R",("I","T"):"R",("I","W"):"C",("I","Y"):"R",("I","V"):"C",("L","M"):"C",("L","F"):"C",("L","P"):"C",("L","S"):"R",("L","T"):"R",("L","W"):"C",("L","Y"):"R",("L","V"):"C",("M","F"):"C",("M","P"):"C",("M","S"):"R",("M","T"):"R",("M","W"):"C",("M","Y"):"R",("M","V"):"C",("F","P"):"C",("F","S"):"R",("F","T"):"R",("F","W"):"C",("F","Y"):"R",("F","V"):"C",("P","S"):"R",("P","T"):"R",("P","W"):"C",("P","Y"):"R",("P","V"):"C",("S","T"):"C",("S","W"):"R",("S","Y"):"C",("S","V"):"R",("T","W"):"R",("T","Y"):"C",("T","V"):"R",("W","Y"):"R",("W","V"):"C",("Y","V"):"R",("H","R"):"C",("K","R"):"C",("D","R"):"C",("E","R"):"C",("A","R"):"R",("N","R"):"C",("C","R"):"C",("Q","R"):"C",("G","R"):"C",("I","R"):"R",("L","R"):"R",("M","R"):"R",("F","R"):"R",("P","R"):"R",("S","R"):"C",("T","R"):"C",("W","R"):"R",("Y","R"):"C",("V","R"):"R",("K","H"):"C",("D","H"):"C",("E","H"):"C",("A","H"):"R",("N","H"):"C",("C","H"):"C",("Q","H"):"C",("G","H"):"C",("I","H"):"R",("L","H"):"R",("M","H"):"R",("F","H"):"R",("P","H"):"R",("S","H"):"C",("T","H"):"C",("W","H"):"R",("Y","H"):"C",("V","H"):"R",("D","K"):"C",("E","K"):"C",("A","K"):"R",("N","K"):"C",("C","K"):"C",("Q","K"):"C",("G","K"):"C",("I","K"):"R",("L","K"):"R",("M","K"):"R",("F","K"):"R",("P","K"):"R",("S","K"):"C",("T","K"):"C",("W","K"):"R",("Y","K"):"C",("V","K"):"R",("E","D"):"C",("A","D"):"R",("N","D"):"C",("C","D"):"C",("Q","D"):"C",("G","D"):"C",("I","D"):"R",("L","D"):"R",("M","D"):"R",("F","D"):"R",("P","D"):"R",("S","D"):"C",("T","D"):"C",("W","D"):"R",("Y","D"):"C",("V","D"):"R",("A","E"):"R",("N","E"):"C",("C","E"):"C",("Q","E"):"C",("G","E"):"C",("I","E"):"R",("L","E"):"R",("M","E"):"R",("F","E"):"R",("P","E"):"R",("S","E"):"C",("T","E"):"C",("W","E"):"R",("Y","E"):"C",("V","E"):"R",("N","A"):"R",("C","A"):"R",("Q","A"):"R",("G","A"):"R",("I","A"):"C",("L","A"):"C",("M","A"):"C",("F","A"):"C",("P","A"):"C",("S","A"):"R",("T","A"):"R",("W","A"):"C",("Y","A"):"R",("V","A"):"C",("C","N"):"C",("Q","N"):"C",("G","N"):"C",("I","N"):"R",("L","N"):"R",("M","N"):"R",("F","N"):"R",("P","N"):"R",("S","N"):"C",("T","N"):"C",("W","N"):"R",("Y","N"):"C",("V","N"):"R",("Q","C"):"C",("G","C"):"C",("I","C"):"R",("L","C"):"R",("M","C"):"R",("F","C"):"R",("P","C"):"R",("S","C"):"C",("T","C"):"C",("W","C"):"R",("Y","C"):"C",("V","C"):"R",("G","Q"):"C",("I","Q"):"R",("L","Q"):"R",("M","Q"):"R",("F","Q"):"R",("P","Q"):"R",("S","Q"):"C",("T","Q"):"C",("W","Q"):"R",("Y","Q"):"C",("V","Q"):"R",("I","G"):"R",("L","G"):"R",("M","G"):"R",("F","G"):"R",("P","G"):"R",("S","G"):"C",("T","G"):"C",("W","G"):"R",("Y","G"):"C",("V","G"):"R",("L","I"):"C",("M","I"):"C",("F","I"):"C",("P","I"):"C",("S","I"):"R",("T","I"):"R",("W","I"):"C",("Y","I"):"R",("V","I"):"C",("M","L"):"C",("F","L"):"C",("P","L"):"C",("S","L"):"R",("T","L"):"R",("W","L"):"C",("Y","L"):"R",("V","L"):"C",("F","M"):"C",("P","M"):"C",("S","M"):"R",("T","M"):"R",("W","M"):"C",("Y","M"):"R",("V","M"):"C",("P","F"):"C",("S","F"):"R",("T","F"):"R",("W","F"):"C",("Y","F"):"R",("V","F"):"C",("S","P"):"R",("T","P"):"R",("W","P"):"C",("Y","P"):"R",("V","P"):"C",("T","S"):"C",("W","S"):"R",("Y","S"):"C",("V","S"):"R",("W","T"):"R",("Y","T"):"C",("V","T"):"R",("Y","W"):"R",("V","W"):"C",("V","Y"):"R",("R","*"):"R",("H","*"):"R",("K","*"):"R",("D","*"):"R",("E","*"):"R",("A","*"):"R",("N","*"):"R",("C","*"):"R",("Q","*"):"R",("G","*"):"R",("I","*"):"R",("L","*"):"R",("M","*"):"R",("F","*"):"R",("P","*"):"R",("S","*"):"R",("T","*"):"R",("W","*"):"R",("Y","*"):"R",("V","*"):"R",("*","R"):"R",("*","H"):"R",("*","K"):"R",("*","D"):"R",("*","E"):"R",("*","A"):"R",("*","N"):"R",("*","C"):"R",("*","Q"):"R",("*","G"):"R",("*","I"):"R",("*","L"):"R",("*","M"):"R",("*","F"):"R",("*","P"):"R",("*","S"):"R",("*","T"):"R",("*","W"):"R",("*","Y"):"R",("*","V"):"R"}
    aaSchemeDict3 = {("R","H"):"C",("R","K"):"C",("R","D"):"R",("R","E"):"R",("R","A"):"R",("R","N"):"R",("R","C"):"R",("R","Q"):"R",("R","G"):"R",("R","I"):"R",("R","L"):"R",("R","M"):"R",("R","F"):"R",("R","P"):"R",("R","S"):"R",("R","T"):"R",("R","W"):"R",("R","Y"):"R",("R","V"):"R",("H","K"):"C",("H","D"):"R",("H","E"):"R",("H","A"):"R",("H","N"):"R",("H","C"):"R",("H","Q"):"R",("H","G"):"R",("H","I"):"R",("H","L"):"R",("H","M"):"R",("H","F"):"R",("H","P"):"R",("H","S"):"R",("H","T"):"R",("H","W"):"R",("H","Y"):"R",("H","V"):"R",("K","D"):"R",("K","E"):"R",("K","A"):"R",("K","N"):"R",("K","C"):"R",("K","Q"):"R",("K","G"):"R",("K","I"):"R",("K","L"):"R",("K","M"):"R",("K","F"):"R",("K","P"):"R",("K","S"):"R",("K","T"):"R",("K","W"):"R",("K","Y"):"R",("K","V"):"R",("D","E"):"C",("D","A"):"R",("D","N"):"C",("D","C"):"R",("D","Q"):"C",("D","G"):"R",("D","I"):"R",("D","L"):"R",("D","M"):"R",("D","F"):"R",("D","P"):"R",("D","S"):"R",("D","T"):"R",("D","W"):"R",("D","Y"):"R",("D","V"):"R",("E","A"):"R",("E","N"):"C",("E","C"):"R",("E","Q"):"C",("E","G"):"R",("E","I"):"R",("E","L"):"R",("E","M"):"R",("E","F"):"R",("E","P"):"R",("E","S"):"R",("E","T"):"R",("E","W"):"R",("E","Y"):"R",("E","V"):"R",("A","N"):"R",("A","C"):"R",("A","Q"):"R",("A","G"):"C",("A","I"):"R",("A","L"):"R",("A","M"):"R",("A","F"):"R",("A","P"):"C",("A","S"):"C",("A","T"):"C",("A","W"):"R",("A","Y"):"R",("A","V"):"R",("N","C"):"R",("N","Q"):"C",("N","G"):"R",("N","I"):"R",("N","L"):"R",("N","M"):"R",("N","F"):"R",("N","P"):"R",("N","S"):"R",("N","T"):"R",("N","W"):"R",("N","Y"):"R",("N","V"):"R",("C","Q"):"R",("C","G"):"R",("C","I"):"R",("C","L"):"R",("C","M"):"R",("C","F"):"R",("C","P"):"R",("C","S"):"R",("C","T"):"R",("C","W"):"R",("C","Y"):"R",("C","V"):"R",("Q","G"):"R",("Q","I"):"R",("Q","L"):"R",("Q","M"):"R",("Q","F"):"R",("Q","P"):"R",("Q","S"):"R",("Q","T"):"R",("Q","W"):"R",("Q","Y"):"R",("Q","V"):"R",("G","I"):"R",("G","L"):"R",("G","M"):"R",("G","F"):"R",("G","P"):"C",("G","S"):"C",("G","T"):"C",("G","W"):"R",("G","Y"):"R",("G","V"):"R",("I","L"):"C",("I","M"):"C",("I","F"):"R",("I","P"):"R",("I","S"):"R",("I","T"):"R",("I","W"):"R",("I","Y"):"R",("I","V"):"C",("L","M"):"C",("L","F"):"R",("L","P"):"R",("L","S"):"R",("L","T"):"R",("L","W"):"R",("L","Y"):"R",("L","V"):"C",("M","F"):"R",("M","P"):"R",("M","S"):"R",("M","T"):"R",("M","W"):"R",("M","Y"):"R",("M","V"):"C",("F","P"):"R",("F","S"):"C",("F","T"):"C",("F","W"):"R",("F","Y"):"R",("F","V"):"R",("P","S"):"C",("P","T"):"C",("P","W"):"R",("P","Y"):"R",("P","V"):"R",("S","T"):"C",("S","W"):"R",("S","Y"):"R",("S","V"):"R",("T","W"):"R",("T","Y"):"R",("T","V"):"R",("W","Y"):"C",("W","V"):"R",("Y","V"):"R",("H","R"):"C",("K","R"):"C",("D","R"):"R",("E","R"):"R",("A","R"):"R",("N","R"):"R",("C","R"):"R",("Q","R"):"R",("G","R"):"R",("I","R"):"R",("L","R"):"R",("M","R"):"R",("F","R"):"R",("P","R"):"R",("S","R"):"R",("T","R"):"R",("W","R"):"R",("Y","R"):"R",("V","R"):"R",("K","H"):"C",("D","H"):"R",("E","H"):"R",("A","H"):"R",("N","H"):"R",("C","H"):"R",("Q","H"):"R",("G","H"):"R",("I","H"):"R",("L","H"):"R",("M","H"):"R",("F","H"):"R",("P","H"):"R",("S","H"):"R",("T","H"):"R",("W","H"):"R",("Y","H"):"R",("V","H"):"R",("D","K"):"R",("E","K"):"R",("A","K"):"R",("N","K"):"R",("C","K"):"R",("Q","K"):"R",("G","K"):"R",("I","K"):"R",("L","K"):"R",("M","K"):"R",("F","K"):"R",("P","K"):"R",("S","K"):"R",("T","K"):"R",("W","K"):"R",("Y","K"):"R",("V","K"):"R",("E","D"):"C",("A","D"):"R",("N","D"):"C",("C","D"):"R",("Q","D"):"C",("G","D"):"R",("I","D"):"R",("L","D"):"R",("M","D"):"R",("F","D"):"R",("P","D"):"R",("S","D"):"R",("T","D"):"R",("W","D"):"R",("Y","D"):"R",("V","D"):"R",("A","E"):"R",("N","E"):"C",("C","E"):"R",("Q","E"):"C",("G","E"):"R",("I","E"):"R",("L","E"):"R",("M","E"):"R",("F","E"):"R",("P","E"):"R",("S","E"):"R",("T","E"):"R",("W","E"):"R",("Y","E"):"R",("V","E"):"R",("N","A"):"R",("C","A"):"R",("Q","A"):"R",("G","A"):"C",("I","A"):"R",("L","A"):"R",("M","A"):"R",("F","A"):"R",("P","A"):"C",("S","A"):"C",("T","A"):"C",("W","A"):"R",("Y","A"):"R",("V","A"):"R",("C","N"):"R",("Q","N"):"C",("G","N"):"R",("I","N"):"R",("L","N"):"R",("M","N"):"R",("F","N"):"R",("P","N"):"R",("S","N"):"R",("T","N"):"R",("W","N"):"R",("Y","N"):"R",("V","N"):"R",("Q","C"):"R",("G","C"):"R",("I","C"):"R",("L","C"):"R",("M","C"):"R",("F","C"):"R",("P","C"):"R",("S","C"):"R",("T","C"):"R",("W","C"):"R",("Y","C"):"R",("V","C"):"R",("G","Q"):"R",("I","Q"):"R",("L","Q"):"R",("M","Q"):"R",("F","Q"):"R",("P","Q"):"R",("S","Q"):"R",("T","Q"):"R",("W","Q"):"R",("Y","Q"):"R",("V","Q"):"R",("I","G"):"R",("L","G"):"R",("M","G"):"R",("F","G"):"R",("P","G"):"C",("S","G"):"C",("T","G"):"C",("W","G"):"R",("Y","G"):"R",("V","G"):"R",("L","I"):"C",("M","I"):"C",("F","I"):"R",("P","I"):"R",("S","I"):"R",("T","I"):"R",("W","I"):"R",("Y","I"):"R",("V","I"):"C",("M","L"):"C",("F","L"):"R",("P","L"):"R",("S","L"):"R",("T","L"):"R",("W","L"):"R",("Y","L"):"R",("V","L"):"C",("F","M"):"R",("P","M"):"R",("S","M"):"R",("T","M"):"R",("W","M"):"R",("Y","M"):"R",("V","M"):"C",("P","F"):"R",("S","F"):"C",("T","F"):"C",("W","F"):"R",("Y","F"):"R",("V","F"):"R",("S","P"):"C",("T","P"):"C",("W","P"):"R",("Y","P"):"R",("V","P"):"R",("T","S"):"C",("W","S"):"R",("Y","S"):"R",("V","S"):"R",("W","T"):"R",("Y","T"):"R",("V","T"):"R",("Y","W"):"C",("V","W"):"R",("V","Y"):"R",("R","*"):"R",("H","*"):"R",("K","*"):"R",("D","*"):"R",("E","*"):"R",("A","*"):"R",("N","*"):"R",("C","*"):"R",("Q","*"):"R",("G","*"):"R",("I","*"):"R",("L","*"):"R",("M","*"):"R",("F","*"):"R",("P","*"):"R",("S","*"):"R",("T","*"):"R",("W","*"):"R",("Y","*"):"R",("V","*"):"R",("*","R"):"R",("*","H"):"R",("*","K"):"R",("*","D"):"R",("*","E"):"R",("*","A"):"R",("*","N"):"R",("*","C"):"R",("*","Q"):"R",("*","G"):"R",("*","I"):"R",("*","L"):"R",("*","M"):"R",("*","F"):"R",("*","P"):"R",("*","S"):"R",("*","T"):"R",("*","W"):"R",("*","Y"):"R",("*","V"):"R"}
    aaSchemeDict4 = {("R","H"):"C",("R","K"):"C",("R","D"):"R",("R","E"):"R",("R","A"):"R",("R","N"):"R",("R","C"):"R",("R","Q"):"C",("R","G"):"R",("R","I"):"R",("R","L"):"R",("R","M"):"R",("R","F"):"C",("R","P"):"R",("R","S"):"R",("R","T"):"R",("R","W"):"C",("R","Y"):"C",("R","V"):"R",("H","K"):"C",("H","D"):"R",("H","E"):"R",("H","A"):"R",("H","N"):"R",("H","C"):"R",("H","Q"):"C",("H","G"):"R",("H","I"):"R",("H","L"):"R",("H","M"):"R",("H","F"):"C",("H","P"):"R",("H","S"):"R",("H","T"):"R",("H","W"):"C",("H","Y"):"C",("H","V"):"R",("K","D"):"R",("K","E"):"R",("K","A"):"R",("K","N"):"R",("K","C"):"R",("K","Q"):"C",("K","G"):"R",("K","I"):"R",("K","L"):"R",("K","M"):"R",("K","F"):"C",("K","P"):"R",("K","S"):"R",("K","T"):"R",("K","W"):"C",("K","Y"):"C",("K","V"):"R",("D","E"):"C",("D","A"):"R",("D","N"):"R",("D","C"):"R",("D","Q"):"R",("D","G"):"R",("D","I"):"R",("D","L"):"R",("D","M"):"R",("D","F"):"R",("D","P"):"R",("D","S"):"R",("D","T"):"R",("D","W"):"R",("D","Y"):"R",("D","V"):"R",("E","A"):"R",("E","N"):"R",("E","C"):"R",("E","Q"):"R",("E","G"):"R",("E","I"):"R",("E","L"):"R",("E","M"):"R",("E","F"):"R",("E","P"):"R",("E","S"):"R",("E","T"):"R",("E","W"):"R",("E","Y"):"R",("E","V"):"R",("A","N"):"C",("A","C"):"C",("A","Q"):"R",("A","G"):"C",("A","I"):"R",("A","L"):"R",("A","M"):"R",("A","F"):"R",("A","P"):"C",("A","S"):"C",("A","T"):"C",("A","W"):"R",("A","Y"):"R",("A","V"):"R",("N","C"):"C",("N","Q"):"R",("N","G"):"C",("N","I"):"R",("N","L"):"R",("N","M"):"R",("N","F"):"R",("N","P"):"C",("N","S"):"C",("N","T"):"C",("N","W"):"R",("N","Y"):"R",("N","V"):"R",("C","Q"):"R",("C","G"):"C",("C","I"):"R",("C","L"):"R",("C","M"):"R",("C","F"):"R",("C","P"):"C",("C","S"):"C",("C","T"):"C",("C","W"):"R",("C","Y"):"R",("C","V"):"R",("Q","G"):"R",("Q","I"):"R",("Q","L"):"R",("Q","M"):"R",("Q","F"):"C",("Q","P"):"R",("Q","S"):"R",("Q","T"):"R",("Q","W"):"C",("Q","Y"):"C",("Q","V"):"R",("G","I"):"R",("G","L"):"R",("G","M"):"R",("G","F"):"R",("G","P"):"C",("G","S"):"C",("G","T"):"C",("G","W"):"R",("G","Y"):"R",("G","V"):"R",("I","L"):"C",("I","M"):"C",("I","F"):"R",("I","P"):"R",("I","S"):"R",("I","T"):"R",("I","W"):"R",("I","Y"):"R",("I","V"):"C",("L","M"):"C",("L","F"):"R",("L","P"):"R",("L","S"):"R",("L","T"):"R",("L","W"):"R",("L","Y"):"R",("L","V"):"C",("M","F"):"R",("M","P"):"R",("M","S"):"R",("M","T"):"R",("M","W"):"R",("M","Y"):"R",("M","V"):"C",("F","P"):"R",("F","S"):"R",("F","T"):"R",("F","W"):"C",("F","Y"):"C",("F","V"):"R",("P","S"):"C",("P","T"):"C",("P","W"):"R",("P","Y"):"R",("P","V"):"R",("S","T"):"C",("S","W"):"R",("S","Y"):"R",("S","V"):"R",("T","W"):"R",("T","Y"):"R",("T","V"):"R",("W","Y"):"C",("W","V"):"R",("Y","V"):"R",("H","R"):"C",("K","R"):"C",("D","R"):"R",("E","R"):"R",("A","R"):"R",("N","R"):"R",("C","R"):"R",("Q","R"):"C",("G","R"):"R",("I","R"):"R",("L","R"):"R",("M","R"):"R",("F","R"):"C",("P","R"):"R",("S","R"):"R",("T","R"):"R",("W","R"):"C",("Y","R"):"C",("V","R"):"R",("K","H"):"C",("D","H"):"R",("E","H"):"R",("A","H"):"R",("N","H"):"R",("C","H"):"R",("Q","H"):"C",("G","H"):"R",("I","H"):"R",("L","H"):"R",("M","H"):"R",("F","H"):"C",("P","H"):"R",("S","H"):"R",("T","H"):"R",("W","H"):"C",("Y","H"):"C",("V","H"):"R",("D","K"):"R",("E","K"):"R",("A","K"):"R",("N","K"):"R",("C","K"):"R",("Q","K"):"C",("G","K"):"R",("I","K"):"R",("L","K"):"R",("M","K"):"R",("F","K"):"C",("P","K"):"R",("S","K"):"R",("T","K"):"R",("W","K"):"C",("Y","K"):"C",("V","K"):"R",("E","D"):"C",("A","D"):"R",("N","D"):"R",("C","D"):"R",("Q","D"):"R",("G","D"):"R",("I","D"):"R",("L","D"):"R",("M","D"):"R",("F","D"):"R",("P","D"):"R",("S","D"):"R",("T","D"):"R",("W","D"):"R",("Y","D"):"R",("V","D"):"R",("A","E"):"R",("N","E"):"R",("C","E"):"R",("Q","E"):"R",("G","E"):"R",("I","E"):"R",("L","E"):"R",("M","E"):"R",("F","E"):"R",("P","E"):"R",("S","E"):"R",("T","E"):"R",("W","E"):"R",("Y","E"):"R",("V","E"):"R",("N","A"):"C",("C","A"):"C",("Q","A"):"R",("G","A"):"C",("I","A"):"R",("L","A"):"R",("M","A"):"R",("F","A"):"R",("P","A"):"C",("S","A"):"C",("T","A"):"C",("W","A"):"R",("Y","A"):"R",("V","A"):"R",("C","N"):"C",("Q","N"):"R",("G","N"):"C",("I","N"):"R",("L","N"):"R",("M","N"):"R",("F","N"):"R",("P","N"):"C",("S","N"):"C",("T","N"):"C",("W","N"):"R",("Y","N"):"R",("V","N"):"R",("Q","C"):"R",("G","C"):"C",("I","C"):"R",("L","C"):"R",("M","C"):"R",("F","C"):"R",("P","C"):"C",("S","C"):"C",("T","C"):"C",("W","C"):"R",("Y","C"):"R",("V","C"):"R",("G","Q"):"R",("I","Q"):"R",("L","Q"):"R",("M","Q"):"R",("F","Q"):"C",("P","Q"):"R",("S","Q"):"R",("T","Q"):"R",("W","Q"):"C",("Y","Q"):"C",("V","Q"):"R",("I","G"):"R",("L","G"):"R",("M","G"):"R",("F","G"):"R",("P","G"):"C",("S","G"):"C",("T","G"):"C",("W","G"):"R",("Y","G"):"R",("V","G"):"R",("L","I"):"C",("M","I"):"C",("F","I"):"R",("P","I"):"R",("S","I"):"R",("T","I"):"R",("W","I"):"R",("Y","I"):"R",("V","I"):"C",("M","L"):"C",("F","L"):"R",("P","L"):"R",("S","L"):"R",("T","L"):"R",("W","L"):"R",("Y","L"):"R",("V","L"):"C",("F","M"):"R",("P","M"):"R",("S","M"):"R",("T","M"):"R",("W","M"):"R",("Y","M"):"R",("V","M"):"C",("P","F"):"R",("S","F"):"R",("T","F"):"R",("W","F"):"C",("Y","F"):"C",("V","F"):"R",("S","P"):"C",("T","P"):"C",("W","P"):"R",("Y","P"):"R",("V","P"):"R",("T","S"):"C",("W","S"):"R",("Y","S"):"R",("V","S"):"R",("W","T"):"R",("Y","T"):"R",("V","T"):"R",("Y","W"):"C",("V","W"):"R",("V","Y"):"R",("R","*"):"R",("H","*"):"R",("K","*"):"R",("D","*"):"R",("E","*"):"R",("A","*"):"R",("N","*"):"R",("C","*"):"R",("Q","*"):"R",("G","*"):"R",("I","*"):"R",("L","*"):"R",("M","*"):"R",("F","*"):"R",("P","*"):"R",("S","*"):"R",("T","*"):"R",("W","*"):"R",("Y","*"):"R",("V","*"):"R",("*","R"):"R",("*","H"):"R",("*","K"):"R",("*","D"):"R",("*","E"):"R",("*","A"):"R",("*","N"):"R",("*","C"):"R",("*","Q"):"R",("*","G"):"R",("*","I"):"R",("*","L"):"R",("*","M"):"R",("*","F"):"R",("*","P"):"R",("*","S"):"R",("*","T"):"R",("*","W"):"R",("*","Y"):"R",("*","V"):"R"}
    aaSchemeDict5 = {("R","H"):"C",("R","K"):"C",("R","D"):"R",("R","E"):"R",("R","A"):"R",("R","N"):"R",("R","C"):"R",("R","Q"):"R",("R","G"):"R",("R","I"):"R",("R","L"):"R",("R","M"):"R",("R","F"):"R",("R","P"):"R",("R","S"):"R",("R","T"):"R",("R","W"):"R",("R","Y"):"R",("R","V"):"R",("H","K"):"C",("H","D"):"R",("H","E"):"R",("H","A"):"R",("H","N"):"R",("H","C"):"R",("H","Q"):"R",("H","G"):"R",("H","I"):"R",("H","L"):"R",("H","M"):"R",("H","F"):"R",("H","P"):"R",("H","S"):"R",("H","T"):"R",("H","W"):"R",("H","Y"):"R",("H","V"):"R",("K","D"):"R",("K","E"):"R",("K","A"):"R",("K","N"):"R",("K","C"):"R",("K","Q"):"R",("K","G"):"R",("K","I"):"R",("K","L"):"R",("K","M"):"R",("K","F"):"R",("K","P"):"R",("K","S"):"R",("K","T"):"R",("K","W"):"R",("K","Y"):"R",("K","V"):"R",("D","E"):"C",("D","A"):"R",("D","N"):"R",("D","C"):"R",("D","Q"):"R",("D","G"):"R",("D","I"):"R",("D","L"):"R",("D","M"):"R",("D","F"):"R",("D","P"):"R",("D","S"):"R",("D","T"):"R",("D","W"):"R",("D","Y"):"R",("D","V"):"R",("E","A"):"R",("E","N"):"R",("E","C"):"R",("E","Q"):"R",("E","G"):"R",("E","I"):"R",("E","L"):"R",("E","M"):"R",("E","F"):"R",("E","P"):"R",("E","S"):"R",("E","T"):"R",("E","W"):"R",("E","Y"):"R",("E","V"):"R",("A","N"):"C",("A","C"):"C",("A","Q"):"C",("A","G"):"C",("A","I"):"C",("A","L"):"C",("A","M"):"C",("A","F"):"R",("A","P"):"C",("A","S"):"C",("A","T"):"C",("A","W"):"R",("A","Y"):"R",("A","V"):"C",("N","C"):"C",("N","Q"):"C",("N","G"):"C",("N","I"):"C",("N","L"):"C",("N","M"):"C",("N","F"):"R",("N","P"):"C",("N","S"):"C",("N","T"):"C",("N","W"):"R",("N","Y"):"R",("N","V"):"C",("C","Q"):"C",("C","G"):"C",("C","I"):"C",("C","L"):"C",("C","M"):"C",("C","F"):"R",("C","P"):"C",("C","S"):"C",("C","T"):"C",("C","W"):"R",("C","Y"):"R",("C","V"):"C",("Q","G"):"C",("Q","I"):"C",("Q","L"):"C",("Q","M"):"C",("Q","F"):"R",("Q","P"):"C",("Q","S"):"C",("Q","T"):"C",("Q","W"):"R",("Q","Y"):"R",("Q","V"):"C",("G","I"):"C",("G","L"):"C",("G","M"):"C",("G","F"):"R",("G","P"):"C",("G","S"):"C",("G","T"):"C",("G","W"):"R",("G","Y"):"R",("G","V"):"C",("I","L"):"C",("I","M"):"C",("I","F"):"R",("I","P"):"C",("I","S"):"C",("I","T"):"C",("I","W"):"R",("I","Y"):"R",("I","V"):"C",("L","M"):"C",("L","F"):"R",("L","P"):"C",("L","S"):"C",("L","T"):"C",("L","W"):"R",("L","Y"):"R",("L","V"):"C",("M","F"):"R",("M","P"):"C",("M","S"):"C",("M","T"):"C",("M","W"):"R",("M","Y"):"R",("M","V"):"C",("F","P"):"R",("F","S"):"R",("F","T"):"R",("F","W"):"C",("F","Y"):"C",("F","V"):"R",("P","S"):"C",("P","T"):"C",("P","W"):"R",("P","Y"):"R",("P","V"):"C",("S","T"):"C",("S","W"):"R",("S","Y"):"R",("S","V"):"R",("T","W"):"R",("T","Y"):"R",("T","V"):"C",("W","Y"):"C",("W","V"):"R",("Y","V"):"R",("H","R"):"C",("K","R"):"C",("D","R"):"R",("E","R"):"R",("A","R"):"R",("N","R"):"R",("C","R"):"R",("Q","R"):"R",("G","R"):"R",("I","R"):"R",("L","R"):"R",("M","R"):"R",("F","R"):"R",("P","R"):"R",("S","R"):"R",("T","R"):"R",("W","R"):"R",("Y","R"):"R",("V","R"):"R",("K","H"):"C",("D","H"):"R",("E","H"):"R",("A","H"):"R",("N","H"):"R",("C","H"):"R",("Q","H"):"R",("G","H"):"R",("I","H"):"R",("L","H"):"R",("M","H"):"R",("F","H"):"R",("P","H"):"R",("S","H"):"R",("T","H"):"R",("W","H"):"R",("Y","H"):"R",("V","H"):"R",("D","K"):"R",("E","K"):"R",("A","K"):"R",("N","K"):"R",("C","K"):"R",("Q","K"):"R",("G","K"):"R",("I","K"):"R",("L","K"):"R",("M","K"):"R",("F","K"):"R",("P","K"):"R",("S","K"):"R",("T","K"):"R",("W","K"):"R",("Y","K"):"R",("V","K"):"R",("E","D"):"C",("A","D"):"R",("N","D"):"R",("C","D"):"R",("Q","D"):"R",("G","D"):"R",("I","D"):"R",("L","D"):"R",("M","D"):"R",("F","D"):"R",("P","D"):"R",("S","D"):"R",("T","D"):"R",("W","D"):"R",("Y","D"):"R",("V","D"):"R",("A","E"):"R",("N","E"):"R",("C","E"):"R",("Q","E"):"R",("G","E"):"R",("I","E"):"R",("L","E"):"R",("M","E"):"R",("F","E"):"R",("P","E"):"R",("S","E"):"R",("T","E"):"R",("W","E"):"R",("Y","E"):"R",("V","E"):"R",("N","A"):"C",("C","A"):"C",("Q","A"):"C",("G","A"):"C",("I","A"):"C",("L","A"):"C",("M","A"):"C",("F","A"):"R",("P","A"):"C",("S","A"):"C",("T","A"):"C",("W","A"):"R",("Y","A"):"R",("V","A"):"C",("C","N"):"C",("Q","N"):"C",("G","N"):"C",("I","N"):"C",("L","N"):"C",("M","N"):"C",("F","N"):"R",("P","N"):"C",("S","N"):"C",("T","N"):"C",("W","N"):"R",("Y","N"):"R",("V","N"):"C",("Q","C"):"C",("G","C"):"C",("I","C"):"C",("L","C"):"C",("M","C"):"C",("F","C"):"R",("P","C"):"C",("S","C"):"C",("T","C"):"C",("W","C"):"R",("Y","C"):"R",("V","C"):"C",("G","Q"):"C",("I","Q"):"C",("L","Q"):"C",("M","Q"):"C",("F","Q"):"R",("P","Q"):"C",("S","Q"):"C",("T","Q"):"C",("W","Q"):"R",("Y","Q"):"R",("V","Q"):"C",("I","G"):"C",("L","G"):"C",("M","G"):"C",("F","G"):"R",("P","G"):"C",("S","G"):"C",("T","G"):"C",("W","G"):"R",("Y","G"):"R",("V","G"):"C",("L","I"):"C",("M","I"):"C",("F","I"):"R",("P","I"):"C",("S","I"):"C",("T","I"):"C",("W","I"):"R",("Y","I"):"R",("V","I"):"C",("M","L"):"C",("F","L"):"R",("P","L"):"C",("S","L"):"C",("T","L"):"C",("W","L"):"R",("Y","L"):"R",("V","L"):"C",("F","M"):"R",("P","M"):"C",("S","M"):"C",("T","M"):"C",("W","M"):"R",("Y","M"):"R",("V","M"):"C",("P","F"):"R",("S","F"):"R",("T","F"):"R",("W","F"):"C",("Y","F"):"C",("V","F"):"R",("S","P"):"C",("T","P"):"C",("W","P"):"R",("Y","P"):"R",("V","P"):"C",("T","S"):"C",("W","S"):"R",("Y","S"):"R",("V","S"):"R",("W","T"):"R",("Y","T"):"R",("V","T"):"C",("Y","W"):"C",("V","W"):"R",("V","Y"):"R",("R","*"):"R",("H","*"):"R",("K","*"):"R",("D","*"):"R",("E","*"):"R",("A","*"):"R",("N","*"):"R",("C","*"):"R",("Q","*"):"R",("G","*"):"R",("I","*"):"R",("L","*"):"R",("M","*"):"R",("F","*"):"R",("P","*"):"R",("S","*"):"R",("T","*"):"R",("W","*"):"R",("Y","*"):"R",("V","*"):"R",("*","R"):"R",("*","H"):"R",("*","K"):"R",("*","D"):"R",("*","E"):"R",("*","A"):"R",("*","N"):"R",("*","C"):"R",("*","Q"):"R",("*","G"):"R",("*","I"):"R",("*","L"):"R",("*","M"):"R",("*","F"):"R",("*","P"):"R",("*","S"):"R",("*","T"):"R",("*","W"):"R",("*","Y"):"R",("*","V"):"R"}
    aaSchemeDict6 = {("R","H"):"C",("R","K"):"C",("R","D"):"R",("R","E"):"R",("R","A"):"R",("R","N"):"R",("R","C"):"R",("R","Q"):"R",("R","G"):"R",("R","I"):"R",("R","L"):"R",("R","M"):"R",("R","F"):"R",("R","P"):"R",("R","S"):"R",("R","T"):"R",("R","W"):"R",("R","Y"):"R",("R","V"):"R",("H","K"):"C",("H","D"):"R",("H","E"):"R",("H","A"):"R",("H","N"):"R",("H","C"):"R",("H","Q"):"R",("H","G"):"R",("H","I"):"R",("H","L"):"R",("H","M"):"R",("H","F"):"R",("H","P"):"R",("H","S"):"R",("H","T"):"R",("H","W"):"R",("H","Y"):"R",("H","V"):"R",("K","D"):"R",("K","E"):"R",("K","A"):"R",("K","N"):"R",("K","C"):"R",("K","Q"):"R",("K","G"):"R",("K","I"):"R",("K","L"):"R",("K","M"):"R",("K","F"):"R",("K","P"):"R",("K","S"):"R",("K","T"):"R",("K","W"):"R",("K","Y"):"R",("K","V"):"R",("D","E"):"C",("D","A"):"R",("D","N"):"R",("D","C"):"R",("D","Q"):"R",("D","G"):"R",("D","I"):"R",("D","L"):"R",("D","M"):"R",("D","F"):"R",("D","P"):"R",("D","S"):"R",("D","T"):"R",("D","W"):"R",("D","Y"):"R",("D","V"):"R",("E","A"):"R",("E","N"):"R",("E","C"):"R",("E","Q"):"R",("E","G"):"R",("E","I"):"R",("E","L"):"R",("E","M"):"R",("E","F"):"R",("E","P"):"R",("E","S"):"R",("E","T"):"R",("E","W"):"R",("E","Y"):"R",("E","V"):"R",("A","N"):"R",("A","C"):"R",("A","Q"):"R",("A","G"):"C",("A","I"):"C",("A","L"):"C",("A","M"):"C",("A","F"):"C",("A","P"):"C",("A","S"):"R",("A","T"):"R",("A","W"):"C",("A","Y"):"R",("A","V"):"C",("N","C"):"C",("N","Q"):"C",("N","G"):"R",("N","I"):"R",("N","L"):"R",("N","M"):"R",("N","F"):"R",("N","P"):"R",("N","S"):"C",("N","T"):"C",("N","W"):"R",("N","Y"):"C",("N","V"):"R",("C","Q"):"C",("C","G"):"R",("C","I"):"R",("C","L"):"R",("C","M"):"R",("C","F"):"R",("C","P"):"R",("C","S"):"C",("C","T"):"C",("C","W"):"R",("C","Y"):"C",("C","V"):"R",("Q","G"):"R",("Q","I"):"R",("Q","L"):"R",("Q","M"):"R",("Q","F"):"R",("Q","P"):"R",("Q","S"):"C",("Q","T"):"C",("Q","W"):"R",("Q","Y"):"C",("Q","V"):"R",("G","I"):"C",("G","L"):"C",("G","M"):"C",("G","F"):"C",("G","P"):"C",("G","S"):"R",("G","T"):"R",("G","W"):"C",("G","Y"):"R",("G","V"):"C",("I","L"):"C",("I","M"):"C",("I","F"):"C",("I","P"):"C",("I","S"):"R",("I","T"):"R",("I","W"):"C",("I","Y"):"R",("I","V"):"C",("L","M"):"C",("L","F"):"C",("L","P"):"C",("L","S"):"R",("L","T"):"R",("L","W"):"C",("L","Y"):"R",("L","V"):"C",("M","F"):"C",("M","P"):"C",("M","S"):"R",("M","T"):"R",("M","W"):"C",("M","Y"):"R",("M","V"):"C",("F","P"):"C",("F","S"):"R",("F","T"):"R",("F","W"):"C",("F","Y"):"R",("F","V"):"C",("P","S"):"R",("P","T"):"R",("P","W"):"C",("P","Y"):"R",("P","V"):"C",("S","T"):"C",("S","W"):"R",("S","Y"):"C",("S","V"):"R",("T","W"):"R",("T","Y"):"C",("T","V"):"R",("W","Y"):"R",("W","V"):"C",("Y","V"):"R",("H","R"):"C",("K","R"):"C",("D","R"):"R",("E","R"):"R",("A","R"):"R",("N","R"):"R",("C","R"):"R",("Q","R"):"R",("G","R"):"R",("I","R"):"R",("L","R"):"R",("M","R"):"R",("F","R"):"R",("P","R"):"R",("S","R"):"R",("T","R"):"R",("W","R"):"R",("Y","R"):"R",("V","R"):"R",("K","H"):"C",("D","H"):"R",("E","H"):"R",("A","H"):"R",("N","H"):"R",("C","H"):"R",("Q","H"):"R",("G","H"):"R",("I","H"):"R",("L","H"):"R",("M","H"):"R",("F","H"):"R",("P","H"):"R",("S","H"):"R",("T","H"):"R",("W","H"):"R",("Y","H"):"R",("V","H"):"R",("D","K"):"R",("E","K"):"R",("A","K"):"R",("N","K"):"R",("C","K"):"R",("Q","K"):"R",("G","K"):"R",("I","K"):"R",("L","K"):"R",("M","K"):"R",("F","K"):"R",("P","K"):"R",("S","K"):"R",("T","K"):"R",("W","K"):"R",("Y","K"):"R",("V","K"):"R",("E","D"):"C",("A","D"):"R",("N","D"):"R",("C","D"):"R",("Q","D"):"R",("G","D"):"R",("I","D"):"R",("L","D"):"R",("M","D"):"R",("F","D"):"R",("P","D"):"R",("S","D"):"R",("T","D"):"R",("W","D"):"R",("Y","D"):"R",("V","D"):"R",("A","E"):"R",("N","E"):"R",("C","E"):"R",("Q","E"):"R",("G","E"):"R",("I","E"):"R",("L","E"):"R",("M","E"):"R",("F","E"):"R",("P","E"):"R",("S","E"):"R",("T","E"):"R",("W","E"):"R",("Y","E"):"R",("V","E"):"R",("N","A"):"R",("C","A"):"R",("Q","A"):"R",("G","A"):"C",("I","A"):"C",("L","A"):"C",("M","A"):"C",("F","A"):"C",("P","A"):"C",("S","A"):"R",("T","A"):"R",("W","A"):"C",("Y","A"):"R",("V","A"):"C",("C","N"):"C",("Q","N"):"C",("G","N"):"R",("I","N"):"R",("L","N"):"R",("M","N"):"R",("F","N"):"R",("P","N"):"R",("S","N"):"C",("T","N"):"C",("W","N"):"R",("Y","N"):"C",("V","N"):"R",("Q","C"):"C",("G","C"):"R",("I","C"):"R",("L","C"):"R",("M","C"):"R",("F","C"):"R",("P","C"):"R",("S","C"):"C",("T","C"):"C",("W","C"):"R",("Y","C"):"C",("V","C"):"R",("G","Q"):"R",("I","Q"):"R",("L","Q"):"R",("M","Q"):"R",("F","Q"):"R",("P","Q"):"R",("S","Q"):"C",("T","Q"):"C",("W","Q"):"R",("Y","Q"):"C",("V","Q"):"R",("I","G"):"C",("L","G"):"C",("M","G"):"C",("F","G"):"C",("P","G"):"C",("S","G"):"R",("T","G"):"R",("W","G"):"C",("Y","G"):"R",("V","G"):"C",("L","I"):"C",("M","I"):"C",("F","I"):"C",("P","I"):"C",("S","I"):"R",("T","I"):"R",("W","I"):"C",("Y","I"):"R",("V","I"):"C",("M","L"):"C",("F","L"):"C",("P","L"):"C",("S","L"):"R",("T","L"):"R",("W","L"):"C",("Y","L"):"R",("V","L"):"C",("F","M"):"C",("P","M"):"C",("S","M"):"R",("T","M"):"R",("W","M"):"C",("Y","M"):"R",("V","M"):"C",("P","F"):"C",("S","F"):"R",("T","F"):"R",("W","F"):"C",("Y","F"):"R",("V","F"):"C",("S","P"):"R",("T","P"):"R",("W","P"):"C",("Y","P"):"R",("V","P"):"C",("T","S"):"C",("W","S"):"R",("Y","S"):"C",("V","S"):"R",("W","T"):"R",("Y","T"):"C",("V","T"):"R",("Y","W"):"R",("V","W"):"C",("V","Y"):"R",("R","*"):"R",("H","*"):"R",("K","*"):"R",("D","*"):"R",("E","*"):"R",("A","*"):"R",("N","*"):"R",("C","*"):"R",("Q","*"):"R",("G","*"):"R",("I","*"):"R",("L","*"):"R",("M","*"):"R",("F","*"):"R",("P","*"):"R",("S","*"):"R",("T","*"):"R",("W","*"):"R",("Y","*"):"R",("V","*"):"R",("*","R"):"R",("*","H"):"R",("*","K"):"R",("*","D"):"R",("*","E"):"R",("*","A"):"R",("*","N"):"R",("*","C"):"R",("*","Q"):"R",("*","G"):"R",("*","I"):"R",("*","L"):"R",("*","M"):"R",("*","F"):"R",("*","P"):"R",("*","S"):"R",("*","T"):"R",("*","W"):"R",("*","Y"):"R",("*","V"):"R"}
    aaSchemeDict7 = {("R","H"):"C",("R","K"):"C",("R","D"):"R",("R","E"):"R",("R","A"):"R",("R","N"):"R",("R","C"):"R",("R","Q"):"R",("R","G"):"R",("R","I"):"R",("R","L"):"R",("R","M"):"R",("R","F"):"R",("R","P"):"R",("R","S"):"R",("R","T"):"R",("R","W"):"R",("R","Y"):"R",("R","V"):"R",("H","K"):"C",("H","D"):"R",("H","E"):"R",("H","A"):"R",("H","N"):"R",("H","C"):"R",("H","Q"):"R",("H","G"):"R",("H","I"):"R",("H","L"):"R",("H","M"):"R",("H","F"):"R",("H","P"):"R",("H","S"):"R",("H","T"):"R",("H","W"):"R",("H","Y"):"R",("H","V"):"R",("K","D"):"R",("K","E"):"R",("K","A"):"R",("K","N"):"R",("K","C"):"R",("K","Q"):"R",("K","G"):"R",("K","I"):"R",("K","L"):"R",("K","M"):"R",("K","F"):"R",("K","P"):"R",("K","S"):"R",("K","T"):"R",("K","W"):"R",("K","Y"):"R",("K","V"):"R",("D","E"):"C",("D","A"):"R",("D","N"):"R",("D","C"):"R",("D","Q"):"R",("D","G"):"R",("D","I"):"R",("D","L"):"R",("D","M"):"R",("D","F"):"R",("D","P"):"R",("D","S"):"R",("D","T"):"R",("D","W"):"R",("D","Y"):"R",("D","V"):"R",("E","A"):"R",("E","N"):"R",("E","C"):"R",("E","Q"):"R",("E","G"):"R",("E","I"):"R",("E","L"):"R",("E","M"):"R",("E","F"):"R",("E","P"):"R",("E","S"):"R",("E","T"):"R",("E","W"):"R",("E","Y"):"R",("E","V"):"R",("A","N"):"R",("A","C"):"R",("A","Q"):"R",("A","G"):"R",("A","I"):"C",("A","L"):"C",("A","M"):"C",("A","F"):"C",("A","P"):"C",("A","S"):"R",("A","T"):"R",("A","W"):"C",("A","Y"):"R",("A","V"):"C",("N","C"):"C",("N","Q"):"C",("N","G"):"C",("N","I"):"R",("N","L"):"R",("N","M"):"R",("N","F"):"R",("N","P"):"R",("N","S"):"C",("N","T"):"C",("N","W"):"R",("N","Y"):"C",("N","V"):"R",("C","Q"):"C",("C","G"):"C",("C","I"):"R",("C","L"):"R",("C","M"):"R",("C","F"):"R",("C","P"):"R",("C","S"):"C",("C","T"):"C",("C","W"):"R",("C","Y"):"C",("C","V"):"R",("Q","G"):"C",("Q","I"):"R",("Q","L"):"R",("Q","M"):"R",("Q","F"):"R",("Q","P"):"R",("Q","S"):"C",("Q","T"):"C",("Q","W"):"R",("Q","Y"):"C",("Q","V"):"R",("G","I"):"R",("G","L"):"R",("G","M"):"R",("G","F"):"R",("G","P"):"R",("G","S"):"C",("G","T"):"C",("G","W"):"R",("G","Y"):"C",("G","V"):"R",("I","L"):"C",("I","M"):"C",("I","F"):"C",("I","P"):"C",("I","S"):"R",("I","T"):"R",("I","W"):"C",("I","Y"):"R",("I","V"):"C",("L","M"):"C",("L","F"):"C",("L","P"):"C",("L","S"):"R",("L","T"):"R",("L","W"):"C",("L","Y"):"R",("L","V"):"C",("M","F"):"C",("M","P"):"C",("M","S"):"R",("M","T"):"R",("M","W"):"C",("M","Y"):"R",("M","V"):"C",("F","P"):"C",("F","S"):"R",("F","T"):"R",("F","W"):"C",("F","Y"):"R",("F","V"):"C",("P","S"):"R",("P","T"):"R",("P","W"):"C",("P","Y"):"R",("P","V"):"C",("S","T"):"C",("S","W"):"R",("S","Y"):"C",("S","V"):"R",("T","W"):"R",("T","Y"):"C",("T","V"):"R",("W","Y"):"R",("W","V"):"C",("Y","V"):"R",("H","R"):"C",("K","R"):"C",("D","R"):"R",("E","R"):"R",("A","R"):"R",("N","R"):"R",("C","R"):"R",("Q","R"):"R",("G","R"):"R",("I","R"):"R",("L","R"):"R",("M","R"):"R",("F","R"):"R",("P","R"):"R",("S","R"):"R",("T","R"):"R",("W","R"):"R",("Y","R"):"R",("V","R"):"R",("K","H"):"C",("D","H"):"R",("E","H"):"R",("A","H"):"R",("N","H"):"R",("C","H"):"R",("Q","H"):"R",("G","H"):"R",("I","H"):"R",("L","H"):"R",("M","H"):"R",("F","H"):"R",("P","H"):"R",("S","H"):"R",("T","H"):"R",("W","H"):"R",("Y","H"):"R",("V","H"):"R",("D","K"):"R",("E","K"):"R",("A","K"):"R",("N","K"):"R",("C","K"):"R",("Q","K"):"R",("G","K"):"R",("I","K"):"R",("L","K"):"R",("M","K"):"R",("F","K"):"R",("P","K"):"R",("S","K"):"R",("T","K"):"R",("W","K"):"R",("Y","K"):"R",("V","K"):"R",("E","D"):"C",("A","D"):"R",("N","D"):"R",("C","D"):"R",("Q","D"):"R",("G","D"):"R",("I","D"):"R",("L","D"):"R",("M","D"):"R",("F","D"):"R",("P","D"):"R",("S","D"):"R",("T","D"):"R",("W","D"):"R",("Y","D"):"R",("V","D"):"R",("A","E"):"R",("N","E"):"R",("C","E"):"R",("Q","E"):"R",("G","E"):"R",("I","E"):"R",("L","E"):"R",("M","E"):"R",("F","E"):"R",("P","E"):"R",("S","E"):"R",("T","E"):"R",("W","E"):"R",("Y","E"):"R",("V","E"):"R",("N","A"):"R",("C","A"):"R",("Q","A"):"R",("G","A"):"R",("I","A"):"C",("L","A"):"C",("M","A"):"C",("F","A"):"C",("P","A"):"C",("S","A"):"R",("T","A"):"R",("W","A"):"C",("Y","A"):"R",("V","A"):"C",("C","N"):"C",("Q","N"):"C",("G","N"):"C",("I","N"):"R",("L","N"):"R",("M","N"):"R",("F","N"):"R",("P","N"):"R",("S","N"):"C",("T","N"):"C",("W","N"):"R",("Y","N"):"C",("V","N"):"R",("Q","C"):"C",("G","C"):"C",("I","C"):"R",("L","C"):"R",("M","C"):"R",("F","C"):"R",("P","C"):"R",("S","C"):"C",("T","C"):"C",("W","C"):"R",("Y","C"):"C",("V","C"):"R",("G","Q"):"C",("I","Q"):"R",("L","Q"):"R",("M","Q"):"R",("F","Q"):"R",("P","Q"):"R",("S","Q"):"C",("T","Q"):"C",("W","Q"):"R",("Y","Q"):"C",("V","Q"):"R",("I","G"):"R",("L","G"):"R",("M","G"):"R",("F","G"):"R",("P","G"):"R",("S","G"):"C",("T","G"):"C",("W","G"):"R",("Y","G"):"C",("V","G"):"R",("L","I"):"C",("M","I"):"C",("F","I"):"C",("P","I"):"C",("S","I"):"R",("T","I"):"R",("W","I"):"C",("Y","I"):"R",("V","I"):"C",("M","L"):"C",("F","L"):"C",("P","L"):"C",("S","L"):"R",("T","L"):"R",("W","L"):"C",("Y","L"):"R",("V","L"):"C",("F","M"):"C",("P","M"):"C",("S","M"):"R",("T","M"):"R",("W","M"):"C",("Y","M"):"R",("V","M"):"C",("P","F"):"C",("S","F"):"R",("T","F"):"R",("W","F"):"C",("Y","F"):"R",("V","F"):"C",("S","P"):"R",("T","P"):"R",("W","P"):"C",("Y","P"):"R",("V","P"):"C",("T","S"):"C",("W","S"):"R",("Y","S"):"C",("V","S"):"R",("W","T"):"R",("Y","T"):"C",("V","T"):"R",("Y","W"):"R",("V","W"):"C",("V","Y"):"R",("R","*"):"R",("H","*"):"R",("K","*"):"R",("D","*"):"R",("E","*"):"R",("A","*"):"R",("N","*"):"R",("C","*"):"R",("Q","*"):"R",("G","*"):"R",("I","*"):"R",("L","*"):"R",("M","*"):"R",("F","*"):"R",("P","*"):"R",("S","*"):"R",("T","*"):"R",("W","*"):"R",("Y","*"):"R",("V","*"):"R",("*","R"):"R",("*","H"):"R",("*","K"):"R",("*","D"):"R",("*","E"):"R",("*","A"):"R",("*","N"):"R",("*","C"):"R",("*","Q"):"R",("*","G"):"R",("*","I"):"R",("*","L"):"R",("*","M"):"R",("*","F"):"R",("*","P"):"R",("*","S"):"R",("*","T"):"R",("*","W"):"R",("*","Y"):"R",("*","V"):"R"}
    totalSynSites = 0.0
    totalNonsynSites = 0.0
    totalC1Sites = 0.0
    totalR1Sites = 0.0
    totalC2Sites = 0.0
    totalR2Sites = 0.0
    totalC3Sites = 0.0
    totalR3Sites = 0.0
    totalC4Sites = 0.0
    totalR4Sites = 0.0
    totalC5Sites = 0.0
    totalR5Sites = 0.0
    totalC6Sites = 0.0
    totalR6Sites = 0.0
    totalC7Sites = 0.0
    totalR7Sites = 0.0
    codonNum = 0
    for codon in codonList:
        if 'N' in codon or '-' in codon:
            totalSynSites += 0.729166667
            totalNonsynSites += 2.270833333
            totalC1Sites += 1.395833333	
            totalR1Sites += 0.875	
            totalC2Sites += 1.270833333	
            totalR2Sites += 1	
            totalC3Sites += 0.708333333	
            totalR3Sites += 1.5625	
            totalC4Sites += 0.895833333	
            totalR4Sites += 1.375	
            totalC5Sites += 1.0625	
            totalR5Sites += 1.208333333	
            totalC6Sites += 0.854166667	
            totalR6Sites += 1.416666667	
            totalC7Sites += 0.8125	
            totalR7Sites += 1.458333333
        else:
            currS = 0.0
            currN = 0.0
            currC1 = 0.0
            currC2 = 0.0
            currC3 = 0.0
            currC4 = 0.0
            currC5 = 0.0
            currC6 = 0.0
            currC7 = 0.0
            currR1 = 0.0
            currR2 = 0.0
            currR3 = 0.0
            currR4 = 0.0
            currR5 = 0.0
            currR6 = 0.0
            currR7 = 0.0
            site1 = codon[0]
            site2 = codon[1]
            site3 = codon[2]
            if site1 == 'A':
                mut1 = 'C' + site2 + site3
                mut2 = 'G' + site2 + site3
                mut3 = 'T' + site2 + site3
            elif site1 == 'C':
                mut1 = 'A' + site2 + site3
                mut2 = 'G' + site2 + site3
                mut3 = 'T' + site2 + site3
            elif site1 == 'G':
                mut1 = 'A' + site2 + site3
                mut2 = 'C' + site2 + site3
                mut3 = 'T' + site2 + site3
            elif site1 == 'T':
                mut1 = 'A' + site2 + site3
                mut2 = 'C' + site2 + site3
                mut3 = 'G' + site2 + site3
            if site2 == 'A':
                mut4 = site1 + 'C' + site3
                mut5 = site1 + 'G' + site3
                mut6 = site1 + 'T' + site3
            elif site2 == 'C':
                mut4 = site1 + 'A' + site3
                mut5 = site1 + 'G' + site3
                mut6 = site1 + 'T' + site3
            elif site2 == 'G':
                mut4 = site1 + 'A' + site3
                mut5 = site1 + 'C' + site3
                mut6 = site1 + 'T' + site3
            elif site2 == 'T':
                mut4 = site1 + 'A' + site3
                mut5 = site1 + 'C' + site3
                mut6 = site1 + 'G' + site3
            if site3 == 'A':
                mut7 = site1 + site2 + 'C'
                mut8 = site1 + site2 + 'G'
                mut9 = site1 + site2 + 'T'
            elif site3 == 'C':
                mut7 = site1 + site2 + 'A'
                mut8 = site1 + site2 + 'G'
                mut9 = site1 + site2 + 'T'
            elif site3 == 'G':
                mut7 = site1 + site2 + 'A'
                mut8 = site1 + site2 + 'C'
                mut9 = site1 + site2 + 'T'
            elif site3 == 'T':
                mut7 = site1 + site2 + 'A'
                mut8 = site1 + site2 + 'C'
                mut9 = site1 + site2 + 'G'
            if codonNum == 0:
                aaList = []
                if codon in startCodons:
                    currAA = 'M'
                else:
                    currAA = geneticCode[codon]
                if mut1 in startCodons:
                    aaList.append('M')
                else:
                    aaList.append(geneticCode[mut1])
                if mut2 in startCodons:
                    aaList.append('M')
                else:
                    aaList.append(geneticCode[mut2])
                if mut3 in startCodons:
                    aaList.append('M')
                else:
                    aaList.append(geneticCode[mut3])
                if mut4 in startCodons:
                    aaList.append('M')
                else:
                    aaList.append(geneticCode[mut4])
                if mut5 in startCodons:
                    aaList.append('M')
                else:
                    aaList.append(geneticCode[mut5])
                if mut6 in startCodons:
                    aaList.append('M')
                else:
                    aaList.append(geneticCode[mut6])
                if mut7 in startCodons:
                    aaList.append('M')
                else:
                    aaList.append(geneticCode[mut7])
                if mut8 in startCodons:
                    aaList.append('M')
                else:
                    aaList.append(geneticCode[mut8])
                if mut9 in startCodons:
                    aaList.append('M')
                else:
                    aaList.append(geneticCode[mut9])
            else:
                aaList = [geneticCode[mut1],geneticCode[mut2],geneticCode[mut3], geneticCode[mut4],geneticCode[mut5],geneticCode[mut6],geneticCode[mut7],geneticCode[mut8],geneticCode[mut9]]
                currAA = geneticCode[codon]
            for aa in aaList:
                if aa == currAA:
                    currS += 1.0
                else:
                    currN += 1.0
                    conRad1 = aaSchemeDict1[(currAA,aa)]
                    conRad2 = aaSchemeDict2[(currAA,aa)]
                    conRad3 = aaSchemeDict3[(currAA,aa)]
                    conRad4 = aaSchemeDict4[(currAA,aa)]
                    conRad5 = aaSchemeDict5[(currAA,aa)]
                    conRad6 = aaSchemeDict6[(currAA,aa)]
                    conRad7 = aaSchemeDict7[(currAA,aa)]
                    if conRad1 == 'R':
                        currR1 += 1
                    else:
                        currC1 += 1
                    if conRad2 == 'R':
                        currR2 += 1
                    else:
                        currC2 += 1
                    if conRad3 == 'R':
                        currR3 += 1
                    else:
                        currC3 += 1
                    if conRad4 == 'R':
                        currR4 += 1
                    else:
                        currC4 += 1
                    if conRad5 == 'R':
                        currR5 += 1
                    else:
                        currC5 += 1
                    if conRad6 == 'R':
                        currR6 += 1
                    else:
                        currC6 += 1
                    if conRad7 == 'R':
                        currR7 += 1
                    else:
                        currC7 += 1
            currS /= 3.0
            currN /= 3.0
            currC1 /= 3.0
            currC2 /= 3.0
            currC3 /= 3.0
            currC4 /= 3.0
            currC5 /= 3.0
            currC6 /= 3.0
            currC7 /= 3.0
            currR1 /= 3.0
            currR2 /= 3.0
            currR3 /= 3.0
            currR4 /= 3.0
            currR5 /= 3.0
            currR6 /= 3.0
            currR7 /= 3.0
            totalSynSites += currS
            totalNonsynSites += currN
            totalC1Sites += currC1
            totalR1Sites += currR1
            totalC2Sites += currC2
            totalR2Sites += currR2
            totalC3Sites += currC3
            totalR3Sites += currR3
            totalC4Sites += currC4
            totalR4Sites += currR4
            totalC5Sites += currC5
            totalR5Sites += currR5
            totalC6Sites += currC6
            totalR6Sites += currR6
            totalC7Sites += currC7
            totalR7Sites += currR7
            codonNum += 1
    return [totalSynSites,totalNonsynSites,totalC1Sites,totalR1Sites,totalC2Sites,totalR2Sites,totalC3Sites,totalR3Sites,totalC4Sites,totalR4Sites,totalC5Sites,totalR5Sites,totalC6Sites,totalR6Sites,totalC7Sites,totalR7Sites]

def mapChanges(fasta):
    cladeDict = {'A': ['>$Heron2',  '>$clone_1',  '>$Rotoiti_1_4n',  '>$AC51',  '>$Heron_mitochondrion',  '>$Grasmere_6_3n',  '>$Poerua_triploid',  '>$Brunner_6_3n',  '>$McGregor',  '>$Poerua_72_4n',  '>$Gunn',  '>$*Lady',  '>$Grasmere_1_4n',  '>$*Kaniere_1_2n',  '>$*Rotoroa_1_2n',  '>$*AlexMap',  '>$*Alexsex',  '>$*Yellow_Contig_56',  '>$clone_7',  '>$DenmarkA',  '>$Duluth',  '>$Waik_lane4_TCCTGAGC_trimmed_paired_contig_237',  '>$*Ianthe',  '>$*Ianthe_lane1_TAAGGCGA_trimmed_paired_contig_309',  '>$Waik37',  '>$Waik372',  '>$Tarawera',  '>$Kaniere_triploid',  '>$Waik36',  '>$WalesC',  '>$Brunner_2_4n'], 'B': ['>$Waik37',  '>$Waik372',  '>$Tarawera',  '>$Kaniere_triploid',  '>$Waik36',  '>$WalesC',  '>$Brunner_2_4n'], 'C': ['>$Waik37',  '>$Waik372',  '>$Tarawera',  '>$Kaniere_triploid',  '>$Waik36',  '>$WalesC'], 'D': ['>$Waik37',  '>$Waik372',  '>$Tarawera',  '>$Kaniere_triploid',  '>$Waik36'], 'E': ['>$Waik37', '>$Waik372', '>$Tarawera', '>$Kaniere_triploid'], 'F': ['>$Waik37', '>$Waik372', '>$Tarawera'], 'G': ['>$Heron2',  '>$clone_1',  '>$Rotoiti_1_4n',  '>$AC51',  '>$Heron_mitochondrion',  '>$Grasmere_6_3n',  '>$Poerua_triploid',  '>$Brunner_6_3n',  '>$McGregor',  '>$Poerua_72_4n',  '>$Gunn',  '>$*Lady',  '>$Grasmere_1_4n',  '>$*Kaniere_1_2n',  '>$*Rotoroa_1_2n',  '>$*AlexMap',  '>$*Alexsex',  '>$*Yellow_Contig_56',  '>$clone_7',  '>$DenmarkA',  '>$Duluth',  '>$Waik_lane4_TCCTGAGC_trimmed_paired_contig_237',  '>$*Ianthe',  '>$*Ianthe_lane1_TAAGGCGA_trimmed_paired_contig_309'], 'H': ['>$*Ianthe',  '>$*Ianthe_lane1_TAAGGCGA_trimmed_paired_contig_309'], 'I': ['>$Heron2',  '>$clone_1',  '>$Rotoiti_1_4n',  '>$AC51',  '>$Heron_mitochondrion',  '>$Grasmere_6_3n',  '>$Poerua_triploid',  '>$Brunner_6_3n',  '>$McGregor',  '>$Poerua_72_4n',  '>$Gunn',  '>$*Lady',  '>$Grasmere_1_4n',  '>$*Kaniere_1_2n',  '>$*Rotoroa_1_2n',  '>$*AlexMap',  '>$*Alexsex',  '>$*Yellow_Contig_56',  '>$clone_7',  '>$DenmarkA',  '>$Duluth',  '>$Waik_lane4_TCCTGAGC_trimmed_paired_contig_237'], 'J': ['>$clone_7',  '>$DenmarkA',  '>$Duluth',  '>$Waik_lane4_TCCTGAGC_trimmed_paired_contig_237'], 'K': ['>$clone_7', '>$DenmarkA', '>$Duluth'], 'L': ['>$clone_7', '>$DenmarkA'], 'M': ['>$Heron2',  '>$clone_1',  '>$Rotoiti_1_4n',  '>$AC51',  '>$Heron_mitochondrion',  '>$Grasmere_6_3n',  '>$Poerua_triploid',  '>$Brunner_6_3n',  '>$McGregor',  '>$Poerua_72_4n',  '>$Gunn',  '>$*Lady',  '>$Grasmere_1_4n',  '>$*Kaniere_1_2n',  '>$*Rotoroa_1_2n',  '>$*AlexMap',  '>$*Alexsex',  '>$*Yellow_Contig_56'], 'N': ['>$*AlexMap', '>$*Alexsex', '>$*Yellow_Contig_56'], 'O': ['>$Heron2',  '>$clone_1',  '>$Rotoiti_1_4n',  '>$AC51',  '>$Heron_mitochondrion',  '>$Grasmere_6_3n',  '>$Poerua_triploid',  '>$Brunner_6_3n',  '>$McGregor',  '>$Poerua_72_4n',  '>$Gunn',  '>$*Lady',  '>$Grasmere_1_4n',  '>$*Kaniere_1_2n',  '>$*Rotoroa_1_2n'], 'P': ['>$Heron2',  '>$clone_1',  '>$Rotoiti_1_4n',  '>$AC51',  '>$Heron_mitochondrion',  '>$Grasmere_6_3n',  '>$Poerua_triploid',  '>$Brunner_6_3n',  '>$McGregor',  '>$Poerua_72_4n',  '>$Gunn',  '>$*Lady',  '>$Grasmere_1_4n',  '>$*Kaniere_1_2n'], 'Q': ['>$*Lady', '>$Grasmere_1_4n', '>$*Kaniere_1_2n'], 'R': ['>$*Lady', '>$Grasmere_1_4n'], 'S': ['>$Heron2',  '>$clone_1',  '>$Rotoiti_1_4n',  '>$AC51',  '>$Heron_mitochondrion',  '>$Grasmere_6_3n',  '>$Poerua_triploid',  '>$Brunner_6_3n',  '>$McGregor',  '>$Poerua_72_4n',  '>$Gunn'], 'T': ['>$McGregor', '>$Poerua_72_4n', '>$Gunn'], 'U': ['>$McGregor', '>$Poerua_72_4n'], 'V': ['>$Heron2',  '>$clone_1',  '>$Rotoiti_1_4n',  '>$AC51',  '>$Heron_mitochondrion',  '>$Grasmere_6_3n',  '>$Poerua_triploid',  '>$Brunner_6_3n'], 'W': ['>$AC51',  '>$Heron_mitochondrion',  '>$Grasmere_6_3n',  '>$Poerua_triploid'], 'X': ['>$AC51', '>$Heron_mitochondrion', '>$Grasmere_6_3n'], 'Y': ['>$Heron2', '>$clone_1', '>$Rotoiti_1_4n'], 'Z': ['>$Heron2', '>$clone_1']}
    positionDict = {(0,1533):'COI',(1533,2217):'COII',(2217,2373):'ATP8',(2373,3066):'ATP6',(3066,4005):'ND1',(4005,4509):'ND6',(4509,5646):'CYTB',(5646,5940):'ND4L',(5940,7314):'ND4',(7314,9030):'ND5',(9030,9807):'COIII',(9807,10158):'ND3',(10158,11214):'ND2'} #{(start,stop):gene}
    seqDict, seqList, codonDict = buildCodonDict(fasta)
    cladeList = ['H','L','R','U','Z','F','K','N','Q','T','Y','X','E','J','W','D','C','B','V','S','P','O','M','I','G','A']
    popList = []
    sexList = []
    outList = [] 
    asexList = []
    for seq in seqList:
        if '$' in seq:
            popList.append(seq)
            if '*' in seq:
                sexList.append(seq)
            else:
                asexList.append(seq)
        else:
            outList.append(seq)
    outSeq = seqDict[outList[0]]
    sys.stdout.write('Total Polymorphisms\nGene\tSite\tCodon\tLineages w/ Derived Allele\t# Individuals w/ derived allele\tAlleles\tP. est\n')
    i = 0
    while i < len(seqDict[seqList[0]]):
        outNuc = outSeq[i]
        gene = False
        for locus in positionDict:
            start = locus[0]
            stop = locus[1]
            if i >= start and i <= stop:
                gene = positionDict[locus]
        currAlleleDict = {}
        currAlleleList = []
        for seq in popList:
            currSeq = seqDict[seq]
            currNuc = currSeq[i]
            if currNuc not in currAlleleDict and 'N' != currNuc and '-' != currNuc:
                currAlleleDict[currNuc] = [seq]
                currAlleleList.append(currNuc)
            elif 'N' != currNuc and '-' != currNuc:
                currList = currAlleleDict[currNuc]
                currList.append(seq)
                currAlleleDict[currNuc] = currList
        if len(currAlleleDict) > 1:
            for nuc in currAlleleList:
                if nuc != outNuc:
                    currCladeList = cladeList
                    currList = currAlleleDict[nuc]
                    for group in cladeList:
                        compClade = cladeDict[group]
                        removeClade = False
                        for lineage in currList:
                            if lineage not in compClade:
                                removeClade = True
                        if removeClade == True:
                            currCladeList.remove(group)
                    print currCladeList
                    if len(currAlleleDict[nuc]) > 1:
                        sys.stdout.write(gene + '\t' + str(i + 1) + '\t' + str((i*3)+1) + '\t' + str(currAlleleDict[nuc]) + '\t' + str(len(currAlleleDict[nuc])) + '\t' + str(currAlleleList) + '\t' + outNuc)
                        for clade in currCladeList:
                            sys.stdout.write('\t' + str(cladeDict[clade]))
                        sys.stdout.write('\n')
                    else:
                        sys.stdout.write(gene + '\t' + str(i + 1) + '\t' + str((i*3)+1) + '\t' + str(currAlleleDict[nuc]) + '\t' + str(len(currAlleleDict[nuc])) + '\t' + str(currAlleleList) + '\t' + outNuc + '\n')
        i += 1

def aN(N):
    aN = 0.0
    i = 1
    while i < N:
        aN += 1.0/i
        i += 1
    return aN

def thetaU(fasta,code='invertebrateMt'):
    geneticCodes = {'standard':{"TTT":"F",	"TTC":"F",	"TTA":"L",	"TTG":"L",	"TCT":"S",	"TCC":"S",	"TCA":"S",	"TCG":"S",	"TAT":"Y",	"TAC":"Y",	"TAA":"*",	"TAG":"*",	"TGT":"C",	"TGC":"C",	"TGA":"*",	"TGG":"W",	"CTT":"L",	"CTC":"L",	"CTA":"L",	"CTG":"L",	"CCT":"P",	"CCC":"P",	"CCA":"P",	"CCG":"P",	"CAT":"H",	"CAC":"H",	"CAA":"Q",	"CAG":"Q",	"CGT":"R",	"CGC":"R",	"CGA":"R",	"CGG":"R",	"ATT":"I",	"ATC":"I",	"ATA":"I",	"ATG":"M",	"ACT":"T",	"ACC":"T",	"ACA":"T",	"ACG":"T",	"AAT":"N",	"AAC":"N",	"AAA":"K",	"AAG":"K",	"AGT":"S",	"AGC":"S",	"AGA":"R",	"AGG":"R",	"GTT":"V",	"GTC":"V",	"GTA":"V",	"GTG":"V",	"GCT":"A",	"GCC":"A",	"GCA":"A",	"GCG":"A",	"GAT":"D",	"GAC":"D",	"GAA":"E",	"GAG":"E",	"GGT":"G",	"GGC":"G",	"GGA":"G",	"GGG":"G"},'invertebrateMt':{'CTT': 'L', 'TAG': '*', 'ACA': 'T', 'ACG': 'T', 'ATC': 'I', 'AAC': 'N', 'ATA': 'M', 'AGG': 'S', 'CCT': 'P', 'ACT': 'T', 'AGC': 'S', 'AAG': 'K', 'AGA': 'S', 'CAT': 'H', 'AAT': 'N', 'ATT': 'I', 'CTG': 'L', 'CTA': 'L', 'CTC': 'L', 'CAC': 'H', 'AAA': 'K', 'CCG': 'P', 'AGT': 'S', 'CCA': 'P', 'CAA': 'Q', 'CCC': 'P', 'TAT': 'Y', 'GGT': 'G', 'TGT': 'C', 'CGA': 'R', 'CAG': 'Q', 'TCT': 'S', 'GAT': 'D', 'CGG': 'R', 'TTT': 'F', 'TGC': 'C', 'GGG': 'G', 'TGA': 'W', 'GGA': 'G', 'TGG': 'W', 'GGC': 'G', 'TAC': 'Y', 'TTC': 'F', 'TCG': 'S', 'TTA': 'L', 'TTG': 'L', 'TCC': 'S', 'ACC': 'T', 'TAA': '*', 'GCA': 'A', 'GTA': 'V', 'GCC': 'A', 'GTC': 'V', 'GCG': 'A', 'GTG': 'V', 'GAG': 'E', 'GTT': 'V', 'GCT': 'A', 'GAC': 'D', 'CGT': 'R', 'GAA': 'E', 'TCA': 'S', 'ATG': 'M', 'CGC': 'R'},'vertebrateMt':{'CTT': 'L', 'TAG': '*', 'ACA': 'T', 'ACG': 'T', 'ATC': 'I', 'AAC': 'N', 'ATA': 'M', 'AGG': '*', 'CCT': 'P', 'ACT': 'T', 'AGC': 'S', 'AAG': 'K', 'AGA': '*', 'CAT': 'H', 'AAT': 'N', 'ATT': 'I', 'CTG': 'L', 'CTA': 'L', 'CTC': 'L', 'CAC': 'H', 'AAA': 'K', 'CCG': 'P', 'AGT': 'S', 'CCA': 'P', 'CAA': 'Q', 'CCC': 'P', 'TAT': 'Y', 'GGT': 'G', 'TGT': 'C', 'CGA': 'R', 'CAG': 'Q', 'TCT': 'S', 'GAT': 'D', 'CGG': 'R', 'TTT': 'F', 'TGC': 'C', 'GGG': 'G', 'TGA': 'W', 'GGA': 'G', 'TGG': 'W', 'GGC': 'G', 'TAC': 'Y', 'TTC': 'F', 'TCG': 'S', 'TTA': 'L', 'TTG': 'L', 'TCC': 'S', 'ACC': 'T', 'TAA': '*', 'GCA': 'A', 'GTA': 'V', 'GCC': 'A', 'GTC': 'V', 'GCG': 'A', 'GTG': 'V', 'GAG': 'E', 'GTT': 'V', 'GCT': 'A', 'GAC': 'D', 'CGT': 'R', 'GAA': 'E', 'TCA': 'S', 'ATG': 'M', 'CGC': 'R'}, 'yeastMt':{'CTT': 'T', 'TAG': '*', 'ACA': 'T', 'ACG': 'T', 'ATC': 'I', 'AAC': 'N', 'ATA': 'M', 'AGG': 'R', 'CCT': 'P', 'ACT': 'T', 'AGC': 'S', 'AAG': 'K', 'AGA': 'R', 'CAT': 'H', 'AAT': 'N', 'ATT': 'I', 'CTG': 'T', 'CTA': 'T', 'CTC': 'T', 'CAC': 'H', 'AAA': 'K', 'CCG': 'P', 'AGT': 'S', 'CCA': 'P', 'CAA': 'Q', 'CCC': 'P', 'TAT': 'Y', 'GGT': 'G', 'TGT': 'C', 'CGA': 'R', 'CAG': 'Q', 'TCT': 'S', 'GAT': 'D', 'CGG': 'R', 'TTT': 'F', 'TGC': 'C', 'GGG': 'G', 'TGA': 'W', 'GGA': 'G', 'TGG': 'W', 'GGC': 'G', 'TAC': 'Y', 'TTC': 'F', 'TCG': 'S', 'TTA': 'L', 'TTG': 'L', 'TCC': 'S', 'ACC': 'T', 'TAA': '*', 'GCA': 'A', 'GTA': 'V', 'GCC': 'A', 'GTC': 'V', 'GCG': 'A', 'GTG': 'V', 'GAG': 'E', 'GTT': 'V', 'GCT': 'A', 'GAC': 'D', 'CGT': 'R', 'GAA': 'E', 'TCA': 'S', 'ATG': 'M', 'CGC': 'R'}, 'coelenterateMt':{'CTT': 'L', 'TAG': '*', 'ACA': 'T', 'ACG': 'T', 'ATC': 'I', 'AAC': 'N', 'ATA': 'I', 'AGG': 'R', 'CCT': 'P', 'ACT': 'T', 'AGC': 'S', 'AAG': 'K', 'AGA': 'R', 'CAT': 'H', 'AAT': 'N', 'ATT': 'I', 'CTG': 'L', 'CTA': 'L', 'CTC': 'L', 'CAC': 'H', 'AAA': 'K', 'CCG': 'P', 'AGT': 'S', 'CCA': 'P', 'CAA': 'Q', 'CCC': 'P', 'TAT': 'Y', 'GGT': 'G', 'TGT': 'C', 'CGA': 'R', 'CAG': 'Q', 'TCT': 'S', 'GAT': 'D', 'CGG': 'R', 'TTT': 'F', 'TGC': 'C', 'GGG': 'G', 'TGA': 'W', 'GGA': 'G', 'TGG': 'W', 'GGC': 'G', 'TAC': 'Y', 'TTC': 'F', 'TCG': 'S', 'TTA': 'L', 'TTG': 'L', 'TCC': 'S', 'ACC': 'T', 'TAA': '*', 'GCA': 'A', 'GTA': 'V', 'GCC': 'A', 'GTC': 'V', 'GCG': 'A', 'GTG': 'V', 'GAG': 'E', 'GTT': 'V', 'GCT': 'A', 'GAC': 'D', 'CGT': 'R', 'GAA': 'E', 'TCA': 'S', 'ATG': 'M', 'CGC': 'R'},'ciliateNuc':{'CTT': 'L', 'TAG': 'Q', 'ACA': 'T', 'ACG': 'T', 'ATC': 'I', 'AAC': 'N', 'ATA': 'I', 'AGG': 'R', 'CCT': 'P', 'ACT': 'T', 'AGC': 'S', 'AAG': 'K', 'AGA': 'R', 'CAT': 'H', 'AAT': 'N', 'ATT': 'I', 'CTG': 'L', 'CTA': 'L', 'CTC': 'L', 'CAC': 'H', 'AAA': 'K', 'CCG': 'P', 'AGT': 'S', 'CCA': 'P', 'CAA': 'Q', 'CCC': 'P', 'TAT': 'Y', 'GGT': 'G', 'TGT': 'C', 'CGA': 'R', 'CAG': 'Q', 'TCT': 'S', 'GAT': 'D', 'CGG': 'R', 'TTT': 'F', 'TGC': 'C', 'GGG': 'G', 'TGA': '*', 'GGA': 'G', 'TGG': 'W', 'GGC': 'G', 'TAC': 'Y', 'TTC': 'F', 'TCG': 'S', 'TTA': 'L', 'TTG': 'L', 'TCC': 'S', 'ACC': 'T', 'TAA': 'Q', 'GCA': 'A', 'GTA': 'V', 'GCC': 'A', 'GTC': 'V', 'GCG': 'A', 'GTG': 'V', 'GAG': 'E', 'GTT': 'V', 'GCT': 'A', 'GAC': 'D', 'CGT': 'R', 'GAA': 'E', 'TCA': 'S', 'ATG': 'M', 'CGC': 'R'},'echinodermMt':{'CTT': 'L', 'TAG': '*', 'ACA': 'T', 'ACG': 'T', 'ATC': 'I', 'AAC': 'N', 'ATA': 'I', 'AGG': 'S', 'CCT': 'P', 'ACT': 'T', 'AGC': 'S', 'AAG': 'K', 'AGA': 'S', 'CAT': 'H', 'AAT': 'N', 'ATT': 'I', 'CTG': 'L', 'CTA': 'L', 'CTC': 'L', 'CAC': 'H', 'AAA': 'N', 'CCG': 'P', 'AGT': 'S', 'CCA': 'P', 'CAA': 'Q', 'CCC': 'P', 'TAT': 'Y', 'GGT': 'G', 'TGT': 'C', 'CGA': 'R', 'CAG': 'Q', 'TCT': 'S', 'GAT': 'D', 'CGG': 'R', 'TTT': 'F', 'TGC': 'C', 'GGG': 'G', 'TGA': 'W', 'GGA': 'G', 'TGG': 'W', 'GGC': 'G', 'TAC': 'Y', 'TTC': 'F', 'TCG': 'S', 'TTA': 'L', 'TTG': 'L', 'TCC': 'S', 'ACC': 'T', 'TAA': '*', 'GCA': 'A', 'GTA': 'V', 'GCC': 'A', 'GTC': 'V', 'GCG': 'A', 'GTG': 'V', 'GAG': 'E', 'GTT': 'V', 'GCT': 'A', 'GAC': 'D', 'CGT': 'R', 'GAA': 'E', 'TCA': 'S', 'ATG': 'M', 'CGC': 'R'}, 'euplotidNuc':{'CTT': 'L', 'TAG': '*', 'ACA': 'T', 'ACG': 'T', 'ATC': 'I', 'AAC': 'N', 'ATA': 'I', 'AGG': 'R', 'CCT': 'P', 'ACT': 'T', 'AGC': 'S', 'AAG': 'K', 'AGA': 'R', 'CAT': 'H', 'AAT': 'N', 'ATT': 'I', 'CTG': 'L', 'CTA': 'L', 'CTC': 'L', 'CAC': 'H', 'AAA': 'K', 'CCG': 'P', 'AGT': 'S', 'CCA': 'P', 'CAA': 'Q', 'CCC': 'P', 'TAT': 'Y', 'GGT': 'G', 'TGT': 'C', 'CGA': 'R', 'CAG': 'Q', 'TCT': 'S', 'GAT': 'D', 'CGG': 'R', 'TTT': 'F', 'TGC': 'C', 'GGG': 'G', 'TGA': 'C', 'GGA': 'G', 'TGG': 'W', 'GGC': 'G', 'TAC': 'Y', 'TTC': 'F', 'TCG': 'S', 'TTA': 'L', 'TTG': 'L', 'TCC': 'S', 'ACC': 'T', 'TAA': '*', 'GCA': 'A', 'GTA': 'V', 'GCC': 'A', 'GTC': 'V', 'GCG': 'A', 'GTG': 'V', 'GAG': 'E', 'GTT': 'V', 'GCT': 'A', 'GAC': 'D', 'CGT': 'R', 'GAA': 'E', 'TCA': 'S', 'ATG': 'M', 'CGC': 'R'}, 'bacterial':{'CTT': 'L', 'TAG': '*', 'ACA': 'T', 'ACG': 'T', 'ATC': 'I', 'AAC': 'N', 'ATA': 'I', 'AGG': 'R', 'CCT': 'P', 'ACT': 'T', 'AGC': 'S', 'AAG': 'K', 'AGA': 'R', 'CAT': 'H', 'AAT': 'N', 'ATT': 'I', 'CTG': 'L', 'CTA': 'L', 'CTC': 'L', 'CAC': 'H', 'AAA': 'K', 'CCG': 'P', 'AGT': 'S', 'CCA': 'P', 'CAA': 'Q', 'CCC': 'P', 'TAT': 'Y', 'GGT': 'G', 'TGT': 'C', 'CGA': 'R', 'CAG': 'Q', 'TCT': 'S', 'GAT': 'D', 'CGG': 'R', 'TTT': 'F', 'TGC': 'C', 'GGG': 'G', 'TGA': '*', 'GGA': 'G', 'TGG': 'W', 'GGC': 'G', 'TAC': 'Y', 'TTC': 'F', 'TCG': 'S', 'TTA': 'L', 'TTG': 'L', 'TCC': 'S', 'ACC': 'T', 'TAA': '*', 'GCA': 'A', 'GTA': 'V', 'GCC': 'A', 'GTC': 'V', 'GCG': 'A', 'GTG': 'V', 'GAG': 'E', 'GTT': 'V', 'GCT': 'A', 'GAC': 'D', 'CGT': 'R', 'GAA': 'E', 'TCA': 'S', 'ATG': 'M', 'CGC': 'R'},'yeastNuc':{'CTT': 'L', 'TAG': '*', 'ACA': 'T', 'ACG': 'T', 'ATC': 'I', 'AAC': 'N', 'ATA': 'I', 'AGG': 'R', 'CCT': 'P', 'ACT': 'T', 'AGC': 'S', 'AAG': 'K', 'AGA': 'R', 'CAT': 'H', 'AAT': 'N', 'ATT': 'I', 'CTG': 'S', 'CTA': 'L', 'CTC': 'L', 'CAC': 'H', 'AAA': 'K', 'CCG': 'P', 'AGT': 'S', 'CCA': 'P', 'CAA': 'Q', 'CCC': 'P', 'TAT': 'Y', 'GGT': 'G', 'TGT': 'C', 'CGA': 'R', 'CAG': 'Q', 'TCT': 'S', 'GAT': 'D', 'CGG': 'R', 'TTT': 'F', 'TGC': 'C', 'GGG': 'G', 'TGA': '*', 'GGA': 'G', 'TGG': 'W', 'GGC': 'G', 'TAC': 'Y', 'TTC': 'F', 'TCG': 'S', 'TTA': 'L', 'TTG': 'L', 'TCC': 'S', 'ACC': 'T', 'TAA': '*', 'GCA': 'A', 'GTA': 'V', 'GCC': 'A', 'GTC': 'V', 'GCG': 'A', 'GTG': 'V', 'GAG': 'E', 'GTT': 'V', 'GCT': 'A', 'GAC': 'D', 'CGT': 'R', 'GAA': 'E', 'TCA': 'S', 'ATG': 'M', 'CGC': 'R'}, 'ascidianMt':{'CTT': 'L', 'TAG': '*', 'ACA': 'T', 'ACG': 'T', 'ATC': 'I', 'AAC': 'N', 'ATA': 'M', 'AGG': 'G', 'CCT': 'P', 'ACT': 'T', 'AGC': 'S', 'AAG': 'K', 'AGA': 'G', 'CAT': 'H', 'AAT': 'N', 'ATT': 'I', 'CTG': 'L', 'CTA': 'L', 'CTC': 'L', 'CAC': 'H', 'AAA': 'K', 'CCG': 'P', 'AGT': 'S', 'CCA': 'P', 'CAA': 'Q', 'CCC': 'P', 'TAT': 'Y', 'GGT': 'G', 'TGT': 'C', 'CGA': 'R', 'CAG': 'Q', 'TCT': 'S', 'GAT': 'D', 'CGG': 'R', 'TTT': 'F', 'TGC': 'C', 'GGG': 'G', 'TGA': 'W', 'GGA': 'G', 'TGG': 'W', 'GGC': 'G', 'TAC': 'Y', 'TTC': 'F', 'TCG': 'S', 'TTA': 'L', 'TTG': 'L', 'TCC': 'S', 'ACC': 'T', 'TAA': '*', 'GCA': 'A', 'GTA': 'V', 'GCC': 'A', 'GTC': 'V', 'GCG': 'A', 'GTG': 'V', 'GAG': 'E', 'GTT': 'V', 'GCT': 'A', 'GAC': 'D', 'CGT': 'R', 'GAA': 'E', 'TCA': 'S', 'ATG': 'M', 'CGC': 'R'},'flatwormMt':{'CTT': 'L', 'TAG': '*', 'ACA': 'T', 'ACG': 'T', 'ATC': 'I', 'AAC': 'N', 'ATA': 'I', 'AGG': 'S', 'CCT': 'P', 'ACT': 'T', 'AGC': 'S', 'AAG': 'K', 'AGA': 'S', 'CAT': 'H', 'AAT': 'N', 'ATT': 'I', 'CTG': 'L', 'CTA': 'L', 'CTC': 'L', 'CAC': 'H', 'AAA': 'N', 'CCG': 'P', 'AGT': 'S', 'CCA': 'P', 'CAA': 'Q', 'CCC': 'P', 'TAT': 'Y', 'GGT': 'G', 'TGT': 'C', 'CGA': 'R', 'CAG': 'Q', 'TCT': 'S', 'GAT': 'D', 'CGG': 'R', 'TTT': 'F', 'TGC': 'C', 'GGG': 'G', 'TGA': 'W', 'GGA': 'G', 'TGG': 'W', 'GGC': 'G', 'TAC': 'Y', 'TTC': 'F', 'TCG': 'S', 'TTA': 'L', 'TTG': 'L', 'TCC': 'S', 'ACC': 'T', 'TAA': 'Y', 'GCA': 'A', 'GTA': 'V', 'GCC': 'A', 'GTC': 'V', 'GCG': 'A', 'GTG': 'V', 'GAG': 'E', 'GTT': 'V', 'GCT': 'A', 'GAC': 'D', 'CGT': 'R', 'GAA': 'E', 'TCA': 'S', 'ATG': 'M', 'CGC': 'R'},'chlorophyceanMt':{'CTT': 'L', 'TAG': 'L', 'ACA': 'T', 'ACG': 'T', 'ATC': 'I', 'AAC': 'N', 'ATA': 'I', 'AGG': 'R', 'CCT': 'P', 'ACT': 'T', 'AGC': 'S', 'AAG': 'K', 'AGA': 'R', 'CAT': 'H', 'AAT': 'N', 'ATT': 'I', 'CTG': 'L', 'CTA': 'L', 'CTC': 'L', 'CAC': 'H', 'AAA': 'K', 'CCG': 'P', 'AGT': 'S', 'CCA': 'P', 'CAA': 'Q', 'CCC': 'P', 'TAT': 'Y', 'GGT': 'G', 'TGT': 'C', 'CGA': 'R', 'CAG': 'Q', 'TCT': 'S', 'GAT': 'D', 'CGG': 'R', 'TTT': 'F', 'TGC': 'C', 'GGG': 'G', 'TGA': '*', 'GGA': 'G', 'TGG': 'W', 'GGC': 'G', 'TAC': 'Y', 'TTC': 'F', 'TCG': 'S', 'TTA': 'L', 'TTG': 'L', 'TCC': 'S', 'ACC': 'T', 'TAA': '*', 'GCA': 'A', 'GTA': 'V', 'GCC': 'A', 'GTC': 'V', 'GCG': 'A', 'GTG': 'V', 'GAG': 'E', 'GTT': 'V', 'GCT': 'A', 'GAC': 'D', 'CGT': 'R', 'GAA': 'E', 'TCA': 'S', 'ATG': 'M', 'CGC': 'R'},'trematodeMt':{'CTT': 'L', 'TAG': '*', 'ACA': 'T', 'ACG': 'T', 'ATC': 'I', 'AAC': 'N', 'ATA': 'M', 'AGG': 'S', 'CCT': 'P', 'ACT': 'T', 'AGC': 'S', 'AAG': 'K', 'AGA': 'S', 'CAT': 'H', 'AAT': 'N', 'ATT': 'I', 'CTG': 'L', 'CTA': 'L', 'CTC': 'L', 'CAC': 'H', 'AAA': 'N', 'CCG': 'P', 'AGT': 'S', 'CCA': 'P', 'CAA': 'Q', 'CCC': 'P', 'TAT': 'Y', 'GGT': 'G', 'TGT': 'C', 'CGA': 'R', 'CAG': 'Q', 'TCT': 'S', 'GAT': 'D', 'CGG': 'R', 'TTT': 'F', 'TGC': 'C', 'GGG': 'G', 'TGA': 'W', 'GGA': 'G', 'TGG': 'W', 'GGC': 'G', 'TAC': 'Y', 'TTC': 'F', 'TCG': 'S', 'TTA': 'L', 'TTG': 'L', 'TCC': 'S', 'ACC': 'T', 'TAA': '*', 'GCA': 'A', 'GTA': 'V', 'GCC': 'A', 'GTC': 'V', 'GCG': 'A', 'GTG': 'V', 'GAG': 'E', 'GTT': 'V', 'GCT': 'A', 'GAC': 'D', 'CGT': 'R', 'GAA': 'E', 'TCA': 'S', 'ATG': 'M', 'CGC': 'R'},'pterobranchiaMt':{'CTT': 'L', 'TAG': '*', 'ACA': 'T', 'ACG': 'T', 'ATC': 'I', 'AAC': 'N', 'ATA': 'I', 'AGG': 'K', 'CCT': 'P', 'ACT': 'T', 'AGC': 'S', 'AAG': 'K', 'AGA': 'S', 'CAT': 'H', 'AAT': 'N', 'ATT': 'I', 'CTG': 'L', 'CTA': 'L', 'CTC': 'L', 'CAC': 'H', 'AAA': 'K', 'CCG': 'P', 'AGT': 'S', 'CCA': 'P', 'CAA': 'Q', 'CCC': 'P', 'TAT': 'Y', 'GGT': 'G', 'TGT': 'C', 'CGA': 'R', 'CAG': 'Q', 'TCT': 'S', 'GAT': 'D', 'CGG': 'R', 'TTT': 'F', 'TGC': 'C', 'GGG': 'G', 'TGA': 'W', 'GGA': 'G', 'TGG': 'W', 'GGC': 'G', 'TAC': 'Y', 'TTC': 'F', 'TCG': 'S', 'TTA': 'L', 'TTG': 'L', 'TCC': 'S', 'ACC': 'T', 'TAA': '*', 'GCA': 'A', 'GTA': 'V', 'GCC': 'A', 'GTC': 'V', 'GCG': 'A', 'GTG': 'V', 'GAG': 'E', 'GTT': 'V', 'GCT': 'A', 'GAC': 'D', 'CGT': 'R', 'GAA': 'E', 'TCA': 'S', 'ATG': 'M', 'CGC': 'R'}}
    geneticCode = geneticCodes[code]
    startCodons = ['ATT','ATC','ATA','ATG','GTG'] #invertebrateMt code
    positionDict = {(0,1533):'COI',(1533,2217):'COII',(2217,2373):'ATP8',(2373,3066):'ATP6',(3066,4005):'ND1',(4005,4509):'ND6',(4509,5646):'CYTB',(5646,5940):'ND4L',(5940,7314):'ND4',(7314,9030):'ND5',(9030,9807):'COIII',(9807,10158):'ND3',(10158,11214):'ND2'} #{(start,stop):gene}
    seqDict, seqList, codonDict = buildCodonDict(fasta)
    popList = []
    sexList = []
    outList = [] 
    thetaUSDict = {">$Heron2":(3,2598),	">$clone_1":(2,2598),	">$Rotoiti_1_4n":(2,2594.35416672),	">$AC51":(0,2598.33333333),	">$Heron_mitochondrion":(0,2599),	">$Grasmere_6_3n":(0,2599.62500001),	">$Poerua_triploid":(2,2597),	">$Brunner_6_3n":(2,2592.9583334),	">$McGregor":(0,2599),	">$Poerua_72_4n":(0,2605.47916675),	">$Gunn":(4,2597.66666667),	">$Grasmere_1_4n":(1,2628.66666703),	">$clone_7":(0,2592.85416667),	">$DenmarkA":(0,2593.125),	">$Duluth":(0,2591.52083333),	">$Waik_lane4_TCCTGAGC_trimmed_paired_contig_237":(3,2593.79166667),	">$Waik37":(0,2586.58333333),	">$Waik372":(4,2589.25),	">$Tarawera":(0,2586.58333333),	">$Kaniere_triploid":(1,2586.58333333),	">$Waik36":(14,2586.91666667),	">$WalesC":(2,2584.91666667),	">$Brunner_2_4n":(0,2593.60416674),	">$Lady":(9,2598.66666667),	">$Kaniere_1_2n":(9,2598.33333333),	">$Rotoroa_1_2n":(13,2598.58333338),	">$AlexMap":(0,2592.33333333),	">$Alexsex":(0,2592.33333333),	">$Yellow_Contig_56":(0,2592.33333333),	">$Ianthe":(4,2597),	">$Ianthe_lane1_TAAGGCGA_trimmed_paired_contig_309":(4,2595)}
    thetaUmeanCDict = {">$Heron2":(1,4307.57142857),	">$clone_1":(0,4307.80952381),	">$Rotoiti_1_4n":(0,4283.76190474),	">$AC51":(0,4307.04761905),	">$Heron_mitochondrion":(0,4307.04761905),	">$Grasmere_6_3n":(0,4299.99999999),	">$Poerua_triploid":(1,4308.90476191),	">$Brunner_6_3n":(3,4277.5238095),	">$McGregor":(0,4307.14285714),	">$Poerua_72_4n":(0,4263.99999996),	">$Gunn":(1,4308.57142857),	">$Grasmere_1_4n":(1,4132.47619032),	">$clone_7":(0,4310.19047619),	">$DenmarkA":(0,4310.04761905),	">$Duluth":(0,4310.80952381),	">$Waik_lane4_TCCTGAGC_trimmed_paired_contig_237":(0,4308.85714286),	">$Waik37":(0,4311.76190476),	">$Waik372":(4,4314.52380952),	">$Tarawera":(0,4312.28571428),	">$Kaniere_triploid":(0,4312.80952381),	">$Waik36":(6,4313.14285714),	">$WalesC":(3,4315),	">$Brunner_2_4n":(3,4273.47619044),	">$Lady":(5,4307.52380952),	">$Kaniere_1_2n":(2,4308.23809524),	">$Rotoroa_1_2n":(4,4280.80952379),	">$AlexMap":(0,4311),	">$Alexsex":(0,4311),	">$Yellow_Contig_56":(0,4311),	">$Ianthe":(1,4308.52380952),	">$Ianthe_lane1_TAAGGCGA_trimmed_paired_contig_309":(1,4309.19047619)}
    thetaUmeanRDict = {">$Heron2":(0,4308.42857143),	">$clone_1":(0,4308.19047619),	">$Rotoiti_1_4n":(0,4335.88392856),	">$AC51":(1,4308.61904762),	">$Heron_mitochondrion":(0,4307.95238095),	">$Grasmere_6_3n":(1,4314.375),	">$Poerua_triploid":(0,4308.09523809),	">$Brunner_6_3n":(3,4343.51785713),	">$McGregor":(0,4307.85714286),	">$Poerua_72_4n":(0,4344.52083332),	">$Gunn":(3,4307.76190476),	">$Grasmere_1_4n":(1,4452.85714279999),	">$clone_7":(0,4310.95535714),	">$DenmarkA":(0,4310.82738095),	">$Duluth":(1,4311.66964286),	">$Waik_lane4_TCCTGAGC_trimmed_paired_contig_237":(1,4311.35119048),	">$Waik37":(1,4315.65476191),	">$Waik372":(3,4310.22619048),	">$Tarawera":(0,4315.13095238),	">$Kaniere_triploid":(0,4314.60714286),	">$Waik36":(0,4313.94047619),	">$WalesC":(0,4314.08333333),	">$Brunner_2_4n":(3,4346.91964285),	">$Lady":(1,4307.80952381),	">$Kaniere_1_2n":(0,4307.42857143),	">$Rotoroa_1_2n":(1,4334.60714285),	">$AlexMap":(0,4310.66666667),	">$Alexsex":(0,4310.66666667),	">$Yellow_Contig_56":(0,4310.66666667),	">$Ianthe":(0,4308.47619048),	">$Ianthe_lane1_TAAGGCGA_trimmed_paired_contig_309":(2,4309.80952381)}
    thetaUC1Dict = {">$Heron2":(1,6320.33333333),	">$clone_1":(0,6319.66666667),	">$Rotoiti_1_4n":(0,6264.68749995),	">$AC51":(0,6318.66666667),	">$Heron_mitochondrion":(0,6319.33333333),	">$Grasmere_6_3n":(1,6307.62499999),	">$Poerua_triploid":(1,6321.66666667),	">$Brunner_6_3n":(4,6262.95833327),	">$McGregor":(0,6319),	">$Poerua_72_4n":(0,6232.81249992),	">$Gunn":(2,6324.33333333),	">$Grasmere_1_4n":(1,5990.99999963),	">$clone_7":(0,6322.52083333),	">$DenmarkA":(0,6322.45833333),	">$Duluth":(1,6323.85416667),	">$Waik_lane4_TCCTGAGC_trimmed_paired_contig_237":(0,6320.125),	">$Waik37":(0,6327.25),	">$Waik372":(6,6330.58333333),	">$Tarawera":(0,6329.25),	">$Kaniere_triploid":(0,6330.58333333),	">$Waik36":(6,6330.25),	">$WalesC":(3,6333.25),	">$Brunner_2_4n":(4,6259.27083326),	">$Lady":(6,6318),	">$Kaniere_1_2n":(2,6320.33333333),	">$Rotoroa_1_2n":(4,6271.58333329),	">$AlexMap":(0,6326.33333333),	">$Alexsex":(0,6326.33333333),	">$Yellow_Contig_56":(0,6326.33333333),	">$Ianthe":(1,6321.33333333),	">$Ianthe_lane1_TAAGGCGA_trimmed_paired_contig_309":(2,6321)}
    thetaUC2Dict = {">$Heron2":(1,5090.33333333),	">$clone_1":(0,5091.33333333),	">$Rotoiti_1_4n":(0,5085.97916662),	">$AC51":(1,5089.33333333),	">$Heron_mitochondrion":(0,5088.66666667),	">$Grasmere_6_3n":(0,5084.70833332),	">$Poerua_triploid":(1,5092),	">$Brunner_6_3n":(4,5076.37499994),	">$McGregor":(0,5089.66666667),	">$Poerua_72_4n":(0,5059.52083325),	">$Gunn":(2,5090.33333333),	">$Grasmere_1_4n":(2,4999.33333297),	">$clone_7":(0,5092.14583333),	">$DenmarkA":(0,5091.875),	">$Duluth":(0,5093.47916667),	">$Waik_lane4_TCCTGAGC_trimmed_paired_contig_237":(1,5091.20833333),	">$Waik37":(0,5096.75),	">$Waik372":(4,5097.41666667),	">$Tarawera":(0,5097.08333333),	">$Kaniere_triploid":(0,5096.75),	">$Waik36":(3,5100.75),	">$WalesC":(1,5101.75),	">$Brunner_2_4n":(3,5082.39583326),	">$Lady":(4,5089),	">$Kaniere_1_2n":(0,5090),	">$Rotoroa_1_2n":(5,5078.41666662),	">$AlexMap":(0,5097.33333333),	">$Alexsex":(0,5097.33333333),	">$Yellow_Contig_56":(0,5097.33333333),	">$Ianthe":(1,5093),	">$Ianthe_lane1_TAAGGCGA_trimmed_paired_contig_309":(2,5095.33333333)}
    thetaUC3Dict = {">$Heron2":(0,2945),	">$clone_1":(0,2944.66666667),	">$Rotoiti_1_4n":(0,2932.12499995),	">$AC51":(0,2945),	">$Heron_mitochondrion":(0,2944.66666667),	">$Grasmere_6_3n":(0,2941.74999999),	">$Poerua_triploid":(1,2945.66666667),	">$Brunner_6_3n":(2,2925.4166666),	">$McGregor":(0,2945),	">$Poerua_72_4n":(0,2926.20833325),	">$Gunn":(1,2944),	">$Grasmere_1_4n":(0,2832.33333297),	">$clone_7":(0,2949.79166667),	">$DenmarkA":(0,2949.75),	">$Duluth":(0,2949.125),	">$Waik_lane4_TCCTGAGC_trimmed_paired_contig_237":(0,2948.75),	">$Waik37":(0,2950.5),	">$Waik372":(1,2952.83333333),	">$Tarawera":(0,2950.5),	">$Kaniere_triploid":(0,2950.83333333),	">$Waik36":(6,2947.16666667),	">$WalesC":(3,2950.83333333),	">$Brunner_2_4n":(3,2917.29166659),	">$Lady":(4,2947.33333333),	">$Kaniere_1_2n":(2,2945.66666667),	">$Rotoroa_1_2n":(1,2928.16666662),	">$AlexMap":(0,2946.66666667),	">$Alexsex":(0,2946.66666667),	">$Yellow_Contig_56":(0,2946.66666667),	">$Ianthe":(1,2945.33333333),	">$Ianthe_lane1_TAAGGCGA_trimmed_paired_contig_309":(1,2945.33333333)}
    thetaUC4Dict = {">$Heron2":(0,3419.66666667),	">$clone_1":(0,3419.33333333),	">$Rotoiti_1_4n":(0,3422.85416662),	">$AC51":(0,3419),	">$Heron_mitochondrion":(0,3419),	">$Grasmere_6_3n":(0,3416.95833332),	">$Poerua_triploid":(1,3421),	">$Brunner_6_3n":(3,3421.95833327),	">$McGregor":(0,3420),	">$Poerua_72_4n":(0,3422.97916658),	">$Gunn":(2,3420),	">$Grasmere_1_4n":(0,3382.99999963),	">$clone_7":(0,3422.6875),	">$DenmarkA":(0,3422.45833333),	">$Duluth":(0,3422.02083333),	">$Waik_lane4_TCCTGAGC_trimmed_paired_contig_237":(0,3421.79166667),	">$Waik37":(0,3424.58333333),	">$Waik372":(0,3428.25),	">$Tarawera":(0,3424.91666667),	">$Kaniere_triploid":(0,3423.58333333),	">$Waik36":(6,3420.25),	">$WalesC":(3,3423.25),	">$Brunner_2_4n":(3,3405.10416659),	">$Lady":(4,3423),	">$Kaniere_1_2n":(2,3420.33333333),	">$Rotoroa_1_2n":(1,3414.91666662),	">$AlexMap":(0,3420.66666667),	">$Alexsex":(0,3420.66666667),	">$Yellow_Contig_56":(0,3420.66666667),	">$Ianthe":(1,3419.33333333),	">$Ianthe_lane1_TAAGGCGA_trimmed_paired_contig_309":(1,3420)}
    thetaUC5Dict = {">$Heron2":(0,4382.33333333),	">$clone_1":(0,4382.33333333),	">$Rotoiti_1_4n":(0,4363.35416667),	">$AC51":(0,4382),	">$Heron_mitochondrion":(0,4382.33333333),	">$Grasmere_6_3n":(1,4375.95833333),	">$Poerua_triploid":(1,4383.33333333),	">$Brunner_6_3n":(4,4354.95833333),	">$McGregor":(0,4382),	">$Poerua_72_4n":(0,4354.14583333),	">$Gunn":(2,4382.66666667),	">$Grasmere_1_4n":(0,4238),	">$clone_7":(0,4385.1875),	">$DenmarkA":(0,4385.125),	">$Duluth":(1,4384.85416667),	">$Waik_lane4_TCCTGAGC_trimmed_paired_contig_237":(0,4383.79166667),	">$Waik37":(0,4385.58333333),	">$Waik372":(2,4390.58333333),	">$Tarawera":(0,4385.58333333),	">$Kaniere_triploid":(0,4386.25),	">$Waik36":(6,4383.58333333),	">$WalesC":(3,4385.58333333),	">$Brunner_2_4n":(4,4338.9375),	">$Lady":(6,4385.33333333),	">$Kaniere_1_2n":(2,4383.33333333),	">$Rotoroa_1_2n":(2,4354.91666667),	">$AlexMap":(0,4381.66666667),	">$Alexsex":(0,4381.66666667),	">$Yellow_Contig_56":(0,4381.66666667),	">$Ianthe":(1,4384.66666667),	">$Ianthe_lane1_TAAGGCGA_trimmed_paired_contig_309":(2,4384)}
    thetaUC6Dict = {">$Heron2":(1,4124.66666667),	">$clone_1":(0,4125.66666667),	">$Rotoiti_1_4n":(0,4084.39583338),	">$AC51":(0,4124.66666667),	">$Heron_mitochondrion":(0,4125),	">$Grasmere_6_3n":(0,4112.54166668),	">$Poerua_triploid":(1,4126),	">$Brunner_6_3n":(3,4075.2083334),	">$McGregor":(0,4124.33333333),	">$Poerua_72_4n":(0,4050.43750008),	">$Gunn":(0,4126.33333333),	">$Grasmere_1_4n":(1,3848.3333337),	">$clone_7":(0,4126.89583333),	">$DenmarkA":(0,4127.04166667),	">$Duluth":(0,4128.5625),	">$Waik_lane4_TCCTGAGC_trimmed_paired_contig_237":(0,4126.04166667),	">$Waik37":(0,4123.41666667),	">$Waik372":(5,4126.08333333),	">$Tarawera":(0,4124.08333333),	">$Kaniere_triploid":(0,4125.75),	">$Waik36":(3,4130.08333333),	">$WalesC":(1,4129.75),	">$Brunner_2_4n":(3,4078.47916674),	">$Lady":(5,4121),	">$Kaniere_1_2n":(0,4126.33333333),	">$Rotoroa_1_2n":(4,4085.08333338),	">$AlexMap":(0,4127.33333333),	">$Alexsex":(0,4127.33333333),	">$Yellow_Contig_56":(0,4127.33333333),	">$Ianthe":(1,4123.66666667),	">$Ianthe_lane1_TAAGGCGA_trimmed_paired_contig_309":(1,4125)}
    thetaUC7Dict = {">$Heron2":(1,3870.66666667),	">$clone_1":(0,3871.66666667),	">$Rotoiti_1_4n":(0,3832.9375),	">$AC51":(0,3870.66666667),	">$Heron_mitochondrion":(0,3870.33333333),	">$Grasmere_6_3n":(0,3860.45833333),	">$Poerua_triploid":(1,3872.66666667),	">$Brunner_6_3n":(3,3825.79166667),	">$McGregor":(0,3870),	">$Poerua_72_4n":(0,3801.89583333),	">$Gunn":(0,3872.33333333),	">$Grasmere_1_4n":(1,3635.33333333),	">$clone_7":(0,3872.10416667),	">$DenmarkA":(0,3871.625),	">$Duluth":(0,3873.77083333),	">$Waik_lane4_TCCTGAGC_trimmed_paired_contig_237":(0,3870.29166667),	">$Waik37":(0,3874.25),	">$Waik372":(4,3875.91666667),	">$Tarawera":(0,3874.58333333),	">$Kaniere_triploid":(0,3875.91666667),	">$Waik36":(3,3879.91666667),	">$WalesC":(1,3880.58333333),	">$Brunner_2_4n":(3,3832.85416667),	">$Lady":(4,3869),	">$Kaniere_1_2n":(0,3871.66666667),	">$Rotoroa_1_2n":(4,3832.58333333),	">$AlexMap":(0,3877),	">$Alexsex":(0,3877),	">$Yellow_Contig_56":(0,3877),	">$Ianthe":(1,3872.33333333),	">$Ianthe_lane1_TAAGGCGA_trimmed_paired_contig_309":(1,3873.66666667)}
    thetaUR1Dict = {">$Heron2":(0,2295.66666667),	">$clone_1":(0,2296.33333333),	">$Rotoiti_1_4n":(0,2354.95833333),	">$AC51":(1,2297),	">$Heron_mitochondrion":(0,2295.66666667),	">$Grasmere_6_3n":(0,2306.75),	">$Poerua_triploid":(0,2295.33333333),	">$Brunner_6_3n":(2,2358.08333333),	">$McGregor":(0,2296),	">$Poerua_72_4n":(0,2375.70833333),	">$Gunn":(2,2292),	">$Grasmere_1_4n":(1,2594.33333333),	">$clone_7":(0,2298.625),	">$DenmarkA":(0,2298.41666667),	">$Duluth":(0,2298.625),	">$Waik_lane4_TCCTGAGC_trimmed_paired_contig_237":(1,2300.08333333),	">$Waik37":(1,2300.16666667),	">$Waik372":(1,2294.16666667),	">$Tarawera":(0,2298.16666667),	">$Kaniere_triploid":(0,2296.83333333),	">$Waik36":(0,2296.83333333),	">$WalesC":(0,2295.83333333),	">$Brunner_2_4n":(2,2361.125),	">$Lady":(0,2297.33333333),	">$Kaniere_1_2n":(0,2295.33333333),	">$Rotoroa_1_2n":(1,2343.83333333),	">$AlexMap":(0,2295.33333333),	">$Alexsex":(0,2295.33333333),	">$Yellow_Contig_56":(0,2295.33333333),	">$Ianthe":(0,2295.66666667),	">$Ianthe_lane1_TAAGGCGA_trimmed_paired_contig_309":(1,2298)}
    thetaUR2Dict = {">$Heron2":(0,3525.66666667),	">$clone_1":(0,3524.66666667),	">$Rotoiti_1_4n":(0,3533.66666667),	">$AC51":(0,3526.33333333),	">$Heron_mitochondrion":(0,3526.33333333),	">$Grasmere_6_3n":(1,3529.66666667),	">$Poerua_triploid":(0,3525),	">$Brunner_6_3n":(2,3544.66666667),	">$McGregor":(0,3525.33333333),	">$Poerua_72_4n":(0,3549),	">$Gunn":(2,3526),	">$Grasmere_1_4n":(0,3586),	">$clone_7":(0,3529),	">$DenmarkA":(0,3529),	">$Duluth":(1,3529),	">$Waik_lane4_TCCTGAGC_trimmed_paired_contig_237":(0,3529),	">$Waik37":(1,3530.66666667),	">$Waik372":(3,3527.33333333),	">$Tarawera":(0,3530.33333333),	">$Kaniere_triploid":(0,3530.66666667),	">$Waik36":(3,3526.33333333),	">$WalesC":(2,3527.33333333),	">$Brunner_2_4n":(3,3538),	">$Lady":(2,3526.33333333),	">$Kaniere_1_2n":(2,3525.66666667),	">$Rotoroa_1_2n":(0,3537),	">$AlexMap":(0,3524.33333333),	">$Alexsex":(0,3524.33333333),	">$Yellow_Contig_56":(0,3524.33333333),	">$Ianthe":(0,3524),	">$Ianthe_lane1_TAAGGCGA_trimmed_paired_contig_309":(1,3523.66666667)}
    thetaUR3Dict = {">$Heron2":(1,5671),	">$clone_1":(0,5671.33333333),	">$Rotoiti_1_4n":(0,5687.52083333),	">$AC51":(1,5670.66666667),	">$Heron_mitochondrion":(0,5670.33333333),	">$Grasmere_6_3n":(1,5672.625),	">$Poerua_triploid":(0,5671.33333333),	">$Brunner_6_3n":(4,5695.625),	">$McGregor":(0,5670),	">$Poerua_72_4n":(0,5682.3125),	">$Gunn":(3,5672.33333333),	">$Grasmere_1_4n":(2,5753),	">$clone_7":(0,5671.35416667),	">$DenmarkA":(0,5671.125),	">$Duluth":(1,5673.35416667),	">$Waik_lane4_TCCTGAGC_trimmed_paired_contig_237":(1,5671.45833333),	">$Waik37":(1,5676.91666667),	">$Waik372":(6,5671.91666667),	">$Tarawera":(0,5676.91666667),	">$Kaniere_triploid":(0,5676.58333333),	">$Waik36":(0,5679.91666667),	">$WalesC":(0,5678.25),	">$Brunner_2_4n":(3,5703.10416667),	">$Lady":(2,5668),	">$Kaniere_1_2n":(0,5670),	">$Rotoroa_1_2n":(4,5687.25),	">$AlexMap":(0,5675),	">$Alexsex":(0,5675),	">$Yellow_Contig_56":(0,5675),	">$Ianthe":(0,5671.66666667),	">$Ianthe_lane1_TAAGGCGA_trimmed_paired_contig_309":(2,5673.66666667)}
    thetaUR4Dict = {">$Heron2":(1,5196.33333333),	">$clone_1":(0,5196.66666667),	">$Rotoiti_1_4n":(0,5196.79166667),	">$AC51":(1,5196.66666667),	">$Heron_mitochondrion":(0,5196),	">$Grasmere_6_3n":(1,5197.41666667),	">$Poerua_triploid":(0,5196),	">$Brunner_6_3n":(3,5199.08333333),	">$McGregor":(0,5195),	">$Poerua_72_4n":(0,5185.54166667),	">$Gunn":(2,5196.33333333),	">$Grasmere_1_4n":(2,5202.33333333),	">$clone_7":(0,5198.45833333),	">$DenmarkA":(0,5198.41666667),	">$Duluth":(1,5200.45833333),	">$Waik_lane4_TCCTGAGC_trimmed_paired_contig_237":(1,5198.41666667),	">$Waik37":(1,5202.83333333),	">$Waik372":(7,5196.5),	">$Tarawera":(0,5202.5),	">$Kaniere_triploid":(0,5203.83333333),	">$Waik36":(0,5206.83333333),	">$WalesC":(0,5205.83333333),	">$Brunner_2_4n":(3,5215.29166667),	">$Lady":(2,5192.33333333),	">$Kaniere_1_2n":(0,5195.33333333),	">$Rotoroa_1_2n":(4,5200.5),	">$AlexMap":(0,5201),	">$Alexsex":(0,5201),	">$Yellow_Contig_56":(0,5201),	">$Ianthe":(0,5197.66666667),	">$Ianthe_lane1_TAAGGCGA_trimmed_paired_contig_309":(2,5199)}
    thetaUR5Dict = {">$Heron2":(1,4233.66666667),	">$clone_1":(0,4233.66666667),	">$Rotoiti_1_4n":(0,4256.29166662),	">$AC51":(1,4233.66666667),	">$Heron_mitochondrion":(0,4232.66666667),	">$Grasmere_6_3n":(0,4238.41666665),	">$Poerua_triploid":(0,4233.66666667),	">$Brunner_6_3n":(2,4266.08333327),	">$McGregor":(0,4233),	">$Poerua_72_4n":(0,4254.37499992),	">$Gunn":(2,4233.66666667),	">$Grasmere_1_4n":(2,4347.33333297),	">$clone_7":(0,4235.95833333),	">$DenmarkA":(0,4235.75),	">$Duluth":(0,4237.625),	">$Waik_lane4_TCCTGAGC_trimmed_paired_contig_237":(1,4236.41666667),	">$Waik37":(1,4241.83333333),	">$Waik372":(5,4234.16666667),	">$Tarawera":(0,4241.83333333),	">$Kaniere_triploid":(0,4241.16666667),	">$Waik36":(0,4243.5),	">$WalesC":(0,4243.5),	">$Brunner_2_4n":(2,4281.45833326),	">$Lady":(0,4230),	">$Kaniere_1_2n":(0,4232.33333333),	">$Rotoroa_1_2n":(3,4260.49999996),	">$AlexMap":(0,4240),	">$Alexsex":(0,4240),	">$Yellow_Contig_56":(0,4240),	">$Ianthe":(0,4232.33333333),	">$Ianthe_lane1_TAAGGCGA_trimmed_paired_contig_309":(1,4235)}
    thetaUR6Dict = {">$Heron2":(0,4491.33333333),	">$clone_1":(0,4490.33333333),	">$Rotoiti_1_4n":(0,4535.25000005),	">$AC51":(1,4491),	">$Heron_mitochondrion":(0,4490),	">$Grasmere_6_3n":(1,4501.83333335),	">$Poerua_triploid":(0,4491),	">$Brunner_6_3n":(3,4545.8333334),	">$McGregor":(0,4490.66666667),	">$Poerua_72_4n":(0,4558.08333342),	">$Gunn":(4,4490),	">$Grasmere_1_4n":(1,4737.00000037),	">$clone_7":(0,4494.25),	">$DenmarkA":(0,4493.83333333),	">$Duluth":(1,4493.91666667),	">$Waik_lane4_TCCTGAGC_trimmed_paired_contig_237":(1,4494.16666667),	">$Waik37":(1,4504),	">$Waik372":(2,4498.66666667),	">$Tarawera":(0,4503.33333333),	">$Kaniere_triploid":(0,4501.66666667),	">$Waik36":(3,4497),	">$WalesC":(2,4499.33333333),	">$Brunner_2_4n":(3,4541.91666674),	">$Lady":(1,4494.33333333),	">$Kaniere_1_2n":(2,4489.33333333),	">$Rotoroa_1_2n":(1,4530.33333338),	">$AlexMap":(0,4494.33333333),	">$Alexsex":(0,4494.33333333),	">$Yellow_Contig_56":(0,4494.33333333),	">$Ianthe":(0,4493.33333333),	">$Ianthe_lane1_TAAGGCGA_trimmed_paired_contig_309":(2,4494)}
    thetaUR7Dict = {">$Heron2":(0,4745.33333333),	">$clone_1":(0,4744.33333333),	">$Rotoiti_1_4n":(0,4786.70833328),	">$AC51":(1,4745),	">$Heron_mitochondrion":(0,4744.66666667),	">$Grasmere_6_3n":(1,4753.91666665),	">$Poerua_triploid":(0,4744.33333333),	">$Brunner_6_3n":(3,4795.24999994),	">$McGregor":(0,4745),	">$Poerua_72_4n":(0,4806.62499992),	">$Gunn":(4,4744),	">$Grasmere_1_4n":(1,4949.99999963),	">$clone_7":(0,4749.04166667),	">$DenmarkA":(0,4749.25),	">$Duluth":(1,4748.70833333),	">$Waik_lane4_TCCTGAGC_trimmed_paired_contig_237":(1,4749.91666667),	">$Waik37":(1,4753.16666667),	">$Waik372":(3,4748.83333333),	">$Tarawera":(0,4752.83333333),	">$Kaniere_triploid":(0,4751.5),	">$Waik36":(3,4747.16666667),	">$WalesC":(2,4748.5),	">$Brunner_2_4n":(3,4787.54166659),	">$Lady":(2,4746.33333333),	">$Kaniere_1_2n":(2,4744),	">$Rotoroa_1_2n":(1,4782.83333329),	">$AlexMap":(0,4744.66666667),	">$Alexsex":(0,4744.66666667),	">$Yellow_Contig_56":(0,4744.66666667),	">$Ianthe":(0,4744.66666667),	">$Ianthe_lane1_TAAGGCGA_trimmed_paired_contig_309":(2,4745.33333333)}
    D1 = {'mean':[],1:[],2:[],3:[],4:[],5:[],6:[],7:[]}#thetaU-C/thetaU-S
    D2 = {'mean':[],1:[],2:[],3:[],4:[],5:[],6:[],7:[]}#thetaU-R/thetaU-S
    logfile = open('mt_nullDistribution_thetaU.log','w')
    for seq in seqList:
        if '$' in seq:
            popList.append(seq)
        else:
            outList.append(seq)
    seqNums = range(len(popList))
    currPCT = 0
    sexN = 8
    asexN = 23
    sexAn = aN(sexN)
    asexAn = aN(asexN)
    logfile.write('Calculating population genetic parameters:\n')
    logfile.close()
    while len(D1['mean']) < 10000:
        newPCT = int(round(100*len(D1['mean'])/10000.0))
        if newPCT > currPCT:
            logfile = open('mt_nullDistribution_thetaU.log','a')
            logfile.write('\t' + str(newPCT) + '% complete\n')
            logfile.close()
            currPCT = newPCT
        sexList = []
        asexList = []
        while len(sexList) < sexN:
            currNum = random.choice(seqNums)
            if popList[currNum] not in sexList:
                sexList.append(popList[currNum])
        while len(asexList) < asexN:
            currNum = random.choice(seqNums)
            if popList[currNum] not in asexList and popList[currNum] not in sexList:
                asexList.append(popList[currNum])
        asexSS = 0
        asexMeanCS = 0
        asexMeanRS = 0
        asexC1S = 0
        asexC2S = 0
        asexC3S = 0
        asexC4S = 0
        asexC5S = 0
        asexC6S = 0
        asexC7S = 0
        asexR1S = 0
        asexR2S = 0
        asexR3S = 0
        asexR4S = 0
        asexR5S = 0
        asexR6S = 0
        asexR7S = 0
        sexSS = 0
        sexMeanCS = 0
        sexMeanRS = 0
        sexC1S = 0
        sexC2S = 0
        sexC3S = 0
        sexC4S = 0
        sexC5S = 0
        sexC6S = 0
        sexC7S = 0
        sexR1S = 0
        sexR2S = 0
        sexR3S = 0
        sexR4S = 0
        sexR5S = 0
        sexR6S = 0
        sexR7S = 0
        asexSynSites = 0
        asexMeanCSites = 0
        asexMeanRSites = 0
        asexC1Sites = 0
        asexC2Sites = 0
        asexC3Sites = 0
        asexC4Sites = 0
        asexC5Sites = 0
        asexC6Sites = 0
        asexC7Sites = 0
        asexR1Sites = 0
        asexR2Sites = 0
        asexR3Sites = 0
        asexR4Sites = 0
        asexR5Sites = 0
        asexR6Sites = 0
        asexR7Sites = 0
        sexSynSites = 0
        sexMeanCSites = 0
        sexMeanRSites = 0
        sexC1Sites = 0
        sexC2Sites = 0
        sexC3Sites = 0
        sexC4Sites = 0
        sexC5Sites = 0
        sexC6Sites = 0
        sexC7Sites = 0
        sexR1Sites = 0
        sexR2Sites = 0
        sexR3Sites = 0
        sexR4Sites = 0
        sexR5Sites = 0
        sexR6Sites = 0
        sexR7Sites = 0
        for asexual in asexList:
            currSynValues = thetaUSDict[asexual]
            asexSS += currSynValues[0]
            asexSynSites += currSynValues[1]
            currMeanCValues = thetaUmeanCDict[asexual]
            asexMeanCS += currMeanCValues[0]
            asexMeanCSites += currMeanCValues[1]
            currMeanRValues = thetaUmeanRDict[asexual]
            asexMeanRS += currMeanRValues[0]
            asexMeanRSites += currMeanRValues[1]
            currC1Values = thetaUC1Dict[asexual]
            asexC1S += currC1Values[0]
            asexC1Sites += currC1Values[1]
            currC2Values = thetaUC2Dict[asexual]
            asexC2S += currC2Values[0]
            asexC2Sites += currC2Values[1]
            currC3Values = thetaUC3Dict[asexual]
            asexC3S += currC3Values[0]
            asexC3Sites += currC3Values[1]
            currC4Values = thetaUC4Dict[asexual]
            asexC4S += currC4Values[0]
            asexC4Sites += currC4Values[1]
            currC5Values = thetaUC5Dict[asexual]
            asexC5S += currC5Values[0]
            asexC5Sites += currC5Values[1]
            currC6Values = thetaUC6Dict[asexual]
            asexC6S += currC6Values[0]
            asexC6Sites += currC6Values[1]
            currC7Values = thetaUC7Dict[asexual]
            asexC7S += currC7Values[0]
            asexC7Sites += currC7Values[1]
            currR1Values = thetaUR1Dict[asexual]
            asexR1S += currR1Values[0]
            asexR1Sites += currR1Values[1]
            currR2Values = thetaUR2Dict[asexual]
            asexR2S += currR2Values[0]
            asexR2Sites += currR2Values[1]
            currR3Values = thetaUR3Dict[asexual]
            asexR3S += currR3Values[0]
            asexR3Sites += currR3Values[1]
            currR4Values = thetaUR4Dict[asexual]
            asexR4S += currR4Values[0]
            asexR4Sites += currR4Values[1]
            currR5Values = thetaUR5Dict[asexual]
            asexR5S += currR5Values[0]
            asexR5Sites += currR5Values[1]
            currR6Values = thetaUR6Dict[asexual]
            asexR6S += currR6Values[0]
            asexR6Sites += currR6Values[1]
            currR7Values = thetaUR7Dict[asexual]
            asexR7S += currR7Values[0]
            asexR7Sites += currR7Values[1]
        for sexual in sexList:
            currSynValues = thetaUSDict[sexual]
            sexSS += currSynValues[0]
            sexSynSites += currSynValues[1]
            currMeanCValues = thetaUmeanCDict[sexual]
            sexMeanCS += currMeanCValues[0]
            sexMeanCSites += currMeanCValues[1]
            currMeanRValues = thetaUmeanRDict[sexual]
            sexMeanRS += currMeanRValues[0]
            sexMeanRSites += currMeanRValues[1]
            currC1Values = thetaUC1Dict[sexual]
            sexC1S += currC1Values[0]
            sexC1Sites += currC1Values[1]
            currC2Values = thetaUC2Dict[sexual]
            sexC2S += currC2Values[0]
            sexC2Sites += currC2Values[1]
            currC3Values = thetaUC3Dict[sexual]
            sexC3S += currC3Values[0]
            sexC3Sites += currC3Values[1]
            currC4Values = thetaUC4Dict[sexual]
            sexC4S += currC4Values[0]
            sexC4Sites += currC4Values[1]
            currC5Values = thetaUC5Dict[sexual]
            sexC5S += currC5Values[0]
            sexC5Sites += currC5Values[1]
            currC6Values = thetaUC6Dict[sexual]
            sexC6S += currC6Values[0]
            sexC6Sites += currC6Values[1]
            currC7Values = thetaUC7Dict[sexual]
            sexC7S += currC7Values[0]
            sexC7Sites += currC7Values[1]
            currR1Values = thetaUR1Dict[sexual]
            sexR1S += currR1Values[0]
            sexR1Sites += currR1Values[1]
            currR2Values = thetaUR2Dict[sexual]
            sexR2S += currR2Values[0]
            sexR2Sites += currR2Values[1]
            currR3Values = thetaUR3Dict[sexual]
            sexR3S += currR3Values[0]
            sexR3Sites += currR3Values[1]
            currR4Values = thetaUR4Dict[sexual]
            sexR4S += currR4Values[0]
            sexR4Sites += currR4Values[1]
            currR5Values = thetaUR5Dict[sexual]
            sexR5S += currR5Values[0]
            sexR5Sites += currR5Values[1]
            currR6Values = thetaUR6Dict[sexual]
            sexR6S += currR6Values[0]
            sexR6Sites += currR6Values[1]
            currR7Values = thetaUR7Dict[sexual]
            sexR7S += currR7Values[0]
            sexR7Sites += currR7Values[1]
        asexThetaUS = float(asexSS)/(asexAn*(float(asexSynSites)/len(asexList)))
        asexThetaUMeanC = float(asexMeanCS)/(asexAn*(float(asexMeanCSites)/len(asexList)))
        asexThetaUMeanR = float(asexMeanRS)/(asexAn*(float(asexMeanRSites)/len(asexList)))
        asexThetaUC1 = float(asexC1S)/(asexAn*(float(asexC1Sites)/len(asexList)))
        asexThetaUC2 = float(asexC2S)/(asexAn*(float(asexC2Sites)/len(asexList)))
        asexThetaUC3 = float(asexC3S)/(asexAn*(float(asexC3Sites)/len(asexList)))
        asexThetaUC4 = float(asexC4S)/(asexAn*(float(asexC4Sites)/len(asexList)))
        asexThetaUC5 = float(asexC5S)/(asexAn*(float(asexC5Sites)/len(asexList)))
        asexThetaUC6 = float(asexC6S)/(asexAn*(float(asexC6Sites)/len(asexList)))
        asexThetaUC7 = float(asexC7S)/(asexAn*(float(asexC7Sites)/len(asexList)))
        asexThetaUR1 = float(asexR1S)/(asexAn*(float(asexR1Sites)/len(asexList)))
        asexThetaUR2 = float(asexR2S)/(asexAn*(float(asexR2Sites)/len(asexList)))
        asexThetaUR3 = float(asexR3S)/(asexAn*(float(asexR3Sites)/len(asexList)))
        asexThetaUR4 = float(asexR4S)/(asexAn*(float(asexR4Sites)/len(asexList)))
        asexThetaUR5 = float(asexR5S)/(asexAn*(float(asexR5Sites)/len(asexList)))
        asexThetaUR6 = float(asexR6S)/(asexAn*(float(asexR6Sites)/len(asexList)))
        asexThetaUR7 = float(asexR7S)/(asexAn*(float(asexR7Sites)/len(asexList)))
        sexThetaUS = float(sexSS)/(sexAn*(float(sexSynSites)/len(sexList)))
        sexThetaUMeanC = float(sexMeanCS)/(sexAn*(float(sexMeanCSites)/len(sexList)))
        sexThetaUMeanR = float(sexMeanRS)/(sexAn*(float(sexMeanRSites)/len(sexList)))
        sexThetaUC1 = float(sexC1S)/(sexAn*(float(sexC1Sites)/len(sexList)))
        sexThetaUC2 = float(sexC2S)/(sexAn*(float(sexC2Sites)/len(sexList)))
        sexThetaUC3 = float(sexC3S)/(sexAn*(float(sexC3Sites)/len(sexList)))
        sexThetaUC4 = float(sexC4S)/(sexAn*(float(sexC4Sites)/len(sexList)))
        sexThetaUC5 = float(sexC5S)/(sexAn*(float(sexC5Sites)/len(sexList)))
        sexThetaUC6 = float(sexC6S)/(sexAn*(float(sexC6Sites)/len(sexList)))
        sexThetaUC7 = float(sexC7S)/(sexAn*(float(sexC7Sites)/len(sexList)))
        sexThetaUR1 = float(sexR1S)/(sexAn*(float(sexR1Sites)/len(sexList)))
        sexThetaUR2 = float(sexR2S)/(sexAn*(float(sexR2Sites)/len(sexList)))
        sexThetaUR3 = float(sexR3S)/(sexAn*(float(sexR3Sites)/len(sexList)))
        sexThetaUR4 = float(sexR4S)/(sexAn*(float(sexR4Sites)/len(sexList)))
        sexThetaUR5 = float(sexR5S)/(sexAn*(float(sexR5Sites)/len(sexList)))
        sexThetaUR6 = float(sexR6S)/(sexAn*(float(sexR6Sites)/len(sexList)))
        sexThetaUR7 = float(sexR7S)/(sexAn*(float(sexR7Sites)/len(sexList)))
        if asexThetaUS != 0 and sexThetaUS != 0:
            asexThetaUMeanC_thetaUS = asexThetaUMeanC/asexThetaUS
            asexThetaUMeanR_thetaUS = asexThetaUMeanR/asexThetaUS
            asexThetaUC1_thetaUS = asexThetaUC1/asexThetaUS
            asexThetaUC2_thetaUS = asexThetaUC2/asexThetaUS
            asexThetaUC3_thetaUS = asexThetaUC3/asexThetaUS
            asexThetaUC4_thetaUS = asexThetaUC4/asexThetaUS
            asexThetaUC5_thetaUS = asexThetaUC5/asexThetaUS
            asexThetaUC6_thetaUS = asexThetaUC6/asexThetaUS
            asexThetaUC7_thetaUS = asexThetaUC7/asexThetaUS
            asexThetaUR1_thetaUS = asexThetaUR1/asexThetaUS
            asexThetaUR2_thetaUS = asexThetaUR2/asexThetaUS
            asexThetaUR3_thetaUS = asexThetaUR3/asexThetaUS
            asexThetaUR4_thetaUS = asexThetaUR4/asexThetaUS
            asexThetaUR5_thetaUS = asexThetaUR5/asexThetaUS
            asexThetaUR6_thetaUS = asexThetaUR6/asexThetaUS
            asexThetaUR7_thetaUS = asexThetaUR7/asexThetaUS
            sexThetaUMeanC_thetaUS = sexThetaUMeanC/sexThetaUS
            sexThetaUMeanR_thetaUS = sexThetaUMeanR/sexThetaUS
            sexThetaUC1_thetaUS = sexThetaUC1/sexThetaUS
            sexThetaUC2_thetaUS = sexThetaUC2/sexThetaUS
            sexThetaUC3_thetaUS = sexThetaUC3/sexThetaUS
            sexThetaUC4_thetaUS = sexThetaUC4/sexThetaUS
            sexThetaUC5_thetaUS = sexThetaUC5/sexThetaUS
            sexThetaUC6_thetaUS = sexThetaUC6/sexThetaUS
            sexThetaUC7_thetaUS = sexThetaUC7/sexThetaUS
            sexThetaUR1_thetaUS = sexThetaUR1/sexThetaUS
            sexThetaUR2_thetaUS = sexThetaUR2/sexThetaUS
            sexThetaUR3_thetaUS = sexThetaUR3/sexThetaUS
            sexThetaUR4_thetaUS = sexThetaUR4/sexThetaUS
            sexThetaUR5_thetaUS = sexThetaUR5/sexThetaUS
            sexThetaUR6_thetaUS = sexThetaUR6/sexThetaUS
            sexThetaUR7_thetaUS = sexThetaUR7/sexThetaUS
            D1_mean = asexThetaUMeanC_thetaUS - sexThetaUMeanC_thetaUS
            D1_1 = asexThetaUC1_thetaUS - sexThetaUC1_thetaUS
            D1_2 = asexThetaUC2_thetaUS - sexThetaUC2_thetaUS
            D1_3 = asexThetaUC3_thetaUS - sexThetaUC3_thetaUS
            D1_4 = asexThetaUC4_thetaUS - sexThetaUC4_thetaUS
            D1_5 = asexThetaUC5_thetaUS - sexThetaUC5_thetaUS
            D1_6 = asexThetaUC6_thetaUS - sexThetaUC6_thetaUS
            D1_7 = asexThetaUC7_thetaUS - sexThetaUC7_thetaUS
            D2_mean = asexThetaUMeanR_thetaUS - sexThetaUMeanR_thetaUS
            D2_1 = asexThetaUR1_thetaUS - sexThetaUR1_thetaUS
            D2_2 = asexThetaUR2_thetaUS - sexThetaUR2_thetaUS
            D2_3 = asexThetaUR3_thetaUS - sexThetaUR3_thetaUS
            D2_4 = asexThetaUR4_thetaUS - sexThetaUR4_thetaUS
            D2_5 = asexThetaUR5_thetaUS - sexThetaUR5_thetaUS
            D2_6 = asexThetaUR6_thetaUS - sexThetaUR6_thetaUS
            D2_7 = asexThetaUR7_thetaUS - sexThetaUR7_thetaUS
            currD1_Mean = D1['mean']
            currD1_1 = D1[1]
            currD1_2 = D1[2]
            currD1_3 = D1[3]
            currD1_4 = D1[4]
            currD1_5 = D1[5]
            currD1_6 = D1[6]
            currD1_7 = D1[7]
            currD2_Mean = D2['mean']
            currD2_1 = D2[1]
            currD2_2 = D2[2]
            currD2_3 = D2[3]
            currD2_4 = D2[4]
            currD2_5 = D2[5]
            currD2_6 = D2[6]
            currD2_7 = D2[7]
            currD1_Mean.append(D1_mean)
            currD1_1.append(D1_1)
            currD1_2.append(D1_2)
            currD1_3.append(D1_3)
            currD1_4.append(D1_4)
            currD1_5.append(D1_5)
            currD1_6.append(D1_6)
            currD1_7.append(D1_7)
            currD2_Mean.append(D2_mean)
            currD2_1.append(D2_1)
            currD2_2.append(D2_2)
            currD2_3.append(D2_3)
            currD2_4.append(D2_4)
            currD2_5.append(D2_5)
            currD2_6.append(D2_6)
            currD2_7.append(D2_7)
            D1['mean'] = currD1_Mean
            D1[1] = currD1_1
            D1[2] = currD1_2
            D1[3] = currD1_3
            D1[4] = currD1_4
            D1[5] = currD1_5
            D1[6] = currD1_6
            D1[7] = currD1_7
            D2['mean'] = currD2_Mean
            D2[1] = currD2_1
            D2[2] = currD2_2
            D2[3] = currD2_3
            D2[4] = currD2_4
            D2[5] = currD2_5
            D2[6] = currD2_6
            D2[7] = currD2_7
    logfile = open('mt_nullDistribution_thetaU.log','a')
    logfile.write('Finished calculating population genetic parameters\nSorting Population Genetic Parameters\n')
    logfile.close()
    sortedD1_1 = sorted(D1[1])
    logfile = open('mt_nullDistribution_thetaU.log','a')
    logfile.write('\t' + str(round(100*(1.0/32))) + '% complete\n')
    logfile.close()
    sortedD1_2 = sorted(D1[2])
    logfile = open('mt_nullDistribution_thetaU.log','a')
    logfile.write('\t' + str(round(100*(2.0/32))) + '% complete\n')
    logfile.close()
    sortedD1_3 = sorted(D1[3])
    logfile = open('mt_nullDistribution_thetaU.log','a')
    logfile.write('\t' + str(round(100*(3.0/32))) + '% complete\n')
    logfile.close()
    sortedD1_4 = sorted(D1[4])
    logfile = open('mt_nullDistribution_thetaU.log','a')
    logfile.write('\t' + str(round(100*(4.0/32))) + '% complete\n')
    logfile.close()
    sortedD1_5 = sorted(D1[5])
    logfile = open('mt_nullDistribution_thetaU.log','a')
    logfile.write('\t' + str(round(100*(5.0/32))) + '% complete\n')
    logfile.close()
    sortedD1_6 = sorted(D1[6])
    logfile = open('mt_nullDistribution_thetaU.log','a')
    logfile.write('\t' + str(round(100*(6.0/32))) + '% complete\n')
    logfile.close()
    sortedD1_7 = sorted(D1[7])
    logfile = open('mt_nullDistribution_thetaU.log','a')
    logfile.write('\t' + str(round(100*(7.0/32))) + '% complete\n')
    logfile.close()
    sortedD1_Mean = sorted(D1['mean'])
    logfile = open('mt_nullDistribution_thetaU.log','a')
    logfile.write('\t' + str(round(100*(8.0/32))) + '% complete\n')
    logfile.close()
    sortedD2_1 = sorted(D2[1])
    logfile = open('mt_nullDistribution_thetaU.log','a')
    logfile.write('\t' + str(round(100*(9.0/32))) + '% complete\n')
    logfile.close()
    sortedD2_2 = sorted(D2[2])
    logfile = open('mt_nullDistribution_thetaU.log','a')
    logfile.write('\t' + str(round(100*(10.0/32))) + '% complete\n')
    logfile.close()
    sortedD2_3 = sorted(D2[3])
    logfile = open('mt_nullDistribution_thetaU.log','a')
    logfile.write('\t' + str(round(100*(11.0/32))) + '% complete\n')
    logfile.close()
    sortedD2_4 = sorted(D2[4])
    logfile = open('mt_nullDistribution_thetaU.log','a')
    logfile.write('\t' + str(round(100*(12.0/32))) + '% complete\n')
    logfile.close()
    sortedD2_5 = sorted(D2[5])
    logfile = open('mt_nullDistribution_thetaU.log','a')
    logfile.write('\t' + str(round(100*(13.0/32))) + '% complete\n')
    logfile.close()
    sortedD2_6 = sorted(D2[6])
    logfile = open('mt_nullDistribution_thetaU.log','a')
    logfile.write('\t' + str(round(100*(14.0/32))) + '% complete\n')
    logfile.close()
    sortedD2_7 = sorted(D2[7])
    logfile = open('mt_nullDistribution_thetaU.log','a')
    logfile.write('\t' + str(round(100*(15.0/32))) + '% complete\n')
    logfile.close()
    sortedD2_Mean = sorted(D2['mean'])
    logfile = open('mt_nullDistribution_thetaU.log','a')
    logfile.write('\t' + str(round(100*(16.0/32))) + '% complete\n')
    logfile.close()
    i = 0
    sys.stdout.write('D1_mean\tD2_mean\tD1_1\tD1_2\tD1_3\tD1_4\tD1_5\tD1_6\tD1_7\tD2_1\tD2_2\tD2_3\tD2_4\tD2_5\tD2_6\tD2_7\n')
    while i < 10000:
        sys.stdout.write(str(sortedD1_Mean[i]) + '\t' + str(sortedD2_Mean[i]) + '\t' + str(sortedD1_1[i]) + '\t' + str(sortedD1_2[i]) + '\t' + str(sortedD1_3[i]) + '\t' + str(sortedD1_4[i]) + '\t' + str(sortedD1_5[i]) + '\t' + str(sortedD1_6[i]) + '\t' + str(sortedD1_7[i]) + '\t' + str(sortedD2_1[i]) + '\t' + str(sortedD2_2[i]) + '\t' + str(sortedD2_3[i]) + '\t' + str(sortedD2_4[i]) + '\t' + str(sortedD2_5[i]) + '\t' + str(sortedD2_6[i]) + '\t' + str(sortedD2_7[i]) + '\n')
        i += 1
    logfile.close()

def thetaUSyn(fasta,code='invertebrateMt'):
    geneticCodes = {'standard':{"TTT":"F",	"TTC":"F",	"TTA":"L",	"TTG":"L",	"TCT":"S",	"TCC":"S",	"TCA":"S",	"TCG":"S",	"TAT":"Y",	"TAC":"Y",	"TAA":"*",	"TAG":"*",	"TGT":"C",	"TGC":"C",	"TGA":"*",	"TGG":"W",	"CTT":"L",	"CTC":"L",	"CTA":"L",	"CTG":"L",	"CCT":"P",	"CCC":"P",	"CCA":"P",	"CCG":"P",	"CAT":"H",	"CAC":"H",	"CAA":"Q",	"CAG":"Q",	"CGT":"R",	"CGC":"R",	"CGA":"R",	"CGG":"R",	"ATT":"I",	"ATC":"I",	"ATA":"I",	"ATG":"M",	"ACT":"T",	"ACC":"T",	"ACA":"T",	"ACG":"T",	"AAT":"N",	"AAC":"N",	"AAA":"K",	"AAG":"K",	"AGT":"S",	"AGC":"S",	"AGA":"R",	"AGG":"R",	"GTT":"V",	"GTC":"V",	"GTA":"V",	"GTG":"V",	"GCT":"A",	"GCC":"A",	"GCA":"A",	"GCG":"A",	"GAT":"D",	"GAC":"D",	"GAA":"E",	"GAG":"E",	"GGT":"G",	"GGC":"G",	"GGA":"G",	"GGG":"G"},'invertebrateMt':{'CTT': 'L', 'TAG': '*', 'ACA': 'T', 'ACG': 'T', 'ATC': 'I', 'AAC': 'N', 'ATA': 'M', 'AGG': 'S', 'CCT': 'P', 'ACT': 'T', 'AGC': 'S', 'AAG': 'K', 'AGA': 'S', 'CAT': 'H', 'AAT': 'N', 'ATT': 'I', 'CTG': 'L', 'CTA': 'L', 'CTC': 'L', 'CAC': 'H', 'AAA': 'K', 'CCG': 'P', 'AGT': 'S', 'CCA': 'P', 'CAA': 'Q', 'CCC': 'P', 'TAT': 'Y', 'GGT': 'G', 'TGT': 'C', 'CGA': 'R', 'CAG': 'Q', 'TCT': 'S', 'GAT': 'D', 'CGG': 'R', 'TTT': 'F', 'TGC': 'C', 'GGG': 'G', 'TGA': 'W', 'GGA': 'G', 'TGG': 'W', 'GGC': 'G', 'TAC': 'Y', 'TTC': 'F', 'TCG': 'S', 'TTA': 'L', 'TTG': 'L', 'TCC': 'S', 'ACC': 'T', 'TAA': '*', 'GCA': 'A', 'GTA': 'V', 'GCC': 'A', 'GTC': 'V', 'GCG': 'A', 'GTG': 'V', 'GAG': 'E', 'GTT': 'V', 'GCT': 'A', 'GAC': 'D', 'CGT': 'R', 'GAA': 'E', 'TCA': 'S', 'ATG': 'M', 'CGC': 'R'},'vertebrateMt':{'CTT': 'L', 'TAG': '*', 'ACA': 'T', 'ACG': 'T', 'ATC': 'I', 'AAC': 'N', 'ATA': 'M', 'AGG': '*', 'CCT': 'P', 'ACT': 'T', 'AGC': 'S', 'AAG': 'K', 'AGA': '*', 'CAT': 'H', 'AAT': 'N', 'ATT': 'I', 'CTG': 'L', 'CTA': 'L', 'CTC': 'L', 'CAC': 'H', 'AAA': 'K', 'CCG': 'P', 'AGT': 'S', 'CCA': 'P', 'CAA': 'Q', 'CCC': 'P', 'TAT': 'Y', 'GGT': 'G', 'TGT': 'C', 'CGA': 'R', 'CAG': 'Q', 'TCT': 'S', 'GAT': 'D', 'CGG': 'R', 'TTT': 'F', 'TGC': 'C', 'GGG': 'G', 'TGA': 'W', 'GGA': 'G', 'TGG': 'W', 'GGC': 'G', 'TAC': 'Y', 'TTC': 'F', 'TCG': 'S', 'TTA': 'L', 'TTG': 'L', 'TCC': 'S', 'ACC': 'T', 'TAA': '*', 'GCA': 'A', 'GTA': 'V', 'GCC': 'A', 'GTC': 'V', 'GCG': 'A', 'GTG': 'V', 'GAG': 'E', 'GTT': 'V', 'GCT': 'A', 'GAC': 'D', 'CGT': 'R', 'GAA': 'E', 'TCA': 'S', 'ATG': 'M', 'CGC': 'R'}, 'yeastMt':{'CTT': 'T', 'TAG': '*', 'ACA': 'T', 'ACG': 'T', 'ATC': 'I', 'AAC': 'N', 'ATA': 'M', 'AGG': 'R', 'CCT': 'P', 'ACT': 'T', 'AGC': 'S', 'AAG': 'K', 'AGA': 'R', 'CAT': 'H', 'AAT': 'N', 'ATT': 'I', 'CTG': 'T', 'CTA': 'T', 'CTC': 'T', 'CAC': 'H', 'AAA': 'K', 'CCG': 'P', 'AGT': 'S', 'CCA': 'P', 'CAA': 'Q', 'CCC': 'P', 'TAT': 'Y', 'GGT': 'G', 'TGT': 'C', 'CGA': 'R', 'CAG': 'Q', 'TCT': 'S', 'GAT': 'D', 'CGG': 'R', 'TTT': 'F', 'TGC': 'C', 'GGG': 'G', 'TGA': 'W', 'GGA': 'G', 'TGG': 'W', 'GGC': 'G', 'TAC': 'Y', 'TTC': 'F', 'TCG': 'S', 'TTA': 'L', 'TTG': 'L', 'TCC': 'S', 'ACC': 'T', 'TAA': '*', 'GCA': 'A', 'GTA': 'V', 'GCC': 'A', 'GTC': 'V', 'GCG': 'A', 'GTG': 'V', 'GAG': 'E', 'GTT': 'V', 'GCT': 'A', 'GAC': 'D', 'CGT': 'R', 'GAA': 'E', 'TCA': 'S', 'ATG': 'M', 'CGC': 'R'}, 'coelenterateMt':{'CTT': 'L', 'TAG': '*', 'ACA': 'T', 'ACG': 'T', 'ATC': 'I', 'AAC': 'N', 'ATA': 'I', 'AGG': 'R', 'CCT': 'P', 'ACT': 'T', 'AGC': 'S', 'AAG': 'K', 'AGA': 'R', 'CAT': 'H', 'AAT': 'N', 'ATT': 'I', 'CTG': 'L', 'CTA': 'L', 'CTC': 'L', 'CAC': 'H', 'AAA': 'K', 'CCG': 'P', 'AGT': 'S', 'CCA': 'P', 'CAA': 'Q', 'CCC': 'P', 'TAT': 'Y', 'GGT': 'G', 'TGT': 'C', 'CGA': 'R', 'CAG': 'Q', 'TCT': 'S', 'GAT': 'D', 'CGG': 'R', 'TTT': 'F', 'TGC': 'C', 'GGG': 'G', 'TGA': 'W', 'GGA': 'G', 'TGG': 'W', 'GGC': 'G', 'TAC': 'Y', 'TTC': 'F', 'TCG': 'S', 'TTA': 'L', 'TTG': 'L', 'TCC': 'S', 'ACC': 'T', 'TAA': '*', 'GCA': 'A', 'GTA': 'V', 'GCC': 'A', 'GTC': 'V', 'GCG': 'A', 'GTG': 'V', 'GAG': 'E', 'GTT': 'V', 'GCT': 'A', 'GAC': 'D', 'CGT': 'R', 'GAA': 'E', 'TCA': 'S', 'ATG': 'M', 'CGC': 'R'},'ciliateNuc':{'CTT': 'L', 'TAG': 'Q', 'ACA': 'T', 'ACG': 'T', 'ATC': 'I', 'AAC': 'N', 'ATA': 'I', 'AGG': 'R', 'CCT': 'P', 'ACT': 'T', 'AGC': 'S', 'AAG': 'K', 'AGA': 'R', 'CAT': 'H', 'AAT': 'N', 'ATT': 'I', 'CTG': 'L', 'CTA': 'L', 'CTC': 'L', 'CAC': 'H', 'AAA': 'K', 'CCG': 'P', 'AGT': 'S', 'CCA': 'P', 'CAA': 'Q', 'CCC': 'P', 'TAT': 'Y', 'GGT': 'G', 'TGT': 'C', 'CGA': 'R', 'CAG': 'Q', 'TCT': 'S', 'GAT': 'D', 'CGG': 'R', 'TTT': 'F', 'TGC': 'C', 'GGG': 'G', 'TGA': '*', 'GGA': 'G', 'TGG': 'W', 'GGC': 'G', 'TAC': 'Y', 'TTC': 'F', 'TCG': 'S', 'TTA': 'L', 'TTG': 'L', 'TCC': 'S', 'ACC': 'T', 'TAA': 'Q', 'GCA': 'A', 'GTA': 'V', 'GCC': 'A', 'GTC': 'V', 'GCG': 'A', 'GTG': 'V', 'GAG': 'E', 'GTT': 'V', 'GCT': 'A', 'GAC': 'D', 'CGT': 'R', 'GAA': 'E', 'TCA': 'S', 'ATG': 'M', 'CGC': 'R'},'echinodermMt':{'CTT': 'L', 'TAG': '*', 'ACA': 'T', 'ACG': 'T', 'ATC': 'I', 'AAC': 'N', 'ATA': 'I', 'AGG': 'S', 'CCT': 'P', 'ACT': 'T', 'AGC': 'S', 'AAG': 'K', 'AGA': 'S', 'CAT': 'H', 'AAT': 'N', 'ATT': 'I', 'CTG': 'L', 'CTA': 'L', 'CTC': 'L', 'CAC': 'H', 'AAA': 'N', 'CCG': 'P', 'AGT': 'S', 'CCA': 'P', 'CAA': 'Q', 'CCC': 'P', 'TAT': 'Y', 'GGT': 'G', 'TGT': 'C', 'CGA': 'R', 'CAG': 'Q', 'TCT': 'S', 'GAT': 'D', 'CGG': 'R', 'TTT': 'F', 'TGC': 'C', 'GGG': 'G', 'TGA': 'W', 'GGA': 'G', 'TGG': 'W', 'GGC': 'G', 'TAC': 'Y', 'TTC': 'F', 'TCG': 'S', 'TTA': 'L', 'TTG': 'L', 'TCC': 'S', 'ACC': 'T', 'TAA': '*', 'GCA': 'A', 'GTA': 'V', 'GCC': 'A', 'GTC': 'V', 'GCG': 'A', 'GTG': 'V', 'GAG': 'E', 'GTT': 'V', 'GCT': 'A', 'GAC': 'D', 'CGT': 'R', 'GAA': 'E', 'TCA': 'S', 'ATG': 'M', 'CGC': 'R'}, 'euplotidNuc':{'CTT': 'L', 'TAG': '*', 'ACA': 'T', 'ACG': 'T', 'ATC': 'I', 'AAC': 'N', 'ATA': 'I', 'AGG': 'R', 'CCT': 'P', 'ACT': 'T', 'AGC': 'S', 'AAG': 'K', 'AGA': 'R', 'CAT': 'H', 'AAT': 'N', 'ATT': 'I', 'CTG': 'L', 'CTA': 'L', 'CTC': 'L', 'CAC': 'H', 'AAA': 'K', 'CCG': 'P', 'AGT': 'S', 'CCA': 'P', 'CAA': 'Q', 'CCC': 'P', 'TAT': 'Y', 'GGT': 'G', 'TGT': 'C', 'CGA': 'R', 'CAG': 'Q', 'TCT': 'S', 'GAT': 'D', 'CGG': 'R', 'TTT': 'F', 'TGC': 'C', 'GGG': 'G', 'TGA': 'C', 'GGA': 'G', 'TGG': 'W', 'GGC': 'G', 'TAC': 'Y', 'TTC': 'F', 'TCG': 'S', 'TTA': 'L', 'TTG': 'L', 'TCC': 'S', 'ACC': 'T', 'TAA': '*', 'GCA': 'A', 'GTA': 'V', 'GCC': 'A', 'GTC': 'V', 'GCG': 'A', 'GTG': 'V', 'GAG': 'E', 'GTT': 'V', 'GCT': 'A', 'GAC': 'D', 'CGT': 'R', 'GAA': 'E', 'TCA': 'S', 'ATG': 'M', 'CGC': 'R'}, 'bacterial':{'CTT': 'L', 'TAG': '*', 'ACA': 'T', 'ACG': 'T', 'ATC': 'I', 'AAC': 'N', 'ATA': 'I', 'AGG': 'R', 'CCT': 'P', 'ACT': 'T', 'AGC': 'S', 'AAG': 'K', 'AGA': 'R', 'CAT': 'H', 'AAT': 'N', 'ATT': 'I', 'CTG': 'L', 'CTA': 'L', 'CTC': 'L', 'CAC': 'H', 'AAA': 'K', 'CCG': 'P', 'AGT': 'S', 'CCA': 'P', 'CAA': 'Q', 'CCC': 'P', 'TAT': 'Y', 'GGT': 'G', 'TGT': 'C', 'CGA': 'R', 'CAG': 'Q', 'TCT': 'S', 'GAT': 'D', 'CGG': 'R', 'TTT': 'F', 'TGC': 'C', 'GGG': 'G', 'TGA': '*', 'GGA': 'G', 'TGG': 'W', 'GGC': 'G', 'TAC': 'Y', 'TTC': 'F', 'TCG': 'S', 'TTA': 'L', 'TTG': 'L', 'TCC': 'S', 'ACC': 'T', 'TAA': '*', 'GCA': 'A', 'GTA': 'V', 'GCC': 'A', 'GTC': 'V', 'GCG': 'A', 'GTG': 'V', 'GAG': 'E', 'GTT': 'V', 'GCT': 'A', 'GAC': 'D', 'CGT': 'R', 'GAA': 'E', 'TCA': 'S', 'ATG': 'M', 'CGC': 'R'},'yeastNuc':{'CTT': 'L', 'TAG': '*', 'ACA': 'T', 'ACG': 'T', 'ATC': 'I', 'AAC': 'N', 'ATA': 'I', 'AGG': 'R', 'CCT': 'P', 'ACT': 'T', 'AGC': 'S', 'AAG': 'K', 'AGA': 'R', 'CAT': 'H', 'AAT': 'N', 'ATT': 'I', 'CTG': 'S', 'CTA': 'L', 'CTC': 'L', 'CAC': 'H', 'AAA': 'K', 'CCG': 'P', 'AGT': 'S', 'CCA': 'P', 'CAA': 'Q', 'CCC': 'P', 'TAT': 'Y', 'GGT': 'G', 'TGT': 'C', 'CGA': 'R', 'CAG': 'Q', 'TCT': 'S', 'GAT': 'D', 'CGG': 'R', 'TTT': 'F', 'TGC': 'C', 'GGG': 'G', 'TGA': '*', 'GGA': 'G', 'TGG': 'W', 'GGC': 'G', 'TAC': 'Y', 'TTC': 'F', 'TCG': 'S', 'TTA': 'L', 'TTG': 'L', 'TCC': 'S', 'ACC': 'T', 'TAA': '*', 'GCA': 'A', 'GTA': 'V', 'GCC': 'A', 'GTC': 'V', 'GCG': 'A', 'GTG': 'V', 'GAG': 'E', 'GTT': 'V', 'GCT': 'A', 'GAC': 'D', 'CGT': 'R', 'GAA': 'E', 'TCA': 'S', 'ATG': 'M', 'CGC': 'R'}, 'ascidianMt':{'CTT': 'L', 'TAG': '*', 'ACA': 'T', 'ACG': 'T', 'ATC': 'I', 'AAC': 'N', 'ATA': 'M', 'AGG': 'G', 'CCT': 'P', 'ACT': 'T', 'AGC': 'S', 'AAG': 'K', 'AGA': 'G', 'CAT': 'H', 'AAT': 'N', 'ATT': 'I', 'CTG': 'L', 'CTA': 'L', 'CTC': 'L', 'CAC': 'H', 'AAA': 'K', 'CCG': 'P', 'AGT': 'S', 'CCA': 'P', 'CAA': 'Q', 'CCC': 'P', 'TAT': 'Y', 'GGT': 'G', 'TGT': 'C', 'CGA': 'R', 'CAG': 'Q', 'TCT': 'S', 'GAT': 'D', 'CGG': 'R', 'TTT': 'F', 'TGC': 'C', 'GGG': 'G', 'TGA': 'W', 'GGA': 'G', 'TGG': 'W', 'GGC': 'G', 'TAC': 'Y', 'TTC': 'F', 'TCG': 'S', 'TTA': 'L', 'TTG': 'L', 'TCC': 'S', 'ACC': 'T', 'TAA': '*', 'GCA': 'A', 'GTA': 'V', 'GCC': 'A', 'GTC': 'V', 'GCG': 'A', 'GTG': 'V', 'GAG': 'E', 'GTT': 'V', 'GCT': 'A', 'GAC': 'D', 'CGT': 'R', 'GAA': 'E', 'TCA': 'S', 'ATG': 'M', 'CGC': 'R'},'flatwormMt':{'CTT': 'L', 'TAG': '*', 'ACA': 'T', 'ACG': 'T', 'ATC': 'I', 'AAC': 'N', 'ATA': 'I', 'AGG': 'S', 'CCT': 'P', 'ACT': 'T', 'AGC': 'S', 'AAG': 'K', 'AGA': 'S', 'CAT': 'H', 'AAT': 'N', 'ATT': 'I', 'CTG': 'L', 'CTA': 'L', 'CTC': 'L', 'CAC': 'H', 'AAA': 'N', 'CCG': 'P', 'AGT': 'S', 'CCA': 'P', 'CAA': 'Q', 'CCC': 'P', 'TAT': 'Y', 'GGT': 'G', 'TGT': 'C', 'CGA': 'R', 'CAG': 'Q', 'TCT': 'S', 'GAT': 'D', 'CGG': 'R', 'TTT': 'F', 'TGC': 'C', 'GGG': 'G', 'TGA': 'W', 'GGA': 'G', 'TGG': 'W', 'GGC': 'G', 'TAC': 'Y', 'TTC': 'F', 'TCG': 'S', 'TTA': 'L', 'TTG': 'L', 'TCC': 'S', 'ACC': 'T', 'TAA': 'Y', 'GCA': 'A', 'GTA': 'V', 'GCC': 'A', 'GTC': 'V', 'GCG': 'A', 'GTG': 'V', 'GAG': 'E', 'GTT': 'V', 'GCT': 'A', 'GAC': 'D', 'CGT': 'R', 'GAA': 'E', 'TCA': 'S', 'ATG': 'M', 'CGC': 'R'},'chlorophyceanMt':{'CTT': 'L', 'TAG': 'L', 'ACA': 'T', 'ACG': 'T', 'ATC': 'I', 'AAC': 'N', 'ATA': 'I', 'AGG': 'R', 'CCT': 'P', 'ACT': 'T', 'AGC': 'S', 'AAG': 'K', 'AGA': 'R', 'CAT': 'H', 'AAT': 'N', 'ATT': 'I', 'CTG': 'L', 'CTA': 'L', 'CTC': 'L', 'CAC': 'H', 'AAA': 'K', 'CCG': 'P', 'AGT': 'S', 'CCA': 'P', 'CAA': 'Q', 'CCC': 'P', 'TAT': 'Y', 'GGT': 'G', 'TGT': 'C', 'CGA': 'R', 'CAG': 'Q', 'TCT': 'S', 'GAT': 'D', 'CGG': 'R', 'TTT': 'F', 'TGC': 'C', 'GGG': 'G', 'TGA': '*', 'GGA': 'G', 'TGG': 'W', 'GGC': 'G', 'TAC': 'Y', 'TTC': 'F', 'TCG': 'S', 'TTA': 'L', 'TTG': 'L', 'TCC': 'S', 'ACC': 'T', 'TAA': '*', 'GCA': 'A', 'GTA': 'V', 'GCC': 'A', 'GTC': 'V', 'GCG': 'A', 'GTG': 'V', 'GAG': 'E', 'GTT': 'V', 'GCT': 'A', 'GAC': 'D', 'CGT': 'R', 'GAA': 'E', 'TCA': 'S', 'ATG': 'M', 'CGC': 'R'},'trematodeMt':{'CTT': 'L', 'TAG': '*', 'ACA': 'T', 'ACG': 'T', 'ATC': 'I', 'AAC': 'N', 'ATA': 'M', 'AGG': 'S', 'CCT': 'P', 'ACT': 'T', 'AGC': 'S', 'AAG': 'K', 'AGA': 'S', 'CAT': 'H', 'AAT': 'N', 'ATT': 'I', 'CTG': 'L', 'CTA': 'L', 'CTC': 'L', 'CAC': 'H', 'AAA': 'N', 'CCG': 'P', 'AGT': 'S', 'CCA': 'P', 'CAA': 'Q', 'CCC': 'P', 'TAT': 'Y', 'GGT': 'G', 'TGT': 'C', 'CGA': 'R', 'CAG': 'Q', 'TCT': 'S', 'GAT': 'D', 'CGG': 'R', 'TTT': 'F', 'TGC': 'C', 'GGG': 'G', 'TGA': 'W', 'GGA': 'G', 'TGG': 'W', 'GGC': 'G', 'TAC': 'Y', 'TTC': 'F', 'TCG': 'S', 'TTA': 'L', 'TTG': 'L', 'TCC': 'S', 'ACC': 'T', 'TAA': '*', 'GCA': 'A', 'GTA': 'V', 'GCC': 'A', 'GTC': 'V', 'GCG': 'A', 'GTG': 'V', 'GAG': 'E', 'GTT': 'V', 'GCT': 'A', 'GAC': 'D', 'CGT': 'R', 'GAA': 'E', 'TCA': 'S', 'ATG': 'M', 'CGC': 'R'},'pterobranchiaMt':{'CTT': 'L', 'TAG': '*', 'ACA': 'T', 'ACG': 'T', 'ATC': 'I', 'AAC': 'N', 'ATA': 'I', 'AGG': 'K', 'CCT': 'P', 'ACT': 'T', 'AGC': 'S', 'AAG': 'K', 'AGA': 'S', 'CAT': 'H', 'AAT': 'N', 'ATT': 'I', 'CTG': 'L', 'CTA': 'L', 'CTC': 'L', 'CAC': 'H', 'AAA': 'K', 'CCG': 'P', 'AGT': 'S', 'CCA': 'P', 'CAA': 'Q', 'CCC': 'P', 'TAT': 'Y', 'GGT': 'G', 'TGT': 'C', 'CGA': 'R', 'CAG': 'Q', 'TCT': 'S', 'GAT': 'D', 'CGG': 'R', 'TTT': 'F', 'TGC': 'C', 'GGG': 'G', 'TGA': 'W', 'GGA': 'G', 'TGG': 'W', 'GGC': 'G', 'TAC': 'Y', 'TTC': 'F', 'TCG': 'S', 'TTA': 'L', 'TTG': 'L', 'TCC': 'S', 'ACC': 'T', 'TAA': '*', 'GCA': 'A', 'GTA': 'V', 'GCC': 'A', 'GTC': 'V', 'GCG': 'A', 'GTG': 'V', 'GAG': 'E', 'GTT': 'V', 'GCT': 'A', 'GAC': 'D', 'CGT': 'R', 'GAA': 'E', 'TCA': 'S', 'ATG': 'M', 'CGC': 'R'}}
    geneticCode = geneticCodes[code]
    startCodons = ['ATT','ATC','ATA','ATG','GTG'] #invertebrateMt code
    positionDict = {(0,1533):'COI',(1533,2217):'COII',(2217,2373):'ATP8',(2373,3066):'ATP6',(3066,4005):'ND1',(4005,4509):'ND6',(4509,5646):'CYTB',(5646,5940):'ND4L',(5940,7314):'ND4',(7314,9030):'ND5',(9030,9807):'COIII',(9807,10158):'ND3',(10158,11214):'ND2'} #{(start,stop):gene}
    seqDict, seqList, codonDict = buildCodonDict(fasta)
    popList = []
    sexList = []
    outList = [] 
    thetaUSDict = {">$Heron2":(3,2598),	">$clone_1":(2,2598),	">$Rotoiti_1_4n":(2,2594.35416672),	">$AC51":(0,2598.33333333),	">$Heron_mitochondrion":(0,2599),	">$Grasmere_6_3n":(0,2599.62500001),	">$Poerua_triploid":(2,2597),	">$Brunner_6_3n":(2,2592.9583334),	">$McGregor":(0,2599),	">$Poerua_72_4n":(0,2605.47916675),	">$Gunn":(4,2597.66666667),	">$Grasmere_1_4n":(1,2628.66666703),	">$clone_7":(0,2592.85416667),	">$DenmarkA":(0,2593.125),	">$Duluth":(0,2591.52083333),	">$Waik_lane4_TCCTGAGC_trimmed_paired_contig_237":(3,2593.79166667),	">$Waik37":(0,2586.58333333),	">$Waik372":(4,2589.25),	">$Tarawera":(0,2586.58333333),	">$Kaniere_triploid":(1,2586.58333333),	">$Waik36":(14,2586.91666667),	">$WalesC":(2,2584.91666667),	">$Brunner_2_4n":(0,2593.60416674),	">$Lady":(9,2598.66666667),	">$Kaniere_1_2n":(9,2598.33333333),	">$Rotoroa_1_2n":(13,2598.58333338),	">$AlexMap":(0,2592.33333333),	">$Alexsex":(0,2592.33333333),	">$Yellow_Contig_56":(0,2592.33333333),	">$Ianthe":(4,2597),	">$Ianthe_lane1_TAAGGCGA_trimmed_paired_contig_309":(4,2595)}
    syn = []
    logfile = open('mt_nullDistribution_thetaU-S.log','w')
    for seq in seqList:
        if '$' in seq:
            popList.append(seq)
        else:
            outList.append(seq)
    seqNums = range(len(popList))
    currPCT = 0
    sexN = 8
    asexN = 23
    sexAn = aN(sexN)
    asexAn = aN(asexN)
    logfile.write('Calculating population genetic parameters:\n')
    logfile.close()
    while len(syn) < 10000:
        newPCT = int(round(100*len(syn)/10000.0))
        if newPCT > currPCT:
            logfile = open('mt_nullDistribution_thetaU-S.log','a')
            logfile.write('\t' + str(newPCT) + '% complete\n')
            logfile.close()
            currPCT = newPCT
        sexList = []
        asexList = []
        while len(sexList) < sexN:
            currNum = random.choice(seqNums)
            if popList[currNum] not in sexList:
                sexList.append(popList[currNum])
        while len(asexList) < asexN:
            currNum = random.choice(seqNums)
            if popList[currNum] not in asexList and popList[currNum] not in sexList:
                asexList.append(popList[currNum])
        asexSS = 0
        sexSS = 0
        asexSynSites = 0
        sexSynSites = 0
        for asexual in asexList:
            currSynValues = thetaUSDict[asexual]
            asexSS += currSynValues[0]
            asexSynSites += currSynValues[1]
        for sexual in sexList:
            currSynValues = thetaUSDict[sexual]
            sexSS += currSynValues[0]
            sexSynSites += currSynValues[1]
        asexThetaUS = float(asexSS)/(asexAn*(float(asexSynSites)/len(asexList)))
        sexThetaUS = float(sexSS)/(sexAn*(float(sexSynSites)/len(sexList)))
        Dsyn = asexThetaUS - sexThetaUS
        syn.append(Dsyn)
    logfile = open('mt_nullDistribution_thetaU-S.log','a')
    logfile.write('Finished calculating population genetic parameters\nSorting Population Genetic Parameters\n')
    logfile.close()
    sortedDSyn = sorted(syn)
    i = 0
    sys.stdout.write('Dsyn\n')
    while i < 10000:
        sys.stdout.write(str(sortedDSyn[i]) + '\n')
        i += 1

        
            
        
    

#thetaU(sys.argv[1])