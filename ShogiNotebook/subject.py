black_5 = {
    '一直線穴熊': 'sfen ln3gsnk/1r1s4l/p1pppgbpp/1p3pp2/4P4/2P6/PP1PSPPPP/1B2R2SL/LN1G1G1NK b - 25',
    '54歩64銀': 'ln1g1gsnl/1r3k3/p1pp1p1pp/3sp1p2/1p7/2P1P4/PPSP1PPPP/4R2K1/LN1G1GSNL b Bb 19',
    '55dragon': '55dragon'
}
black_4 = {}
black_3 = {}
black_2 = {
    'ダイレクト': 'direct'
}
white_4 = {}
white_3 = {}
white_2 = {
    'ダイレクト': 'direct',
    '角換わり拒否': 'deny_kakugawari',
    '阪田': 'sakata',
    '鬼殺し': 'onigaroshi',
    'メリケン': 'America'
}
black_fujii = {}
white_fujii = {}
black_kks = {}
white_kks = {}

kondo_fujii = {
    'op': 'sfen lnsgkgsnl/4r4/pppp1p2p/6pR1/9/2P1P4/PP1P1PP1P/1S2G4/LN1GK1SNL w B2Pbp 16',
    '57歩': 'sfen lnsgkgsnl/4r4/pppp1p2p/6pR1/9/2P1P4/PP1PpPP1P/1S2G4/LN1GK1SNL b B2Pb 17',
    '都成': 'sfen lnsg1gs1+R/3kr4/pppp1pL1p/6p2/4N4/2P1P4/PP1P1PP1P/4G4/+bN1GK1SNL w B2Pslp 24',
    '33角': 'sfen lnsg1gs1+R/3kr4/pppp4p/5pp2/4N4/2PLP4/PP1P1PP1P/4G4/+bN1GK1SNL w S2Pblp 28'
}
kondo_hoshino = {
    '銀対抗': 'sfen lnsgkg1nl/4r4/pppp1pbpp/5sp2/4p2P1/2P2SP2/PP1PPP2P/1B1K3R1/LNSG1G1NL b - 17',
    '菅井44歩': 'sfen lnsgkg1nl/4r1s2/pppp2bpp/5pp2/4p2P1/2P3P2/PP1PPPS1P/1B1K3R1/LNSG1G1NL b - 15',
    '72玉': 'sfen lnsg1gsnl/1k2r4/pppp1pbpp/6p2/4p2P1/2P2SP2/PP1PPP2P/1B1K3R1/LNSG1G1NL b - 17'
}
kondo_maruyama = {
    '佐藤': 'sfen lnsgkg1nl/4r2s1/pppp1p1pp/4p1p2/7P1/P1P6/1P1PPPP1P/7R1/LNSGKGSNL w Bb 10'
}
kondo = {
    '超急戦': kondo_fujii,
    '超速': kondo_hoshino,
    '丸山': kondo_maruyama,
    '穴熊': 'anaguma'
}

aifuri = {
    '相三間': 'each3',
    '中飛車左穴熊VS三間飛車': 'black_5left_white_3',
    '角交換四間飛車VS向かい飛車': 'black_kks_white_2',
    'ノーマル四間飛車VS三間飛車': 'black_4_white_3',
    '後手44角型向かい飛車': 'white_44b',
}

aigakari_26r = {
    'op': 'sfen lnsgk1snl/1r4gb1/p1ppppppp/9/1p7/7R1/PPPPPPP1P/1BG6/LNS1KGSNL w P 12',
    '塚田': 'sfen ln1gk1snl/2s3gb1/2p1pppp1/p2p3Pp/9/PrP4RP/3PPPP2/1BG3S2/LNS1KG1NL w Pp 24'
}
aigakari_28r = {
    'op': 'sfen lnsgk1snl/1r4gb1/p1ppppppp/9/1p7/9/PPPPPPP1P/1BG4R1/LNS1KGSNL w P 12'
}
aigakari = {
    'op': 'sfen lnsgk1snl/1r4gb1/p1ppppppp/9/1p5P1/9/PPPPPPP1P/1BG4R1/LNS1KGSNL b - 7',
    '5手': 'sfen lnsgkgsnl/1r5b1/p1ppppp1p/7R1/1p7/9/PPPPPPP1P/1B7/LNSGKGSNL w Pp 8',
    '浮き飛車': aigakari_26r,
    '引き飛車': aigakari_28r
}

yokofu_gosenzo = {
    'op': 'sfen lnsgk1snl/1r4gb1/p1pppp1pp/6pR1/1p7/2P6/PP1PPPP1P/1BG6/LNS1KGSNL b P 13'
}
yokofu_waki = {
    'op': 'sfen lnsgk1s1l/6gb1/p1ppppn1p/6R2/9/1rP6/P2PPPP1P/1BG6/LNS1KGSNL b 3P2p 17'
}
yokofu_each = {
    'op': 'sfen lnsgk1snl/6g2/p1pppp2p/6R2/9/2r6/P2PPPP1P/1SG6/LN2KGSNL b B3Pb3p 19',
    '77桂': 'sfen lnsgk1snl/6g2/p1pppp2p/6R2/9/2r6/P1NPPPP1P/1SG6/L3KGSNL w B3Pb3p 20',
    '羽生の頭脳': 'sfen l+B1gk1snl/2S3g2/p2ppp2p/9/2p6/2K6/P2PPP2P/2G6/LN2+b1G1L b RS2N5Prs2p 1',
    'Ponanza': 'sfen lnsgk1snl/6g2/p1pppp2p/2r6/9/6R2/P1PPPPP1P/1SG6/LN2KGSNL w B2Pb3p 22'
}
yokofu_38p = {
    '44角56角': 'sfen lnsgk1snl/6g2/p1pppp2p/2r2bR2/9/4B4/PPSPPPP1P/2G3S2/LN2KG1NL w 3P2p 1',
    '44角77角決定版': 'sfen lnsgk1snl/4p1g2/p1pp+Bpp1p/4R4/9/2r6/P1NPPPP1P/1S1G2S2/Lb2KG1NL w 5P 1'
}
yokofu_28p = {
    '77角op': 'sfen lnsgk1snl/6g2/p1pppp2p/6R2/9/1rP6/P1BPPPP1P/1SG4p1/LN2KGSNL w 3Pbp 1',
    '77角84飛必勝定跡': 'sfen lnsgk1snl/6g2/p1ppppp1p/1R7/9/7r1/P1BPPPPpP/1SG3G2/LN2K1SNL w 4Pb 1',
    '45角op': 'sfen lnsgk1snl/6g2/p1pppp2p/6R2/5b3/1rP6/P2PPPP1P/1SG4S1/LN2KG1NL b B4Pp 1'
}
yokofu_33b = {
    'op': 'sfen lnsgk1snl/6g2/p1ppppb1p/6R2/9/1rP6/P2PPPP1P/1BG6/LNS1KGSNL b 3P2p 1',
    '竹部': 'sfen lnsgk1snl/6g2/p1pppp+R1p/9/9/1rP6/P2PPPP1P/1BG6/LNS1KGSNL w B3P2p 1',
    '青野': 'sfen lnsgk1snl/6g2/p1ppppb1p/6R2/9/1rP6/P2PPPP1P/1BG1K4/LNS2GSNL w 3P2p 18',
    '勇気': 'sfen lnsgk1snl/6g2/p1ppppb1p/6R2/9/1rP6/P2PPPP1P/1BGK5/LNS2GSNL w 3P2p 18',
    '36飛': 'sfen lnsgk1snl/6g2/p1ppppb1p/9/9/1rP3R2/P2PPPP1P/1BG6/LNS1KGSNL w 3P2p 18',
}
yokofu_naito_52k72s = {
    'op': 'sfen ln1g3nl/2s1k1gs1/p1ppppb1p/1r7/9/2P4R1/PP1PPPP1P/1BG1K4/LNS2GSNL b 2P2p 25',
    '斎藤15歩': 'sfen ln1g3nl/2s1k1gs1/p1ppppb2/9/4b1P1p/2P4R1/P2PPP2P/1SG1KSG2/LN5NL b R3P2p 37',
    '68玉': 'sfen ln1g3nl/2s1k1gs1/p1ppppb1p/1r7/9/2P4R1/PP1PPPP1P/1BGK5/LNS2GSNL b 2P2p 25'
}
yokofu_naito_52k_nakahara = {
    '中住まい': 'sfen ln2g2nl/3sk1gs1/p1ppppb1p/1r7/9/2P4R1/PP1PPPP1P/1BG1KSG2/LNS4NL w 2P2p 28',
    '38銀': 'sfen ln2g2nl/3sk1gs1/p1ppppb1p/1r7/9/2P4R1/PP1PPPP1P/1BG1K1S2/LNS2G1NL b 2P2p 27',
    '68玉46歩': 'sfen ln2g2nl/3sk1gs1/p1ppppb1p/1r7/9/2P2P1R1/PP1PP1P1P/1BGK1S3/LNS2G1NL w 2P2p 28'
}
yokofu_naito_41k_nakahara = {
    '中住まい': 'sfen ln2gk1nl/3s2gs1/p1ppppb1p/1r7/9/2P4R1/PP1PPPP1P/1BG1KSG2/LNS4NL w 2P2p 28',
    '38銀': 'sfen ln2gk1nl/3s2gs1/p1ppppb1p/1r7/9/2P4R1/PP1PPPP1P/1BG1K1S2/LNS2G1NL b 2P2p 27',
    '68玉46歩': 'sfen ln2gk1nl/3s2gs1/p1ppppb1p/1r7/9/2P2P1R1/PP1PP1P1P/1BGK1S3/LNS2G1NL w 2P2p 28'
}
yokofu_naito_52k_nakazumai = {
    '中住まい': 'sfen ln5nl/2gsk1gs1/p1ppppb1p/1r7/9/2P4R1/PP1PPPP1P/1BG1KSG2/LNS4NL w 2P2p 28',
    '38銀': 'sfen ln5nl/2gsk1gs1/p1ppppb1p/1r7/9/2P4R1/PP1PPPP1P/1BG1K1S2/LNS2G1NL b 2P2p 27',
    '68玉46歩': 'sfen ln2g2nl/3sk1gs1/p1ppppb1p/1r7/9/2P2P1R1/PP1PP1P1P/1BGK1S3/LNS2G1NL w 2P2p 28'
}
yokofu_naito = {
    '豊島アタック': 'sfen lnsg3Bl/3k2gs1/p1ppppn1p/1r7/9/2P4R1/PP1PPPP1P/2G6/LNS1KGSNL w 2Pb2p 26',
    '52玉72銀': yokofu_naito_52k72s,
    '52玉中原': yokofu_naito_52k_nakahara,
    '41玉中原': yokofu_naito_41k_nakahara,
    '中住まい': yokofu_naito_52k_nakazumai
}
yokofu_chuza_41k_nakahara = {
    '中住まい': 'sfen ln2gk1nl/3s2gs1/p1ppppb1p/9/1r7/2P4R1/PP1PPPP1P/1BG1KSG2/LNS4NL w 2P2p 28',
    '新山崎': 'sfen ln2gk1nl/3s2gs1/p2pppb1p/2p6/1r4P2/2P4R1/PP1PPPN1P/1BG2S3/LNS1KG2L w 2P2p 30',
    '58玉中原': 'sfen l3gk1nl/3s2gs1/p1npppb1p/2p6/1r7/2P4R1/PPBPPPP1P/2GSKS3/LN2G2NL w 2P2p 32',
    '69玉中原': 'sfen l3gk1nl/3s2gs1/p1npppb1p/2p6/1r7/2P4R1/PPBPPPP1P/2GS1S3/LN1KG2NL w 2P2p 32'
}
yokofu_chuza_52k_nakahara = {
    '中住まい': 'sfen ln2g2nl/3sk1gs1/p1ppppb1p/9/1r7/2P4R1/PP1PPPP1P/1BG1KSG2/LNS4NL w 2P2p 28',
    '58玉中原': 'sfen l3g2nl/3sk1gs1/p1npppb1p/2p6/1r7/2P4R1/PPBPPPP1P/2GSKS3/LN2G2NL w 2P2p 32',
    '69玉中原': 'sfen l3g2nl/3sk1gs1/p1npppb1p/2p6/1r7/2P4R1/PPBPPPP1P/2GS1S3/LN1KG2NL w 2P2p 32'
}
yokofu_chuza_52k72s = {
    'op': 'sfen ln1g3nl/2s1k1gs1/p1ppppb1p/9/1r7/2P4R1/PP1PPPP1P/1BG1K4/LNS2GSNL b 2P2p 25'
}
yokofu_chuza_52k_nakazumai = {
    '中住まい': 'sfen ln5nl/2gsk1gs1/p1ppppb1p/9/1r7/2P4R1/PP1PPPP1P/1BG1KSG2/LNS4NL w 2P2p 28',
    '38銀': 'sfen ln5nl/2gsk1gs1/p1ppppb1p/9/1r7/2P4R1/PP1PPPP1P/1BG1K1S2/LNS2G1NL b 2P2p 27'
}
yokofu_chuza = {
    '41玉中原': yokofu_chuza_41k_nakahara,
    '52玉中原': yokofu_chuza_52k_nakahara,
    '中住まい': yokofu_chuza_52k_nakazumai,
    '52玉72銀': yokofu_chuza_52k72s
}
yokofu = {
    '23歩': yokofu_gosenzo,
    '33桂': yokofu_waki,
    '相横歩': yokofu_each,
    '38歩': yokofu_38p,
    '28歩': yokofu_28p,
    '33角': yokofu_33b,
    '84飛': yokofu_naito,
    '85飛': yokofu_chuza
}

kakugawari_bou = {}
kakugawari_hayakuri = {}
kakugawari_koshikake = {}

kakugawari = {
    '棒銀': kakugawari_bou,
    '早繰り銀': kakugawari_hayakuri,
    '腰掛銀': kakugawari_koshikake
}

kakugawari_tezon = {}

yagura_op = {
    '66歩': 'sfen lnsgkgsnl/1r5b1/p1pppp1pp/1p4p2/9/2PP5/PP2PPPPP/1B1S3R1/LN1GKGSNL w - 6',
    '77銀': 'sfen lnsgkgsnl/1r5b1/p1pppp1pp/1p4p2/9/2P6/PPSPPPPPP/1B5R1/LN1GKGSNL w - 6',
    '新24手組': 'sfen ln3kbnl/1r1sg1g2/p2p2spp/1pp1ppp2/9/2PPP1P2/PPSG1P1PP/2G2S1R1/LNBK3NL b - 25'
}
yagura_kato = {}
yagura_46s37n = {
    '25桂': 'sfen ln5nl/1r4gk1/3psg1p1/1pp1pPpsp/p4S1N1/2PPP+bPPP/PPSG5/1KG3R1L/LN7 w Bp 60',
    '25桂93飛': 'sfen ln4k1l/1r7/r3+Pgn2/1pp1ppppp/p6N1/2P1P1+bPP/PPSG5/1KG2s2L/LN7 b GSPbs2p 83',
    '宮田': 'sfen ln5nl/1r4gk1/2bpsg1p1/1pp1pppsp/p2P5/2P1PSPPP/PPSG1PN2/1KGB2R1L/LN7 w - 46',
    '91手': 'sfen l+R7/6pk1/6gpp/2ppp4/pp5+sl/2P1P4/PPSG1P3/1KG6/LN7 w 2SN2Pr2bg2nl3p 92',
    'Ponanza': 'sfen ln5nl/1r3sgk1/2b2g1pP/2p1ppp2/pp1p3Np/2P1P2P1/PPSG1Ps2/1KGB2R1L/LN7 b S2p 63'
}
yagura_45p = {
    'op': 'sfen ln5nl/1r1s2gk1/3p1gspp/pppbp1p2/5p3/2PPPSPP1/PPSG1P2P/1KGB3R1/LN5NL b - 1'
}
yagura_35p = {
    'op': 'sfen ln3k1nl/1r1sg1g2/p2p2spp/1ppbppp2/6P2/2PPP4/PPSG1P1PP/2G2S2R/LNBK3NL w - 28'
}
yagura_fujii = {
    'op': 'sfen ln5nl/1r1sg1gk1/p2p2spp/2pbppp2/1p5P1/2PPPBP2/PPSG1PS1P/2KG3R1/LN5NL w - 34'
}
yagura_morishita = {
    'op': 'sfen ln3kbnl/1r1s2g2/p2p1gspp/1pp1ppp2/9/2PPP1PP1/PPSG1P2P/2GB1S1R1/LN1K3NL w - 1',
    '47銀同型': 'sfen l6nl/1r3bgk1/p1ns1gspp/2ppppp2/1p5P1/2PPPPP2/PPSG1SN1P/1KGB3R1/LN6L b - 41',
    '棒銀': 'sfen ln5nl/1r3bgk1/3p1gspp/psp1ppp2/1p1P5/2PSP1PP1/PPSG1PN1P/1KGB2R2/LN6L w - 42',
    '雀': '1n3kbnl/r2sg1g2/l2p2spp/1pp1ppp2/p8/2PPP1PP1/PPSG1P2P/1KGB1S1R1/LN5NL b - 33',
    '雀深浦': '1n3kbnl/r2sg1g2/l2p2spp/1pp1ppp2/p3P4/2PP1SP2/PPSG1P1PP/2GB3R1/LNK4NL w - 34'
}
yagura_waki = {
    'op': 'sfen ln5nl/1r4gk1/p1sp1gspp/2pbppp2/1p5P1/2PPPBP2/PPSG1PS1P/1KG4R1/LN5NL b - 37',
    'GPS': 'sfen ln5nl/1r4gk1/p2p1gsp1/1s1bppp1p/1pP4P1/3PP1P1P/PPSG1PS2/1KGB3R1/LN5NL b P 43'
}
yagura_suzume = {}
yagura_nakahara = {}
yagura_yonenaga = {
    'op': 'sfen l4k1nl/1r2g1gb1/p1ns1pspp/2ppp1p2/1p5P1/2PPP1P2/PPSG1P2P/2G2S1R1/LNBK3NL b - 29'
}
yagura_right4 = {}
yagura_yakura = {
    'op': 'sfen ln1g1k1nl/4rsgb1/p2s1p1pp/1pppp1p2/9/2PPP2P1/PPSG1PP1P/1BG2S1R1/LN1K3NL b - 23'
}
yagura_akutsu = {
    'op': 'sfen ln1g1k1nl/1r3sg2/p2psp1pp/2p3p2/1p2b4/2PP3P1/PPSG1PP1P/1BG2S1R1/LN1K3NL b Pp 25',
    '55歩': 'sfen ln1g1k1nl/5sg2/p1bp1p1pp/2rs2p2/1p2p4/3PPB1P1/PPSG1PP1P/2G2S1R1/LN1K3NL b Pp 35',
    '渡辺31玉' : 'sfen ln1g2knl/5sg2/p1bp1p1pp/2rs2p2/1p7/3PPB1P1/PPSG1PP1P/2G2S1R1/LN1K3NL b P2p 35',
    '渡辺33銀' : 'sfen ln1g1k1nl/1r4g2/p2pspspp/2p3p2/1p2b2P1/2PP5/PPSG1PP1P/1BG2S1R1/LN1K3NL b Pp 27'
}
yagura_left_mino = {}
yagura = {
    'op': yagura_op,
    '加藤': yagura_kato,
    '46銀37桂': yagura_46s37n,
    '45歩': yagura_45p,
    '35歩': yagura_35p,
    '藤井': yagura_fujii,
    '森下': yagura_morishita,
    '脇' : yagura_waki,
    '雀': yagura_suzume,
    '中原': yagura_nakahara,
    '米長': yagura_yonenaga,
    '右四間飛車': yagura_right4,
    '矢倉中飛車': yagura_yakura,
    '阿久津': yagura_akutsu,
    '左美濃': yagura_left_mino,
}

other = {
    '嬉野': 'uresino',
    '筋違い角': 'takeichi',
    'カニカニ銀': 'kojima',
    'パックマン': 'packman'
}

mate_basic = {
    '0': 'sfen 7+rk/7bl/9/9/9/9/9/9/9 b Nrb4g4s3n3l18p 1',
    '1': 'sfen 9/9/3pp4/+r2k1p3/2L1+p4/2+R6/B8/B8/9 b 4g4s4n3l14p 1',
    '2': 'sfen 6r2/6Sl1/5p3/4P1k1N/4s1B2/5RL2/7pL/4b1N2/6L2 b 4g2s2n15p 1',
    '3': 'sfen 6S2/5nnnk/9/8N/7S1/9/9/+r8/+r8 b 2B4g2s4l18p 1',
    '4': 'sfen 5R1nl/5Bsk1/7p1/8p/9/9/9/9/9 b GSrb3g2s3n3l16p 1',
    '5': 'sfen 4k4/9/9/9/9/4K4/9/9/9 b 2R2G2b2g4s4n4l18p 1',
    '6': 'sfen 9/5s2B/5pkP1/7p1/6l2/4R3p/9/9/9 b BSPr4g2s4n3l13p 1',
    '7': 'sfen 8l/8k/6RPb/5K3/9/9/9/9/9 b SPrb4g3s4n3l16p 1',
    '8': 'sfen 9/9/1g1l5/2G1l4/gl6B/gk7/1s1S5/lSpKS4/4Br3 b R4n17p 1',
    '9': 'sfen 5l1+PS/5p1Pk/8p/5R1B+p/9/6N2/9/9/9 b BSr4g2s3n3l13p 1'
}
mate_ex = {
    '0': 'sfen g1+P1k1+P+P+L/1p3P3/+R+p2pp1pl/1NNsg+p2+R/+b+nL+P1+p3/1P3ssP1/2P1+Ps2N/4+P1P1L/+B5G1g b - 1', # ミクロコスモス
    '1': 'sfen 9/9/9/9/4R2N1/3+BSG1R1/9/5G3/2Pk1S3 b b2g2s3n4l17p 1', # 詰将棋選手権：チャンピオン戦から
    '2': 'sfen 2Gp1n3/2r3G2/p1+L1S1S2/1pp+Bp1ppp/1k2l3n/5p3/PPPPPPPPP/1B5R1/LNSGKGSNL b - 1', # 攻方実戦初形
    '3': 'sfen bp1pppk2/g1+P6/2N5g/PR5PP/p2P4+P/1NS4p1/2S6/N2sSNp+pg/2+p2BG1r b 3Ll3p 1', # ベンハー
    '4': 'sfen +P1+Pgg2+P1/1+nP1+P2+sP/1p2N2l+P/+PP+P1P1+Pp1/3n2b2/1+P+p1B2r1/2+p3K1N/1+PS1L1G+ls/2L2kS+Rg b - 1', # 双玉還元玉煙詰
    '5': 'sfen 1+P1pS2+PR/2n2S1lg/1l3p1p1/1G2n1pS1/N1p2k3/3S2l2/4K1lgP/3P1+p2p/4Pg1PN b BPrb4p 1', # 最後の審判
    '6': 'sfen 3pl3p/1+Pn3pk1/2+p6/4+pG3/1K3p2P/+B5l1+B/+p3pS1+ll/p+p2PN3/3S1+sSPN b 2R2P3gn2p 1', # 木星の旅
    '7': 'sfen p2+N3g1/P2R3+pP/g3+BnpP1/lPP1+p3p/+LnnS2+LS+p/G+P1l+Bp+P1+p/3pp1P1g/9/4kSR1s b - 1', # 新桃源郷
    '8': 'sfen 9/5lPS+p/4SnpS+p/1+P2+P2pg/2+P+PL4/lppp1pBk1/r3p3N/3GsR3/+p2G1NKP1 b B2Pgnl 1', # 特異点
    '9': 'sfen 1p3p3/4gP1p1/3+Pp1nl+p/5+P+NlN/+p1Bs1sGlG/3+RS2ln/2Gp+p1k1b/2P+RS2Pp/P4+p3 b 2P 1' # 幻想飛行
}
mate = {
    '通常': mate_basic,
    '高難度': mate_ex
}

test = {
    '羽生 加藤 52銀': 'sfen ln1g5/1r2S1k2/p2pppn2/2ps2p2/1p7/2P6/PPSPPPPLP/2G2K1pr/LN4G1b w BGSLPnp 62',
    '羽生 三浦 86飛': 'sfen l6nl/2B3gk1/p2gp1sp1/5pp1p/6P2/1rP4PP/PpSGP2sR/L8/KNGs3+bL b N4Pnp 69',
    '羽生 渡辺 66銀': 'sfen l7l/g1S6/k1n4pp/ppN3p2/2p4P1/PP1s1bP2/KSNP4P/1G7/L1bS4L b 2RN5P2gp 123',
    '羽生 阿久津 56銀': 'sfen l1r3knl/P2+B1ggPp/1Sn1p2p1/3p2P1P/2n2P2L/pPp1s4/1p1PP4/K1GS1G3/LN5R1 b 2Pbsp 79',
    '谷川 羽生 77桂': 'sfen l6nl/3r1sgk1/2s+B2g2/p4Pp1p/1pp1Sp1p1/P1S1G1PPP/1Pn1P4/1KG6/LN1Rb3L b N3Pp 71',
    '天彦 盤上のシンデレラ54銀':'sfen l5knl/1r2g1g2/p3p2p1/2p1Sp1sp/1p3N3/P1P2P2P/1P2P+p3/2G1G1b2/LNKR4L w BSNPs3p 56',
    '森内 深浦 12銀': 'sfen l3s1+P2/5+r2s/8k/p3P1pR1/9/PSGP3L1/1P5P1/1KG+p+p4/LNG6 b 3N5P2bgsl3p 149',
    '森内 羽生 2枚飛車2枚角': 'sfen lnsg2snl/4k1g2/2pppp1pp/6p2/p8/1GPb2S2/P2RPPP1P/1S5R1/LN2KG1NL w 3Pbp 36',
    '谷川 大山 角不成': 'sfen ln1g2p2/pgks2g2/1p1p3g+R/P1p3B2/N5P2/2P1+pp3/1PSP4P/2K6/LNS3L1L b BSN4Prp 79',
    '杉本 渡辺 角不成変形': 'sfen 1n5nk/4pB3/5p1s1/p2+r2p2/1PP1P2pl/9/P5gsK/3+pg3L/1N5+B1 b R2G2S2L4Pn4p 1'
}
start = {
    '平手': 'sfen lnsgkgsnl/1r5b1/ppppppppp/9/9/9/PPPPPPPPP/1B5R1/LNSGKGSNL b - 1',
    '香': 'sfen lnsgkgsn1/1r5b1/ppppppppp/9/9/9/PPPPPPPPP/1B5R1/LNSGKGSNL w - 1',
    '右香': 'sfen 1nsgkgsnl/1r5b1/ppppppppp/9/9/9/PPPPPPPPP/1B5R1/LNSGKGSNL w - 1',
    '桂': 'sfen lnsgkgs1l/1r5b1/ppppppppp/9/9/9/PPPPPPPPP/1B5R1/LNSGKGSNL w - 1',
    '右桂': 'sfen l1sgkgsnl/1r5b1/ppppppppp/9/9/9/PPPPPPPPP/1B5R1/LNSGKGSNL w - 1',
    '銀': 'sfen lnsgkg1nl/1r5b1/ppppppppp/9/9/9/PPPPPPPPP/1B5R1/LNSGKGSNL w - 1',
    '右銀': 'sfen ln1gkgsnl/1r5b1/ppppppppp/9/9/9/PPPPPPPPP/1B5R1/LNSGKGSNL w - 1',
    '金': 'sfen lnsgk1snl/1r5b1/ppppppppp/9/9/9/PPPPPPPPP/1B5R1/LNSGKGSNL w - 1',
    '右金': 'sfen lns1kgsnl/1r5b1/ppppppppp/9/9/9/PPPPPPPPP/1B5R1/LNSGKGSNL w - 1',
    '両香': 'sfen 1nsgkgsn1/1r5b1/ppppppppp/9/9/9/PPPPPPPPP/1B5R1/LNSGKGSNL w - 1',
    '両桂': 'sfen l1sgkgs1l/1r5b1/ppppppppp/9/9/9/PPPPPPPPP/1B5R1/LNSGKGSNL w - 1',
    '両銀': 'sfen ln1gkg1nl/1r5b1/ppppppppp/9/9/9/PPPPPPPPP/1B5R1/LNSGKGSNL w - 1',
    '両金': 'sfen lns1k1snl/1r5b1/ppppppppp/9/9/9/PPPPPPPPP/1B5R1/LNSGKGSNL w - 1',
    '桂香': 'sfen lnsgkgs11/1r5b1/ppppppppp/9/9/9/PPPPPPPPP/1B5R1/LNSGKGSNL w - 1',
    '右桂香': 'sfen 11sgkgsnl/1r5b1/ppppppppp/9/9/9/PPPPPPPPP/1B5R1/LNSGKGSNL w - 1',
    '桂右香': 'sfen 1nsgkgs1l/1r5b1/ppppppppp/9/9/9/PPPPPPPPP/1B5R1/LNSGKGSNL w - 1',
    '香右桂': 'sfen l1sgkgsn1/1r5b1/ppppppppp/9/9/9/PPPPPPPPP/1B5R1/LNSGKGSNL w - 1',
    '両桂香': 'sfen 11sgkgs11/1r5b1/ppppppppp/9/9/9/PPPPPPPPP/1B5R1/LNSGKGSNL w - 1',
    '飛': 'sfen lnsgkgsnl/7b1/ppppppppp/9/9/9/PPPPPPPPP/1B5R1/LNSGKGSNL w - 1',
    '角': 'sfen lnsgkgsnl/1r7/ppppppppp/9/9/9/PPPPPPPPP/1B5R1/LNSGKGSNL w - 1',
    '飛香': 'sfen lnsgkgsn1/7b1/ppppppppp/9/9/9/PPPPPPPPP/1B5R1/LNSGKGSNL w - 1',
    '飛右香': 'sfen 1nsgkgsnl/7b1/ppppppppp/9/9/9/PPPPPPPPP/1B5R1/LNSGKGSNL w - 1',
    '角香': 'sfen lnsgkgsn1/1r7/ppppppppp/9/9/9/PPPPPPPPP/1B5R1/LNSGKGSNL w - 1',
    '角右香': 'sfen 1nsgkgsnl/1r7/ppppppppp/9/9/9/PPPPPPPPP/1B5R1/LNSGKGSNL w - 1',
    '２枚': 'sfen lnsgkgsnl/9/ppppppppp/9/9/9/PPPPPPPPP/1B5R1/LNSGKGSNL w - 1',
    '４枚': 'sfen 1nsgkgsn1/9/ppppppppp/9/9/9/PPPPPPPPP/1B5R1/LNSGKGSNL w - 1',
    '６枚': 'sfen 2sgkgs2/9/ppppppppp/9/9/9/PPPPPPPPP/1B5R1/LNSGKGSNL w - 1',
    '８枚': 'sfen 3gkg3/9/ppppppppp/9/9/9/PPPPPPPPP/1B5R1/LNSGKGSNL w - 1',
    '後手飛角逆': 'sfen lnsgkgsnl/1b5r1/ppppppppp/9/9/9/PPPPPPPPP/1B5R1/LNSGKGSNL b - 1',
    '５三歩': 'sfen lnsgkgsnl/1r5b1/pppp1pppp/9/9/9/PPPPPPPPP/1B5R1/LNSGKGSNL w - 1',
    '５七と': 'sfen lnsgkgsnl/1r5b1/ppppppppp/9/9/9/PPPP+PPPPP/1B5R1/LNSGKGSNL b - 1',
    '先手飛': 'sfen lnsgkgsnl/1r5b1/ppppppppp/9/9/9/PPPPPPPPP/1B5R1/LNSGKGSNL b R 1',
    '先手角': 'sfen lnsgkgsnl/1r5b1/ppppppppp/9/9/9/PPPPPPPPP/1B5R1/LNSGKGSNL b B 1',
    '先手金': 'sfen lnsgkgsnl/1r5b1/ppppppppp/9/9/9/PPPPPPPPP/1B5R1/LNSGKGSNL b G 1',
    '先手銀': 'sfen lnsgkgsnl/1r5b1/ppppppppp/9/9/9/PPPPPPPPP/1B5R1/LNSGKGSNL b S 1',
    '先手桂': 'sfen lnsgkgsnl/1r5b1/ppppppppp/9/9/9/PPPPPPPPP/1B5R1/LNSGKGSNL b N 1',
    '先手香': 'sfen lnsgkgsnl/1r5b1/ppppppppp/9/9/9/PPPPPPPPP/1B5R1/LNSGKGSNL b L 1',
    '先手歩': 'sfen lnsgkgsnl/1r5b1/ppppppppp/9/9/9/PPPPPPPPP/1B5R1/LNSGKGSNL b P 1',
    '先手１森下': 'sfen lnsgkgsnl/1r5b1/ppppppppp/9/9/9/PPPPPPPPP/1B5R1/LNSGKGSNL b 5P 1'
}

subject = {
    '初形': start,
    '先手中飛車': black_5,
    'ゴキゲン中飛車': kondo,
    '先手四間飛車': black_4,
    '後手四間飛車': white_4,
    '先手三間飛車': black_3,
    '後手三間飛車': white_3,
    '先手向かい飛車': black_2,
    '後手向かい飛車': white_2,
    '先手藤井システム': black_fujii,
    '後手藤井システム': white_fujii,
    '先手角交換四間飛車': black_kks,
    '後手角交換四間飛車': white_kks,
    '相振り飛車': aifuri,
    '相掛かり': aigakari,
    '横歩取り': yokofu,
    '角換わり': kakugawari,
    '一手損角換わり': kakugawari_tezon,
    '矢倉': yagura,
    'その他': other,
    '詰将棋': mate,
    'test': test
}
