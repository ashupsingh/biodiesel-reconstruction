"""New reconstruction, 2026-10-23. Demo inputs are synthetic, not historical results."""
def mass_recovery(feedstock_g, separated_product_g):
    if feedstock_g<=0 or separated_product_g<0:raise ValueError('Invalid masses')
    return 100*separated_product_g/feedstock_g
def compare_consumption(reference_g_per_hour,candidate_g_per_hour):
    if reference_g_per_hour<=0 or candidate_g_per_hour<0:raise ValueError('Invalid rates')
    return 100*(reference_g_per_hour-candidate_g_per_hour)/reference_g_per_hour
def demo():
    assert mass_recovery(100,80)==80
    return {'synthetic_mass_recovery_percent':mass_recovery(100,80),'not_chemical_conversion_or_purity':True,'no_engine_test_performed':True}

if __name__ == "__main__":
    import json
    print(json.dumps(demo(), indent=2))
