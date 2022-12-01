-- (1)

INSERT INTO Doctors 
VALUES ('Timsi', 'Muttreja', 'Optometrist', 'OD','Dr. Timsi Muttreja is a compassionate optometrist driven to provide exceptional care to her patients in New York. Dr. Muttreja earned her Bachelor''s degree in Chemistry from SUNY Oswego. She received her Doctorate of Optometry from IAUPR School of Optometry, where she received the Award for Clinical Excellence. Dr. Muttreja provides comprehensive eye examinations and manages various ocular diseases including, but not limited to, dry eyes, cataracts, glaucoma and corneal related problems. She is fluent in Hindi, Punjabi, and Spanish. In her free time, Dr. Muttreja enjoys traveling, art and spending time with her family',
 '1669143079', 'https://d1k13df5m14swc.cloudfront.net/photos/Dr-Timsi-Muttreja-OD-353436-circle_large__v1__.png', 4.5, 'Universidad Interamericana de Puerto Rico', 32, '2128475075',
 {'dry eyes', 'cataracts', 'glaucoma', 'Annual Eye Exam', 'Contact Lenses', 'Eye Infection', 'General Eye Consultation'});

INSERT INTO Hospitals
VALUES ('Eyes on Park', '287 Park Ave South, New York, NY 10010', '110112', '3323452363');

INSERT INTO Medical_Issues
VALUES ('Optometrist','A practitioner who provides primary eye and vision care, performs eye examinations to detect vision problems, and prescribes corrective lenses to correct those problems.');

INSERT INTO Works_At
VALUES ('1669143079', '110112');

INSERT INTO Specializes_In
VALUES ('1669143079', 'Optometrist');

-- (2)

INSERT INTO Doctors
VALUES ('Ellen', 'Edgar', 'Neurologist', 'MD',
'Located in the heart of Forrest Hills, Dr. Ellen Edgar is a leading board certified neurologist and board certified neurophysiologist. Dr. Edgar specializes in treatment of muscular skeletal pain, eplilepsy and other types of neurological conditions including all types of headaches such as Botox injections for treatment of refractory migranes, cyrvical dystonya and other types of movement disorder.',
'1326343625', 'https://d1k13df5m14swc.cloudfront.net/12493154-7705-4933-aca0-3901e9ac3e6bzoom.jpg',
4.3, 'Andizhan State Medical Institute', 23, '8002008196',
{'Back Pain', 'Headache', 'Migraine', 'Neurology Consultation', 'Sleep Problems', 'Neuromuscular Disorders', 'Spasticity Management'});

INSERT INTO Hospitals
VALUES ('Complete Neurological Care', '11247 Queens Blvd, Forest Hills, NY 11375', '120023', '8002008196');

INSERT INTO Medical_Issues
VALUES ('Neurologist', 'A physician who specializes in the diagnosis and treatment of disorders of the nervous system.');

INSERT INTO Works_At
VALUES ('1326343625', '120023');

INSERT INTO Specializes_In
VALUES ('1326343625', 'Neurologist');

-- (3)

INSERT INTO Doctors
VALUES ('Howard', 'Shaw', 'OB-GYN', 'MD',
'Dr. Howard Shaw has been a practicing Obstetrician and Gynecologist since 1995. He graduated Cum Laude from Rutgers in 1987 where he earned his bachelor''s degree in biological science.',
'1255379509', 'https://d2uur722ua7fvv.cloudfront.net/0e991dfc-cbe6-4e49-a923-6ecd82bb2ff9zoom.jpg',
4.71, 'State University of New York', 13, '2125179048',
{'Pap smear irregularities', 'annual check ups', 'pre and post- menopausal symptoms', 'obstetrics', 'gynecology'});

INSERT INTO Hospitals
VALUES ('ROSH Maternal', '115 East 67th St, New York, NY 10065', '552304', '2122493949');

INSERT INTO Medical_Issues
VALUES ('Gynecologist', 'A physician who specializes in treating diseases of the female reproductive organs and providing well-woman health care that focuses primarily on the reproductive organs.');

INSERT INTO Works_At
VALUES ('1255379509', '552304');

INSERT INTO Specializes_In
VALUES ('1255379509', 'Gynecologist');

-- (4)

INSERT INTO Doctors
VALUES ('Jed', 'Kaminetsky', 'Urologist', 'MD',
'Dr. Jed Kaminetsky, M.D. is a Clinical Associate Professor at New York University Medical Center, and is a practicing urologist with University Urology Associates, one of the largest urologic practices in the New York City metropolitan area. He is a board certified urologist and is highly skilled in treating all urologic disorders, performing minimally invasive prostate surgeries and penile implants. Dr. Kaminetsky’s academic interests include the study of both male and female sexual dysfunction, which has led him to become a national and world thought leader.',
'1952378598', 'https://d2uur722ua7fvv.cloudfront.net/photos/Dr-Jed-Kaminetsky-MD-48127-circle_large__v1__.png',
4.75, 'New York University', 55, '2126869015',
{'benign prostatic hyperplasia', 'erectile dysfunction', 'low testosterone', 'vasectomy', 'Incontinence', 'Sexually Transmitted Disease (STD)', 'Urinary Tract Infection (UTI)'});

INSERT INTO Hospitals
VALUES ('University Urology', '215 Lexington Avenue 21st Floor, New York, NY 10016', '445923', '2126869015');

INSERT INTO Medical_Issues
VALUES ('Urologist', 'A physician who specializes in diseases of the urinary organs in females and the urinary and sex organs in males.');

INSERT INTO Works_At
VALUES ('1952378598', '445923');

INSERT INTO Specializes_In
VALUES ('1952378598', 'Urologist');

-- (5)

INSERT INTO Doctors
VALUES ('Sameh', 'Elguizaoui', 'Orthopedic Surgeon', 'MD',
'Sameh Elguizaoui, M.D. is a fellowship trained orthopedic surgeon who specializes in sports medicine and arthroscopic surgery as well as the treatment of general orthopedic injuries and trauma. In addition to his clinical interest in shoulder and knee disorders, Dr. Elguizaoui has a focused specialization on joint preservation and treatment of arthritis in young active patients with current regenerative medicine and cartilage repair and transplant techniques, as well as biologic alternatives to surgery.',
'1568755460', 'https://d2uur722ua7fvv.cloudfront.net/photos/Dr-Sameh-Elguizaoui-MD-236423-circle_large__v2__.png',
4.80, 'Ohio State University', 121, '2127373301',
{'Cartilage Repair', 'Joint preservation', 'Arthroscopy of the shoulder, elbow, knee and ankle', 'ACL and ligament injuries of the knee', 'Cartilage repair and joint preservation', 'Cartilage transplantation', 'Meniscal tears', 'Meniscal transplantation', 'Shoulder instability and labral tears', 'Rotator cuff tears'});

INSERT INTO Hospitals
VALUES ('NY Orthopedics', '159 E 74th St, New York, NY 10021', '330020', '2127373301');

INSERT INTO Medical_Issues
VALUES ('Orthopedist', 'A doctor who corrects congenital or functional abnormalities of the bones with surgery, casting, and bracing. Orthopedists also treat injuries to the bones.');

INSERT INTO Works_At
VALUES ('1568755460', '330020');

INSERT INTO Specializes_In
VALUES ('1568755460', 'Orthopedist');

-- (6)

INSERT INTO Doctors
VALUES ('Saleh', 'Rachidi', 'Dermatologist', 'MD',
'Dr. Saleh Rachidi is a leading NYC dermatologist at Dermatology, Laser and Surgery of Flatiron, specializing in laser skin resurfacing and rejuvenation, body contouring, skin tightening, injectables, laser hair removal, vein treatments, hair loss treatments, and personalized skin care. Dr. Rachidi offers the latest cosmetic treatments and procedures. Patients trust Dr. Rachidi’s expertise because he consistently provides high-quality care that leads to positive and lasting health outcomes. Dr. Rachidi graduated from the Medical University of South Carolina (MUSC), where he received both his MD and PhD degrees. During his time at MUSC, he earned the Distinguished Graduate of the Year award and was inducted into the Alpha Omega Alpha Honor Medical Society. For his postgraduate training, Dr. Rachidi completed his residency in dermatology at Johns Hopkins University. He then finished his fellowship training in cosmetic dermatologic surgery. During his postgraduate training, Dr. Rachidi received awards from the Society of Investigative Dermatology, the American Society for Dermatologic Surgery, and the American Society for Laser Medicine and Surgery, and also received a research grant from the Center for Clinical Data Analysis. He is pleased to bring his dermatologic expertise to Dermatology, Laser and Surgery of Flatiron.',
'1447609615', 'https://d1k13df5m14swc.cloudfront.net/457ac590-bf0a-4695-8277-e5c48699c5d1zoom.jpg',
4.61, 'Medical University of South Carolina', 3, '8443376362',
{'Acne', 'Allergy Consultation', 'Annual Skin Screening', 'Dermatology Consultation', 'Sexually Transmitted Disease (STD)', 'laser skin resurfacing and rejuvenation', 'body contouring', 'skin tightening', 'injectables', 'laser hair removal', 'vein treatments', 'hair loss treatments', 'personalized skin care'});

INSERT INTO Hospitals
VALUES ('Dermatology Laser & Surgery of Carnegie Hill PLLC', '1095 Park Ave New York, NY 10128', '310254', '6466616131');

INSERT INTO Medical_Issues
VALUES ('Dermatologist','A physician who specializes in the diagnosis and treatment of skin problems.');

INSERT INTO Works_At
VALUES ('1447609615', '310254');

INSERT INTO Specializes_In
VALUES ('1447609615', 'Dermatologist');

-- (7)

INSERT INTO Doctors
VALUES ('Daniel', 'Demesh', 'Ear, Nose & Throat Doctor', 'MD',
'Daniel Demesh, MD is a member of the Facial Plastic and Reconstructive Surgery and Ear, Nose, and Throat (ENT) teams. Dr. Demesh is a fellowship-trained facial plastic surgeon specializing in facial and neck rejuvenation.',
'1629485586', 'https://d2uur722ua7fvv.cloudfront.net/f9bdb3a4-4b91-4a55-9ed8-9d1168975235zoom.jpg',
4.62, 'Albert Einstein College of Medicine of Yeshiva University', 8, '6465937200',
{'face-lifts', 'nose reshaping', 'eyelid surgery', 'chronic sinusitis', 'nasal congestion', 'deviated septum', 'nasal polyps', 'turbinate hypertrophy', 'chronic rhinitis'});

INSERT INTO Hospitals
VALUES ('Summit Health - New York', '1865 Broadway New York, NY 10023', '237789', '6465937200');

INSERT INTO Medical_Issues
VALUES ('Ear, Nose & Throat Doctor', 'Otolaryngologists are physicians uniquely trained in the surgical and medical treatment of patients with disorders and diseases of ear, nose, throat (ENT).');

INSERT INTO Works_At
VALUES ('1629485586', '237789');

INSERT INTO Specializes_In
VALUES ('1629485586', 'Ear, Nose & Throat Doctor');

-- (8)

INSERT INTO Doctors
VALUES ('Jaskaran', 'Grewal', 'Psychiatrist', 'MD',
'Expert in treating all psychiatric conditions. Employ a targeted approach utilizing the biopsychosocial model to target appropriate medications, and utilized the appropriate therapy for mental well being. Years of success in treating the most refractory of cases. We work together to form the strongest therapeutic alliance so you can be well. 10 years of experience managing all psychiatric conditions. Excellence and mastery of psychopharmacology and drug interactions. Successfully have treated the most difficult and refractory of all psychiatric pathologies. Will see patients on weekends. Let''s get you better together! We''ll work to treat you together and then maintain the success as we strive for new heights across the board!',
'1053808535', 'https://d3wnzga3fpd9a.cloudfront.net/96ee66ad-1b17-462c-b97f-277bd65421b9zoom.jpg',
4.93, 'American University of Antigua College of Medicine', 39, '6468498413',
{'Anxiety', 'Depression', 'Hyperactive Disorder (ADD, ADHD)', 'Prescription and Refill', 'Psychiatry Consultation'});

INSERT INTO Hospitals
VALUES ('NYC Psychiatric Associates', '353 Lexington Ave New York, NY 10016', '900021', '9173910076');

INSERT INTO Medical_Issues
VALUES ('Psychiatrist', 'A physician who specializes in the prevention, diagnosis, and treatment of mental illness. Psychiatrist can prescribe medication.');

INSERT INTO Works_At
VALUES ('1053808535', '900021');

INSERT INTO Specializes_In
VALUES ('1053808535', 'Psychiatrist');

-- (9)

INSERT INTO Doctors
VALUES ('Anna', 'Kezerashvili', 'Cardiologist', 'MD',
'Anna Kezerashvili, MD, FACC is a caring and dedicated cardiologist serving the community of Bronx and New York, NY. Dr. Kezerashvili attended the Albert Einstein College of Medicine of Yeshiva University, where she received her MD with HONORS and completed her residency in internal medicine at the same university. She completed a fellowship in cardiology at Winthrop-University Hospital. Dr. Kezerashvili is a part of KezMed Medical PC. She is board certified in internal medicine and cardiovascular disease by the American Board of Internal Medicine.',
'1245528975', 'https://d1k13df5m14swc.cloudfront.net/92f5b50c-edac-41dc-9219-f53e7890b521zoom.jpg',
4.71, 'Albert Einstein College of Medicine of Yeshiva University', 43, '6465308447',
{'Vascular Interpretations (RPVI)', 'aortic aneurysm', 'venous insufficiency', 'varicose veins', 'peripheral arterial disease'});

INSERT INTO Hospitals
VALUES ('KezMed Medical PC', '1963 Williamsbridge Rd Bronx, NY 10461', '323276', '6465308447');

INSERT INTO Medical_Issues
VALUES ('Cardiologist', 'A physician who specializes in treating heart disorders.');

INSERT INTO Works_At
VALUES ('1245528975', '323276');

INSERT INTO Specializes_In
VALUES ('1245528975', 'Cardiologist');

-- (10)

INSERT INTO Doctors
VALUES ('Purvi', 'Parikh', 'Allergist', 'MD',
'Dr. Purvi Parikh is an allergist with a specialization in pediatric allergies. She works with Allergy and Asthma Associates of Murray Hill at their Hauppauge, New York, Forest Hills, and Huntington, NY locations. Patients visit Dr. Parikh to seek treatment for concerns and conditions, such as hives, hay fever, asthma, drug allergies, and eczema. She strives to stay updated with technological advancements in medicine to incorporate them into her treatment plans. Dr. Parikh earned her medical degree from the St. George''s University School of Medicine. She has been certified by the American Board of Allergy and Immunology and the American Board of Internal Medicine.',
'1629212592', 'https://d1k13df5m14swc.cloudfront.net/bba7ccdc-113d-46e7-94e3-0bea1f76fe18zoom.jpg',
4.63, 'St. George''s University School of Medicine', 15, '7182612661',
{'Infectious Disease Allergy', 'Immunology', 'Pediatric Allergy', 'allergy', 'asthma', 'common variable immunodeficiency', 'hives', 'hay fever'});

INSERT INTO Hospitals
VALUES ('Allergy and Asthma Associates of Murray Hill', '161 Madison Ave New York, NY 10016', '458099', '2126854225');

INSERT INTO Medical_Issues
VALUES ('Allergist', 'An allergist is a physician who specializes in the diagnosis and treatment of asthma and other allergic diseases.');

INSERT INTO Works_At
VALUES ('1629212592', '458099');

INSERT INTO Specializes_In
VALUES ('1629212592', 'Allergist');

--(1)

INSERT INTO StudentPatients
VALUES ('Aysha', 'Jamal', 'aj2604', 'cucumber', 23, 'SEAS');

INSERT INTO Saves
VALUES ('aj2604', '1568755460');

INSERT INTO Saves
VALUES ('aj2604', '1255379509');

INSERT INTO Appointments -- Past
VALUES (5, '2022-02-01', '9:00:00', 'Injured knee while playing basketball');

INSERT INTO Schedules
VALUES ('1568755460', '330020', 5, 'aj2604');

INSERT INTO Reviews
VALUES (5, '2022-02-01', 'Awesome experience! Great staff and Doctor. Highly recommend!', 5);

INSERT INTO Writes -- date review written
VALUES ('1568755460', 'aj2604', 5, '2022-02-13');

INSERT INTO Appointments -- Future
VALUES (7, '2023-02-01', '9:00:00', 'Pre-surgery information');

INSERT INTO Schedules
VALUES ('1568755460', '330020', 7, 'aj2604');

--(2)

INSERT INTO StudentPatients
VALUES ('Anoushka', 'Thakre', 'at3144', 'pineapple', 22, 'GS');

INSERT INTO Saves
VALUES ('at3144', '1952378598');

INSERT INTO Appointments -- Future
VALUES (6, '2022-12-22', '16:00:00', 'UTI followup');

INSERT INTO Schedules
VALUES ('1952378598', '445923', 6, 'at3144');

--(3)

INSERT INTO StudentPatients
VALUES ('Bridget', 'Jones', 'bj1213', 'orange', 26, 'College');

INSERT INTO Saves
VALUES ('bj1213', '1952378598');

INSERT INTO Appointments -- Past
VALUES (3, '2021-02-15', '14:00:00', 'Checkup');

INSERT INTO Schedules
VALUES ('1255379509', '552304', 3, 'bj1213');

INSERT INTO Reviews
VALUES (3, '2021-02-15', 'Although I waited over an hour and half to be seen by the doctor they were friendly and informative regarding my injury.', 3);

INSERT INTO Writes -- date review written
VALUES ('1255379509', 'bj1213', 3, '2021-02-20');

INSERT INTO Appointments -- Past
VALUES (4, '2021-10-22', '16:00:00', 'UTI');

INSERT INTO Schedules
VALUES ('1952378598', '445923', 4, 'bj1213');

INSERT INTO Reviews
VALUES (4, '2021-10-22', 'It was a great experience. The staff was really friendly and the Doctor went straight to the point. I would recommend.', 4);

INSERT INTO Writes -- date review written
VALUES ('1952378598', 'bj1213', 4, '2021-10-23');

--(4)

INSERT INTO StudentPatients
VALUES ('Amelie', 'Maxwell', 'am6783', 'pickle', 18, 'SEAS');

INSERT INTO Saves
VALUES ('am6783', '1326343625');

INSERT INTO Appointments -- Past
VALUES (2, '2022-07-10', '6:00:00', 'Extremely painful headaches.');

INSERT INTO Schedules 
VALUES ('1326343625', '120023', 2, 'am6783');

INSERT INTO Reviews -- date visited
VALUES (2, '2022-07-10', 'They did not review my X-ray with me, they didn’t send the prescription when they were supposed to, and they were very busy.', 1);

INSERT INTO Writes -- date review written
VALUES ('1326343625', 'am6783', 2, '2022-10-18');

--(5)

INSERT INTO StudentPatients
VALUES ('Michael', 'Jordan', 'mj4112', 'umbrella', 20, 'College');

INSERT INTO Appointments -- Past
VALUES (1, '2022-10-10', '12:00:00', 'Weak eyes. Blurry vision. Need new prescription.');

INSERT INTO Schedules
VALUES ('1669143079', '110112', 1, 'mj4112');

INSERT INTO Reviews -- date visited
VALUES (1, '2022-10-10', 'Overall, very welcoming office with friendly staff that provided clear instructions and were able to answer my questions.', 5);

INSERT INTO Writes -- date review written
VALUES ('1669143079', 'mj4112', 1, '2022-10-15');

--(6)

INSERT INTO StudentPatients
VALUES ('Umaymah', 'Imran', 'ui2733', 'cookies', 24, 'Barnard');

INSERT INTO Saves
VALUES ('ui2733', '1447609615');

INSERT INTO Saves
VALUES ('ui2733', '1629212592');

INSERT INTO Saves
VALUES ('ui2733', '1629485586');

INSERT INTO Appointments
VALUES (8, '2021-12-14', '13:00:00', 'Rashed skin around arm folds');

INSERT INTO Schedules -- Past
VALUES ('1447609615', '310254', 8, 'ui2733');

INSERT INTO Reviews
VALUES (6, '2021-12-14', 
'Very clear in explaining everything. Very smart but not arrogant. Very thorough. Nice staff. Clean office. Nice staff', 4);

INSERT INTO Writes
VALUES ('1447609615', 'ui2733', 6, '2022-01-03');

INSERT INTO Appointments
VALUES (9, '2022-09-19', '11:35:00', 'Left ear feels clogged');

INSERT INTO Schedules -- Past
VALUES ('1629485586', '237789', 9, 'ui2733');

INSERT INTO Reviews
VALUES (7, '2022-09-19', 
'Efficiently addressed my concerns. Physician''s assistant was very thorough in discussing symptoms and prior history.', 5);

INSERT INTO Writes
VALUES ('1629485586', 'ui2733', 7, '2022-10-01');


--(7)

INSERT INTO StudentPatients
VALUES ('Natalie', 'Smith', 'ns3746', 'jellybean', 19, 'SEAS');

INSERT INTO Saves
VALUES ('ns3746', '1053808535');

INSERT INTO Appointments 
VALUES (10, '2022-03-01', '13:00:00', 'Feeling very anxious with increasing work load');

INSERT INTO Schedules -- Past
VALUES ('1053808535', '900021', 10, 'ns3746');

INSERT INTO Reviews
VALUES (8, '2022-03-01', 
'They made me feel safe about the choices I made from their options. They kindly gave thorough explanations and thoughtful comments. Also, they made sure I had all my questions answered.', 5);

INSERT INTO Writes
VALUES ('1053808535', 'ns3746', 8, '2022-03-03');

INSERT INTO Appointments
VALUES (14, '2022-12-22', '14:45:00', 'Non-stop sneezing during pollen season');

INSERT INTO Schedules -- Future
VALUES ('1629212592', '458099', 14, 'ns3746');

--(8)

INSERT INTO StudentPatients
VALUES ('Alex', 'Joshi', 'aj8032', 'airpods', 20, 'College');

INSERT INTO Appointments
VALUES (12, '2022-09-01', '10:45:00', 'Face swollen after having peanuts');

INSERT INTO Schedules -- Past
VALUES ('1629212592', '458099', 12, 'aj8032');

INSERT INTO Reviews
VALUES (10, '2022-09-01', 
'I was seen immediately and they took the time to address my concerns. Thrilled to have found such a great doctor with great bedside manner that has availability.', 4);

INSERT INTO Writes
VALUES ('1629212592', 'aj8032', 10, '2022-09-21');

--(9)

INSERT INTO StudentPatients
VALUES ('Hasan', 'Khan', 'hk9821', 'blanket', 21, 'Barnard');

INSERT INTO Saves
VALUES ('hk9821', '1245528975');

INSERT INTO Saves
VALUES ('hk9821', '1629485586');

INSERT INTO Appointments
VALUES (11, '2022-08-10', '09:15:00', 'Observed irregular heartbeat during resting periods');

INSERT INTO Schedules -- Past
VALUES ('1245528975', '323276', 11, 'hk9821');

INSERT INTO Reviews
VALUES (9, '2022-08-10', 
'The doctor was wonderful, very kind, efficient and was able to pick up on my blood panels right away regarding a coinciding health problem I have. Very sweet front desk too!', 5);

INSERT INTO Writes
VALUES ('1245528975', 'hk9821', 9, '2022-08-18');

--(10)

INSERT INTO StudentPatients
VALUES ('Michelle', 'Coder', 'mc7456', 'purple', 18, 'SEAS');

INSERT INTO Appointments
VALUES (13, '2022-11-19', '11:15:00', 'Ear infection');

INSERT INTO Schedules -- Future
VALUES ('1629485586', '237789', 13, 'mc7456');

-- Commands:
-- psql -U aj2604 -h 34.75.94.195 -d proj1part2
-- \d (List table)
-- \i FILE (Execute file)
-- DROP TABLE studentpatients, schedules, appointments, writes, reviews, saves, doctors, hospitals, works_at, medical_issues, specializes_in CASCADE;

-- Summary: 11 Tables
-- Doctors: 10
-- Hospitals: 10
-- Medical_Issues: 10
-- Works_At: 10
-- Specializes_In: 10
-- StudentPatients: 10
-- Saves: 11
-- Schedules: 14
-- Appointments: 14
-- Reviews: 10
-- Writes: 10