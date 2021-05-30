
import streamlit as st
from PIL import Image

st.sidebar.write('頭蓋骨のデッサンindex')

st.title('頭蓋骨のデッサン')
if st.sidebar.checkbox('頭蓋骨を描く―動画'):
    video_file = open('zugai.MP4', 'rb')
    video_bytes = video_file.read()
    st.video(video_bytes)

if st.sidebar.checkbox('いろいろな角度の頭蓋骨'):
    image = Image.open('z1.jpg')
    st.image(image, caption='いろいろな角度の頭蓋骨', use_column_width=True)
    st.write('''描く前に立体的な頭蓋骨のイメージをイメージしましょう。
    写すことよりも構造的な形を理解することがもっとも大切です。''')

if st.sidebar.checkbox('頭蓋骨の描き方'):
    image = Image.open('z2.jpg')
    st.image(image, caption='頭蓋骨の描き方', use_column_width=True)
    st.write('''色、形等バランスを見ながら描き進めていきましょう、
    途中で形がおかしいなと感じたら積極的に直しながら描いていきましょう''')

if st.sidebar.checkbox('頭蓋骨演習1'):
    image = Image.open('z3.jpg')
    st.image(image, caption='頭蓋骨演習1', use_column_width=True)
    st.write('''頭蓋骨演習1、
画像をダウンロードしてプリント
アウトして上から描いてみよう''')

if st.sidebar.checkbox('頭蓋骨演習2'):
    image = Image.open('z4.jpg')
    st.image(image, caption='頭蓋骨演習2', use_column_width=True)
    st.write('''頭蓋骨演習2、
画像をダウンロードしてプリント
アウトして上から描いてみよう''')