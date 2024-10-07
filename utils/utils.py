# change ref_date to whatever date is needed
from datetime import datetime

def get_age(dob, fmt="%Y-%m-%d", ref_date="2024-01-01"):
    ref = datetime.strptime(ref_date, fmt)
    try:
#         dob = datetime.strptime(dob, fmt) # assumes string, not timestamp
        return ref.year - dob.year - ((ref.month,  ref.day) < (dob.month, dob.day))
    except:
        return np.nan

# insert icd10 coodes here
secondary_dia_icd10 = [
    
]

secondary_dia_snomed = [
    "121076010", # 121076010 NORMAL PREGNANCY
    "460449010", # 460449010 [V]NORMAL PREGNANCY
    "398571013", # 398571013 NORMAL PREGNANCY &/OR DELIVERY (& [SPONTANEOUS VAGINAL DELIVERY])
    "398576015", # 398576015 NORMAL PREGNANCY+DELIV.
    "78671013", # 78671013 HIGH RISK PREGNANCY
    "3006031013", # 3006031013 SUPERVISION OF HIGH RISK PREGNANCY WITH HISTORY OF PREVIOUS CAESAREAN SECTION DONE
    "2873075017", # 2873075017 HIGH RISK PREGNANCY DUE TO HISTORY OF PRETERM LABOR
    "3006012019", # 3006012019 SUPERVISION OF HIGH RISK PREGNANCY WITH HISTORY OF PREVIOUS CESAREAN SECTION DONE
    "2873076016", # 2873076016 HIGH RISK PREGNANCY DUE TO HISTORY OF PRETERM LABOUR
    "3289898015", # 3289898015 HIGH RISK PREGNANCY DUE TO RECURRENT PREGNANCY LOSS
    "3006048017", # 3006048017 SUPERVISION OF HIGH RISK PREGNANCY WITH HISTORY OF GESTATIONAL DIABETES MELLITUS DONE
    "3289849012", # 3289849012 HIGH RISK PREGNANCY DUE TO RECURRENT MISCARRIAGE
    "3006052017", # 3006052017 SUPERVISION OF HIGH RISK PREGNANCY WITH HISTORY OF PREVIOUS MOLAR PREGNANCY DONE
    "1230428012", # 1230428012 HRP - HIGH RISK PREGNANCY
    "3006041011", # 3006041011 SUPERVISION OF HIGH RISK PREGNANCY DONE
    "3006040012", # 3006040012 SUPERVISION OF HIGH RISK PREGNANCY WITH HISTORY OF PREVIOUS PRECIPITATE LABOUR DONE
    "27701016", # 27701016 MULTIPLE PREGNANCY
    "2695071019", # 2695071019 MULTIPLE PREGNANCY WITH ONE FETAL LOSS
    "106809012", # 106809012 TRIPLET PREGNANCY
    "243546014", # 243546014 TRIPLET PREGNANCY
    "2922695015", # 2922695015 DICHORIONIC DIAMNIOTIC TWIN PREGNANCY
    "108265019", # 108265019 TWIN PREGNANCY
    "2922687019", # 2922687019 MONOCHORIONIC DIAMNIOTIC TWIN PREGNANCY
    "2922690013", # 2922690013 MONOCHORIONIC TWIN PREGNANCY
    "3290185017", # 3290185017 DIZYGOTIC TWIN PREGNANCY
    "2922701014", # 2922701014 MONOCHORIONIC MONOAMNIOTIC TWIN PREGNANCY
    "411066013",  # 411066013 FH: TWIN PREGNANCY
    "3290254018", # 3290254018 MONOZYGOTIC TWIN PREGNANCY
    "243545013",  # 243545013 TWIN PREGNANCY
    "306223017",  # 306223017 TWIN PREGNANCY - DELIVERED
    "2922681018", # 2922681018 MONOCHORIONIC DIAMNIOTIC TWIN PREGNANCY WITH DISSIMILAR AMNIOTIC FLUID VOLUMES
    "3010971015", # 3010971015 CONTINUING PREGNANCY AFTER INTRAUTERINE DEATH OF TWIN FOETUS
    "2922692017", # 2922692017 MONOCHORIONIC DIAMNIOTIC TWIN PREGNANCY WITH SIMILAR AMNIOTIC FLUID VOLUMES
    "2693038016", # 2693038016 CONTINUING PREGNANCY AFTER INTRAUTERINE DEATH OF TWIN FETUS
    "306224011", # 306224011 TWIN PREGNANCY WITH ANTENATAL PROBLEM
    "2965910018", # 2965910018 FETAL OR NEONATAL EFFECT OF TWIN PREGNANCY
   
]

secondary_pregnancy_terms = [
    # General Pregnancy Terms
    "Pregnancy",
    "Gestation",
    "Prenatal",
    "Antenatal",
    
    # Stages of Pregnancy
    "First trimester",
    "Second trimester",
    "Third trimester",
    
    # Complications
    "Miscarriage",
    "Stillbirth",
    "Preterm labor",
    "Gestational diabetes",
    "Preeclampsia",
    "Eclampsia",
    "Hyperemesis gravidarum",
    "Placenta previa",
    "Placental abruption",
    "Intrauterine growth restriction",
    "Oligohydramnios",
    "Polyhydramnios"
]


llt_meds = [
    'simvastatin',
    'lovastatin',
    'pravastatin',
    'atorvastatin',
    'rosuvastatin',
    'niaspan',
    'ezetimibe',
    'evolocumab',
    'caduet',
    'atavor',
    'atocor',
    'atoris',
    'atorvon',
    'atswift',
    'beatorva',
    'eturion',
    'inatorvas',
    'lipitor',
    'torvalipin',
    'tulip',
    'lochol',
    'lovastin',
    'medostatin',
    'rovacor',
    'rovast',
    'rozat',
    'rozuva',
    'covastin',
    'ifistatin',
    'kardak',
    'priacin',
    'simlo',
    'simtin',
    'simvacor',
    'simvas',
    'simvor',
    'zocor',
    'colestyramine',
    'cholestyramine',
    'resincolestiramina',
    'alirocumab',
    'praluent',
    'repatha',
    'alvotrol',
    'ezetrol',
    'ezoleta',
    'ezzicad',
    'lipez',
    'zient',
    'zimiex',
    'inclisiran',
    'leqvio',
    'atozet',
    'lypstaplus',
    'rozevon',
    'suvezen',
    'ezetimibe-simvastatin',
    'lypstaplus',
    'valcore',
    'vytorin',
    'pravafen',
    'cholib',
    'dualpress',
    'triveram',
    'trinomia',
]

fh_snomed = [
    
]

fh_icd10 = [
    
]

# # stage 1 utils
# secondary_dia = [
#     "NORMAL PREGNANCY",
#     "HIGH RISK PREGNANCY",
#     "HIGH RISK PREGNANCY CARE,"
#     "SPECIFIED HIGH RISK PREGNANCY",
#     "POST TERM PREGNANCY", 
#     "POST-TERM PREGNANCY",
#     "POST-TERM PREGNANCY – DELIVERED",
#     "MULTIPLE GESTATION",
#     "MULTIPLE PREGNANCY",
#     "MULTIPLE PREGNANCY AFFECTING NEW BORN",
#     "TWIN PREGNANCY",
#     "TRIPLET PREGNANCY",
#     "MULTIPLE GESTATION WITH ONE OR MORE FETAL MALPRESENTATIONS",
# ]