
# import random

# roll_numbers = [i for i in range(21100001, 21100601)]


# departments = ["humanities", 'chemistry', 'maths', 'physics', 'biology', 'economics', 'computer science', 'urdu', "English", 'Politics', 'Business Ethics']


# majors = ["Computer Science", "Mathematics", "Electrical Engineering", "Physics", "Biology", "Chemistry", "Chemical Engineering", "Civil Engineering", "Accounting and Finance", "Management Sciences", "Economics", "Sociology", "History", "Psycology", "Political Science", "Econ Pol", "Law"]


# minors = majors[0:7]

# major_req_ch = [126, 128, 130, 132]

# class_capacity = [45, 50, 60, 70, 80, 90, 100, 150, 200]

# credit_hours = [2, 3, 4]

# credit_hours_taken = [i for i in range(50, 120)]

# helper_cgpa = [*range(1,41,1)]
# cgpas = [x/10 for x in helper_cgpa]

# grad_years = [i for i in range(2018,2023)]

# schools = ['SBASSE', 'HSS', 'SAHSOL', "SDSB"]

# ratings = [i for i in range(0,10)]

# semester_term = ["fall", "summer", "spring"]

# years = [i for i in range(2011, 2020)]



# course_names = ['Programming and Data Analysis for Social Sciences', 'Digital Logic Circuits', 'Constitutional Development in Pakistan', 'Readings in Economics', "Rethinking Policy: Critical Perspectives on Pakistan's Agricultural Development", 'Logic & Critical Thinking', 'Governance and its Discontents', 'Software Engineering', 'Advanced Partial Differential Equations', 'Mathematical Methods in Physics and Engineering-I', 'Islamic Ethics', 'Electromechanical Systems', 'Gender and Development', 'Advanced Condensed Matter Physics', 'Sales Force Management', 'Agrarian Change and Peasant Struggle in the Twenty-First Century', 'Applied Data Analysis', 'Sociology of Education', 'Data Mining', 'Discontents of Politics', 'Human Resource Management', 'Psychology of Love and Attachment', 'Criminal Procedure', 'Digital Signal Processing', 'Naya Urdu Afsana', 'Education Policy and Practice for Development', 'Business and Government Relations', 'Experimental Methods in Chemical Research', 'Developmental Biology 1', 'Principles of Economics', 'Experimental Physics Lab I', 'Labor Law', 'The Word & the World', 'Education and Conflict', 'Time Series Econometrics', 'Eukaryotic Development', 'Intermediate Macroeconomics', 'Education Policy Analysis', 'Modern Thought in Social Policy', 'Competition Law and Policy', 'Legal Theory', 'Civil Society and Social Movements', 'Western Canon II', 'Enlightenment, Romanticism and the Law', 'Strategic Business Management', 'Special Topics in Physical Chemistry', 'Pashto for Non Pashto Speakers', 'The Art of Healing in Medieval Islam', 'Methods in Cell and Molecular Biology', 'Agribusiness & Value Chain Management', 'Advanced Microeconomics', 'Speech Processing', 'Modern Physics', 'Philosophy of Education', 'Introduction to Management Science', 'Electricity Markets', 'Qualitative Research Methods', 'Physical Chemistry Lab', 'Organic Chemistry Lab II', 'Sports Management', 'Principles of Optics', 'Digital Logic Circuits Lab', 'Development Economics', 'Chemical Thermodynamics', 'International Trade', 'Introduction to Gender and Sexuality Studies', 'Foundations of Modern South Asian History', 'Nanoelectronic Devices', 'A brief history of feminist movement in Pakistan', 'Sectors and Policy in Development', 'Principles of Management Accounting', 'Policy Analysis and Communication', 'Cell Signaling', 'Text, Performance and Religion', 'Plato & Aristotle', 'Marketing Models', 'Chemical Kinetics and Reaction Engineering', 'Business Analytics', 'Digital Signal Processing Lab', 'Philosophy Gym', 'Operations and Supply Chain Management', 'Fintech Revolution: Market Disruption and Emerging Opportunities', 'Project Management', 'Healthcare Operations Management', 'Financial Modelling', 'Western Political Philosophy', 'Social Entrepreneurship', 'Legal Practice III: Drafting Pleadings and Statutory Interpretation', 'Managing People', 'Operations Management Fundamentals', 'Computational Problem Solving', 'Managerial Accounting and Control', 'Could Education be Bad for Society?', 'Machine Learning', 'Retail Management', 'Introduction to Political Science', 'Quantum Computation and Information', 'Graduate Physics Lab', 'Channel Management', 'Data Lab', 'Feedback Control Systems Lab', 'Statistics and Data Analysis', 'Advanced Methods in Biology', 'Intermediate Finance', 'History of Miniature Painting', 'Principles of Financial Accounting', 'Environmental Chemistry', 'Big Data Analytics', 'Topics in Internet Research', 'Equity, Specific Relief & Trusts', 'Operations Research-II', 'Politics of Armed Groups', 'Engineering Laboratory', 'Professional Communication Skills', 'Strength Training and Conditioning for Beginners', 'Business Strategy', 'Multiphase Processing', 'Inorganic Chemistry Lab', 'General Relativity', 'Symmetry Methods, Conservation Laws and Exact Solutions for Differential Equations', 'Opto-Electronic Devices', 'Firms, Markets and Public Policy', 'Applied Statistics for Humanities', 'Introduction to Game Theory', 'Econometrics', 'Scientific Computation and Simulation', 'Financial Management', 'Managerial Communication', 'Human Rights', 'Corporate Strategy', 'Transport Phenomena II', 'Advanced Physical Chemistry-I', 'Deep Learning', 'Advanced Urban Economics', 'Operations Management-Technology, Innovation and Emerging Trends', 'Business Government Relations', 'Family Business', 'Issues in Economic Policy', 'Symmetry Methods for Differential Equations', 'Organizational Power and Politics', 'Education in the Globalized World', 'Introduction to Analysis I', 'Introduction to Logic', 'Mathematical Applications in Economics', 'Civil Procedure', 'Constitutionalization of Gende', 'Partial Differential Equations', 'Data Driven Marketing', 'Deviance and Social Control', 'Tech-Entrepreneurship', 'Persian II', 'Investments', 'Advanced Digital & Wireless Communication Technologies', 'The Romantic Imagination: British Romantic Poetry', 'Cognition and Computers', 'Data Structures', 'Principles of Microeconomics', 'High Voltage Engineering', 'The (Instructional) Core and How to Work it', 'Socio-Ecological Systems & Sustainability', 'Trauma and Resilience', 'Qualitative & Quantitative Methods in Business', 'Literary Theory', 'Particle Science and Engineering', 'Corporate Finance', 'Advanced Programming', 'Media Writing', 'Financial Crises', 'Optimization Methods in Management Science', 'Computational Physics', 'Technology in Educational Environments', 'Theory of Automata', 'Business Venture Proposal Writing', 'Academic Writing and Editing', 'Introduction to Sociology', 'Concept of Law', 'Theories and Methods in the study of Religion', 'Natural Language Processing', 'Introduction to Environmental Studies', 'Organotransition Metal Chemistry', 'Advance Biochemistry', 'Human Behaviour', 'RNA Biology', 'Electromagnetic Fields & Waves', 'Convex Optimization', 'Quantum Chemistry & Spectroscopy', 'Introduction to Cultural Anthropology', 'Mechanics of Fiction', 'Economics of Pandemics', 'Explorations in Pakistani Cinemas', 'Organic Spectroscopy', 'Circuits 2', 'Feminisms in Abrahamic Traditions', 'Trade and Development', 'Topics in Systems Biology', 'Protein Informatics', 'Sindhi for Non Sindhi Speakers', 'Statistics', 'Globalization: Theory & Practice', 'Africa in the World System', 'Polymer Science & Technology', 'Topics in Law and Economics', 'Logic & Rhetoric in the Quran', 'Software Development: Tools and Processes', 'Condensed Matter Physics', 'Macroeconomic Analysis', 'The Politics of Sub-Saharan Africa', 'Words are all we have: Identity Predicament in the Theatre of the Absurd', 'Political Economy of Development', 'Chemical Engineering Thermodynamics', 'Image and Video Coding', 'Business Data Management', 'Principles of Management', 'EMBA Project', 'Data Science for Decision Making', 'Advanced Algebra', 'Technology, Design and Innovation Management', 'Spectra of Differential Operators and Quantum Graphs', 'Signals and Systems', 'Managerial Economics', 'Punjabi II', 'Microelectronic Design', 'World Civilizations', 'Law Professing', 'General Topology', 'Introduction to Quranic and Modern Standard Arabic', 'Classical Anthropological Theory', 'Introduction to Artificial Intelligence', 'Intermediate Microeconomics', 'Political Sociology', 'Corporate Financial Reporting-II', 'Scientific Computation and Simulation with Python', 'My Startup', 'VLSI Design', 'Conceptual Understanding of Borders and Borderlands Studies', 'MBA Consultancy Project', 'Cosmopolitan Circuits from Asia to Africa', 'Health Systems Management', 'Computer and Problem Solving', 'Quantum Mechanics - II', 'Leading Organizations', 'School Effectiveness and Development', 'Introduction to Quantative Research Method', 'Islamic Studies', 'Decision Analysis', 'Applied Corporate Finance', 'Entrepreneurial Finance', 'Calculus-I', 'Auditing', 'Organizational Behaviour', 'Decision Behaviour', 'Arabic II', 'The Politics of Class and Markets', 'Seminar in Organizational Behavior', 'Introductory Biology', 'Financial Institutions & Markets', 'Investments Theory and Financial Markets', 'Literary Adaptations and its Discontents', 'Biology Laboratory', 'Politics of Pakistan', 'Information and Communication Technology for Development', 'Ordinary Differential Equations', 'Basketball for Beginners', 'Pre-calculus', 'Topics in Energy Economics', 'Introduction to Environmental Economics', 'Reforming The Public Sector', 'Applied Taxation', 'Inclusive Education: Rethinking the Other', 'Law Professing: Research and Writing Intensive', 'Introduction to Development Studies', 'Constitutionalization of Gender in Pakistan', 'Multi-agent Systems', 'Legal Practice I:Legal Writing and Research Methods', 'Embedded Systems', 'Molecular Spectroscopy', 'Photovoltaic Devices', 'Software Engineering for Smart Grids', 'Advanced Research Methods', 'Marcel Mauss and Postmodern Critique:How Law, Language, Morality, and Justice are related to Economy', 'Principles of Marketing', 'Arabic I', 'Engineering Mathematics', 'Practicum', 'Utopian Literature', 'Linear Algebra with Differential Equations', 'Introduction to Business Process Modeling', 'Rethinking the Politics of Harem in Literature: Women, Islam, and Gendered Spaces', 'Chemical Process Simulation', 'End of Nature: Disaster & Geopolitics in Environmental Fiction', 'Introduction to Quantum Field Theory', 'Writing and Communication', 'An Anthology of Pashto Literature', 'Electrical Drives', 'Innovation and Entrepreneurship in Healthcare', 'A Brief history of Evil', 'Political Islam: Ideology & Politics', 'Ethnography for Education Policy', 'Introduction to the Arts in Education', 'Course Title', 'Healthcare Policy, Politics and Law', 'Intelligent Computing', 'Pakistan Studies: Culture and Heritage', 'Service Oriented Computing', 'Research Methods', 'Advanced General Topology', 'Principles of Macroeconomics', 'Entrepreneurship & Management in the Restaurant Industry', 'Tax Law', "Pakistan's Foreign Relations", 'Econometrics and Research Methodology II', 'Introduction to Data Mining', 'Business Ethics & Islam', 'Experimental Physics Lab-II', 'Introduction to Comparative Politics', 'Politics of Class & Markets', 'Political Leadership', 'The World Since 1453', 'Mobile Lives:Im/migration and Education', 'Introduction to Legal Reasoning', 'Business Ethics & Corporate Social Responsibility', 'Organic Chemistry Lab I', 'Policy Design and Delivery', 'Seminar in Organization Theory', 'Market Institutions', 'Chemical Engineering Lab II', 'Introduction to Programming', 'Business Communication', 'Introduction to Policy Analysis', 'Cognition', 'Electrical Power Systems', 'Islamic Historiography: An Introduction', 'Advanced Macroeconomics', 'Language, Culture and Society', 'Business Law', 'Corporate Financial Reporting-I', 'Network-Centric Computing', 'Spectra of Differential Operators', 'Using New Media Technologies in Marketing', 'Probability', 'Modernity as a Way of Life', 'Technology and Operations Management', 'Effective Teaching and Learning in Higher Education', 'Introductory Circuits Lab', 'Principles of Finance', 'Plant Physiology', 'Supply Chain & Logistics Management', 'Mir and Ghalib', 'Feedback Control Systems', 'Methods in Comparative Literature', 'Probability and Statistics', 'Seminar in Biology-II', 'Business Intelligence', 'Actuarial Sciences and Insurance', 'Advanced Calculus', 'Principles and Techniques of Data Science', 'Accounting for Islamic Financial Institutions', 'Experimental Chemistry', 'Chemical Engineering Lab 1', 'Introduction to Literature in English', 'Advanced Organic Chemistry', 'The Poetics and Politics of a Performative Past: Vaar in Punjabi Literary Tradition', 'Education and Development', 'Personal Effectiveness', 'Telling Stories with Data', 'Islamicate Poetry in South Asia', 'Advanced Topics in Chinese Law', 'International Module; Globalization and Cross Cultural Management', 'Selected Topics in Physical Chemistry', 'Aag ka Darya: A close Reading', 'Operational Research II', 'Software Engineering for the Smart Grid', 'Consumer Behaviour', 'Electromechanical Systems Lab', 'Network Security', 'Max Weber', 'The Arts and Education', 'Public Law', 'Computational Biology I', 'Legal Practice IV: Advocacy', 'Calculus-II', 'Biochemistry', 'International Business']


# student_names =['Shahzil Hamayun', 'Uzair Butt', 'Agha Abbas', 'Moneeba Rehman', 'Taha Abideen', 'Syed Shah Patel', 'Farrukh Tufail', 'Farrukh Gulzar', 'Salman Butt', 'Afnan Amin', 'Faisal Naseem', 'Syed Abbas Arshad', 'Talha Rasool', 'Nouman Munir', 'Talha Khan', 'Taha Dodhy', 'Abdurreman Iqbal', 'Haider Hamas', 'Salaar Hashmi', 'Haseeb Ijaz', 'Mesum Munir', 'Hashim Hassan', 'Humza Hakim', 'Ramez Naseem', 'Ahmad Aslam', 'Syed Shah Ali', 'Kinza Javed', 'Saifullah Asif', 'Haider Kamran', 'Aurengzeb Akbar', 'Waasif Rasul', 'Nazish Saleem', 'Daniyal Ejaz', 'Mustafa Ch', 'Adnan Rasul', 'Humza Cheema', 'Ghulam Hashmi', 'Hayder Amir', 'Husnain Arhsad', 'Hafsa Bhatti', 'Uzair Rana', 'Matloob Hamayun', 'Yahya Saleem', 'Salaar Islam', 'Uzair Raza', 'Waasif Zaidi', 'Mumtaz Athar', 'Zainab Adeeb', 'Aqsa Nawaz', 'HIra Hassan', 'Aleeha Ali', 'Sheheryar Raza', 'Mesum Raza', 'Waleed Suri', 'Anam Amin', 'Mustafa Rafi', 'Abdullah Shah', 'Salaar Rehman', 'Hafsa Amin', 'Salaar Yousaf', 'Haleema ALi', 'Raahim Kemall', 'Arslan Abbasi', 'Dilkisha Amir', 'Maha Ejaz', 'Yahya Saleemi', 'Aiyan Amir', 'Farhan Hamayun', 'Talha Arif', 'Aaqib Shahzad', 'Naureen Bugvi', 'Uzair Mehmood', 'Ayesha Kemall', 'Zohaib Dodhy', 'Sabeeh Tahir', 'Ahmed Rasool', 'Arham Amin', 'Aaqib Alam', 'Arham Shams', 'Syed Mohsin Mirza', 'Alishba Shah', 'Ayesha Bhatti', 'Jawaria Abideen', 'Saad Awan', 'Balaj Hakim', 'Zain Hassan', 'Haleema Iqbal', 'Aleeha Nawaz', 'Sheheryar Salman', 'Sarmad Shah', 'Maroof Aslam', 'Saifullah Awan', 'Daniyal Islam', 'Eman Awais', 'Salman Arif', 'Zoha Rasul', 'Alishba Saleem', 'Moneeba Butt', 'Momin Noor', 'Imran Dodhy', 'Dilkisha Majid', 'Maroof Hamas', 'Zoha Munir', 'Ramez HUrrairah', 'Rabeeya Hakim', 'Hafiza Suri', 'Hayder Shakeel', 'Furqan Tahir', 'Haris Bhatti', 'Hayder Amin', 'Daniyal Tufail', 'Ali Mannan', 'Taimoor Bhatti', 'Kashif Mannan', 'Nazish Yasser', 'Waleed Zafar', 'Nazish Haq', 'Wadood Ch', 'Nouman Salman', 'Nadia Naeem', 'Hafiza Butt', 'Aadam Raza', 'Salaar Naeem', 'Abdurreman Javed', 'Keven Naeem', 'Daniyal Rana', 'Aiyan Kamran', 'Nadia Awan', 'Kashif Majid', 'Dilkisha Shah', 'Syed Shah Shakeel', 'Saad Rehman', 'Mustafa Butt', 'Aurengzeb Iqbal', 'Khawaja Hakim', 'Anum ALtaf', 'Numan Hoshi', 'Furqan Mansoor', 'Jawaria Arif', 'Hayat Ejaz', 'Abu Rasool', 'Usama Bashir', 'Humza Lodhi', 'Shehsawar Shahzad', 'Kashif Salman', 'Hamza Bhatti', 'Minahil Khan', 'Abdurreman Hassan', 'Waasif Shams', 'Aimen Arshad', 'Yahya Rasool', 'Sala Hoshi', 'Syed Mohsin Saeed', 'Agha Mansoor', 'Farrukh Nazir', 'Naureen Athar', 'Agha Dodhy', 'Nabeel Arif', 'Faisal Salman', 'Haris Cheema', 'Zoha Mehmood', 'Muaz Raza', 'Taimoor Saleemi', 'Agha Hoshi', 'Keven Saleemi', 'Nadia Athar', 'Yahya Ali', 'Dilkisha Ijaz', 'Muhammad Mujtaba', 'Haleema Zafar', 'Laila Nadeem', 'Mariyam Baig', 'Sala Athar', 'Ahmad Tahir', 'Shehsawar Javed', 'Naureen Hamayun', 'Ramez Bhatti', 'Usman Lodhi', 'Mariyam Ahmed', 'Hasan Awan', 'Haider Tufail', 'Hafiza Hakim', 'Maham Awan', 'Sohaib Anwar', 'Afnan Qureshi', 'Aena Mustafa', 'Adnan Hakim', 'Farrukh Hamayun', 'Humza Afzal', 'Arslan Masood', 'Aimen Cheema', 'Shehsawar Hamas', 'Maroof Naeem', 'Syed Mohsin Rafi', 'Saifullah Zia', 'Ahmad Munir', 'Uzair Zia', 'Mesum Hakim', 'HIra Tahir', 'Adnan Dodhy', 'Momin Ejaz', 'Laila Ali', 'Hashim Saleem', 'Muneeb Yasin', 'Momin Yasser', 'Dania Mujtaba', 'Huzaifa Noor', 'Shahzil Tariq', 'Nadia Abbasi', 'Haider Abideen', 'Eman Kamran', 'HIra Ahmed', 'Aena ALi', 'Anum Ahmed', 'Uzair Salman', 'Yahya Amir', 'Rabeeya Arshad', 'Turab Saeed', 'Ali Javed', 'Uzair Arhsad', 'Hamas Asif', 'Niha Hakim', 'Hayat Hakim', 'Hamas Rasool', 'Saifullah Shakeel', 'Mustafa Hakim', 'Syed Mohsin Sardar', 'Aiyan Adeeb', 'Raahim Abbas', 'Shahzil Arif', 'Shahzil Ch', 'Momin Tarannum', 'Harum Rasool', 'Haider Alam', 'Agha Gulzar', 'Kashif Bhatti', 'Niha Asif', 'Sabeeh Rafi', 'Usman Hakim', 'Eman ALtaf', 'Khawaja Asif', 'Balaj Hashmi', 'Zain Ahmed', 'Ibrahim Farhan', 'Yahya Bashir', 'Hayat Javed', 'Ghulam Jamal Khan', 'Aaqib Zahid', 'Rabeeya Tahir', 'Minahil Moaz', 'Uzair Yasin', 'Ahmed Javed', 'Sala Mehmood', 'Naureen Abideen', 'Mahad Rizwan', 'Ibrahim Alam', 'Shehsawar Majid', 'Anam Kemall', 'Zohaib Saleemi', 'Ramez Tariq', 'Ghulam Asif', 'Alishba Nadeem', 'Dania Rizwan', 'Waasif Suri', 'Muaz Jamal Khan', 'Zain Farhan', 'Salaar Siddique', 'Sala Munir', 'Mustafa Rauf', 'Talha Abbas', 'Dilkisha Iftikhar', 'Mustafa Tahir', 'Nadia Hakim', 'Huzaifa Naeem', 'Shahrukh Hamas', 'Muhammad Butt', 'Qasim Tarannum', 'Taimoor Ejaz', 'Haris Arif', 'HIra Rizwan', 'Aadam Tariq', 'Waasif Raza', 'Farhan HUrrairah', 'Saad Noor', 'Faisal Abbas', 'Syed Shah Suri', 'Aaqib Nawaz', 'Harum Gulzar', 'Farrukh ALtaf', 'Imran Mansoor', 'Nadia Nizam', 'Shahrukh Qureshi', 'Mariyam Patel', 'Aadam Gulzar', 'Ahmed Anwar', 'Maroof Awais', 'Uzair Aamir', 'Talha Athar', 'Dania Abbas', 'Aurengzeb Zahid', 'Ahmed Yasin', 'Anum Arshad', 'Salman Shakeel', 'Arslan Nadeem', 'Mesum Siddique', 'Mesum Razzaq', 'Eman Mehmood', 'Bilal Saeed', 'Aurengzeb Mansoor', 'Ghulam Yasin', 'Sohaib Yasin', 'Dania Tanveer', 'Syed Abbas Hakim', 'Ayesha Saeed', 'Hammad Amir', 'Junaid Mahad', 'Maroof Amin', 'Agha Ali Mahad', 'Mubashir Javed', 'Husnain Mannan', 'Aurengzeb Bhatti', 'Maha Mannan', 'Haseeb Haq', 'Haseeb Cheema', 'Naureen Arshad', 'Keven Mustafa', 'Sannan Farhan', 'Daniyal Salman', 'Ayesha Mansoor', 'Nouman Athar', 'Dilkisha Patel', 'Saad Bugvi', 'Hashim Naseem', 'Huzaifa Raza', 'Muteeullah Anwar', 'Turab Tarannum', 'Dania Butt', 'Afnan Mustafa', 'Dania Saleem', 'Matloob Zahid', 'Taha Zaidi', 'Maha Khalid', 'Daniyal Noor', 'Aena Raza', 'Taha Mansoor', 'Kashif Javed', 'Ibrahim Majid', 'Muteeullah Saleemi', 'Alishba Athar', 'Bilal Saleemi', 'Qasim ALtaf', 'Imran Rana', 'Eman Hashmi', 'Aleeha Akbar', 'Zoha Shah', 'Hafsa Lodhi', 'Salaar Yasser', 'Maha Patel', 'Muteeullah Tauqir', 'Saad Jamal Khan', 'Aleeha Bugvi', 'Ahmad Iftikhar', 'Faisal Sardar', 'Abdurreman Hashmi', 'Ibrahim Hamayun', 'Huzaifa Shams', 'Hafiza Tariq', 'Junaid Iftikhar', 'Haider Patel', 'Ahmad Ch', 'Harum Sardar', 'Furqan Rauf', 'Ramez Raza', 'Ghulam Kamran', 'Maroof Hakim', 'Rabeeya Nawaz', 'Junaid Tauqir', 'Ahmad Arshad', 'Ahmad Rehman', 'Moneeba Patel', 'Sarmad Amin', 'Hashim Ijaz', 'Haider Awais', 'Taimoor Raza', 'Farhan Nizam', 'Alishba Ijaz', 'Aimen Khan', 'Ahmad Rasool', 'Turab Aslam', 'Farhan Saeed', 'Zain Nazir', 'Waleed Moaz', 'Muteeullah Tanveer', 'Dilkisha Arhsad', 'Nabeel Noor', 'Sheheryar Ch', 'Aqsa Majid', 'Sannan Qureshi', 'Alishba Anwar', 'Mariyam Dodhy', 'Kashif Rauf', 'Maroof Shams', 'Haseeb Qureshi', 'Niha Iftikhar', 'Humza Ch', 'Moneeba Nazir', 'Rabeeya Iqbal', 'Wadood Tauqir', 'Shehsawar Arshad', 'Sheheryar Abideen', 'Muneeb Abbasi', 'Zoha Bhatti', 'Nabeel HUrrairah', 'Khawaja Amir', 'Nouman Mirza', 'Muaz Masood', 'Dania Hamayun', 'Dania Javed', 'Turab Iqbal', 'Junaid Adeeb', 'Abdurreman Khan', 'Waleed Iqbal', 'Syed Shah Rehman', 'Keven Shams', 'Sarmad Shams', 'Hashim Shakeel', 'Muteeullah Athar', 'Taha Butt', 'Abu Chandio', 'Zainab Salman', 'Sarmad Abbasi', 'Bilal Ahmed', 'Ibrahim Nizam', 'Haider Raza', 'Numan Yasser', 'Nabeel Hashmi', 'Maha Saleemi', 'Naveed Tufail', 'Hayat Rasool', 'Aqsa Abideen', 'Ibrahim Tufail', 'Hayder Mustafa', 'Junaid Farhan', 'Daniyal Asif', 'Muaz Sardar', 'Haris Athar', 'Zain Tauqir', 'Raahim Asif', 'Yahya Akbar', 'Yahya Hamas', 'Faisal Hassan', 'Aleeha Abideen', 'Aqsa Suri', 'Adnan Saleem', 'Mahad Mujtaba', 'Zain Hamas', 'Rabeeya Zahid', 'Mahad ALi', 'Adnan Tanveer', 'Dyass Jamal Khan', 'Daniyal Naeem', 'Usman Patel', 'Maham Ahmed', 'Yahya Suri', 'Saifullah Shahzad', 'Aleeha Arhsad', 'Naveed Ahmed', 'Sheheryar Mirza', 'Hafsa Kemall', 'Yahya Bhatti', 'Saifullah Patel', 'Arslan Rauf', 'Abdullah Raza', 'Naveed Rehman', 'Bilal Tufail', 'Zohaib Javed', 'Haseeb Hamas', 'Arslan Adeeb', 'Uzair Chandio', 'Saifullah Baig', 'HIra Majid', 'Niha Bashir', 'Aleeha Cheema', 'Sohaib Bugvi', 'Salaar Hoshi', 'Haider Zafar', 'Sala Aamir', 'Hafiza Shahzad', 'Abdullah Asif', 'Sabeeh Naseem', 'Nabeel Zia', 'Turab Farhan', 'Moneeba Adeeb', 'Haider Dodhy', 'Sarmad Tarannum', 'Aleeha ALtaf', 'Sala Gulzar', 'Muneeb Lodhi', 'Abdurreman Khalid', 'Humza Mansoor']


# instructor_names = ['Matloob Shams', 'Mahad Islam', 'Mubashir Aamir', 'Laila Arshad', 'Harum Qureshi', 'Syed Abbas Yasin', 'Mahad Ijaz', 'Sabeeh Salman', 'Kashif Mujtaba', 'Arslan Shams', 'Muteeullah Hassan', 'Qasim Hassan', 'Minahil Farhan', 'Aurengzeb Tanveer', 'Turab Hashmi', 'Hayat Jamal Khan', 'Zainab Qureshi', 'Ramez Bugvi', 'Eman Qureshi', 'Adnan Masood', 'Keven Abideen', 'Usman Saleemi', 'Turab Aamir', 'Hammad Tahir', 'Zain Nawaz', 'Muteeullah Butt', 'Numan Adeeb', 'Syed Mohsin Saleemi', 'Aadam Haq', 'Uzair Asif', 'Agha Asif', 'Haleema Abbasi', 'Husnain Arif', 'Haseeb Suri', 'Usama Tufail', 'Aadam Majid', 'Wadood Siddique', 'Mustafa Islam', 'Yahya Shahzad', 'Ahmad Mujtaba', 'Shahzil ALtaf', 'Mahad Arif', 'Shiza Shah', 'Hamza Hoshi', 'Rabeeya Patel', 'Huzaifa Rafi', 'Ayesha Yousaf', 'Huzaifa Zafar', 'Zoha Mahad', 'Saifullah Abideen', 'Aleeha Qureshi', 'Farhan Hakim', 'Farhan Saleemi', 'Nadia Abideen', 'Naureen Nadeem', 'Agha Hamayun', 'Waasif Siddique', 'Muneeb Rasool', 'Naureen Yasser', 'Moneeba Iftikhar', 'Usman Gulzar', 'Afnan Raza', 'Haseeb Yousaf', 'Farhan Alam', 'Shahzil Tauqir', 'Saifullah Salman', 'Sala Shakeel', 'Saifullah Khalid', 'Agha Ali Salman', 'Ibrahim Ali', 'Shahzil Rafi', 'Maroof Iqbal', 'Agha Zaidi', 'Nabeel Shah', 'Qasim Saleem', 'Hamas Akbar', 'Kinza Ejaz', 'Wadood Ali', 'Sabeeh Adeeb', 'Kinza Hoshi', 'Hamza Khalid', 'Jawaria ALtaf', 'Dania Afzal', 'Salman Zahid', 'Yahya Islam', 'Matloob Abbas', 'Hamza Athar', 'Sohaib Masood', 'Farhan Naseem', 'Syed Shah Rasul', 'Usman Bugvi', 'Taha Saeed', 'Yahya Zahid', 'Syed Shah Amir', 'Mesum Saeed', 'Hafsa Ejaz', 'Wadood Rauf', 'Zain Mustafa', 'Ramez Ahmed', 'Mahad Ali', 'Syed Abbas Iftikhar', 'Kashif Patel', 'Daniyal Yasser', 'Niha Arhsad', 'Agha Ali Shah', 'Dilkisha Arif', 'Maham Jamal Khan', 'Momin Mahad', 'Farrukh Amir', 'Shahzil Athar', 'Agha Ali Mustafa', 'Naveed Adeeb', 'Turab Zahid', 'Maham Hamas', 'Hashim Siddique', 'Waleed Mahad', 'Mumtaz HUrrairah', 'Syed Abbas Mansoor', 'Daniyal HUrrairah', 'Husnain Chandio', 'Huzaifa Afzal', 'Anum Akbar', 'Anam Tufail', 'Salman Ahmed', 'Syed Shah Ejaz', 'Usman Amir', 'Shehsawar Zaidi', 'Khawaja Iqbal', 'Abu Moaz', 'Muaz Hamayun', 'Naureen Rasul', 'Aena Mahad', 'Balaj Noor', 'Syed Shah Salman', 'Momin Hoshi', 'Abdurreman Naseem', 'Sabeeh Siddique', 'Maha Hamas', 'Haleema Arshad', 'Mubashir Saeed', 'Sheheryar Hakim', 'Shahzil Arshad', 'Hasan Masood', 'Yahya Iqbal', 'Hafiza Rana', 'Anum Siddique', 'Ramez Tauqir', 'Mahad Arhsad', 'Nazish Maqbool', 'Haseeb Naeem', 'Hasan Munir', 'Dyass Afzal', 'Faisal Yasin', 'Hamas Aamir', 'Shiza Tanveer', 'Hasan Hakim', 'Syed Mohsin Zahid', 'Maha Tanveer', 'Aleeha Iftikhar', 'Zain Munir', 'Hafiza Salman', 'Maha Mehmood', 'Arham Rizwan', 'Shahzil Shakeel', 'Hayder Zahid', 'Muteeullah Rana', 'Furqan Shahzad', 'Naveed Kemall', 'Omer Anwar', 'Hammad Yasser', 'Maham Mahad', 'Zainab Mahad', 'Shahzil Zahid', 'Aadam Islam', 'Maham Islam', 'Ahmed Dodhy', 'Syed Mohsin Lodhi', 'Saad Yasser', 'Afnan Bashir', 'Minahil Ch', 'Hamza Zaidi', 'Muaz Zaidi', 'Imran Yasser', 'Aurengzeb Hamayun', 'Taimoor Anwar', 'Aqsa Zafar', 'Laila Rehman', 'Arslan Mujtaba', 'Mesum Maqbool', 'Hayder Salman', 'Muaz Awais', 'Dyass Yasser', 'Arslan Afzal', 'Arham Tariq', 'Naveed Patel', 'Nazish Hassan', 'Salaar Shams', 'Turab Kamran', 'Sabeeh Islam', 'Wadood Salman']


# conn = c.connect(host="localhost", port="3306", user="root", password="", database="djangoRawSQL")
# cur = conn.cursor()

# # #enterting majors
# # for index, major in enumerate(majors):
# #     cur.execute("INSERT INTO Major(id, name, school, req_ch) VALUES(%s,%s,%s,%s)",(index, major, random.choice(schools), random.choice(major_req_ch)))

# #enterting minors
# # for index, minor in enumerate(minors):
#     # cur.execute("INSERT INTO minor(id, name, school, req_ch) VALUES(%s,%s,%s,%s)",(index, minor, random.choice(schools), 30))

# #entering instructors
# # for i in range(200):
# #     ins_name = random.choice(instructor_names)
# #     cur.execute("INSERT INTO instructor(instructor_id, name, department, rating, school) VALUES(%s,%s,%s,%s,%s)",(i, ins_name, random.choice(departments), random.choice(ratings) ,random.choice(schools)))


# #entering courses
# # for index, course in enumerate(course_names):
# #     course_id = index
# #     name = course
# #     school = random.choice(schools)
# #     major = random.choice([i for i in range(0,len(majors))])
# #     instructor = random.choice([i for i in range(0,200)])
# #     course_cap = random.choice(class_capacity)
# #     semester = random.choice(semester_term)
# #     year = random.choice(years)
# #     ch = random.choice(credit_hours)
# #     cur.execute("INSERT INTO courses(course_id, name, school, major, instructor, course_cap, semester, year, credit_hours) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)",(course_id, name, school, major, instructor, course_cap, semester, year, ch))

# # # #entering minor courses
# # for index, minor in enumerate(minors):
# #     x = index * 6
# #     for i in range(6):
# #         m_id = index
# #         course_id = x
# #         cur.execute("INSERT INTO minor_courses(minor, course_id) VALUES(%s,%s)",(m_id, course_id))
# #         x = x + i

# #entering prereqs
# # for i in range(23):
# #     course_id = random.choice([i for i in range(0, len(course_names))])
# #     prereq_id = random.choice([i for i in range(0, len(course_names))])
# #     while course_id == prereq_id:
# #         prereq_id = random.choice([i for i in range(0, len(course_names))])
# #     try:
# #         cur.execute("INSERT INTO prereqs(course_id, prereq_id) VALUES(%s,%s)",(course_id, prereq_id))
# #     except Exception as e:
# #         print(e)


# #entering students
# # for index, student in enumerate(student_names):
# #     roll_number = roll_numbers[index]
# #     full_name = student
# #     grad_year = random.choice(grad_years)
# #     cgpa = random.choice(cgpas)
# #     ch_taken = random.choice(credit_hours_taken)
# #     major = random.choice([i for i in range(0, len(majors))])
# #     try:
# #         cur.execute("INSERT INTO students(roll_number, full_name, grad_year, cgpa, ch_taken, major) VALUES(%s,%s,%s,%s,%s,%s)",(roll_number, full_name, grad_year, cgpa, ch_taken, major))
# #     except Exception as e:
# #         print(e)

# # entering student course info
# # for roll_number in roll_numbers:
# #     student_courses = random.choice([x for x in range(15,25)])
# #     for i in range(student_courses):
# #         course_id = random.choice([i for i in range(0, len(course_names))])
# #         course_gpa = random.choice(cgpas)
# #         semester = random.choice(semester_term)
# #         year = random.choice(years) 
# #         try:
# #             cur.execute("INSERT INTO student_course_info(roll_number, course_id, course_gpa, semester, year) VALUES(%s,%s,%s,%s,%s)", (roll_number, course_id, course_gpa, semester, year))
# #         except:
# #             pass


# #entering major cores
# # for index, major in enumerate(majors):
# #     major_cores_numbers = random.choice([x for x in range(6,10)])
# #     major_cores = set()
# #     while(len(major_cores) != major_cores_numbers):
# #         major_cores.add(random.choice([i for i in range(0, len(course_names))]))
# #     for c_id in major_cores:
# #         course_id = c_id
# #         name = course_names[c_id]
# #         major = index
# #         try:
# #             cur.execute("INSERT INTO major_cores(course_id, name, major) VALUES(%s,%s,%s)", (course_id, name, index))
# #         except:
# #             pass

# #entering advisors
# # for roll_number in roll_numbers:
# #     r_n = roll_number
# #     instructor_id = random.choice([i for i in range(0, 200)])
# #     try:
# #         cur.execute("INSERT INTO advisor(roll_number, instructor_id) VALUES(%s,%s)", (r_n, instructor_id))
# #     except Exception as e:
# #         print(e)

# # entering antireqs
# for i in range(100):
#     course_id = random.choice([i for i in range(0, len(course_names))])
#     antireq_id = random.choice([i for i in range(0, len(course_names))])
#     while course_id == antireq_id:
#         antireq_id = random.choice([i for i in range(0, len(course_names))])
#     try:
#         cur.execute("INSERT INTO antireqs(course_id, antireq_id) VALUES(%s,%s)",(course_id, antireq_id))
#     except:
#         pass

import mysql.connector as c
import random
import names
from RandomWordGenerator import RandomWord

conn = c.connect(host="remotemysql.com", port="3306", user="DapokUse1q", password="CBAcV2ngg5", database="DapokUse1q")
# conn = c.connect(host="localhost", port="3306", user="root", password="", database="djangoRawSQL")
cursor = conn.cursor()

'''
CREATE TABLE `Major` (
 `id` int(11) NOT NULL,
 `name` varchar(30) NOT NULL,
 `school` varchar(30) NOT NULL,
 `req_ch` int(11) NOT NULL,
 PRIMARY KEY (`id`)
)
'''

# for i in range (12):
#     if (i < 5):
#         m_id = 3550 + i
#         name = ['Mathematics', 'Biology', 'Physics', 'Chemistry', 'CS']
#         school = 'SSE'
#         req_ch = [125, 125, 130 , 125, 130]
#         cursor.execute('INSERT INTO Major(id, name, school, req_ch) VALUES(%s, %s , %s, %s)',(m_id, name[i], school, req_ch[i]))
#         #print('INSERT INTO Major(id, name, school, req_ch) VALUES({}, {} , {}, {})'.format(m_id, name[i], school, req_ch[i]))

#     if (4 < i < 7):
#         m_id = 3550 +i
#         name = ['MGS', 'ACF']
#         school = 'SDSB'
#         req_ch = [125, 125]
#         cursor.execute('INSERT INTO Major(id, name, school, req_ch) VALUES(%s, %s , %s, %s)',(m_id, name[i-5], school, req_ch[i-5]))
#         #print('INSERT INTO Major(id, name, school, req_ch) VALUES({}, {} , {}, {})'.format(m_id, name[i-5], school, req_ch[i-5]))

#     if (6 < i < 11):
#         m_id = 3550 +i
#         name = ['Economics', 'English', 'Social Sciences', 'History']
#         school = 'HSS'
#         req_ch = [130, 125, 125 , 125]
#         cursor.execute('INSERT INTO Major(id, name, school, req_ch) VALUES(%s, %s , %s, %s)',(m_id, name[i-7], school, req_ch[i-7]))
#         #print('INSERT INTO Major(id, name, school, req_ch) VALUES({}, {} , {}, {})'.format(m_id, name[i-7], school, req_ch[i-7]))
    
#     if (10 < i < 12):
#         m_id = 3550 +i
#         name = ['Law']
#         school = 'LAW'
#         req_ch = [130, 125, 125 , 125]
#         cursor.execute('INSERT INTO Major(id, name, school, req_ch) VALUES(%s, %s , %s, %s)',(m_id, name[i-11], school, req_ch[i-11]))
#         #print('INSERT INTO Major(id, name, school, req_ch) VALUES({}, {} , {}, {})'.format(m_id, name[i-11], school, req_ch[i-11]))

# '''
# CREATE TABLE `minor` (
#  `id` int(11) NOT NULL,
#  `name` varchar(100) NOT NULL,
#  `school` varchar(200) NOT NULL,
#  `req_ch` int(11) NOT NULL,
#  PRIMARY KEY (`id`)
# ) 
# '''

# for i in range (12):
#     if (i < 5):
#         m_id = 3550 + i
#         name = ['Mathematics', 'Biology', 'Physics', 'Chemistry', 'CS']
#         school = 'SSE'
#         req_ch = [125, 125, 130 , 125, 130]
#         cursor.execute('INSERT INTO minor(id, name, school, req_ch) VALUES(%s, %s , %s, %s)',(m_id, name[i], school, req_ch[i]))
#         #print('INSERT INTO minor(id, name, school, req_ch) VALUES({}, {} , {}, {})'.format(m_id, name[i], school, req_ch[i]))

#     if (4 < i < 7):
#         m_id = 3550 +i
#         name = ['MGS', 'ACF']
#         school = 'SDSB'
#         req_ch = [125, 125]
#         cursor.execute('INSERT INTO minor(id, name, school, req_ch) VALUES(%s, %s , %s, %s)',(m_id, name[i-5], school, req_ch[i-5]))
#         #print('INSERT INTO minor(id, name, school, req_ch) VALUES({}, {} , {}, {})'.format(m_id, name[i-5], school, req_ch[i-5]))

#     if (6 < i < 11):
#         m_id = 3550 +i
#         name = ['Economics', 'English', 'Social Sciences', 'History']
#         school = 'HSS'
#         req_ch = [130, 125, 125 , 125]
#         cursor.execute('INSERT INTO minor(id, name, school, req_ch) VALUES(%s, %s , %s, %s)',(m_id, name[i-7], school, req_ch[i-7]))
#         #print('INSERT INTO minor(id, name, school, req_ch) VALUES({}, {} , {}, {})'.format(m_id, name[i-7], school, req_ch[i-7]))
    
#     if (10 < i < 12):
#         m_id = 3550 +i
#         name = ['Law']
#         school = 'LAW'
#         req_ch = [130, 125, 125 , 125]
#         cursor.execute('INSERT INTO minor(id, name, school, req_ch) VALUES(%s, %s , %s, %s)',(m_id, name[i-11], school, req_ch[i-11]))
#         #print('INSERT INTO minor(id, name, school, req_ch) VALUES({}, {} , {}, {})'.format(m_id, name[i-11], school, req_ch[i-11]))



# '''
# CREATE TABLE `instructor` (
#  `instructor_id` int(11) NOT NULL,
#  `name` varchar(50) NOT NULL,
#  `department` varchar(200) NOT NULL,
#  `rating` int(11) DEFAULT 0,
#  `school` varchar(200) DEFAULT NULL,
#  PRIMARY KEY (`instructor_id`)
# )
# '''

# dept_SSE = ['Mathematics', 'Biology', 'Physics', 'Chemistry', 'CS']
# dept_SDSB = ['MGS', 'ACF']
# dept_HSS = ['Economics', 'English', 'Social Sciences', 'History']
# dept_LAW = ['Law']

# Ratings = [1,2,3,4,5,6,7,8,9,10]

# for i in range(10000):
#     if i < 3000:
#         instructor_id = 511500 + i
#         name = names.get_full_name()
#         department = random.choice(dept_SSE)
#         rating = random.choice(Ratings)
#         school = 'SSE'
#         cursor.execute('INSERT INTO instructor(instructor_id, name, department, rating, school) VALUES(%s,%s,%s,%s,%s)',(instructor_id, name, department, rating, school))
#     if 2999 < i < 6000:
#         instructor_id = 511500 + i
#         name = names.get_full_name()
#         department = random.choice(dept_HSS)
#         rating = random.choice(Ratings)
#         school = 'HSS'
#         cursor.execute('INSERT INTO instructor(instructor_id, name, department, rating, school) VALUES(%s,%s,%s,%s,%s)',(instructor_id, name, department, rating, school))

#     if 5999 < i < 8000:
#         instructor_id = 511500 + i
#         name = names.get_full_name()
#         department = random.choice(dept_SDSB)
#         rating = random.choice(Ratings)
#         school = 'SDSB'
#         cursor.execute('INSERT INTO instructor(instructor_id, name, department, rating, school) VALUES(%s,%s,%s,%s,%s)',(instructor_id, name, department, rating, school))

#     if 7999 < i < 10000:
#         instructor_id = 511500 + i
#         name = names.get_full_name()
#         department = random.choice(dept_LAW)
#         rating = random.choice(Ratings)
#         school = 'LAW'
#         cursor.execute('INSERT INTO instructor(instructor_id, name, department, rating, school) VALUES(%s,%s,%s,%s,%s)',(instructor_id, name, department, rating, school)) 

# '''
# CREATE TABLE `courses` (
#  `course_id` int(11) NOT NULL,
#  `name` varchar(200) NOT NULL,
#  `school` varchar(200) NOT NULL,
#  `major` int(11) DEFAULT NULL,
#  `instructor` int(11) DEFAULT NULL,
#  `course_cap` int(11) DEFAULT NULL CHECK (`course_cap` > 0),
#  `semester` varchar(100) DEFAULT NULL CHECK (lcase(`semester`) in ('fall','spring','summer')),
#  `year` int(11) NOT NULL CHECK (`year` > 2000),
#  `credit_hours` int(11) NOT NULL,
#  PRIMARY KEY (`course_id`),
#  FOREIGN KEY (`major`) REFERENCES `Major` (`id`),
#  FOREIGN KEY (`instructor`) REFERENCES `instructor` (`instructor_id`) ON DELETE SET NULL
# )
# '''

# '''
# CREATE TABLE `major_cores` (
#  `id` int(11) NOT NULL AUTO_INCREMENT,
#  `course_id` int(11) NOT NULL,
#  `name` varchar(200) NOT NULL,
#  `major` int(11) NOT NULL,
#  PRIMARY KEY (`id`),
#  FOREIGN KEY (`course_id`) REFERENCES `courses` (`course_id`) ON DELETE CASCADE,
#  FOREIGN KEY (`major`) REFERENCES `Major` (`id`) ON DELETE CASCADE
# )
# '''


# rw = RandomWord()
# rw.generate()

# SSE_majors = [3550, 3551, 3552, 3553, 3554]
# HSS_majors = [3557, 3558, 3559, 3560]
# SDSB_majors = [3555, 3556]
# LAW_majors = [3561]

# for i in range(10000):

#     if i < 3000:
#         course_id = 111111+i
#         name = rw.generate()
#         school = 'SSE'
#         major = random.choice(SSE_majors)
#         instructor = random.randint(511500, 514499)
#         course_cap = random.randint(50, 300)
#         semester = random.choice(['fall','spring','summer'])
#         year = random.randint(2001, 2021)
#         credit_hours = random.randint(2, 4)

#         cursor.execute('INSERT INTO courses(course_id,name,school,major,instructor,course_cap,semester,year,credit_hours ) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)',(course_id,name,school,major,instructor,course_cap,semester,year,credit_hours))
        
#         if ((random.randint(0,10000) % 13) == 0 ):
#             cursor.execute('INSERT INTO major_cores(id,course_id,name,major) VALUES(%s,%s,%s,%s)',(course_id,course_id,name,major))
#             #print('INSERT INTO major_cores(id,course_id,name,major) VALUES({}, {} , {}, {})'.format(course_id,course_id,name,major))
    
#     elif 2999 < i < 6000:
#         course_id = 111111+i
#         name = rw.generate()
#         school = 'HSS'
#         major = random.choice(HSS_majors)
#         instructor = random.randint(514500,517499)
#         course_cap = random.randint(50, 300)
#         semester = random.choice(['fall','spring','summer'])
#         year = random.randint(2001, 2021)
#         credit_hours = random.randint(2, 4)

#         cursor.execute('INSERT INTO courses(course_id,name,school,major,instructor,course_cap,semester,year,credit_hours ) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)',(course_id,name,school,major,instructor,course_cap,semester,year,credit_hours))
#         #print('INSERT INTO courses(course_id,name,school,major,instructor,course_cap,semester,year,credit_hours ) VALUES({}, {} , {}, {}, {}, {} , {}, {}, {})'.format(course_id,name,school,major,instructor,course_cap,semester,year,credit_hours))

#         if ((random.randint(0,10000) % 13) == 0 ):
#             cursor.execute('INSERT INTO major_cores(id,course_id,name,major) VALUES(%s,%s,%s,%s)',(course_id,course_id,name,major))
#             #print('INSERT INTO major_cores(id,course_id,name,major) VALUES({}, {} , {}, {})'.format(course_id,course_id,name,major))
    
        
        
#     elif 5999 < i < 8000:
#         course_id = 111111+i
#         name = rw.generate()
#         school = 'SDSB'
#         major = random.choice(SDSB_majors)
#         instructor = random.randint(517500,519499)
#         course_cap = random.randint(50, 300)
#         semester = random.choice(['fall','spring','summer'])
#         year = random.randint(2001, 2021)
#         credit_hours = random.randint(2, 4)

#         cursor.execute('INSERT INTO courses(course_id,name,school,major,instructor,course_cap,semester,year,credit_hours ) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)',(course_id,name,school,major,instructor,course_cap,semester,year,credit_hours))
#         #print('INSERT INTO courses(course_id,name,school,major,instructor,course_cap,semester,year,credit_hours ) VALUES({}, {} , {}, {}, {}, {} , {}, {}, {})'.format(course_id,name,school,major,instructor,course_cap,semester,year,credit_hours))
#         if ((random.randint(0,10000) % 13) == 0 ):
#             cursor.execute('INSERT INTO major_cores(id,course_id,name,major) VALUES(%s,%s,%s,%s)',(course_id,course_id,name,major))
#             #print('INSERT INTO major_cores(id,course_id,name,major) VALUES({}, {} , {}, {})'.format(course_id,course_id,name,major))
    
        
    
#     elif 7999 < i < 10000:
            
#         course_id = 111111+i
#         name = rw.generate()
#         school = 'LAW'
#         major = random.choice(LAW_majors)
#         instructor = random.randint(519500,521499)
#         course_cap = random.randint(50, 300)
#         semester = random.choice(['fall','spring','summer'])
#         year = random.randint(2001, 2021)
#         credit_hours = random.randint(2, 4)

#         cursor.execute('INSERT INTO courses(course_id,name,school,major,instructor,course_cap,semester,year,credit_hours ) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)',(course_id,name,school,major,instructor,course_cap,semester,year,credit_hours))
#         #print('INSERT INTO courses(course_id,name,school,major,instructor,course_cap,semester,year,credit_hours ) VALUES({}, {} , {}, {}, {}, {} , {}, {}, {})'.format(course_id,name,school,major,instructor,course_cap,semester,year,credit_hours))
#         if ((random.randint(0,10000) % 13) == 0 ):
#             cursor.execute('INSERT INTO major_cores(id,course_id,name,major) VALUES(%s,%s,%s,%s)',(course_id,course_id,name,major))
#             #print('INSERT INTO major_cores(id,course_id,name,major) VALUES({}, {} , {}, {})'.format(course_id,course_id,name,major))
# conn.commit()
# print("courses", "major cores")
# # '''
# # CREATE TABLE `minor_courses` (
# #  `id` int(11) NOT NULL AUTO_INCREMENT,
# #  `minor` int(11) NOT NULL,
# #  `course_id` int(11) DEFAULT NULL,
# #  PRIMARY KEY (`id`),
# #  FOREIGN KEY (`minor`) REFERENCES `minor` (`id`) ON DELETE CASCADE,
# #  FOREIGN KEY (`course_id`) REFERENCES `courses` (`course_id`) ON DELETE SET NULL
# # ) 

# # '''

# rw = RandomWord()
# rw.generate()

# SSE_majors = [3550, 3551, 3552, 3553, 3554]
# HSS_majors = [3557, 3558, 3559, 3560]
# SDSB_majors = [3555, 3556]
# LAW_majors = [3561]

# for i in range(10000):

#     if i < 3000:
#         course_id = 111111+i
#         minor = random.choice(SSE_majors)

#         cursor.execute('INSERT INTO minor_courses(id,minor,course_id ) VALUES(%s,%s,%s)',(course_id,minor,course_id))
#         #print('INSERT INTO minor_courses(id,minor,course_id ) VALUES({}, {} , {})'.format(course_id,minor,course_id))

#     elif 2999 < i < 6000:
#         course_id = 111111+i
#         minor = random.choice(HSS_majors)
        
#         cursor.execute('INSERT INTO minor_courses(id,minor,course_id ) VALUES(%s,%s,%s)',(course_id,minor,course_id))
#         #print('INSERT INTO minor_courses(id,minor,course_id ) VALUES({}, {} , {})'.format(course_id,minor,course_id))

#     elif 5999 < i < 8000:
#         course_id = 111111+i
#         minor = random.choice(SDSB_majors)
        
#         cursor.execute('INSERT INTO minor_courses(id,minor,course_id ) VALUES(%s,%s,%s)',(course_id,minor,course_id))
#         #print('INSERT INTO minor_courses(id,minor,course_id ) VALUES({}, {} , {})'.format(course_id,minor,course_id))

    
#     elif 7999 < i < 10000:
            
#         course_id = 111111+i
#         minor = random.choice(LAW_majors)
        
#         cursor.execute('INSERT INTO minor_courses(id,minor,course_id ) VALUES(%s,%s,%s)',(course_id,minor,course_id))
# ##print('INSERT INTO minor_courses(id,minor,course_id ) VALUES({}, {} , {})'.format(course_id,minor,course_id))
# conn.commit()
# print("minor courses")
# # '''
# # CREATE TABLE `prereqs` (
# #  `course_id` int(11) NOT NULL,
# #  `prereq_id` int(11) NOT NULL,
# #  PRIMARY KEY (`course_id`,`prereq_id`),
# #  FOREIGN KEY (`course_id`) REFERENCES `courses` (`course_id`) ON DELETE CASCADE,
# #  FOREIGN KEY (`prereq_id`) REFERENCES `courses` (`course_id`) ON DELETE CASCADE
# # ) 
# # '''

# for i in range (1000):
    
#     prereq_id =  111111 + i
#     course_id = 111111 + (5*(i+1))
    
#     cursor.execute('INSERT INTO prereqs(course_id, prereq_id ) VALUES(%s, %s)',(course_id, prereq_id))
#     #print('INSERT INTO prereqs(course_id, prereq_id ) VALUES({}, {})'.format(course_id, prereq_id))
# conn.commit()
# print("prereqs")
# # '''
# # CREATE TABLE `students` (
# #  `roll_number` int(11) NOT NULL,
# #  `full_name` varchar(50) NOT NULL,
# #  `grad_year` int(11) NOT NULL,
# #  `cgpa` float DEFAULT 0,
# #  `ch_taken` int(11) DEFAULT 0,
# #  `major` int(11) DEFAULT NULL,
# #  PRIMARY KEY (`roll_number`),
# #  FOREIGN KEY (`major`) REFERENCES `Major` (`id`)
# # ) 
# # '''

# majors = [3550, 3551, 3552, 3553, 3554 , 3557, 3558, 3559, 3560 , 3555, 3556 ,3561]


# for i in range (10000):
#     roll_number = 21100000 + i
#     full_name = names.get_full_name()
#     grad_year = random.randint(2001, 2021)
#     cgpa = round(random.uniform(2, 4), 3)
#     if (2017 < grad_year < 2021 ):
#         ch_taken = random.randint(0 , 135)
#     else:
#         ch_taken = random.randint(125 , 135)
    
#     major = random.choice(majors)
    
#     cursor.execute('INSERT INTO students(roll_number,full_name, grad_year, cgpa, ch_taken, major) VALUES(%s,%s,%s,%s,%s,%s)',(roll_number,full_name, grad_year, cgpa, ch_taken, major))
#     #print('INSERT INTO students(roll_number,full_name, grad_year, cgpa, ch_taken, major) VALUES({}, {} , {}, {} , {}, {})'.format(roll_number,full_name, grad_year, cgpa, ch_taken, major))
# conn.commit()
# print("students")
# '''
# CREATE TABLE `student_course_info` (
#  `roll_number` int(11) NOT NULL,
#  `course_id` int(11) NOT NULL,
#  `course_gpa` float DEFAULT NULL CHECK (`course_gpa` >= 0 and `course_gpa` <= 4),
#  `semester` varchar(50) NOT NULL CHECK (lcase(`semester`) in ('fall','spring','summer')),
#  `year` int(11) NOT NULL,
#  PRIMARY KEY (`roll_number`,`course_id`),
#  FOREIGN KEY (`roll_number`) REFERENCES `students` (`roll_number`) ON DELETE CASCADE,
#  FOREIGN KEY (`course_id`) REFERENCES `courses` (`course_id`) ON DELETE CASCADE
# )
# '''

for i in range (10000):
    roll_number = 21100000 + i
    x = random.randint(111111, 121069)
    y = random.randint(2001, 2020)
    rand = random.randint(2, 20)
    for j in range (rand):
        course_id = x+j
        course_gpa = round(random.uniform(2, 4), 3)
        semester = random.choice(['fall','spring','summer'])
        year = y + random.randint(0, 3)
        cursor.execute('INSERT INTO student_course_info(roll_number,course_id, course_gpa, semester, year) VALUES(%s,%s,%s,%s,%s)',(roll_number,course_id, course_gpa, semester, year))
        #print('INSERT INTO student_course_info(roll_number,course_id, course_gpa, semester, year) VALUES({}, {} , {}, {} , {})'.format(roll_number,course_id, course_gpa, semester, year))
conn.commit()
print("student course info")
# '''
# CREATE TABLE `advisor` (
#  `roll_number` int(11) NOT NULL,
#  `instructor_id` int(11) DEFAULT NULL,
#  PRIMARY KEY (`roll_number`),
#  FOREIGN KEY (`roll_number`) REFERENCES `students` (`roll_number`) ON DELETE CASCADE,
#  FOREIGN KEY (`instructor_id`) REFERENCES `instructor` (`instructor_id`) ON DELETE SET NULL
# )
# '''

# for i in range (10000):
#     roll_number = 21100000 + i 
#     instructor_id = 511500 + (random.randint(0, 9999))
#     cursor.execute('INSERT INTO advisor(roll_number,instructor_id) VALUES(%s,%s)',(roll_number,instructor_id))
# conn.commit()
# print("advisor")
# '''
# CREATE TABLE `antireqs` (
#  `course_id` int(11) NOT NULL,
#  `antireq_id` int(11) NOT NULL,
#  PRIMARY KEY (`course_id`,`antireq_id`),
#  FOREIGN KEY (`course_id`) REFERENCES `courses` (`course_id`) ON DELETE CASCADE,
#  FOREIGN KEY (`antireq_id`) REFERENCES `courses` (`course_id`) ON DELETE CASCADE
# ) 
# '''

# for i in range (1000):
#     antireq_id =  111111 + (random.randint(0, 9999))
#     course_id = 111111 + (random.randint(0, 9999))
    
#     if (antireq_id == course_id ):
#         continue
    
#     cursor.execute('INSERT INTO antireqs(course_id, antireq_id ) VALUES(%s, %s)',(course_id, antireq_id))
#     #print('INSERT INTO antireqs(course_id, antireq_id ) VALUES({}, {})'.format(course_id, antireq_id))
##conn.commit()
# print("antireqs")
# conn.commit()
cursor.close()
conn.close()