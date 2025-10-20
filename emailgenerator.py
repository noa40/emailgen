# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PySide6.QtCore import Qt
from PySide6.QtCore import QMimeData

# Import the generated UI file
from ui_form import Ui_MainWindow

class MainWindow(QMainWindow):
    all_data = {
                'הפועלים': {
                    'פירוט אשראי' : (
                        '<p style="text-align: left;">זה מסמך שמפרט את כל הפעולות שנעשו באשראי שבבעלותך ומראים לנו מה ההעברות שביצעת</p>'
                        '<p style="text-align: left;">אנחנו דורשים פירוט של השלושה חודשים האחרונים.</p>'
                        '<p style="text-align: left;">ניתן להשיג אותו דרך אתר חברת האשראי בד"כ או מהבנק אליו משויך הכרטיס.</p>'
                        '<p style="text-align: left;">יש לשים לב שבדרך כלל המסמך מגיע כל חודש בנפרד, לכן לאחר שהשגת את שלושת החודשים האחרונים ניתן לאגד אותם לקובץ אחוד באתר הבא (<a href="https://gbr01.safelinks.protection.outlook.com/?url=https%3A%2F%2Fwww.adobe.com%2Facrobat%2Fonline%2Fmerge-pdf.html&amp;data=05%7C02%7Crecruitment%40moshalprogram.org%7C74175f9d59214f8b00a908de04b4aa10%7Cd01f81685d374261bf620ef33b01fe74%7C0%7C0%7C638953371177834321%7CUnknown%7CTWFpbGZsb3d8eyJFbXB0eU1hcGkiOnRydWUsIlYiOiIwLjAuMDAwMCIsIlAiOiJXaW4zMiIsIkFOIjoiTWFpbCIsIldUIjoyfQ%3D%3D%7C0%7C%7C%7C&amp;sdata=wkq2UmCfPx1TjyyRESi8jZMRnCr1B9H9EHleCO0hS1c%3D&amp;reserved=0">קישור</a>).</p>'
                        '<p style="text-align: left;">לאחר שאיגדת אותם יש להעלות אותם באתר תחת "פירוט אשראי - מועמד".</p>'
                    ),
                    'פירוט עו״ש' : (
                    '<p style="text-align: left;">זה מסמך שמפרט את כלל הפעולות שעשית בחשבון העובר ושב שלך בשלושה חודשים האחרונים.</p>'
                    '<p style="text-align: left;">מצרפת לך סרטון איך להשיג את המסמך הרלוונטי (<a href="https://www.youtube.com/watch?v=_2RnAk8UoEs">קישור</a>) מהבנק. יש לשים לב כי בחלק מן הבנקים לא ניתן לעשות זאת באפליקציה בנייד ולכן צריך מחשב.</p>'
                    '<p style="text-align: left;">אם אין באפשרותך להשיג מחשב צריך לפנות לבנק והוא יוכל להדפיס לך את המסמכים. לאחר סריקה באופן קריא ניתן להעלות אותם לאתר.</p>'
                    ),
                    'דוח ריכוז יתרות': (
                    '<p style="text-align:left;">דוח ריכוז יתרות הוא מסמך הבנקאי המשערך את כלל הנכסים בבעלותך. </p>'
                    '<p style="text-align:left;">.בתוכנית אנחנו מבקשים מסמך ריכוז יתרות <strong>עדכני לחודש זה ולא דוח ריכוז יתרות לסוף השנה</strong> </p>'
                    '<p style="text-align:left;">.ניתן להיעזר בסרטון הבא: (<a href="https://www.youtube.com/watch?v=AeMsrQEmJx0">קישור)</a> </p>'
                    '<p style="text-align:left;"> יש לשים לב כי לא ניתן להוציא מסמך זה דרך האפליקציה לכן יש להכנס לאתר האינטרנטי דרך מחשב או לחילופין לשוחח עם בנקאי</p>'
                    ),
                    'תשלום קצבה/ אסמכתא לקצבה': (
                    '<p style="text-align: left;">אם הינך או אחד מההורים שלך מקבלים קצבה, המלגה תבקש את פירוט התשלומים לכל הפחות בשלושה חודשים האחרונים.</p>'
                    '<p style = "text-align: left;">במידה והקצבה התקבלה מהביטוח הלאומי, ניתן להיעזר בקישור הבא: (<a href="https://www.btl.gov.il/%D7%98%D7%A4%D7%A1%D7%99%D7%9D%20%D7%95%D7%90%D7%99%D7%A9%D7%95%D7%A8%D7%99%D7%9D/%D7%90%D7%99%D7%A9%D7%95%D7%A8%D7%99%D7%9D/General_Authorizations/Pages/%D7%90%D7%99%D7%A9%D7%95%D7%A8%20%D7%AA%D7%A9%D7%9C%D7%95%D7%9E%D7%99%D7%9D%20%D7%A9%D7%A0%D7%AA%D7%99.aspx">קישור)</p>'
                    ),
                    'גיליון ציוני בגרות':(
                    '<p style = "text-align:left;">ניתן להוריד את גיליון ציוני הבגרות מאתר משרד החינוך בקישור הבא: (<a href= "https://www.gov.il/he/service/production-matriculation-certificate-and-grades">קישור)</p>'
                    ),
                    'פירוט חובות/הלוואות': (
                    '<p style="text-align:left";>מסמך רשמי המפרט על גובה החובות או ההלוואות שנלקחו.</p>'
                    '<p style="text-align:left";>נצטרך את גובה החוב או ההלוואה, כמה נותר לפירעון, תאריך התשלום הבא וכדומה..</p>'
                    '<p style="text-align:left";>במידה והחוב או ההלוואה נלקחו מהבנק, ניתן להיעזר בקישורים הבאים:(<a href="https://www.youtube.com/watch?v=FVOE0gkc8Bk">קישור)</p>'
                    ),
                    'מסמך לסילוק משכנתא': (
                    '<p style="text-align:left";>מסמך רשמי המפרט אודות תאריך לקיחת המשכנתא, גובהה וכמה נותר לשלם. ניתן לצרף מסמך ממנו נלקחה המשכנתא.</p>'
                    '<p style="text-align":left";>במידה והמשכנתא נקלחה מהבנק, ניתן להיעזר בקישור הבא: (<a href="https://www.youtube.com/watch?v=ALNLv_poRbM">קישור)</p>'
                    ),
                    'יתרת פיקדון צבאי':(
                    '<p style="text-align:left";>לאחר סיום השירות הצבאי, מתקבל פיקדון בהתאם לסוג השירות הצבאי הנעשה בידי האגף לחיילים משוררים וחיילי מילואים של משרד הביטחון. אנחנו דורשים מסמך המעיד באופן עדכני על היתרה של פיקדון זה. להלן השלבים להנפקת המסמך:</p>'
                    '<p style="text-align:left";> 1.נכנסים לאתר של האגף לחיילים משוחררים ומילואים בקישור הבא:  (<a href="https://www.hachvana.mod.gov.il/modseclogin/Dispatcher?TAM_OP=login&ERROR_CODE=0x00000000&ERROR_TEXT=HPDBA0521I%20%20%20Successful%20completion&URL=https%3A%2F%2Fwww.hachvana.mod.gov.il%2FHachvanaOnline%2F&h=www.hachvana.mod.gov.il&AUTHNLEVEL=&PROTOCOL=https">קישור)</p>'
                    '<p style="text-align:left";>2. נכנסים לאיזור האישי </p>'
                    '<p style="text-align:left";> 3.נכנסים ליתרת פיקדון</p>'
                    '<p style="text-align:left";>4. לוחצים על הדפס ושומרים את המסמך בנייד ולאחר מכן מעלים לאתר</p>'
                    ),
                    'תלוש שכר הורה':(
                    '<p style="text-align:left";>בתוכנית נבקש סריקה או מסמך ובו מופיע תלוש השכר של הוריכם נבקש שלושה תלושי שכר, אחד לכל חודש.</p>'
                    '<p style="text-align:left";>נבקש שתלושי השכר יהיו לכל היותר 4 חודשים אחורה. </p>'
                    ),
                    'ציון פסיכומטרי/ גליון ציונים/ מבחן יעל':(
                    '<p style="text-align:left";>הציונים נשלחים למייל איתם נרשמתם לבחינה. במידה ואינכם מוצאים את המייל עם קובץ הציונים ניתן להורידם מהאתר של מאל"ו בקישור הבא (<a href="https://www.nite.org.il/psychometric-entrance-test/scores/">קישור) </p>'
                    '<p style="text-align:left";> במידה ואינכם סטודנטים שנה א סמסטר א נבקש גם גיליון ציונים מהאוניברסיטה עבור לימודים אלו.</p>'
                    ),
                    'שומת מס לשנה הנוכחית': (
                    '<p style="text-align:left";>שומת מס הוא מסמך הניתן בסוף שנת מס ממשרד האוצר, הוא מסכם את כלל הרווחים, החובות והמיסים וניתן לאחר שהוגש דוח מס. ניתן להיעזר בסרטון הבא כדי להוציא אותו מהאתר (<a href="https://www.youtube.com/watch?v=4vHIyiLUtnc&t=2s">קישור) </p>'
                    '<p style="text-align:left";>לחילופין ניתן לפנות למשרד האוצר שישלחו את המסמך בדואר. </p>'
                    ),
                    'אסמכתא לניתוק קשר מהורה': (
                    '<p style="text-align:left";> מסמך רשמי בנוכחות עורך דין בו מצהירים כי אין קשר רגשי, חברתי או כלכלי עם ההורה ממנו מנותק הקשר.</p>'
                    '<p style="text-align:left";>לעיתים גם נקרא ״תצהיר אמת״ </p>'
                    ),
                    'מעמד לא עובד': (
                    '<p style="text-align:left";> זה מסמך רשמי מביטוח לאומי שמצהיר כי הוריך כרגע לא מועסק בשום עבודה וכאינו מוגדר כעובד במדינת ישראל. </p>'
                    '<p style="text-align:left";>ניתן להוציא את האישור בקישור הבא: (<a href="https://www.btl.gov.il/%D7%98%D7%A4%D7%A1%D7%99%D7%9D%20%D7%95%D7%90%D7%99%D7%A9%D7%95%D7%A8%D7%99%D7%9D/%D7%90%D7%99%D7%A9%D7%95%D7%A8%D7%99%D7%9D/Insurance_authorizations/Pages/%D7%90%D7%99%D7%A9%D7%95%D7%A8%20%D7%A2%D7%9C%20%D7%9E%D7%A2%D7%9E%D7%93%20%D7%9C%D7%90%20%D7%A2%D7%95%D7%91%D7%93.aspx">קישור) </p>'
                    '<p style="text-align:left";>לחילופין, ניתן להתקשר אל הביטוח הלאומי במספר *6050 או לפנות לאחת מעמדות השירות המפורזות ברחבי הארץ </p>'
                    '<p style="text-align:left";> שימו לב במקרים הבאים ההורה שלכם לא יהיה מוגדר במעמד לא עובד:גמלאי/פנסיונר, מקבל דמי אבטלה, תאונת עבודה, חל״ת.</p>'
                    '<p style="text-align:left";>ניתן לברר את המעמד בביטוח לאומי באתר תחת נתוני המבוטח. </p>'
                    )
                },
            'לאומי': {
            'פירוט אשראי' : (
                '<p style="text-align: left;">זה מסמך שמפרט את כל הפעולות שנעשו באשראי שבבעלותך ומראים לנו מה ההעברות שביצעת</p>'
                '<p style="text-align: left;">אנחנו דורשים פירוט של השלושה חודשים האחרונים.</p>'
                '<p style="text-align: left;">ניתן להשיג אותו דרך אתר חברת האשראי בד"כ או מהבנק אליו משויך הכרטיס.</p>'
                '<p style="text-align: left;">יש לשים לב שבדרך כלל המסמך מגיע כל חודש בנפרד, לכן לאחר שהשגת את שלושת החודשים האחרונים ניתן לאגד אותם לקובץ אחוד באתר הבא (<a href="https://gbr01.safelinks.protection.outlook.com/?url=https%3A%2F%2Fwww.adobe.com%2Facrobat%2Fonline%2Fmerge-pdf.html&amp;data=05%7C02%7Crecruitment%40moshalprogram.org%7C74175f9d59214f8b00a908de04b4aa10%7Cd01f81685d374261bf620ef33b01fe74%7C0%7C0%7C638953371177834321%7CUnknown%7CTWFpbGZsb3d8eyJFbXB0eU1hcGkiOnRydWUsIlYiOiIwLjAuMDAwMCIsIlAiOiJXaW4zMiIsIkFOIjoiTWFpbCIsIldUIjoyfQ%3D%3D%7C0%7C%7C%7C&amp;sdata=wkq2UmCfPx1TjyyRESi8jZMRnCr1B9H9EHleCO0hS1c%3D&amp;reserved=0">קישור</a>).</p>'
                '<p style="text-align: left;">לאחר שאיגדת אותם יש להעלות אותם באתר תחת "פירוט אשראי - מועמד".</p>'
            ),
            'פירוט עו״ש' : (
            '<p style="text-align: left;">זה מסמך שמפרט את כלל הפעולות שעשית בחשבון העובר ושב שלך בשלושה חודשים האחרונים.</p>'
            '<p style="text-align: left;">מצרפת לך סרטון איך להשיג את המסמך הרלוונטי (<a href="https://www.youtube.com/watch?v=egN2-oDhN58">קישור</a>) מהבנק. יש לשים לב כי בחלק מן הבנקים לא ניתן לעשות זאת באפליקציה בנייד ולכן צריך מחשב.</p>'
            '<p style="text-align: left;">אם אין באפשרותך להשיג מחשב צריך לפנות לבנק והוא יוכל להדפיס לך את המסמכים. לאחר סריקה באופן קריא ניתן להעלות אותם לאתר.</p>'
            ),
            'דוח ריכוז יתרות': (
            '<p style="text-align:left;">דוח ריכוז יתרות הוא מסמך הבנקאי המשערך את כלל הנכסים בבעלותך. </p>'
            '<p style="text-align:left;">.בתוכנית אנחנו מבקשים מסמך ריכוז יתרות <strong>עדכני לחודש זה ולא דוח ריכוז יתרות לסוף השנה</strong> </p>'
            '<p style="text-align:left;">.ניתן להיעזר בסרטון הבא: (<a href="https://www.youtube.com/watch?v=LYmGGYd8vvs">קישור)</a> </p>'
            '<p style="text-align:left;"> יש לשים לב כי לא ניתן להוציא מסמך זה דרך האפליקציה לכן יש להכנס לאתר האינטרנטי דרך מחשב או לחילופין לשוחח עם בנקאי</p>'
            ),
            'תשלום קצבה/ אסמכתא לקצבה': (
            '<p style="text-align: left;">אם הינך או אחד מההורים שלך מקבלים קצבה, המלגה תבקש את פירוט התשלומים לכל הפחות בשלושה חודשים האחרונים.</p>'
            '<p style = "text-align: left;">במידה והקצבה התקבלה מהביטוח הלאומי, ניתן להיעזר בקישור הבא: (<a href="https://www.btl.gov.il/%D7%98%D7%A4%D7%A1%D7%99%D7%9D%20%D7%95%D7%90%D7%99%D7%A9%D7%95%D7%A8%D7%99%D7%9D/%D7%90%D7%99%D7%A9%D7%95%D7%A8%D7%99%D7%9D/General_Authorizations/Pages/%D7%90%D7%99%D7%A9%D7%95%D7%A8%20%D7%AA%D7%A9%D7%9C%D7%95%D7%9E%D7%99%D7%9D%20%D7%A9%D7%A0%D7%AA%D7%99.aspx">קישור)</p>'
            ),
            'גיליון ציוני בגרות':(
            '<p style = "text-align:left;">ניתן להוריד את גיליון ציוני הבגרות מאתר משרד החינוך בקישור הבא: (<a href= "https://www.gov.il/he/service/production-matriculation-certificate-and-grades">קישור)</p>'
            ),
            'פירוט חובות/הלוואות': (
            '<p style="text-align:left";>מסמך רשמי המפרט על גובה החובות או ההלוואות שנלקחו.</p>'
            '<p style="text-align:left";>נצטרך את גובה החוב או ההלוואה, כמה נותר לפירעון, תאריך התשלום הבא וכדומה..</p>'
            '<p style="text-align:left";>במידה והחוב או ההלוואה נלקחו מהבנק, ניתן להיעזר בקישורים הבאים:(<a href="https://www.youtube.com/watch?v=O_AdhCvbePE">קישור)</p>'
            ),
            'מסמך לסילוק משכנתא': (
            '<p style="text-align:left";>מסמך רשמי המפרט אודות תאריך לקיחת המשכנתא, גובהה וכמה נותר לשלם. ניתן לצרף מסמך ממנו נלקחה המשכנתא.</p>'
            ),
            'יתרת פיקדון צבאי':(
            '<p style="text-align:left";>לאחר סיום השירות הצבאי, מתקבל פיקדון בהתאם לסוג השירות הצבאי הנעשה בידי האגף לחיילים משוררים וחיילי מילואים של משרד הביטחון. אנחנו דורשים מסמך המעיד באופן עדכני על היתרה של פיקדון זה. להלן השלבים להנפקת המסמך:</p>'
            '<p style="text-align:left";> 1.נכנסים לאתר של האגף לחיילים משוחררים ומילואים בקישור הבא:  (<a href="https://www.hachvana.mod.gov.il/modseclogin/Dispatcher?TAM_OP=login&ERROR_CODE=0x00000000&ERROR_TEXT=HPDBA0521I%20%20%20Successful%20completion&URL=https%3A%2F%2Fwww.hachvana.mod.gov.il%2FHachvanaOnline%2F&h=www.hachvana.mod.gov.il&AUTHNLEVEL=&PROTOCOL=https">קישור)</p>'
            '<p style="text-align:left";>2. נכנסים לאיזור האישי </p>'
            '<p style="text-align:left";> 3.נכנסים ליתרת פיקדון</p>'
            '<p style="text-align:left";>4. לוחצים על הדפס ושומרים את המסמך בנייד ולאחר מכן מעלים לאתר</p>'
            ),
            'תלוש שכר הורה':(
            '<p style="text-align:left";>בתוכנית נבקש סריקה או מסמך ובו מופיע תלוש השכר של הוריכם נבקש שלושה תלושי שכר, אחד לכל חודש.</p>'
            '<p style="text-align:left";>נבקש שתלושי השכר יהיו לכל היותר 4 חודשים אחורה. </p>'
            ),
            'ציון פסיכומטרי/ גליון ציונים/ מבחן יעל':(
            '<p style="text-align:left";>הציונים נשלחים למייל איתם נרשמתם לבחינה. במידה ואינכם מוצאים את המייל עם קובץ הציונים ניתן להורידם מהאתר של מאל"ו בקישור הבא (<a href="https://www.nite.org.il/psychometric-entrance-test/scores/">קישור) </p>'
            '<p style="text-align:left";> במידה ואינכם סטודנטים שנה א סמסטר א נבקש גם גיליון ציונים מהאוניברסיטה עבור לימודים אלו.</p>'
            ),
            'שומת מס לשנה הנוכחית': (
            '<p style="text-align:left";>שומת מס הוא מסמך הניתן בסוף שנת מס ממשרד האוצר, הוא מסכם את כלל הרווחים, החובות והמיסים וניתן לאחר שהוגש דוח מס. ניתן להיעזר בסרטון הבא כדי להוציא אותו מהאתר (<a href="https://www.youtube.com/watch?v=4vHIyiLUtnc&t=2s">קישור) </p>'
            '<p style="text-align:left";>לחילופין ניתן לפנות למשרד האוצר שישלחו את המסמך בדואר. </p>'
            ),
            'אסמכתא לניתוק קשר מהורה': (
            '<p style="text-align:left";> מסמך רשמי בנוכחות עורך דין בו מצהירים כי אין קשר רגשי, חברתי או כלכלי עם ההורה ממנו מנותק הקשר.</p>'
            '<p style="text-align:left";>לעיתים גם נקרא ״תצהיר אמת״ </p>'
            ),
            'מעמד לא עובד': (
            '<p style="text-align:left";> זה מסמך רשמי מביטוח לאומי שמצהיר כי הוריך כרגע לא מועסק בשום עבודה וכאינו מוגדר כעובד במדינת ישראל. </p>'
            '<p style="text-align:left";>ניתן להוציא את האישור בקישור הבא: (<a href="https://www.btl.gov.il/%D7%98%D7%A4%D7%A1%D7%99%D7%9D%20%D7%95%D7%90%D7%99%D7%A9%D7%95%D7%A8%D7%99%D7%9D/%D7%90%D7%99%D7%A9%D7%95%D7%A8%D7%99%D7%9D/Insurance_authorizations/Pages/%D7%90%D7%99%D7%A9%D7%95%D7%A8%20%D7%A2%D7%9C%20%D7%9E%D7%A2%D7%9E%D7%93%20%D7%9C%D7%90%20%D7%A2%D7%95%D7%91%D7%93.aspx">קישור) </p>'
            '<p style="text-align:left";>לחילופין, ניתן להתקשר אל הביטוח הלאומי במספר *6050 או לפנות לאחת מעמדות השירות המפורזות ברחבי הארץ </p>'
            '<p style="text-align:left";> שימו לב במקרים הבאים ההורה שלכם לא יהיה מוגדר במעמד לא עובד:גמלאי/פנסיונר, מקבל דמי אבטלה, תאונת עבודה, חל״ת.</p>'
            '<p style="text-align:left";>ניתן לברר את המעמד בביטוח לאומי באתר תחת נתוני המבוטח. </p>'
            )
        },

        'דיסקונט/מרכנתיל': {
        'פירוט אשראי' : (
        '<p style="text-align: left;">זה מסמך שמפרט את כל הפעולות שנעשו באשראי שבבעלותך ומראים לנו מה ההעברות שביצעת</p>'
        '<p style="text-align: left;">אנחנו דורשים פירוט של השלושה חודשים האחרונים.</p>'
        '<p style="text-align: left;">ניתן להשיג אותו דרך אתר חברת האשראי בד"כ או מהבנק אליו משויך הכרטיס.</p>'
        '<p style="text-align: left;">יש לשים לב שבדרך כלל המסמך מגיע כל חודש בנפרד, לכן לאחר שהשגת את שלושת החודשים האחרונים ניתן לאגד אותם לקובץ אחוד באתר הבא (<a href="https://gbr01.safelinks.protection.outlook.com/?url=https%3A%2F%2Fwww.adobe.com%2Facrobat%2Fonline%2Fmerge-pdf.html&amp;data=05%7C02%7Crecruitment%40moshalprogram.org%7C74175f9d59214f8b00a908de04b4aa10%7Cd01f81685d374261bf620ef33b01fe74%7C0%7C0%7C638953371177834321%7CUnknown%7CTWFpbGZsb3d8eyJFbXB0eU1hcGkiOnRydWUsIlYiOiIwLjAuMDAwMCIsIlAiOiJXaW4zMiIsIkFOIjoiTWFpbCIsIldUIjoyfQ%3D%3D%7C0%7C%7C%7C&amp;sdata=wkq2UmCfPx1TjyyRESi8jZMRnCr1B9H9EHleCO0hS1c%3D&amp;reserved=0">קישור</a>).</p>'
        '<p style="text-align: left;">לאחר שאיגדת אותם יש להעלות אותם באתר תחת "פירוט אשראי - מועמד".</p>'
        ),
        'פירוט עו״ש' : (
        '<p style="text-align: left;">זה מסמך שמפרט את כלל הפעולות שעשית בחשבון העובר ושב שלך בשלושה חודשים האחרונים.</p>'
        '<p style="text-align: left;">מצרפת לך סרטון איך להשיג את המסמך הרלוונטי (<a href="https://www.youtube.com/watch?v=KQ6kSSWq2E0">קישור</a>) מהבנק. יש לשים לב כי בחלק מן הבנקים לא ניתן לעשות זאת באפליקציה בנייד ולכן צריך מחשב.</p>'
        '<p style="text-align: left;">אם אין באפשרותך להשיג מחשב צריך לפנות לבנק והוא יוכל להדפיס לך את המסמכים. לאחר סריקה באופן קריא ניתן להעלות אותם לאתר.</p>'
        ),
        'דוח ריכוז יתרות': (
        '<p style="text-align:left;">דוח ריכוז יתרות הוא מסמך הבנקאי המשערך את כלל הנכסים בבעלותך. </p>'
        '<p style="text-align:left;">.בתוכנית אנחנו מבקשים מסמך ריכוז יתרות <strong>עדכני לחודש זה ולא דוח ריכוז יתרות לסוף השנה</strong> </p>'
        '<p style="text-align:left;">.ניתן להיעזר בסרטון הבא: (<a href="	https://www.youtube.com/watch?v=LYmGGYd8vvs">קישור)</a> </p>'
        '<p style="text-align:left;"> יש לשים לב כי לא ניתן להוציא מסמך זה דרך האפליקציה לכן יש להכנס לאתר האינטרנטי דרך מחשב או לחילופין לשוחח עם בנקאי</p>'
        ),
        'תשלום קצבה/ אסמכתא לקצבה': (
        '<p style="text-align: left;">אם הינך או אחד מההורים שלך מקבלים קצבה, המלגה תבקש את פירוט התשלומים לכל הפחות בשלושה חודשים האחרונים.</p>'
        '<p style = "text-align: left;">במידה והקצבה התקבלה מהביטוח הלאומי, ניתן להיעזר בקישור הבא: (<a href="https://www.btl.gov.il/%D7%98%D7%A4%D7%A1%D7%99%D7%9D%20%D7%95%D7%90%D7%99%D7%A9%D7%95%D7%A8%D7%99%D7%9D/%D7%90%D7%99%D7%A9%D7%95%D7%A8%D7%99%D7%9D/General_Authorizations/Pages/%D7%90%D7%99%D7%A9%D7%95%D7%A8%20%D7%AA%D7%A9%D7%9C%D7%95%D7%9E%D7%99%D7%9D%20%D7%A9%D7%A0%D7%AA%D7%99.aspx">קישור)</p>'
        ),
        'גיליון ציוני בגרות':(
        '<p style = "text-align:left;">ניתן להוריד את גיליון ציוני הבגרות מאתר משרד החינוך בקישור הבא: (<a href= "https://www.gov.il/he/service/production-matriculation-certificate-and-grades">קישור)</p>'
        ),
        'פירוט חובות/הלוואות': (
        '<p style="text-align:left";>מסמך רשמי המפרט על גובה החובות או ההלוואות שנלקחו.</p>'
        '<p style="text-align:left";>נצטרך את גובה החוב או ההלוואה, כמה נותר לפירעון, תאריך התשלום הבא וכדומה..</p>'
        '<p style="text-align:left";>במידה והחוב או ההלוואה נלקחו מהבנק, ניתן להיעזר בקישורים הבאים:(<a href="https://www.youtube.com/watch?v=Os7IRr9qXO8">קישור)</p>'
        ),
        'מסמך לסילוק משכנתא': (
        '<p style="text-align:left";>מסמך רשמי המפרט אודות תאריך לקיחת המשכנתא, גובהה וכמה נותר לשלם. ניתן לצרף מסמך ממנו נלקחה המשכנתא.</p>'
        ),
        'יתרת פיקדון צבאי':(
        '<p style="text-align:left";>לאחר סיום השירות הצבאי, מתקבל פיקדון בהתאם לסוג השירות הצבאי הנעשה בידי האגף לחיילים משוררים וחיילי מילואים של משרד הביטחון. אנחנו דורשים מסמך המעיד באופן עדכני על היתרה של פיקדון זה. להלן השלבים להנפקת המסמך:</p>'
        '<p style="text-align:left";> 1.נכנסים לאתר של האגף לחיילים משוחררים ומילואים בקישור הבא:  (<a href="https://www.hachvana.mod.gov.il/modseclogin/Dispatcher?TAM_OP=login&ERROR_CODE=0x00000000&ERROR_TEXT=HPDBA0521I%20%20%20Successful%20completion&URL=https%3A%2F%2Fwww.hachvana.mod.gov.il%2FHachvanaOnline%2F&h=www.hachvana.mod.gov.il&AUTHNLEVEL=&PROTOCOL=https">קישור)</p>'
        '<p style="text-align:left";>2. נכנסים לאיזור האישי </p>'
        '<p style="text-align:left";> 3.נכנסים ליתרת פיקדון</p>'
        '<p style="text-align:left";>4. לוחצים על הדפס ושומרים את המסמך בנייד ולאחר מכן מעלים לאתר</p>'
        ),
        'תלוש שכר הורה':(
        '<p style="text-align:left";>בתוכנית נבקש סריקה או מסמך ובו מופיע תלוש השכר של הוריכם נבקש שלושה תלושי שכר, אחד לכל חודש.</p>'
        '<p style="text-align:left";>נבקש שתלושי השכר יהיו לכל היותר 4 חודשים אחורה. </p>'
        ),
        'ציון פסיכומטרי/ גליון ציונים/ מבחן יעל':(
        '<p style="text-align:left";>הציונים נשלחים למייל איתם נרשמתם לבחינה. במידה ואינכם מוצאים את המייל עם קובץ הציונים ניתן להורידם מהאתר של מאל"ו בקישור הבא (<a href="https://www.nite.org.il/psychometric-entrance-test/scores/">קישור) </p>'
        '<p style="text-align:left";> במידה ואינכם סטודנטים שנה א סמסטר א נבקש גם גיליון ציונים מהאוניברסיטה עבור לימודים אלו.</p>'
        ),
        'שומת מס לשנה הנוכחית': (
        '<p style="text-align:left";>שומת מס הוא מסמך הניתן בסוף שנת מס ממשרד האוצר, הוא מסכם את כלל הרווחים, החובות והמיסים וניתן לאחר שהוגש דוח מס. ניתן להיעזר בסרטון הבא כדי להוציא אותו מהאתר (<a href="https://www.youtube.com/watch?v=4vHIyiLUtnc&t=2s">קישור) </p>'
        '<p style="text-align:left";>לחילופין ניתן לפנות למשרד האוצר שישלחו את המסמך בדואר. </p>'
        ),
        'אסמכתא לניתוק קשר מהורה': (
        '<p style="text-align:left";> מסמך רשמי בנוכחות עורך דין בו מצהירים כי אין קשר רגשי, חברתי או כלכלי עם ההורה ממנו מנותק הקשר.</p>'
        '<p style="text-align:left";>לעיתים גם נקרא ״תצהיר אמת״ </p>'
        ),
        'מעמד לא עובד': (
        '<p style="text-align:left";> זה מסמך רשמי מביטוח לאומי שמצהיר כי הוריך כרגע לא מועסק בשום עבודה וכאינו מוגדר כעובד במדינת ישראל. </p>'
        '<p style="text-align:left";>ניתן להוציא את האישור בקישור הבא: (<a href="https://www.btl.gov.il/%D7%98%D7%A4%D7%A1%D7%99%D7%9D%20%D7%95%D7%90%D7%99%D7%A9%D7%95%D7%A8%D7%99%D7%9D/%D7%90%D7%99%D7%A9%D7%95%D7%A8%D7%99%D7%9D/Insurance_authorizations/Pages/%D7%90%D7%99%D7%A9%D7%95%D7%A8%20%D7%A2%D7%9C%20%D7%9E%D7%A2%D7%9E%D7%93%20%D7%9C%D7%90%20%D7%A2%D7%95%D7%91%D7%93.aspx">קישור) </p>'
        '<p style="text-align:left";>לחילופין, ניתן להתקשר אל הביטוח הלאומי במספר *6050 או לפנות לאחת מעמדות השירות המפורזות ברחבי הארץ </p>'
        '<p style="text-align:left";> שימו לב במקרים הבאים ההורה שלכם לא יהיה מוגדר במעמד לא עובד:גמלאי/פנסיונר, מקבל דמי אבטלה, תאונת עבודה, חל״ת.</p>'
        '<p style="text-align:left";>ניתן לברר את המעמד בביטוח לאומי באתר תחת נתוני המבוטח. </p>'
        )
        },
        'מזרחי טפחות': {
        'פירוט אשראי' : (
        '<p style="text-align: left;">זה מסמך שמפרט את כל הפעולות שנעשו באשראי שבבעלותך ומראים לנו מה ההעברות שביצעת</p>'
        '<p style="text-align: left;">אנחנו דורשים פירוט של השלושה חודשים האחרונים.</p>'
        '<p style="text-align: left;">ניתן להשיג אותו דרך אתר חברת האשראי בד"כ או מהבנק אליו משויך הכרטיס.</p>'
        '<p style="text-align: left;">יש לשים לב שבדרך כלל המסמך מגיע כל חודש בנפרד, לכן לאחר שהשגת את שלושת החודשים האחרונים ניתן לאגד אותם לקובץ אחוד באתר הבא (<a href="https://gbr01.safelinks.protection.outlook.com/?url=https%3A%2F%2Fwww.adobe.com%2Facrobat%2Fonline%2Fmerge-pdf.html&amp;data=05%7C02%7Crecruitment%40moshalprogram.org%7C74175f9d59214f8b00a908de04b4aa10%7Cd01f81685d374261bf620ef33b01fe74%7C0%7C0%7C638953371177834321%7CUnknown%7CTWFpbGZsb3d8eyJFbXB0eU1hcGkiOnRydWUsIlYiOiIwLjAuMDAwMCIsIlAiOiJXaW4zMiIsIkFOIjoiTWFpbCIsIldUIjoyfQ%3D%3D%7C0%7C%7C%7C&amp;sdata=wkq2UmCfPx1TjyyRESi8jZMRnCr1B9H9EHleCO0hS1c%3D&amp;reserved=0">קישור</a>).</p>'
        '<p style="text-align: left;">לאחר שאיגדת אותם יש להעלות אותם באתר תחת "פירוט אשראי - מועמד".</p>'
        ),
        'פירוט עו״ש' : (
        '<p style="text-align: left;">זה מסמך שמפרט את כלל הפעולות שעשית בחשבון העובר ושב שלך בשלושה חודשים האחרונים.</p>'
        '<p style="text-align: left;">מצרפת לך סרטון איך להשיג את המסמך הרלוונטי (<a href="https://www.youtube.com/watch?v=raXTAmuSr-U">קישור</a>) מהבנק. יש לשים לב כי בחלק מן הבנקים לא ניתן לעשות זאת באפליקציה בנייד ולכן צריך מחשב.</p>'
        '<p style="text-align: left;">אם אין באפשרותך להשיג מחשב צריך לפנות לבנק והוא יוכל להדפיס לך את המסמכים. לאחר סריקה באופן קריא ניתן להעלות אותם לאתר.</p>'
        ),
        'דוח ריכוז יתרות': (
        '<p style="text-align:left;">דוח ריכוז יתרות הוא מסמך הבנקאי המשערך את כלל הנכסים בבעלותך. </p>'
        '<p style="text-align:left;">.בתוכנית אנחנו מבקשים מסמך ריכוז יתרות <strong>עדכני לחודש זה ולא דוח ריכוז יתרות לסוף השנה</strong> </p>'
        '<p style="text-align:left;">.ניתן להיעזר בסרטון הבא: (<a href="	https://www.youtube.com/watch?v=snJS-6isIrQ">קישור)</a> </p>'
        '<p style="text-align:left;"> יש לשים לב כי לא ניתן להוציא מסמך זה דרך האפליקציה לכן יש להכנס לאתר האינטרנטי דרך מחשב או לחילופין לשוחח עם בנקאי</p>'
        ),
        'תשלום קצבה/ אסמכתא לקצבה': (
        '<p style="text-align: left;">אם הינך או אחד מההורים שלך מקבלים קצבה, המלגה תבקש את פירוט התשלומים לכל הפחות בשלושה חודשים האחרונים.</p>'
        '<p style = "text-align: left;">במידה והקצבה התקבלה מהביטוח הלאומי, ניתן להיעזר בקישור הבא: (<a href="https://www.btl.gov.il/%D7%98%D7%A4%D7%A1%D7%99%D7%9D%20%D7%95%D7%90%D7%99%D7%A9%D7%95%D7%A8%D7%99%D7%9D/%D7%90%D7%99%D7%A9%D7%95%D7%A8%D7%99%D7%9D/General_Authorizations/Pages/%D7%90%D7%99%D7%A9%D7%95%D7%A8%20%D7%AA%D7%A9%D7%9C%D7%95%D7%9E%D7%99%D7%9D%20%D7%A9%D7%A0%D7%AA%D7%99.aspx">קישור)</p>'
        ),
        'גיליון ציוני בגרות':(
        '<p style = "text-align:left;">ניתן להוריד את גיליון ציוני הבגרות מאתר משרד החינוך בקישור הבא: (<a href= "https://www.gov.il/he/service/production-matriculation-certificate-and-grades">קישור)</p>'
        ),
        'פירוט חובות/הלוואות': (
        '<p style="text-align:left";>מסמך רשמי המפרט על גובה החובות או ההלוואות שנלקחו.</p>'
        '<p style="text-align:left";>נצטרך את גובה החוב או ההלוואה, כמה נותר לפירעון, תאריך התשלום הבא וכדומה..</p>'
        '<p style="text-align:left";>במידה והחוב או ההלוואה נלקחו מהבנק, ניתן להיעזר בקישורים הבאים:(<a href="">קישור)</p>'
        ),
        'מסמך לסילוק משכנתא': (
        '<p style="text-align:left";>מסמך רשמי המפרט אודות תאריך לקיחת המשכנתא, גובהה וכמה נותר לשלם. ניתן לצרף מסמך ממנו נלקחה המשכנתא.</p>'
        '<p style="text-align":left";>במידה והמשכנתא נקלחה מהבנק, ניתן להיעזר בקישור הבא: (<a href="https://www.youtube.com/watch?v=XedY4TCKETQ">קישור)</p>'
        ),
        'יתרת פיקדון צבאי':(
        '<p style="text-align:left";>לאחר סיום השירות הצבאי, מתקבל פיקדון בהתאם לסוג השירות הצבאי הנעשה בידי האגף לחיילים משוררים וחיילי מילואים של משרד הביטחון. אנחנו דורשים מסמך המעיד באופן עדכני על היתרה של פיקדון זה. להלן השלבים להנפקת המסמך:</p>'
        '<p style="text-align:left";> 1.נכנסים לאתר של האגף לחיילים משוחררים ומילואים בקישור הבא:  (<a href="https://www.hachvana.mod.gov.il/modseclogin/Dispatcher?TAM_OP=login&ERROR_CODE=0x00000000&ERROR_TEXT=HPDBA0521I%20%20%20Successful%20completion&URL=https%3A%2F%2Fwww.hachvana.mod.gov.il%2FHachvanaOnline%2F&h=www.hachvana.mod.gov.il&AUTHNLEVEL=&PROTOCOL=https">קישור)</p>'
        '<p style="text-align:left";>2. נכנסים לאיזור האישי </p>'
        '<p style="text-align:left";> 3.נכנסים ליתרת פיקדון</p>'
        '<p style="text-align:left";>4. לוחצים על הדפס ושומרים את המסמך בנייד ולאחר מכן מעלים לאתר</p>'
        ),
        'תלוש שכר הורה':(
        '<p style="text-align:left";>בתוכנית נבקש סריקה או מסמך ובו מופיע תלוש השכר של הוריכם נבקש שלושה תלושי שכר, אחד לכל חודש.</p>'
        '<p style="text-align:left";>נבקש שתלושי השכר יהיו לכל היותר 4 חודשים אחורה. </p>'
        ),
        'ציון פסיכומטרי/ גליון ציונים/ מבחן יעל':(
        '<p style="text-align:left";>הציונים נשלחים למייל איתם נרשמתם לבחינה. במידה ואינכם מוצאים את המייל עם קובץ הציונים ניתן להורידם מהאתר של מאל"ו בקישור הבא (<a href="https://www.nite.org.il/psychometric-entrance-test/scores/">קישור) </p>'
        '<p style="text-align:left";> במידה ואינכם סטודנטים שנה א סמסטר א נבקש גם גיליון ציונים מהאוניברסיטה עבור לימודים אלו.</p>'
        ),
        'שומת מס לשנה הנוכחית': (
        '<p style="text-align:left";>שומת מס הוא מסמך הניתן בסוף שנת מס ממשרד האוצר, הוא מסכם את כלל הרווחים, החובות והמיסים וניתן לאחר שהוגש דוח מס. ניתן להיעזר בסרטון הבא כדי להוציא אותו מהאתר (<a href="https://www.youtube.com/watch?v=4vHIyiLUtnc&t=2s">קישור) </p>'
        '<p style="text-align:left";>לחילופין ניתן לפנות למשרד האוצר שישלחו את המסמך בדואר. </p>'
        ),
        'אסמכתא לניתוק קשר מהורה': (
        '<p style="text-align:left";> מסמך רשמי בנוכחות עורך דין בו מצהירים כי אין קשר רגשי, חברתי או כלכלי עם ההורה ממנו מנותק הקשר.</p>'
        '<p style="text-align:left";>לעיתים גם נקרא ״תצהיר אמת״ </p>'
        ),
        'מעמד לא עובד': (
        '<p style="text-align:left";> זה מסמך רשמי מביטוח לאומי שמצהיר כי הוריך כרגע לא מועסק בשום עבודה וכאינו מוגדר כעובד במדינת ישראל. </p>'
        '<p style="text-align:left";>ניתן להוציא את האישור בקישור הבא: (<a href="https://www.btl.gov.il/%D7%98%D7%A4%D7%A1%D7%99%D7%9D%20%D7%95%D7%90%D7%99%D7%A9%D7%95%D7%A8%D7%99%D7%9D/%D7%90%D7%99%D7%A9%D7%95%D7%A8%D7%99%D7%9D/Insurance_authorizations/Pages/%D7%90%D7%99%D7%A9%D7%95%D7%A8%20%D7%A2%D7%9C%20%D7%9E%D7%A2%D7%9E%D7%93%20%D7%9C%D7%90%20%D7%A2%D7%95%D7%91%D7%93.aspx">קישור) </p>'
        '<p style="text-align:left";>לחילופין, ניתן להתקשר אל הביטוח הלאומי במספר *6050 או לפנות לאחת מעמדות השירות המפורזות ברחבי הארץ </p>'
        '<p style="text-align:left";> שימו לב במקרים הבאים ההורה שלכם לא יהיה מוגדר במעמד לא עובד:גמלאי/פנסיונר, מקבל דמי אבטלה, תאונת עבודה, חל״ת.</p>'
        '<p style="text-align:left";>ניתן לברר את המעמד בביטוח לאומי באתר תחת נתוני המבוטח. </p>'
        )
        },
        'הבינלאומי': {
        'פירוט אשראי' : (
        '<p style="text-align: left;">זה מסמך שמפרט את כל הפעולות שנעשו באשראי שבבעלותך ומראים לנו מה ההעברות שביצעת</p>'
        '<p style="text-align: left;">אנחנו דורשים פירוט של השלושה חודשים האחרונים.</p>'
        '<p style="text-align: left;">ניתן להשיג אותו דרך אתר חברת האשראי בד"כ או מהבנק אליו משויך הכרטיס.</p>'
        '<p style="text-align: left;">יש לשים לב שבדרך כלל המסמך מגיע כל חודש בנפרד, לכן לאחר שהשגת את שלושת החודשים האחרונים ניתן לאגד אותם לקובץ אחוד באתר הבא (<a href="https://gbr01.safelinks.protection.outlook.com/?url=https%3A%2F%2Fwww.adobe.com%2Facrobat%2Fonline%2Fmerge-pdf.html&amp;data=05%7C02%7Crecruitment%40moshalprogram.org%7C74175f9d59214f8b00a908de04b4aa10%7Cd01f81685d374261bf620ef33b01fe74%7C0%7C0%7C638953371177834321%7CUnknown%7CTWFpbGZsb3d8eyJFbXB0eU1hcGkiOnRydWUsIlYiOiIwLjAuMDAwMCIsIlAiOiJXaW4zMiIsIkFOIjoiTWFpbCIsIldUIjoyfQ%3D%3D%7C0%7C%7C%7C&amp;sdata=wkq2UmCfPx1TjyyRESi8jZMRnCr1B9H9EHleCO0hS1c%3D&amp;reserved=0">קישור</a>).</p>'
        '<p style="text-align: left;">לאחר שאיגדת אותם יש להעלות אותם באתר תחת "פירוט אשראי - מועמד".</p>'
        ),
        'פירוט עו״ש' : (
        '<p style="text-align: left;">זה מסמך שמפרט את כלל הפעולות שעשית בחשבון העובר ושב שלך בשלושה חודשים האחרונים.</p>'
        '<p style="text-align: left;">מצרפת לך סרטון איך להשיג את המסמך הרלוונטי (<a href="https://www.youtube.com/watch?v=daxcPC7GmNs">קישור</a>) מהבנק. יש לשים לב כי בחלק מן הבנקים לא ניתן לעשות זאת באפליקציה בנייד ולכן צריך מחשב.</p>'
        '<p style="text-align: left;">אם אין באפשרותך להשיג מחשב צריך לפנות לבנק והוא יוכל להדפיס לך את המסמכים. לאחר סריקה באופן קריא ניתן להעלות אותם לאתר.</p>'
        ),
        'דוח ריכוז יתרות': (
        '<p style="text-align:left;">דוח ריכוז יתרות הוא מסמך הבנקאי המשערך את כלל הנכסים בבעלותך. </p>'
        '<p style="text-align:left;">.בתוכנית אנחנו מבקשים מסמך ריכוז יתרות <strong>עדכני לחודש זה ולא דוח ריכוז יתרות לסוף השנה</strong> </p>'
        '<p style="text-align:left;">.ניתן להיעזר בסרטון הבא: (<a href="https://www.youtube.com/watch?v=gijc1q_pcuw&t=6s">קישור)</a> </p>'
        '<p style="text-align:left;"> יש לשים לב כי לא ניתן להוציא מסמך זה דרך האפליקציה לכן יש להכנס לאתר האינטרנטי דרך מחשב או לחילופין לשוחח עם בנקאי</p>'
        ),
        'תשלום קצבה/ אסמכתא לקצבה': (
        '<p style="text-align: left;">אם הינך או אחד מההורים שלך מקבלים קצבה, המלגה תבקש את פירוט התשלומים לכל הפחות בשלושה חודשים האחרונים.</p>'
        '<p style = "text-align: left;">במידה והקצבה התקבלה מהביטוח הלאומי, ניתן להיעזר בקישור הבא: (<a href="https://www.btl.gov.il/%D7%98%D7%A4%D7%A1%D7%99%D7%9D%20%D7%95%D7%90%D7%99%D7%A9%D7%95%D7%A8%D7%99%D7%9D/%D7%90%D7%99%D7%A9%D7%95%D7%A8%D7%99%D7%9D/General_Authorizations/Pages/%D7%90%D7%99%D7%A9%D7%95%D7%A8%20%D7%AA%D7%A9%D7%9C%D7%95%D7%9E%D7%99%D7%9D%20%D7%A9%D7%A0%D7%AA%D7%99.aspx">קישור)</p>'
        ),
        'גיליון ציוני בגרות':(
        '<p style = "text-align:left;">ניתן להוריד את גיליון ציוני הבגרות מאתר משרד החינוך בקישור הבא: (<a href= "https://www.gov.il/he/service/production-matriculation-certificate-and-grades">קישור)</p>'
        ),
        'פירוט חובות/הלוואות': (
        '<p style="text-align:left";>מסמך רשמי המפרט על גובה החובות או ההלוואות שנלקחו.</p>'
        '<p style="text-align:left";>נצטרך את גובה החוב או ההלוואה, כמה נותר לפירעון, תאריך התשלום הבא וכדומה..</p>'
        '<p style="text-align:left";>במידה והחוב או ההלוואה נלקחו מהבנק, ניתן להיעזר בקישורים הבאים:(<a href="https://www.youtube.com/watch?v=m2yclByduco">קישור)</p>'
        ),
        'מסמך לסילוק משכנתא': (
        '<p style="text-align:left";>מסמך רשמי המפרט אודות תאריך לקיחת המשכנתא, גובהה וכמה נותר לשלם. ניתן לצרף מסמך ממנו נלקחה המשכנתא.</p>'
        '<p style="text-align":left";>במידה והמשכנתא נקלחה מהבנק, ניתן להיעזר בקישור הבא: (<a href="https://www.youtube.com/watch?v=RZJlTAYzoIM">קישור)</p>'
        ),
        'יתרת פיקדון צבאי':(
        '<p style="text-align:left";>לאחר סיום השירות הצבאי, מתקבל פיקדון בהתאם לסוג השירות הצבאי הנעשה בידי האגף לחיילים משוררים וחיילי מילואים של משרד הביטחון. אנחנו דורשים מסמך המעיד באופן עדכני על היתרה של פיקדון זה. להלן השלבים להנפקת המסמך:</p>'
        '<p style="text-align:left";> 1.נכנסים לאתר של האגף לחיילים משוחררים ומילואים בקישור הבא:  (<a href="https://www.hachvana.mod.gov.il/modseclogin/Dispatcher?TAM_OP=login&ERROR_CODE=0x00000000&ERROR_TEXT=HPDBA0521I%20%20%20Successful%20completion&URL=https%3A%2F%2Fwww.hachvana.mod.gov.il%2FHachvanaOnline%2F&h=www.hachvana.mod.gov.il&AUTHNLEVEL=&PROTOCOL=https">קישור)</p>'
        '<p style="text-align:left";>2. נכנסים לאיזור האישי </p>'
        '<p style="text-align:left";> 3.נכנסים ליתרת פיקדון</p>'
        '<p style="text-align:left";>4. לוחצים על הדפס ושומרים את המסמך בנייד ולאחר מכן מעלים לאתר</p>'
        ),
        'תלוש שכר הורה':(
        '<p style="text-align:left";>בתוכנית נבקש סריקה או מסמך ובו מופיע תלוש השכר של הוריכם נבקש שלושה תלושי שכר, אחד לכל חודש.</p>'
        '<p style="text-align:left";>נבקש שתלושי השכר יהיו לכל היותר 4 חודשים אחורה. </p>'
        ),
        'ציון פסיכומטרי/ גליון ציונים/ מבחן יעל':(
        '<p style="text-align:left";>הציונים נשלחים למייל איתם נרשמתם לבחינה. במידה ואינכם מוצאים את המייל עם קובץ הציונים ניתן להורידם מהאתר של מאל"ו בקישור הבא (<a href="https://www.nite.org.il/psychometric-entrance-test/scores/">קישור) </p>'
        '<p style="text-align:left";> במידה ואינכם סטודנטים שנה א סמסטר א נבקש גם גיליון ציונים מהאוניברסיטה עבור לימודים אלו.</p>'
        ),
        'שומת מס לשנה הנוכחית': (
        '<p style="text-align:left";>שומת מס הוא מסמך הניתן בסוף שנת מס ממשרד האוצר, הוא מסכם את כלל הרווחים, החובות והמיסים וניתן לאחר שהוגש דוח מס. ניתן להיעזר בסרטון הבא כדי להוציא אותו מהאתר (<a href="https://www.youtube.com/watch?v=4vHIyiLUtnc&t=2s">קישור) </p>'
        '<p style="text-align:left";>לחילופין ניתן לפנות למשרד האוצר שישלחו את המסמך בדואר. </p>'
        ),
        'אסמכתא לניתוק קשר מהורה': (
        '<p style="text-align:left";> מסמך רשמי בנוכחות עורך דין בו מצהירים כי אין קשר רגשי, חברתי או כלכלי עם ההורה ממנו מנותק הקשר.</p>'
        '<p style="text-align:left";>לעיתים גם נקרא ״תצהיר אמת״ </p>'
        ),
        'מעמד לא עובד': (
        '<p style="text-align:left";> זה מסמך רשמי מביטוח לאומי שמצהיר כי הוריך כרגע לא מועסק בשום עבודה וכאינו מוגדר כעובד במדינת ישראל. </p>'
        '<p style="text-align:left";>ניתן להוציא את האישור בקישור הבא: (<a href="https://www.btl.gov.il/%D7%98%D7%A4%D7%A1%D7%99%D7%9D%20%D7%95%D7%90%D7%99%D7%A9%D7%95%D7%A8%D7%99%D7%9D/%D7%90%D7%99%D7%A9%D7%95%D7%A8%D7%99%D7%9D/Insurance_authorizations/Pages/%D7%90%D7%99%D7%A9%D7%95%D7%A8%20%D7%A2%D7%9C%20%D7%9E%D7%A2%D7%9E%D7%93%20%D7%9C%D7%90%20%D7%A2%D7%95%D7%91%D7%93.aspx">קישור) </p>'
        '<p style="text-align:left";>לחילופין, ניתן להתקשר אל הביטוח הלאומי במספר *6050 או לפנות לאחת מעמדות השירות המפורזות ברחבי הארץ </p>'
        '<p style="text-align:left";> שימו לב במקרים הבאים ההורה שלכם לא יהיה מוגדר במעמד לא עובד:גמלאי/פנסיונר, מקבל דמי אבטלה, תאונת עבודה, חל״ת.</p>'
        '<p style="text-align:left";>ניתן לברר את המעמד בביטוח לאומי באתר תחת נתוני המבוטח. </p>'
        )
        },
        'בנק הדואר': {
        'פירוט אשראי' : (
        '<p style="text-align: left;">זה מסמך שמפרט את כל הפעולות שנעשו באשראי שבבעלותך ומראים לנו מה ההעברות שביצעת</p>'
        '<p style="text-align: left;">אנחנו דורשים פירוט של השלושה חודשים האחרונים.</p>'
        '<p style="text-align: left;">ניתן להשיג אותו דרך אתר חברת האשראי בד"כ או מהבנק אליו משויך הכרטיס.</p>'
        '<p style="text-align: left;">יש לשים לב שבדרך כלל המסמך מגיע כל חודש בנפרד, לכן לאחר שהשגת את שלושת החודשים האחרונים ניתן לאגד אותם לקובץ אחוד באתר הבא (<a href="https://gbr01.safelinks.protection.outlook.com/?url=https%3A%2F%2Fwww.adobe.com%2Facrobat%2Fonline%2Fmerge-pdf.html&amp;data=05%7C02%7Crecruitment%40moshalprogram.org%7C74175f9d59214f8b00a908de04b4aa10%7Cd01f81685d374261bf620ef33b01fe74%7C0%7C0%7C638953371177834321%7CUnknown%7CTWFpbGZsb3d8eyJFbXB0eU1hcGkiOnRydWUsIlYiOiIwLjAuMDAwMCIsIlAiOiJXaW4zMiIsIkFOIjoiTWFpbCIsIldUIjoyfQ%3D%3D%7C0%7C%7C%7C&amp;sdata=wkq2UmCfPx1TjyyRESi8jZMRnCr1B9H9EHleCO0hS1c%3D&amp;reserved=0">קישור</a>).</p>'
        '<p style="text-align: left;">לאחר שאיגדת אותם יש להעלות אותם באתר תחת "פירוט אשראי - מועמד".</p>'
        ),
        'פירוט עו״ש' : (
        '<p style="text-align: left;">זה מסמך שמפרט את כלל הפעולות שעשית בחשבון העובר ושב שלך בשלושה חודשים האחרונים.</p>'
        '<p style="text-align: left;">מצרפת לך סרטון איך להשיג את המסמך הרלוונטי (<a href="https://www.youtube.com/watch?v=PR5TKfwSnp0">קישור</a>) מהבנק. יש לשים לב כי בחלק מן הבנקים לא ניתן לעשות זאת באפליקציה בנייד ולכן צריך מחשב.</p>'
        '<p style="text-align: left;">אם אין באפשרותך להשיג מחשב צריך לפנות לבנק והוא יוכל להדפיס לך את המסמכים. לאחר סריקה באופן קריא ניתן להעלות אותם לאתר.</p>'
        ),
        'דוח ריכוז יתרות': (
        '<p style="text-align:left;">דוח ריכוז יתרות הוא מסמך הבנקאי המשערך את כלל הנכסים בבעלותך. </p>'
        '<p style="text-align:left;">.בתוכנית אנחנו מבקשים מסמך ריכוז יתרות <strong>עדכני לחודש זה ולא דוח ריכוז יתרות לסוף השנה</strong> </p>'
        '<p style="text-align:left;">.ניתן להיעזר בסרטון הבא: (<a href="https://www.youtube.com/watch?v=XyW2JkVzWGc">קישור)</a> </p>'
        '<p style="text-align:left;"> יש לשים לב כי לא ניתן להוציא מסמך זה דרך האפליקציה לכן יש להכנס לאתר האינטרנטי דרך מחשב או לחילופין לשוחח עם בנקאי</p>'
        ),
        'תשלום קצבה/ אסמכתא לקצבה': (
        '<p style="text-align: left;">אם הינך או אחד מההורים שלך מקבלים קצבה, המלגה תבקש את פירוט התשלומים לכל הפחות בשלושה חודשים האחרונים.</p>'
        '<p style = "text-align: left;">במידה והקצבה התקבלה מהביטוח הלאומי, ניתן להיעזר בקישור הבא: (<a href="https://www.btl.gov.il/%D7%98%D7%A4%D7%A1%D7%99%D7%9D%20%D7%95%D7%90%D7%99%D7%A9%D7%95%D7%A8%D7%99%D7%9D/%D7%90%D7%99%D7%A9%D7%95%D7%A8%D7%99%D7%9D/General_Authorizations/Pages/%D7%90%D7%99%D7%A9%D7%95%D7%A8%20%D7%AA%D7%A9%D7%9C%D7%95%D7%9E%D7%99%D7%9D%20%D7%A9%D7%A0%D7%AA%D7%99.aspx">קישור)</p>'
        ),
        'גיליון ציוני בגרות':(
        '<p style = "text-align:left;">ניתן להוריד את גיליון ציוני הבגרות מאתר משרד החינוך בקישור הבא: (<a href= "https://www.gov.il/he/service/production-matriculation-certificate-and-grades">קישור)</p>'
        ),
        'פירוט חובות/הלוואות': (
        '<p style="text-align:left";>מסמך רשמי המפרט על גובה החובות או ההלוואות שנלקחו.</p>'
        '<p style="text-align:left";>נצטרך את גובה החוב או ההלוואה, כמה נותר לפירעון, תאריך התשלום הבא וכדומה..</p>'
        ),
        'מסמך לסילוק משכנתא': (
        '<p style="text-align:left";>מסמך רשמי המפרט אודות תאריך לקיחת המשכנתא, גובהה וכמה נותר לשלם. ניתן לצרף מסמך ממנו נלקחה המשכנתא.</p>'
        ),
        'יתרת פיקדון צבאי':(
        '<p style="text-align:left";>לאחר סיום השירות הצבאי, מתקבל פיקדון בהתאם לסוג השירות הצבאי הנעשה בידי האגף לחיילים משוררים וחיילי מילואים של משרד הביטחון. אנחנו דורשים מסמך המעיד באופן עדכני על היתרה של פיקדון זה. להלן השלבים להנפקת המסמך:</p>'
        '<p style="text-align:left";> 1.נכנסים לאתר של האגף לחיילים משוחררים ומילואים בקישור הבא:  (<a href="https://www.hachvana.mod.gov.il/modseclogin/Dispatcher?TAM_OP=login&ERROR_CODE=0x00000000&ERROR_TEXT=HPDBA0521I%20%20%20Successful%20completion&URL=https%3A%2F%2Fwww.hachvana.mod.gov.il%2FHachvanaOnline%2F&h=www.hachvana.mod.gov.il&AUTHNLEVEL=&PROTOCOL=https">קישור)</p>'
        '<p style="text-align:left";>2. נכנסים לאיזור האישי </p>'
        '<p style="text-align:left";> 3.נכנסים ליתרת פיקדון</p>'
        '<p style="text-align:left";>4. לוחצים על הדפס ושומרים את המסמך בנייד ולאחר מכן מעלים לאתר</p>'
        ),
        'תלוש שכר הורה':(
        '<p style="text-align:left";>בתוכנית נבקש סריקה או מסמך ובו מופיע תלוש השכר של הוריכם נבקש שלושה תלושי שכר, אחד לכל חודש.</p>'
        '<p style="text-align:left";>נבקש שתלושי השכר יהיו לכל היותר 4 חודשים אחורה. </p>'
        ),
        'ציון פסיכומטרי/ גליון ציונים/ מבחן יעל':(
        '<p style="text-align:left";>הציונים נשלחים למייל איתם נרשמתם לבחינה. במידה ואינכם מוצאים את המייל עם קובץ הציונים ניתן להורידם מהאתר של מאל"ו בקישור הבא (<a href="https://www.nite.org.il/psychometric-entrance-test/scores/">קישור) </p>'
        '<p style="text-align:left";> במידה ואינכם סטודנטים שנה א סמסטר א נבקש גם גיליון ציונים מהאוניברסיטה עבור לימודים אלו.</p>'
        ),
        'שומת מס לשנה הנוכחית': (
        '<p style="text-align:left";>שומת מס הוא מסמך הניתן בסוף שנת מס ממשרד האוצר, הוא מסכם את כלל הרווחים, החובות והמיסים וניתן לאחר שהוגש דוח מס. ניתן להיעזר בסרטון הבא כדי להוציא אותו מהאתר (<a href="https://www.youtube.com/watch?v=4vHIyiLUtnc&t=2s">קישור) </p>'
        '<p style="text-align:left";>לחילופין ניתן לפנות למשרד האוצר שישלחו את המסמך בדואר. </p>'
        ),
        'אסמכתא לניתוק קשר מהורה': (
        '<p style="text-align:left";> מסמך רשמי בנוכחות עורך דין בו מצהירים כי אין קשר רגשי, חברתי או כלכלי עם ההורה ממנו מנותק הקשר.</p>'
        '<p style="text-align:left";>לעיתים גם נקרא ״תצהיר אמת״ </p>'
        ),
        'מעמד לא עובד': (
        '<p style="text-align:left";> זה מסמך רשמי מביטוח לאומי שמצהיר כי הוריך כרגע לא מועסק בשום עבודה וכאינו מוגדר כעובד במדינת ישראל. </p>'
        '<p style="text-align:left";>ניתן להוציא את האישור בקישור הבא: (<a href="https://www.btl.gov.il/%D7%98%D7%A4%D7%A1%D7%99%D7%9D%20%D7%95%D7%90%D7%99%D7%A9%D7%95%D7%A8%D7%99%D7%9D/%D7%90%D7%99%D7%A9%D7%95%D7%A8%D7%99%D7%9D/Insurance_authorizations/Pages/%D7%90%D7%99%D7%A9%D7%95%D7%A8%20%D7%A2%D7%9C%20%D7%9E%D7%A2%D7%9E%D7%93%20%D7%9C%D7%90%20%D7%A2%D7%95%D7%91%D7%93.aspx">קישור) </p>'
        '<p style="text-align:left";>לחילופין, ניתן להתקשר אל הביטוח הלאומי במספר *6050 או לפנות לאחת מעמדות השירות המפורזות ברחבי הארץ </p>'
        '<p style="text-align:left";> שימו לב במקרים הבאים ההורה שלכם לא יהיה מוגדר במעמד לא עובד:גמלאי/פנסיונר, מקבל דמי אבטלה, תאונת עבודה, חל״ת.</p>'
        '<p style="text-align:left";>ניתן לברר את המעמד בביטוח לאומי באתר תחת נתוני המבוטח. </p>'
        )
        },
        'פפר': {
        'פירוט אשראי' : (
        '<p style="text-align: left;">זה מסמך שמפרט את כל הפעולות שנעשו באשראי שבבעלותך ומראים לנו מה ההעברות שביצעת</p>'
        '<p style="text-align: left;">אנחנו דורשים פירוט של השלושה חודשים האחרונים.</p>'
        '<p style="text-align: left;">ניתן להשיג אותו דרך אתר חברת האשראי בד"כ או מהבנק אליו משויך הכרטיס.</p>'
        '<p style="text-align: left;">יש לשים לב שבדרך כלל המסמך מגיע כל חודש בנפרד, לכן לאחר שהשגת את שלושת החודשים האחרונים ניתן לאגד אותם לקובץ אחוד באתר הבא (<a href="https://gbr01.safelinks.protection.outlook.com/?url=https%3A%2F%2Fwww.adobe.com%2Facrobat%2Fonline%2Fmerge-pdf.html&amp;data=05%7C02%7Crecruitment%40moshalprogram.org%7C74175f9d59214f8b00a908de04b4aa10%7Cd01f81685d374261bf620ef33b01fe74%7C0%7C0%7C638953371177834321%7CUnknown%7CTWFpbGZsb3d8eyJFbXB0eU1hcGkiOnRydWUsIlYiOiIwLjAuMDAwMCIsIlAiOiJXaW4zMiIsIkFOIjoiTWFpbCIsIldUIjoyfQ%3D%3D%7C0%7C%7C%7C&amp;sdata=wkq2UmCfPx1TjyyRESi8jZMRnCr1B9H9EHleCO0hS1c%3D&amp;reserved=0">קישור</a>).</p>'
        '<p style="text-align: left;">לאחר שאיגדת אותם יש להעלות אותם באתר תחת "פירוט אשראי - מועמד".</p>'
        ),
        'פירוט עו״ש' : (
        '<p style="text-align: left;">זה מסמך שמפרט את כלל הפעולות שעשית בחשבון העובר ושב שלך בשלושה חודשים האחרונים.</p>'
        '<p style="text-align: left;">מצרפת לך סרטון איך להשיג את המסמך הרלוונטי (<a href="https://www.youtube.com/watch?v=wax96UpAP7M&list=PLggDhgzBukWuLKfhvc9vncn-0Z4HJEvVA&index=2">קישור</a>) מהבנק. יש לשים לב כי בחלק מן הבנקים לא ניתן לעשות זאת באפליקציה בנייד ולכן צריך מחשב.</p>'
        '<p style="text-align: left;">אם אין באפשרותך להשיג מחשב צריך לפנות לבנק והוא יוכל להדפיס לך את המסמכים. לאחר סריקה באופן קריא ניתן להעלות אותם לאתר.</p>'
        ),
        'דוח ריכוז יתרות': (
        '<p style="text-align:left;">דוח ריכוז יתרות הוא מסמך הבנקאי המשערך את כלל הנכסים בבעלותך. </p>'
        '<p style="text-align:left;">.בתוכנית אנחנו מבקשים מסמך ריכוז יתרות <strong>עדכני לחודש זה ולא דוח ריכוז יתרות לסוף השנה</strong> </p>'
        '<p style="text-align:left;">.ניתן להיעזר בסרטון הבא: (<a href="https://www.youtube.com/watch?v=29SULg-_00Y&list=PLggDhgzBukWuLKfhvc9vncn-0Z4HJEvVA">קישור)</a> </p>'
        '<p style="text-align:left;"> יש לשים לב כי לא ניתן להוציא מסמך זה דרך האפליקציה לכן יש להכנס לאתר האינטרנטי דרך מחשב או לחילופין לשוחח עם בנקאי</p>'
        ),
        'תשלום קצבה/ אסמכתא לקצבה': (
        '<p style="text-align: left;">אם הינך או אחד מההורים שלך מקבלים קצבה, המלגה תבקש את פירוט התשלומים לכל הפחות בשלושה חודשים האחרונים.</p>'
        '<p style = "text-align: left;">במידה והקצבה התקבלה מהביטוח הלאומי, ניתן להיעזר בקישור הבא: (<a href="https://www.btl.gov.il/%D7%98%D7%A4%D7%A1%D7%99%D7%9D%20%D7%95%D7%90%D7%99%D7%A9%D7%95%D7%A8%D7%99%D7%9D/%D7%90%D7%99%D7%A9%D7%95%D7%A8%D7%99%D7%9D/General_Authorizations/Pages/%D7%90%D7%99%D7%A9%D7%95%D7%A8%20%D7%AA%D7%A9%D7%9C%D7%95%D7%9E%D7%99%D7%9D%20%D7%A9%D7%A0%D7%AA%D7%99.aspx">קישור)</p>'
        ),
        'גיליון ציוני בגרות':(
        '<p style = "text-align:left;">ניתן להוריד את גיליון ציוני הבגרות מאתר משרד החינוך בקישור הבא: (<a href= "https://www.gov.il/he/service/production-matriculation-certificate-and-grades">קישור)</p>'
        ),
        'פירוט חובות/הלוואות': (
        '<p style="text-align:left";>מסמך רשמי המפרט על גובה החובות או ההלוואות שנלקחו.</p>'
        '<p style="text-align:left";>נצטרך את גובה החוב או ההלוואה, כמה נותר לפירעון, תאריך התשלום הבא וכדומה..</p>'
        ),
        'מסמך לסילוק משכנתא': (
        '<p style="text-align:left";>מסמך רשמי המפרט אודות תאריך לקיחת המשכנתא, גובהה וכמה נותר לשלם. ניתן לצרף מסמך ממנו נלקחה המשכנתא.</p>'
        ),
        'יתרת פיקדון צבאי':(
        '<p style="text-align:left";>לאחר סיום השירות הצבאי, מתקבל פיקדון בהתאם לסוג השירות הצבאי הנעשה בידי האגף לחיילים משוררים וחיילי מילואים של משרד הביטחון. אנחנו דורשים מסמך המעיד באופן עדכני על היתרה של פיקדון זה. להלן השלבים להנפקת המסמך:</p>'
        '<p style="text-align:left";> 1.נכנסים לאתר של האגף לחיילים משוחררים ומילואים בקישור הבא:  (<a href="https://www.hachvana.mod.gov.il/modseclogin/Dispatcher?TAM_OP=login&ERROR_CODE=0x00000000&ERROR_TEXT=HPDBA0521I%20%20%20Successful%20completion&URL=https%3A%2F%2Fwww.hachvana.mod.gov.il%2FHachvanaOnline%2F&h=www.hachvana.mod.gov.il&AUTHNLEVEL=&PROTOCOL=https">קישור)</p>'
        '<p style="text-align:left";>2. נכנסים לאיזור האישי </p>'
        '<p style="text-align:left";> 3.נכנסים ליתרת פיקדון</p>'
        '<p style="text-align:left";>4. לוחצים על הדפס ושומרים את המסמך בנייד ולאחר מכן מעלים לאתר</p>'
        ),
        'תלוש שכר הורה':(
        '<p style="text-align:left";>בתוכנית נבקש סריקה או מסמך ובו מופיע תלוש השכר של הוריכם נבקש שלושה תלושי שכר, אחד לכל חודש.</p>'
        '<p style="text-align:left";>נבקש שתלושי השכר יהיו לכל היותר 4 חודשים אחורה. </p>'
        ),
        'ציון פסיכומטרי/ גליון ציונים/ מבחן יעל':(
        '<p style="text-align:left";>הציונים נשלחים למייל איתם נרשמתם לבחינה. במידה ואינכם מוצאים את המייל עם קובץ הציונים ניתן להורידם מהאתר של מאל"ו בקישור הבא (<a href="https://www.nite.org.il/psychometric-entrance-test/scores/">קישור) </p>'
        '<p style="text-align:left";> במידה ואינכם סטודנטים שנה א סמסטר א נבקש גם גיליון ציונים מהאוניברסיטה עבור לימודים אלו.</p>'
        ),
        'שומת מס לשנה הנוכחית': (
        '<p style="text-align:left";>שומת מס הוא מסמך הניתן בסוף שנת מס ממשרד האוצר, הוא מסכם את כלל הרווחים, החובות והמיסים וניתן לאחר שהוגש דוח מס. ניתן להיעזר בסרטון הבא כדי להוציא אותו מהאתר (<a href="https://www.youtube.com/watch?v=4vHIyiLUtnc&t=2s">קישור) </p>'
        '<p style="text-align:left";>לחילופין ניתן לפנות למשרד האוצר שישלחו את המסמך בדואר. </p>'
        ),
        'אסמכתא לניתוק קשר מהורה': (
        '<p style="text-align:left";> מסמך רשמי בנוכחות עורך דין בו מצהירים כי אין קשר רגשי, חברתי או כלכלי עם ההורה ממנו מנותק הקשר.</p>'
        '<p style="text-align:left";>לעיתים גם נקרא ״תצהיר אמת״ </p>'
        ),
        'מעמד לא עובד': (
        '<p style="text-align:left";> זה מסמך רשמי מביטוח לאומי שמצהיר כי הוריך כרגע לא מועסק בשום עבודה וכאינו מוגדר כעובד במדינת ישראל. </p>'
        '<p style="text-align:left";>ניתן להוציא את האישור בקישור הבא: (<a href="https://www.btl.gov.il/%D7%98%D7%A4%D7%A1%D7%99%D7%9D%20%D7%95%D7%90%D7%99%D7%A9%D7%95%D7%A8%D7%99%D7%9D/%D7%90%D7%99%D7%A9%D7%95%D7%A8%D7%99%D7%9D/Insurance_authorizations/Pages/%D7%90%D7%99%D7%A9%D7%95%D7%A8%20%D7%A2%D7%9C%20%D7%9E%D7%A2%D7%9E%D7%93%20%D7%9C%D7%90%20%D7%A2%D7%95%D7%91%D7%93.aspx">קישור) </p>'
        '<p style="text-align:left";>לחילופין, ניתן להתקשר אל הביטוח הלאומי במספר *6050 או לפנות לאחת מעמדות השירות המפורזות ברחבי הארץ </p>'
        '<p style="text-align:left";> שימו לב במקרים הבאים ההורה שלכם לא יהיה מוגדר במעמד לא עובד:גמלאי/פנסיונר, מקבל דמי אבטלה, תאונת עבודה, חל״ת.</p>'
        '<p style="text-align:left";>ניתן לברר את המעמד בביטוח לאומי באתר תחת נתוני המבוטח. </p>'
        )
        },
        'לא בטוח/ה': {
        'פירוט אשראי' : (
        '<p style="text-align: left;">זה מסמך שמפרט את כל הפעולות שנעשו באשראי שבבעלותך ומראים לנו מה ההעברות שביצעת</p>'
        '<p style="text-align: left;">אנחנו דורשים פירוט של השלושה חודשים האחרונים.</p>'
        '<p style="text-align: left;">ניתן להשיג אותו דרך אתר חברת האשראי בד"כ או מהבנק אליו משויך הכרטיס.</p>'
        '<p style="text-align: left;">יש לשים לב שבדרך כלל המסמך מגיע כל חודש בנפרד, לכן לאחר שהשגת את שלושת החודשים האחרונים ניתן לאגד אותם לקובץ אחוד באתר הבא (<a href="https://gbr01.safelinks.protection.outlook.com/?url=https%3A%2F%2Fwww.adobe.com%2Facrobat%2Fonline%2Fmerge-pdf.html&amp;data=05%7C02%7Crecruitment%40moshalprogram.org%7C74175f9d59214f8b00a908de04b4aa10%7Cd01f81685d374261bf620ef33b01fe74%7C0%7C0%7C638953371177834321%7CUnknown%7CTWFpbGZsb3d8eyJFbXB0eU1hcGkiOnRydWUsIlYiOiIwLjAuMDAwMCIsIlAiOiJXaW4zMiIsIkFOIjoiTWFpbCIsIldUIjoyfQ%3D%3D%7C0%7C%7C%7C&amp;sdata=wkq2UmCfPx1TjyyRESi8jZMRnCr1B9H9EHleCO0hS1c%3D&amp;reserved=0">קישור</a>).</p>'
        '<p style="text-align: left;">לאחר שאיגדת אותם יש להעלות אותם באתר תחת "פירוט אשראי - מועמד".</p>'
        ),
        'פירוט עו״ש' : (
        '<p style="text-align: left;">זה מסמך שמפרט את כלל הפעולות שעשית בחשבון העובר ושב שלך בשלושה חודשים האחרונים.</p>'
        '<p style="text-align: left;">אם אין באפשרותך להשיג מחשב צריך לפנות לבנק והוא יוכל להדפיס לך את המסמכים. לאחר סריקה באופן קריא ניתן להעלות אותם לאתר.</p>'
        ),
        'דוח ריכוז יתרות': (
        '<p style="text-align:left;">דוח ריכוז יתרות הוא מסמך הבנקאי המשערך את כלל הנכסים בבעלותך. </p>'
        '<p style="text-align:left;">.בתוכנית אנחנו מבקשים מסמך ריכוז יתרות <strong>עדכני לחודש זה ולא דוח ריכוז יתרות לסוף השנה</strong> </p>'
        '<p style="text-align:left;"> יש לשים לב כי לא ניתן להוציא מסמך זה דרך האפליקציה לכן יש להכנס לאתר האינטרנטי דרך מחשב או לחילופין לשוחח עם בנקאי</p>'
        ),
        'תשלום קצבה/ אסמכתא לקצבה': (
        '<p style="text-align: left;">אם הינך או אחד מההורים שלך מקבלים קצבה, המלגה תבקש את פירוט התשלומים לכל הפחות בשלושה חודשים האחרונים.</p>'
        '<p style = "text-align: left;">במידה והקצבה התקבלה מהביטוח הלאומי, ניתן להיעזר בקישור הבא: (<a href="https://www.btl.gov.il/%D7%98%D7%A4%D7%A1%D7%99%D7%9D%20%D7%95%D7%90%D7%99%D7%A9%D7%95%D7%A8%D7%99%D7%9D/%D7%90%D7%99%D7%A9%D7%95%D7%A8%D7%99%D7%9D/General_Authorizations/Pages/%D7%90%D7%99%D7%A9%D7%95%D7%A8%20%D7%AA%D7%A9%D7%9C%D7%95%D7%9E%D7%99%D7%9D%20%D7%A9%D7%A0%D7%AA%D7%99.aspx">קישור)</p>'
        ),
        'גיליון ציוני בגרות':(
        '<p style = "text-align:left;">ניתן להוריד את גיליון ציוני הבגרות מאתר משרד החינוך בקישור הבא: (<a href= "https://www.gov.il/he/service/production-matriculation-certificate-and-grades">קישור)</p>'
        ),
        'פירוט חובות/הלוואות': (
        '<p style="text-align:left";>מסמך רשמי המפרט על גובה החובות או ההלוואות שנלקחו.</p>'
        '<p style="text-align:left";>נצטרך את גובה החוב או ההלוואה, כמה נותר לפירעון, תאריך התשלום הבא וכדומה..</p>'
        ),
        'מסמך לסילוק משכנתא': (
        '<p style="text-align:left";>מסמך רשמי המפרט אודות תאריך לקיחת המשכנתא, גובהה וכמה נותר לשלם. ניתן לצרף מסמך ממנו נלקחה המשכנתא.</p>'
        ),
        'יתרת פיקדון צבאי':(
        '<p style="text-align:left";>לאחר סיום השירות הצבאי, מתקבל פיקדון בהתאם לסוג השירות הצבאי הנעשה בידי האגף לחיילים משוררים וחיילי מילואים של משרד הביטחון. אנחנו דורשים מסמך המעיד באופן עדכני על היתרה של פיקדון זה. להלן השלבים להנפקת המסמך:</p>'
        '<p style="text-align:left";> 1.נכנסים לאתר של האגף לחיילים משוחררים ומילואים בקישור הבא:  (<a href="https://www.hachvana.mod.gov.il/modseclogin/Dispatcher?TAM_OP=login&ERROR_CODE=0x00000000&ERROR_TEXT=HPDBA0521I%20%20%20Successful%20completion&URL=https%3A%2F%2Fwww.hachvana.mod.gov.il%2FHachvanaOnline%2F&h=www.hachvana.mod.gov.il&AUTHNLEVEL=&PROTOCOL=https">קישור)</p>'
        '<p style="text-align:left";>2. נכנסים לאיזור האישי </p>'
        '<p style="text-align:left";> 3.נכנסים ליתרת פיקדון</p>'
        '<p style="text-align:left";>4. לוחצים על הדפס ושומרים את המסמך בנייד ולאחר מכן מעלים לאתר</p>'
        ),
        'תלוש שכר הורה':(
        '<p style="text-align:left";>בתוכנית נבקש סריקה או מסמך ובו מופיע תלוש השכר של הוריכם נבקש שלושה תלושי שכר, אחד לכל חודש.</p>'
        '<p style="text-align:left";>נבקש שתלושי השכר יהיו לכל היותר 4 חודשים אחורה. </p>'
        ),
        'ציון פסיכומטרי/ גליון ציונים/ מבחן יעל':(
        '<p style="text-align:left";>הציונים נשלחים למייל איתם נרשמתם לבחינה. במידה ואינכם מוצאים את המייל עם קובץ הציונים ניתן להורידם מהאתר של מאל"ו בקישור הבא (<a href="https://www.nite.org.il/psychometric-entrance-test/scores/">קישור) </p>'
        '<p style="text-align:left";> במידה ואינכם סטודנטים שנה א סמסטר א נבקש גם גיליון ציונים מהאוניברסיטה עבור לימודים אלו.</p>'
        ),
        'שומת מס לשנה הנוכחית': (
        '<p style="text-align:left";>שומת מס הוא מסמך הניתן בסוף שנת מס ממשרד האוצר, הוא מסכם את כלל הרווחים, החובות והמיסים וניתן לאחר שהוגש דוח מס. ניתן להיעזר בסרטון הבא כדי להוציא אותו מהאתר (<a href="https://www.youtube.com/watch?v=4vHIyiLUtnc&t=2s">קישור) </p>'
        '<p style="text-align:left";>לחילופין ניתן לפנות למשרד האוצר שישלחו את המסמך בדואר. </p>'
        ),
        'אסמכתא לניתוק קשר מהורה': (
        '<p style="text-align:left";> מסמך רשמי בנוכחות עורך דין בו מצהירים כי אין קשר רגשי, חברתי או כלכלי עם ההורה ממנו מנותק הקשר.</p>'
        '<p style="text-align:left";>לעיתים גם נקרא ״תצהיר אמת״ </p>'
        ),
        'מעמד לא עובד': (
        '<p style="text-align:left";> זה מסמך רשמי מביטוח לאומי שמצהיר כי הוריך כרגע לא מועסק בשום עבודה וכאינו מוגדר כעובד במדינת ישראל. </p>'
        '<p style="text-align:left";>ניתן להוציא את האישור בקישור הבא: (<a href="https://www.btl.gov.il/%D7%98%D7%A4%D7%A1%D7%99%D7%9D%20%D7%95%D7%90%D7%99%D7%A9%D7%95%D7%A8%D7%99%D7%9D/%D7%90%D7%99%D7%A9%D7%95%D7%A8%D7%99%D7%9D/Insurance_authorizations/Pages/%D7%90%D7%99%D7%A9%D7%95%D7%A8%20%D7%A2%D7%9C%20%D7%9E%D7%A2%D7%9E%D7%93%20%D7%9C%D7%90%20%D7%A2%D7%95%D7%91%D7%93.aspx">קישור) </p>'
        '<p style="text-align:left";>לחילופין, ניתן להתקשר אל הביטוח הלאומי במספר *6050 או לפנות לאחת מעמדות השירות המפורזות ברחבי הארץ </p>'
        '<p style="text-align:left";> שימו לב במקרים הבאים ההורה שלכם לא יהיה מוגדר במעמד לא עובד:גמלאי/פנסיונר, מקבל דמי אבטלה, תאונת עבודה, חל״ת.</p>'
        '<p style="text-align:left";>ניתן לברר את המעמד בביטוח לאומי באתר תחת נתוני המבוטח. </p>'
        )
        }
            }

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        #submit button
        try:
            self.ui.pushButton.clicked.connect(self.submit)
            self.statusBar().showMessage("האפליקציה מוכנה. אנא בחר/י בנק ומסמכים, ולחץ/י על 'שלח'.")
        except AttributeError as e:
            QMessageBox.critical(self, "שגיאת ממשק", f"שגיאה בחיבור כפתור: {e}. ודא/י ששם הכפתור ב-Qt Designer הוא 'pushButton'.")
            print(f"Error connecting button: {e}")

        #copy button
        try:
            self.ui.pushButton_2.clicked.connect(self.copy)
            self.statusBar().showMessage('העתק/י טקסט לשליחה במייל')
        except AttributeError as e:
            QMessageBox.critical(self, "שגיאת ממשק", f"שגיאה בחיבור כפתור: {e}. ודא/י ששם הכפתור ב-Qt Designer הוא 'pushButton'.")
            print(f"Error connecting button: {e}")


    def submit(self):
        try:
            a_name = self.ui.lineEdit.text().strip()
            a_bank = self.ui.comboBox.currentText().strip()
            a_docs_objects = self.ui.listWidget.selectedItems()
        except AttributeError as e:
            QMessageBox.critical(self, "שגיאת ממשק", f"חסר רכיב: {e}. ודא/י את שמות הרכיבים במעצב ה-Qt.")
            return

        if not a_bank or a_bank not in self.all_data:
            QMessageBox.warning(self, "בחר בנק", "אנא בחר/י בנק תקין מרשימת הבחירה.")
            return

        if not a_docs_objects:
            QMessageBox.warning(self, "בחר מסמכים", "אנא בחר/י לפחות מסמך אחד מהרשימה.")
            return
        a_docs_texts = [item.text() for item in a_docs_objects]
        bank_library = self.all_data[a_bank]
        full_explanation_parts = []

        for doc_name in a_docs_texts:
            explanation = bank_library.get(doc_name, f"שגיאה: לא נמצא הסבר למסמך '{doc_name}' עבור בנק '{a_bank}'.")
            formatted_explanation = explanation.replace('\n', '<br>')
            full_explanation_parts.append(
                f"<div style='margin-bottom: 20px; border-right: 4px solid #005A9C; padding-right: 10px; direction: rtl;'>"
                f"<p><b>{doc_name}<\b></p>"
                f"<p style='margin-top: 5px; line-height: 1.5;'>{formatted_explanation}</p>"
                f"</div>"
            )
        display_name = a_name if a_name else ""
        documents_html = "\n".join(full_explanation_parts)
        final_html_output = (
            f"<div style='direction: rtl; text-align: left; font-family: arial, sans-serif;'>"
            f"<p> שלום {display_name},<p>"
            f"<p>להלן פירוט אודות המסמכים החסרים להמשך הגשת מועמדותך:</p>"
            f"{documents_html}"
            f"<p>בברכה,</p>"
            f"<p><b>תוכנית מושל<\b> </p>"
            f"</div>"
        )


        try:
            self.ui.textEdit.setHtml(final_html_output)
            self.statusBar().showMessage(f"נוצר פירוט עבור {len(a_docs_texts)} מסמכים.", 5000)
        except AttributeError:
            QMessageBox.critical(self, "שגיאת ממשק", "רכיב הפלט (textEdit) לא נמצא. ודא/י ששמו הוא 'textEdit'.")

    def copy(self):
        clipboard = QApplication.clipboard()
        html_to_copy = self.ui.textEdit.toHtml()
        data = QMimeData()
        data.setHtml(html_to_copy)
        clipboard.setMimeData(data)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
