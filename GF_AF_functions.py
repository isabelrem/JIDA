### Genotype frequency function ###


def gtfreq(GT00, GT01, GT10, GT11):
    ''' Calculates the genotype frequency based on the samples that exhibit a specific GT. The function recieves
        the count of each GT and divides it by the total sample count (which is the sum of all GT counts).
        The function assumes diploid samples. Thus, it only recieves 4 numeric inputs in the following order:
        GT 0|0, 0|1, 1|0, 1|1 in the format GT 00,01,10,11, respectively.
        Returns a dictionary with the genotype as key and the frequency as value rounded to 3 decimal places . '''

    # Calculates sample count by adding the frequency of each genotype.
    sample_count = GT00 + GT01 + GT10 + GT11

    # GT frequency for each genotype is calculated and dividied by sample_count to 3 decimal places
    gf00 = round(GT00 / sample_count, 3)
    gf01 = round(GT01 / sample_count, 3)
    gf10 = round(GT10 / sample_count, 3)
    gf11 = round(GT11 / sample_count, 3)

    # Creates a dictionary storing the genotype as key and its frequency as value
    gf_dict = {"0|0": gf00,
               "0|1": gf01,
               "1|0": gf10,
               "1|1": gf11
               }

    # Returns the dictionary
    return gf_dict


# -----------------------------------------------------------------------------------------------------------------------------------------------------------#

### Allele frequency function ###

def allefreq(GT00, GT01, GT10, GT11):
    ''' Calculates the allele frequency based on the samples that exhibit a specific GT. The function recieves
        the count of each GT, adds the corresponding allele values together and divides it by the total sample
        count (which is the sum of all GT counts).
        The function assumes diploid samples. Thus, it only recieves 4 inputs in the following order:
        GT 0|0, 0|1, 1|0, 1|1 in the format GT 00,01,10,11, respectively.
        Returns a dictionary with the allele as key and the frequency as value rounded to 3 decimal places. '''

    # Calculates sample count by adding the frequency of each genotype.
    sample_count = GT00 + GT01 + GT10 + GT11

    # Calculates allele frequency for the 0 allele to 3 decimal places
    af_0 = round(((GT00 * 2) + GT01 + GT10) / (sample_count * 2), 3)

    # Calculates allele frequency for the 1 allele to 3 decimal places
    af_1 = round(((GT11 * 2) + GT01 + GT10) / (sample_count * 2), 3)

    # Creates a dictionary with the results where key is the allele and value is the frequency
    af_dict = {
        0: af_0,
        1: af_1
    }

    return af_dict


