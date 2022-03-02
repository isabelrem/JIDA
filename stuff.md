<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN">
<html><head><title>Python: module stats</title>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
</head><body bgcolor="#f0f0f8">

<table width="100%" cellspacing=0 cellpadding=2 border=0 summary="heading">
<tr bgcolor="#7799ee">
<td valign=bottom>&nbsp;<br>
<font color="#ffffff" face="helvetica, arial">&nbsp;<br><big><big><strong>stats</strong></big></big></font></td
><td align=right valign=bottom
><font color="#ffffff" face="helvetica, arial"><a href=".">index</a><br><a href="file:c%3A%5Cusers%5Cjanee%5Cdesktop%5Cjaneesh%5Cuniversity%5Cmsc%20bioinformatics%5Cgroup%20project%5Capp-01-03-22%5Cstats.py">c:\users\janee\desktop\janeesh\university\msc bioinformatics\group project\app-01-03-22\stats.py</a></font></td></tr></table>
    <p><tt>###############################&nbsp;SQL&nbsp;TO&nbsp;PANDAS&nbsp;###############################</tt></p>
<p>
<table width="100%" cellspacing=0 cellpadding=2 border=0 summary="section">
<tr bgcolor="#aa55cc">
<td colspan=3 valign=bottom>&nbsp;<br>
<font color="#ffffff" face="helvetica, arial"><big><strong>Modules</strong></big></font></td></tr>
    
<tr><td bgcolor="#aa55cc"><tt>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</tt></td><td>&nbsp;</td>
<td width="100%"><table width="100%" summary="list"><tr><td width="25%" valign=top><a href="allel.html">allel</a><br>
</td><td width="25%" valign=top><a href="numpy.html">numpy</a><br>
</td><td width="25%" valign=top></td><td width="25%" valign=top></td></tr></table></td></tr></table><p>
<table width="100%" cellspacing=0 cellpadding=2 border=0 summary="section">
<tr bgcolor="#eeaa77">
<td colspan=3 valign=bottom>&nbsp;<br>
<font color="#ffffff" face="helvetica, arial"><big><strong>Functions</strong></big></font></td></tr>
    
<tr><td bgcolor="#eeaa77"><tt>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</tt></td><td>&nbsp;</td>
<td width="100%"><dl><dt><a name="-SQLtoFST"><strong>SQLtoFST</strong></a>(df_pop1, df_pop2)</dt><dd><tt>Using&nbsp;two&nbsp;population&nbsp;dataframes&nbsp;as&nbsp;input,&nbsp;calculates&nbsp;the&nbsp;FST&nbsp;value&nbsp;for&nbsp;the&nbsp;two&nbsp;populations.<br>
&nbsp;<br>
Parameters<br>
----------<br>
&nbsp;<br>
df_pop1:&nbsp;a&nbsp;pandas&nbsp;dataframe&nbsp;containing&nbsp;variant&nbsp;data&nbsp;from&nbsp;only&nbsp;1&nbsp;population,&nbsp;created&nbsp;using&nbsp;the&nbsp;python&nbsp;pandas&nbsp;library.<br>
df_pop2:&nbsp;a&nbsp;pandas&nbsp;dataframe&nbsp;containing&nbsp;variant&nbsp;data&nbsp;from&nbsp;only&nbsp;1&nbsp;population,&nbsp;created&nbsp;using&nbsp;the&nbsp;python&nbsp;pandas&nbsp;library.<br>
&nbsp;<br>
&nbsp;<br>
Description<br>
-----------<br>
&nbsp;<br>
Recieves&nbsp;2&nbsp;parameters,&nbsp;one&nbsp;pandas&nbsp;dataframe&nbsp;for&nbsp;one&nbsp;population,&nbsp;another&nbsp;pandas&nbsp;dataframe&nbsp;for&nbsp;a&nbsp;second&nbsp;population.<br>
The&nbsp;FST&nbsp;statistic&nbsp;is&nbsp;calculated&nbsp;across&nbsp;both&nbsp;dataframes.<br>
Calculating&nbsp;the&nbsp;FST&nbsp;for&nbsp;each&nbsp;window&nbsp;uses&nbsp;the&nbsp;pre-written&nbsp;functions&nbsp;<a href="#-genotype_list">genotype_list</a>()&nbsp;and&nbsp;<a href="#-hudson_FST">hudson_FST</a>().<br>
This&nbsp;function&nbsp;depends&nbsp;on&nbsp;the&nbsp;python&nbsp;packages/modules&nbsp;scikit-allel,&nbsp;pandas,&nbsp;numpy.<br>
&nbsp;<br>
Returns<br>
-------<br>
&nbsp;<br>
A&nbsp;list&nbsp;of&nbsp;FST&nbsp;values&nbsp;calculated&nbsp;for&nbsp;each&nbsp;window.</tt></dd></dl>
 <dl><dt><a name="-SQLtoFST_window"><strong>SQLtoFST_window</strong></a>(df_pop1, df_pop2, window_size=10)</dt><dd><tt>Using&nbsp;two&nbsp;population&nbsp;dataframes&nbsp;and&nbsp;(optional)&nbsp;window&nbsp;size&nbsp;as&nbsp;input,&nbsp;calculates&nbsp;windowed&nbsp;FST&nbsp;between&nbsp;the&nbsp;two&nbsp;populations.<br>
&nbsp;<br>
Parameters<br>
----------<br>
&nbsp;<br>
df_pop1:&nbsp;a&nbsp;pandas&nbsp;dataframe&nbsp;containing&nbsp;variant&nbsp;data&nbsp;from&nbsp;only&nbsp;1&nbsp;population,&nbsp;created&nbsp;using&nbsp;the&nbsp;python&nbsp;pandas&nbsp;library.<br>
df_pop2:&nbsp;a&nbsp;pandas&nbsp;dataframe&nbsp;containing&nbsp;variant&nbsp;data&nbsp;from&nbsp;only&nbsp;1&nbsp;population,&nbsp;created&nbsp;using&nbsp;the&nbsp;python&nbsp;pandas&nbsp;library.<br>
window_size:&nbsp;int<br>
&nbsp;<br>
Description<br>
-----------<br>
&nbsp;<br>
Recieves&nbsp;3&nbsp;parameters,&nbsp;one&nbsp;pandas&nbsp;dataframe&nbsp;for&nbsp;one&nbsp;population,&nbsp;another&nbsp;pandas&nbsp;dataframe&nbsp;for&nbsp;a&nbsp;second&nbsp;population,&nbsp;and&nbsp;a&nbsp;window_size.<br>
Using&nbsp;the&nbsp;window_size&nbsp;integer,&nbsp;the&nbsp;both&nbsp;population&nbsp;dataframes&nbsp;are&nbsp;subset&nbsp;into&nbsp;windows&nbsp;and&nbsp;the&nbsp;FST&nbsp;statistic&nbsp;is&nbsp;calculated&nbsp;across&nbsp;the&nbsp;window&nbsp;using&nbsp;both&nbsp;dataframes.<br>
Calculating&nbsp;the&nbsp;FST&nbsp;for&nbsp;each&nbsp;window&nbsp;uses&nbsp;the&nbsp;pre-written&nbsp;functions&nbsp;<a href="#-SQLtoFST">SQLtoFST</a>().<br>
This&nbsp;function&nbsp;depends&nbsp;on&nbsp;the&nbsp;python&nbsp;packages/modules&nbsp;scikit-allel,&nbsp;pandas,&nbsp;numpy&nbsp;and&nbsp;math.<br>
&nbsp;<br>
Returns<br>
-------<br>
&nbsp;<br>
A&nbsp;list&nbsp;of&nbsp;FST&nbsp;values&nbsp;calculated&nbsp;for&nbsp;each&nbsp;window.</tt></dd></dl>
 <dl><dt><a name="-SQLtoHapDiv"><strong>SQLtoHapDiv</strong></a>(df)</dt><dd><tt>Using&nbsp;a&nbsp;dataframe&nbsp;as&nbsp;input,&nbsp;outputs&nbsp;the&nbsp;haplotype&nbsp;diversity<br>
&nbsp;<br>
Parameters<br>
----------<br>
&nbsp;<br>
dataframe:&nbsp;a&nbsp;pandas&nbsp;dataframe,&nbsp;created&nbsp;using&nbsp;the&nbsp;python&nbsp;pandas&nbsp;library.<br>
&nbsp;<br>
Description<br>
-----------<br>
&nbsp;<br>
Recieves&nbsp;1&nbsp;parameter,&nbsp;a&nbsp;pandas&nbsp;dataframe.&nbsp;The&nbsp;haplotype&nbsp;diversity&nbsp;is&nbsp;calculated&nbsp;across&nbsp;the&nbsp;dataframe.<br>
Calculating&nbsp;haplotype&nbsp;diversity&nbsp;uses&nbsp;the&nbsp;pre-written&nbsp;functions&nbsp;<a href="#-haplotype_list">haplotype_list</a>()&nbsp;and&nbsp;<a href="#-haplotype_diversity">haplotype_diversity</a>().<br>
This&nbsp;function&nbsp;depends&nbsp;on&nbsp;the&nbsp;python&nbsp;packages/modules&nbsp;scikit-allel,&nbsp;pandas.<br>
&nbsp;<br>
Returns<br>
-------<br>
&nbsp;<br>
A&nbsp;haplotype&nbsp;diversity&nbsp;value.</tt></dd></dl>
 <dl><dt><a name="-SQLtoHapDiv_window"><strong>SQLtoHapDiv_window</strong></a>(dataframe, window_size=10)</dt><dd><tt>Using&nbsp;a&nbsp;dataframe&nbsp;and&nbsp;(optional)&nbsp;window&nbsp;size&nbsp;as&nbsp;input,&nbsp;outputs&nbsp;a&nbsp;list&nbsp;of&nbsp;haplotype&nbsp;diversities&nbsp;for&nbsp;each&nbsp;window<br>
&nbsp;<br>
Parameters<br>
----------<br>
&nbsp;<br>
dataframe:&nbsp;a&nbsp;pandas&nbsp;dataframe,&nbsp;created&nbsp;using&nbsp;the&nbsp;python&nbsp;pandas&nbsp;library.<br>
window_size:&nbsp;int<br>
&nbsp;<br>
Description<br>
-----------<br>
&nbsp;<br>
Recieves&nbsp;2&nbsp;parameters,&nbsp;a&nbsp;pandas&nbsp;dataframe&nbsp;and&nbsp;a&nbsp;window_size.&nbsp;Using&nbsp;the&nbsp;window_size&nbsp;integer,&nbsp;the&nbsp;dataframe&nbsp;is&nbsp;subset&nbsp;into&nbsp;windows&nbsp;and&nbsp;the&nbsp;haplotype&nbsp;diversity&nbsp;is&nbsp;calculated&nbsp;across&nbsp;the&nbsp;window.<br>
Calculating&nbsp;haplotype&nbsp;diversity&nbsp;for&nbsp;the&nbsp;windows&nbsp;uses&nbsp;the&nbsp;pre-written&nbsp;functions&nbsp;<a href="#-haplotype_list">haplotype_list</a>()&nbsp;and&nbsp;<a href="#-haplotype_diversity">haplotype_diversity</a>().<br>
This&nbsp;function&nbsp;depends&nbsp;on&nbsp;the&nbsp;python&nbsp;packages/modules&nbsp;scikit-allel,&nbsp;pandas&nbsp;and&nbsp;math.<br>
&nbsp;<br>
Returns<br>
-------<br>
&nbsp;<br>
A&nbsp;list&nbsp;of&nbsp;haplotype&nbsp;diversity&nbsp;values&nbsp;calculated&nbsp;for&nbsp;each&nbsp;window.</tt></dd></dl>
 <dl><dt><a name="-SQLtoNucDiv"><strong>SQLtoNucDiv</strong></a>(df, start, end)</dt><dd><tt>Using&nbsp;a&nbsp;dataframe&nbsp;and&nbsp;genomic&nbsp;start&nbsp;and&nbsp;end&nbsp;coordinates&nbsp;as&nbsp;inputs,&nbsp;outputs&nbsp;nucleotide&nbsp;diversity.<br>
&nbsp;<br>
Parameters<br>
----------<br>
dataframe:&nbsp;a&nbsp;pandas&nbsp;dataframe,&nbsp;created&nbsp;using&nbsp;the&nbsp;python&nbsp;pandas&nbsp;library.<br>
start:&nbsp;int,&nbsp;the&nbsp;genomic&nbsp;position&nbsp;to&nbsp;begin&nbsp;the&nbsp;search&nbsp;at.<br>
end:&nbsp;int,&nbsp;the&nbsp;genomic&nbsp;position&nbsp;to&nbsp;end&nbsp;the&nbsp;search&nbsp;at.<br>
Description<br>
-----------<br>
Recieves&nbsp;3&nbsp;parameters,&nbsp;a&nbsp;pandas&nbsp;dataframe&nbsp;and&nbsp;start&nbsp;and&nbsp;end&nbsp;genomic&nbsp;positions.<br>
The&nbsp;nucleotide&nbsp;diversity&nbsp;is&nbsp;calculated&nbsp;across&nbsp;the&nbsp;dataframe.<br>
Calculating&nbsp;nucleotide&nbsp;diversity&nbsp;for&nbsp;the&nbsp;windows&nbsp;uses&nbsp;the&nbsp;pre-written&nbsp;functions&nbsp;<a href="#-genotype_list">genotype_list</a>()&nbsp;and&nbsp;<a href="#-nucleotide_diversity">nucleotide_diversity</a>().<br>
This&nbsp;function&nbsp;depends&nbsp;on&nbsp;the&nbsp;python&nbsp;packages/modules&nbsp;scikit-allel,&nbsp;pandas.<br>
Returns<br>
-------<br>
A&nbsp;nucleotide&nbsp;diversity&nbsp;value&nbsp;for&nbsp;between&nbsp;the&nbsp;specified&nbsp;start&nbsp;and&nbsp;end&nbsp;genomic&nbsp;positions.</tt></dd></dl>
 <dl><dt><a name="-SQLtoPandasViaPOS"><strong>SQLtoPandasViaPOS</strong></a>(database, table, start, end)</dt><dd><tt>Using&nbsp;the&nbsp;inputs&nbsp;of&nbsp;a&nbsp;database&nbsp;name,&nbsp;table&nbsp;name,&nbsp;and&nbsp;start&nbsp;and&nbsp;end&nbsp;genomic&nbsp;coordinates,&nbsp;produces&nbsp;a&nbsp;pandas&nbsp;dataframe</tt></dd></dl>
 <dl><dt><a name="-SQLtoTD"><strong>SQLtoTD</strong></a>(df)</dt><dd><tt>Using&nbsp;a&nbsp;dataframe&nbsp;as&nbsp;input,&nbsp;calculates&nbsp;Tajima's&nbsp;D.<br>
&nbsp;<br>
&nbsp;Parameters<br>
----------<br>
&nbsp;<br>
dataframe:&nbsp;a&nbsp;pandas&nbsp;dataframe,&nbsp;created&nbsp;using&nbsp;the&nbsp;python&nbsp;pandas&nbsp;library.<br>
&nbsp;<br>
Description<br>
-----------<br>
&nbsp;<br>
Recieves&nbsp;1&nbsp;parameter,&nbsp;a&nbsp;pandas&nbsp;dataframe.&nbsp;The&nbsp;Tajima's&nbsp;D&nbsp;statistic&nbsp;is&nbsp;calculated&nbsp;across&nbsp;the&nbsp;dataframe.<br>
Calculating&nbsp;Tajima's&nbsp;D&nbsp;uses&nbsp;the&nbsp;pre-written&nbsp;functions&nbsp;<a href="#-Tajimas_D">Tajimas_D</a>()&nbsp;and&nbsp;genotype_list.<br>
This&nbsp;function&nbsp;depends&nbsp;on&nbsp;the&nbsp;python&nbsp;packages/modules&nbsp;scikit-allel,&nbsp;pandas,&nbsp;numpy.<br>
&nbsp;<br>
Returns<br>
-------<br>
&nbsp;<br>
A&nbsp;Tajima's&nbsp;D&nbsp;value.</tt></dd></dl>
 <dl><dt><a name="-SQLtoTD_window"><strong>SQLtoTD_window</strong></a>(dataframe, window_size=10)</dt><dd><tt>Using&nbsp;a&nbsp;dataframe&nbsp;and&nbsp;(optional)&nbsp;window&nbsp;size&nbsp;as&nbsp;input,&nbsp;returns&nbsp;a&nbsp;list&nbsp;of&nbsp;Tajima's&nbsp;D&nbsp;values&nbsp;for&nbsp;each&nbsp;window.<br>
&nbsp;<br>
Parameters<br>
----------<br>
&nbsp;<br>
dataframe:&nbsp;a&nbsp;pandas&nbsp;dataframe,&nbsp;created&nbsp;using&nbsp;the&nbsp;python&nbsp;pandas&nbsp;library.<br>
window_size:&nbsp;int<br>
&nbsp;<br>
Description<br>
-----------<br>
&nbsp;<br>
Recieves&nbsp;2&nbsp;parameters,&nbsp;a&nbsp;pandas&nbsp;dataframe&nbsp;and&nbsp;a&nbsp;window_size.&nbsp;Using&nbsp;the&nbsp;window_size&nbsp;integer,&nbsp;the&nbsp;dataframe&nbsp;is&nbsp;subset&nbsp;into&nbsp;windows&nbsp;and&nbsp;the&nbsp;Tajima's&nbsp;D&nbsp;statistic&nbsp;is&nbsp;calculated&nbsp;across&nbsp;the&nbsp;window.<br>
Calculating&nbsp;Tajima's&nbsp;D&nbsp;for&nbsp;each&nbsp;window&nbsp;uses&nbsp;the&nbsp;pre-written&nbsp;functions&nbsp;<a href="#-SQLtoTD">SQLtoTD</a>().<br>
This&nbsp;function&nbsp;depends&nbsp;on&nbsp;the&nbsp;python&nbsp;packages/modules&nbsp;scikit-allel,&nbsp;pandas,&nbsp;numpy&nbsp;and&nbsp;math.<br>
&nbsp;<br>
Returns<br>
-------<br>
&nbsp;<br>
A&nbsp;list&nbsp;of&nbsp;Tajima's&nbsp;D&nbsp;values&nbsp;calculated&nbsp;for&nbsp;each&nbsp;window.</tt></dd></dl>
 <dl><dt><a name="-Tajimas_D"><strong>Tajimas_D</strong></a>(genotype_list, POS)</dt><dd><tt>Calculates&nbsp;Tajima's&nbsp;D<br>
Parameters<br>
----------<br>
genotype_list:&nbsp;list<br>
POS:&nbsp;list<br>
Description<br>
-----------<br>
Converts&nbsp;the&nbsp;genotype&nbsp;list&nbsp;into&nbsp;a&nbsp;genotype&nbsp;array&nbsp;and&nbsp;extracts&nbsp;the&nbsp;allele&nbsp;counts.&nbsp;Using&nbsp;the&nbsp;SciKit&nbsp;Allel&nbsp;function<br>
tajima&nbsp;d&nbsp;the&nbsp;allele&nbsp;count&nbsp;and&nbsp;variant&nbsp;position&nbsp;list&nbsp;is&nbsp;inserted,&nbsp;the&nbsp;minimum&nbsp;segregated&nbsp;sites&nbsp;selected&nbsp;is&nbsp;1.<br>
Returns<br>
-------<br>
Single&nbsp;Tajima's&nbsp;D&nbsp;value</tt></dd></dl>
 <dl><dt><a name="-genotype_list"><strong>genotype_list</strong></a>(dataframe)</dt><dd><tt>Produces&nbsp;a&nbsp;genotype&nbsp;list&nbsp;from&nbsp;a&nbsp;dataframe<br>
Parameters<br>
----------<br>
dataframe:&nbsp;dataframe<br>
Description<br>
-----------<br>
From&nbsp;the&nbsp;dataframe&nbsp;the&nbsp;phased&nbsp;genotype&nbsp;frequency&nbsp;columns&nbsp;are&nbsp;extracted.&nbsp;For&nbsp;each&nbsp;row&nbsp;the&nbsp;value&nbsp;of&nbsp;the&nbsp;counter&nbsp;is<br>
the&nbsp;number&nbsp;of&nbsp;times&nbsp;the&nbsp;phased&nbsp;genotype&nbsp;is&nbsp;appended&nbsp;to&nbsp;the&nbsp;list.&nbsp;This&nbsp;runs&nbsp;through&nbsp;each&nbsp;phased&nbsp;genotype&nbsp;column.<br>
Returns<br>
-------<br>
Genotype&nbsp;list</tt></dd></dl>
 <dl><dt><a name="-haplotype_diversity"><strong>haplotype_diversity</strong></a>(haplotypelist)</dt><dd><tt>Calculates&nbsp;haplotype&nbsp;diversity<br>
Parameters<br>
----------<br>
haplotypelist:&nbsp;list<br>
Description<br>
-----------<br>
Converts&nbsp;the&nbsp;haplotype&nbsp;list&nbsp;into&nbsp;a&nbsp;haplotype&nbsp;array.&nbsp;The&nbsp;haplotype&nbsp;array&nbsp;is&nbsp;inserted&nbsp;in&nbsp;the&nbsp;haplotype&nbsp;diversity<br>
function&nbsp;from&nbsp;SciKit&nbsp;Allel.<br>
Returns<br>
-------<br>
Single&nbsp;haplotype&nbsp;diversity&nbsp;value</tt></dd></dl>
 <dl><dt><a name="-haplotype_list"><strong>haplotype_list</strong></a>(dataframe)</dt><dd><tt>Produces&nbsp;a&nbsp;haplotype&nbsp;list&nbsp;from&nbsp;a&nbsp;dataframe<br>
Parameters<br>
----------<br>
dataframe:&nbsp;dataframe<br>
Description<br>
-----------<br>
From&nbsp;the&nbsp;dataframe&nbsp;the&nbsp;phased&nbsp;genotype&nbsp;frequency&nbsp;columns&nbsp;are&nbsp;extracted.&nbsp;For&nbsp;each&nbsp;row&nbsp;the&nbsp;value&nbsp;of&nbsp;the&nbsp;counter&nbsp;is<br>
the&nbsp;number&nbsp;of&nbsp;times&nbsp;the&nbsp;phased&nbsp;genotype&nbsp;is&nbsp;appended&nbsp;to&nbsp;the&nbsp;list.&nbsp;Both&nbsp;the&nbsp;alleles&nbsp;are&nbsp;appended&nbsp;to&nbsp;the&nbsp;haplotype&nbsp;list.<br>
This&nbsp;runs&nbsp;through&nbsp;each&nbsp;phased&nbsp;genotype&nbsp;column.<br>
Returns<br>
-------<br>
Haplotype&nbsp;list</tt></dd></dl>
 <dl><dt><a name="-hudson_FST"><strong>hudson_FST</strong></a>(pop1_genotype_list, pop2_genotype_list)</dt><dd><tt>Calculates&nbsp;Hudson&nbsp;FST<br>
Parameters<br>
----------<br>
pop1_genotype_list:&nbsp;list<br>
pop2_genotype_list:&nbsp;list<br>
Description<br>
-----------<br>
Converts&nbsp;the&nbsp;genotype&nbsp;lists&nbsp;for&nbsp;both&nbsp;populations&nbsp;into&nbsp;a&nbsp;genotype&nbsp;arrays&nbsp;and&nbsp;extracts&nbsp;the&nbsp;allele&nbsp;counts.&nbsp;Using&nbsp;the<br>
hudson&nbsp;fst&nbsp;function&nbsp;from&nbsp;SciKit&nbsp;Allel&nbsp;the&nbsp;numerator&nbsp;and&nbsp;denominator&nbsp;values&nbsp;are&nbsp;extracted.&nbsp;If&nbsp;the&nbsp;denominator&nbsp;value<br>
is&nbsp;0,&nbsp;then&nbsp;the&nbsp;FST&nbsp;value&nbsp;is&nbsp;returned&nbsp;as&nbsp;0.&nbsp;Otherwise,&nbsp;FST&nbsp;is&nbsp;calculated&nbsp;by&nbsp;dividing&nbsp;the&nbsp;sum&nbsp;of&nbsp;the&nbsp;numerator&nbsp;and<br>
denominator.&nbsp;If&nbsp;NaN&nbsp;is&nbsp;returned&nbsp;then&nbsp;the&nbsp;FST&nbsp;value&nbsp;is&nbsp;returned&nbsp;as&nbsp;0.<br>
Returns<br>
-------<br>
Single&nbsp;Hudson&nbsp;FST&nbsp;value</tt></dd></dl>
 <dl><dt><a name="-nuc_div_sliding"><strong>nuc_div_sliding</strong></a>(dataframe, window_size)</dt><dd><tt>Using&nbsp;a&nbsp;dataframe&nbsp;and&nbsp;window&nbsp;size&nbsp;as&nbsp;input,&nbsp;outputs&nbsp;a&nbsp;list&nbsp;of&nbsp;nucleotide&nbsp;diversity&nbsp;values&nbsp;for&nbsp;each&nbsp;window<br>
Parameters<br>
----------<br>
dataframe:&nbsp;a&nbsp;pandas&nbsp;dataframe,&nbsp;created&nbsp;using&nbsp;the&nbsp;python&nbsp;pandas&nbsp;library.<br>
window_size:&nbsp;int<br>
Description<br>
-----------<br>
Recieves&nbsp;2&nbsp;parameters,&nbsp;a&nbsp;pandas&nbsp;dataframe&nbsp;and&nbsp;a&nbsp;window_size.&nbsp;Using&nbsp;the&nbsp;window_size&nbsp;integer,&nbsp;the&nbsp;dataframe&nbsp;is&nbsp;subset&nbsp;into&nbsp;windows&nbsp;and&nbsp;the&nbsp;nucleotide&nbsp;diversity&nbsp;is&nbsp;calculated&nbsp;across&nbsp;the&nbsp;window.<br>
Calculating&nbsp;nucleotide&nbsp;diversity&nbsp;for&nbsp;the&nbsp;windows&nbsp;uses&nbsp;the&nbsp;pre-written&nbsp;functions&nbsp;<a href="#-genotype_list">genotype_list</a>()&nbsp;and&nbsp;<a href="#-nucleotide_diversity">nucleotide_diversity</a>().<br>
This&nbsp;function&nbsp;depends&nbsp;on&nbsp;the&nbsp;python&nbsp;packages/modules&nbsp;scikit-allel,&nbsp;pandas&nbsp;and&nbsp;math.<br>
Returns<br>
-------<br>
A&nbsp;list&nbsp;of&nbsp;nucleotide&nbsp;diversity&nbsp;values&nbsp;calculated&nbsp;for&nbsp;each&nbsp;window.</tt></dd></dl>
 <dl><dt><a name="-nucleotide_diversity"><strong>nucleotide_diversity</strong></a>(genotype_list, start, end)</dt><dd><tt>Calculates&nbsp;nucleotide&nbsp;diversity<br>
Parameters<br>
----------<br>
genotype_list:&nbsp;list<br>
start:&nbsp;int<br>
end:&nbsp;int<br>
Description<br>
-----------<br>
Converts&nbsp;the&nbsp;genotype&nbsp;list&nbsp;into&nbsp;a&nbsp;genotype&nbsp;array&nbsp;and&nbsp;extracts&nbsp;the&nbsp;allele&nbsp;counts.&nbsp;Using&nbsp;the&nbsp;start&nbsp;and&nbsp;end&nbsp;genomic<br>
position&nbsp;inputs&nbsp;a&nbsp;variant&nbsp;position&nbsp;list&nbsp;is&nbsp;produced.&nbsp;Using&nbsp;the&nbsp;sequence&nbsp;diversity&nbsp;function&nbsp;from&nbsp;SciKit&nbsp;Allel<br>
the&nbsp;variant&nbsp;position&nbsp;and&nbsp;allele&nbsp;counts&nbsp;are&nbsp;inserted.<br>
Returns<br>
-------<br>
Single&nbsp;nucleotide&nbsp;diversity&nbsp;value</tt></dd></dl>
</td></tr></table>
</body></html>
