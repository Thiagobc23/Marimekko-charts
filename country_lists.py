# countries from https://data.worldbank.org/country
all_countries = ['Afghanistan', 'Albania', 'Algeria', 'American Samoa', 
                 'Andorra', 'Angola', 'Antigua and Barbuda', 'Argentina', 
                 'Armenia', 'Aruba', 'Australia', 'Austria', 'Azerbaijan', 
                 'Bahamas, The', 'Bahrain', 'Bangladesh', 'Barbados', 
                 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bermuda', 
                 'Bhutan', 'Bolivia', 'Bosnia and Herzegovina', 'Botswana', 
                 'Brazil', 'British Virgin Islands', 'Brunei Darussalam', 
                 'Bulgaria', 'Burkina Faso', 'Burundi', 'Cabo Verde', 
                 'Cambodia', 'Cameroon', 'Canada', 'Cayman Islands', 
                 'Central African Republic', 'Chad', 'Channel Islands', 
                 'Chile', 'China', 'Colombia', 'Comoros', 'Congo, Dem. Rep.', 
                 'Congo, Rep.', 'Costa Rica', "Cote d'Ivoire", 'Croatia', 
                 'Cuba', 'Curacao', 'Cyprus', 'Czech Republic', 'Denmark', 
                 'Djibouti', 'Dominica', 'Dominican Republic', 'Ecuador', 
                 'Egypt, Arab Rep.', 'El Salvador', 'Equatorial Guinea', 
                 'Eritrea', 'Estonia', 'Eswatini', 'Ethiopia', 'Faroe Islands', 
                 'Fiji', 'Finland', 'France', 'French Polynesia', 'Gabon', 
                 'Gambia, The', 'Georgia', 'Germany', 'Ghana', 'Gibraltar', 
                 'Greece', 'Greenland', 'Grenada', 'Guam', 'Guatemala', 
                 'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti', 'Honduras', 
                 'Hong Kong SAR, China', 'Hungary', 'Iceland', 'India', 
                 'Indonesia', 'Iran, Islamic Rep.', 'Iraq', 'Ireland', 
                 'Isle of Man', 'Israel', 'Italy', 'Jamaica', 'Japan', 
                 'Jordan', 'Kazakhstan', 'Kenya', 'Kiribati', 
                 'Korea, Dem. People’s Rep.', 'Korea, Rep.', 'Kosovo', 
                 'Kuwait', 'Kyrgyz Republic', 'Lao PDR', 'Latvia', 'Lebanon', 
                 'Lesotho', 'Liberia', 'Libya', 'Liechtenstein', 'Lithuania', 
                 'Luxembourg', 'Macao SAR, China', 'Madagascar', 'Malawi', 
                 'Malaysia', 'Maldives', 'Mali', 'Malta', 'Marshall Islands', 
                 'Mauritania', 'Mauritius', 'Mexico', 'Micronesia, Fed. Sts.', 
                 'Moldova', 'Monaco', 'Mongolia', 'Montenegro', 'Morocco', 
                 'Mozambique', 'Myanmar', 'Namibia', 'Nauru', 'Nepal', 'Netherlands', 
                 'New Caledonia', 'New Zealand', 'Nicaragua', 'Niger', 'Nigeria', 
                 'North Macedonia', 'Northern Mariana Islands', 'Norway', 'Oman', 
                 'Pakistan', 'Palau', 'Panama', 'Papua New Guinea', 'Paraguay', 
                 'Peru', 'Philippines', 'Poland', 'Portugal', 'Puerto Rico', 'Qatar', 
                 'Romania', 'Russian Federation', 'Rwanda', 'Samoa', 'San Marino', 
                 'Sao Tome and Principe', 'Saudi Arabia', 'Senegal', 'Serbia', 
                 'Seychelles', 'Sierra Leone', 'Singapore', 'Sint Maarten (Dutch part)', 
                 'Slovak Republic', 'Slovenia', 'Solomon Islands', 'Somalia', 
                 'South Africa', 'South Sudan', 'Spain', 'Sri Lanka', 
                 'St. Kitts and Nevis', 'St. Lucia', 'St. Martin (French part)', 
                 'St. Vincent and the Grenadines', 'Sudan', 'Suriname', 'Sweden', 
                 'Switzerland', 'Syrian Arab Republic', 'Tajikistan', 'Tanzania', 
                 'Thailand', 'Timor-Leste', 'Togo', 'Tonga', 'Trinidad and Tobago', 
                 'Tunisia', 'Turkey', 'Turkmenistan', 'Turks and Caicos Islands', 
                 'Tuvalu', 'Uganda', 'Ukraine', 'United Arab Emirates', 'United Kingdom', 
                 'United States', 'Uruguay', 'Uzbekistan', 'Vanuatu', 'Venezuela, RB', 
                 'Vietnam', 'Virgin Islands (U.S.)', 'West Bank and Gaza', 'Yemen, Rep.', 
                 'Zambia', 'Zimbabwe']

eu = ['Austria', 'Belgium', 'Bulgaria', 'Croatia', 'Cyprus', 'Czech Republic', 'Denmark', 
      'Estonia', 'Finland', 'France', 'Germany', 'Greece', 'Hungary', 'Ireland', 'Italy', 
      'Latvia', 'Lithuania', 'Luxembourg', 'Malta', 'Netherlands', 'Poland', 'Portugal', 
      'Romania', 'Slovak Republic', 'Slovenia', 'Spain', 'Sweden']

la_c = ['Antigua and Barbuda', 'Argentina', 'Aruba', 'Bahamas, The', 'Barbados', 'Belize', 
        'Bolivia', 'Brazil', 'British Virgin Islands', 'Cayman Islands', 'Chile', 'Colombia', 
        'Costa Rica', 'Cuba', 'Curacao', 'Dominica', 'Dominican Republic', 'Ecuador', 
        'El Salvador', 'Grenada', 'Guatemala', 'Guyana', 'Haiti', 'Honduras', 'Jamaica', 
        'Mexico', 'Nicaragua', 'Panama', 'Paraguay', 'Peru', 'Puerto Rico', 
        'Sint Maarten (Dutch Part)', 'St. Kitts And Nevis', 'St. Lucia', 
        'St. Martin (French Part)','St. Vincent and The Grenadines', 'Suriname', 
        'Trinidad and Tobago', 'Turks and Caicos Islands', 'Uruguay', 'Venezuela, Rb', 
        'Virgin Islands (U.S.)']

# east asia and pacific
eap = ['American Samoa', 'Australia', 'Brunei Darussalam', 
       'Cambodia', 'China', 'Fiji', 'French Polynesia', 'Guam', 
       'Hong Kong Sar, China', 'Indonesia', 'Japan', 'Kiribati', 
       'Korea, Dem. People’S Rep.', 'Korea, Rep.', 'Lao Pdr', 
       'Macao Sar, China', 'Malaysia', 'Marshall Islands', 
       'Micronesia, Fed. Sts.', 'Mongolia', 'Myanmar', 'Nauru', 
       'New Caledonia', 'New Zealand', 'Northern Mariana Islands', 
       'Palau', 'Papua New Guinea', 'Philippines', 'Samoa', 
       'Singapore', 'Solomon Islands', 'Thailand', 'Timor-Leste', 
       'Tonga', 'Tuvalu', 'Vanuatu', 'Vietnam']

# europe and central asia
eca = ['Albania', 'Andorra', 'Armenia', 'Austria', 'Azerbaijan', 
       'Belarus', 'Belgium', 'Bosnia And Herzegovina', 'Bulgaria', 
       'Channel Islands', 'Croatia', 'Cyprus', 'Czech Republic', 
       'Denmark', 'Estonia', 'Faroe Islands', 'Finland', 'France', 
       'Georgia', 'Germany', 'Gibraltar', 'Greece', 'Greenland', 
       'Hungary', 'Iceland', 'Ireland', 'Isle Of Man', 'Italy', 
       'Kazakhstan', 'Kosovo', 'Kyrgyz Republic', 'Latvia', 
       'Liechtenstein', 'Lithuania', 'Luxembourg', 'Moldova', 
       'Monaco', 'Montenegro', 'Netherlands', 'North Macedonia', 
       'Norway', 'Poland', 'Portugal', 'Romania', 'Russian Federation', 
       'San Marino', 'Serbia', 'Slovak Republic', 'Slovenia', 'Spain', 
       'Sweden', 'Switzerland', 'Tajikistan', 'Turkey', 'Turkmenistan', 
       'Ukraine', 'United Kingdom', 'Uzbekistan']

# middle east and north africa
mena = ['Algeria', 'Bahrain', 'Djibouti', 'Egypt, Arab Rep.', 
        'Iran, Islamic Rep.', 'Iraq', 'Israel', 'Jordan', 'Kuwait', 
        'Lebanon', 'Libya', 'Malta', 'Morocco', 'Oman', 'Qatar', 
        'Saudi Arabia', 'Syrian Arab Republic', 'Tunisia', 
        'United Arab Emirates', 'West Bank And Gaza', 'Yemen, Rep.']
# Sub-saharan africa
ssa = ['Angola', 'Benin', 'Botswana', 'Burkina Faso', 'Burundi', 
       'Cabo Verde', 'Cameroon', 'Central African Republic', 'Chad', 
       'Comoros', 'Congo, Dem. Rep.', 'Congo, Rep.', "Cote D'Ivoire", 
       'Equatorial Guinea', 'Eritrea', 'Eswatini', 'Ethiopia', 'Gabon', 
       'Gambia, The', 'Ghana', 'Guinea', 'Guinea-Bissau', 'Kenya', 
       'Lesotho', 'Liberia', 'Madagascar', 'Malawi', 'Mali', 
       'Mauritania', 'Mauritius', 'Mozambique', 'Namibia', 'Niger', 
       'Nigeria', 'Rwanda', 'Sao Tome And Principe', 'Senegal', 
       'Seychelles', 'Sierra Leone', 'Somalia', 'South Africa', 
       'South Sudan', 'Sudan', 'Tanzania', 'Togo', 'Uganda', 'Zambia', 
       'Zimbabwe']

# north america
na = ['Bermuda', 'Canada', 'United States']

# south asia
sa = ['Afghanistan', 'Bangladesh', 'Bhutan', 'India', 'Maldives', 
      'Nepal', 'Pakistan', 'Sri Lanka']

# Highlight countries
highlight_all = ['China', 'India', 'United States', 'Russian Federation', 
                 'Brazil', 'Indonesia', 'Nigeria']

highlight_eu = ['Austria', 'Belgium', 'Czech Republic', 'France', 'Germany',
                'Italy', 'Poland', 'Portugal', 'Romania', 'Spain', 'Sweden']

highlight_la_c = ['Argentina', 'Brazil', 'Mexico', 'Guatemala', 
                  'Colombia', 'Bolivia']

var_dict = {'Rural Population':
                {'file':'API_SP.RUR.TOTL.ZS_DS2_en_csv_v2_2166125.csv',
                 'label':'Rural Pop. (%)',
                 'legend':['Rural Population', 'Urban Population'],
                 'min_year':1960,
                 'max_year':2019}, 
            'Access to Electricity':
                {'file':'API_EG.ELC.ACCS.ZS_DS2_en_csv_v2_2164123.csv',
                 'label':'Access to Electricity (%)',
                 'legend':['Access to Electricity', 'No Access to Electricity'],
                 'min_year':1990,
                 'max_year':2018},
            'Literacy':
                {'file':'API_SE.ADT.LITR.ZS_DS2_en_csv_v2_2163525.csv',
                 'label':'Literacy Rate (age +15)',
                 'legend':['Literate Pop.', 'Illiterate Pop.'],
                 'min_year':1970,
                 'max_year':2018},
            'Unemployment':
                {'file':'API_SL.UEM.TOTL.ZS_DS2_en_csv_v2_2163385.csv',
                 'label':'Unemployment (ILO Estimate)',
                 'legend':['Unemployed', 'Employed'],
                 'min_year':1991,
                 'max_year':2019}}