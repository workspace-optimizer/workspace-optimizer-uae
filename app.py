import streamlit as st
from fpdf import FPDF
import random

# إعداد واجهة الموقع بروح احترافية
st.set_page_config(page_title="Workspace Optimizer AI - Gulf Edition", page_icon="🏗️")

st.title("🏗️ مهندس المساحات الذكي (نسخة الخليج)")
st.subheader("حول زاوية منزلك إلى مكتب تنفيذي احترافي في دقيقة")

# مدخلات المستخدم
uploaded_file = st.file_uploader("ارفع صورة الزاوية أو الغرفة", type=["jpg", "jpeg", "png"])
budget = st.select_slider("حدد ميزانيتك التقريبية (بالدرهم الإماراتي/الريال السعودي)", 
                         options=["اقتصادية", "متوسطة", "فاخرة"])
style = st.selectbox("اختر نمط التصميم", ["عصري (Modern)", "كلاسيكي (Classic)", "صناعي (Industrial)"])

if uploaded_file and st.button("🚀 توليد التقرير الهندسي والمخطط"):
    with st.spinner('جاري تحليل المساحة هندسياً وتوزيع الإضاءة...'):
        
        # محاكاة ذكاء اصطناعي للتحليل (سيتم ربطه بـ API لاحقاً)
        report_id = random.randint(1000, 9999)
        
        # محتوى التقرير (هندسة اقتصادية)
        analysis_text = f"""
        REPORT ID: {report_id}
        TARGET MARKET: GULF REGION (UAE/KSA)
        
        1. التحليل الهندسي للمساحة:
        - توزيع الإضاءة: يوصى بوضع المكتب بزاوية 90 درجة من النافذة لتجنب الوهج.
        - بيئة العمل: المقاس المثالي للمكتب في هذه المساحة هو 120x60 سم.
        
        2. قائمة التجهيزات المقترحة (متاجر الخليج):
        - المكتب: ايكيا (تارفا) أو أبيات (سلسلة أوفيس).
        - الكرسي: ماركة هيرمان ميلر (للفاخرة) أو هوم بوكس (للاقتصادية).
        - الإضاءة: مصباح طاولة ذكي من أمازون الإمارات.
        
        3. نصيحة الإنتاجية:
        - عزل الصوت باستخدام لوحات امتصاص في الزاوية لزيادة التركيز في اجتماعات Zoom.
        """
        
        st.success("تم الانتهاء من التحليل!")
        st.info(analysis_text)
        
        # إنشاء ملف PDF احترافي
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.cell(200, 10, txt="Professional Workspace Analysis - Gulf Edition", ln=True, align='C')
        pdf.ln(10)
        pdf.multi_cell(0, 10, txt=analysis_text)
        
        pdf_output = f"Report_{report_id}.pdf"
        pdf.output(pdf_output)
        
        with open(pdf_output, "rb") as file:
            st.download_button(
                label="📥 تحميل التقرير الهندسي (PDF)",
                data=file,
                file_name=f"Workspace_Plan_{report_id}.pdf",
                mime="application/pdf"
            )
            st.balloons()

st.markdown("---")
st.caption("هذا النظام مدعوم بالذكاء الاصطناعي لخدمة المبدعين في الخليج العربي.")
