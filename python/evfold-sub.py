import requests

url = "http://evfold.org/evfold-web/newmarkeccomputesubmit.do"
name = 'abc'
email = 'wj_hust08@163.com'
seq = 'MTEYKLVVVGAGGVGKSALTIQLIQNHFVDEYDPTIEDSYRKQVVIDGETCLLDILDTAGQEEYSAMRDQYMRTGEGFLCVFAINNTKSFEDIHQYREQIKRVKDSDDVPMVLVGNKCDLAARTVESRQAQDLARSYGIPYIETSAKTRQGVEDAFYTLVREIRQHKLRKLNPPDESGPGCMSCKCVLS'

files = {
    'coupling_scoring' : (None, 'PLM'),
    'output_file_prefix' : (None, name),
    'contact_email' : (None, email),
    'protein_Input' : (None, seq),
    'is_transmembrane' : (None, 'no'),
    'coupling_scoring' : (None, 'PLM'),
    'pdb_identifier' : (None, '5p21'),
    'alignment_generation_tool' : (None, 'jackhmmer'),
    'start_offset' : (None, '1'),
    'end_offset' : (None, ''),
    'alignment_inclusiveness' : (None, 'balanced'),
    'match_column_gap_pct_limit' : (None, '30'),
    'pfam_accession' : (None, ''),
    'pfam_member_selector' : (None, ''),
    'pfam_name' : (None, ''),
    'alignment_member_gap_pct_limit' : (None, '30'),
    'alignment_member_sequence_identity_minimum' : (None, ''),
    'alignment_member_sequence_identity_rank_limit' : (None, ''),
    'contact_map_ec_count_list_size' : (None, 'standard'),
    'custom_contact_map_ec_count_list' : (None, ''),
    'residue_proximity_threshold' : (None, '5'),
    'residue_proximity_method' : (None, 'nearest_atom'),
    'false_positive_plot_ec_count' : (None, '300'),
    'additional_contact_maps' : (None, 'none'),
    'ss_upstream_residues' : (None, '7'),
    'ss_downstream_residues' : (None, '7'),
    'membrane_helix_topology_override' : (None, ''),
    'psipred_helix_override' : (None, ''),
    'psipred_strand_override' : (None, ''),
    'family_weighting_distance_threshold' : (None, '0.1'),
    'high_conservation_threshold' : (None, '100'),
    'exclude_gaps' : (None, 'no'),
    'pair_min_residue_offset_distance' : (None, '5'),
    'gap_count_limit' : (None, '3'),
    'identical_dist' : (None, '0'),
    'correct_ambiguous_dist' : (None, '1'),
    'ambiguous_ambiguous_dist' : (None, '2'),
    'other_ambiguous_dist' : (None, '4'),
    'mismatch_dist' : (None, '34'),
    'allowable_mismatch_offset_list' : (None, ''),
    'unaligned_uniprot_residue_dist' : (None, '10'),
    'internal_gap_open_dist' : (None, '3'),
    'peripheral_gap_open_dist' : (None, '1'),
    'maximum_distance_cutoff_sequence_length_denominator' : (None, '16'),
    'maximum_distance_cutoff_absolute_minimum' : (None, '4'),
    'substantial_coverage_after_gap' : (None, '4'),
    'suggestion_gap_count' : (None, '2'),
    'maximum_domain_width' : (None, '500'),
    'minimum_domain_width' : (None, '30'),
    'minimum_alignment_member_count' : (None, '300'),
    'abundant_alignment_member_count' : (None, '120000'),
    'maximum_alignment_member_count' : (None, '150000'),
    'minimum_alignment_match_col_pct' : (None, '30'),
    'jackhmmer_alignment_iteration_count' : (None, '5'),
    'hhblits_alignment_iteration_count' : (None, '2'),
    'alignment_e_value_exploration_1' : (None, '-3'),
    'alignment_e_value_exploration_2' : (None, '-5'),
    'alignment_e_value_exploration_3' : (None, '-10'),
    'alignment_e_value_exploration_4' : (None, '-20'),
    'alignment_e_value_exploration_5' : (None, '-30'),
    'alignment_e_value_exploration_6' : (None, '-50'),
    'di_method_to_resolve_ambiguous_residues' : (None, 'suppress_member'),
    'di_pseudocount_weight' : (None, '0.5'),
    'plm_field_coefficient' : (None, '0.01'),
    'plm_coupling_coefficient' : (None, '0.01')
}

response = requests.post(url, files=files)

print response.text




