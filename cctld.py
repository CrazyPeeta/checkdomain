# -*- coding: utf-8 -*-
# https://check.rs/

class WhOISccTLD:
    
    def get_whois_server(self, extension):
        dict_extension = {
            'ac': 'whois.nic.ac',
            # 'ad': 'https://www.andorratelecom.ad/',
            'ae': 'whois.aeda.net.ae',
            'af': 'whois.nic.af',
            'ag': 'whois.nic.ag',
            'ai': 'whois.nic.ai',
            # 'al': 'https://akep.al/en/domain-e-application/',
            'am':'whois.amnic.net',
            # 'ao': 'https://www.dns.ao/ao/gca/index.php?id=19',
            # 'aq': 'No Information',
            'ar': 'whois.nic.ar',
            'as': 'whois.nic.as',
            'at': 'whois.nic.at',
            'au': 'whois.auda.org.au',
            'aw': 'whois.nic.aw',
            'ax': 'whois.ax',
            # 'az': 'http://whois.az/',
            # 'ba': 'https://nic.ba/?culture=en',
            # 'bb': 'https://whois.telecoms.gov.bb/search/',
            # 'bd': 'http://domainreg.btcl.com.bd/',
            'be': 'whois.dns.be',
            'bf': 'whois.registre.bf',
            'bg': 'whois.register.bg',
            'bh': 'whois.nic.bh',
            'bi': 'whois1.nic.bi',
            'bj': 'whois.nic.bj',
            'bm': 'whois.afilias-srs.net',
            'bn': 'whois.bnnic.bn',
            'bo': 'whois.nic.bo',
            'br': 'whois.registro.br',
            # 'bs': 'http://www.register.bs/',
            # 'bt': 'https://www.nic.bt/',
            'bw': 'whois.nic.net.bw',
            'by': 'whois.cctld.by',
            'bz': 'whois.afilias-srs.net',
            'ca': 'whois.cira.ca',
            'cc': 'ccwhois.verisign-grs.com',
            'cd': 'whois.nic.cd',
            'ch': 'whois.nic.ch',
            'ci': 'whois.nic.ci',
            # 'ck': 'http://www.vodafone.co.ck',
            'cl': 'whois.nic.cl',
            'cm': 'whois.netcom.cm',
            'cn': 'whois.cnnic.cn',
            'co': 'whois.nic.co',
            'cr': 'whois.nic.cr',
            # 'cu': 'http://www.nic.cu',
            # 'cv': 'http://www.dns.cv/',
            # 'cw': 'http://www.uoc.cw/cw-registry',
            'cx': 'whois.nic.cx',
            # 'cy': 'http://www.nic.cy',
            'cz': 'whois.nic.cz',
            'de': 'whois.denic.de',
            # 'dj': 'http://www.dj/',
            'dk': 'whois.dk-hostmaster.dk',
            'dm': 'whois.dmdomains.dm',
            'do': 'whois.nic.do',
            # 'dz': 'whois.nic.dz',
            # 'ec': 'whois.nic.ec',
            'ee': 'whois.tld.ee',
            # 'eg': 'https://domain.eg/',
            # 'eh': '',
            # 'er': 'https://www.eritel.com.er/',
            'es': 'whois.nic.es',
            'et': 'whois.ethiotelecom.et',
            'eu': 'whois.eu',
            'fi': 'whois.fi',
            'fj': 'whois.fj',
            # 'fk': 'http://www.sure.co.fk',
            'fm': 'whois.nic.fm',
            'fo': 'whois.nic.fo',
            'fr': 'whois.nic.fr',
            'ga': 'whois.nic.ga',
            'gd': 'whois.nic.gd',
            'ge': 'whois.nic.ge',
            'gf': 'whois.mediaserv.net',
            'gg': 'whois.gg',
            'gh': 'whois.nic.gh',
            'gi': 'whois2.afilias-grs.net',
            'gl': 'whois.nic.gl',
            # 'gm': 'http://www.nic.gm/htmlpages/whois.htm',
            # 'gn': 'https://psg.com/dns/gn/',
            # 'gp': 'https://whois.nic.gp/',
            'gq': 'whois.dominio.gq',
            # 'gr': 'https://grweb.ics.forth.gr/public/whois',
            'gs': 'whois.nic.gs',
            'gt': 'https://www.gt/sitio/index.php?lang=en',
            # 'gu': 'https://give.uog.edu/gu-domain-application-form/',
            # 'gw': 'https://nic.gw/en/whois/',
            'gy': 'whois.registry.gy',
            'hk': 'whois.hkirc.hk',
            # 'hm': 'whois.registry.hm',
            'hn': 'whois.nic.hn',
            'hr': 'whois.dns.hr',
            'ht': 'whois.nic.ht',
            'hu': 'whois.nic.hu',
            'id': 'whois.id',
            'ie': 'whois.weare.ie',
            'il': 'whois.isoc.org.il',
            'im': 'whois.nic.im',
            'in': 'whois.registry.in',
            'io': 'whois.nic.io',
            # 'iq': 'whois.cmc.iq',
            'ir': 'whois.nic.ir',
            'is': 'whois.isnic.is',
            'it': 'whois.nic.it',
            'je': 'whois.je',
            # 'jm': 'http://myspot.mona.uwi.edu/mits/',
            # 'jo': 'https://dns.jo/FirstPageen.aspx',
            'jp': 'whois.jprs.jp',
            'ke': 'whois.kenic.or.ke',
            'kg': 'whois.kg',
            # 'kh': 'http://www.tc.com.kh/public/',
            'ki': 'whois.coccaregistry.org',
            # 'km': 'https://comorestelecom.km/',
            'kn': 'whois.nic.kn',
            # 'kp': 'http://www.star.co.kp',
            'kr': 'whois.kr',
            'kw': 'whois.nic.kw',
            'ky': 'whois.kyregistry.ky',
            'kz': 'whois.nic.kz',
            'la': 'whois.nic.la',
            'lb': 'whois.lbdr.org.lb',
            'lc': 'whois2.afilias-grs.net',
            'li': 'whois.nic.li',
            # 'lk': 'whois.nic.lk',
            # 'lr': 'http://www.psg.com/dns/lr/',
            'ls': 'whois.nic.ls',
            'lt': 'whois.domreg.lt',
            'lu': 'whois.dns.lu',
            'lv': 'whois.nic.lv',
            'ly': 'whois.nic.ly',
            'ma': 'whois.registre.ma',
            # 'mc': 'https://www.nic.mc/',
            'md': 'whois.nic.md',
            'me': 'whois.nic.me',
            # 'mf': '',
            'mg': 'whois.nic.mg',
            # 'mh': 'http://www.nic.net.mh/',
            'mk': 'whois.marnet.mk',
            'ml': 'whois.nic.ml',
            'mn': 'whois.nic.mn',
            'mo': 'whois.monic.mo',
            'mp': 'https://get.mp/',
            'mq': 'whois.mediaserv.net',
            'mr': 'whois.nic.mr',
            'ms': 'whois.nic.ms',
            # 'mt': 'https://www.nic.org.mt/dotmt/',
            'mu': 'whois.nic.mu',
            # 'mv': 'dhiraagu.com.mv',
            'mw': 'whois.nic.mw',
            'mx': 'whois.mx', # recheck
            'my': 'rdap.mynic.my',
            'mz': 'whois.nic.mz',
            'na': 'whois.na-nic.com.na',
            'nc': 'whois.nc',
            # 'ne': ' http://www.intnet.ne',
            'nf': 'whois.nic.nf',
            'ng': 'whois.nic.net.ng',
            # 'ni': 'http://www.nic.ni',
            'nl': 'whois.domain-registry.nl',
            'no': 'whois.norid.no',
            # 'np': 'https://register.com.np/domainwhoisdetail',
            # 'nr': 'https://www.cenpac.net.nr/dns/whois.html',
            'nu': 'whois.iis.nu',
            'nz': 'whois.irs.net.nz',
            'om': 'whois.registry.om',
            # 'pa': 'http://www.nic.pa/',
            'pe': 'kero.yachay.pe',
            'pf': 'whois.registry.pf',
            # 'pg': 'https://www.unitech.ac.pg/',
            # 'ph': 'https://whois.dot.ph/',
            'pk': 'whois.pknic.net.pk',
            'pl': 'whois.dns.pl',
            'pm': 'whois.nic.pm',
            # 'pn': 'https://nic.pn/cgi-bin/whois.cgi',
            'pr': 'whois.afilias-srs.net',
            'ps': '95.217.44.246',
            'pt': 'whois.dns.pt',
            'pw': 'whois.nic.pw',
            # 'py': 'https://www.nic.py/',
            'qa': 'whois.registry.qa',
            're': 'whois.nic.re',
            'ro': 'whois.rotld.ro',
            'rs': 'whois.rnids.rs',
            'ru': 'whois.tcinet.ru',
            'rw': 'whois.ricta.org.rw',
            'sa': 'whois.nic.net.sa',
            'sb': 'whois.nic.net.sb',
            'sc': 'whois2.afilias-grs.net',
            # 'sd': 'whois.sdnic.sd',
            'se': 'whois.iis.se',
            'sg': 'whois.sgnic.sg',
            'sh': 'whois.nic.sh',
            'si': 'whois.register.si',
            'sk': 'whois.sk-nic.sk',
            'sl': 'whois.nic.sl',
            'sm': 'whois.nic.sm',
            'sn': 'whois.nic.sn',
            'so': 'whois.nic.so',
            # 'sr': 'https://isp.datasur.sr/',
            'ss': 'whois.nic.ss',
            'st': 'whois.nic.st',
            'su': 'whois.tcinet.ru',
            # 'sv': 'https://svnet.sv/',
            'sx': 'whois.sx',
            'sy': 'whois.tld.sy',
            # 'sz': 'http://www.sispa.org.sz/',
            'tc': 'whois.nic.tc',
            'td': 'whois.nic.td',
            'tf': 'whois.nic.tf',
            'tg': 'whois.nic.tg',
            'th': 'whois.thnic.co.th',
            'tj': 'http://www.nic.tj/whois.html',
            'tk': 'whois.dot.tk',
            'tl': 'whois.nic.tl',
            'tm': 'whois.nic.tm',
            'tn': 'whois.ati.tn',
            'to': 'whois.tonic.to',
            'tr': 'whois.trabis.gov.tr',
            # 'tt': 'https://www.nic.tt/cgi-bin/search.pl',
            'tv': 'whois.nic.tv',
            'tw': 'whois.twnic.net.tw',
            'tz': 'whois.tznic.or.tz',
            'ua': 'whois.ua',
            'ug': 'whois.co.ug',
            'uk': 'whois.nic.uk',
            'us': 'whois.nic.us',
            # 'uy': 'whois.nic.org.uy',
            'uz': 'whois.cctld.uz',
            # 'va': '',
            'vc': 'whois2.afilias-grs.net',
            've': 'whois.nic.ve',
            'vg': 'whois.nic.vg',
            # 'vi': 'https://whmcs.nic.vi/index.php?m=whois',
            # 'vn': 'https://www.vnnic.vn/en',
            'vu': 'whois.dnrs.vu',
            'wf': 'whois.nic.wf',
            'ws': 'whois.website.ws',
            'yt': 'whois.nic.yt',
            # 'za': 'https://www.nic.za/za-domains/',
            'zm': 'whois.zicta.zm',
            # 'zw': 'http://www.zispa.co.zw/',
            'ye': 'whois.y.net.ye',
        }
        
        pseudo_sld = {
            'br.com': 'whois.centralnic.net',
            'cn.com': 'whois.centralnic.net',
            'de.com': 'whois.centralnic.net',
            'eu.com': 'whois.centralnic.net',
            'gb.net': 'whois.centralnic.net',
            'gr.com': 'whois.centralnic.net',
            'in.net': 'whois.centralnic.net',
            'ru.com': 'whois.centralnic.net',
            'sa.com': 'whois.centralnic.net',
            'se.net': 'whois.centralnic.net',
            'uk.com': 'whois.centralnic.net',
            'uk.net': 'whois.centralnic.net',
            'us.com': 'whois.centralnic.net',
            'za.com': 'whois.centralnic.net',
            'jpn.com': 'whois.centralnic.net',
            'it.com': 'whois.it.com',
            
            'priv.at': 'whois.nic.priv.at',
            'co.ca': 'whois.co.ca',
            'co.pl': 'whois.co.pl',
            'ac.ru': 'whois.free.net',
            'com.ru': 'whois.flexireg.net',
            'msk.ru': 'whois.flexireg.net',
            'net.ru': 'whois.nic.net.ru',
            'nov.ru': 'whois.flexireg.net',
            'org.ru': 'whois.nic.net.ru',
            'pp.ru': 'whois.nic.net.ru',
            'spb.ru': 'whois.flexireg.net',
            'ac.uk': 'whois.ac.uk',
            'gov.uk': 'whois.gov.uk',
            'co.uz': 'whois.reg.uz',
            'com.uz': 'whois.reg.uz',
            'net.uz': 'whois.reg.uz',
            'org.uz': 'whois.reg.uz',
        }
        dict_extension.update(pseudo_sld)
        return dict_extension.get(extension, False)