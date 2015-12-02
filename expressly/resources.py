class CountryCode:
    def __init__(self, iso2=None, iso3=None):
        self.iso2 = iso2
        self.iso3 = iso3


class CountryCodes:
    codes = [
        CountryCode('AF', 'AFG'),
        CountryCode('AX', 'ALA'),
        CountryCode('AL', 'ALB'),
        CountryCode('DZ', 'DZA'),
        CountryCode('AS', 'ASM'),
        CountryCode('AD', 'AND'),
        CountryCode('AO', 'AGO'),
        CountryCode('AI', 'AIA'),
        CountryCode('AQ', 'ATA'),
        CountryCode('AG', 'ATG'),
        CountryCode('AR', 'ARG'),
        CountryCode('AM', 'ARM'),
        CountryCode('AW', 'ABW'),
        CountryCode('AU', 'AUS'),
        CountryCode('AT', 'AUT'),
        CountryCode('AZ', 'AZE'),
        CountryCode('BS', 'BHS'),
        CountryCode('BH', 'BHR'),
        CountryCode('BD', 'BGD'),
        CountryCode('BB', 'BRB'),
        CountryCode('BY', 'BLR'),
        CountryCode('BE', 'BEL'),
        CountryCode('BZ', 'BLZ'),
        CountryCode('BJ', 'BEN'),
        CountryCode('BM', 'BMU'),
        CountryCode('BT', 'BTN'),
        CountryCode('BO', 'BOL'),
        CountryCode('BA', 'BIH'),
        CountryCode('BW', 'BWA'),
        CountryCode('BV', 'BVT'),
        CountryCode('BR', 'BRA'),
        CountryCode('VG', 'VGB'),
        CountryCode('IO', 'IOT'),
        CountryCode('BN', 'BRN'),
        CountryCode('BG', 'BGR'),
        CountryCode('BF', 'BFA'),
        CountryCode('BI', 'BDI'),
        CountryCode('KH', 'KHM'),
        CountryCode('CM', 'CMR'),
        CountryCode('CA', 'CAN'),
        CountryCode('CV', 'CPV'),
        CountryCode('KY', 'CYM'),
        CountryCode('CF', 'CAF'),
        CountryCode('TD', 'TCD'),
        CountryCode('CL', 'CHL'),
        CountryCode('CN', 'CHN'),
        CountryCode('HK', 'HKG'),
        CountryCode('MO', 'MAC'),
        CountryCode('CX', 'CXR'),
        CountryCode('CC', 'CCK'),
        CountryCode('CO', 'COL'),
        CountryCode('KM', 'COM'),
        CountryCode('CG', 'COG'),
        CountryCode('CD', 'COD'),
        CountryCode('CK', 'COK'),
        CountryCode('CR', 'CRI'),
        CountryCode('CI', 'CIV'),
        CountryCode('HR', 'HRV'),
        CountryCode('CU', 'CUB'),
        CountryCode('CY', 'CYP'),
        CountryCode('CZ', 'CZE'),
        CountryCode('DK', 'DNK'),
        CountryCode('DJ', 'DJI'),
        CountryCode('DM', 'DMA'),
        CountryCode('DO', 'DOM'),
        CountryCode('EC', 'ECU'),
        CountryCode('EG', 'EGY'),
        CountryCode('SV', 'SLV'),
        CountryCode('GQ', 'GNQ'),
        CountryCode('ER', 'ERI'),
        CountryCode('EE', 'EST'),
        CountryCode('ET', 'ETH'),
        CountryCode('FK', 'FLK'),
        CountryCode('FO', 'FRO'),
        CountryCode('FJ', 'FJI'),
        CountryCode('FI', 'FIN'),
        CountryCode('FR', 'FRA'),
        CountryCode('GF', 'GUF'),
        CountryCode('PF', 'PYF'),
        CountryCode('TF', 'ATF'),
        CountryCode('GA', 'GAB'),
        CountryCode('GM', 'GMB'),
        CountryCode('GE', 'GEO'),
        CountryCode('DE', 'DEU'),
        CountryCode('GH', 'GHA'),
        CountryCode('GI', 'GIB'),
        CountryCode('GR', 'GRC'),
        CountryCode('GL', 'GRL'),
        CountryCode('GD', 'GRD'),
        CountryCode('GP', 'GLP'),
        CountryCode('GU', 'GUM'),
        CountryCode('GT', 'GTM'),
        CountryCode('GG', 'GGY'),
        CountryCode('GN', 'GIN'),
        CountryCode('GW', 'GNB'),
        CountryCode('GY', 'GUY'),
        CountryCode('HT', 'HTI'),
        CountryCode('HM', 'HMD'),
        CountryCode('VA', 'VAT'),
        CountryCode('HN', 'HND'),
        CountryCode('HU', 'HUN'),
        CountryCode('IS', 'ISL'),
        CountryCode('IN', 'IND'),
        CountryCode('ID', 'IDN'),
        CountryCode('IR', 'IRN'),
        CountryCode('IQ', 'IRQ'),
        CountryCode('IE', 'IRL'),
        CountryCode('IM', 'IMN'),
        CountryCode('IL', 'ISR'),
        CountryCode('IT', 'ITA'),
        CountryCode('JM', 'JAM'),
        CountryCode('JP', 'JPN'),
        CountryCode('JE', 'JEY'),
        CountryCode('JO', 'JOR'),
        CountryCode('KZ', 'KAZ'),
        CountryCode('KE', 'KEN'),
        CountryCode('KI', 'KIR'),
        CountryCode('KP', 'PRK'),
        CountryCode('KR', 'KOR'),
        CountryCode('KW', 'KWT'),
        CountryCode('KG', 'KGZ'),
        CountryCode('LA', 'LAO'),
        CountryCode('LV', 'LVA'),
        CountryCode('LB', 'LBN'),
        CountryCode('LS', 'LSO'),
        CountryCode('LR', 'LBR'),
        CountryCode('LY', 'LBY'),
        CountryCode('LI', 'LIE'),
        CountryCode('LT', 'LTU'),
        CountryCode('LU', 'LUX'),
        CountryCode('MK', 'MKD'),
        CountryCode('MG', 'MDG'),
        CountryCode('MW', 'MWI'),
        CountryCode('MY', 'MYS'),
        CountryCode('MV', 'MDV'),
        CountryCode('ML', 'MLI'),
        CountryCode('MT', 'MLT'),
        CountryCode('MH', 'MHL'),
        CountryCode('MQ', 'MTQ'),
        CountryCode('MR', 'MRT'),
        CountryCode('MU', 'MUS'),
        CountryCode('YT', 'MYT'),
        CountryCode('MX', 'MEX'),
        CountryCode('FM', 'FSM'),
        CountryCode('MD', 'MDA'),
        CountryCode('MC', 'MCO'),
        CountryCode('MN', 'MNG'),
        CountryCode('ME', 'MNE'),
        CountryCode('MS', 'MSR'),
        CountryCode('MA', 'MAR'),
        CountryCode('MZ', 'MOZ'),
        CountryCode('MM', 'MMR'),
        CountryCode('NA', 'NAM'),
        CountryCode('NR', 'NRU'),
        CountryCode('NP', 'NPL'),
        CountryCode('NL', 'NLD'),
        CountryCode('AN', 'ANT'),
        CountryCode('NC', 'NCL'),
        CountryCode('NZ', 'NZL'),
        CountryCode('NI', 'NIC'),
        CountryCode('NE', 'NER'),
        CountryCode('NG', 'NGA'),
        CountryCode('NU', 'NIU'),
        CountryCode('NF', 'NFK'),
        CountryCode('MP', 'MNP'),
        CountryCode('NO', 'NOR'),
        CountryCode('OM', 'OMN'),
        CountryCode('PK', 'PAK'),
        CountryCode('PW', 'PLW'),
        CountryCode('PS', 'PSE'),
        CountryCode('PA', 'PAN'),
        CountryCode('PG', 'PNG'),
        CountryCode('PY', 'PRY'),
        CountryCode('PE', 'PER'),
        CountryCode('PH', 'PHL'),
        CountryCode('PN', 'PCN'),
        CountryCode('PL', 'POL'),
        CountryCode('PT', 'PRT'),
        CountryCode('PR', 'PRI'),
        CountryCode('QA', 'QAT'),
        CountryCode('RE', 'REU'),
        CountryCode('RO', 'ROU'),
        CountryCode('RU', 'RUS'),
        CountryCode('RW', 'RWA'),
        CountryCode('BL', 'BLM'),
        CountryCode('SH', 'SHN'),
        CountryCode('KN', 'KNA'),
        CountryCode('LC', 'LCA'),
        CountryCode('MF', 'MAF'),
        CountryCode('PM', 'SPM'),
        CountryCode('VC', 'VCT'),
        CountryCode('WS', 'WSM'),
        CountryCode('SM', 'SMR'),
        CountryCode('ST', 'STP'),
        CountryCode('SA', 'SAU'),
        CountryCode('SN', 'SEN'),
        CountryCode('RS', 'SRB'),
        CountryCode('SC', 'SYC'),
        CountryCode('SL', 'SLE'),
        CountryCode('SG', 'SGP'),
        CountryCode('SK', 'SVK'),
        CountryCode('SI', 'SVN'),
        CountryCode('SB', 'SLB'),
        CountryCode('SO', 'SOM'),
        CountryCode('ZA', 'ZAF'),
        CountryCode('GS', 'SGS'),
        CountryCode('SS', 'SSD'),
        CountryCode('ES', 'ESP'),
        CountryCode('LK', 'LKA'),
        CountryCode('SD', 'SDN'),
        CountryCode('SR', 'SUR'),
        CountryCode('SJ', 'SJM'),
        CountryCode('SZ', 'SWZ'),
        CountryCode('SE', 'SWE'),
        CountryCode('CH', 'CHE'),
        CountryCode('SY', 'SYR'),
        CountryCode('TW', 'TWN'),
        CountryCode('TJ', 'TJK'),
        CountryCode('TZ', 'TZA'),
        CountryCode('TH', 'THA'),
        CountryCode('TL', 'TLS'),
        CountryCode('TG', 'TGO'),
        CountryCode('TK', 'TKL'),
        CountryCode('TO', 'TON'),
        CountryCode('TT', 'TTO'),
        CountryCode('TN', 'TUN'),
        CountryCode('TR', 'TUR'),
        CountryCode('TM', 'TKM'),
        CountryCode('TC', 'TCA'),
        CountryCode('TV', 'TUV'),
        CountryCode('UG', 'UGA'),
        CountryCode('UA', 'UKR'),
        CountryCode('AE', 'ARE'),
        CountryCode('GB', 'GBR'),
        CountryCode('US', 'USA'),
        CountryCode('UM', 'UMI'),
        CountryCode('UY', 'URY'),
        CountryCode('UZ', 'UZB'),
        CountryCode('VU', 'VUT'),
        CountryCode('VE', 'VEN'),
        CountryCode('VN', 'VNM'),
        CountryCode('VI', 'VIR'),
        CountryCode('WF', 'WLF'),
        CountryCode('EH', 'ESH'),
        CountryCode('YE', 'YEM'),
        CountryCode('ZM', 'ZMB'),
        CountryCode('ZW', 'ZWE')
    ]

    def iso2(self, code=None):
        if code is None:
            return list(c.iso2 for c in self.codes)
        elif len(code) == 3:
            return next((c.iso2 for c in self.codes if c.iso3 == code), None)
        else:
            return next((c.iso2 for c in self.codes if c.iso2 == code), None)

    def iso3(self, code=None):
        if code is None:
            return list(c.iso3 for c in self.codes)
        elif len(code) == 2:
            return next((c.iso3 for c in self.codes if c.iso2 == code), None)
        else:
            return next((c.iso3 for c in self.codes if c.iso3 == code), None)
