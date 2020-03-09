# Create a dictionary of country Latitude and logitude strongs
country_coordinate = {
    'United-States': {'lat': '39.495914459', 'log':'-98.989982605'},
    'Mexico': {'lat':'23.940620422', 'log':'-102.525138855'},
    'Greece':{'lat':'39.347442627','log':'22.571271896'},
    'Vietnam':{'lat':'16.167692184','log':'107.839050293'},
    'China':{'lat':'36.563114166','log':'103.735809326'},
    'Taiwan':{'lat':'23.748992920','log':'120.971282959'},
    'India':{'lat':'22.493118286','log':'79.727012634'},
    'Philippines':{'lat':'15.948041916','log':'121.422599792'},
    'Trinadad&Tobago':{'lat':'10.423745155','log':'-61.296531677'},
    'Canada':{'lat':'62.536041260','log':'-96.388351440'},
    'South':{'lat':'2.632999897','log':'36.599998474'},
    'Holand-Netherlands':{'lat':'52.250000000','log':'4.666999817'},
    'Puerto-Rico':{'lat':'18.225063324','log':'-66.478912354'},
    'Poland':{'lat':'52.129039764','log':'19.393701553'},
    'Iran':{'lat':'32.564262390','log':'54.303672791'},
    'England':{'lat':'52.598876953','log':'-1.466881037'},
    'Germany':{'lat':'51.121807098','log':'10.400694847'},
    'Italy':{'lat':'43.529029846','log':'12.162183762'},
    'Japan':{'lat':'36.653335571','log':'137.981689453'},
    'Hong':{'lat':'22.333080292','log':'114.191223145'},
    'Honduras':{'lat':'14.823818207','log':'-86.597541809'},
    'Cuba':{'lat':'21.610517502','log':'-78.960273743'},
    'Ireland':{'lat':'53.184986115','log':'-8.146889687'},
    'Cambodia':{'lat':'12.710771561','log':'104.916786194'},
    'Peru':{'lat':'-9.171242714','log':'-74.356880188'},
    'Nicaragua':{'lat':'12.844159126','log':'-85.031967163'},
    'Dominican-Republic':{'lat':'18.897331238','log':'-70.499938965'},
    'Haiti':{'lat':'18.933517456','log':'-72.674591064'},
    'El-Salvador':{'lat':'13.733005524','log':'-88.866500854'},
    'Hungary':{'lat':'47.165191650','log':'19.412044525'},
    'Columbia':{'lat':'3.906449080','log':'-73.075027466'},
    'Guatemala':{'lat':'15.696107864','log':'-90.357093811'},
    'Jamaica':{'lat':'18.236000061','log':'-77.363998413'},
    'Ecuador':{'lat':'-1.465569973','log':'-78.397209167'},
    'France':{'lat':'46.621841431','log':'2.451944113'},
    'Yugoslavia':{'lat':'44.820560455','log':'20.462219238'},
    'Scotland':{'lat':'56.690368652','log':'-4.044013977'},
    'Portugal':{'lat':'39.679908752','log':'-7.968665123'},
    'Laos':{'lat':'18.495557785','log':'103.767959595'},
    'Thailand':{'lat':'15.130673409','log':'101.017784119'},
    'Outlying-US(Guam-USVI-etc)':{'lat':'13.443708420','log':'144.777740479'},
    '?':{'lat':'0','log':'0'}
    }

# combining Categories of education levels
edu_categories = {'HS-grad':'HS', 'Some-college':'college', '7th-8th':'preHS', '10th':'preHS', 'Doctorate':'postGrad', 'Prof-school':'college',
 'Bachelors':'college', 'Masters':'postGrad', '11th':'preHS', 'Assoc-acdm':'college', 'Assoc-voc':'college', '1st-4th':'preHS', '5th-6th':'preHS', '12th':'preHS', '9th':'preHS', 'Preschool':'preHS'}

 # combining some of the workclass values
workclass_categories = {'?':'other', 'Without-pay':'other', 'Never-worked':'other', 'Private':'private', 'State-gov':'government', 'Federal-gov':'government', 'Local-gov':'government', 'Self-emp-not-inc':'entrepreneur', 'Self-emp-inc':'entrepreneur'}
