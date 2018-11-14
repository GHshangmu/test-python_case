stations_dict_res = {'VAP': '北京北', 'BOP': '北京东', 'BJP': '北京', 'VNP': '北京南', 'BXP': '北京西', 'IZQ': '广州南', 'CUW': '重庆北', 'CQW': '重庆', 'CRW': '重庆南', 'GGQ': '广州东', 'SHH': '上海', 'SNH': '上海南', 'AOH': '上海虹桥', 'SXH': '上海西', 'TBP': '天津北', 'TJP': '天津', 'TIP': '天津南', 'TXP': '天津西', 'CCT': '长春', 'CET': '长春南', 'CRT': '长春西', 'ICW': '成都东', 'CNW': '成都南', 'CDW': '成都', 'CSQ': '长沙', 'CWQ': '长沙南', 'FZS': '福州', 'FYS': '福州南', 'GIW': '贵阳', 'GZQ': '广州', 'GXQ': '广州西', 'HBB': '哈尔滨', 'VBB': '哈尔滨东', 'VAB': '哈尔滨西', 'HFH': '合肥', 'HTH': '合肥西', 'NDC': '呼和浩特东', 'HHC': '呼和浩特', 'KEQ': '口东', 'HMQ': '海口东', 'VUQ': '海口', 'HGH': '杭州东', 'HZH': '杭州', 'XHH': '杭州南', 'JNK': '济南', 'JAK': '济南东', 'JGK': '济南西', 'KMM': '昆明', 'KXM': '昆明西', 'LSO': '拉萨', 'LVJ': '兰州东', 'LZJ': '兰州', 'LAJ': '兰州西', 'NCG': '南昌', 'NJH': '南京', 'NKH': '南京南', 'NNZ': '南宁', 'VVP': '石家庄北', 'SJP': '石家庄', 'SYT': '沈阳', 'SBT': '沈阳北', 'SDT': '沈阳东', 'TBV': '太原北', 'TDV': '太原东', 'TYV': '太原', 'WHN': '武汉', 'KNM': '王家营西', 'WMR': '乌鲁木齐南', 'EAY': '西安北', 'XAY': '西安', 'CAY': '西安南', 'XNO': '西宁', 'YIJ': '银川', 'ZZF': '郑州', 'ART': '阿尔山', 'AKY': '安康', 'ASR': '阿克苏', 'AHX': '阿里河', 'AKR': '阿拉山口', 'APT': '安平', 'AQH': '安庆', 'ASW': '安顺', 'AST': '鞍山', 'AYF': '安阳', 'BAB': '北安', 'BBH': '蚌埠', 'BCT': '白城', 'BHZ': '北海', 'BEL': '白河', 'BAP': '白涧', 'BJY': '宝鸡', 'BJB': '滨江', 'BKX': '博克图', 'BIZ': '百色', 'HJL': '白山市', 'BTT': '北台', 'BDC': '包头东', 'BTC': '包头', 'BXR': '北屯市', 'BXT': '本溪', 'BEC': '白云鄂博', 'BXJ': '白银西', 'BZH': '亳州', 'CBN': '赤壁', 'VGQ': '常德', 'CDP': '承德', 'CDT': '长甸', 'CFD': '赤峰', 'CDG': '茶陵', 'CEH': '苍南', 'CPP': '昌平', 'CRG': '崇仁', 'CTT': '昌图', 'CDB': '长汀镇', 'CXK': '曹县', 'COM': '楚雄南', 'CXT': '陈相屯', 'CBF': '长治北', 'IYH': '池州', 'CZJ': '长征', 'CZH': '常州', 'CZQ': '郴州', 'CZF': '长治', 'COP': '沧州', 'CZZ': '崇左', 'RNT': '大安北', 'DCT': '大成', 'DUT': '丹东', 'DFB': '东方红', 'DMQ': '东莞东', 'DHD': '大虎山', 'DHJ': '敦煌', 'DHL': '敦化', 'DHT': '德惠', 'DJB': '东京城', 'DFP': '大涧', 'DDW': '都江堰', 'DFT': '大连北', 'DKM': '大理', 'DLT': '大连', 'DNG': '定南', 'DZX': '大庆', 'DOC': '东胜', 'DQT': '大石桥', 'DTV': '大同', 'DPK': '东营', 'DUX': '大杨树', 'RYW': '都匀', 'DOF': '邓州', 'RXW': '达州', 'DZP': '德州', 'EJC': '额济纳', 'RLC': '二连', 'ESN': '恩施', 'FES': '福鼎', 'FJQ': '凤凰机场', 'FLV': '风陵渡', 'FLW': '涪陵', 'FRX': '富拉尔基', 'FET': '抚顺北', 'FSQ': '佛山', 'FXD': '阜新南', 'FYH': '阜阳', 'GRO': '格尔木', 'GHW': '广汉', 'GJV': '古交', 'GBZ': '桂林北', 'GRX': '古莲', 'GLZ': '桂林', 'GXN': '固始', 'GSN': '广水', 'GNJ': '干塘', 'GYW': '广元', 'GBQ': '广州北', 'GZG': '赣州', 'GLT': '公主岭', 'GBT': '公主岭南', 'AUH': '淮安', 'HRH': '淮北', 'HMB': '鹤北', 'HVN': '淮滨', 'HBV': '河边', 'KCN': '潢川', 'HCY': '韩城', 'HDP': '邯郸', 'HDB': '横道河子', 'HGB': '鹤岗', 'HTT': '皇姑屯', 'HEM': '红果', 'HJB': '黑河', 'HHQ': '怀化', 'HKN': '汉口', 'HLD': '葫芦岛', 'HRX': '海拉尔', 'HWD': '霍林郭勒', 'HLB': '海伦', 'HMV': '侯马', 'HMR': '哈密', 'HAH': '淮南', 'HNB': '桦南', 'EUH': '海宁西', 'HQM': '鹤庆', 'HBP': '怀柔北', 'HRP': '怀柔', 'OSN': '黄石东', 'HSY': '华山', 'HKH': '黄山', 'HSN': '黄石', 'HSP': '衡水', 'HYQ': '衡阳', 'HIK': '菏泽', 'HXZ': '贺州', 'HOY': '汉中', 'HCQ': '惠州', 'VAG': '吉安', 'JAL': '集安', 'JBG': '江边村', 'JCF': '晋城', 'JJZ': '金城江', 'JCG': '景德镇', 'JFF': '嘉峰', 'JGX': '加格达奇', 'JGG': '井冈山', 'JHL': '蛟河', 'RNH': '金华南', 'JBH': '金华', 'JJG': '九江', 'JLL': '吉林', 'JMN': '荆门', 'JMB': '佳木斯', 'JIK': '济宁', 'JAC': '集宁南', 'JQJ': '酒泉', 'JUH': '江山', 'JIQ': '吉首', 'JTL': '九台', 'JVJ': '镜铁山', 'JXB': '鸡西', 'JRH': '绩溪县', 'JGJ': '嘉峪关', 'JFW': '江油', 'JZD': '锦州', 'JZT': '金州', 'JKP': '蓟州', 'KLR': '库尔勒', 'KFF': '开封', 'KLV': '岢岚', 'KLW': '凯里', 'KSR': '喀什', 'KNH': '昆山南', 'KTR': '奎屯', 'KYT': '开原', 'UAH': '六安', 'LBF': '灵宝', 'UCH': '芦潮港', 'LCW': '隆昌', 'LKZ': '陆川', 'LCN': '利川', 'LCG': '临川', 'UTP': '潞城', 'LDL': '鹿道', 'LDQ': '娄底', 'LFV': '临汾', 'LGP': '良各庄', 'LHC': '临河', 'LON': '漯河', 'LWJ': '绿化', 'UHP': '隆化', 'LHM': '丽江', 'LQL': '临江', 'LJL': '龙井', 'LHV': '吕梁', 'LLG': '醴陵', 'LKV': '柳林南', 'UPP': '滦平', 'UMW': '六盘水', 'LVV': '灵丘', 'LST': '旅顺', 'LWH': '兰溪', 'LXJ': '陇西', 'LEQ': '澧县', 'UEP': '临西', 'LYS': '龙岩', 'LYQ': '耒阳', 'LYF': '洛阳', 'UKH': '连云港东', 'LDF': '洛阳东', 'LVK': '临沂', 'LLF': '洛阳龙门', 'DHR': '柳园', 'LYD': '凌源', 'LYL': '辽源', 'LZX': '立志', 'LZZ': '柳州', 'LZD': '辽中', 'MCN': '麻城', 'MDX': '免渡河', 'MDB': '牡丹江', 'MRX': '莫尔道嘎', 'MGH': '明光', 'MHX': '满归', 'MVX': '漠河', 'MDQ': '茂名', 'MMZ': '茂名西', 'MSB': '密山', 'MJT': '马三家', 'VAW': '麻尾', 'MYW': '绵阳', 'MOQ': '梅州', 'MLX': '满洲里', 'NVH': '宁波东', 'NGH': '宁波', 'NCB': '南岔', 'NCW': '南充', 'NDZ': '南丹', 'NMP': '南大庙', 'NFT': '南芬', 'NHX': '讷河', 'NGX': '嫩江', 'NJW': '内江', 'NPS': '南平', 'NUH': '南通', 'NFF': '南阳', 'NZX': '碾子山', 'PEN': '平顶山', 'PVD': '盘锦', 'PIJ': '平凉', 'POJ': '平凉南', 'PQP': '平泉', 'PSQ': '坪石', 'PXG': '萍乡', 'PXZ': '凭祥', 'PCW': '郫县西', 'PRW': '攀枝花', 'QRN': '蕲春', 'QSW': '青城山', 'QDK': '青岛', 'QYP': '清河城', 'QJM': '曲靖', 'QNW': '黔江', 'QEB': '前进镇', 'QHX': '齐齐哈尔', 'QTB': '七台河', 'QVV': '沁县', 'QRS': '泉州东', 'QYS': '泉州', 'QEH': '衢州', 'RAZ': '融安', 'RQJ': '汝箕沟', 'RJG': '瑞金', 'RZK': '日照', 'SCB': '双城堡', 'SFB': '绥芬河', 'SGQ': '韶关东', 'SHD': '山海关', 'SHB': '绥化', 'SFX': '三间房', 'SXT': '苏家屯', 'SLL': '舒兰', 'SMS': '三明', 'OMY': '神木', 'SMF': '三门峡', 'ONY': '商南', 'NIW': '遂宁', 'SPT': '四平', 'SQF': '商丘', 'SRG': '上饶', 'SSQ': '韶山', 'OAH': '宿松', 'OTQ': '汕头', 'SWS': '邵武', 'OEP': '涉县', 'SEQ': '三亚', 'JUQ': '亚', 'SYQ': '邵阳', 'SNN': '十堰', 'SSB': '双鸭山', 'VYT': '松原', 'SZH': '苏州', 'SZQ': '深圳', 'OXH': '宿州', 'SZN': '随州', 'SUV': '朔州', 'OSQ': '深圳西', 'TBQ': '塘豹', 'TVX': '塔尔气', 'TGY': '潼关', 'TGP': '塘沽', 'TXX': '塔河', 'THL': '通化', 'TLX': '泰来', 'TFR': '吐鲁番', 'TLD': '通辽', 'TLT': '铁岭', 'TPT': '陶赖昭', 'TML': '图们', 'RDQ': '铜仁', 'FUP': '唐山北', 'TFT': '田师府', 'TAK': '泰山', 'TSP': '唐山', 'TSJ': '天水', 'TYT': '通远堡', 'TQT': '太阳升', 'UTH': '泰州', 'TZW': '桐梓', 'TAP': '通州西', 'WCB': '五常', 'WCN': '武昌', 'WDT': '瓦房店', 'WKK': '威海', 'WHH': '芜湖', 'WXC': '乌海西', 'WJT': '吴家屯', 'WLW': '武隆', 'WWT': '乌兰浩特', 'WNY': '渭南', 'WSM': '威舍', 'WIT': '歪头山', 'WUJ': '武威', 'WWJ': '武威南', 'WXH': '无锡', 'WXR': '乌西', 'WPB': '乌伊岭', 'WAS': '武夷山', 'WYY': '万源', 'WYW': '万州', 'WZZ': '梧州', 'RZH': '温州', 'VRH': '温州南', 'ECW': '西昌', 'XCF': '许昌', 'ENW': '西昌南', 'XFB': '香坊', 'XGV': '轩岗', 'EUG': '兴国', 'XHY': '宣汉', 'EFQ': '新会', 'XLQ': '新晃', 'XTC': '锡林浩特', 'EXP': '兴隆县', 'XKS': '厦门北', 'XMS': '厦门', 'XBS': '厦门高崎', 'XST': '小市', 'ETW': '秀山', 'XTG': '向塘', 'XWM': '宣威', 'XXF': '新乡', 'XUN': '信阳', 'XYY': '咸阳', 'XFN': '襄阳', 'XYT': '熊岳城', 'VIH': '新沂', 'XRZ': '兴义', 'XUG': '新余', 'XCH': '徐州', 'YWY': '延安', 'YBW': '宜宾', 'YWB': '亚布力南', 'YBD': '叶柏寿', 'HAN': '宜昌东', 'YCW': '永川', 'AFH': '盐城', 'YCN': '宜昌', 'YNV': '运城', 'YCB': '伊春', 'YCV': '榆次', 'YBP': '杨村', 'YCG': '宜春西', 'YET': '伊尔施', 'YGW': '燕岗', 'YIV': '永济', 'YJL': '延吉', 'YKT': '营口', 'YKX': '牙克石', 'YNY': '阎良', 'YLZ': '玉林', 'ALY': '榆林', 'TWQ': '亚龙湾', 'YPB': '一面坡', 'YMR': '伊宁', 'YAY': '阳平关', 'YZW': '玉屏', 'YPV': '原平', 'YNP': '延庆', 'YYV': '阳泉曲', 'YQB': '玉泉', 'AQP': '阳泉', 'NUW': '营山', 'YNG': '玉山', 'AOP': '燕山', 'YRT': '榆树', 'YTG': '鹰潭', 'YAK': '烟台', 'YEX': '伊图里河', 'ATP': '玉田县', 'YWH': '义乌', 'YON': '阳新', 'YXD': '义县', 'AEQ': '益阳', 'YYQ': '岳阳', 'YUQ': '崖州', 'AOQ': '永州', 'YLH': '扬州', 'ZBK': '淄博', 'ZDV': '镇城底', 'ZGW': '自贡', 'ZHQ': '珠海', 'ZIQ': '珠海北', 'ZJZ': '湛江', 'ZJH': '镇江', 'DIQ': '张家界', 'ZKP': '张家口', 'ZMP': '张家口南', 'ZKN': '周口', 'ZLC': '哲里木', 'ZTX': '扎兰屯', 'ZDN': '驻马店', 'ZVQ': '肇庆', 'ZIT': '周水子', 'ZDW': '昭通', 'ZWJ': '中卫', 'ZYW': '资阳', 'ZIW': '遵义西', 'ZEK': '枣庄', 'ZZW': '资中', 'ZZQ': '株洲', 'ZFK': '枣庄西', 'AAX': '昂昂溪', 'ACB': '阿城', 'ADX': '安达', 'ARW': '安德', 'ADP': '安定', 'ADO': '安多', 'AGT': '安广', 'YED': '敖汉', 'AHP': '艾河', 'PKQ': '安化', 'AJJ': '艾家村', 'ARH': '鳌江', 'AJB': '安家', 'AJD': '阿金', 'PYW': '安靖', 'AER': '阿克陶', 'AYY': '安口窑', 'ALD': '敖力布告', 'AUZ': '安龙', 'ASX': '阿龙山', 'ALN': '安陆', 'JTX': '阿木尔', 'AZM': '阿南庄', 'APH': '安庆西', 'AXT': '鞍山西', 'ATV': '安塘', 'ASH': '安亭北', 'ATR': '阿图什', 'ATL': '安图', 'AXS': '安溪', 'BWQ': '博鳌', 'BPW': '北碚', 'BGV': '白壁关', 'BMH': '蚌埠南', 'BCR': '巴楚', 'BUP': '板城', 'BEP': '北戴河', 'BDP': '保定', 'BPP': '宝坻', 'ILP': '八达岭', 'BNN': '巴东', 'BGM': '柏果', 'BUT': '布海', 'BIY': '白河东', 'BVC': '贲红', 'BWH': '宝华山', 'BEY': '白河县', 'BJJ': '白芨沟', 'BJM': '碧鸡关', 'IBQ': '北滘', 'BLQ': '碧江', 'BBM': '白鸡坡', 'BSB': '笔架山', 'BTD': '八角台', 'BKD': '保康', 'BKB': '白奎堡', 'BAT': '白狼', 'BRZ': '百浪', 'BOR': '博乐', 'BQC': '宝拉格', 'BLX': '巴林', 'BNB': '宝林', 'BOZ': '北流', 'BLB': '勃利', 'BLR': '布列开', 'BND': '宝龙山', 'AAP': '百里峡', 'BMD': '八面城', 'BNM': '班猫箐', 'BMB': '八面通', 'BRP': '北马圈子', 'RPD': '北票南', 'BQP': '白旗', 'BQB': '宝泉岭', 'BQL': '白泉', 'BAY': '巴山', 'BSY': '白水江', 'BPM': '白沙坡', 'BAL': '白石山', 'BUM': '白水镇', 'FDC': '东', 'BTQ': '坂田', 'BZP': '泊头', 'BYP': '北屯', 'BHT': '本溪湖', 'BXK': '博兴', 'VXD': '八仙筒', 'BYC': '白音察干', 'BYB': '背荫河', 'BIV': '北营', 'BAC': '巴彦高勒', 'BID': '白音他拉', 'BYT': '鲅鱼圈', 'BNJ': '白银市', 'BCD': '白音胡硕', 'IEW': '巴中', 'RMP': '霸州', 'BVP': '北宅', 'CIN': '赤壁北', 'CBC': '查布嘎', 'CEJ': '长城', 'CCM': '长冲', 'CCP': '承德东', 'CID': '赤峰西', 'CAX': '嵯岗', 'CGT': '柴岗', 'CEF': '长葛', 'CGV': '柴沟堡', 'CGY': '城固', 'CAJ': '陈官营', 'CZB': '成高子', 'WBW': '草海', 'CHB': '柴河', 'CHZ': '册亨', 'CKT': '草河口', 'CHP': '崔黄口', 'CIH': '巢湖', 'CJT': '蔡家沟', 'CJX': '成吉思汗', 'CAM': '岔江', 'CJY': '蔡家坡', 'CLK': '昌乐', 'CYP': '超梁沟', 'CUQ': '慈利', 'CLP': '昌黎', 'CLT': '长岭子', 'CMB': '晨明', 'CNJ': '长农', 'VBP': '昌平北', 'DAQ': '常平', 'CPM': '长坡岭', 'CQB': '辰清', 'CON': '蔡山', 'CSB': '楚山', 'EFW': '长寿', 'CSP': '磁山', 'CST': '苍石', 'CSL': '草市', 'CSC': '察素齐', 'CVT': '长山屯', 'CES': '长汀', 'CPT': '昌图西', 'CQQ': '春湾', 'CIP': '磁县', 'CNZ': '岑溪', 'CXQ': '辰溪', 'CRP': '磁西', 'CFH': '长兴南', 'CYK': '磁窑', 'CYD': '朝阳', 'CAL': '春阳', 'CEK': '城阳', 'CEX': '创业村', 'CYL': '朝阳川', 'CDD': '朝阳地', 'CYF': '长垣', 'CZL': '朝阳镇', 'CUH': '滁州北', 'ESH': '常州北', 'CXH': '滁州', 'CKQ': '潮州', 'CVK': '常庄', 'CFP': '曹子里', 'CWM': '车转湾', 'ICQ': '郴州西', 'CBP': '沧州西', 'DAG': '德安', 'RAT': '大安', 'DBJ': '大坝', 'DBC': '大板', 'DBD': '大巴', 'RBT': '到保', 'DYJ': '定边', 'DBB': '东边井', 'RDT': '德伯斯', 'DGJ': '打柴沟', 'DVW': '德昌', 'DDB': '滴道', 'DKJ': '大磴沟', 'DRD': '刀尔登', 'DRX': '得耳布尔', 'UFQ': '东方', 'DGY': '丹凤', 'DIL': '东丰', 'DMM': '都格', 'DTT': '大官屯', 'RGW': '大关', 'DGP': '东光', 'DHB': '东海', 'DHP': '大灰厂', 'DQD': '大红旗', 'SOQ': '大禾塘', 'DQH': '东海县', 'DXT': '德惠西', 'DJT': '达家沟', 'DKB': '东津', 'DJL': '杜家', 'DKP': '大口屯', 'RVD': '东来', 'DHO': '德令哈', 'DLC': '大陆号', 'DLB': '带岭', 'DLD': '大林', 'DIC': '达拉特旗', 'DTX': '独立屯', 'DLV': '豆罗', 'DNC': '达拉特西', 'GZT': '大连西', 'DMD': '东明村', 'DEP': '洞庙河', 'DNF': '东明县', 'DNZ': '大拟', 'DPD': '大平房', 'RPP': '大盘石', 'DPI': '大埔', 'DVT': '大堡', 'LFX': '大庆东', 'DQX': '大其拉哈', 'DML': '道清', 'DQB': '对青山', 'MOH': '德清西', 'RHX': '大庆西', 'DRQ': '东升', 'DKH': '砀山', 'RWW': '独山', 'DWT': '登沙河', 'DPM': '读书铺', 'DSL': '大石头', 'DYC': '东胜西', 'RZT': '大石寨', 'DBH': '东台', 'DQK': '定陶', 'DGT': '灯塔', 'DBM': '大田边', 'DTL': '东通化', 'RUH': '丹徒', 'DNT': '大屯', 'DRJ': '东湾', 'DFJ': '大武口', 'DWJ': '低窝铺', 'DZZ': '大王滩', 'DFM': '大湾子', 'DXL': '大兴沟', 'DXX': '大兴', 'DSJ': '定西', 'DXM': '甸心', 'DXG': '东乡', 'DKV': '代县', 'DXV': '定襄', 'RXP': '东戌', 'DXD': '东辛庄', 'DYH': '丹阳', 'DYW': '德阳', 'DYX': '大雁', 'DYN': '当阳', 'EXH': '丹阳北', 'IAW': '大英东', 'DBV': '东淤地', 'DYV': '大营', 'EWH': '定远', 'RYV': '岱岳', 'DYZ': '大元', 'DJP': '大营镇', 'DZD': '大营子', 'DTJ': '大战场', 'DIP': '德州东', 'DCH': '东至', 'DVQ': '低庄', 'DNV': '东镇', 'DFZ': '道州', 'DZV': '东庄', 'DWV': '兑镇', 'ROP': '豆庄', 'DXP': '定州', 'DZY': '大竹园', 'DAP': '大杖子', 'RZP': '豆张庄', 'EBW': '峨边', 'RDP': '二道沟门', 'RDX': '二道湾', 'EEC': '鄂尔多斯', 'RLD': '二龙', 'ELA': '二龙山屯', 'EMW': '峨眉', 'RML': '二密河', 'RYJ': '二营', 'ECN': '鄂州', 'FAS': '福安', 'FCG': '丰城', 'FNG': '丰城南', 'FIH': '肥东', 'FEM': '发耳', 'FHX': '富海', 'FHR': '福海', 'FHT': '凤凰城', 'FEV': '汾河', 'FHH': '奉化', 'FIB': '富锦', 'FTT': '范家屯', 'FLJ': '福利区', 'FTB': '福利屯', 'FZB': '丰乐镇', 'FNH': '阜南', 'AKH': '阜宁', 'FNP': '抚宁', 'FQS': '福清', 'VMW': '福泉', 'FSJ': '丰水村', 'FUQ': '丰顺', 'FSV': '繁峙', 'FST': '抚顺', 'FKP': '福山口', 'FSZ': '扶绥', 'FTX': '冯屯', 'FYP': '浮图峪', 'FDY': '富县东', 'FXY': '凤县', 'FEY': '富县', 'FXK': '费县', 'FUH': '凤阳', 'FAV': '汾阳', 'FBT': '扶余北', 'FYG': '分宜', 'FYM': '富源', 'FYT': '扶余', 'FYX': '富裕', 'FBG': '抚州北', 'FZY': '凤州', 'FZC': '丰镇', 'VZK': '范镇', 'GFP': '固安', 'VJW': '广安', 'GBP': '高碑店', 'GBD': '沟帮子', 'GDJ': '甘草店', 'GCN': '谷城', 'GEP': '藁城', 'GCV': '高村', 'GZB': '古城镇', 'GRH': '广德', 'GTW': '贵定', 'IDW': '贵定南', 'GDV': '古东', 'GGZ': '贵港', 'GVP': '官高', 'GGT': '葛根庙', 'GGL': '干沟', 'GGJ': '甘谷', 'GGP': '高各庄', 'GAX': '甘河', 'GEX': '根河', 'GDT': '郭家店', 'GKT': '孤家子', 'GLJ': '古浪', 'GEJ': '皋兰', 'GFM': '高楼房', 'GHT': '归流河', 'GLF': '关林', 'VOW': '甘洛', 'GLP': '郭磊庄', 'GMK': '高密', 'GMC': '公庙子', 'GRT': '工农湖', 'GNT': '广宁寺南', 'GNM': '广南卫', 'GPF': '高平', 'GEY': '甘泉北', 'GAG': '共青城', 'GQD': '甘旗卡', 'GQY': '甘泉', 'GZD': '高桥镇', 'GST': '灌水', 'GSW': '赶水', 'GSP': '孤山口', 'GSL': '果松', 'GSD': '高山子', 'GXD': '嘎什甸子', 'GTJ': '高台', 'GAY': '高滩', 'GTS': '古田', 'GTP': '官厅', 'KEP': '官厅西', 'GXG': '贵溪', 'GYH': '涡阳', 'GXF': '巩义', 'GIP': '高邑', 'GYF': '巩义南', 'GAW': '广元南', 'GUJ': '固原', 'GYL': '菇园', 'GYD': '公营子', 'GZS': '光泽', 'GNQ': '古镇', 'GEH': '固镇', 'GZY': '虢镇', 'GZJ': '瓜州', 'GSQ': '高州', 'GXT': '盖州', 'GOT': '官字井', 'GSS': '冠豸山', 'GAT': '盖州西', 'AMH': '淮安南', 'HWN': '红安', 'HIH': '海安县', 'VXN': '红安西', 'HBL': '黄柏', 'HEB': '海北', 'HAF': '鹤壁', 'XEG': '会昌北', 'VCQ': '华城', 'HCZ': '河唇', 'HCN': '汉川', 'HCT': '海城', 'WKW': '合川', 'HCJ': '黑冲滩', 'HCP': '黄村', 'HXT': '海城西', 'HGC': '化德', 'HDV': '洪洞', 'HFR': '霍尔果斯', 'HFG': '横峰', 'HXJ': '韩府湾', 'HGP': '汉沽', 'HYM': '黄瓜园', 'IGW': '红光镇', 'HHT': '浑河', 'VHD': '红花沟', 'HUD': '黄花筒', 'HJJ': '贺家店', 'HJR': '和静', 'HFM': '红江', 'HIM': '黑井', 'HJF': '获嘉', 'HJV': '河津', 'HJS': '涵江', 'HJT': '华家', 'HDC': '杭锦后旗', 'HXP': '河间西', 'HJM': '花家庄', 'HKJ': '河口南', 'KOH': '黄口', 'HKG': '湖口', 'HUB': '呼兰', 'HPD': '葫芦岛北', 'HHB': '浩良河', 'HIT': '哈拉海', 'HOB': '鹤立', 'HIB': '桦林', 'ULY': '黄陵', 'HRB': '海林', 'VLB': '虎林', 'HAT': '寒岭', 'HLL': '和龙', 'HIL': '海龙', 'HAX': '哈拉苏', 'VTJ': '呼鲁斯太', 'HLT': '火连寨', 'VEH': '黄梅', 'HYP': '韩麻营', 'HHL': '黄泥河', 'HNH': '海宁', 'HMJ': '惠农', 'VAQ': '和平', 'HZM': '花棚子', 'VQH': '花桥', 'HEY': '宏庆', 'HRV': '怀仁', 'HRN': '华容', 'HDY': '华山北', 'HDL': '黄松甸', 'VSR': '和什托洛盖', 'VSB': '红山', 'VSQ': '汉寿', 'HSQ': '衡山', 'HOT': '黑水', 'VCH': '惠山', 'HHP': '虎什哈', 'HSJ': '红寺堡', 'HUT': '虎石台', 'HSO': '海石湾', 'HEQ': '衡山西', 'VSJ': '红砂岘', 'HQB': '黑台', 'VTK': '桓台', 'VTR': '和田', 'VTQ': '会同', 'HZT': '海坨子', 'HWK': '黑旺', 'RWH': '海湾', 'VXB': '红星', 'HYY': '徽县', 'VHB': '红兴隆', 'VTB': '换新天', 'HTJ': '红岘台', 'VIX': '红彦', 'HAY': '合阳', 'HYK': '海阳', 'HVQ': '衡阳东', 'HUW': '华蓥', 'HQY': '汉阴', 'HGJ': '黄羊滩', 'WHW': '汉源', 'VIQ': '河源', 'HUN': '花园', 'HNO': '湟源', 'HYJ': '黄羊镇', 'VZH': '湖州', 'HZZ': '化州', 'VON': '黄州', 'HZV': '霍州', 'VXQ': '惠州西', 'JRT': '巨宝', 'JIY': '靖边', 'JBD': '金宝屯', 'JEF': '晋城北', 'JCJ': '金昌', 'JCK': '鄄城', 'JNV': '交城', 'JFD': '建昌', 'JDB': '峻德', 'JFP': '井店', 'JOB': '鸡东', 'UDH': '江都', 'JST': '鸡冠山', 'VGP': '金沟屯', 'JHP': '静海', 'JHX': '金河', 'JHB': '锦河', 'JHR': '精河', 'JIR': '精河南', 'JHZ': '江华', 'AJH': '建湖', 'VJD': '纪家沟', 'JJS': '晋江', 'JJB': '姜家', 'JJW': '江津', 'JKT': '金坑', 'JLJ': '芨岭', 'JMM': '金马村', 'JWQ': '江门东', 'JES': '角美', 'JOK': '莒南', 'JNP': '井南', 'JVS': '建瓯', 'JPC': '经棚', 'JQX': '江桥', 'SSX': '九三', 'EGH': '金山北', 'JSH': '嘉善', 'JCN': '京山', 'JRN': '建始', 'JVV': '稷山', 'JSL': '吉舒', 'JET': '建设', 'JOP': '甲山', 'JIB': '建三江', 'EAH': '嘉善南', 'JTB': '金山屯', 'JOM': '江所田', 'JTJ': '景泰', 'JNL': '九台南', 'JWX': '吉文', 'JUG': '进贤', 'JKK': '莒县', 'JUK': '嘉祥', 'JXV': '介休', 'JXH': '嘉兴', 'JJP': '井陉', 'EPH': '嘉兴南', 'JXT': '夹心子', 'UEH': '姜堰', 'JRQ': '揭阳', 'JYS': '建阳', 'JYW': '简阳', 'JYK': '巨野', 'JYZ': '江永', 'JYH': '缙云', 'JYJ': '靖远', 'SZL': '江源', 'JYF': '济源', 'JXJ': '靖远西', 'JZK': '胶州北', 'WEF': '焦作东', 'JZH': '金寨', 'JEQ': '靖州', 'JBN': '荆州', 'JXK': '胶州', 'JXP': '晋州', 'JOD': '锦州南', 'JOF': '焦作', 'JVP': '旧庄窝', 'JYD': '金杖子', 'KAT': '开安', 'KCR': '库车', 'KCP': '康城', 'KDX': '库都尔', 'KDT': '宽甸', 'KOB': '克东', 'KDC': '昆都仑召', 'KAW': '开江', 'KJB': '康金井', 'KQX': '喀喇其', 'KLC': '开鲁', 'KHR': '克拉玛依', 'KQL': '口前', 'KSH': '昆山', 'KAB': '奎山', 'KSB': '克山', 'KTT': '开通', 'KXZ': '康熙岭', 'KAM': '昆阳', 'KHX': '克一河', 'KXT': '开原西', 'KZP': '康庄', 'UBZ': '来宾', 'LLT': '老边', 'LPF': '灵宝西', 'LUQ': '龙川', 'LCQ': '乐昌', 'UCP': '黎城', 'UCK': '聊城', 'LCK': '蓝村', 'LDY': '两当', 'LRC': '林东', 'LDO': '乐都', 'LDP': '梁底下', 'LVP': '六道河子', 'LVM': '鲁番', 'LJP': '廊坊', 'LOP': '落垡', 'LFP': '廊坊北', 'UFD': '老府', 'LNB': '兰岗', 'LGM': '龙骨甸', 'LOM': '芦沟', 'LGJ': '龙沟', 'LGB': '拉古', 'UFH': '临海', 'LXX': '林海', 'LHX': '拉哈', 'JID': '凌海', 'LNL': '柳河', 'KLH': '六合', 'LHP': '龙华', 'UNP': '滦河沿', 'LEX': '六合镇', 'LRT': '亮甲店', 'UDT': '刘家店', 'LVT': '刘家河', 'LKS': '连江', 'UJH': '庐江', 'LJB': '李家', 'LJW': '罗江', 'LJZ': '廉江', 'UJT': '两家', 'LJX': '龙江', 'UJL': '龙嘉', 'LHB': '莲江口', 'ULK': '蔺家楼', 'LIJ': '李家坪', 'LKF': '兰考', 'LKB': '林口', 'LKQ': '路口铺', 'LAX': '老莱', 'LAB': '拉林', 'LRM': '陆良', 'LLW': '龙里', 'LWQ': '临澧', 'LLB': '兰棱', 'UWZ': '零陵', 'UAP': '卢龙', 'LMX': '喇嘛甸', 'LMB': '里木店', 'LMJ': '洛门', 'UNG': '龙南', 'UQW': '梁平', 'LPM': '罗平', 'LPP': '落坡岭', 'UPJ': '六盘山', 'LPG': '乐平市', 'UQK': '临清', 'UQJ': '龙泉寺', 'UTW': '乐山北', 'LUM': '乐善村', 'UDQ': '冷水江东', 'LGT': '连山关', 'USP': '流水沟', 'LIQ': '陵水', 'USH': '丽水', 'LRN': '罗山', 'LAF': '鲁山', 'LMK': '梁山', 'LSV': '灵石', 'LUL': '露水河', 'LSG': '庐山', 'LBT': '林盛堡', 'LSD': '柳树屯', 'LAS': '龙山镇', 'LSB': '梨树镇', 'LET': '李石寨', 'LTZ': '黎塘', 'LAR': '轮台', 'LTP': '芦台', 'LBM': '龙塘坝', 'LVZ': '濑湍', 'LTJ': '骆驼巷', 'VLJ': '李旺', 'LWK': '莱芜东', 'LRJ': '狼尾山', 'LNJ': '灵武', 'UXK': '莱芜西', 'LXB': '朗乡', 'LXY': '陇县', 'LXQ': '临湘', 'LUG': '芦溪', 'LXK': '莱西', 'LXC': '林西', 'UXP': '滦县', 'LYY': '略阳', 'LYK': '莱阳', 'LYT': '辽阳', 'UYK': '临沂北', 'LDD': '凌源东', 'UIH': '连云港', 'LNF': '临颍', 'LXL': '老营', 'LMH': '龙游', 'LVS': '罗源', 'LYX': '林源', 'LAQ': '涟源', 'LYP': '涞源', 'LPQ': '耒阳西', 'LEJ': '临泽', 'LZT': '龙爪沟', 'UAQ': '雷州', 'LIW': '六枝', 'LIZ': '鹿寨', 'LZS': '来舟', 'LZA': '龙镇', 'LEM': '拉鲊', 'LQJ': '兰州新区', 'MAH': '马鞍山', 'MBY': '毛坝', 'MGY': '毛坝关', 'MBN': '麻城北', 'MCF': '渑池', 'MCL': '明城', 'MAP': '庙城', 'MNF': '渑池南', 'KPM': '茅草坪', 'MUQ': '猛洞河', 'MOB': '磨刀石', 'MDF': '弥渡', 'MRB': '帽儿山', 'MGN': '明港', 'MHL': '梅河口', 'MHZ': '马皇', 'MGB': '孟家岗', 'MHQ': '美兰', 'MQQ': '汨罗东', 'MHB': '马莲河', 'MLZ': '茅岭', 'MLL': '庙岭', 'MLD': '茂林', 'MLB': '穆棱', 'MID': '马林', 'MGM': '马龙', 'MUD': '木里图', 'MLQ': '汨罗', 'MNR': '玛纳斯湖', 'UGW': '冕宁', 'MPQ': '沐滂', 'MQB': '马桥河', 'MQS': '闽清', 'MQF': '民权', 'MUT': '明水河', 'MAB': '麻山', 'MSW': '眉山', 'MKW': '漫水湾', 'MOM': '茂舍祖', 'MST': '米沙子', 'MEB': '美溪', 'MVY': '勉县', 'MVQ': '麻阳', 'MUP': '密云北', 'MMW': '米易', 'MYS': '麦园', 'MUR': '墨玉', 'MZJ': '庙庄', 'MEY': '米脂', 'MFQ': '明珠', 'NAB': '宁安', 'NAT': '农安', 'NBK': '南博山', 'NCK': '南仇', 'NSP': '南城司', 'NCZ': '宁村', 'NES': '宁德', 'NGP': '南观村', 'NFP': '南宫东', 'NLT': '南关岭', 'NNH': '宁国', 'NHH': '宁海', 'NHS': '南华北', 'NHJ': '南河川', 'NHD': '泥河子', 'NVT': '宁家', 'NJS': '南靖', 'NJB': '牛家', 'NJD': '能家', 'NKP': '南口', 'NKT': '南口前', 'NNQ': '南朗', 'NLD': '乃林', 'NIR': '尼勒克', 'ULZ': '那罗', 'NLF': '宁陵县', 'NMD': '奈曼', 'NMZ': '宁明', 'NMX': '南木', 'NNS': '南平南', 'NPZ': '那铺', 'NQD': '南桥', 'NQO': '那曲', 'NQJ': '暖泉', 'NTT': '南台', 'NOQ': '南头', 'NWV': '宁武', 'NWP': '南湾子', 'NEH': '南翔北', 'NXQ': '宁乡', 'NXF': '内乡', 'NXT': '牛心台', 'NUP': '南峪', 'NIP': '娘子关', 'NAF': '南召', 'NZT': '南杂木', 'PAW': '蓬安', 'PAL': '平安', 'PNO': '平安驿', 'PAJ': '磐安镇', 'PZT': '平安镇', 'PEY': '蒲城东', 'PCY': '蒲城', 'PDB': '裴德', 'PRP': '偏店', 'BFF': '平顶山西', 'PXJ': '坡底下', 'PRT': '瓢儿屯', 'PFB': '平房', 'PGL': '平岗', 'PGM': '平关', 'PAM': '盘关', 'PGZ': '平果', 'PHP': '徘徊北', 'PHM': '平河口', 'PHQ': '平湖', 'PBD': '盘锦北', 'PDP': '潘家店', 'PKT': '皮口南', 'PLT': '普兰店', 'PNT': '偏岭', 'PSB': '平山', 'PSW': '彭山', 'PSR': '皮山', 'PSL': '磐石', 'PSV': '平社', 'PHW': '彭水', 'PVT': '平台', 'PTM': '平田', 'PTS': '莆田', 'PTW': '葡萄菁', 'PWT': '普湾', 'PWV': '平旺', 'PGV': '平型关', 'POW': '普雄', 'PWW': '郫县', 'PYX': '平洋', 'PYJ': '彭阳', 'PYV': '平遥', 'PIK': '平邑', 'PPJ': '平原堡', 'PYK': '平原', 'PYP': '平峪', 'PZG': '彭泽', 'PJH': '邳州', 'PZD': '平庄', 'POD': '泡子', 'PND': '平庄南', 'QOT': '乾安', 'QAB': '庆安', 'QQP': '迁安', 'QRQ': '祁东北', 'QDM': '七甸', 'QAK': '曲阜东', 'QFT': '庆丰', 'QVP': '奇峰塔', 'QFK': '曲阜', 'QYQ': '琼海', 'QTP': '秦皇岛', 'QUY': '千河', 'QIP': '清河', 'QHD': '清河门', 'QHP': '清华园', 'INH': '全椒', 'QJZ': '渠旧', 'QJN': '潜江', 'QJB': '秦家', 'QJW': '綦江', 'QBT': '祁家堡', 'QNY': '清涧县', 'QZV': '秦家庄', 'QLD': '七里河', 'QLY': '秦岭', 'QLZ': '渠黎', 'QIB': '青龙', 'QGH': '青龙山', 'QIH': '祁门', 'QMP': '前磨头', 'QSB': '青山', 'QSN': '确山', 'QXQ': '前山', 'QUJ': '清水', 'QYH': '戚墅堰', 'QVH': '青田', 'QAT': '桥头', 'QTJ': '青铜峡', 'QWD': '前卫', 'QWP': '前苇塘', 'QRW': '渠县', 'QXV': '祁县', 'QXP': '青县', 'QXJ': '桥西', 'QUV': '清徐', 'QXC': '旗下营', 'QOY': '千阳', 'QYF': '沁阳', 'QYL': '泉阳', 'QVQ': '祁阳北', 'QYJ': '七营', 'QSJ': '庆阳山', 'QBQ': '清远', 'QYT': '清原', 'QDZ': '钦州东', 'QRZ': '钦州', 'QZK': '青州市', 'RAH': '瑞安', 'RCW': '荣昌', 'RCG': '瑞昌', 'RBH': '如皋', 'RUQ': '容桂', 'RQP': '任丘', 'ROK': '乳山', 'RSZ': '融水', 'RSD': '热水', 'RXZ': '容县', 'RVP': '饶阳', 'RYF': '汝阳', 'RHD': '绕阳河', 'ROF': '汝州', 'OBJ': '石坝', 'SBP': '上板城', 'AQW': '施秉', 'OBP': '上板城南', 'ZWT': '世博园', 'SBB': '双城北', 'OCH': '舒城', 'SWN': '商城', 'SCR': '莎车', 'SCS': '顺昌', 'SMV': '神池', 'SCP': '沙城', 'SCT': '石城', 'SCL': '山城镇', 'SDJ': '山丹', 'ORQ': '顺德', 'ODY': '绥德', 'SIL': '水洞', 'SXC': '商都', 'SEP': '十渡', 'OUD': '四道湾', 'OJQ': '顺德学院', 'OLH': '绅坊', 'OFB': '双丰', 'STB': '四方台', 'OTW': '水富', 'OKJ': '三关口', 'OGC': '桑根达来', 'SNQ': '韶关', 'SVK': '上高镇', 'JBS': '上杭', 'SED': '沙海', 'SBM': '松河', 'SHP': '沙河', 'SKT': '沙河口', 'SHC': '赛汗塔拉', 'VOP': '沙河市', 'SSD': '沙后所', 'SHL': '山河屯', 'OXP': '三河县', 'OHD': '四合永', 'OZW': '三汇镇', 'SEL': '双河镇', 'SZR': '石河子', 'SVP': '三合庄', 'ODP': '三家店', 'SQH': '水家湖', 'OJJ': '沈家河', 'SJL': '松江河', 'SJB': '尚家', 'SUB': '孙家', 'OJB': '沈家', 'SML': '双吉', 'SAH': '松江', 'SKD': '三江口', 'OLK': '司家岭', 'IMH': '松江南', 'SRP': '石景山南', 'SJJ': '邵家堂', 'SOZ': '三江县', 'SMM': '三家寨', 'SJD': '十家子', 'OZL': '松江镇', 'SHM': '施家嘴', 'SWT': '深井子', 'OMP': '什里店', 'SUR': '疏勒', 'SHJ': '疏勒河', 'VLD': '舍力虎', 'SPB': '石磷', 'SLM': '石林', 'ZJD': '双辽', 'SIB': '绥棱', 'SOL': '石岭', 'LNM': '石林南', 'SLQ': '石龙', 'SLC': '萨拉齐', 'SNT': '索伦', 'OLY': '商洛', 'SLP': '沙岭子', 'VFQ': '石门县北', 'SCF': '三门峡南', 'OQH': '三门县', 'OMQ': '石门县', 'SXF': '三门峡西', 'SYP': '肃宁', 'SOB': '宋', 'SBZ': '双牌', 'PPT': '四平东', 'SON': '遂平', 'SFJ': '沙坡头', 'SQM': '沙桥', 'SPF': '商丘南', 'SID': '水泉', 'SXY': '石泉县', 'SQT': '石桥子', 'SRB': '石人城', 'SRL': '石人', 'SQB': '山市', 'SWB': '神树', 'SSR': '鄯善', 'SJQ': '三水', 'OSK': '泗水', 'SAD': '石山', 'SFT': '松树', 'SAT': '首山', 'SRD': '三十家', 'SST': '三十里堡', 'SSL': '松树镇', 'MZQ': '松桃', 'SHX': '索图罕', 'SDH': '三堂集', 'OTB': '石头', 'SEV': '神头', 'SFM': '沙沱', 'SWP': '上万', 'SKB': '孙吴', 'SXR': '沙湾县', 'OVH': '歙县', 'SXZ': '遂溪', 'SAS': '沙县', 'SOH': '绍兴', 'SXL': '石岘', 'SXM': '上西铺', 'SXJ': '石峡子', 'FMH': '沭阳', 'SYB': '绥阳', 'SYV': '寿阳', 'OYP': '水洋', 'SYJ': '三阳川', 'SPJ': '上腰墩', 'OEJ': '三营', 'SOP': '顺义', 'OYD': '三义井', 'SYL': '三源浦', 'BDH': '上虞', 'SAY': '三原', 'SUD': '上园', 'OYJ': '水源', 'SAJ': '桑园子', 'SND': '绥中北', 'OHH': '苏州北', 'SRH': '宿州东', 'BJQ': '深圳东', 'OZP': '深州', 'OZY': '孙镇', 'SZD': '绥中', 'SZB': '尚志', 'SNM': '师庄', 'SIN': '松滋', 'SEM': '师宗', 'KAH': '苏州园区', 'ITH': '苏州新区', 'TMK': '泰安', 'TID': '台安', 'TAJ': '通安驿', 'TBF': '桐柏', 'TBB': '通北', 'TTH': '桐城', 'TCX': '汤池', 'TZK': '郯城', 'TCL': '铁厂', 'TCK': '桃村', 'TRQ': '通道', 'TDZ': '田东', 'TGL': '天岗', 'TGC': '土贵乌拉', 'TOL': '通沟', 'TGV': '太谷', 'THX': '塔哈', 'THM': '棠海', 'THF': '唐河', 'THG': '泰和', 'TKH': '太湖', 'TIX': '团结', 'TNJ': '谭家井', 'TOT': '陶家屯', 'PDQ': '唐家湾', 'TZP': '统军庄', 'TKX': '泰康', 'TMD': '吐列毛杜', 'TEX': '图里河', 'TJH': '铜陵', 'TFZ': '田林', 'TIZ': '亭亮', 'TLB': '铁力', 'PXT': '铁岭西', 'QSL': '图们北', 'TMN': '天门', 'TNN': '天门南', 'TLS': '太姥山', 'TRC': '土牧尔台', 'TCJ': '土门子', 'TVT': '洮南', 'TVW': '潼南', 'TIT': '太平川', 'TEB': '太平镇', 'TQX': '图强', 'TTK': '台前', 'TQL': '天桥岭', 'TQJ': '土桥子', 'TCT': '汤山城', 'TAB': '桃山', 'TIM': '塔石嘴', 'TUT': '通途', 'THB': '汤旺河', 'TXJ': '同心', 'TSW': '土溪', 'TCH': '桐乡', 'TRZ': '田阳', 'TND': '天义', 'TYF': '汤阴', 'TIL': '驼腰岭', 'TYJ': '太阳山', 'TYB': '汤原', 'TYP': '塔崖驿', 'TEK': '滕州东', 'TZH': '台州', 'TZJ': '天祝', 'TXK': '滕州', 'TZV': '天镇', 'TEW': '桐子林', 'QWH': '天柱山', 'WBP': '文安', 'WAP': '武安', 'WVP': '王安镇', 'WUY': '吴堡', 'WEW': '旺苍', 'WCT': '五叉沟', 'WEQ': '文昌', 'WDB': '温春', 'WRB': '五大连池', 'WBK': '文登', 'WDL': '五道沟', 'WHP': '五道河', 'WNZ': '文地', 'WVT': '卫东', 'WRN': '武当山', 'WDP': '望都', 'WHX': '乌尔旗汗', 'WFK': '潍坊', 'WFB': '万发屯', 'WUT': '王府', 'WXT': '瓦房店西', 'WGB': '王岗', 'WGY': '武功', 'WGL': '湾沟', 'WGM': '吴官田', 'WVC': '乌海', 'WHB': '苇河', 'WHF': '卫辉', 'WCJ': '吴家川', 'WUB': '五家', 'WAM': '威箐', 'WJP': '午汲', 'WJL': '渭津', 'WJJ': '王家湾', 'WQB': '倭肯', 'WKT': '五棵树', 'WBT': '五龙背', 'WLC': '乌兰哈达', 'WEB': '万乐', 'WVX': '瓦拉干', 'VHH': '温岭', 'WLK': '五莲', 'WQC': '乌拉特前旗', 'WSC': '乌拉山', 'WLX': '卧里屯', 'WBY': '渭南北', 'WRX': '乌奴耳', 'WNQ': '万宁', 'WWG': '万年', 'WVY': '渭南南', 'WNJ': '渭南镇', 'WPT': '沃皮', 'WUP': '吴桥', 'WQL': '汪清', 'WWP': '武清', 'WSJ': '武山', 'WEV': '文水', 'WSP': '魏善庄', 'WTP': '王瞳', 'WSV': '五台山', 'WZJ': '王团庄', 'WVR': '五五', 'WGH': '无锡东', 'WVB': '卫星', 'WXV': '闻喜', 'WVV': '武乡', 'IFH': '无锡新区', 'WXN': '武穴', 'WYZ': '吴圩', 'WYB': '王杨', 'RYH': '武义', 'WWB': '五营', 'WIM': '瓦窑田', 'WYC': '五原', 'WZL': '苇子沟', 'WZY': '韦庄', 'WZV': '五寨', 'WZB': '王兆屯', 'WQP': '微子镇', 'WKD': '魏杖子', 'EAM': '新安', 'XAZ': '兴安', 'XAF': '新安县', 'XAP': '新保安', 'EBP': '下板城', 'XLP': '西八里', 'ECH': '宣城', 'XCD': '兴城', 'XEM': '小村', 'XRX': '新绰源', 'XCB': '下城子', 'XCT': '新城子', 'EDW': '喜德', 'EJM': '小得江', 'XMP': '西大庙', 'XEZ': '小董', 'XOD': '小东', 'EFG': '信丰', 'XFV': '襄汾', 'XFW': '息烽', 'EGG': '新干', 'XGN': '孝感', 'XUJ': '西固城', 'XIJ': '西固', 'XGJ': '夏官营', 'NBB': '西岗子', 'XXB': '襄河', 'XIR': '新和', 'XWJ': '宣和', 'EEP': '斜河涧', 'XAX': '新华屯', 'XHB': '新华', 'EHQ': '新化', 'XHP': '宣化', 'XEC': '兴和西', 'XYD': '小河沿', 'XYP': '下花园', 'EKY': '小河镇', 'XJB': '徐家', 'EJG': '峡江', 'XJV': '新绛', 'ENP': '辛集', 'XJM': '新江', 'EKM': '西街口', 'XJT': '许家屯', 'XTJ': '许家台', 'XMT': '谢家镇', 'EKB': '兴凯', 'EAQ': '小榄', 'XNB': '香兰', 'XDD': '兴隆店', 'ELP': '新乐', 'XPX': '新林', 'XLB': '小岭', 'XLJ': '新李', 'XYB': '西林', 'GCT': '西柳', 'XPH': '仙林', 'XLD': '新立屯', 'XZB': '兴隆镇', 'XGT': '新立镇', 'XMD': '新民', 'XMB': '西麻山', 'XAT': '下马塘', 'XNV': '孝南', 'XRN': '咸宁北', 'ENQ': '兴宁', 'XNN': '咸宁', 'XAW': '犀浦东', 'XPN': '西平', 'XPY': '兴平', 'XPM': '新坪田', 'XOS': '霞浦', 'EPQ': '溆浦', 'XIW': '犀浦', 'XQB': '新青', 'XQD': '新邱', 'XQJ': '兴泉堡', 'XRL': '仙人桥', 'ESP': '小寺沟', 'XSB': '杏树', 'XZN': '浠水', 'XSV': '下社', 'XSP': '徐水', 'XIZ': '夏石', 'XAM': '小哨', 'XOB': '新松浦', 'XDT': '杏树屯', 'XSJ': '许三湾', 'XTQ': '湘潭', 'XTP': '邢台', 'XAN': '仙桃西', 'EIP': '下台子', 'XJQ': '徐闻', 'EPD': '新窝铺', 'XWF': '修武', 'XSN': '新县', 'ENN': '息县', 'XQY': '西乡', 'XXQ': '湘乡', 'XIF': '西峡', 'XOV': '孝西', 'XXM': '小新街', 'XGQ': '新兴县', 'XZC': '西小召', 'XXP': '小西庄', 'XDB': '向阳', 'XUY': '旬阳', 'XBY': '旬阳北', 'XWN': '襄阳东', 'SNZ': '兴业', 'XHM': '小雨谷', 'EEQ': '信宜', 'XFM': '小月旧', 'XYX': '小扬气', 'EXM': '祥云', 'EIF': '襄垣', 'EJH': '夏邑县', 'EYB': '新友谊', 'XZJ': '新阳镇', 'UUH': '徐州东', 'XZX': '新帐房', 'XRP': '悬钟', 'XZT': '新肇', 'XXV': '忻州', 'XZD': '汐子', 'XRD': '西哲里木', 'ERP': '新杖子', 'YAC': '姚安', 'YAX': '依安', 'YAS': '永安', 'YNB': '永安乡', 'YBB': '亚布力', 'YUD': '元宝山', 'YAB': '羊草', 'YKM': '秧草地', 'AIH': '阳澄湖', 'YYB': '迎春', 'YER': '叶城', 'YKJ': '盐池', 'YYY': '砚川', 'YQQ': '阳春', 'YIN': '宜城', 'YHN': '应城', 'YCK': '禹城', 'YEK': '晏城', 'YNF': '阳城', 'YAL': '阳岔', 'YPK': '郓城', 'YAP': '雁翅', 'ACP': '云彩岭', 'IXH': '虞城县', 'YCT': '营城子', 'YDQ': '英德', 'YDJ': '永登', 'YDM': '尹地', 'YGS': '永定', 'YGH': '雁荡山', 'YDG': '于都', 'YAJ': '园墩', 'IIQ': '英德西', 'YYM': '永丰营', 'YRB': '杨岗', 'YOV': '阳高', 'YIK': '阳谷', 'YOB': '友好', 'EVH': '余杭', 'YHP': '沿河城', 'AEP': '岩会', 'YHM': '羊臼河', 'URH': '永嘉', 'YAM': '营街', 'AEW': '盐津', 'YHG': '余江', 'AJP': '燕郊', 'YAT': '姚家', 'YGJ': '岳家井', 'YJT': '一间堡', 'YIR': '英吉沙', 'AFP': '云居寺', 'AZK': '燕家庄', 'RFH': '永康', 'YGT': '营口东', 'YJX': '银浪', 'YLW': '永郎', 'YSM': '宜良北', 'YDY': '永乐店', 'YLX': '伊拉哈', 'YLB': '伊林', 'YSY': '杨陵', 'ALW': '彝良', 'YLM': '杨林', 'YLD': '余粮堡', 'YQP': '杨柳青', 'YUM': '月亮田', 'YMF': '义马', 'YVV': '阳明堡', 'YXJ': '玉门', 'YMN': '云梦', 'YMM': '元谋', 'YST': '一面山', 'YNK': '沂南', 'YVM': '宜耐', 'YNR': '伊宁东', 'YZJ': '营盘水', 'ABM': '羊堡', 'YPP': '阳泉北', 'UPH': '乐清', 'YSR': '焉耆', 'AQK': '源迁', 'YQT': '姚千户屯', 'YQV': '阳曲', 'YGP': '榆树沟', 'YBF': '月山', 'YSJ': '玉石', 'AUM': '玉舍', 'YSF': '偃师', 'YUK': '沂水', 'YSV': '榆社', 'YVH': '颍上', 'ASP': '窑上', 'YSP': '元氏', 'YAD': '杨树岭', 'AIP': '野三坡', 'YSX': '榆树屯', 'YUT': '榆树台', 'YIP': '鹰手营子', 'YTQ': '源潭', 'YTZ': '牙屯堡', 'YSL': '烟筒山', 'YUX': '烟筒屯', 'YWM': '羊尾哨', 'YHW': '越西', 'YOG': '攸县', 'ACG': '永修', 'YXM': '玉溪西', 'YIG': '弋阳', 'YYH': '余姚', 'AFW': '酉阳', 'YIQ': '岳阳东', 'ARP': '阳邑', 'YYL': '鸭园', 'YYJ': '鸳鸯镇', 'YZY': '燕子砭', 'UZH': '仪征', 'YSZ': '宜州', 'YZK': '兖州', 'YQM': '迤资', 'AEM': '羊者窝', 'YZD': '杨杖子', 'ZEY': '镇安', 'ZAD': '治安', 'ZBP': '招柏', 'ZUP': '张百湾', 'ZJJ': '中川机场', 'ZCN': '枝城', 'ZHY': '子长', 'ZQK': '诸城', 'ZIK': '邹城', 'ZCV': '赵城', 'ZHT': '章党', 'ZDP': '正定', 'ZDB': '肇东', 'ZFM': '照福铺', 'ZGD': '章古台', 'ZGB': '赵光', 'ZHX': '中和', 'VNH': '中华门', 'ZIN': '枝江北', 'ZJY': '钟家村', 'ZUB': '朱家沟', 'ZYP': '紫荆关', 'ZOB': '周家', 'ZDH': '诸暨', 'ZEH': '镇江南', 'ZOD': '周家屯', 'CWJ': '褚家湾', 'ZWQ': '湛江西', 'ZUJ': '朱家窑', 'ZBW': '曾家坪子', 'ZLV': '张兰', 'ZLT': '镇赉', 'ZIV': '枣林', 'ZLD': '扎鲁特', 'ZXX': '扎赉诺尔西', 'ZOQ': '樟木头', 'ZGF': '中牟', 'ZDJ': '中宁东', 'VNJ': '中宁', 'ZNJ': '中宁南', 'ZPF': '镇平', 'ZPS': '漳平', 'ZPR': '泽普', 'ZVP': '枣强', 'ZQY': '张桥', 'ZTK': '章丘', 'ZRC': '朱日和', 'ZLM': '泽润里', 'ZGQ': '中山北', 'ZOG': '樟树东', 'ZHD': '珠斯花', 'ZSQ': '中山', 'ZSY': '柞水', 'ZSZ': '钟山', 'ZSG': '樟树', 'ZOP': '珠窝', 'ZWB': '张维屯', 'ZWD': '彰武', 'ZOY': '棕溪', 'ZTN': '钟祥', 'ZXS': '资溪', 'ZVT': '镇西', 'ZIP': '张辛', 'ZXC': '正镶白旗', 'ZVY': '紫阳', 'ZYN': '枣阳', 'ZAW': '竹园坝', 'ZYJ': '张掖', 'ZUW': '镇远', 'GOS': '漳州东', 'ZUS': '漳州', 'ZUX': '壮志', 'ZZY': '子洲', 'ZZM': '中寨', 'ZXP': '涿州', 'ZAL': '咋子', 'ZZC': '卓资山', 'ZAQ': '株洲西', 'XPF': '郑州西', 'AQC': '阿巴嘎旗', 'ARX': '阿尔山北', 'AUR': '阿勒泰', 'ARG': '安仁', 'ASE': '安顺西', 'AXL': '安图西', 'ADF': '安阳东', 'BBZ': '博白', 'BBE': '八步', 'FWH': '栟茶', 'BMP': '保定东', 'FEP': '白沟', 'FHP': '滨海', 'FCP': '滨海北', 'BBY': '宝鸡南', 'BRT': '北井子', 'BFQ': '白马井', 'BUB': '宝清', 'FZW': '璧山', 'BSN': '白沙铺', 'BGY': '白水县', 'NGQ': '板塘', 'BVT': '本溪新城', 'BXY': '彬县', 'UKZ': '宾阳', 'FWP': '白洋淀', 'FHW': '百宜', 'FNC': '白音华南', 'BDE': '巴中东', 'BIK': '滨州', 'FOP': '霸州西', 'CUY': '澄城', 'VAT': '查干湖', 'GUH': '巢湖东', 'KNW': '从江', 'CVO': '茶卡', 'FVH': '长临河', 'CNG': '茶陵南', 'FQQ': '常平东', 'CQJ': '长庆桥', 'COW': '长寿北', 'CSE': '长寿湖', 'CBQ': '潮汕', 'CNS': '长汀南', 'CWY': '长武', 'CBH': '长兴', 'CXE': '苍溪', 'CYN': '长阳', 'CNQ': '潮阳', 'CWT': '城子坦', 'DCZ': '东安东', 'RBZ': '德保', 'DCJ': '东岔', 'RDD': '东戴河', 'RWT': '丹东西', 'DRB': '东二道河', 'KRQ': '大丰', 'DNE': '大方南', 'RGT': '东港北', 'RMT': '大孤山', 'RTQ': '东莞', 'UWQ': '鼎湖东', 'NVQ': '鼎湖山', 'FWQ': '洞井', 'DJE': '垫江', 'DIM': '大苴', 'DNY': '大荔', 'DSD': '大青沟', 'DRH': '德清', 'PRH': '砀山南', 'DAL': '大石头南', 'OWH': '当涂东', 'DTO': '大通西', 'WWQ': '大旺', 'DNJ': '定西北', 'DWG': '德兴', 'IRQ': '丹霞山', 'DBN': '大冶北', 'KJW': '都匀东', 'DOK': '东营南', 'DYG': '大余', 'DOP': '定州东', 'WZQ': '端州', 'FQW': '大足南', 'IXW': '峨眉山', 'EFN': '鄂州东', 'FBZ': '防城港北', 'FDT': '凤城东', 'FDZ': '富川', 'PUH': '繁昌西', 'FUW': '丰都', 'FEW': '涪陵北', 'FNM': '富宁', 'FQE': '法启', 'KCQ': '芙蓉南', 'FAW': '复盛', 'FSL': '抚松', 'FOQ': '佛山西', 'FZQ': '福山镇', 'NZQ': '福田', 'FBM': '富源北', 'FYB': '抚远', 'FDG': '抚州东', 'FZG': '抚州', 'GCG': '高安', 'VUW': '广安南', 'GAE': '贵安', 'GMP': '高碑店东', 'GCZ': '恭城', 'FMW': '贵定北', 'GNN': '葛店南', 'KIW': '贵定县', 'GVW': '广汉北', 'GEM': '革居', 'GLE': '关岭', 'GEZ': '桂林西', 'IMQ': '光明城', 'FBQ': '广宁', 'GQT': '广宁寺', 'GXM': '广南县', 'GAZ': '桂平', 'GPT': '弓棚子', 'GUN': '光山', 'GBS': '古田北', 'GPM': '广通北', 'GAJ': '高台南', 'STS': '古田会址', 'KQW': '贵阳北', 'GNP': '高邑西', 'HNS': '惠安', 'HFF': '鹤壁东', 'HKB': '寒葱沟', 'SER': '霍城', 'HUL': '珲春', 'HPP': '邯郸东', 'KDQ': '惠东', 'HDJ': '哈达铺', 'HDO': '海东西', 'HTV': '洪洞西', 'HTB': '哈尔滨北', 'COH': '合肥北城', 'ENH': '合肥南', 'KGN': '黄冈', 'KAN': '黄冈东', 'HNN': '横沟桥东', 'KXN': '黄冈西', 'HPB': '洪河', 'KAQ': '怀化南', 'HCF': '黄河景区', 'KHN': '花湖', 'KHQ': '惠环', 'IHN': '后湖', 'FAQ': '怀集', 'HBM': '河口北', 'KLQ': '黄流', 'VLY': '黄陵南', 'KMQ': '鲘门', 'IUQ': '虎门', 'HPV': '侯马西', 'HNG': '衡南', 'HOH': '淮南东', 'HVZ': '合浦', 'FBH': '霍邱', 'HFV': '怀仁东', 'HPN': '华容东', 'KRN': '华容南', 'KSN': '黄石北', 'NYH': '黄山北', 'HLN': '贺胜桥东', 'VUR': '和硕', 'KNN': '花山南', 'KXQ': '荷塘', 'HTY': '合阳北', 'HEK': '海阳北', 'IYN': '槐荫', 'HYT': '花园口', 'HWV': '霍州东', 'KNQ': '惠州南', 'JAJ': '泾川', 'NSH': '旌德', 'PFQ': '尖峰', 'JOL': '蛟河西', 'JMP': '军粮城北', 'JLS': '将乐', 'JLF': '贾鲁河', 'KJQ': '九郎山', 'JVK': '即墨北', 'JCS': '建宁县北', 'JJH': '江宁', 'OKH': '江宁西', 'JUS': '建瓯西', 'JNJ': '酒泉南', 'JWH': '句容西', 'JSM': '建水', 'JUN': '界首市', 'NRH': '绩溪北', 'JDV': '介休东', 'LOH': '泾县', 'JMZ': '靖西', 'JXG': '进贤南', 'JBJ': '嘉峪关南', 'JOW': '简阳南', 'JTN': '金银潭', 'JYL': '靖宇', 'PYQ': '金月湾', 'PYH': '缙云西', 'JZV': '晋中', 'KBF': '开封北', 'QKW': '凯里南', 'KLD': '库伦', 'KOM': '昆明南', 'KTQ': '葵潭', 'KVW': '开阳', 'IDZ': '隆安东', 'UCZ': '来宾北', 'GMH': '灵璧', 'LCF': '绿博园', 'NWW': '隆昌北', 'ILQ': '乐昌东', 'UUP': '临城', 'VCZ': '罗城', 'LGK': '陵城', 'ACQ': '老城镇', 'FVW': '龙洞堡', 'LVO': '乐都南', 'UOQ': '娄底南', 'UQQ': '乐东', 'INW': '离堆公园', 'LLQ': '陆丰', 'KFQ': '龙丰', 'LQM': '禄丰南', 'LXV': '临汾西', 'KGQ': '临高南', 'UDP': '滦河', 'LBN': '漯河西', 'IKW': '罗江东', 'UQZ': '柳江', 'LNK': '利津南', 'LUF': '兰考南', 'COK': '兰陵北', 'KFW': '龙里北', 'KBQ': '沥林北', 'UKQ': '醴陵东', 'INJ': '陇南', 'LPE': '梁平南', 'LGY': '礼泉', 'UDV': '灵石东', 'IVW': '乐山', 'LAG': '龙市', 'LDH': '溧水', 'KRW': '洛湾三江', 'LBK': '莱西北', 'LEH': '溧阳', 'LUK': '临邑', 'LNR': '柳园南', 'LSZ': '鹿寨北', 'LZE': '阆中', 'LDJ': '临泽南', 'OMH': '马鞍山东', 'MHN': '毛陈', 'MDN': '明港东', 'MNO': '民和南', 'MJN': '闵集', 'MLR': '马兰', 'MBJ': '民乐', 'MLM': '弥勒', 'MSR': '玛纳斯', 'MBK': '牟平', 'MBS': '闽清北', 'MIF': '民权北', 'IUW': '眉山东', 'MSN': '庙山', 'MXJ': '岷县', 'MYO': '门源', 'KIQ': '暮云', 'MBM': '蒙自北', 'MZF': '孟庄', 'MZM': '蒙自', 'NBE': '南部', 'NEF': '南曹', 'NCE': '南充北', 'NDG': '南城', 'NXG': '南昌西', 'NDJ': '宁东南', 'NOJ': '宁东', 'NUT': '南芬北', 'NFG': '南丰', 'NDN': '南湖东', 'NKW': '内江北', 'FIW': '南江', 'NDQ': '南江口', 'LLH': '南陵', 'NMO': '尼木', 'NFZ': '南宁东', 'NXZ': '南宁西', 'NBS': '南平北', 'NCQ': '南雄', 'NYE': '纳雍', 'NYF': '南阳寨', 'PAN': '普安', 'PUE': '普安县', 'PBM': '屏边', 'PBE': '平坝南', 'PCE': '平昌', 'PGW': '普定', 'PAK': '平度', 'PUT': '皮口', 'PNN': '盘龙城', 'PEQ': '普宁', 'PAZ': '平南南', 'PPW': '彭山北', 'PSK': '坪上', 'PBG': '萍乡北', 'PYF': '濮阳', 'PDV': '平遥古城', 'PZM': '普者黑', 'PAE': '盘州', 'PMW': '彭州', 'QGJ': '秦安', 'QFW': '青白江东', 'QHK': '青岛北', 'QMQ': '祁东', 'QET': '青堆', 'QFB': '前锋', 'QBM': '曲靖北', 'QIM': '曲江', 'QEW': '青莲', 'QNB': '齐齐哈尔南', 'QEJ': '清水北', 'QVW': '青神', 'QAY': '岐山', 'QSQ': '庆盛', 'QSO': '曲水县', 'QGV': '祁县东', 'QBY': '乾县', 'QNC': '旗下营南', 'QWQ': '祁阳', 'QNZ': '全州南', 'QZQ': '棋子湾', 'RUO': '仁布', 'RQW': '荣昌北', 'RCK': '荣成', 'RIH': '如东', 'RVW': '榕江', 'RKO': '日喀则', 'RVQ': '饶平', 'SFF': '宋城路', 'SDL': '三道湖', 'FIQ': '邵东', 'KKW': '三都县', 'SUP': '胜芳', 'NFQ': '双峰北', 'SOK': '商河', 'GQH': '泗洪', 'AHQ': '四会', 'SWZ': '三江南', 'OJT': '三井子', 'IPW': '双流机场', 'SYM': '石林西', 'IQW': '双流西', 'SHS': '三明北', 'SVM': '嵩明', 'FMQ': '树木岭', 'ONC': '苏尼特左旗', 'SBN': '山坡东', 'SQE': '石桥', 'SQN': '沈丘', 'SMR': '鄯善北', 'NSQ': '狮山北', 'ARQ': '三水北', 'KSQ': '狮山', 'RNQ': '三水南', 'INQ': '韶山南', 'QHW': '三穗', 'STE': '石梯', 'OGQ': '汕尾', 'NPH': '歙县北', 'SLH': '绍兴北', 'SSH': '绍兴东', 'GPH': '泗县', 'IPQ': '始兴', 'MPH': '泗阳', 'OVQ': '邵阳北', 'OCT': '松原北', 'SNV': '山阴', 'SOT': '沈阳南', 'IOQ': '深圳北', 'SRQ': '神州', 'IFQ': '深圳坪山', 'QQJ': '石嘴山', 'OSW': '石柱县', 'TOK': '桃村北', 'TBZ': '田东北', 'TTN': '土地堂东', 'TIV': '太谷西', 'THR': '吐哈', 'TAM': '通海', 'TJN': '天河机场', 'TEN': '天河街', 'TXL': '通化县', 'TJB': '同江', 'KXH': '铜陵北', 'TAR': '吐鲁番北', 'TNS': '泰宁', 'TNW': '铜仁南', 'TIJ': '天水南', 'TWJ': '通渭', 'KQQ': '田心东', 'THN': '汤逊湖', 'TAZ': '藤县', 'TNV': '太原南', 'TST': '通远堡西', 'WGK': '文登东', 'WFG': '五府山', 'WBL': '威虎岭北', 'WHK': '威海北', 'WPC': '乌兰察布', 'WMT': '五龙背东', 'WFN': '乌龙泉南', 'WAR': '乌鲁木齐', 'WET': '五女山', 'WSE': '武胜', 'IIH': '无为', 'WAH': '瓦屋山', 'WOV': '闻喜西', 'WDH': '武义北', 'WBS': '武夷山北', 'WCS': '武夷山东', 'WYG': '婺源', 'WEJ': '渭源', 'WZE': '万州北', 'WIF': '武陟', 'WBZ': '梧州南', 'XDZ': '兴安北', 'XVF': '许昌东', 'ERN': '项城', 'EWW': '新都东', 'XFT': '西丰', 'NQQ': '先锋', 'FVQ': '湘府路', 'XTV': '襄汾西', 'XJN': '孝感北', 'GDN': '孝感东', 'WDQ': '西湖东', 'EJQ': '新化南', 'EWQ': '新晃西', 'IRW': '新津', 'NKQ': '小金口', 'ITW': '新津南', 'XKN': '咸宁东', 'UNN': '咸宁南', 'EMQ': '溆浦南', 'EDQ': '湘潭北', 'EDP': '邢台东', 'XWC': '西乌旗', 'EXF': '修武西', 'QSH': '萧县北', 'EGF': '新乡东', 'XBG': '新余北', 'XQF': '西阳村', 'OYN': '信阳东', 'XOY': '咸阳秦都', 'XWS': '仙游', 'EZF': '新郑机场', 'FNQ': '香樟路', 'YFW': '迎宾路', 'RGH': '永城北', 'ABV': '运城北', 'WMW': '永川东', 'YEG': '宜春', 'AWW': '岳池', 'NAQ': '云东海', 'AOJ': '姚渡', 'IXQ': '云浮东', 'YBZ': '永福南', 'VTM': '雨格', 'GTH': '洋河', 'AJV': '永济北', 'RVH': '弋江', 'YKP': '于家堡', 'YXL': '延吉西', 'QUH': '永康南', 'YEF': '运粮河', 'YAG': '炎陵', 'YEY': '杨陵南', 'YMX': '伊敏', 'YKQ': '郁南', 'KPQ': '银瓶', 'ASY': '永寿', 'YCZ': '阳朔', 'KZQ': '云山', 'YGG': '玉山南', 'YTS': '永泰', 'CTQ': '银滩', 'YKG': '鹰潭北', 'YLK': '烟台南', 'YXS': '尤溪', 'YBS': '云霄', 'YUH': '宜兴', 'AXM': '玉溪', 'YVK': '阳信', 'YZV': '应县', 'YXG': '攸县南', 'CTH': '余姚北', 'IZJ': '榆中', 'ZDS': '诏安', 'ZHP': '正定机场', 'ZMN': '纸坊东', 'ZUT': '庄河北', 'ZHW': '昭化', 'ZJE': '织金北', 'ZPQ': '芷江', 'IZW': '织金', 'KKQ': '仲恺', 'ZKE': '曾口', 'ZSN': '左岭', 'ZRQ': '樟木头东', 'ZLN': '驻马店西', 'ZCS': '漳浦', 'FCQ': '肇庆东', 'ZQH': '庄桥', 'KWQ': '昭山', 'ZAZ': '钟山西', 'ZXJ': '漳县', 'FYW': '资阳北', 'ZEJ': '张掖西', 'WZW': '资中北', 'ZAP': '涿州东', 'ZNK': '枣庄东', 'ZDC': '卓资东', 'ZAF': '郑州东', 'KVQ': '株洲南'}



