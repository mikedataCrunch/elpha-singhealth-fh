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


cvd_terms = [
    "Stroke",
    "Cerebral Infarction",
    "Hemorrhagic Stroke",
    "Ischemic Stroke",
    "Transient Ischemic Attack",
    "Cerebral Hemorrhage",
    "Subarachnoid Hemorrhage",
    "Intracerebral Hemorrhage",
    "Brain Aneurysm",
    "Cerebral Aneurysm",
    "Arteriovenous Malformation",
    "Cerebral Venous Thrombosis",
    "Cerebral Venous Sinus Thrombosis",
    "Carotid Stenosis",
    "Vertebrobasilar Insufficiency",
    "Moyamoya Disease",
    "Lacunar Stroke",
    "Cerebral Arteriosclerosis",
    "Carotid Artery Dissection",
    "Cerebral Vasculitis",
    "Cerebral Embolism",
    "Vascular Dementia",
    "Hypertensive Encephalopathy",
    "Carotid Endarterectomy",
    "Stroke Rehabilitation",
    "Cerebrovascular Accident",
    "Cerebrovascular Occlusion"
]

cvd_procedure_terms = [
    "Coronary Artery Bypass Graft (CABG)",
    "Percutaneous Coronary Intervention (PCI)",
    "Angioplasty",
    "Stent Placement",
    "Cardiac Catheterization",
    "Electrophysiological Study",
    "Pacemaker Insertion",
    "Implantable Cardioverter Defibrillator (ICD) Placement",
    "Transcatheter Aortic Valve Replacement (TAVR)",
    "Carotid Endarterectomy",
    "Aneurysm Repair",
    "Endovascular Repair of Aorta",
    "Thrombectomy",
    "Thrombolysis",
    "Echocardiography",
    "Cardiac MRI",
    "Cardiac Stress Testing",
    "Holter Monitoring",
    "Electrocardiogram (ECG or EKG)",
    "Loop Recorder Implantation",
    "Pulmonary Thromboendarterectomy",
    "Vascular Scaffolding",
    "Cardiac Resynchronization Therapy (CRT)",
    "Left Ventricular Assist Device (LVAD) Implantation",
    "Heart Transplant"
]


chd_terms = [
    "Atrial Septal Defect",
    "Ventricular Septal Defect",
    "Tetralogy of Fallot",
    "Patent Ductus Arteriosus",
    "Coarctation of the Aorta",
    "Transposition of the Great Arteries",
    "Hypoplastic Left Heart Syndrome",
    "Pulmonary Atresia",
    "Tricuspid Atresia",
    "Total Anomalous Pulmonary Venous Return",
    "Ebstein's Anomaly",
    "Double Outlet Right Ventricle",
    "Aortic Valve Stenosis",
    "Pulmonary Valve Stenosis",
    "Bicuspid Aortic Valve",
    "Congenital Mitral Valve Anomalies",
    "Single Ventricle Defects",
    "Endocardial Cushion Defect",
    "Mitral Valve Prolapse",
    "Anomalous Pulmonary Venous Connection",
    "Interrupted Aortic Arch",
    "Atrioventricular Septal Defect",
    "Congenital Aortic Valve Insufficiency",
    "Congenital Pulmonary Valve Insufficiency",
    "Right Hypoplastic Heart Syndrome",
    "Left Hypoplastic Heart Syndrome",
    "Congenital Tricuspid Valve Stenosis",
    "Congenital Tricuspid Valve Insufficiency",
    "Subaortic Stenosis",
    "Supravalvular Aortic Stenosis",
    "Cor Triatriatum",
    "Pulmonary Artery Stenosis",
    "Pulmonary Artery Atresia",
    "Anomalous Left Coronary Artery From the Pulmonary Artery",
    "Anomalous Right Coronary Artery From the Pulmonary Artery",
    "Coronary Artery Anomaly",
    "Dextrocardia",
    "Eisenmenger Syndrome",
    "Mitral Atresia",
    "Double Inlet Left Ventricle",
    "Double Inlet Right Ventricle",
    "Uhl's Anomaly",
    "Heterotaxy Syndrome",
    "Congenital Heart Block",
    "L-transposition of the great arteries",
    "D-transposition of the great arteries",
    "Shone's Complex",
    "Heart Malformation",
    "Heart Defects, Congenital",
    "Congenital Cardiovascular Anomaly"
]

chd_procedure_terms = [
    "Heart Valve Replacement",
    "Heart Valve Repair",
    "Atrial or Ventricular Septal Defect Repair",
    "Transcatheter Aortic Valve Replacement (TAVR)",  # Also used in CVD
    "Echocardiography",  # Also used in CVD
    "Cardiac Catheterization",  # Also used in CVD
    "Electrophysiological Study",  # Also used in CVD
    "Pacemaker Insertion",  # Also used in CVD for arrhythmias that can be congenital
    "Implantable Cardioverter Defibrillator (ICD) Placement",  # Also used in CVD
    "Cardiac MRI",  # Also used in CVD
    "Heart Transplant"  # Also used in severe CHD cases
]

physical_exam_xa_terms = [
    # Xanthomas
    "Achilles Tendinous Xanthomas",
    "Achilles tendon xanthoma",
    "Cutaneous Xanthomas",
    "Nodular Achilles Tendons",
    "Palmar Xanthomas",
    "Palpable Xanthomas",
    "Possible Tendon Xanthom",
    "Tendinous Xanthoma",
    "Tendinous Xanthomas",
    "Tendinous Xanthomata",
    "Tendon Xanthoma",
    "Tendon Xanthomas",
    "Tendon Xanthomata",
    "Thickened Achilles Tendon",
    "Thickening Of Achilles Tendon",
    "Tuberoeruptive Xanthomas",
    "Tuberous Xanthomas",
    "Xanthomas",
    "Xanthomas Of Achilles Tendon",
    "Xanthomas Of The Hands",
    "Xanthomas On The Extensor Surfaces",
]

physical_exam_ca_terms = [
    # corneal arcus
    "Corneal arcus",
    "Arcus cornealis",
    "Early arcus senilis",
]

physical_exam_exclude_terms = [
    "Eruptive xanthomas",
    "Irruptive xanthomas",
    "Xanthomas around both eyes",
    "Xanthomas around the left eye",
    "Xanthomas around the right eye",
    "Eyelid xanthomas",
    "Eye lid xanthomas",
    "Xanthomas on the eye",
    "Xanthomas over eyelids",
    "Xanthomas over the eyes",
    "Xanthomas over both eyelids",
    "Xanthomas on the upper lids",
    "Xanthomas beneath both eyes",
    "Xanthomas beneath eye(s)",
    "Xanthomas beneath eyelid",
    "Xanthomas on the face",
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