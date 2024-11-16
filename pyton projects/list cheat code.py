# # # concatinatiom 
# # # l1=[1,2]
# # # l1+=[3,4] # -> [1,2,3,4]
# # # print(l1)

# # #append this help to add single element to the array
# # # l2=[3,4]
# # # l2.append([5,6])
# # # print(l2) #-> [3, 4, [5, 6]]

# # # # extend 
# # # l3=[3,4]
# # # l3.extend([5,6])
# # # print(l3) #-> [3, 4, 5, 6]

# # # slicing [1:3 ] to out put sub list

# # l4=[2,3,4]
# # l5=l4
# # l5.append(6)
# # print(l5==l4) #-> True & both are [2,3,4,5] b/c l5=l4 ths just change chnaging a name not making new copy of l4 for that l4.copy()

# # l6=l4.copy()
# # l6.append(6)
# # print (f'l6 is {l6} and l4 is {l4}') #-> l6 is [2, 3, 4, 6, 6] and l4 is [2, 3, 4, 6]

# # # to remove element from list which is less than 5
# # nums=[1,2,3,4,6,7,5,2,1,3]
# # # wrong b/c remove while itrating affecte the indexing 
# # for num in nums:
# #     if num<5:
# #         nums.remove(num)        
# # # right
# # new_num=[]
# # for num in nums:
# #     if num>=5:
# #         nums.append(num)
# # nw_num=[num for num in nums if num>=5]

# # x=['JHON','matt','Sliniki']
# # y=['jhon','sliniKI']
# # # x+=y
# # # print(x)
# # t=[val.lower() for val in y]
# # common=[num for num in x if num.lower() in t]
# # print(common)

# countries = ['Argentina', 'Somalia', 'Tuvalu', 'Malta', 'Armenia', 'Christmas Island', 'Uganda',
#              'Central African Republic', 'Gambia', 'Morocco', 'Sint Maarten (Dutch part)', 'Tunisia', 'Aland Islands',
#              'Angola', 'Yemen', 'Niue', 'Brunei Darussalam', 'Sudan', 'Holy See (Vatican City State)', 'Malaysia',
#              'New Zealand', 'Palestinian Territory, Occupied', 'Iran, Islamic Republic of', 'Macedonia, Republic of',
#              'Montenegro', 'Macao', 'Belarus', 'Netherlands', 'Greenland', 'Thailand', 'French Southern Territories',
#              'Cyprus', "Korea, Democratic People's Republic of", 'Rwanda', 'Ethiopia', 'Saint Barthélemy', 'Botswana',
#              'Puerto Rico', 'Cape Verde', 'Nicaragua', 'Croatia', 'Guadeloupe', 'Réunion', 'Belize',
#              'Northern Mariana Islands', 'Indonesia', 'Serbia', 'British Indian Ocean Territory', 'Wallis and Futuna',
#              'Saint Martin (French part)', 'Nigeria', 'Spain', 'Guernsey', 'Guyana', 'Namibia',
#              'Venezuela, Bolivarian Republic of', 'Pitcairn', 'Suriname', 'Switzerland', 'Portugal', 'Saudi Arabia',
#              'Tanzania, United Republic of', 'Norfolk Island', 'Iceland', 'Ukraine', 'Estonia', 'Nauru', 'Comoros',
#              'Andorra', 'Turks and Caicos Islands', 'Guatemala', 'Cameroon', 'Chile', 'Bulgaria', 'Afghanistan',
#              'Sri Lanka', 'Romania', 'Tokelau', 'Montserrat', 'Congo', 'Congo, The Democratic Republic of the',
#              'Luxembourg', 'Bolivia, Plurinational State of', 'South Georgia and the South Sandwich Islands',
#              'Djibouti', 'Brazil', 'Burkina Faso', 'Curaçao', 'Heard Island and McDonald Islands', 'Cook Islands',
#              'Cocos (Keeling) Islands', 'China', 'Haiti', 'Swaziland', 'Mali', 'Burundi', 'Taiwan, Province of China',
#              'Ireland', 'Maldives', 'France', 'Martinique', 'Nepal', 'Saint Lucia', 'Uruguay', 'Seychelles', 'Algeria',
#              'Panama', 'Anguilla', 'Cuba', 'San Marino', 'Dominica', 'Germany', 'Iraq', 'Chad', 'Tonga', 'Qatar',
#              'Lesotho', 'Liberia', 'Bosnia and Herzegovina', 'Canada', 'Turkey', 'French Guiana', 'Jersey', 'Niger',
#              'Paraguay', 'Bangladesh', 'Barbados', 'Mauritius', 'United Kingdom', 'Bhutan', 'Isle of Man',
#              'Svalbard and Jan Mayen', 'Falkland Islands (Malvinas)', "Lao People's Democratic Republic",
#              'Saint Vincent and the Grenadines', 'Korea, Republic of', 'Dominican Republic', 'Philippines',
#              'Austria', 'Samoa', 'South Africa', 'Australia', 'Bahamas', 'Fiji', 'Mayotte', 'Albania',
#              'Sierra Leone', 'Gibraltar', 'Kazakhstan', 'French Polynesia', 'Jordan', 'Ecuador', 'Liechtenstein',
#              'Solomon Islands', 'Belgium', 'Gabon', 'Bermuda', 'Georgia', 'Saint Pierre and Miquelon', 'Ghana',
#              'Guinea', 'Singapore', 'Vanuatu', 'New Caledonia', 'Sao Tome and Principe', 'Mexico', 'Equatorial Guinea',
#              'Pakistan', 'Marshall Islands', 'Jamaica', 'Antigua and Barbuda', 'South Sudan', 'Japan', 'Slovenia',
#              'Moldova, Republic of', 'Virgin Islands, British', 'Latvia', 'Kenya', 'Trinidad and Tobago', 'Norway',
#              'Timor-Leste', 'Faroe Islands', 'Zimbabwe', 'Kuwait', 'Mozambique', 'Mauritania', 'Benin', 'Togo',
#              'Sweden', 'Cayman Islands', 'Mongolia', 'United States', 'United States Minor Outlying Islands',
#              'Papua New Guinea', 'Hong Kong', 'Myanmar', 'Viet Nam', 'Malawi', 'Micronesia, Federated States of',
#              'Aruba', 'Virgin Islands, U.S.', 'Saint Helena, Ascension and Tristan da Cunha', 'Oman',
#              'Bonaire, Sint Eustatius and Saba', 'Senegal', 'Monaco', 'Russian Federation', 'Antarctica',
#              'American Samoa', 'Slovakia', 'Guinea-Bissau', 'Egypt', 'Madagascar', 'Guam', 'United Arab Emirates',
#              'Kiribati', 'Israel', 'Eritrea', 'Saint Kitts and Nevis', 'El Salvador', 'Lebanon', 'Poland',
#              'Syrian Arab Republic', 'Cambodia', 'Czech Republic', 'Tajikistan', 'India', 'Denmark', "Côte d'Ivoire",
#              'Kyrgyzstan', 'Peru', 'Italy', 'Bouvet Island', 'Palau', 'Lithuania', 'Colombia', 'Turkmenistan', 'Zambia',
#              'Libya', 'Greece', 'Honduras', 'Azerbaijan', 'Costa Rica', 'Uzbekistan', 'Hungary',
#              'Grenada', 'Bahrain', 'Finland']

# # countries with largest names & small names
# lengths=[len(country) for country in countries]
# val=max(lengths)
# vas=min(lengths)
# largest_names=[country for country in countries if len(country)==val]
# small_names=[country for country in countries if len(country)==vas]
# print(largest_names , small_names)

# # Sort the countries by their lengths in descending order
# tot = sorted(countries, key=len, reverse=True)
# print(tot)

# x=[1,2]
# x.pop(1) # pop (index) & for remove( element_tobe removed)
# print(x)

# #Challenge #1
# # new_num=[]
# # for num in nums:
# #     if num>=5:
# #         nums.append(num)

# #Challenge #2
# x=[10,20,10,20,30]
# y=[]
# for i in range(len(x)):
#     if x[i] not in y:
#         y.append(x[i])
# print(y)

#Challenge #3
# nums = '10,20,30,40,50'
# num=nums.split(',')
# print(num)
# res=[int(nu) for nu in num]
# print(res)

#Challenge #5
# str1="My name is Andrei"
# num=str1.split(' ')
# print(" ".join(num[::-1]))

#Challenge #6
# str2="green-red-yellow-black-white"
# num=str2.split('-')
# num.sort()
# print("-".join(num))

#Challenge #7
str2="I love cat and dogs"
num=str2.split()
val=[nu[::-1] for nu in num]
print(val)










  