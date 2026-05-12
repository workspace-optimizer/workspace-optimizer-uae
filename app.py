import streamlit as st
import time

st.set_page_config(page_title="WorkSpace Optimizer AI", page_icon="🏢", layout="wide")

st.title("🏢 محول المكاتب المنزلية الذكي")
st.markdown("---")

# تقسيم الصفحة لعمودين لشكل أكثر احترافية
col1, col2 = st.columns([1, 1])

with col1:
    st.header("1️⃣ المدخلات")
    uploaded_file = st.file_uploader("ارفع صورة الزاوية", type=["jpg", "png"])
    budget = st.slider("ميزانيتك للأثاث ($)", 100, 2000, 500)
    style = st.selectbox("نمط الديكور المفضل", ["Modern - عصري", "Minimalist - بسيط", "Classic - كلاسيك"])

with col2:
    st.header("2️⃣ المعاينة")
    if uploaded_file:
        st.image(uploaded_file, caption="مساحتك الحالية", use_container_width=True)
    else:
        st.info("في انتظار رفع الصورة...")

st.markdown("---")

if st.button("🚀 توليد خطة التصميم الاحترافية"):
    if uploaded_file:
        # محاكاة عملية التحليل بالذكاء الاصطناعي
        with st.status("جاري فحص أبعاد الغرفة وتوزيع الإضاءة...", expanded=True) as status:
            st.write("🔍 جاري التعرف على العناصر المعمارية...")
            time.sleep(2)
            st.write("💡 جاري حساب زوايا الضوء الطبيعي...")
            time.sleep(2)
            st.write("🛒 جاري مطابقة الميزانية مع المنتجات المتاحة...")
            time.sleep(1)
            status.update(label="تم التحليل بنجاح!", state="complete", expanded=False)

        # عرض النتائج بشكل احترافي
        st.success("✅ التقرير الهندسي جاهز")
        
        tab1, tab2, tab3 = st.tabs(["📋 خطة التنفيذ", "🛒 قائمة المشتريات", "🎨 الألوان والإضاءة"])
        
        with tab1:
            st.write("### خطوات تحويل المكان:")
            st.write("1. قم بإخلاء الزاوية اليمنى تماماً.")
            st.write(f"2. ضع المكتب بزاوية 90 درجة مع النافذة لتجنب انعكاس الضوء (حسب نمط {style}).")
            st.write("3. استخدم رفوفاً جدارية لاستغلال المساحة الرأسية.")
            
        with tab2:
            st.write("### المشتريات المقترحة (ضمن ميزانية {} $):".format(budget))
            # إنشاء جدول مشتريات
            st.table({
                "المنتج": ["مكتب عمل", "كرسي مريح", "مصباح مكتبي", "منظم أسلاك"],
                "المصدر": ["IKEA", "Amazon", "Local Store", "IKEA"],
                "السعر التقريبي": [f"{budget*0.4}$", f"{budget*0.3}$", f"{budget*0.1}$", "15$"]
            })
            
        with tab3:
            st.write("### توصيات الألوان:")
            st.color_picker("لون الحائط المقترح", "#F0F2F6")
            st.write("أكواد الإضاءة: 4000K (Natural White) للتركيز العالي.")
            
    else:
        st.error("من فضلك ارفع صورة الزاوية أولاً لبدء التحليل.")
    