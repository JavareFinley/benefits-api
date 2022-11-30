
def counties_from_zip(lookup_zip):
    matches = []

    for county, zips in zipcodes.items():
        for zip in zips:
            if zip == lookup_zip:
                matches.append(county)

    return matches


zipcodes = {
    "Adams County": [
        "80023",
        "80022",
        "80103",
        "80701",
        "80010",
        "80249",
        "80601",
        "80603",
        "80234",
        "80642",
        "80002",
        "80516",
        "80030",
        "80020",
        "80045",
        "80220",
        "80652",
        "80640",
        "80241",
        "80216",
        "80024",
        "80102",
        "80137",
        "80011",
        "80239",
        "80003",
        "80654",
        "80019",
        "80212",
        "80238",
        "80229",
        "80602",
        "80105",
        "80136",
        "80018",
        "80233",
        "80260",
        "80031",
        "80221",
        "80643",
        "80757",
    ],
    "Alamosa County": [
        "81101",
        "81151",
        "81144",
        "81123",
        "81131",
        "81040",
        "81146",
        "81136",
        "81125",
        "81140",
    ],
    "Arapahoe County": [
        "80103",
        "80010",
        "80012",
        "80013",
        "80219",
        "80828",
        "80122",
        "80123",
        "80120",
        "80014",
        "80129",
        "80101",
        "80111",
        "80246",
        "80128",
        "80045",
        "80237",
        "80220",
        "80017",
        "80102",
        "80137",
        "80011",
        "80124",
        "80019",
        "80110",
        "80113",
        "80236",
        "80223",
        "80125",
        "80105",
        "80136",
        "80112",
        "80016",
        "80015",
        "80018",
        "80230",
        "80126",
        "80121",
        "80247",
        "80231",
        "80224",
        "80222",
        "80209",
        "80210",
        "80138",
        "80134",
        "80107",
        "80757",
    ],
    "Archuleta County": [
        "81147",
        "81154",
        "81121",
        "81128",
        "81130",
        "81120",
        "81122",
        "81137",
    ],
    "Baca County": [
        "81084",
        "81064",
        "81090",
        "81044",
        "81073",
        "81087",
        "81047",
        "81041",
        "81049",
        "81052",
        "81029",
        "81054",
    ],
    "Bent County": [
        "81038",
        "81050",
        "81092",
        "81044",
        "81073",
        "81049",
        "81052",
        "81021",
        "81057",
        "81054",
        "81036",
    ],
    "Boulder County": [
        "80023",
        "80301",
        "80503",
        "80403",
        "80303",
        "80025",
        "80305",
        "80544",
        "80482",
        "80447",
        "80007",
        "80302",
        "80516",
        "80027",
        "80446",
        "80020",
        "80513",
        "80517",
        "80501",
        "80021",
        "80310",
        "80466",
        "80510",
        "80304",
        "80026",
        "80540",
        "80504",
        "80422",
        "80471",
        "80481",
        "80455",
    ],
    "Broomfield County": [
        "80023",
        "80603",
        "80234",
        "80007",
        "80516",
        "80027",
        "80020",
        "80021",
        "80005",
        "80602",
        "80026",
        "80031",
        "80514",
    ],
    "Chaffee County": [
        "81201",
        "81242",
        "81227",
        "81611",
        "81236",
        "80449",
        "81251",
        "81248",
        "81155",
        "81210",
        "81211",
        "80461",
    ],
    "Cheyenne County": [
        "80834",
        "80862",
        "80825",
        "80810",
        "80821",
        "80823",
        "81071",
        "80807",
        "80861",
        "80836",
        "80802",
        "81036",
        "81045",
        "80805",
        "80815",
    ],
    "Clear Creek County": [
        "80403",
        "80435",
        "80427",
        "80482",
        "80421",
        "80444",
        "80497",
        "80448",
        "80470",
        "80439",
        "80476",
        "80452",
        "80468",
        "80422",
        "80436",
        "80438",
    ],
    "Conejos County": [
        "81101",
        "81151",
        "81129",
        "81148",
        "81144",
        "81124",
        "81152",
        "81147",
        "81141",
        "81123",
        "81154",
        "81132",
        "81128",
        "81120",
        "81140",
    ],
    "Costilla County": [
        "81101",
        "81151",
        "81152",
        "81126",
        "81091",
        "81141",
        "81123",
        "81055",
        "81138",
        "81040",
        "81146",
        "81120",
        "81133",
    ],
    "Crowley County": [
        "81025",
        "81062",
        "81050",
        "81033",
        "80864",
        "80823",
        "81063",
        "81021",
        "81076",
        "81058",
        "81039",
        "80833",
        "81067",
    ],
    "Custer County": [
        "81069",
        "81226",
        "81005",
        "81253",
        "81232",
        "81023",
        "81131",
        "81155",
        "81212",
        "81252",
        "81223",
        "81040",
        "81143",
    ],
    "Delta County": [
        "81413",
        "81624",
        "81230",
        "81527",
        "81646",
        "81401",
        "81428",
        "81643",
        "81425",
        "81410",
        "81418",
        "81415",
        "81434",
        "81419",
        "81416",
    ],
    "Denver County": [
        "80022",
        "80010",
        "80012",
        "80204",
        "80249",
        "80219",
        "80603",
        "80202",
        "80214",
        "80293",
        "80642",
        "80002",
        "80123",
        "80014",
        "80206",
        "80235",
        "80111",
        "80246",
        "80045",
        "80237",
        "80220",
        "80207",
        "80290",
        "80127",
        "80216",
        "80137",
        "80011",
        "80239",
        "80205",
        "80227",
        "80232",
        "80019",
        "80212",
        "80110",
        "80113",
        "80236",
        "80223",
        "80238",
        "80211",
        "80226",
        "80016",
        "80015",
        "80203",
        "80230",
        "80294",
        "80033",
        "80221",
        "80247",
        "80231",
        "80224",
        "80222",
        "80209",
        "80210",
        "80218",
        "80264",
    ],
    "Dolores County": [
        "81332",
        "81320",
        "81426",
        "81325",
        "81301",
        "81331",
        "81430",
        "81423",
        "81435",
        "81323",
        "81324",
    ],
    "Douglas County": [
        "80863",
        "80908",
        "80132",
        "80131",
        "80425",
        "80122",
        "80120",
        "80129",
        "80104",
        "80109",
        "80106",
        "80133",
        "80128",
        "80116",
        "80433",
        "80127",
        "80108",
        "80827",
        "80124",
        "80130",
        "80125",
        "80118",
        "80112",
        "80016",
        "80126",
        "80138",
        "80134",
        "80135",
        "80107",
    ],
    "Eagle County": [
        "81620",
        "81649",
        "80423",
        "80463",
        "80426",
        "81623",
        "81601",
        "80498",
        "81621",
        "80479",
        "81632",
        "80459",
        "81642",
        "81637",
        "80443",
        "81657",
        "81655",
        "81645",
        "81631",
        "80461",
    ],
    "El Paso County": [
        "81025",
        "80951",
        "80860",
        "81062",
        "80831",
        "80910",
        "80840",
        "80819",
        "80930",
        "80938",
        "81008",
        "80863",
        "80830",
        "80908",
        "80132",
        "80905",
        "80906",
        "80915",
        "80924",
        "80902",
        "80809",
        "80939",
        "80927",
        "80808",
        "80106",
        "80133",
        "80920",
        "80919",
        "80909",
        "80925",
        "80913",
        "80929",
        "80813",
        "80922",
        "80864",
        "80917",
        "80907",
        "80903",
        "80904",
        "80911",
        "80928",
        "80835",
        "80923",
        "80817",
        "80829",
        "81240",
        "80118",
        "80832",
        "80921",
        "80914",
        "80135",
        "80833",
        "80926",
        "80916",
        "80918",
    ],
    "Elbert County": [
        "80103",
        "80828",
        "80831",
        "80830",
        "80908",
        "80808",
        "80106",
        "80101",
        "80821",
        "80116",
        "80102",
        "80835",
        "80118",
        "80832",
        "80105",
        "80136",
        "80016",
        "80138",
        "80134",
        "80117",
        "80107",
        "80833",
    ],
    "Fremont County": [
        "81201",
        "80860",
        "81226",
        "81221",
        "81005",
        "81253",
        "81232",
        "80449",
        "80813",
        "80820",
        "80816",
        "81233",
        "81222",
        "81155",
        "81212",
        "81252",
        "81223",
        "81240",
        "81244",
        "81007",
        "80926",
    ],
    "Garfield County": [
        "81624",
        "80426",
        "81623",
        "81601",
        "81648",
        "80483",
        "81621",
        "81652",
        "81635",
        "81525",
        "81641",
        "81647",
        "81524",
        "81630",
        "81650",
        "81637",
    ],
    "Gilpin County": [
        "80403",
        "80427",
        "80482",
        "80439",
        "80466",
        "80452",
        "80422",
        "80471",
    ],
    "Grand County": [
        "80423",
        "80463",
        "80451",
        "80467",
        "80498",
        "80482",
        "80447",
        "80446",
        "80442",
        "80459",
        "80497",
        "80487",
        "80517",
        "80473",
        "80466",
        "80510",
        "80476",
        "80452",
        "80478",
        "80468",
        "80480",
        "80512",
        "80422",
        "80436",
        "80481",
        "80438",
    ],
    "Gunnison County": [
        "81201",
        "81624",
        "81623",
        "81230",
        "81241",
        "81239",
        "81237",
        "81401",
        "81654",
        "81428",
        "81432",
        "81611",
        "81236",
        "81225",
        "81231",
        "81415",
        "81434",
        "81403",
        "81235",
        "81224",
        "81248",
        "81210",
        "81211",
        "81220",
        "81243",
    ],
    "Hinsdale County": [
        "81230",
        "81432",
        "81427",
        "81147",
        "81235",
        "81130",
        "81220",
        "81433",
        "81122",
        "81243",
    ],
    "Huerfano County": [
        "81069",
        "81089",
        "81022",
        "81152",
        "81091",
        "81123",
        "81131",
        "81055",
        "81252",
        "81040",
        "81146",
        "81133",
        "81039",
        "81020",
    ],
    "Jackson County": [
        "80447",
        "80428",
        "80446",
        "80459",
        "82063",
        "80487",
        "80473",
        "80480",
        "80512",
        "80434",
    ],
    "Jefferson County": [
        "80403",
        "80204",
        "80219",
        "80214",
        "80456",
        "80303",
        "80025",
        "80427",
        "80007",
        "80425",
        "80421",
        "80002",
        "80123",
        "80027",
        "80235",
        "80228",
        "80030",
        "80020",
        "80128",
        "80448",
        "80457",
        "80433",
        "80127",
        "80470",
        "80419",
        "80021",
        "80439",
        "80227",
        "80232",
        "80827",
        "80005",
        "80004",
        "80465",
        "80003",
        "80212",
        "80236",
        "80401",
        "80226",
        "80454",
        "80125",
        "80422",
        "80453",
        "80033",
        "80031",
        "80135",
        "80215",
    ],
    "Kiowa County": [
        "81050",
        "81092",
        "80825",
        "80810",
        "81047",
        "80823",
        "81071",
        "81052",
        "81021",
        "81076",
        "80802",
        "81054",
        "81036",
        "81045",
    ],
    "Kit Carson County": [
        "80824",
        "80834",
        "80812",
        "80862",
        "80825",
        "80810",
        "80821",
        "80822",
        "80807",
        "80861",
        "80735",
        "80836",
        "80802",
        "80805",
        "80815",
        "80804",
    ],
    "La Plata County": [
        "81332",
        "81147",
        "81301",
        "81328",
        "81121",
        "81326",
        "81323",
        "81334",
        "81433",
        "81122",
        "81137",
        "81303",
    ],
    "Lake County": [
        "80420",
        "81611",
        "80449",
        "81642",
        "80424",
        "81251",
        "80440",
        "80443",
        "81211",
        "81645",
        "80461",
    ],
    "Larimer County": [
        "80503",
        "80447",
        "80534",
        "80525",
        "80521",
        "80526",
        "80524",
        "80515",
        "80511",
        "82063",
        "80538",
        "80532",
        "80547",
        "80513",
        "80517",
        "80550",
        "80535",
        "80612",
        "80510",
        "80480",
        "80512",
        "80540",
        "80504",
        "80536",
        "80545",
        "80537",
        "80528",
        "80549",
    ],
    "Las Animas County": [
        "81089",
        "81064",
        "81050",
        "81152",
        "81082",
        "81091",
        "81073",
        "81024",
        "81027",
        "81081",
        "81059",
        "81049",
        "81055",
        "81054",
        "81039",
        "81020",
        "81067",
    ],
    "Lincoln County": [
        "81025",
        "81062",
        "80828",
        "80830",
        "80862",
        "80825",
        "80818",
        "80821",
        "80864",
        "80823",
        "81063",
        "81021",
        "81076",
        "80832",
        "80105",
        "80740",
        "80833",
        "81045",
        "80815",
        "80804",
        "80757",
    ],
    "Logan County": [
        "80720",
        "80741",
        "80733",
        "80736",
        "80743",
        "80728",
        "80745",
        "80742",
        "80731",
        "80726",
        "80759",
        "80754",
        "80751",
        "80750",
        "80722",
        "80747",
        "80749",
    ],
    "Mesa County": [
        "81413",
        "81507",
        "81624",
        "81623",
        "81527",
        "81646",
        "81428",
        "81652",
        "81635",
        "81520",
        "81523",
        "81525",
        "81647",
        "81643",
        "81505",
        "81524",
        "81425",
        "81501",
        "81504",
        "81434",
        "81630",
        "81522",
        "81506",
        "81650",
        "81503",
        "81422",
        "81419",
        "81526",
        "81416",
        "81521",
    ],
    "Mineral County": [
        "81230", "81149", "81147", "81154", "81235", "81132", "81130"],
    "Moffat County": [
        "81648",
        "81638",
        "81641",
        "81633",
        "81639",
        "81610",
        "81653",
        "81640",
        "81625",
    ],
    "Montezuma County": [
        "81332",
        "81320",
        "81321",
        "81325",
        "81301",
        "81331",
        "81328",
        "81326",
        "81323",
        "81330",
        "81334",
        "81327",
        "81324",
        "81335",
    ],
    "Montrose County": [
        "81230",
        "81527",
        "81401",
        "81432",
        "81325",
        "81429",
        "81425",
        "81415",
        "81403",
        "81430",
        "81522",
        "81424",
        "81423",
        "81411",
        "81422",
        "81431",
        "81220",
        "81416",
    ],
    "Morgan County": [
        "80103",
        "80701",
        "80720",
        "80741",
        "80733",
        "80705",
        "80649",
        "80611",
        "80653",
        "80742",
        "80652",
        "80754",
        "80654",
        "80750",
        "80723",
        "80757",
    ],
    "Otero County": [
        "81062",
        "81050",
        "81077",
        "81059",
        "81049",
        "81063",
        "81030",
        "81021",
        "81076",
        "81058",
        "81054",
        "81039",
        "81067",
    ],
    "Ouray County": [
        "81401",
        "81432",
        "81427",
        "81403",
        "81235",
        "81430",
        "81435",
        "81220",
        "81433",
    ],
    "Park County": [
        "81201",
        "80456",
        "80435",
        "80421",
        "80420",
        "80449",
        "80444",
        "80424",
        "80448",
        "80820",
        "80433",
        "80816",
        "80470",
        "80439",
        "80440",
        "80827",
        "80475",
        "81212",
        "80443",
        "81211",
        "80452",
        "80432",
        "80135",
        "80461",
    ],
    "Phillips County": [
        "80758",
        "80721",
        "80744",
        "80737",
        "80731",
        "80746",
        "80759",
        "80734",
        "80749",
    ],
    "Pitkin County": [
        "81624",
        "81623",
        "81601",
        "81654",
        "81621",
        "81615",
        "81611",
        "81612",
        "81647",
        "81225",
        "81642",
        "81656",
        "81434",
        "81251",
        "81224",
        "81210",
        "81211",
        "81645",
        "80461",
    ],
    "Prowers County": [
        "81084",
        "81090",
        "81092",
        "81073",
        "81047",
        "81043",
        "81041",
        "81071",
        "81052",
        "81036",
    ],
    "Pueblo County": [
        "81025",
        "81062",
        "81069",
        "81008",
        "81089",
        "81005",
        "81022",
        "81253",
        "81001",
        "81003",
        "80864",
        "81023",
        "81059",
        "81004",
        "81019",
        "80928",
        "80817",
        "81240",
        "81040",
        "81006",
        "81007",
        "81039",
        "80833",
        "81020",
        "81067",
    ],
    "Rio Blanco County": [
        "81648",
        "80467",
        "80469",
        "80483",
        "81635",
        "81638",
        "81641",
        "81633",
        "81639",
        "81647",
        "81610",
        "81630",
        "81650",
        "81637",
        "81640",
    ],
    "Rio Grande County": [
        "81101",
        "81144",
        "81147",
        "81154",
        "81132",
        "81130",
        "81120",
        "81125",
        "81140",
    ],
    "Routt County": [
        "80423",
        "80463",
        "80426",
        "80467",
        "80469",
        "80483",
        "81638",
        "81641",
        "81639",
        "80428",
        "80477",
        "80479",
        "80459",
        "81653",
        "80487",
        "81637",
        "80480",
        "80488",
        "81625",
    ],
    "Saguache County": [
        "81201",
        "81230",
        "81149",
        "81239",
        "81235",
        "81132",
        "81131",
        "81233",
        "81222",
        "81248",
        "81155",
        "81130",
        "81252",
        "81223",
        "81040",
        "81146",
        "81136",
        "81143",
        "81125",
        "81243",
    ],
    "San Juan County": [
        "81332",
        "81426",
        "81427",
        "81147",
        "81301",
        "81235",
        "81130",
        "81435",
        "81323",
        "81433",
        "81122",
    ],
    "San Miguel County": [
        "81332",
        "81320",
        "81426",
        "81432",
        "81427",
        "81325",
        "81301",
        "81429",
        "81403",
        "81430",
        "81423",
        "81411",
        "81422",
        "81431",
        "81435",
        "81323",
        "81433",
        "81324",
    ],
    "Sedgwick County": [
        "80721",
        "80744",
        "80737",
        "80728",
        "80731",
        "80726",
        "80734",
        "80749",
    ],
    "Summit County": [
        "81649",
        "80423",
        "80456",
        "80435",
        "80498",
        "80420",
        "80444",
        "80459",
        "80424",
        "80497",
        "80448",
        "80440",
        "80443",
        "80476",
        "80468",
        "81657",
        "81655",
        "81645",
        "80461",
    ],
    "Teller County": [
        "80860",
        "80819",
        "80863",
        "80814",
        "80906",
        "80809",
        "80133",
        "80813",
        "80820",
        "80816",
        "80827",
        "81212",
        "80829",
        "81240",
        "80921",
        "80135",
        "80926",
    ],
    "Washington County": [
        "80701",
        "80720",
        "80828",
        "80834",
        "80741",
        "80733",
        "80812",
        "80743",
        "80728",
        "80818",
        "80731",
        "80759",
        "80822",
        "80751",
        "80861",
        "80750",
        "80105",
        "80723",
        "80740",
        "80801",
        "80815",
        "80804",
        "80722",
        "80757",
    ],
    "Weld County": [
        "80023",
        "80701",
        "80615",
        "80623",
        "80601",
        "80603",
        "80651",
        "80741",
        "80620",
        "80645",
        "80648",
        "80534",
        "80525",
        "80649",
        "80634",
        "80611",
        "80610",
        "80642",
        "80516",
        "80524",
        "80745",
        "80542",
        "80742",
        "80621",
        "80530",
        "80538",
        "80547",
        "80729",
        "80652",
        "80754",
        "80520",
        "80102",
        "80513",
        "80501",
        "80631",
        "80550",
        "80612",
        "80644",
        "80654",
        "80750",
        "80650",
        "80602",
        "80136",
        "80026",
        "80504",
        "80543",
        "80514",
        "80643",
        "80546",
        "80622",
        "80624",
        "80537",
        "80528",
        "80549",
    ],
    "Yuma County": [
        "80720",
        "80758",
        "80824",
        "80812",
        "80743",
        "80727",
        "80731",
        "80759",
        "80822",
        "80807",
        "80734",
        "80861",
        "80735",
        "80836",
        "80755",
        "80805",
    ],
}
