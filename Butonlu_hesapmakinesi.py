import streamlit as st

st.set_page_config(page_title = "Hesap makinesi!",
                   page_icon = "🧮",
                   layout = "centered",
                   initial_sidebar_state = "expanded",
                   menu_items = {
                   "Get help": "https://docs.streamlit.io/",
                   "Report a bug" : "https://github.com/streamlit/streamlit/issues",
                   "About" :"Bu bir basit butonlu hesap makinesidir!"
                   })
st.title("🧮 Hesap makinesi!")

# değişkenleri tutma

if "sayi1" not in st.session_state:
    st.session_state.sayi1 = ""
if "sayi2" not in st.session_state:
    st.session_state.sayi2 = ""
if "aktifsayi" not in st.session_state:
    st.session_state.aktifsayi = "sayi1"
if "sonuc" not in st.session_state:
    st.session_state.sonuc = None

# işlem seçimi

islem = st.selectbox("yapılacak işlemleri seçiniz",
                     ["Toplama","Çıkarma","Çarpma","Bölme"])
st.write(f"Şu anda girilen : {st.session_state.aktifsayi}")

#Sayıları butonlar ile yazdırma

butonlar = [
    ["7","8","9"],
    ["4","5","6"],
    ["1","2","3"],
    ["0","tekrar başlat","="]
]

for row in butonlar:
    cols = st.columns(3)

    for i, b in enumerate(row):
        if cols[i].button(b, use_container_width=True):
            if b == "tekrar başlat":
                st.session_state.sayi1 = ""
                st.session_state.sayi2 = ""
                st.session_state.sonuc = None
                st.session_state.aktifsayi = "sayi1"
            elif b == "=":
                if st.session_state.sayi1 and st.session_state.sayi2:
                    num1 = float(st.session_state.sayi1)
                    num2 = float(st.session_state.sayi2)
                    if islem == "Toplama":
                        st.session_state.sonuc = num1 + num2
                    elif islem == "Çıkarma":
                        st.session_state.sonuc = num1 - num2
                    elif islem == "Çarpma":
                        st.session_state.sonuc = num1 * num2
                    elif islem == "Bölme":
                        st.session_state.sonuc = num1 / num2 if num2 != 0 else "Hata 0 a bölünemez!"
                    else:
                        st.warning("lütfen sayı giriniz!")
            else:
                 if  st.session_state.aktifsayi == "sayi1":
                     st.session_state.sayi1 += b
                 else:
                     st.session_state.sayi2 += b

col1, col2 = st.columns(2)
col1.text_input("sayi1",st.session_state.sayi1)
col2.text_input("sayi2",st.session_state.sayi2)

#2.sayıyı belirleme

if st.button("2.Sayıya geç"):
    st.session_state.aktifsayi = "sayi2"

#Sonuçları gösterme

if st.session_state.sonuc is not None:
    st.success(f"sonuc: {st.session_state.sonuc}")
    st.balloons()
st.write("This calculator made by said basbelen")
