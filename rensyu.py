import streamlit as st
from PIL import Image

image = Image.open('logo.png')
st.image(image, use_column_width=True)
st.sidebar.title('頭蓋骨のデッサンindex')
st.title('頭蓋骨のデッサン')

link = '(https://x6ud.github.io/)'
st.markdown(link, unsafe_allow_html=True)

tit = ['いろいろな角度の頭蓋骨',
    '頭蓋骨の描き方',
    '頭蓋骨の構造１',
    '頭蓋骨の構造2',
    '頭蓋骨演習1',
    '頭蓋骨演習2']

gazo =['z1.jpg',
    'z2.jpg',
    'z5.jpg',
    'z6.jpg',
    'z3.jpg',
    'z4.jpg']

kaisetu =['''描く前に立体的な頭蓋骨のイメージをイメージしましょう。
写すことよりも構造的な形を理解することがもっとも大切です。''',
'''色、形等バランスを見ながら描き進めていきましょう、
途中で形がおかしいなと感じたら積極的に直しながら描いていきましょう''',
'''まずはシンプルなベースとなる形を観察しましょう頭蓋骨の場合は
卵の形と三角形の立体(正四面体)の組み合わせがベースの形になります。''',
'''シンプルなベースの形を削ったり部品を付け足すイメージで細部を造っていきます。''',
'''頭蓋骨演習1、
画像をダウンロードしてプリント
アウトして上から描いてみよう''',
'''頭蓋骨演習2、
画像をダウンロードしてプリント
アウトして上から描いてみよう''']

if st.sidebar.checkbox('頭蓋骨のデッサン(動画）'):
    video_file = open('zugai.MP4', 'rb')
    video_bytes = video_file.read()
    st.video(video_bytes)

def gazou_kai(tit,gazo,kaisetu):
    if st.sidebar.checkbox(tit):
        image = Image.open(gazo)
        st.image(image, caption= tit, use_column_width=True)
        st.write(kaisetu)
        return
for i in range(6):
    gazou_kai(tit[i],gazo[i],kaisetu[i])

