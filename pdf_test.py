import reportlab
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph
from datetime import datetime
from reportlab.pdfbase import pdfmetrics, ttfonts
from reportlab.lib.enums import TA_LEFT,TA_CENTER
from reportlab.lib import colors

pdfmetrics.registerFont(reportlab.pdfbase.ttfonts.TTFont('SimSun', 'SimSun.ttf'))  # 注册字体
# Function to create the PDF certificate with the specified background image
def create_certificate_with_specified_background(result_list,name,passed1,passed2,passed3,filename, background_img_path):
    c = canvas.Canvas(filename, pagesize=letter)
    # 繪製背景圖片
    c.drawImage(background_img_path, 0, 0, width=letter[0], height=letter[1], mask='auto')
    custom_red = colors.Color(0.8, 0, 0)  # 自定义一个较暗的红色
    # 设定段落样式：居中
    center_style = ParagraphStyle(
        'CenterAlign',
        fontName='SimSun',
        fontSize=30,
        leading=30,
        alignment=TA_CENTER,
        spaceAfter=12,
        textColor=custom_red
    )

    center_style1= ParagraphStyle(
        'CenterAlign',
        fontName='SimSun',
        fontSize=25,
        leading=30,
        alignment=TA_CENTER,
        spaceAfter=12,
        textColor=custom_red
    )

    style = ParagraphStyle(
        'LeftAlign',
        fontName='SimSun',
        fontSize=20,
        leading=50,
        alignment=TA_LEFT,
        spaceAfter=12,
    )

    style3 = ParagraphStyle(
        'LeftAlign',
        fontName='SimSun',
        fontSize=20,
        leading=50,
        alignment=TA_LEFT,
        spaceAfter=12,
        textColor=custom_red
    )

    style1 = ParagraphStyle(
        'LeftAlign',
        fontName='SimSun',
        fontSize=16,
        leading=25,
        alignment=TA_LEFT,
        spaceAfter=12,
    )
    # 在頁面中央添加段落
    text = (f"學員姓名: {name}<br/>"
            f"按壓深度: 平均深度 {round(result_list[0]*100,1)}%<br/>"
            f"按壓頻率: 平均頻率 {round(result_list[1]*100,1)}%  <br/>"
            f"按壓姿勢: 平均失敗次數 {result_list[2]} <br/>")

    text_result = (f"{passed1}!<br/>"
                   f"{passed2}!<br/>"
                   f"{passed3}!<br/>"
                   )

    p = Paragraph(text, style)
    p2 = Paragraph(text_result, style3)

    # 計算段落寬高並垂直居中
    w, h = p.wrap(letter[0], letter[1])
    w1, h1 = p2.wrap(letter[0], letter[1])
    p.drawOn(c, 130, 300)
    p2.drawOn(c, 400, 300)

    congrat_text = "恭喜通過   CPR教學輔助系統"
    congrat_text1 = "您未通過本次CPR教學輔助系統，請繼續加油！"
    # 单独居中的一行
    if result_list[0]>=0.8 and result_list[1]>=0.6:
        congrat_p = Paragraph(congrat_text, center_style)
        congrat_w, congrat_h = congrat_p.wrap(letter[0], letter[1])
        congrat_p.drawOn(c, (letter[0] - congrat_w) / 2, (letter[1] - h) / 2 - 40)  # 下移40pt以避免重叠
    else:
        congrat_text1 = ("您未通過本次CPR教學輔助系統"
                         " 請繼續加油！"
                         )

        congrat_p1 = Paragraph(congrat_text1, center_style1)
        congrat_w1, congrat_h1 = congrat_p1.wrap(letter[0], letter[1])
        congrat_p1.drawOn(c, 25, 265)




    # 轉換當前日期到中華民國曆並在證書底部添加
    roc_year = datetime.now().year - 1911
    date_str = f"中 華 民 國 {roc_year} 年 {datetime.now().month:02d} 月 {datetime.now().day:02d} 日"
    c.setFont('SimSun', 20)
    c.drawString(166, 200, date_str)

    # 在頁面右下方添加段落
    text1 = (f"評判標準<br/>"
            "深度: 平均按壓深度落在5-6公分達八成<br/>"
            "頻率: 平均按壓頻率落在100-120下/分鐘達六成<br/>"
            "姿勢: <=5次姿勢錯誤<br/>"
             )
    text2 = "*姿勢不採計標準，深度與頻率必須同時通過才合格*"
    p1 = Paragraph(text1, style1)
    p3 = Paragraph(text2, style1)
    w, h = p1.wrap(letter[0], letter[1])
    w, h = p3.wrap(letter[0], letter[1])
    p1.drawOn(c, 155, 60)
    p3.drawOn(c, 135, 30)

    # Save the PDF
    c.save()


# Participant's name
participant_name = "Jane Doe"

result_list_test = [0.7,0.7675,3]

Passed1 = "Passed"
Passed2 = "Not Passed"
Passed3 = "Passed"

# Filename for the saved PDF certificate
specified_background_pdf_filename = '/home/ezio/CPR_Project_Demo/CPR_Certificate/cpr_certificate.pdf'

# Path to the newly uploaded background image
specified_background_img_path = '/home/ezio/CPR_Project_Demo/pic/cpr_certificate_background3.png'

# Create the certificate with the specified background
create_certificate_with_specified_background(result_list_test,participant_name,Passed1,Passed2,Passed3,specified_background_pdf_filename, specified_background_img_path)
