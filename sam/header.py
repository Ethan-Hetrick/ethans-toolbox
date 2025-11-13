#!/usr/bin/env python3

import argparse
from tabulate import tabulate

def parse_header(sam_data):
    sam_header_dict = { '@HD': [ '''File-level metadata. Optional. If present, there must be only one @HD line and it must be the
first line of the file.''',
{'VN': 'Format version. Accepted format: /^[0-9]+\.[0-9]+$/.',
'SO': ''''Sorting order of alignments. Valid values: unknown (default), unsorted, queryname and
coordinate. For coordinate sort, the major sort key is the RNAME field, with order defined
by the order of @SQ lines in the header. The minor sort key is the POS field. For alignments
with equal RNAME and POS, order is arbitrary. All alignments with ‘*’ in RNAME field follow
alignments with some other value but otherwise are in arbitrary order. For queryname sort, no
explicit requirement is made regarding the ordering other than that it be applied consistently
throughout the entire file.''',
'GO': '''Grouping of alignments, indicating that similar alignment records are grouped together but the
file is not necessarily sorted overall. Valid values: none (default), query (alignments are grouped
by QNAME), and reference (alignments are grouped by RNAME/POS).''',
'SS': ''''Sub-sorting order of alignments. Valid values are of the form sort-order:sub-sort, where sortorder is the same value stored in the SO tag and sub-sort is an implementation-dependent
colon-separated string further describing the sort order, but with some predefined terms defined in Section 1.3.1. For example, if an algorithm relies on a coordinate sort that, at each
coordinate, is further sorted by query name then the header could contain @HD SO:coordinate
SS:coordinate:queryname.
If the primary sort is not one of the predefined primary sort orders,
then unsorted should be used and the sub-sort is effectively the major sort. For example, if
sorted by an auxiliary tag MI then by coordinate then the header could contain @HD SO:unsorted
SS:unsorted:MI:coordinate.
Regular expression: (coordinate|queryname|unsorted)(:[A-Za-z0-9_-]+)+'''} ],
'@SQ': [ 'Reference sequence dictionary. The order of @SQ lines defines the alignment sorting order.',
{'SN': '''Reference sequence name. The SN tags and all individual AN names in all @SQ lines must be
distinct. The value of this field is used in the alignment records in RNAME and RNEXT fields.
Regular expression: [:rname:∧*=][:rname:]*''', 
'LN': 'Reference sequence length. Range: [1, 2^31 − 1]',
'AH': '''Indicates that this sequence is an alternate locus.8 The value is the locus in the primary assembly
for which this sequence is an alternative, in the format ‘chr:start-end’, ‘chr ’ (if known), or ‘*’ (if
unknown), where ‘chr ’ is a sequence in the primary assembly. Must not be present on sequences
in the primary assembly.''',
'AN': '''Alternative reference sequence names. A comma-separated list of alternative names that tools
may use when referring to this reference sequence.9 These alternative names are not used
elsewhere within the SAM file; in particular, they must not appear in alignment records’ RNAME
or RNEXT fields. Regular expression: name(,name)* where name is [:rname:∧*=][:rname:]*''',
'AS': 'Genome assembly identifier.',
'DS': 'Description. UTF-8 encoding may be used.',
'M5': 'MD5 checksum of the sequence. See Section 1.3.2',
'SP': 'Species.',
'TP': 'Molecule topology. Valid values: linear (default) and circular.',
'UR': '''URI of the sequence. This value may start with one of the standard protocols, e.g., ‘http:’ or
‘ftp:’. If it does not start with one of these protocols, it is assumed to be a file-system path.'''} ],
'@RG': ['Read group. Unordered multiple @RG lines are allowed.',
{'ID': '''Read group identifier. Each @RG line must have a unique ID. The value of ID is used in the RG
tags of alignment records. Must be unique among all read groups in header section. Read group
IDs may be modified when merging SAM files in order to handle collisions.''',
'BC': '''Barcode sequence identifying the sample or library. This value is the expected barcode bases
as read by the sequencing machine in the absence of errors. If there are several barcodes for
the sample/library (e.g., one on each end of the template), the recommended implementation
concatenates all the barcodes separating them with hyphens (‘-’).''',
'CN': 'Name of sequencing center producing the read.',
'DS': 'Description. UTF-8 encoding may be used.',
'DT': 'Date the run was produced (ISO8601 date or date/time).',
'FO': '''Flow order. The array of nucleotide bases that correspond to the nucleotides used for each
flow of each read. Multi-base flows are encoded in IUPAC format, and non-nucleotide flows by
various other characters. Format: /\*|[ACMGRSVTWYHKDBN]+/''',
'KS': 'The array of nucleotide bases that correspond to the key sequence of each read.',
'LB': 'Library.',
'PG': 'Programs used for processing the read group.',
'PI': 'Predicted median insert size',
'PL': '''Platform/technology used to produce the reads. Valid values: CAPILLARY, DNBSEQ (MGI/BGI),
ELEMENT, HELICOS, ILLUMINA, IONTORRENT, LS454, ONT (Oxford Nanopore), PACBIO (Pacific Biosciences), SOLID, and ULTIMA. This field should be omitted when the technology is not in this
list (though the PM field may still be present in this case) or is unknown.''',
'PM': 'Platform model. Free-form text providing further details of the platform/technology used.',
'PU': 'Platform unit (e.g., flowcell-barcode.lane for Illumina or slide for SOLiD). Unique identifier.',
'SM': 'Sample. Use pool name where a pool is being sequenced.'} ],
'@PG': [ 'Program.', {
'ID': '''Program record identifier. Each @PG line must have a unique ID. The value of ID is used in the
alignment PG tag and PP tags of other @PG lines. PG IDs may be modified when merging SAM
files in order to handle collisions.''',
'PN': 'Program name',
'CL': 'Command line. UTF-8 encoding may be used.',
'PP': '''Previous @PG-ID. Must match another @PG header’s ID tag. @PG records may be chained using PP
tag, with the last record in the chain having no PP tag. This chain defines the order of programs
that have been applied to the alignment. PP values may be modified when merging SAM files
in order to handle collisions of PG IDs. The first PG record in a chain (i.e., the one referred to
by the PG tag in a SAM record) describes the most recent program that operated on the SAM
record. The next PG record in the chain describes the next most recent program that operated
on the SAM record. The PG ID on a SAM record is not required to refer to the newest PG record
in a chain. It may refer to any PG record in a chain, implying that the SAM record has been
operated on by the program in that PG record, and the program(s) referred to via the PP tag.''',
'DS': 'Description. UTF-8 encoding may be used.',
'VN': 'Program version'} ],
'@CO': '''One-line text comment. Unordered multiple @CO lines are allowed. UTF-8 encoding may be
used.'''}
    
    header_dict = {}
    x = 0
    
    for line in sam_data:
        if line.startswith('@'):
            tabs = line.split('\t')
            label = f"{tabs[0]}_{x}"
            header_dict[label] = list(tabs[1:])
            x += 1
        else:
            break
    
    data_for_table = [['Header', 'Tag', 'Value', 'Description']]
    
    if len(header_dict) == 0:
        print("No SAM headers found")
        exit()
    
    for header, tags in header_dict.items():
        header_type = header.split('_')[0]
        header_line = header.split('_')[-1]
        sam_header_dict_1 = dict(sam_header_dict[header_type][1])
        
        for tag in tags:
            tag_name,tag_value = tag.split(':', 1)[0], tag.split(':', 1)[-1].strip()
            try:
                tag_description = sam_header_dict_1[tag_name].strip("\n")
            except KeyError:
                tag_description = 'Description not found'
    
            data_for_table.append([f'{header_type}\n(line {header_line})', tag_name, tag_value, tag_description])
        
    data_table = tabulate(data_for_table, maxcolwidths=50, headers="firstrow", tablefmt='grid')
    
    return data_table


def run():
    parser = argparse.ArgumentParser()
    parser.add_argument("-a", "--sam", type=str, help="SAM file.")
    args = parser.parse_args()
    
    with open(args.sam, 'r') as sam:
        sam_data = sam.readlines()
        sam.close()
    
    data_table = parse_header(sam_data)
    print(data_table)
    
if __name__ == "__main__":
    run()